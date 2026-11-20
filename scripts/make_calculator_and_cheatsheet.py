# -*- coding: utf-8 -*-

def get_calculator_and_cheatsheet_section():
    return '''
<!-- SECTION 3: INTERACTIVE FACTOR CALCULATOR & CHEAT SHEET -->
<section id="calculator" class="card" style="border-top: 4px solid var(--accent);">
    <div class="section-header">
        <div>
            <h2 class="section-title">🧮 3. เครื่องคำนวณแฟกเตอร์ดอกเบี้ยและอัตราดอกเบี้ยแท้จริง (Interactive Calculator)</h2>
            <p class="section-desc">คำนวณค่า Compound Interest Factors และ Effective Interest Rate ได้แบบทันทีโดยไม่ต้องเปิดเล่มตาราง</p>
        </div>
        <span class="badge badge-warning" style="font-size:0.9rem; padding:0.4rem 0.8rem;">เครื่องมือช่วยคำนวณอัตโนมัติ</span>
    </div>

    <!-- Calculator Grid -->
    <div class="calculator-container">
        <h3 style="font-family:'Kanit'; color:var(--primary-dark); margin-bottom:0.25rem;">⚡ เครื่องมือคำนวณแฟกเตอร์ทางการเงิน (Financial Factor Engine)</h3>
        <p style="font-size:0.88rem; color:var(--text-muted);">ป้อนอัตราดอกเบี้ยต่องวด ($i\\%$) และจำนวนงวด ($n$) ระบบจะคำนวณค่าแฟกเตอร์มาตรฐานทั้ง 8 ตัวให้ทันที</p>
        
        <div class="calc-grid">
            <div class="calc-input-group">
                <label for="calc-i">อัตราดอกเบี้ยต่องวด $i$ (%)</label>
                <input type="number" id="calc-i" value="8" step="0.25" min="0.01" max="100" oninput="calculateFactors()">
            </div>
            <div class="calc-input-group">
                <label for="calc-n">จำนวนงวด $n$ (ปี หรือ งวด)</label>
                <input type="number" id="calc-n" value="10" step="1" min="1" max="120" oninput="calculateFactors()">
            </div>
            <div class="calc-input-group">
                <label for="calc-val">มูลค่าเงินฐาน (Base Amount, บาท)</label>
                <input type="number" id="calc-val" value="10000" step="100" min="0" oninput="calculateFactors()">
            </div>
        </div>

        <div class="calc-results-box">
            <div class="calc-res-item">
                <div class="calc-res-label">(F/P, i%, n) Compound Amount</div>
                <div class="calc-res-val" id="res-fp">2.1589</div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">$F = P \\times (F/P)$</div>
            </div>
            <div class="calc-res-item">
                <div class="calc-res-label">(P/F, i%, n) Present Worth</div>
                <div class="calc-res-val" id="res-pf">0.4632</div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">$P = F \\times (P/F)$</div>
            </div>
            <div class="calc-res-item">
                <div class="calc-res-label">(P/A, i%, n) Series Present</div>
                <div class="calc-res-val" id="res-pa">6.7101</div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">$P = A \\times (P/A)$</div>
            </div>
            <div class="calc-res-item">
                <div class="calc-res-label">(A/P, i%, n) Capital Recovery</div>
                <div class="calc-res-val" id="res-ap">0.1490</div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">$A = P \\times (A/P)$</div>
            </div>
            <div class="calc-res-item">
                <div class="calc-res-label">(F/A, i%, n) Series Compound</div>
                <div class="calc-res-val" id="res-fa">14.4866</div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">$F = A \\times (F/A)$</div>
            </div>
            <div class="calc-res-item">
                <div class="calc-res-label">(A/F, i%, n) Sinking Fund</div>
                <div class="calc-res-val" id="res-af">0.0690</div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">$A = F \\times (A/F)$</div>
            </div>
            <div class="calc-res-item">
                <div class="calc-res-label">(P/G, i%, n) Gradient Present</div>
                <div class="calc-res-val" id="res-pg">25.9287</div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">$P = G \\times (P/G)$</div>
            </div>
            <div class="calc-res-item">
                <div class="calc-res-label">(A/G, i%, n) Gradient Uniform</div>
                <div class="calc-res-val" id="res-ag">3.8713</div>
                <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">$A = G \\times (A/G)$</div>
            </div>
        </div>

        <div style="margin-top:1.5rem; padding-top:1.25rem; border-top:1px solid #cbd5e1;">
            <h4 style="font-family:'Kanit'; font-size:1.05rem; color:var(--primary-dark); margin-bottom:0.5rem;">🔄 แปลงอัตราดอกเบี้ยที่ระบุเป็นอัตราดอกเบี้ยแท้จริง (Nominal to Effective Rate Converter)</h4>
            <div class="calc-grid">
                <div class="calc-input-group">
                    <label for="calc-nom-r">อัตราดอกเบี้ยต่อปี $r$ (Nominal Rate %)</label>
                    <input type="number" id="calc-nom-r" value="6" step="0.25" min="0.1" oninput="calculateEffective()">
                </div>
                <div class="calc-input-group">
                    <label for="calc-comp-m">ความถี่ในการทบต้นต่อปี $m$</label>
                    <select id="calc-comp-m" onchange="calculateEffective()">
                        <option value="1">ปีละ 1 ครั้ง (Annually, m=1)</option>
                        <option value="2">ปีละ 2 ครั้ง (Semiannually, m=2)</option>
                        <option value="4">ปีละ 4 ครั้ง (Quarterly, m=4)</option>
                        <option value="12" selected>ปีละ 12 ครั้ง (Monthly, m=12)</option>
                        <option value="24">ปีละ 24 ครั้ง (Semimonthly, m=24)</option>
                        <option value="365">ทุกวัน (Daily, m=365)</option>
                        <option value="cont">ทบต้นต่อเนื่อง (Continuously, m=∞)</option>
                    </select>
                </div>
                <div class="calc-input-group">
                    <label>อัตราดอกเบี้ยที่แท้จริง $i_e$ (Effective Rate %)</label>
                    <div id="res-eff-rate" style="font-size:1.4rem; font-weight:700; color:var(--primary); font-family:'JetBrains Mono'; padding-top:0.35rem;">6.1678%</div>
                </div>
            </div>
        </div>
    </div>
</section>
'''
