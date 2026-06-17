// Loads apps from apps.json and builds the project grid.
// To add a new app: edit apps.json and create YourApp/index.html

const grid = document.getElementById("project-grid");
const searchInput = document.getElementById("search-input");
const countLabel = document.getElementById("project-count");
const statProjects = document.getElementById("stat-projects");

let allApps = [];

function makeCard(app) {
  const link = document.createElement("a");
  link.className = "card";
  link.href = `${app.folder}/index.html`;
  link.dataset.color = app.color || "cyan";
  link.dataset.name = app.name.toLowerCase();
  link.dataset.tags = (app.tags || []).join(" ").toLowerCase();

  const tagText = (app.tags && app.tags[0]) ? app.tags[0] : "web";

  link.innerHTML = `
    <div class="card-top">
      <span class="card-icon">${app.icon || "📁"}</span>
      <span class="card-tag">${tagText}</span>
    </div>
    <h2>${app.name}</h2>
    <p>${app.description}</p>
    <span class="card-link">Open app →</span>
  `;

  return link;
}

function renderCards(apps) {
  // Keep the "add new" box at the end
  const addBox = document.getElementById("card-add");
  grid.querySelectorAll(".card").forEach((el) => el.remove());

  apps.forEach((app) => {
    grid.insertBefore(makeCard(app), addBox);
  });

  const total = allApps.length;
  countLabel.textContent = `${apps.length} of ${total} shown`;
  if (statProjects) statProjects.textContent = String(total);
}

function filterApps() {
  const q = searchInput.value.trim().toLowerCase();
  const filtered = allApps.filter((app) => {
    const hay = `${app.name} ${app.description} ${(app.tags || []).join(" ")}`.toLowerCase();
    return hay.includes(q);
  });
  renderCards(filtered);
}

// Used if apps.json cannot load (e.g. opening index.html as a file:// URL)
const fallbackApps = [
  { name: "Calculator", folder: "Calculator", icon: "🧮", color: "cyan", tags: ["web"], description: "Math with history." },
  { name: "Rock Paper Scissors", folder: "Rock paper scissor", icon: "✊", color: "violet", tags: ["game"], description: "Play vs the computer." },
  { name: "Dice Roller", folder: "DIce roller", icon: "🎲", color: "violet", tags: ["game"], description: "Roll dice with custom sides and see the total." },
  { name: "Countdown Timer", folder: "Timer", icon: "⏱️", color: "emerald", tags: ["web"], description: "Count down from seconds you enter." },
  { name: "Word Frequency Counter", folder: "Word frequency counter", icon: "📊", color: "amber", tags: ["web"], description: "Count words and letters." },
  { name: "Text to Speech", folder: "Text to speech app", icon: "🔊", color: "rose", tags: ["web"], description: "Hear your text aloud." },
  { name: "BG Remover", folder: "BG remover", icon: "🖼️", color: "blue", tags: ["web"], description: "Remove solid backgrounds in the browser." }
];

async function loadApps() {
  try {
    const res = await fetch("apps.json");
    if (!res.ok) throw new Error("Could not load apps.json");
    allApps = await res.json();
  } catch (err) {
    console.warn("Using built-in app list:", err);
    allApps = fallbackApps;
  }
  renderCards(allApps);
}

searchInput.addEventListener("input", filterApps);
loadApps();
