# -*- coding: utf-8 -*-

def get_footer_and_js():
    return r'''
<!-- SECTION 5: EXAM TIPS & PITFALLS -->
<section id="tips" class="card" style="border-top: 4px solid var(--danger);">
    <div class="section-header">
        <div>
            <h2 class="section-title">🎯 5. สรุปกับดักข้อสอบและเทคนิคทำคะแนนเต็ม (Exam Master Tips)</h2>
            <p class="section-desc">รวมจุดที่นักศึกษามักพลาดบ่อยที่สุดในห้องสอบ และข้อควรระวังสำคัญ</p>
        </div>
        <span class="badge badge-danger" style="font-size:0.86rem; padding:0.4rem 0.85rem;">ข้อควรระวังสูงสุด</span>
    </div>

    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:1.25rem;">
        <div style="background:#fff1f2; padding:1.35rem; border-radius:14px; border-left:4px solid var(--danger);">
            <h4 style="color:#991b1b; font-family:'Kanit'; margin-bottom:0.45rem;">🚫 1. กับดักต้นทุนจม (Sunk Cost Trap)</h4>
            <p style="font-size:0.9rem; color:#4c0519; line-height:1.7;">
                ในโจทย์การทดแทนทรัพย์สิน (Replacement) ราคาที่ซื้อเครื่องจักรเดิมมาเมื่อหลายปีก่อน และค่าเสื่อมราคาสะสมทางบัญชี <strong>ห้ามนำมาคิดเด็ดขาด!</strong> ต้นทุนที่แท้จริงของทรัพย์สินเดิมคือ "ราคาตลาดปัจจุบันที่ขายได้ทันที" (Market / Trade-in Value) เท่านั้น
            </p>
        </div>

        <div style="background:#fffbeb; padding:1.35rem; border-radius:14px; border-left:4px solid var(--accent);">
            <h4 style="color:#92400e; font-family:'Kanit'; margin-bottom:0.45rem;">🚫 2. กับดักการเลือกโครงการด้วย IRR สูงสุด</h4>
            <p style="font-size:0.9rem; color:#78350f; line-height:1.7;">
                สำหรับโครงการที่เลือกได้เพียงทางเลือกเดียว (Mutually Exclusive) <strong>ห้ามเลือกโครงการที่มี IRR สูงสุดตรงๆ เด็ดขาด!</strong> ต้องเรียงลำดับเงินลงทุนและทำ Incremental Analysis ($\Delta$IRR) เสมอ เพราะโครงการขนาดใหญ่กว่าอาจสร้างมูลค่าความมั่งคั่ง (NPW) สูงกว่าแม้ IRR เฉลี่ยจะต่ำกว่า
            </p>
        </div>

        <div style="background:#eff6ff; padding:1.35rem; border-radius:14px; border-left:4px solid var(--primary-light);">
            <h4 style="color:#1e40af; font-family:'Kanit'; margin-bottom:0.45rem;">🚫 3. ครน. (LCM) ในวิธี PW vs วิธี AW</h4>
            <p style="font-size:0.9rem; color:#1e3a8a; line-height:1.7;">
                หากเปรียบเทียบโครงการที่มีอายุไม่เท่ากันด้วย <strong>Present Worth (PW)</strong> <em>ต้องหา ครน. (LCM) ของอายุขัยก่อนเสมอ</em> แต่ถ้าเปรียบเทียบด้วย <strong>Annual Worth (AW)</strong> <em>ไม่ต้องหา ครน.</em> สามารถคิด AW จากอายุของแต่ละโครงการได้ทันที
            </p>
        </div>

        <div style="background:#f0fdf4; padding:1.35rem; border-radius:14px; border-left:4px solid var(--success);">
            <h4 style="color:#166534; font-family:'Kanit'; margin-bottom:0.45rem;">🚫 4. การบวกกลับค่าเสื่อมราคาใน CFAT</h4>
            <p style="font-size:0.9rem; color:#14532d; line-height:1.7;">
                ค่าเสื่อมราคาเป็นค่าใช้จ่ายที่ไม่ใช่เงินสด (Non-cash expense) ใช้เพื่อหักลดหย่อนภาษีเท่านั้น เมื่อคำนวณหากระแสเงินสดสุทธิหลังหักภาษี (CFAT) <strong>ต้องบวกค่าเสื่อมราคากลับเข้าไปในกำไรสุทธิหลังหักภาษีเสมอ</strong> ($CFAT = NPAT + D$)
            </p>
        </div>
    </div>
</section>

    </main>
</div>

<footer>
    <div style="max-width:900px; margin:0 auto;">
        <h3 style="font-family:'Kanit'; color:#FFFFFF; margin-bottom:0.5rem; font-size:1.25rem;">การวิเคราะห์ทางเศรษฐศาสตร์วิศวกรรม (Engineering Economic Analysis)</h3>
        <p style="font-size:0.9rem; margin-bottom:1.2rem; opacity:0.85;">คู่มือสรุปเนื้อหาบทเรียน คลังสูตร เครื่องคำนวณ และเฉลยแบบฝึกหัด จัดทำเพื่อการศึกษาและทบทวนความรู้ทางวิศวกรรม</p>
        <div style="display:flex; justify-content:center; gap:1.5rem; flex-wrap:wrap; font-size:0.85rem; margin-bottom:1.5rem; color:#CBD5E1;">
            <span>📁 เอกสารอ้างอิง: 9 ไฟล์</span>
            <span>📖 ครอบคลุม: 10 บทเรียน</span>
            <span>📝 เฉลยละเอียด: 27 ข้อ</span>
            <span>⚡ คำนวณอัตโนมัติ & MathJax</span>
        </div>
        <p style="font-size:0.8rem; color:#64748B;">© 2026 Engineering Economics Review Project. Executive Study Edition.</p>
    </div>
</footer>

<button class="back-to-top" id="backToTopBtn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="กลับขึ้นด้านบน">↑</button>
<div class="toast-notice" id="toastNotice"></div>

<!-- Interactive Scripts -->
<script>
let activeCategory = 'all';
let completedProblems = new Set();
const STORAGE_KEYS = {
    theme: 'eea_theme_v2',
    fontScale: 'eea_font_scale_v2',
    done: 'eea_completed_problems_v2'
};

function showToast(msg) {
    const toast = document.getElementById('toastNotice');
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(window._toastTimer);
    window._toastTimer = setTimeout(() => toast.classList.remove('show'), 2200);
}

// Theme & Font Size Controls
function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    const btn = document.getElementById('themeToggleBtn');
    if (btn) btn.textContent = theme === 'dark' ? '☀️ โหมดสว่าง' : '🌙 โหมดมืด';
    try { localStorage.setItem(STORAGE_KEYS.theme, theme); } catch (e) {}
}

function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'light';
    applyTheme(current === 'dark' ? 'light' : 'dark');
}

function adjustFontSize(delta) {
    let current = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--font-scale')) || 1;
    let next = Math.min(1.24, Math.max(0.86, +(current + delta).toFixed(2)));
    document.documentElement.style.setProperty('--font-scale', next);
    try { localStorage.setItem(STORAGE_KEYS.fontScale, next); } catch (e) {}
    showToast('ขนาดตัวอักษร ' + Math.round(next * 100) + '%');
}

// 1. Enhanced Calculator Engine (shows both factor AND Baht value + click-to-copy)
function formatBaht(val) {
    return val.toLocaleString('th-TH', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' บาท';
}

function calculateFactors() {
    const i_pct = parseFloat(document.getElementById('calc-i').value) || 8;
    const n = parseInt(document.getElementById('calc-n').value) || 10;
    const baseVal = parseFloat(document.getElementById('calc-val').value) || 10000;
    const i = i_pct / 100;

    const fp = Math.pow(1 + i, n);
    const pf = 1 / fp;
    const fa = (fp - 1) / i;
    const af = i / (fp - 1);
    const pa = (fp - 1) / (i * fp);
    const ap = (i * fp) / (fp - 1);
    const pg = (1 / i) * (pa - (n * pf));
    const ag = (1 / i) - (n / (fp - 1));

    const results = [
        ['res-fp', fp], ['res-pf', pf], ['res-pa', pa], ['res-ap', ap],
        ['res-fa', fa], ['res-af', af], ['res-pg', pg], ['res-ag', ag]
    ];

    results.forEach(([id, factor]) => {
        const el = document.getElementById(id);
        if (!el) return;
        el.innerText = factor.toFixed(4);
        const parent = el.closest('.calc-res-item');
        if (parent) {
            let moneyEl = parent.querySelector('.calc-res-money');
            if (!moneyEl) {
                moneyEl = document.createElement('div');
                moneyEl.className = 'calc-res-money';
                parent.appendChild(moneyEl);
                parent.title = 'คลิกเพื่อคัดลอกค่าแฟกเตอร์';
                parent.addEventListener('click', () => {
                    const valText = el.innerText;
                    if (navigator.clipboard) {
                        navigator.clipboard.writeText(valText);
                        showToast('คัดลอกค่าแฟกเตอร์ ' + valText + ' แล้ว');
                    }
                });
            }
            moneyEl.textContent = '≈ ' + formatBaht(baseVal * factor);
        }
    });
}

function calculateEffective() {
    const r_pct = parseFloat(document.getElementById('calc-nom-r').value) || 6;
    const m_val = document.getElementById('calc-comp-m').value;
    const r = r_pct / 100;
    let ie = 0;

    if (m_val === 'cont') {
        ie = Math.exp(r) - 1;
    } else {
        const m = parseFloat(m_val);
        ie = Math.pow(1 + (r / m), m) - 1;
    }

    document.getElementById('res-eff-rate').innerText = (ie * 100).toFixed(4) + '%';
}

// 2. Accordion Toggles
function toggleSolution(id) {
    const solEl = document.getElementById('sol-' + id);
    const btnEl = document.getElementById('btn-' + id);
    const cardEl = document.getElementById(id);
    if (!solEl) return;

    if (solEl.classList.contains('active')) {
        solEl.classList.remove('active');
        if (cardEl) cardEl.classList.remove('is-open');
        if (btnEl) btnEl.innerHTML = '👁️ ดูเฉลยและวิธีทำละเอียด';
    } else {
        solEl.classList.add('active');
        if (cardEl) cardEl.classList.add('is-open');
        if (btnEl) btnEl.innerHTML = '🔼 ซ่อนเฉลย';
        if (window.MathJax && window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise([solEl]);
        }
    }
}

function toggleAllSolutions(show) {
    const solutions = document.querySelectorAll('.solution-content');
    const buttons = document.querySelectorAll('.solution-toggle-btn');
    const cards = document.querySelectorAll('.problem-card');
    solutions.forEach(sol => sol.classList.toggle('active', show));
    cards.forEach(card => card.classList.toggle('is-open', show));
    buttons.forEach(btn => {
        if (btn.id.startsWith('btn-')) {
            btn.innerHTML = show ? '🔼 ซ่อนเฉลย' : '👁️ ดูเฉลยและวิธีทำละเอียด';
        }
    });
    if (show && window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise();
    }
}

// 3. Unified Category Filter + Live Search
function applyProblemFilters() {
    const input = document.getElementById('problemSearchInput');
    const q = input ? input.value.toLowerCase().trim() : '';
    const cards = document.querySelectorAll('.problem-card');
    let visibleCount = 0;

    cards.forEach(card => {
        const itemCat = card.getAttribute('data-category');
        const matchesCat = (activeCategory === 'all') ||
                           (activeCategory === 'done' && card.classList.contains('completed')) ||
                           (activeCategory === 'todo' && !card.classList.contains('completed')) ||
                           (itemCat === activeCategory);
        const matchesQuery = !q || card.innerText.toLowerCase().includes(q);
        const show = matchesCat && matchesQuery;
        card.style.display = show ? 'block' : 'none';
        if (show) visibleCount++;
    });

    const countEl = document.getElementById('problemResultCount');
    if (countEl) countEl.textContent = 'แสดง ' + visibleCount + ' จาก ' + cards.length + ' ข้อ';
    const emptyEl = document.getElementById('problemsEmptyState');
    if (emptyEl) emptyEl.style.display = visibleCount === 0 ? 'block' : 'none';
}

function filterCategory(cat, btn) {
    activeCategory = cat;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    applyProblemFilters();
}

function searchProblems() {
    applyProblemFilters();
}

// 4. Study Progress Tracking (localStorage)
function loadCompletedProblems() {
    try {
        const saved = JSON.parse(localStorage.getItem(STORAGE_KEYS.done) || '[]');
        completedProblems = new Set(saved);
    } catch (e) {
        completedProblems = new Set();
    }
}

function saveCompletedProblems() {
    try {
        localStorage.setItem(STORAGE_KEYS.done, JSON.stringify(Array.from(completedProblems)));
    } catch (e) {}
}

function updateProgressUI() {
    const total = document.querySelectorAll('.problem-card').length || 27;
    const doneCount = completedProblems.size;
    const pct = Math.round((doneCount / total) * 100);

    const sideText = document.getElementById('sidebarProgressText');
    const sideBar = document.getElementById('sidebarProgressBar');
    const topText = document.getElementById('problemsProgressText');
    if (sideText) sideText.textContent = doneCount + ' / ' + total + ' (' + pct + '%)';
    if (sideBar) sideBar.style.width = pct + '%';
    if (topText) topText.textContent = 'ทำแล้ว ' + doneCount + ' / ' + total + ' ข้อ (' + pct + '%)';
}

function enhanceProblemsUI() {
    const problemsSection = document.getElementById('problems');
    const filterControls = problemsSection ? problemsSection.querySelector('.filter-controls') : null;
    if (filterControls && !filterControls.parentElement.classList.contains('problems-toolbar')) {
        const toolbar = document.createElement('div');
        toolbar.className = 'problems-toolbar';
        filterControls.parentNode.insertBefore(toolbar, filterControls);
        toolbar.appendChild(filterControls);

        const statusBar = document.createElement('div');
        statusBar.className = 'problems-status-bar';
        statusBar.innerHTML = '<span id="problemResultCount">แสดง 27 จาก 27 ข้อ</span><span id="problemsProgressText" style="font-weight:600; color:var(--secondary);">ทำแล้ว 0 / 27 ข้อ (0%)</span>';
        toolbar.insertAdjacentElement('afterend', statusBar);
    }

    const listEl = document.getElementById('problemsList');
    if (listEl && !document.getElementById('problemsEmptyState')) {
        const empty = document.createElement('div');
        empty.id = 'problemsEmptyState';
        empty.className = 'empty-state';
        empty.innerHTML = '<div style="font-size:1.8rem; margin-bottom:0.4rem;">🔍</div><strong>ไม่พบโจทย์ที่ตรงกับคำค้นหา</strong><p style="font-size:0.88rem; margin-top:0.25rem;">ลองเปลี่ยนคำค้นหาหรือเลือกหมวดหมู่ "ทั้งหมด"</p>';
        listEl.appendChild(empty);
    }

    document.querySelectorAll('.problem-card').forEach(card => {
        const id = card.id;
        const header = card.querySelector('.problem-header');
        if (!header) return;

        const sourceEl = header.children[1];
        const rightWrap = document.createElement('div');
        rightWrap.className = 'problem-header-right';
        if (sourceEl) rightWrap.appendChild(sourceEl);

        const doneBtn = document.createElement('button');
        doneBtn.type = 'button';
        doneBtn.className = 'done-check-btn';
        const isDone = completedProblems.has(id);
        if (isDone) {
            card.classList.add('completed');
            doneBtn.classList.add('is-done');
            doneBtn.textContent = '✓ ทำแล้ว';
        } else {
            doneBtn.textContent = '○ ทำเครื่องหมาย';
        }
        doneBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (completedProblems.has(id)) {
                completedProblems.delete(id);
                card.classList.remove('completed');
                doneBtn.classList.remove('is-done');
                doneBtn.textContent = '○ ทำเครื่องหมาย';
            } else {
                completedProblems.add(id);
                card.classList.add('completed');
                doneBtn.classList.add('is-done');
                doneBtn.textContent = '✓ ทำแล้ว';
            }
            saveCompletedProblems();
            updateProgressUI();
        });
        rightWrap.appendChild(doneBtn);

        const chev = document.createElement('span');
        chev.className = 'chevron-icon';
        chev.textContent = '▾';
        rightWrap.appendChild(chev);

        header.appendChild(rightWrap);
    });

    updateProgressUI();
    applyProblemFilters();
}

// 5. Auto-build Chapter Quick-Jump Pills & Sidebar Sub-TOC
function buildChapterNavigation() {
    const theorySec = document.getElementById('theory');
    if (!theorySec) return;
    const chapterCards = theorySec.querySelectorAll(':scope > .card');
    const subToc = document.getElementById('chapterSubToc');

    const pillsBar = document.createElement('div');
    pillsBar.className = 'chapter-pills-bar';

    chapterCards.forEach((card, idx) => {
        const chapId = 'chapter-' + (idx + 1);
        card.id = chapId;
        const h3 = card.querySelector('h3');
        const fullTitle = h3 ? h3.textContent.trim() : ('บทที่ ' + (idx + 1));
        const shortLabel = fullTitle.split('(')[0].trim();

        const pill = document.createElement('a');
        pill.href = '#' + chapId;
        pill.className = 'chapter-pill';
        pill.textContent = shortLabel;
        pillsBar.appendChild(pill);

        if (subToc) {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = '#' + chapId;
            a.className = 'toc-sublink';
            a.textContent = shortLabel;
            a.title = fullTitle;
            li.appendChild(a);
            subToc.appendChild(li);
        }
    });

    const header = theorySec.querySelector('.section-header');
    if (header) header.insertAdjacentElement('afterend', pillsBar);
}

// 6. Scroll Progress, Back-to-Top, and Scroll-Spy
function initScrollBehaviors() {
    const progressBar = document.getElementById('readingProgress');
    const backBtn = document.getElementById('backToTopBtn');
    const sections = ['files', 'theory', 'calculator', 'problems', 'tips']
        .map(id => document.getElementById(id))
        .filter(Boolean);

    function onScroll() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const pct = docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0;
        if (progressBar) progressBar.style.width = pct + '%';
        if (backBtn) backBtn.classList.toggle('visible', scrollTop > 420);

        let activeId = sections[0] ? sections[0].id : '';
        for (const sec of sections) {
            if (sec.getBoundingClientRect().top <= 140) {
                activeId = sec.id;
            }
        }
        document.querySelectorAll('.toc-link').forEach(link => {
            link.classList.toggle('active', link.getAttribute('data-section') === activeId);
        });
        document.querySelectorAll('#topNavMenu .nav-link').forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === '#' + activeId);
        });
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
}

// Initialize on Load
document.addEventListener('DOMContentLoaded', () => {
    try {
        const savedTheme = localStorage.getItem(STORAGE_KEYS.theme);
        if (savedTheme) applyTheme(savedTheme);
        const savedScale = localStorage.getItem(STORAGE_KEYS.fontScale);
        if (savedScale) document.documentElement.style.setProperty('--font-scale', savedScale);
    } catch (e) {}

    loadCompletedProblems();
    calculateFactors();
    calculateEffective();
    buildChapterNavigation();
    enhanceProblemsUI();
    initScrollBehaviors();
});
</script>

</body>
</html>
'''
