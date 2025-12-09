# GDevelop Launcher for Frappe


This Frappe app allows uploading **GDevelop exported HTML5 games** (ZIP), auto‑extracts them into `public/games/<slug>/`, and auto‑creates a playable webpage.


## ✨ Features
- Upload GDevelop ZIP
- Auto-extract into public folder
- Auto-detect `index.html`
- Auto-create `/games/<slug>` webpage
- Game list page `/games`
- REST API endpoint: `/api/method/gdevelop_launcher.api.list_games`


## 🚀 Installation (for production or development)


### 1. Install app via bench


```
bench get-app https://github.com/<your-github>/gdevelop_launcher.git
bench --site site1.local install-app gdevelop_launcher
```


### 2. Create a game
Go to Desk → GDevelop Game → New
- Enter Title
- Attach GDevelop ZIP
- Save → auto‑deploys the game


### 3. Visit game list:
```
/games
```


### 4. Visit auto‑generated game page:
```
/games/<slug>
```


## 📁 Folder Structure
(Already included in repo)


## 📝 License
MIT
