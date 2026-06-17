# Python Projects

A collection of small Python programs built while learning, plus a **web hub** so anyone can try every app in the browser — no install needed.

**Live demo:** [ashishsrs01.github.io/Python-projects](https://ashishsrs01.github.io/Python-projects/)

---

## What's in this repo

Each project lives in its own folder:

- **Python file** — the original script (Tkinter GUI or CLI)
- **`index.html`** — browser version you can open from the hub

The main page [`index.html`](index.html) lists all apps. The list comes from [`apps.json`](apps.json), so adding a new project is one JSON entry + a new folder.

| Project | What it does | Python | Web demo |
|---------|----------------|--------|----------|
| **Calculator** | Math with +, −, ×, ÷, powers, square root, and history | [`Calculator/Calculator.py`](Calculator/Calculator.py) | [`Calculator/index.html`](Calculator/index.html) |
| **Rock Paper Scissors** | Play vs the computer; score tracking | [`Rock paper scissor/Rock-paper-scissor-game.py`](Rock%20paper%20scissor/Rock-paper-scissor-game.py) | [`Rock paper scissor/index.html`](Rock%20paper%20scissor/index.html) |
| **Dice Roller** | Roll multiple dice with custom sides; shows each roll and the total | [`DIce roller/roller.py`](DIce%20roller/roller.py) | [`DIce roller/index.html`](DIce%20roller/index.html) |
| **Countdown Timer** | Enter seconds and count down to zero | [`Timer/Countdown Timer.py`](Timer/Countdown%20Timer.py) | [`Timer/index.html`](Timer/index.html) |
| **Word Frequency Counter** | Count how often words or letters appear | [`Word frequency counter/counter.py`](Word%20frequency%20counter/counter.py) | [`Word frequency counter/index.html`](Word%20frequency%20counter/index.html) |
| **Text to Speech** | Type text and hear it (browser uses Web Speech API) | [`Text to speech app/t-t-s.py`](Text%20to%20speech%20app/t-t-s.py) | [`Text to speech app/index.html`](Text%20to%20speech%20app/index.html) |
| **BG Remover** | Remove a solid-color background (canvas in browser; AI version in Python) | [`BG remover/python-background-remover.py`](BG%20remover/python-background-remover.py) | [`BG remover/index.html`](BG%20remover/index.html) |

---

## Try it in the browser

**Online:** open the [GitHub Pages site](https://ashishsrs01.github.io/Python-projects/) after Pages is enabled (see below).

**On your PC:**

1. Clone or download this repo.
2. Open `index.html` in a browser (Chrome, Edge, Firefox).
3. Click any project card, or go straight to a folder’s `index.html`.

> For the full hub with search, serve the folder over HTTP (e.g. VS Code Live Server) or use GitHub Pages — `fetch('apps.json')` works best that way. A built-in fallback list still shows all apps if you open `index.html` as a file.

---

## Run the Python versions

From the repo root:

```bash
python "Calculator/Calculator.py"
python "Timer/Countdown Timer.py"
python "Rock paper scissor/Rock-paper-scissor-game.py"
python "DIce roller/roller.py"
python "Word frequency counter/counter.py"
python "Text to speech app/t-t-s.py"
```

**BG Remover (AI, needs extra packages):**

```bash
pip install -r requirements.txt
python "BG remover/python-background-remover.py"
```

Then open the URL shown in the terminal (Flask). The web demo in `BG remover/index.html` works without Python and is fine for simple solid backgrounds.

---

## Repo structure

```
Python-projects/
├── index.html              # Project hub (start here)
├── apps.json               # List of apps for the hub
├── ADD_APP.md              # How to add a new project
├── shared/                 # Shared CSS/JS for hub and back buttons
├── .github/workflows/      # GitHub Pages deploy
├── Calculator/
├── Rock paper scissor/
├── DIce roller/
├── Timer/
├── Word frequency counter/
├── Text to speech app/
└── BG remover/
```

---

## Add a new app

1. Create a folder with your `.py` file and an `index.html` demo.
2. Add one object to [`apps.json`](apps.json).
3. Link back to the hub: `<a class="back-link" href="../index.html">← Back to Hub</a>` and optionally [`shared/app.css`](shared/app.css).

Full steps: **[ADD_APP.md](ADD_APP.md)**

---

## Publish on GitHub Pages

1. Push this repository to GitHub.
2. **Settings → Pages → Build and deployment**
3. **Source:** GitHub Actions  
   (uses [`.github/workflows/pages.yml`](.github/workflows/pages.yml))
4. After the workflow succeeds, your site is live at  
   `https://<your-username>.github.io/Python-projects/`

---

## Requirements

| Use case | What you need |
|----------|----------------|
| Web demos only | Any modern browser |
| Most Python apps | Python 3.x, standard library, **Tkinter** (GUI apps) |
| BG Remover (AI) | `flask`, `rembg`, `pillow` — see [`requirements.txt`](requirements.txt) |

---

## About

Built by **Ashish Sharma** — 1st year CS student. Code is kept simple on purpose for learning and practice.

Feel free to fork, change, and add your own apps.

## License

Free for learning and personal use.
