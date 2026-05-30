# Python Projects

A collection of beginner-friendly Python programs, each with a **browser demo** so anyone on GitHub can try them without installing anything.

**Live site (after GitHub Pages is on):** `https://ashishsrs01.github.io/Python-projects/`

## Try in the browser

Open [`index.html`](index.html) locally, or use GitHub Pages (see below). The hub lists every app; click a card to open that project.

| App | Python file | Web demo |
|-----|-------------|----------|
| Calculator | `Calculator/Calculator.py` | `Calculator/index.html` |
| Rock Paper Scissors | `Rock paper scissor/Rock-paper-scissor-game.py` | `Rock paper scissor/index.html` |
| Countdown Timer | `Timer/Countdown Timer.py` | `Timer/index.html` |
| Word Frequency Counter | `Word frequency counter/counter.py` | `Word frequency counter/index.html` |
| Text to Speech | `Text to speech app/t-t-s.py` | `Text to speech app/index.html` |
| BG Remover | `BG remover/python-background-remover.py` | `BG remover/index.html` |

## Run Python locally

```bash
python "Calculator/Calculator.py"
python "Timer/Countdown Timer.py"
python "Rock paper scissor/Rock-paper-scissor-game.py"
```

For the AI background remover (Flask + rembg):

```bash
pip install -r requirements.txt
python "BG remover/python-background-remover.py"
```

## Add a new app

See **[ADD_APP.md](ADD_APP.md)** — create a folder + `index.html`, then add one entry to **`apps.json`**.

## GitHub Pages setup

1. Push this repo to GitHub.
2. Go to **Settings → Pages → Build and deployment**.
3. Source: **GitHub Actions** (the workflow in `.github/workflows/pages.yml` deploys the whole repo).
4. Wait for the green check on the **Pages** workflow, then open your site URL.

## Requirements

- Python 3.x for `.py` files (mostly standard library + Tkinter for GUI apps)
- Extra packages only for BG remover AI version — see `requirements.txt`

## License

Free to use for learning and practice. Copy, change, and experiment as you like.
