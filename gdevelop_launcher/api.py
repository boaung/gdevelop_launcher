# gdevelop_launcher/gdevelop_launcher/api.py
import frappe


@frappe.whitelist(allow_guest=True)
def list_games():
"""Return list of published games: title, slug, index_url"""
games = frappe.get_all('GDevelop Game', filters={'status':'Published'}, fields=['name','title','slug','index_url'])
return games


@frappe.whitelist()
def publish_game(name):
doc = frappe.get_doc('GDevelop Game', name)
doc.status = 'Published'
doc.save()
return doc
