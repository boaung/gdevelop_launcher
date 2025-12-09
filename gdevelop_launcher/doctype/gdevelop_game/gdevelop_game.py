# gdevelop_launcher/gdevelop_launcher/doctype/gdevelop_game/gdevelop_game.py
if os.path.exists(candidate):
file_path = candidate


if not file_path or not os.path.exists(file_path):
doc.db_set('status', 'Error')
frappe.msgprint('Could not locate ZIP file: ' + str(doc.zip_file))
return


# Extract safely
with zipfile.ZipFile(file_path, 'r') as z:
for member in z.namelist():
# Normalize path to avoid absolute or .. entries
member_clean = member.replace('\\', '/').lstrip('/')
if '..' in member_clean.split('/'):
# skip suspicious paths
continue
# write file
dest_path = os.path.join(target_dir, *member_clean.split('/'))
dest_dir = os.path.dirname(dest_path)
os.makedirs(dest_dir, exist_ok=True)
if member_clean.endswith('/'):
continue
with z.open(member) as source, open(dest_path, 'wb') as target_file:
shutil.copyfileobj(source, target_file)


# locate index.html (case-insensitive)
index_path = None
for root, dirs, files in os.walk(target_dir):
for f in files:
if f.lower() == 'index.html':
rel = os.path.relpath(os.path.join(root, f), frappe.get_site_path('public'))
index_path = '/'+rel.replace('\\','/')
break
if index_path:
break


if not index_path:
doc.db_set('status', 'Error')
frappe.msgprint('No index.html found inside ZIP. Extraction aborted.')
return


# success
doc.db_set('index_url', index_path)
doc.db_set('status', 'Published')
frappe.msgprint('Game deployed to: ' + index_path)


except Exception as e:
frappe.log_error(message=frappe.get_traceback(), title='GDevelop extraction error')
doc.db_set('status', 'Error')
frappe.msgprint('Error extracting ZIP: ' + frappe.utils.cstr(e))




def on_trash_delete_files(doc, method=None):
"""When a GDevelop Game is deleted, remove its public files."""
try:
slug = frappe.utils.cstr(doc.slug)
site_games = get_public_base()
target_dir = os.path.join(site_games, slug)
if os.path.exists(target_dir):
shutil.rmtree(target_dir)
except Exception:
frappe.log_error(frappe.get_traceback(), 'Error deleting game files')
