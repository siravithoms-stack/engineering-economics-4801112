# -*- coding: utf-8 -*-
from problems_data_1 import get_problems_part_1
from problems_data_2 import get_problems_part_2

def get_problems_and_solutions_section():
    all_problems = get_problems_part_1() + get_problems_part_2()
    
    html = '''
<!-- SECTION 4: PROBLEMS AND SOLUTIONS COLLECTION -->
<section id="problems" class="card" style="border-top: 4px solid var(--primary-light);">
    <div class="section-header">
        <div>
            <h2 class="section-title">📝 4. รวมโจทย์และเฉลยละเอียดครบทุกบท (27 Problems & Solutions)</h2>
            <p class="section-desc">รวมโจทย์ แบบฝึกหัด และตัวอย่างคำนวณทั้งหมดจากสไลด์และเอกสาร พร้อมแสดงวิธีทำทีละขั้นตอนอย่างละเอียด</p>
        </div>
        <div style="display:flex; gap:0.5rem; align-items:center;">
            <button class="solution-toggle-btn" onclick="toggleAllSolutions(true)">📂 เปิดเฉลยทั้งหมด</button>
            <button class="solution-toggle-btn" style="background:#64748b;" onclick="toggleAllSolutions(false)">📁 ปิดเฉลยทั้งหมด</button>
        </div>
    </div>

    <!-- Filter & Search Bar -->
    <div class="filter-controls">
        <input type="text" id="problemSearchInput" class="search-box" placeholder="🔍 ค้นหาโจทย์, สูตร, ตัวเลข, หรือหัวข้อ..." oninput="searchProblems()">
        <button class="filter-btn active" onclick="filterCategory('all', this)">ทั้งหมด (27)</button>
        <button class="filter-btn" onclick="filterCategory('cost', this)">ต้นทุน (2)</button>
        <button class="filter-btn" onclick="filterCategory('bep', this)">จุดคุ้มทุน (3)</button>
        <button class="filter-btn" onclick="filterCategory('tvm', this)">ดอกเบี้ย & TVM (9)</button>
        <button class="filter-btn" onclick="filterCategory('pw', this)">มูลค่าปัจจุบัน PW (2)</button>
        <button class="filter-btn" onclick="filterCategory('aw', this)">เงินรายปี AW (4)</button>
        <button class="filter-btn" onclick="filterCategory('irr', this)">อัตราผลตอบแทน IRR (3)</button>
        <button class="filter-btn" onclick="filterCategory('bc', this)">B/C Ratio (1)</button>
        <button class="filter-btn" onclick="filterCategory('replacement', this)">การทดแทน (2)</button>
        <button class="filter-btn" onclick="filterCategory('tax', this)">ภาษี & ค่าเสื่อม (1)</button>
        <button class="filter-btn" onclick="filterCategory('decision', this)">ความเสี่ยง & Decision Tree (1)</button>
    </div>

    <div id="problemsList">
'''
    
    for idx, p in enumerate(all_problems, 1):
        html += f'''
        <div class="problem-card" data-category="{p['cat']}" id="{p['id']}">
            <div class="problem-header" onclick="toggleSolution('{p['id']}')">
                <div class="problem-title-area">
                    <span class="problem-num">ข้อ {idx}</span>
                    <span class="badge badge-primary">{p['cat'].upper()}</span>
                    <span class="problem-title">{p['title']}</span>
                </div>
                <div style="font-size:0.82rem; color:var(--text-muted);">{p['source']}</div>
            </div>
            <div class="problem-body">
                <div class="problem-question">
                    <strong>โจทย์:</strong> {p['q']}
                </div>
                <div>
                    <button class="solution-toggle-btn" id="btn-{p['id']}" onclick="toggleSolution('{p['id']}')">
                        👁️ ดูเฉลยและวิธีทำละเอียด
                    </button>
                </div>
                <div class="solution-content" id="sol-{p['id']}">
                    {p['sol']}
                </div>
            </div>
        </div>
'''

    html += '''
    </div>
</section>
'''
    return html
