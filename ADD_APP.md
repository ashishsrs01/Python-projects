# How to add a new app

Follow these 3 steps every time you build something new.

## 1. Create a folder

Example: `My New App/`

Put your Python file inside (optional for GitHub visitors) and an **`index.html`** web demo so people can try it in the browser without installing Python.

## 2. Add a link in `apps.json`

Open `apps.json` at the repo root and copy this block (change the values):

```json
{
  "id": "my-new-app",
  "name": "My New App",
  "folder": "My New App",
  "icon": "🚀",
  "color": "cyan",
  "tags": ["web", "fun"],
  "description": "One sentence about what it does."
}
```

**`color` options:** `cyan`, `violet`, `emerald`, `amber`, `rose`, `blue`

The hub page loads this file automatically — you do not need to edit `index.html`.

## 3. Add a back button on your app page

At the top of your `index.html`:

```html
<link rel="stylesheet" href="../shared/app.css" />
...
<a class="back-link" href="../index.html">← Back to Hub</a>
```

(Use `../../` if your app is in a subfolder.)

## Folder layout

```
Python-projects/
  index.html          ← main hub (do not duplicate cards here)
  apps.json           ← list of all apps
  shared/             ← hub + back-button styles
  Calculator/
    Calculator.py
    index.html
  Your New App/
    your_script.py
    index.html
```

## GitHub Pages

After you push to GitHub, enable **Settings → Pages → Deploy from branch → main → /**.

Your site will be: `https://YOUR_USERNAME.github.io/Python-projects/`
