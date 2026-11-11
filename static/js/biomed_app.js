/**
 * Smart MedWaste AI - Bio-Medical Waste Segregation & IoT Monitoring System
 * Frontend Application Controller
 */

// State
let selectedImageFile = null;
let currentBinsData = {};
let allManifests = [];
let protocolsData = {};
let quizAnswers = {};

document.addEventListener("DOMContentLoaded", async () => {
  await fetchInitialBiomedData();
});

async function fetchInitialBiomedData() {
  await Promise.all([
    fetchBinsTelemetry(),
    fetchManifests(),
    fetchAuditSummary(),
    fetchProtocols()
  ]);
}

// --- TAB SWITCHER ---
function switchTab(tabId) {
  document.querySelectorAll(".biomed-tab-btn").forEach(btn => {
    btn.classList.remove("text-white", "bg-medical-600", "font-bold");
    btn.classList.add("text-slate-400", "hover:bg-slate-800", "hover:text-white");
  });

  const activeBtn = document.getElementById(`btn-tab-${tabId}`);
  if (activeBtn) {
    activeBtn.classList.remove("text-slate-400", "hover:bg-slate-800");
    activeBtn.classList.add("text-white", "bg-medical-600", "font-bold");
  }

  document.querySelectorAll(".tab-pane").forEach(pane => {
    pane.classList.add("hidden");
    pane.classList.remove("active");
  });

  const targetPane = document.getElementById(`tab-${tabId}`);
  if (targetPane) {
    targetPane.classList.remove("hidden");
    targetPane.classList.add("active");
  }

  if (tabId === "telemetry") {
    fetchBinsTelemetry();
  } else if (tabId === "manifest") {
    fetchManifests();
    fetchAuditSummary();
  }
}

// --- BINS TELEMETRY & MONITORING ---
async function fetchBinsTelemetry() {
  try {
    const res = await fetch("/api/biomed/bins");
    const data = await res.json();
    currentBinsData = data.bins || {};
    renderBins(currentBinsData);

    // Global alert banner
    const alertBanner = document.getElementById("systemAlertBanner");
    const alertText = document.getElementById("systemAlertText");
    if (data.alerts_count > 0) {
      alertBanner.classList.remove("hidden");
      alertText.textContent = `ALERT: ${data.total_alerts[0]}`;
    } else {
      alertBanner.classList.add("hidden");
    }
  } catch (err) {
    console.error("Telemetry error:", err);
  }
}

function renderBins(bins) {
  const container = document.getElementById("binsGrid");
  const generalContainer = document.getElementById("generalBinContainer");
  if (!container) return;

  const primaryCats = ["yellow", "red", "white", "blue"];
  
  container.innerHTML = primaryCats.map(cat => {
    const b = bins[cat];
    if (!b) return "";
    return renderBinCard(b);
  }).join("");

  if (generalContainer && bins["general"]) {
    generalContainer.innerHTML = renderBinCard(bins["general"], true);
  }
}

function renderBinCard(b, isWide = false) {
  const cat = b.category;
  const fill = b.fill_percentage;
  const isLocked = b.lockout_full;

  const colorThemes = {
    yellow: { bg: "bg-yellow-500", text: "text-yellow-400", border: "border-yellow-500/40", ring: "ring-yellow-500/20", glow: "shadow-yellow-500/10" },
    red: { bg: "bg-red-500", text: "text-red-400", border: "border-red-500/40", ring: "ring-red-500/20", glow: "shadow-red-500/10" },
    white: { bg: "bg-slate-300", text: "text-slate-200", border: "border-slate-400/40", ring: "ring-slate-400/20", glow: "shadow-slate-400/10" },
    blue: { bg: "bg-blue-500", text: "text-blue-400", border: "border-blue-500/40", ring: "ring-blue-500/20", glow: "shadow-blue-500/10" },
    general: { bg: "bg-emerald-500", text: "text-emerald-400", border: "border-emerald-500/40", ring: "ring-emerald-500/20", glow: "shadow-emerald-500/10" }
  };

  const theme = colorThemes[cat] || colorThemes.yellow;

  return `
    <div class="bin-box bg-slate-800/90 rounded-2xl border ${theme.border} p-5 shadow-xl flex flex-col justify-between ${isLocked ? 'ring-2 ring-red-500' : ''}">
      <div>
        <!-- Bin Header -->
        <div class="flex items-start justify-between gap-2 mb-3">
          <div>
            <span class="text-[10px] font-mono uppercase font-bold tracking-wider ${theme.text} block">
              ${b.id.toUpperCase()}
            </span>
            <h3 class="text-sm font-black text-white mt-0.5">${b.name}</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase ${isLocked ? 'bg-red-500/20 text-red-400 border border-red-500/30 animate-pulse' : 'bg-slate-700 text-slate-300'}">
            ${isLocked ? 'CHUTE LOCKED' : b.status_label}
          </span>
        </div>

        <!-- 3D Liquid Fill Level Tank Simulation -->
        <div class="bg-slate-900 rounded-xl p-3 border border-slate-700/80 mb-4">
          <div class="flex justify-between text-xs font-mono mb-1">
            <span class="text-slate-400">Fill Level:</span>
            <span class="font-bold text-white">${fill}%</span>
          </div>
          <!-- Progress bar -->
          <div class="w-full bg-slate-800 rounded-full h-3 overflow-hidden border border-slate-700">
            <div class="${theme.bg} liquid-fill h-full rounded-full" style="width: ${fill}%"></div>
          </div>
          <div class="flex justify-between text-[10px] text-slate-500 font-mono mt-1.5">
            <span>Depth: ${b.current_depth_cm} cm</span>
            <span>Max: ${b.max_depth_cm} cm</span>
          </div>
        </div>

        <!-- Multi-Sensor Metrics Grid -->
        <div class="grid grid-cols-2 gap-2 text-xs mb-4">
          <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-700/60 font-mono">
            <span class="text-[10px] text-slate-500 block">HX711 Mass</span>
            <strong class="text-white text-xs">${b.weight_kg} kg</strong>
            <span class="text-[9px] text-slate-500 block">/ ${b.max_weight_kg} kg</span>
          </div>
          <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-700/60 font-mono">
            <span class="text-[10px] text-slate-500 block">MQ-135 Gas</span>
            <strong class="${b.gas_ppm >= 250 ? 'text-amber-400' : 'text-slate-300'} text-xs">${b.gas_ppm} ppm</strong>
            <span class="text-[9px] text-slate-500 block">${b.temperature_c}°C</span>
          </div>
        </div>

        <!-- Disposed items counter -->
        <div class="text-[11px] text-slate-400 flex items-center justify-between mb-3">
          <span>Items Deposited:</span>
          <span class="font-mono text-white font-bold">${b.items_count} units</span>
        </div>

        <!-- Alerts if any -->
        ${b.alerts.length > 0 ? `
          <div class="p-2 rounded bg-amber-500/10 border border-amber-500/30 text-[10px] text-amber-300 mb-3 space-y-0.5">
            ${b.alerts.map(a => `<p>⚠️ ${a}</p>`).join("")}
          </div>
        ` : ''}
      </div>

      <!-- Footer Actions -->
      <div class="pt-3 border-t border-slate-700/60 flex items-center justify-between text-xs">
        <span class="text-[10px] text-slate-500">Last Emptied: ${b.last_emptied.split(' ')[1] || b.last_emptied}</span>
        <button onclick="emptyBinAction('${cat}')" class="px-2.5 py-1 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded-lg font-semibold text-[11px] transition flex items-center gap-1">
          <i class="fa-solid fa-broom text-[10px]"></i> <span>Empty</span>
        </button>
      </div>

    </div>
  `;
}

async function emptyBinAction(category) {
  if (!confirm(`Are you sure you want to empty and sanitize the ${category.toUpperCase()} bin?`)) return;

  try {
    const res = await fetch("/api/biomed/bins/empty", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ category })
    });
    const data = await res.json();
    alert(data.message || "Bin emptied!");
    await fetchBinsTelemetry();
  } catch (err) {
    console.error("Empty bin error:", err);
  }
}

// --- IMAGE UPLOAD & CLASSIFICATION ---
function previewSelectedImage(event) {
  const file = event.target.files[0];
  if (file) {
    selectedImageFile = file;
    document.getElementById("imageFilenameLabel").textContent = file.name;

    const reader = new FileReader();
    reader.onload = (e) => {
      document.getElementById("imagePreview").src = e.target.result;
      document.getElementById("imagePreviewContainer").classList.remove("hidden");
    };
    reader.readAsDataURL(file);
  }
}

async function handleImageClassification(e) {
  if (e) e.preventDefault();

  if (!selectedImageFile) {
    alert("Please upload a waste image or choose one of the sample test items above.");
    return;
  }

  const dept = document.getElementById("departmentSelect").value;
  const weight = document.getElementById("itemWeightInput").value;

  const emptyState = document.getElementById("classifierEmptyState");
  const loading = document.getElementById("classifierLoading");
  const resultContainer = document.getElementById("classifierResultContainer");

  emptyState.classList.add("hidden");
  loading.classList.remove("hidden");
  resultContainer.classList.add("hidden");

  try {
    const formData = new FormData();
    formData.append("image", selectedImageFile);
    formData.append("department", dept);
    formData.append("weight_kg", weight);

    const res = await fetch("/api/biomed/classify-image", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    if (data.error) {
      alert(data.error);
      emptyState.classList.remove("hidden");
    } else {
      renderClassificationResult(data);
      currentBinsData = data.all_bins || currentBinsData;
      renderBins(currentBinsData);
    }
  } catch (err) {
    console.error("Classification error:", err);
    alert("Error classifying image.");
    emptyState.classList.remove("hidden");
  } finally {
    loading.classList.add("hidden");
    resultContainer.classList.remove("hidden");
  }
}

// 1-Click Sample Test Item
async function testSampleItem(filename, label) {
  try {
    const res = await fetch(`/static/sample_waste_items/${filename}`);
    const blob = await res.blob();
    const file = new File([blob], filename, { type: "image/jpeg" });
    selectedImageFile = file;
    document.getElementById("imageFilenameLabel").textContent = `${label} (${filename})`;

    const reader = new FileReader();
    reader.onload = (e) => {
      document.getElementById("imagePreview").src = e.target.result;
      document.getElementById("imagePreviewContainer").classList.remove("hidden");
    };
    reader.readAsDataURL(file);

    switchTab("scanner");
    await handleImageClassification();
  } catch (err) {
    console.error("Sample item error:", err);
  }
}

// NLP Query Classification
async function handleQueryClassification(e) {
  if (e) e.preventDefault();
  const query = document.getElementById("queryTextInput").value.trim();
  if (!query) return;

  const dept = document.getElementById("departmentSelect").value;
  const weight = document.getElementById("itemWeightInput").value;

  const emptyState = document.getElementById("classifierEmptyState");
  const loading = document.getElementById("classifierLoading");
  const resultContainer = document.getElementById("classifierResultContainer");

  emptyState.classList.add("hidden");
  loading.classList.remove("hidden");
  resultContainer.classList.add("hidden");

  try {
    const res = await fetch("/api/biomed/classify-query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: query,
        department: dept,
        weight_kg: weight
      })
    });

    const data = await res.json();
    renderClassificationResult(data);
    currentBinsData = data.all_bins || currentBinsData;
    renderBins(currentBinsData);
  } catch (err) {
    console.error("Query classification error:", err);
  } finally {
    loading.classList.add("hidden");
    resultContainer.classList.remove("hidden");
  }
}

function renderClassificationResult(data) {
  const container = document.getElementById("classifierResultContainer");
  if (!container) return;

  const c = data.classification;
  const bin = c.bin;
  const servo = c.servo_actuator;
  const manifest = data.manifest;

  const colorThemes = {
    yellow: { badge: "bg-yellow-500/20 text-yellow-300 border-yellow-500/40", border: "border-yellow-500" },
    red: { badge: "bg-red-500/20 text-red-300 border-red-500/40", border: "border-red-500" },
    white: { badge: "bg-slate-400/20 text-slate-200 border-slate-400/40", border: "border-slate-300" },
    blue: { badge: "bg-blue-500/20 text-blue-300 border-blue-500/40", border: "border-blue-500" },
    general: { badge: "bg-emerald-500/20 text-emerald-300 border-emerald-500/40", border: "border-emerald-500" }
  };

  const theme = colorThemes[c.category] || colorThemes.yellow;

  container.innerHTML = `
    <!-- Top Result Banner -->
    <div class="bg-slate-800/90 rounded-2xl border-2 ${theme.border} p-6 shadow-2xl relative overflow-hidden">
      <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-4">
        <div>
          <div class="flex items-center gap-2 mb-2">
            <span class="px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider border ${theme.badge}">
              ${bin.bin_name}
            </span>
            <span class="text-xs font-mono text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/30">
              Confidence: ${c.confidence}%
            </span>
          </div>

          <h2 class="text-xl font-black text-white">${c.item_name}</h2>
          <p class="text-xs text-slate-400 mt-0.5">Classification Type: <strong class="text-slate-300">${c.item_type}</strong></p>
        </div>

        <!-- Chute Servo Motor Actuator Indicator -->
        <div class="bg-slate-900 p-3.5 rounded-xl border border-slate-700 text-center shrink-0">
          <span class="text-[10px] font-mono uppercase text-slate-400 block mb-1">Chute Servo Actuator</span>
          <div class="text-lg font-black text-yellow-400 font-mono">${servo.angle}°</div>
          <span class="text-[10px] text-slate-400 block">${servo.label}</span>
        </div>
      </div>

      <!-- Hazardous Bio-Specification Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3.5 rounded-xl border border-slate-700/60 text-xs mt-4">
        <div>
          <span class="text-slate-500 text-[10px] uppercase font-bold block">Hazard Rating:</span>
          <strong class="text-red-400">${c.hazard_rating}</strong>
        </div>
        <div>
          <span class="text-slate-500 text-[10px] uppercase font-bold block">Infection Vector Risk:</span>
          <strong class="text-amber-300">${c.infection_risk}</strong>
        </div>
      </div>

      <!-- Official CPCB / WHO Instructions -->
      <div class="mt-4 pt-4 border-t border-slate-700 text-xs space-y-2">
        <div>
          <strong class="text-slate-300 flex items-center gap-1.5 mb-1">
            <i class="fa-solid fa-hand-holding-medical text-medical-400"></i> Handling & Segregation Rules:
          </strong>
          <p class="text-slate-400 leading-relaxed">${c.handling_instructions}</p>
        </div>
        <div>
          <strong class="text-slate-300 flex items-center gap-1.5 mb-1">
            <i class="fa-solid fa-fire-burner text-amber-400"></i> Mandated Treatment & Disposal:
          </strong>
          <p class="text-slate-400 leading-relaxed">${c.treatment_method}</p>
        </div>
      </div>

      <!-- Auto Logged Digital Manifest Info -->
      ${manifest ? `
        <div class="mt-4 pt-3 border-t border-slate-700 flex flex-wrap items-center justify-between text-xs font-mono">
          <span class="text-slate-400">Digital Manifest ID: <strong class="text-medical-400">${manifest.manifest_id}</strong></span>
          <span class="text-slate-400">Barcode: <strong class="text-slate-200">${manifest.barcode}</strong></span>
        </div>
      ` : ''}

    </div>
  `;
}

// --- DIGITAL MANIFEST TABLE ---
async function fetchManifests() {
  const cat = document.getElementById("manifestCategoryFilter")?.value || "";
  const query = document.getElementById("manifestSearchInput")?.value || "";

  try {
    const res = await fetch(`/api/biomed/manifests?category=${cat}&query=${query}`);
    const data = await res.json();
    allManifests = data.manifests || [];
    renderManifestTable(allManifests);
  } catch (err) {
    console.error("Manifest error:", err);
  }
}

async function fetchAuditSummary() {
  try {
    const res = await fetch("/api/biomed/audit-summary");
    const data = await res.json();
    const container = document.getElementById("auditSummaryCards");
    if (!container) return;

    const b = data.weight_breakdown;

    container.innerHTML = `
      <div class="bg-slate-800 p-4 rounded-xl border border-slate-700">
        <span class="text-[10px] uppercase font-bold text-slate-400 block">Total Waste Segregated</span>
        <strong class="text-xl font-black text-white font-mono mt-0.5 block">${data.total_weight_kg} kg</strong>
        <span class="text-[10px] text-slate-500">${data.total_records} manifests logged</span>
      </div>
      <div class="bg-slate-800 p-4 rounded-xl border border-yellow-500/30">
        <span class="text-[10px] uppercase font-bold text-yellow-400 block">Yellow (Infectious)</span>
        <strong class="text-xl font-black text-yellow-400 font-mono mt-0.5 block">${b.yellow} kg</strong>
        <span class="text-[10px] text-slate-500">For Incineration</span>
      </div>
      <div class="bg-slate-800 p-4 rounded-xl border border-red-500/30">
        <span class="text-[10px] uppercase font-bold text-red-400 block">Red (Plastics)</span>
        <strong class="text-xl font-black text-red-400 font-mono mt-0.5 block">${b.red} kg</strong>
        <span class="text-[10px] text-slate-500">For Autoclave/Recycle</span>
      </div>
      <div class="bg-slate-800 p-4 rounded-xl border border-slate-600">
        <span class="text-[10px] uppercase font-bold text-slate-300 block">White (Sharps Safe)</span>
        <strong class="text-xl font-black text-slate-200 font-mono mt-0.5 block">${b.white} kg</strong>
        <span class="text-[10px] text-slate-500">For Encapsulation</span>
      </div>
    `;
  } catch (err) {
    console.error("Audit summary error:", err);
  }
}

function filterManifests() {
  fetchManifests();
}

function renderManifestTable(logs) {
  const tbody = document.getElementById("manifestTableBody");
  if (!tbody) return;

  if (logs.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" class="text-center py-6 text-slate-500">No manifest logs found.</td></tr>`;
    return;
  }

  tbody.innerHTML = logs.map(m => `
    <tr class="hover:bg-slate-800/40 transition">
      <td class="py-3 px-4 font-mono font-bold text-medical-400">${m.manifest_id}</td>
      <td class="py-3 px-4 text-slate-400">${m.timestamp}</td>
      <td class="py-3 px-4 text-slate-200">${m.department}</td>
      <td class="py-3 px-4 text-slate-300 font-medium">${m.item_name}</td>
      <td class="py-3 px-4 font-semibold text-slate-200">${m.category_label}</td>
      <td class="py-3 px-4 font-mono text-white font-bold">${m.weight_kg} kg</td>
      <td class="py-3 px-4 font-mono text-[11px] text-slate-400">${m.barcode}</td>
    </tr>
  `).join("");
}

// --- IOT HARDWARE LAB SLIDERS ---
function updateSliderVal(id, val) {
  const el = document.getElementById(`slider${id}Val`);
  if (el) el.textContent = val;
}

async function applySimulatedTelemetry() {
  const cat = document.getElementById("simBinSelect").value;
  const fill = document.getElementById("sliderFill").value;
  const weight = document.getElementById("sliderWeight").value;
  const gas = document.getElementById("sliderGas").value;

  try {
    const res = await fetch("/api/biomed/bins/update", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        category: cat,
        fill: fill,
        weight: weight,
        gas: gas
      })
    });
    const data = await res.json();
    alert(`Telemetry successfully dispatched to ${cat.toUpperCase()} Bin!`);
    await fetchBinsTelemetry();
  } catch (err) {
    console.error("Slider simulation error:", err);
  }
}

// --- SAFETY PROTOCOLS & STAFF QUIZ ---
async function fetchProtocols() {
  try {
    const res = await fetch("/api/biomed/protocols");
    protocolsData = await res.json();
    renderProtocols(protocolsData);
  } catch (err) {
    console.error("Protocols error:", err);
  }
}

function renderProtocols(data) {
  const pepContainer = document.getElementById("pepStepsContainer");
  const quizContainer = document.getElementById("staffQuizContainer");

  if (pepContainer && data.safety_protocols) {
    const steps = data.safety_protocols.needle_stick_injury.steps;
    pepContainer.innerHTML = steps.map(s => `
      <div class="flex gap-3 p-3 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <div class="w-6 h-6 rounded-full bg-red-600 text-white flex items-center justify-center font-bold text-xs shrink-0">
          ${s.step}
        </div>
        <div>
          <strong class="text-white block">${s.action}</strong>
          <span class="text-slate-400 mt-0.5 block">${s.detail}</span>
        </div>
      </div>
    `).join("");
  }

  if (quizContainer && data.staff_quiz) {
    quizContainer.innerHTML = data.staff_quiz.map((q, idx) => `
      <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-700 text-xs">
        <strong class="text-slate-200 block mb-2">${idx + 1}. ${q.question}</strong>
        <div class="space-y-1.5">
          ${q.options.map(opt => `
            <button onclick="handleQuizAnswer(${q.id}, ${opt.correct}, this, '${q.explanation.replace(/'/g, "\\'")}')" class="w-full text-left p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition flex items-center justify-between">
              <span>${opt.text}</span>
              <span class="quiz-feedback-icon text-xs"></span>
            </button>
          `).join("")}
        </div>
        <div id="quiz-expl-${q.id}" class="mt-2 text-[11px] text-slate-400 hidden p-2 rounded bg-slate-800/80"></div>
      </div>
    `).join("");
  }
}

function handleQuizAnswer(qId, isCorrect, btnEl, explanation) {
  const explEl = document.getElementById(`quiz-expl-${qId}`);
  if (explEl) {
    explEl.classList.remove("hidden");
    explEl.innerHTML = `<strong>${isCorrect ? '✓ Correct!' : '✗ Incorrect.'}</strong> ${explanation}`;
    explEl.className = isCorrect ? "mt-2 text-[11px] text-emerald-400 p-2 rounded bg-emerald-500/10 border border-emerald-500/30" : "mt-2 text-[11px] text-red-400 p-2 rounded bg-red-500/10 border border-red-500/30";
  }

  if (btnEl) {
    btnEl.classList.add(isCorrect ? "bg-emerald-600/30" : "bg-red-600/30");
  }
}

