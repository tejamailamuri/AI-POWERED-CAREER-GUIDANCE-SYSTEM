/**
 * AI-Powered Career Guidance System - Main Client Application Logic
 */

// Global State
let userSkills = [];
let userInterests = [];
let allCareers = [];
let sampleProfiles = {};
let currentRecommendations = [];
let assessmentQuestions = [];
let selectedResumeFile = null;

// Initialize on page load
document.addEventListener("DOMContentLoaded", async () => {
  setupEventListeners();
  await fetchInitialData();
});

function setupEventListeners() {
  // Skill Input Enter Key
  const skillInput = document.getElementById("skillInput");
  if (skillInput) {
    skillInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        const val = skillInput.value.trim();
        if (val) {
          addSkill(val);
          skillInput.value = "";
        }
      }
    });
  }

  // Interest Input Enter Key
  const interestInput = document.getElementById("interestInput");
  if (interestInput) {
    interestInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        const val = interestInput.value.trim();
        if (val) {
          addInterest(val);
          interestInput.value = "";
        }
      }
    });
  }

  // Sample Profile Selector
  const sampleSelect = document.getElementById("sampleProfileSelect");
  if (sampleSelect) {
    sampleSelect.addEventListener("change", (e) => {
      const key = e.target.value;
      if (key) loadSampleProfile(key);
    });
  }

  // Modal Backdrop Click
  const modal = document.getElementById("careerModal");
  if (modal) {
    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeModal();
    });
  }
}

// Fetch Careers & Sample Profiles
async function fetchInitialData() {
  try {
    const [careersRes, profilesRes, questionsRes, marketRes] = await Promise.all([
      fetch("/api/careers"),
      fetch("/api/sample-profiles"),
      fetch("/api/assessment/questions"),
      fetch("/api/market-insights")
    ]);

    const careersData = await careersRes.json();
    allCareers = careersData.careers || [];
    sampleProfiles = await profilesRes.json();
    const qData = await questionsRes.json();
    assessmentQuestions = qData.questions || [];
    const marketData = await marketRes.json();

    populateCareerDropdowns(allCareers);
    populateExplorerGrid(allCareers);
    populateMarketInsights(marketData);
    renderAssessmentQuiz(assessmentQuestions);
    refreshJobMatches();
  } catch (err) {
    console.error("Error loading initial data:", err);
  }
}

// Tab Switching
function switchTab(tabId) {
  // Update Buttons
  document.querySelectorAll(".tab-button").forEach((btn) => {
    btn.classList.remove("active", "text-brand-600", "bg-brand-50", "font-semibold");
    btn.classList.add("hover:bg-slate-100");
  });

  const activeBtn = document.getElementById(`tab-btn-${tabId}`);
  if (activeBtn) {
    activeBtn.classList.add("active", "text-brand-600", "bg-brand-50", "font-semibold");
    activeBtn.classList.remove("hover:bg-slate-100");
  }

  // Update Panes
  document.querySelectorAll(".tab-pane").forEach((pane) => {
    pane.classList.remove("active");
  });

  const targetPane = document.getElementById(`tab-${tabId}`);
  if (targetPane) {
    targetPane.classList.add("active");
  }

  // If opening Skill Gap, update skills summary
  if (tabId === "skill-gap") {
    updateGapSkillsView();
  }
}

// --- SKILL & INTEREST TAG MANAGEMENT ---
function addSkill(skill) {
  const clean = skill.trim();
  if (clean && !userSkills.some(s => s.toLowerCase() === clean.toLowerCase())) {
    userSkills.push(clean);
    renderSkillTags();
    updateGapSkillsView();
  }
}

function removeSkill(index) {
  userSkills.splice(index, 1);
  renderSkillTags();
  updateGapSkillsView();
}

function renderSkillTags() {
  const container = document.getElementById("skillsContainer");
  if (!container) return;
  container.innerHTML = userSkills.map((s, idx) => `
    <span class="inline-flex items-center gap-1.5 bg-brand-50 text-brand-700 text-xs px-2.5 py-1 rounded-lg border border-brand-200 font-medium">
      ${s}
      <button type="button" onclick="removeSkill(${idx})" class="hover:text-red-500 transition">
        <i class="fa-solid fa-xmark text-[10px]"></i>
      </button>
    </span>
  `).join("");
}

function addInterest(interest) {
  const clean = interest.trim();
  if (clean && !userInterests.some(i => i.toLowerCase() === clean.toLowerCase())) {
    userInterests.push(clean);
    renderInterestTags();
  }
}

function removeInterest(index) {
  userInterests.splice(index, 1);
  renderInterestTags();
}

function renderInterestTags() {
  const container = document.getElementById("interestsContainer");
  if (!container) return;
  container.innerHTML = userInterests.map((item, idx) => `
    <span class="inline-flex items-center gap-1.5 bg-indigo-50 text-indigo-700 text-xs px-2.5 py-1 rounded-lg border border-indigo-200 font-medium">
      ${item}
      <button type="button" onclick="removeInterest(${idx})" class="hover:text-red-500 transition">
        <i class="fa-solid fa-xmark text-[10px]"></i>
      </button>
    </span>
  `).join("");
}

function resetForm() {
  userSkills = [];
  userInterests = [];
  renderSkillTags();
  renderInterestTags();
  document.getElementById("profileForm").reset();
  document.getElementById("recommenderEmptyState").classList.remove("hidden");
  document.getElementById("recommendationsList").classList.add("hidden");
  document.getElementById("sampleProfileSelect").value = "";
}

// --- SAMPLE PROFILE LOADER ---
function loadSampleProfile(key) {
  const profile = sampleProfiles[key];
  if (!profile) return;

  userSkills = [...profile.skills];
  userInterests = [...profile.interests];
  renderSkillTags();
  renderInterestTags();

  document.getElementById("degreeSelect").value = profile.degree || "Bachelor's";
  document.getElementById("majorInput").value = profile.major || "";
  document.getElementById("gpaInput").value = profile.gpa || "";
  document.getElementById("workStyleSelect").value = profile.work_style || "Any";
  document.getElementById("targetIndustrySelect").value = profile.preferred_industry || "";

  switchTab("recommender");
  document.getElementById("recommendBtn").click();
}

// --- RECOMMENDATION FORM SUBMISSION ---
async function handleRecommendationSubmit(event) {
  if (event) event.preventDefault();

  if (userSkills.length === 0) {
    alert("Please enter at least 1 or 2 skills or select a sample profile!");
    return;
  }

  const payload = {
    skills: userSkills,
    interests: userInterests,
    degree: document.getElementById("degreeSelect").value,
    major: document.getElementById("majorInput").value,
    gpa: parseFloat(document.getElementById("gpaInput").value) || 0,
    work_style: document.getElementById("workStyleSelect").value,
    preferred_industry: document.getElementById("targetIndustrySelect").value
  };

  const emptyState = document.getElementById("recommenderEmptyState");
  const loading = document.getElementById("recommenderLoading");
  const listContainer = document.getElementById("recommendationsList");

  emptyState.classList.add("hidden");
  loading.classList.remove("hidden");
  listContainer.classList.add("hidden");

  try {
    const res = await fetch("/api/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    currentRecommendations = data.recommendations || [];
    renderRecommendations(currentRecommendations);
  } catch (err) {
    console.error("Recommendation error:", err);
    alert("Error fetching recommendations. Please check console.");
  } finally {
    loading.classList.add("hidden");
    listContainer.classList.remove("hidden");
  }
}

function renderRecommendations(recommendations) {
  const container = document.getElementById("recommendationsList");
  if (!container) return;

  if (recommendations.length === 0) {
    container.innerHTML = `
      <div class="bg-white rounded-2xl border border-slate-200 p-8 text-center text-slate-500">
        No matches found. Try broadening your skills or removing specific filters.
      </div>
    `;
    return;
  }

  container.innerHTML = recommendations.map((rec, index) => {
    const isTop = index === 0;
    const badgeColor = rec.overall_match >= 75 ? "emerald" : (rec.overall_match >= 55 ? "indigo" : "slate");

    return `
      <div class="glass-card rounded-2xl p-6 relative overflow-hidden ${isTop ? 'border-brand-500/50 shadow-md ring-1 ring-brand-500/20' : ''}">
        ${isTop ? `
          <div class="absolute top-0 right-0 bg-gradient-to-l from-brand-600 to-indigo-600 text-white text-[10px] font-bold px-3 py-1 rounded-bl-xl uppercase tracking-wider flex items-center gap-1 shadow-sm">
            <i class="fa-solid fa-crown text-amber-300"></i> Top AI Match
          </div>
        ` : ''}

        <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-4 mb-4">
          <div>
            <span class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-${badgeColor}-50 text-${badgeColor}-700 border border-${badgeColor}-200 mb-1.5 inline-block">
              ${rec.category}
            </span>
            <h3 class="text-lg font-bold text-slate-900">${rec.title}</h3>
            <p class="text-xs text-slate-500 mt-1 line-clamp-2">${rec.description}</p>
          </div>

          <!-- Overall Match Circular Gauge -->
          <div class="shrink-0 flex items-center gap-3">
            <div class="text-right">
              <div class="text-2xl font-black text-brand-600">${rec.overall_match}%</div>
              <div class="text-[10px] uppercase font-bold text-slate-400">Match Score</div>
            </div>
          </div>
        </div>

        <!-- Score Breakdown Bars -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 bg-slate-50 p-3 rounded-xl border border-slate-100 text-xs mb-4">
          <div>
            <span class="text-slate-400 text-[10px] block">Skill Match</span>
            <span class="font-bold text-slate-700">${rec.score_breakdown.skill_match}%</span>
          </div>
          <div>
            <span class="text-slate-400 text-[10px] block">Semantic NLP</span>
            <span class="font-bold text-slate-700">${rec.score_breakdown.nlp_match}%</span>
          </div>
          <div>
            <span class="text-slate-400 text-[10px] block">Interest Fit</span>
            <span class="font-bold text-slate-700">${rec.score_breakdown.interest_alignment}%</span>
          </div>
          <div>
            <span class="text-slate-400 text-[10px] block">Salary Growth</span>
            <span class="font-bold text-emerald-600">${rec.salary_entry}</span>
          </div>
        </div>

        <!-- Matched Skills & Missing Skills -->
        <div class="space-y-2 mb-4 text-xs">
          <div class="flex items-start gap-2">
            <span class="text-slate-400 font-medium shrink-0 w-24">Matched Skills:</span>
            <div class="flex flex-wrap gap-1">
              ${rec.skills_matched.length > 0 ? rec.skills_matched.map(s => `
                <span class="px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 text-[11px] font-medium">✓ ${s}</span>
              `).join("") : '<span class="text-slate-400 italic">Foundational crossover</span>'}
            </div>
          </div>
          ${rec.missing_skills.length > 0 ? `
            <div class="flex items-start gap-2">
              <span class="text-slate-400 font-medium shrink-0 w-24">Key Skills to Add:</span>
              <div class="flex flex-wrap gap-1">
                ${rec.missing_skills.slice(0, 4).map(s => `
                  <span class="px-2 py-0.5 rounded bg-amber-50 text-amber-800 border border-amber-200 text-[11px] font-medium">+ ${s}</span>
                `).join("")}
              </div>
            </div>
          ` : ''}
        </div>

        <!-- Explainable AI (XAI) Reasons -->
        ${rec.reasons.length > 0 ? `
          <div class="bg-indigo-50/50 border border-indigo-100 rounded-xl p-3 mb-4 text-xs text-indigo-900 space-y-1">
            <div class="font-semibold text-brand-700 flex items-center gap-1.5 text-[11px] uppercase tracking-wide">
              <i class="fa-solid fa-lightbulb"></i> Why this matches you:
            </div>
            ${rec.reasons.map(r => `<p class="text-slate-600">• ${r}</p>`).join("")}
          </div>
        ` : ''}

        <!-- Card Action Buttons -->
        <div class="flex flex-wrap items-center justify-between gap-2 pt-3 border-t border-slate-100 text-xs">
          <div class="flex items-center gap-1.5 text-slate-500">
            <i class="fa-solid fa-arrow-trend-up text-emerald-500"></i>
            <span>Growth: <strong class="text-slate-700">${rec.growth_rate}</strong></span>
          </div>

          <div class="flex items-center gap-2">
            <button onclick="goToSkillGap('${rec.career_id}')" class="px-3 py-1.5 bg-brand-50 hover:bg-brand-100 text-brand-700 rounded-lg font-semibold transition flex items-center gap-1">
              <i class="fa-solid fa-chart-pie text-xs"></i> <span>Analyze Gap</span>
            </button>
            <button onclick="openCareerModal('${rec.career_id}')" class="px-3 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg font-semibold transition flex items-center gap-1">
              <i class="fa-solid fa-road text-xs"></i> <span>View Roadmap</span>
            </button>
          </div>
        </div>

      </div>
    `;
  }).join("");
}

// Redirect to Skill Gap Tab with career selected
function goToSkillGap(careerId) {
  const select = document.getElementById("gapCareerSelect");
  if (select) select.value = careerId;
  switchTab("skill-gap");
  runSkillGapAnalysis();
}

// --- SKILL GAP ANALYZER ---
function updateGapSkillsView() {
  const container = document.getElementById("gapCurrentSkillsList");
  if (!container) return;

  if (userSkills.length === 0) {
    container.innerHTML = `<span class="text-slate-400 italic">No skills entered yet. Add skills in the Recommender tab.</span>`;
  } else {
    container.innerHTML = userSkills.map(s => `
      <span class="px-2 py-0.5 rounded bg-brand-50 text-brand-700 border border-brand-200 text-[11px] font-medium">${s}</span>
    `).join("");
  }
}

async function runSkillGapAnalysis() {
  const careerId = document.getElementById("gapCareerSelect").value;
  const container = document.getElementById("skillGapResults");
  if (!careerId) return;

  container.innerHTML = `
    <div class="bg-white rounded-2xl border border-slate-200 p-12 text-center">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-4 border-brand-500 border-t-transparent mb-3"></div>
      <p class="text-sm font-medium text-slate-600">Analyzing skill matrix and building customized action plan...</p>
    </div>
  `;

  try {
    const res = await fetch("/api/skill-gap", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_skills: userSkills,
        target_career_id: careerId
      })
    });

    const data = await res.json();
    renderSkillGapResults(data);
  } catch (err) {
    console.error("Skill Gap error:", err);
    container.innerHTML = `<div class="p-6 bg-red-50 text-red-700 rounded-xl">Error analyzing skill gap.</div>`;
  }
}

function renderSkillGapResults(data) {
  const container = document.getElementById("skillGapResults");
  if (!container) return;

  const readinessColor = data.readiness_score >= 70 ? "emerald" : (data.readiness_score >= 40 ? "amber" : "rose");

  container.innerHTML = `
    <!-- Summary Header Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5 mb-6">
      
      <!-- Readiness Score Gauge -->
      <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm flex items-center justify-between">
        <div>
          <span class="text-xs uppercase font-semibold text-slate-400 block mb-1">Skill Readiness Index</span>
          <h3 class="text-3xl font-extrabold text-${readinessColor}-600">${data.readiness_score}%</h3>
          <span class="text-xs font-medium text-slate-500 block mt-1">${data.readiness_level}</span>
        </div>
        <div class="w-16 h-16 rounded-full bg-${readinessColor}-50 border-4 border-${readinessColor}-400 flex items-center justify-center text-${readinessColor}-600 text-xl font-bold">
          <i class="fa-solid fa-gauge-high"></i>
        </div>
      </div>

      <!-- Missing High Priority Gaps -->
      <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
        <span class="text-xs uppercase font-semibold text-slate-400 block mb-1">Critical Skill Gaps</span>
        <h3 class="text-3xl font-extrabold text-amber-600">${data.high_priority_gaps.length} Tools</h3>
        <p class="text-xs text-slate-500 mt-1">High priority for technical screening rounds.</p>
      </div>

      <!-- Estimated Time to Bridge -->
      <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
        <span class="text-xs uppercase font-semibold text-slate-400 block mb-1">Estimated Preparation</span>
        <h3 class="text-3xl font-extrabold text-brand-600">8 - 14 Weeks</h3>
        <p class="text-xs text-slate-500 mt-1">Based on dedicated 10-15 hrs/week structured practice.</p>
      </div>

    </div>

    <!-- Skills Breakdown Lists -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
      
      <!-- Acquired Skills -->
      <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
        <h4 class="text-sm font-bold text-slate-800 mb-3 flex items-center gap-2">
          <i class="fa-solid fa-circle-check text-emerald-500"></i> Skills You Already Possess (${data.matched_skills.length})
        </h4>
        <div class="flex flex-wrap gap-2">
          ${data.matched_skills.length > 0 ? data.matched_skills.map(s => `
            <span class="px-3 py-1 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-medium">
              ✓ ${s.name}
            </span>
          `).join("") : '<span class="text-xs text-slate-400 italic">None yet. Start with Step 1 in the Action Plan below!</span>'}
        </div>
      </div>

      <!-- Missing Skills by Priority -->
      <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
        <h4 class="text-sm font-bold text-slate-800 mb-3 flex items-center gap-2">
          <i class="fa-solid fa-triangle-exclamation text-amber-500"></i> Missing Skills to Acquire (${data.high_priority_gaps.length + data.medium_priority_gaps.length})
        </h4>
        <div class="space-y-2">
          ${data.high_priority_gaps.map(g => `
            <div class="flex items-center justify-between p-2 rounded-lg bg-red-50/70 border border-red-200 text-xs">
              <span class="font-semibold text-red-900">${g.name}</span>
              <span class="px-2 py-0.5 rounded bg-red-100 text-red-700 font-bold text-[10px] uppercase">High Priority</span>
            </div>
          `).join("")}
          ${data.medium_priority_gaps.map(g => `
            <div class="flex items-center justify-between p-2 rounded-lg bg-amber-50/70 border border-amber-200 text-xs">
              <span class="font-semibold text-amber-900">${g.name}</span>
              <span class="px-2 py-0.5 rounded bg-amber-100 text-amber-700 font-medium text-[10px] uppercase">Secondary Advantage</span>
            </div>
          `).join("")}
        </div>
      </div>

    </div>

    <!-- Personalized Action Plan -->
    <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm mb-8">
      <h3 class="text-base font-bold text-slate-900 mb-4 flex items-center gap-2">
        <i class="fa-solid fa-list-check text-brand-600"></i> Personalized Action Plan to Close the Gap
      </h3>
      <div class="space-y-4">
        ${data.custom_action_steps.map(step => `
          <div class="flex gap-4 p-4 rounded-xl bg-slate-50 border border-slate-200">
            <div class="w-8 h-8 rounded-full bg-brand-600 text-white flex items-center justify-center font-bold text-sm shrink-0">
              ${step.step}
            </div>
            <div>
              <div class="flex items-center gap-3">
                <h5 class="text-sm font-bold text-slate-800">${step.title}</h5>
                <span class="text-[11px] text-brand-600 font-semibold bg-brand-50 px-2 py-0.5 rounded-full border border-brand-200">${step.estimated_timeline}</span>
              </div>
              <p class="text-xs text-slate-700 font-medium mt-1">${step.focus}</p>
              <p class="text-xs text-slate-500 mt-1">${step.recommended_action}</p>
            </div>
          </div>
        `).join("")}
      </div>
    </div>

    <!-- Structured 3-Phase Curriculum -->
    <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
      <h3 class="text-base font-bold text-slate-900 mb-4 flex items-center gap-2">
        <i class="fa-solid fa-graduation-cap text-indigo-600"></i> Complete 3-Phase Career Curriculum & Free Resources
      </h3>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        ${data.full_roadmap.map(phase => `
          <div class="p-4 rounded-xl border border-slate-200 bg-slate-50 flex flex-col justify-between">
            <div>
              <span class="text-[10px] uppercase font-bold text-brand-600 tracking-wider">${phase.phase}</span>
              <h5 class="text-sm font-bold text-slate-800 mt-1 mb-2">${phase.focus}</h5>
              <p class="text-xs text-slate-600 mb-3">${phase.topics.join(", ")}</p>
            </div>
            <div class="pt-3 border-t border-slate-200 text-xs">
              <span class="text-slate-400 font-semibold block text-[10px] uppercase mb-1">Recommended Free Resources:</span>
              <ul class="space-y-1 text-slate-700">
                ${phase.free_resources.map(r => `<li>• ${r}</li>`).join("")}
              </ul>
            </div>
          </div>
        `).join("")}
      </div>
    </div>
  `;
}

// --- RESUME EVALUATOR & ATS SCANNER ---
function handleFileSelect(e) {
  const file = e.target.files[0];
  if (file) {
    selectedResumeFile = file;
    document.getElementById("fileLabel").innerHTML = `<strong class="text-brand-600">${file.name}</strong> (${(file.size / 1024).toFixed(1)} KB)`;
  }
}

async function loadSampleResume(type) {
  const filename = type === "se" ? "sample_software_engineer.txt" : "sample_data_scientist.txt";
  try {
    const res = await fetch(`/static/sample_resumes/${filename}`);
    const text = await res.text();
    document.getElementById("resumeTextInput").value = text;
    selectedResumeFile = null;
    document.getElementById("fileLabel").textContent = "Click to upload your resume document";
    
    // Switch to resume tab and select matching target role
    switchTab("resume");
    const targetCareerSelect = document.getElementById("resumeTargetCareer");
    if (targetCareerSelect) {
      targetCareerSelect.value = type === "se" ? "full-stack-developer" : "data-scientist";
    }

    // Trigger evaluation
    document.getElementById("resumeEvaluateBtn").click();
  } catch (err) {
    console.error("Error loading sample resume:", err);
  }
}

async function handleResumeSubmit(e) {
  if (e) e.preventDefault();

  const textInput = document.getElementById("resumeTextInput").value.trim();
  const targetCareerId = document.getElementById("resumeTargetCareer").value;

  if (!selectedResumeFile && textInput.length < 50) {
    alert("Please upload a resume file or paste at least 50 characters of resume text.");
    return;
  }

  const emptyState = document.getElementById("resumeEmptyState");
  const loading = document.getElementById("resumeLoadingState");
  const resultsContainer = document.getElementById("resumeResults");

  emptyState.classList.add("hidden");
  loading.classList.remove("hidden");
  resultsContainer.classList.add("hidden");

  try {
    let res;
    if (selectedResumeFile) {
      const formData = new FormData();
      formData.append("file", selectedResumeFile);
      if (targetCareerId) formData.append("target_career_id", targetCareerId);

      res = await fetch("/api/resume/evaluate", {
        method: "POST",
        body: formData
      });
    } else {
      res = await fetch("/api/resume/evaluate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          resume_text: textInput,
          target_career_id: targetCareerId
        })
      });
    }

    const data = await res.json();
    if (data.error) {
      alert(data.error);
      emptyState.classList.remove("hidden");
    } else {
      renderResumeResults(data);
    }
  } catch (err) {
    console.error("Resume error:", err);
    alert("Error evaluating resume. Please check console.");
    emptyState.classList.remove("hidden");
  } finally {
    loading.classList.add("hidden");
    resultsContainer.classList.remove("hidden");
  }
}

function renderResumeResults(data) {
  const container = document.getElementById("resumeResults");
  if (!container) return;

  const atsScore = data.ats_score;
  const scoreColor = atsScore >= 80 ? "emerald" : (atsScore >= 60 ? "indigo" : "amber");
  const statusLabel = atsScore >= 80 ? "ATS Ready (High Visibility)" : (atsScore >= 60 ? "Solid Structure (Minor Polish)" : "Needs Optimization");

  container.innerHTML = `
    <!-- Top Score Overview -->
    <div class="glass-card rounded-2xl p-6 border border-slate-200">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-6">
        <div>
          <span class="text-xs uppercase font-bold text-slate-400 tracking-wider">Overall ATS Readability</span>
          <h3 class="text-2xl font-black text-slate-900 mt-1">${statusLabel}</h3>
          <p class="text-xs text-slate-500 mt-1">${data.length_feedback} (Word count: ${data.word_count})</p>
        </div>

        <div class="text-center">
          <div class="w-24 h-24 rounded-full bg-${scoreColor}-50 border-8 border-${scoreColor}-500 flex flex-col items-center justify-center shadow-md">
            <span class="text-2xl font-black text-${scoreColor}-700">${atsScore}</span>
            <span class="text-[9px] font-bold uppercase text-${scoreColor}-600">/ 100</span>
          </div>
        </div>
      </div>

      <!-- Sub-score Breakdown -->
      <div class="grid grid-cols-2 sm:grid-cols-5 gap-2 mt-6 pt-5 border-t border-slate-100 text-center text-xs">
        <div class="p-2 rounded-lg bg-slate-50">
          <span class="text-[10px] text-slate-400 block">Sections</span>
          <strong class="text-slate-800">${data.score_breakdown.section_completeness}/25</strong>
        </div>
        <div class="p-2 rounded-lg bg-slate-50">
          <span class="text-[10px] text-slate-400 block">Contact Info</span>
          <strong class="text-slate-800">${data.score_breakdown.contact_info}/15</strong>
        </div>
        <div class="p-2 rounded-lg bg-slate-50">
          <span class="text-[10px] text-slate-400 block">Skills Detected</span>
          <strong class="text-slate-800">${data.score_breakdown.skill_richness}/25</strong>
        </div>
        <div class="p-2 rounded-lg bg-slate-50">
          <span class="text-[10px] text-slate-400 block">Action & Metrics</span>
          <strong class="text-slate-800">${data.score_breakdown.action_and_metrics}/20</strong>
        </div>
        <div class="p-2 rounded-lg bg-slate-50">
          <span class="text-[10px] text-slate-400 block">Readability</span>
          <strong class="text-slate-800">${data.score_breakdown.formatting_readability}/15</strong>
        </div>
      </div>
    </div>

    <!-- Role Alignment Card (If Target Role selected) -->
    ${data.role_alignment ? `
      <div class="bg-indigo-50/70 border border-indigo-200 rounded-2xl p-5 text-xs">
        <div class="flex items-center justify-between mb-2">
          <h4 class="font-bold text-brand-800 flex items-center gap-1.5 text-sm">
            <i class="fa-solid fa-bullseye text-brand-600"></i> Role Alignment: ${data.role_alignment.target_career}
          </h4>
          <span class="font-extrabold text-brand-700 text-sm">${data.role_alignment.role_match_pct}% Match</span>
        </div>
        <p class="text-slate-600 mb-3">${data.role_alignment.advice}</p>
        <div class="flex items-center gap-2">
          <span class="font-semibold text-indigo-900 shrink-0">Missing Keywords to Add:</span>
          <div class="flex flex-wrap gap-1">
            ${data.role_alignment.missing_keywords_to_add.map(k => `
              <span class="px-2 py-0.5 rounded bg-white text-indigo-700 font-semibold border border-indigo-200 text-[11px]">+ ${k}</span>
            `).join("")}
          </div>
        </div>
      </div>
    ` : ''}

    <!-- Contact & Section Checks -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      
      <!-- Section Checklist -->
      <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm text-xs">
        <h4 class="font-bold text-slate-800 mb-3 flex items-center gap-1.5">
          <i class="fa-solid fa-list text-slate-400"></i> Required ATS Resume Sections
        </h4>
        <div class="space-y-1.5">
          ${Object.entries(data.sections_detected).map(([sec, present]) => `
            <div class="flex items-center justify-between p-1.5 rounded ${present ? 'bg-emerald-50 text-emerald-800' : 'bg-slate-50 text-slate-400'}">
              <span>${sec}</span>
              <span>${present ? '✓ Found' : '✗ Missing'}</span>
            </div>
          `).join("")}
        </div>
      </div>

      <!-- Action Verbs & Metrics -->
      <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm text-xs">
        <h4 class="font-bold text-slate-800 mb-3 flex items-center gap-1.5">
          <i class="fa-solid fa-bolt text-amber-500"></i> Impact Phrasing & Metrics
        </h4>
        <div class="space-y-3">
          <div>
            <span class="text-slate-500 block mb-1">Strong Action Verbs (${data.action_analysis.action_verb_count}):</span>
            <div class="flex flex-wrap gap-1">
              ${data.action_analysis.action_verbs.map(v => `
                <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 text-[11px] font-medium">${v}</span>
              `).join("")}
            </div>
          </div>
          <div>
            <span class="text-slate-500 block mb-1">Quantified Metrics Found (${data.action_analysis.metrics_count}):</span>
            <div class="flex flex-wrap gap-1">
              ${data.action_analysis.metrics_detected.map(m => `
                <span class="px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 font-mono text-[11px] font-semibold">${m}</span>
              `).join("")}
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- Extracted Skills -->
    <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm text-xs">
      <h4 class="font-bold text-slate-800 mb-2 flex items-center gap-1.5">
        <i class="fa-solid fa-code text-brand-600"></i> Skills Extracted (${data.skills_extracted.length})
      </h4>
      <div class="flex flex-wrap gap-1.5">
        ${data.skills_extracted.map(s => `
          <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 border border-slate-200 font-medium text-[11px]">${s}</span>
        `).join("")}
      </div>
    </div>

    <!-- Actionable Improvement Suggestions -->
    ${data.improvement_suggestions.length > 0 ? `
      <div class="bg-amber-50/70 border border-amber-200 rounded-2xl p-5 text-xs text-amber-950">
        <h4 class="font-bold text-amber-900 mb-2 flex items-center gap-1.5">
          <i class="fa-solid fa-wand-magic-sparkles text-amber-600"></i> Recommendations to Boost Your Score
        </h4>
        <ul class="space-y-1 text-slate-700">
          ${data.improvement_suggestions.map(s => `<li>• ${s}</li>`).join("")}
        </ul>
      </div>
    ` : ''}
  `;
}

// --- HOLLAND RIASEC ASSESSMENT QUIZ ---
function renderAssessmentQuiz(questions) {
  const container = document.getElementById("questionsContainer");
  if (!container) return;

  container.innerHTML = questions.map((q, qIdx) => `
    <div class="p-5 rounded-2xl border border-slate-200 bg-slate-50/60">
      <h4 class="text-sm font-bold text-slate-800 mb-3 flex items-center gap-2">
        <span class="w-6 h-6 rounded-full bg-brand-600 text-white flex items-center justify-center text-xs">${q.id}</span>
        <span>${q.question}</span>
      </h4>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
        ${q.options.map((opt, oIdx) => `
          <label class="flex items-start gap-2.5 p-3 rounded-xl border border-slate-200 bg-white hover:border-brand-500 hover:bg-brand-50/20 cursor-pointer transition">
            <input type="radio" name="q_${q.id}" value="${opt.trait}" required class="mt-0.5 text-brand-600 focus:ring-brand-500">
            <span class="text-slate-700 font-medium leading-relaxed">${opt.text}</span>
          </label>
        `).join("")}
      </div>
    </div>
  `).join("");
}

async function handleAssessmentSubmit(e) {
  if (e) e.preventDefault();

  const answers = [];
  assessmentQuestions.forEach(q => {
    const selected = document.querySelector(`input[name="q_${q.id}"]:checked`);
    if (selected) answers.push(selected.value);
  });

  if (answers.length < assessmentQuestions.length) {
    alert("Please answer all questions before submitting.");
    return;
  }

  try {
    const res = await fetch("/api/assessment/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answers })
    });

    const data = await res.json();
    renderAssessmentResults(data);
  } catch (err) {
    console.error("Assessment error:", err);
  }
}

function renderAssessmentResults(data) {
  const quizForm = document.getElementById("quizContainer");
  const resultsContainer = document.getElementById("quizResultsContainer");

  quizForm.classList.add("hidden");
  resultsContainer.classList.remove("hidden");

  resultsContainer.innerHTML = `
    <div class="text-center max-w-xl mx-auto mb-8">
      <span class="text-xs uppercase font-bold text-brand-600 tracking-wider">Your Holland Personality Archetype</span>
      <h2 class="text-3xl font-black text-slate-900 mt-1 mb-2">Holland Code: ${data.holland_code}</h2>
      <p class="text-xs text-slate-500">Based on your answers, your primary vocational traits are:</p>
      <div class="flex flex-wrap justify-center gap-2 mt-3">
        ${data.top_traits.map(t => `
          <span class="px-3 py-1 rounded-full bg-brand-50 text-brand-700 border border-brand-200 text-xs font-bold">
            ${t.name}
          </span>
        `).join("")}
      </div>
    </div>

    <!-- Trait Percentage Breakdown -->
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 mb-8">
      ${data.trait_breakdown.map(t => `
        <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
          <div class="flex justify-between text-xs font-bold mb-1">
            <span class="text-slate-700">${t.code} - ${t.name.split(' ')[0]}</span>
            <span class="text-brand-600">${t.percentage}%</span>
          </div>
          <div class="w-full bg-slate-200 rounded-full h-1.5 mb-2">
            <div class="bg-brand-600 h-1.5 rounded-full" style="width: ${t.percentage}%"></div>
          </div>
          <p class="text-[11px] text-slate-500 line-clamp-2">${t.description}</p>
        </div>
      `).join("")}
    </div>

    <!-- Recommended Careers based on Personality -->
    <div class="mb-8">
      <h3 class="text-base font-bold text-slate-900 mb-4 flex items-center gap-2">
        <i class="fa-solid fa-compass text-brand-600"></i> Top Career Matches for Your Personality
      </h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        ${data.matching_careers.map(c => `
          <div class="p-4 rounded-2xl border border-slate-200 bg-white hover:border-brand-500 transition shadow-sm flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1.5">
                <span class="text-[10px] font-bold uppercase text-brand-600">${c.category}</span>
                <span class="px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 font-bold text-xs">${c.compatibility_score}% Personality Fit</span>
              </div>
              <h4 class="text-sm font-bold text-slate-900">${c.title}</h4>
              <p class="text-xs text-slate-500 mt-1 line-clamp-2">${c.description}</p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs">
              <span class="text-slate-500">Entry: <strong class="text-slate-800">${c.entry_salary}</strong></span>
              <button onclick="openCareerModal('${c.id}')" class="text-brand-600 hover:text-brand-700 font-semibold">
                Explore Pathway →
              </button>
            </div>
          </div>
        `).join("")}
      </div>
    </div>

    <div class="text-center pt-4 border-t border-slate-100">
      <button onclick="retakeQuiz()" class="px-6 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl font-semibold text-xs transition">
        <i class="fa-solid fa-rotate-left mr-1"></i> Retake Assessment Quiz
      </button>
    </div>
  `;
}

function retakeQuiz() {
  document.getElementById("quizContainer").classList.remove("hidden");
  document.getElementById("quizResultsContainer").classList.add("hidden");
  document.getElementById("assessmentForm").reset();
}

// --- CAREER EXPLORER ---
function populateCareerDropdowns(careers) {
  const gapSelect = document.getElementById("gapCareerSelect");
  const resumeSelect = document.getElementById("resumeTargetCareer");
  const catFilter = document.getElementById("explorerCategoryFilter");

  if (gapSelect) {
    gapSelect.innerHTML = careers.map(c => `
      <option value="${c.id}">${c.title} (${c.category})</option>
    `).join("");
  }

  if (resumeSelect) {
    resumeSelect.innerHTML = `
      <option value="">-- General ATS Evaluation (No Specific Role) --</option>
      ${careers.map(c => `<option value="${c.id}">${c.title}</option>`).join("")}
    `;
  }

  if (catFilter) {
    const categories = Array.from(new Set(careers.map(c => c.category))).sort();
    catFilter.innerHTML = `
      <option value="">All Categories</option>
      ${categories.map(cat => `<option value="${cat}">${cat}</option>`).join("")}
    `;
  }
}

function populateExplorerGrid(careers) {
  const grid = document.getElementById("explorerGrid");
  if (!grid) return;

  grid.innerHTML = careers.map(c => `
    <div class="glass-card rounded-2xl p-5 border border-slate-200 flex flex-col justify-between">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-[10px] font-bold uppercase tracking-wider text-brand-600 bg-brand-50 px-2 py-0.5 rounded-full border border-brand-200">
            ${c.category}
          </span>
          <span class="text-[11px] font-bold text-emerald-600 flex items-center gap-1">
            <i class="fa-solid fa-arrow-trend-up text-[10px]"></i> ${c.market_outlook.growth_rate}
          </span>
        </div>
        <h3 class="text-base font-bold text-slate-900">${c.title}</h3>
        <p class="text-xs text-slate-500 mt-1 line-clamp-3">${c.description}</p>
        
        <!-- Core Skills -->
        <div class="mt-4">
          <span class="text-[10px] uppercase font-bold text-slate-400 block mb-1">Required Skills:</span>
          <div class="flex flex-wrap gap-1">
            ${c.required_skills.slice(0, 5).map(s => `
              <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 text-[11px] font-medium">${s}</span>
            `).join("")}
            ${c.required_skills.length > 5 ? `<span class="px-1.5 py-0.5 text-slate-400 text-[10px]">+${c.required_skills.length - 5} more</span>` : ''}
          </div>
        </div>
      </div>

      <div class="mt-5 pt-3 border-t border-slate-100 flex items-center justify-between text-xs">
        <span class="text-slate-500">Entry: <strong class="text-slate-800">${c.salaries.entry_inr}</strong></span>
        <button onclick="openCareerModal('${c.id}')" class="px-3 py-1.5 bg-slate-100 hover:bg-brand-50 hover:text-brand-700 text-slate-700 rounded-lg font-semibold transition text-xs">
          Deep Dive →
        </button>
      </div>
    </div>
  `).join("");
}

function filterExplorerCareers() {
  const query = document.getElementById("explorerSearch").value.toLowerCase();
  const category = document.getElementById("explorerCategoryFilter").value;

  const filtered = allCareers.filter(c => {
    const matchesCat = !category || c.category === category;
    const matchesQuery = !query ||
      c.title.toLowerCase().includes(query) ||
      c.description.toLowerCase().includes(query) ||
      c.required_skills.some(s => s.toLowerCase().includes(query));
    return matchesCat && matchesQuery;
  });

  populateExplorerGrid(filtered);
}

// --- CAREER DEEP DIVE MODAL ---
function openCareerModal(careerId) {
  const career = allCareers.find(c => c.id === careerId);
  if (!career) return;

  const modal = document.getElementById("careerModal");
  const content = document.getElementById("modalContent");

  content.innerHTML = `
    <div class="flex items-start justify-between pb-4 border-b border-slate-100 mb-6">
      <div>
        <span class="text-xs font-bold uppercase tracking-wider text-brand-600 bg-brand-50 px-2.5 py-1 rounded-full border border-brand-200">
          ${career.category}
        </span>
        <h2 class="text-2xl font-black text-slate-900 mt-2">${career.title}</h2>
      </div>
      <button onclick="closeModal()" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500 flex items-center justify-center transition">
        <i class="fa-solid fa-xmark text-sm"></i>
      </button>
    </div>

    <!-- Overview -->
    <div class="mb-6">
      <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Career Overview</h4>
      <p class="text-sm text-slate-700 leading-relaxed">${career.overview}</p>
    </div>

    <!-- Salary Grid -->
    <div class="grid grid-cols-3 gap-3 bg-slate-50 p-4 rounded-2xl border border-slate-100 mb-6 text-center text-xs">
      <div>
        <span class="text-slate-400 block text-[10px] uppercase font-bold">Entry Level</span>
        <strong class="text-sm font-extrabold text-slate-900 mt-0.5 block">${career.salaries.entry_inr}</strong>
        <span class="text-[10px] text-slate-400">$${career.salaries.entry_usd.toLocaleString()}/yr</span>
      </div>
      <div>
        <span class="text-slate-400 block text-[10px] uppercase font-bold">Mid Level (3-5 yrs)</span>
        <strong class="text-sm font-extrabold text-brand-600 mt-0.5 block">${career.salaries.mid_inr}</strong>
        <span class="text-[10px] text-slate-400">$${career.salaries.mid_usd.toLocaleString()}/yr</span>
      </div>
      <div>
        <span class="text-slate-400 block text-[10px] uppercase font-bold">Senior Architect</span>
        <strong class="text-sm font-extrabold text-emerald-600 mt-0.5 block">${career.salaries.senior_inr}</strong>
        <span class="text-[10px] text-slate-400">$${career.salaries.senior_usd.toLocaleString()}/yr</span>
      </div>
    </div>

    <!-- 3-Phase Roadmap -->
    <div class="mb-6">
      <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">Structured Learning Roadmap</h4>
      <div class="space-y-3">
        ${career.learning_roadmap.map(phase => `
          <div class="p-3.5 rounded-xl border border-slate-200 bg-slate-50/50 text-xs">
            <span class="font-bold text-brand-600">${phase.phase}</span>: <strong class="text-slate-800">${phase.focus}</strong>
            <p class="text-slate-600 mt-1">${phase.topics.join(", ")}</p>
          </div>
        `).join("")}
      </div>
    </div>

    <!-- Portfolio & Interview -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6 text-xs">
      <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
        <h5 class="font-bold text-slate-800 mb-2 flex items-center gap-1.5">
          <i class="fa-solid fa-code-fork text-brand-600"></i> Recommended Standout Projects
        </h5>
        <ul class="space-y-1.5 text-slate-700">
          ${career.project_ideas.map(p => `<li>• ${p}</li>`).join("")}
        </ul>
      </div>
      <div class="p-4 rounded-xl border border-slate-200 bg-slate-50">
        <h5 class="font-bold text-slate-800 mb-2 flex items-center gap-1.5">
          <i class="fa-solid fa-comments text-amber-500"></i> Core Interview Topics
        </h5>
        <ul class="space-y-1.5 text-slate-700">
          ${career.interview_topics.map(t => `<li>• ${t}</li>`).join("")}
        </ul>
      </div>
    </div>

    <div class="pt-4 border-t border-slate-100 flex justify-end gap-2">
      <button onclick="goToSkillGap('${career.id}'); closeModal();" class="px-4 py-2 bg-brand-600 hover:bg-brand-700 text-white rounded-xl text-xs font-semibold transition">
        Analyze My Skill Gap for this Role
      </button>
    </div>
  `;

  modal.classList.remove("hidden");
}

function closeModal() {
  const modal = document.getElementById("careerModal");
  if (modal) modal.classList.add("hidden");
}

// --- MARKET INSIGHTS & JOB BOARD ---
function populateMarketInsights(marketData) {
  const skillsList = document.getElementById("marketSkillsList");
  const salaryList = document.getElementById("salaryBenchmarksList");

  if (skillsList && marketData.top_in_demand_skills) {
    skillsList.innerHTML = marketData.top_in_demand_skills.slice(0, 5).map(s => `
      <div class="flex items-center justify-between text-xs">
        <div>
          <strong class="text-slate-800">${s.skill}</strong>
          <span class="text-[10px] text-slate-400 block">${s.domain}</span>
        </div>
        <span class="px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 font-bold text-[11px]">${s.growth}</span>
      </div>
    `).join("");
  }

  if (salaryList && marketData.salary_benchmarks) {
    salaryList.innerHTML = marketData.salary_benchmarks.slice(0, 5).map(b => `
      <div class="flex items-center justify-between text-xs">
        <span class="text-slate-700 font-medium">${b.role}</span>
        <span class="font-bold text-slate-900">${b.inr_entry}</span>
      </div>
    `).join("");
  }
}

async function refreshJobMatches() {
  const container = document.getElementById("jobsList");
  if (!container) return;

  const skillsQuery = userSkills.join(",");
  try {
    const res = await fetch(`/api/jobs?skills=${encodeURIComponent(skillsQuery)}`);
    const data = await res.json();
    renderJobs(data.jobs || []);
  } catch (err) {
    console.error("Jobs error:", err);
  }
}

function renderJobs(jobs) {
  const container = document.getElementById("jobsList");
  if (!container) return;

  container.innerHTML = jobs.map(j => {
    const match = j.match_percentage;
    const matchBadge = match !== null ? (
      match >= 60 ? "bg-emerald-50 text-emerald-700 border-emerald-200" :
      match >= 30 ? "bg-amber-50 text-amber-700 border-amber-200" :
      "bg-slate-100 text-slate-500 border-slate-200"
    ) : "bg-slate-100 text-slate-500 border-slate-200";

    return `
      <div class="p-5 rounded-2xl border border-slate-200 bg-white hover:border-brand-500 transition shadow-sm flex flex-col justify-between">
        <div>
          <div class="flex items-start justify-between gap-2 mb-2">
            <div>
              <span class="text-[10px] font-bold text-slate-400 uppercase">${j.company} • ${j.location}</span>
              <h4 class="text-sm font-bold text-slate-900 mt-0.5">${j.title}</h4>
            </div>
            ${match !== null ? `
              <span class="px-2 py-1 rounded-lg text-xs font-bold border ${matchBadge} shrink-0">
                ${match}% Match
              </span>
            ` : ''}
          </div>
          <p class="text-xs text-slate-500 line-clamp-2 mb-3">${j.description}</p>
          <div class="flex flex-wrap gap-1 text-[11px]">
            ${j.skills_required.map(s => {
              const has = j.matched_skills && j.matched_skills.includes(s);
              return `
                <span class="px-2 py-0.5 rounded font-medium ${has ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-slate-100 text-slate-600'}">
                  ${has ? '✓ ' : ''}${s}
                </span>
              `;
            }).join("")}
          </div>
        </div>

        <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs">
          <span class="text-slate-600 font-medium">${j.salary}</span>
          <span class="text-[11px] text-slate-400">${j.type}</span>
        </div>
      </div>
    `;
  }).join("");
}

// --- AI ADVISOR CHAT ---
async function handleChatSubmit(e) {
  if (e) e.preventDefault();
  const input = document.getElementById("chatInput");
  const msg = input.value.trim();
  if (!msg) return;

  appendChatMessage("user", msg);
  input.value = "";

  try {
    const res = await fetch("/api/advisor/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: msg,
        profile: { skills: userSkills, interests: userInterests }
      })
    });

    const data = await res.json();
    appendChatMessage("bot", data.reply, data.title, data.suggested_actions);
  } catch (err) {
    console.error("Chat error:", err);
    appendChatMessage("bot", "Sorry, I encountered an issue generating advice. Please try again.");
  }
}

function sendQuickPrompt(promptText) {
  const input = document.getElementById("chatInput");
  if (input) {
    input.value = promptText;
    handleChatSubmit();
  }
}

function appendChatMessage(sender, text, title = null, actions = []) {
  const history = document.getElementById("chatHistory");
  if (!history) return;

  const isUser = sender === "user";
  const div = document.createElement("div");
  div.className = `flex gap-3 ${isUser ? 'justify-end' : ''}`;

  // Format bold and markdown lines
  const formatted = text
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n\n/g, '<br><br>')
    .replace(/\n/g, '<br>');

  div.innerHTML = `
    ${!isUser ? `
      <div class="w-8 h-8 rounded-lg bg-brand-100 text-brand-700 flex items-center justify-center shrink-0 text-sm">
        <i class="fa-solid fa-robot"></i>
      </div>
    ` : ''}

    <div class="${isUser ? 'chat-bubble-user' : 'chat-bubble-bot'} p-4 rounded-2xl text-xs sm:text-sm max-w-[85%] space-y-2">
      ${title && !isUser ? `<h5 class="font-bold text-slate-900 border-b border-slate-200/60 pb-1">${title}</h5>` : ''}
      <div class="leading-relaxed">${formatted}</div>

      ${actions && actions.length > 0 ? `
        <div class="pt-2 border-t border-slate-200/50 mt-2 flex flex-wrap gap-1.5">
          ${actions.map(act => `
            <span class="px-2 py-0.5 rounded bg-white/80 text-brand-800 text-[10px] font-semibold border border-brand-200 shadow-2xs">
              → ${act}
            </span>
          `).join("")}
        </div>
      ` : ''}
    </div>

    ${isUser ? `
      <div class="w-8 h-8 rounded-lg bg-indigo-600 text-white flex items-center justify-center shrink-0 text-sm">
        <i class="fa-solid fa-user"></i>
      </div>
    ` : ''}
  `;

  history.appendChild(div);
  history.scrollTop = history.scrollHeight;
}

