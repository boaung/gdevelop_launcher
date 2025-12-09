app_name = "gdevelop_launcher"
app_title = "GDevelop Launcher"
app_publisher = "Bo Aung"
app_description = "Host GDevelop HTML5 games in Frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "you@example.com"
app_license = "MIT"


# expose API endpoints
doc_events = {
"GDevelop Game": {
"on_update": "gdevelop_launcher.gdevelop_launcher.doctype.gdevelop_game.gdevelop_game.on_update_extract",
"on_trash": "gdevelop_launcher.gdevelop_launcher.doctype.gdevelop_game.gdevelop_game.on_trash_delete_files",
}
}


# website pages
website_generators = ["GDevelop Game"]


# REST API
override_whitelisted_methods = {
}
