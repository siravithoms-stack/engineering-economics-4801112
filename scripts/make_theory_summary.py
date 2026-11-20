# -*- coding: utf-8 -*-

def get_theory_summary_section():
    return '''
<!-- SECTION 2: COMPREHENSIVE THEORY SUMMARY -->
<section id="theory" class="card" style="border-top: 4px solid var(--secondary);">
    <div class="section-header">
        <div>
            <h2 class="section-title">📚 2. สรุปเข้มเนื้อหา 10 บทหลัก (Core Engineering Economics Knowledge)</h2>
            <p class="section-desc">รวบรวมทฤษฎี หลักการสำคัญ สูตรคำนวณ และกฎการตัดสินใจทางวิศวกรรมที่จำเป็นสำหรับการวิเคราะห์และทำข้อสอบ</p>
        </div>
        <span class="badge badge-secondary" style="font-size:0.9rem; padding:0.4rem 0.8rem;">10 โมดูลเนื้อหาครบวงจร</span>
    </div>

    <!-- MODULE 1 -->
    <div class="card" style="background:#fafafa; border-left: 4px solid var(--primary);">
        <h3 style="color:var(--primary); font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 1: มโนทัศน์พื้นฐานและพฤติกรรมต้นทุน (Cost Concepts & Cost Behavior)</h3>
        <p>เศรษฐศาสตร์วิศวกรรมคือศาสตร์ที่นำหลักการทางเศรษฐศาสตร์มาประยุกต์ใช้เพื่อเปรียบเทียบประสิทธิภาพ ความคุ้มค่า และช่วยวิศวกรในการตัดสินใจเลือกโครงการลงทุนที่ดีที่สุด</p>
        
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:1rem; margin:1rem 0;">
            <div style="background:white; padding:1rem; border-radius:8px; border:1px solid #e2e8f0;">
                <h5 style="color:var(--primary-dark); font-weight:600;">1. การจำแนกประเภทต้นทุน</h5>
                <ul style="font-size:0.88rem; padding-left:1.2rem; margin-top:0.35rem;">
                    <li><strong>ต้นทุนคงที่ (Fixed Cost - FC):</strong> ต้นทุนที่ไม่แปรผันตามปริมาณผลผลิตในระยะสั้น เช่น ค่าเช่า, เงินเดือนฝ่ายบริหาร, ค่าเสื่อมราคาอาคาร</li>
                    <li><strong>ต้นทุนผันแปร (Variable Cost - VC):</strong> ต้นทุนที่เปลี่ยนแปลงตามปริมาณการผลิตโดยตรง เช่น ค่าวัตถุดิบ, ค่าแรงงานทางตรง, ค่าพลังงานในสายการผลิต</li>
                    <li><strong>ต้นทุนรวม (Total Cost - TC):</strong> $TC = FC + VC = FC + v \cdot N$ (เมื่อ $v$ คือต้นทุนผันแปรต่อหน่วย, $N$ คือปริมาณการผลิต)</li>
                    <li><strong>ต้นทุนเฉลี่ยต่อหน่วย (Average Cost - AC):</strong> $AC = TC / N = (FC / N) + v$ (เมื่อผลิตมากขึ้น $AC$ จะลดลงเนื่องจาก Economy of Scale)</li>
                </ul>
            </div>
            <div style="background:white; padding:1rem; border-radius:8px; border:1px solid #e2e8f0;">
                <h5 style="color:var(--primary-dark); font-weight:600;">2. ต้นทุนพิเศษในการตัดสินใจ</h5>
                <ul style="font-size:0.88rem; padding-left:1.2rem; margin-top:0.35rem;">
                    <li><strong>ต้นทุนจม (Sunk Cost):</strong> เงินที่จ่ายไปแล้วในอดีต ไม่สามารถเรียกคืนได้ <em>กฎเหล็ก: ห้ามนำมาคิดในการตัดสินใจเลือกโครงการในอนาคต!</em></li>
                    <li><strong>ต้นทุนค่าเสียโอกาส (Opportunity Cost):</strong> มูลค่าของผลประโยชน์สูงสุดที่สูญเสียไปจากการเลือกทางเลือกหนึ่งแทนที่จะเลือกอีกทางเลือกหนึ่ง</li>
                    <li><strong>ต้นทุนส่วนเพิ่ม (Marginal Cost - MC):</strong> ต้นทุนที่เพิ่มขึ้นเมื่อผลิตสินค้าเพิ่มขึ้นอีก 1 หน่วย ($MC = d(TC)/dN$)</li>
                </ul>
            </div>
        </div>

        <div class="formula-box">
            <div class="formula-title">📐 วิธีการแยกพฤติกรรมต้นทุน (Cost Separation Methods)</div>
            <p><strong>1) วิธีสูง-ต่ำ (High-Low Method):</strong> ใช้ข้อมูลจุดที่ปริมาณการผลิตสูงสุดและต่ำสุด</p>
            $$v = \\frac{TC_{high} - TC_{low}}{N_{high} - N_{low}}, \\quad FC = TC_{high} - v(N_{high}) = TC_{low} - v(N_{low})$$
            <p style="margin-top:0.5rem;"><strong>2) วิธีสมการถดถอยเชิงเส้น (Least Squares Regression):</strong> กำหนดสมการต้นทุน $Y = a + bX$ โดยที่ $a = FC$, $b = v$</p>
            $$b = \\frac{n\\sum XY - \\sum X \\sum Y}{n\\sum X^2 - (\\sum X)^2}, \\quad a = \\bar{Y} - b\\bar{X}$$
        </div>
    </div>

    <!-- MODULE 2 -->
    <div class="card" style="background:#fafafa; border-left: 4px solid var(--secondary);">
        <h3 style="color:var(--secondary); font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 2: การวิเคราะห์จุดคุ้มทุน (Break-Even Analysis)</h3>
        <p>จุดคุ้มทุนคือระดับกิจกรรมหรือปริมาณการผลิตที่ทำให้รายได้รวม (Total Revenue - TR) เท่ากับต้นทุนรวม (Total Cost - TC) พอดี ส่งผลให้ผลกำไรสุทธิเป็นศูนย์ ($\Pi = 0$)</p>

        <div class="formula-box">
            <div class="formula-title">📐 สูตรจุดคุ้มทุนผลิตภัณฑ์เดี่ยว (Single-Product Break-Even)</div>
            $$TR = p \\cdot N, \\quad TC = FC + v \\cdot N$$
            $$\\text{จุดคุ้มทุน (หน่วย): } N^* = \\frac{FC}{p - v} = \\frac{FC}{MC}$$
            $$\\text{สมการกำไร: } \\Pi = TR - TC = N(p - v) - FC$$
            $$\\text{ปริมาณผลิตเพื่อให้ได้กำไรตามเป้าหมาย } \\Pi: N = \\frac{FC + \\Pi}{p - v}$$
            <p style="font-size:0.85rem; color:#0f766e; margin-top:0.3rem;">*โดยที่ $p$ = ราคาขายต่อหน่วย, $v$ = ต้นทุนผันแปรต่อหน่วย, $(p - v) = MC$ = ส่วนผลได้ต่อหน่วย (Contribution Margin per unit)</p>
        </div>

        <div class="formula-box" style="background:#fefce8; border-color:var(--accent);">
            <div class="formula-title" style="color:#b45309;">📊 จุดคุ้มทุนผลิตภัณฑ์หลายชนิด (Multi-Product Break-Even Analysis)</div>
            <p>กรณีโรงงานผลิตสินค้าหลายชนิดที่ไม่สามารถรวมจำนวนหน่วยได้ตรงๆ ต้องวิเคราะห์ผ่านสัดส่วนรายได้และ <strong>อัตราร้อยละส่วนผลได้ถ่วงน้ำหนัก (Average Margin Contribution - AMC)</strong>:</p>
            $$MS_i = \\frac{p_i - v_i}{p_i} = \\frac{MC_i}{p_i} \\quad (\\text{\\% ส่วนผลได้ต่อราคาขายของสินค้าแต่ละชนิด})$$
            $$IS_i = \\frac{R_i}{R_{total}} \\quad (\\text{สัดส่วนยอดขายของสินค้าแต่ละชนิดเทียบยอดขายรวม})$$
            $$AMC = \\sum_{i=1}^k (IS_i \\times MS_i) = \\frac{\\sum R_i \\cdot MS_i}{R_{total}} \\quad (\\text{ส่วนผลได้เฉลี่ยถ่วงน้ำหนัก})$$
            $$\\text{ยอดขายรวม ณ จุดคุ้มทุน (บาท): } R^* = \\frac{FC}{AMC}$$
        </div>

        <div class="callout-box callout-warning">
            <h5 style="color:#92400e; font-weight:600;">⚠️ ข้อสังเกตสำคัญในการตัดสินใจยกเลิกผลิตภัณฑ์ที่ขาดทุน:</h5>
            <p style="font-size:0.9rem;">การที่สินค้าชนิดหนึ่งมีตัวเลขกำไรติดลบ (ขาดทุนทางบัญชี) ไม่ได้แปลว่าควรยกเลิกการผลิตทันที! <strong>ตราบใดที่ส่วนผลได้ ($MS_i$ หรือ $p_i - v_i$) ยังเป็นบวก</strong> สินค้านั้นยังช่วยแบกรับต้นทุนคงที่ (FC) ส่วนกลาง หากยกเลิกไปโดยที่ FC ไม่ได้ลดลงตาม จะทำให้กำไรสุทธิรวมของบริษัทลดลงทันที (ดูตัวอย่างในโจทย์ข้อ 5)</p>
        </div>
    </div>

    <!-- MODULE 3 -->
    <div class="card" style="background:#fafafa; border-left: 4px solid var(--accent);">
        <h3 style="color:var(--accent); font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 3: มูลค่าของเงินตามเวลาและอัตราดอกเบี้ย (Time Value of Money & TVM Factors)</h3>
        <p>เงิน 1 บาทในวันนี้มีค่ามากกว่าเงิน 1 บาทในอนาคตเสมอ เนื่องจากความสามารถในการสร้างผลตอบแทนจากการลงทุน (Earning Power) และผลกระทบจากอัตราเงินเฟ้อ</p>

        <div class="formula-box">
            <div class="formula-title">📐 ดอกเบี้ยเชิงเดี่ยว vs ดอกเบี้ยทบต้น (Simple vs Compound Interest)</div>
            <p><strong>ดอกเบี้ยเชิงเดี่ยว (Simple Interest):</strong> $I = P \\cdot i \\cdot n \\implies F = P(1 + in)$</p>
            <p><strong>ดอกเบี้ยทบต้น (Compound Interest):</strong> คิดดอกเบี้ยบนดอกเบี้ยของงวดก่อนหน้า $F = P(1 + i)^n$</p>
            <p><strong>อัตราดอกเบี้ยแท้จริง (Effective Interest Rate, $i_e$):</strong> เมื่ออัตราดอกเบี้ยที่ระบุคือ $r$ ต่อปี และทบต้น $m$ ครั้งต่อปี:</p>
            $$i_e = \\left(1 + \\frac{r}{m}\\right)^m - 1, \\quad \\text{ทบต้นต่อเนื่อง (Continuous Compounding): } i_e = e^r - 1$$
        </div>

        <div class="data-table-container">
            <table class="data-table">
                <thead>
                    <tr>
                        <th>แฟกเตอร์ (Factor)</th>
                        <th>สัญลักษณ์ย่อ</th>
                        <th>ชื่อเต็ม (Factor Name)</th>
                        <th>สมการคำนวณ (Formula)</th>
                        <th>โจทย์ให้ / หา</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>$(F/P, i, n)$</strong></td>
                        <td>CAF / SPCAF</td>
                        <td>Single Payment Compound Amount</td>
                        <td>$(1 + i)^n$</td>
                        <td>รู้ $P$ หา $F$</td>
                    </tr>
                    <tr>
                        <td><strong>$(P/F, i, n)$</strong></td>
                        <td>PWF / SPPWF</td>
                        <td>Single Payment Present Worth</td>
                        <td>$(1 + i)^{-n} = \\frac{1}{(1+i)^n}$</td>
                        <td>รู้ $F$ หา $P$</td>
                    </tr>
                    <tr>
                        <td><strong>$(F/A, i, n)$</strong></td>
                        <td>SCAF / USCAF</td>
                        <td>Uniform Series Compound Amount</td>
                        <td>$\\frac{(1 + i)^n - 1}{i}$</td>
                        <td>รู้ $A$ หา $F$</td>
                    </tr>
                    <tr>
                        <td><strong>$(A/F, i, n)$</strong></td>
                        <td>SFF</td>
                        <td>Sinking Fund Factor</td>
                        <td>$\\frac{i}{(1 + i)^n - 1}$</td>
                        <td>รู้ $F$ หา $A$</td>
                    </tr>
                    <tr>
                        <td><strong>$(P/A, i, n)$</strong></td>
                        <td>SPWF / USPWF</td>
                        <td>Uniform Series Present Worth</td>
                        <td>$\\frac{(1 + i)^n - 1}{i(1 + i)^n}$</td>
                        <td>รู้ $A$ หา $P$</td>
                    </tr>
                    <tr>
                        <td><strong>$(A/P, i, n)$</strong></td>
                        <td>CRF</td>
                        <td>Capital Recovery Factor</td>
                        <td>$\\frac{i(1 + i)^n}{(1 + i)^n - 1}$</td>
                        <td>รู้ $P$ หา $A$</td>
                    </tr>
                    <tr>
                        <td><strong>$(P/G, i, n)$</strong></td>
                        <td>GPWF</td>
                        <td>Arithmetic Gradient Present Worth</td>
                        <td>$\\frac{1}{i}\\left[\\frac{(1+i)^n - 1}{i(1+i)^n} - \\frac{n}{(1+i)^n}\\right]$</td>
                        <td>รู้ $G$ หา $P$</td>
                    </tr>
                    <tr>
                        <td><strong>$(A/G, i, n)$</strong></td>
                        <td>GUSF</td>
                        <td>Gradient Uniform Series</td>
                        <td>$\\frac{1}{i} - \\frac{n}{(1+i)^n - 1}$</td>
                        <td>รู้ $G$ หา $A$</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div style="background:#e0f2fe; padding:0.85rem 1.25rem; border-radius:8px; font-size:0.9rem; color:#0369a1;">
            💡 <strong>กฎการเพิ่มเป็นสองเท่า (Rule of 72):</strong> ระยะเวลาที่เงินลงทุนจะเพิ่มขึ้นเป็น 2 เท่า ประมาณได้จาก $n \\approx 72 / (i\\%)$. เช่น ที่ดอกเบี้ย 8% จะใช้เวลาประมาณ $72/8 = 9$ ปี (ค่าแท้จริงคือ $\\ln(2)/\\ln(1.08) = 9.006$ ปี)
        </div>
    </div>

    <!-- MODULE 4 & 5 -->
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(380px, 1fr)); gap:1.25rem; margin-top:1.5rem;">
        
        <!-- MODULE 4 -->
        <div class="card" style="background:#fafafa; border-left: 4px solid #6366f1;">
            <h3 style="color:#4f46e5; font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 4: การเปรียบเทียบด้วยมูลค่าปัจจุบัน (Present Worth - PW)</h3>
            <p style="font-size:0.9rem;">แปลงกระแสเงินสดรับและจ่ายทั้งหมดในอนาคตกลับมาเป็นมูลค่า ณ เวลาปัจจุบัน ($t = 0$) ที่อัตราคิดลด $i$ (MARR)</p>
            <div class="formula-box" style="margin:0.75rem 0;">
                $$PW = \\sum_{t=0}^n \\frac{CF_t}{(1 + i)^t} = PW(\\text{Inflow}) - PW(\\text{Outflow})$$
            </div>
            <h5 style="color:var(--primary-dark); font-size:0.92rem; margin-top:0.5rem;">📌 กฎการเปรียบเทียบทางเลือกที่มีอายุไม่เท่ากัน:</h5>
            <ul style="font-size:0.85rem; padding-left:1.2rem; line-height:1.6;">
                <li><strong>วิธีหา ครน. ของอายุ (Least Common Multiple - LCM):</strong> สมมติการลงทุนซ้ำ (Repeatability Assumption) เพื่อให้ระยะเวลาเปรียบเทียบเท่ากัน เช่น ทางเลือกอายุ 6 ปี กับ 8 ปี ต้องเปรียบเทียบที่ระยะเวลา 24 ปี</li>
                <li><strong>วิธีกำหนดกรอบเวลาการศึกษา (Study Period):</strong> กำหนดช่วงเวลาแน่นอน เช่น 10 ปี และคิดมูลค่าซากที่หลงเหลือ ณ สิ้นปีที่ 10</li>
                <li><strong>มูลค่าเทียบเท่าเงินลงทุนนิรันดร์ (Capitalized Cost - CC):</strong> สำหรับโครงการอายุยาวนานอนันต์ ($n \\to \\infty$) เช่น คลอง เขื่อน สะพาน
                $$CC = P_0 + \\frac{A}{i} + \\frac{\\text{Replacement Fund}}{(1+i)^k - 1}$$</li>
            </ul>
        </div>

        <!-- MODULE 5 -->
        <div class="card" style="background:#fafafa; border-left: 4px solid #06b6d4;">
            <h3 style="color:#0891b2; font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 5: ค่าเทียบเท่าเงินจ่ายเท่ากันรายปี (Annual Worth - AW / EUAC)</h3>
            <p style="font-size:0.9rem;">แปลงกระแสเงินสดทั้งหมดให้เป็นเงินรายปีที่เท่ากันทุกปีตลอดอายุโครงการ</p>
            <div class="callout-box" style="background:#ecfeff; border-color:#06b6d4; padding:0.75rem; margin:0.75rem 0; font-size:0.88rem;">
                ⭐ <strong>ข้อได้เปรียบสูงสุดของวิธี AW:</strong> เมื่อเปรียบเทียบทางเลือกที่มีอายุขัยไม่เท่ากัน <em>ไม่จำเป็นต้องหา ครน. (LCM)</em> คำนวณ AW ของแต่ละทางเลือกตามอายุขัยของตัวเองได้ทันที!
            </div>
            <div class="formula-box" style="margin:0.75rem 0;">
                <div class="formula-title">สูตร Capital Recovery (CR) 4 รูปแบบ:</div>
                <div style="font-size:0.85rem; line-height:1.7;">
                    1) $A = P(A/P, i, n) - S(A/F, i, n)$<br>
                    2) $A = [P - S(P/F, i, n)](A/P, i, n)$<br>
                    3) $A = (P - S)(A/P, i, n) + S \\cdot i$<br>
                    4) $A = (P - S)(A/F, i, n) + P \\cdot i$
                </div>
            </div>
        </div>
    </div>

    <!-- MODULE 6 & 7 -->
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(380px, 1fr)); gap:1.25rem; margin-top:1.5rem;">
        
        <!-- MODULE 6 -->
        <div class="card" style="background:#fafafa; border-left: 4px solid #8b5cf6;">
            <h3 style="color:#7c3aed; font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 6: อัตราผลตอบแทนภายในและการลงทุนส่วนเพิ่ม (IRR & $\\Delta$IRR)</h3>
            <p style="font-size:0.9rem;"><strong>IRR ($i^*$):</strong> คืออัตราคิดลดที่ทำให้มูลค่าปัจจุบันสุทธิเป็นศูนย์ ($NPW = 0$) หรือทำให้ $PW(\\text{รายรับ}) = PW(\\text{รายจ่าย})$</p>
            <div class="callout-box callout-danger" style="padding:0.75rem; margin:0.75rem 0; font-size:0.85rem;">
                🚨 <strong>กับดักข้อสอบยอดนิยม (Crucial Rule):</strong> ห้ามเลือกโครงการที่มี IRR สูงสุดตรงๆ เด็ดขาด! เพราะโครงการที่เงินลงทุนน้อยอาจให้ IRR สูง แต่สร้างมูลค่ารวม (NPW) น้อยกว่าโครงการขนาดใหญ่ ต้องใช้วิธี <strong>วิเคราะห์เงินลงทุนส่วนเพิ่ม ($\\Delta$IRR)</strong>
            </div>
            <h5 style="color:var(--primary-dark); font-size:0.9rem;">ขั้นตอน Incremental Analysis:</h5>
            <ol style="font-size:0.85rem; padding-left:1.2rem; line-height:1.6;">
                <li>เรียงลำดับทางเลือกตามเงินลงทุนเริ่มต้นจากน้อยไปมาก ($P_1 < P_2 < P_3$)</li>
                <li>ตรวจว่า $IRR_{base} \\ge MARR$ หรือไม่ ถ้าไม่ผ่านให้ตัดทิ้ง</li>
                <li>เปรียบเทียบส่วนต่าง $\\Delta P = P_2 - P_1$ และ $\\Delta A = A_2 - A_1$ เพื่อหา $\\Delta i^*$</li>
                <li>ถ้า $\\Delta i^* \\ge MARR$ ให้เลือกโครงการที่มีเงินลงทุนสูงกว่า ($P_2$); ถ้าไม่ถึงให้เลือกโครงการเดิม ($P_1$)</li>
            </ol>
        </div>

        <!-- MODULE 7 -->
        <div class="card" style="background:#fafafa; border-left: 4px solid #14b8a6;">
            <h3 style="color:#0d9488; font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 7: อัตราส่วนผลประโยชน์ต่อเงินลงทุน (Benefit-Cost Ratio - B/C)</h3>
            <p style="font-size:0.9rem;">ใช้สำหรับประเมินโครงการภาครัฐหรือสาธารณูปโภค โดยคำนึงถึงผลประโยชน์ของผู้ใช้บริการ (User Benefits) เทียบกับต้นทุนที่รัฐจ่าย</p>
            <div class="formula-box" style="margin:0.75rem 0;">
                $$B/C = \\frac{PW(\\text{Benefits}) - PW(\\text{Disbenefits})}{PW(\\text{Capital Cost}) + PW(\\text{O\\&M})} = \\frac{\\Delta B}{\\Delta C}$$
            </div>
            <ul style="font-size:0.85rem; padding-left:1.2rem; line-height:1.6;">
                <li><strong>เกณฑ์การตัดสินใจ:</strong> ถ้า $B/C \\ge 1.0$ โครงการคุ้มค่าและยอมรับได้</li>
                <li><strong>การเปรียบเทียบโครงการทางเลือก (Incremental B/C):</strong> เรียงลำดับเงินลงทุน แล้วคำนวณ $\\Delta B / \\Delta C$ หาก $\\ge 1.0$ จึงจะยอมรับการเพิ่มเงินลงทุนไปยังโครงการที่ใหญ่กว่า</li>
            </ul>
        </div>
    </div>

    <!-- MODULE 8, 9, 10 -->
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap:1.25rem; margin-top:1.5rem;">
        
        <!-- MODULE 8 -->
        <div class="card" style="background:#fafafa; border-left: 4px solid #f97316;">
            <h3 style="color:#ea580c; font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 8: การทดแทนทรัพย์สิน (Replacement Analysis)</h3>
            <ul style="font-size:0.86rem; padding-left:1.2rem; line-height:1.65;">
                <li><strong>Defender:</strong> ทรัพย์สินเดิมที่ใช้งานอยู่ปัจจุบัน</li>
                <li><strong>Challenger:</strong> ทรัพย์สินใหม่ที่เสนอเข้ามาทดแทน</li>
                <li><strong>Sunk Cost:</strong> ราคาซื้อทรัพย์สินเดิมในอดีตและมูลค่าทางบัญชี <em>ห้ามนำมาคิด!</em> ให้ใช้ <strong>ราคาตลาดปัจจุบัน (Market/Trade-in Value)</strong> เสมือนเป็นเงินลงทุนตั้งต้นของ Defender</li>
                <li><strong>วิธีการวิเคราะห์:</strong> นิยมใช้การเปรียบเทียบค่าเทียบเท่ารายปี ($AW$) หรือวิธีกระแสเงินสดส่วนเพิ่ม</li>
                <li><strong>สาเหตุการทดแทน:</strong> การเสื่อมสภาพทางกายภาพ, ความล้าสมัยทางเทคโนโลยี, สมรรถนะการผลิตไม่พอ</li>
            </ul>
        </div>

        <!-- MODULE 9 -->
        <div class="card" style="background:#fafafa; border-left: 4px solid #10b981;">
            <h3 style="color:#059669; font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 9: ค่าเสื่อมราคาและภาษีเงินได้ (Depreciation & Tax)</h3>
            <div style="font-size:0.86rem; line-height:1.7;">
                <p><strong>1) รายได้สุทธิ (Net Income):</strong> $R - (FC + VC)$</p>
                <p><strong>2) รายได้ที่ต้องเสียภาษี (Taxable Income, TI):</strong> $\\text{Net Income} - D$ (หักค่าเสื่อมราคา)</p>
                <p><strong>3) ภาษีเงินได้ (Income Tax, T):</strong> $TI \\times \\text{Tax Rate}(\\%)$</p>
                <p><strong>4) กำไรหลังหักภาษี (Net Profit):</strong> $TI - T = TI(1 - t)$</p>
                <p><strong>5) กระแสเงินสดหลังหักภาษี (CFAT):</strong> $\\text{Net Profit} + D$ (บวกค่าเสื่อมราคากลับเข้าสู่กระแสเงินสด เพราะไม่ใช่เงินสดจ่ายจริง)</p>
            </div>
        </div>

        <!-- MODULE 10 -->
        <div class="card" style="background:#fafafa; border-left: 4px solid #ec4899;">
            <h3 style="color:#db2777; font-family:'Kanit'; margin-bottom:0.75rem;">บทที่ 10: ความเสี่ยงและต้นไม้ตัดสินใจ (Risk & Decision Trees)</h3>
            <ul style="font-size:0.86rem; padding-left:1.2rem; line-height:1.65;">
                <li><strong>มูลค่าคาดหมาย (Expected Monetary Value - EMV):</strong> $E(X) = \\sum X_i \\cdot P(X_i)$</li>
                <li><strong>Decision Node (สี่เหลี่ยม $\\square$):</strong> กิ่งที่เกิดจากการตัดสินใจของผู้วิเคราะห์ ให้เลือกกิ่งที่ให้ผลตอบแทนสูงสุด ($Max$) หรือต้นทุนต่ำสุด</li>
                <li><strong>Chance Node (วงกลม $\\bigcirc$):</strong> กิ่งที่เกิดจากความไม่แน่นอนของธรรมชาติ/ตลาด ให้คำนวณหาค่าเฉลี่ยถ่วงน้ำหนักความน่าจะเป็น ($EMV$)</li>
                <li><strong>Rollback Procedure:</strong> การคำนวณย้อนหลังจากปลายกิ่งขวาสุดกลับมายังโคนต้นไม้ทางซ้าย</li>
            </ul>
        </div>

    </div>
</section>
'''
