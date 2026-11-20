# -*- coding: utf-8 -*-

def get_file_analysis_section():
    return '''
<!-- SECTION 1: FILE ANALYSIS -->
<section id="files" class="card" style="margin-top: -1.5rem; border-top: 4px solid var(--primary);">
    <div class="section-header">
        <div>
            <h2 class="section-title">📁 1. การวิเคราะห์ไฟล์ทั้งหมดในโฟลเดอร์ (File Inventory & Analysis)</h2>
            <p class="section-desc">จากการตรวจสอบโครงสร้างและเนื้อหาไฟล์ทั้งหมด 9 ไฟล์ ทั้งในโฟลเดอร์หลักและโฟลเดอร์ย่อย "ไฟล์เอกสารเก่า ปี 2025"</p>
        </div>
        <span class="badge badge-primary" style="font-size:0.9rem; padding:0.4rem 0.8rem;">รวมทั้งหมด 9 ไฟล์ (208 หน้า)</span>
    </div>

    <div class="callout-box">
        <h4 style="color:var(--primary); margin-bottom:0.4rem;">📌 ภาพรวมของชุดเอกสาร (Curriculum Architecture)</h4>
        <p>โฟลเดอร์นี้บรรจุเอกสารประกอบการสอน เอกสารสรุปสูตร ตารางปัจจัยดอกเบี้ย และเฉลยการบ้านของรายวิชา <strong>4801112 / 4811112 การวิเคราะห์ทางเศรษฐศาสตร์วิศวกรรม (Engineering Economic Analysis)</strong> อย่างครบวงจร ตั้งแต่ระดับพื้นฐานพฤติกรรมต้นทุน การวิเคราะห์จุดคุ้มทุน การแปลงมูลค่าเงินตามเวลา การเปรียบเทียบโครงการด้วยมูลค่าปัจจุบัน (PW) มูลค่าเงินรายปี (AW) อัตราผลตอบแทนภายใน (IRR) อัตราส่วนผลประโยชน์ต่อเงินลงทุน (B/C Ratio) การทดแทนทรัพย์สิน (Replacement) ภาษีและค่าเสื่อมราคา จนถึงการตัดสินใจภายใต้ความไม่แน่นอนและแผนภาพต้นไม้การตัดสินใจ (Decision Trees)</p>
    </div>

    <!-- Summary Table -->
    <div class="data-table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 50px;">ลำดับ</th>
                    <th>ชื่อไฟล์ (File Name)</th>
                    <th>ตำแหน่งที่อยู่</th>
                    <th>ขนาด / หน้า</th>
                    <th>ประเภท / บทบาท</th>
                    <th>หัวข้อหลักที่ครอบคลุม</th>
                    <th>จุดสังเกตสำคัญ / ไฮไลต์</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>1</strong></td>
                    <td><strong>4801112  1-69    Midterm.pdf</strong></td>
                    <td>Root Directory</td>
                    <td>57.0 MB <br><span class="badge badge-primary">125 หน้า</span></td>
                    <td><span class="badge badge-primary">สไลด์หลัก (Midterm)</span></td>
                    <td>ต้นทุน, High-Low, Least Squares, จุดคุ้มทุน 1 & หลายสินค้า, มูลค่าเงินตามเวลา, ดอกเบี้ยแท้จริง, การเปรียบเทียบ PW, เงินลงทุนนิรันดร์</td>
                    <td>เป็นสไลด์แม่บทครึ่งแรกของวิชา มีโจทย์ตัวอย่างและแบบฝึกหัดขนาดใหญ่ 3 ชุด (หน้า 49-51, 91-99, 124-125)</td>
                </tr>
                <tr>
                    <td><strong>2</strong></td>
                    <td><strong>ตารางดอกเบี้ย-แปลงดอกเบี้ย.pdf</strong></td>
                    <td>Root Directory</td>
                    <td>335 KB <br><span class="badge badge-secondary">24 หน้า</span></td>
                    <td><span class="badge badge-secondary">ตารางอ้างอิง & สูตร</span></td>
                    <td>ตารางแฟกเตอร์ดอกเบี้ย $i = 0.25\%$ ถึง $30\%$ (F/P, P/F, A/P, P/A, A/F, F/A), สูตรดอกเบี้ยระบุและดอกเบี้ยแท้จริง, Gradient</td>
                    <td>เป็นเอกสารตารางดอกเบี้ยมาตรฐานที่ใช้เปิดสอบ พร้อมสรุปความสัมพันธ์ของแฟกเตอร์ทุกประเภทอย่างเป็นทางการ</td>
                </tr>
                <tr>
                    <td><strong>3</strong></td>
                    <td><strong>07 4811112 เงินรายปี A.pdf</strong></td>
                    <td>ไฟล์เอกสารเก่า ปี 2025</td>
                    <td>7.76 MB <br><span class="badge badge-primary">21 หน้า</span></td>
                    <td><span class="badge badge-primary">สไลด์บรรยายเฉพาะบท</span></td>
                    <td>ค่าเทียบเท่าเงินจ่ายเท่ากันรายปี (Annual Worth - AW / EUAC), Capital Recovery (CR) 4 รูปแบบ, ตัวอย่างแทรคเตอร์, สะพาน, คลังสินค้า</td>
                    <td>เน้นจุดเด่นของวิธี AW ที่ไม่ต้องหา ครน. (LCM) เมื่ออายุขัยไม่เท่ากัน และการวิเคราะห์ค่าเสื่อมบำรุงรักษาแบบเกรเดียนต์</td>
                </tr>
                <tr>
                    <td><strong>4</strong></td>
                    <td><strong>1.pdf</strong></td>
                    <td>ไฟล์เอกสารเก่า ปี 2025</td>
                    <td>2.86 MB <br><span class="badge badge-success">6 หน้า</span></td>
                    <td><span class="badge badge-success">เฉลยทางการ (Solutions)</span></td>
                    <td>เฉลยแบบฝึกหัดบทที่ 4: การฝากเงินรายไตรมาส, เงินรวมทบต้นรายเดือน, การปรับโครงสร้างสัญญารายปียกยอด (Deferred Annuity)</td>
                    <td>แสดงวิธีทำ 2 รูปแบบอย่างละเอียดสำหรับโจทย์การปรับโครงสร้างสัญญาเงินรายปี (ข้อ 3)</td>
                </tr>
                <tr>
                    <td><strong>5</strong></td>
                    <td><strong>481112  ตอนที่ 2  นศ.pdf</strong></td>
                    <td>ไฟล์เอกสารเก่า ปี 2025</td>
                    <td>218 KB <br><span class="badge badge-primary">19 หน้า</span></td>
                    <td><span class="badge badge-primary">สไลด์บรรยาย (Final)</span></td>
                    <td>อัตราผลตอบแทนภายใน (IRR), การลงทุนส่วนเพิ่ม ($\Delta$IRR), B/C Ratio โครงการรัฐ, การทดแทนทรัพย์สิน, ต้นไม้ตัดสินใจ (Decision Trees)</td>
                    <td>สไลด์ภาคเรียนหลังมิดเทอม มีโจทย์คำนวณเชิงลึก EX 5.1-5.4, EX 6.1-6.2, EX 11.1-11.3, EX 14.1-14.2</td>
                </tr>
                <tr>
                    <td><strong>6</strong></td>
                    <td><strong>คาดหมาย.pdf</strong></td>
                    <td>ไฟล์เอกสารเก่า ปี 2025</td>
                    <td>88 KB <br><span class="badge badge-warning">3 หน้า</span></td>
                    <td><span class="badge badge-warning">ชีทโจทย์ตัวอย่าง</span></td>
                    <td>ค่าคาดหมาย (Expected Value - EMV), การวิเคราะห์กระแสเงินสดภายใต้ความไม่แน่นอนของอุปสงค์ 3 สภาวะ (A, B, C) ร่วมกับเกรเดียนต์</td>
                    <td>ตัวอย่างอู่ซ่อมเรือ และตัวอย่างการตัดสินใจเปิดตัวสินค้าใหม่ที่รวมเรื่องความน่าจะเป็นเข้ากับการแปลงมูลค่าปัจจุบัน</td>
                </tr>
                <tr>
                    <td><strong>7</strong></td>
                    <td><strong>ทดแทน.pdf</strong></td>
                    <td>ไฟล์เอกสารเก่า ปี 2025</td>
                    <td>65 KB <br><span class="badge badge-warning">7 หน้า</span></td>
                    <td><span class="badge badge-warning">สไลด์เฉพาะบท</span></td>
                    <td>การศึกษาการทดแทนทรัพย์สิน (Replacement Analysis), Defender vs Challenger, Sunk Cost, วิธี Conventional vs Cash Flow, บริษัท X vs Y</td>
                    <td>เน้นย้ำเรื่องต้นทุนจม (Sunk Cost) ว่าราคาที่ซื้อมาในอดีตต้องตัดทิ้ง ไม่นำมาคิดในการตัดสินใจ</td>
                </tr>
                <tr>
                    <td><strong>8</strong></td>
                    <td><strong>ภาษี.pdf</strong></td>
                    <td>ไฟล์เอกสารเก่า ปี 2025</td>
                    <td>60 KB <br><span class="badge badge-warning">2 หน้า</span></td>
                    <td><span class="badge badge-warning">ชีทสรุป & โจทย์</span></td>
                    <td>ภาษีเงินได้นิติบุคคล (Corporate Income Tax), ค่าเสื่อมราคา (Depreciation), Taxable Income, Net Profit, CFAT</td>
                    <td>มีโจทย์ตัวอย่างการคำนวณภาษี 30% พร้อมข้อสังเกตจุดพิมพ์ตกตัวเลขในสไลด์ต้นฉบับที่ต้องระวัง</td>
                </tr>
                <tr>
                    <td><strong>9</strong></td>
                    <td><strong>สูตร.pdf</strong></td>
                    <td>ไฟล์เอกสารเก่า ปี 2025</td>
                    <td>242 KB <br><span class="badge badge-secondary">1 หน้า</span></td>
                    <td><span class="badge badge-secondary">สรุปสูตรย่อ (Cheat Sheet)</span></td>
                    <td>แฟกเตอร์หลัก 6 ตัว: P/F, F/P, P/A, A/P, A/F, F/A และสูตรดอกเบี้ยเชิงเดี่ยว $F = P(1+in)$</td>
                    <td>แผ่นสรุปสูตรด่วนขนาด 1 หน้า เหมาะสำหรับทบทวนสัญลักษณ์ Functional Notation และสมการพื้นฐาน</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- Deep-dive Cards for Key Files -->
    <h3 style="font-family:'Kanit'; margin: 2rem 0 1rem 0; color:var(--primary-dark);">🔍 รายละเอียดเชิงวิเคราะห์เจาะลึกรายไฟล์ (In-Depth Insights)</h3>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 1.25rem;">
        
        <div class="card" style="border-left:4px solid var(--primary);">
            <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem;">
                <h4 style="color:var(--primary-dark); font-family:'Kanit';">1. 4801112  1-69    Midterm.pdf</h4>
                <span class="badge badge-primary">ไฟล์หลัก Midterm</span>
            </div>
            <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:0.75rem;">ไฟล์เอกสารขนาดใหญ่ที่สุด (125 หน้า) เป็นสไลด์บรรยายหลักของอาจารย์ประจำวิชา</p>
            <ul style="font-size:0.88rem; padding-left:1.2rem; line-height:1.7;">
                <li><strong>หน้าที่ 1-20:</strong> ทบทวนหลักการเศรษฐศาสตร์วิศวกรรม, การจำแนกต้นทุน (Fixed, Variable, Sunk, Opportunity), วิธีแยกต้นทุน High-Low Method และวิธีสมการถดถอยเชิงเส้น (Least Squares)</li>
                <li><strong>หน้าที่ 21-51:</strong> การวิเคราะห์จุดคุ้มทุน (Break-Even Analysis) ทั้งกรณีสินค้าเดียว, กลยุทธ์แก้ปัญหาโรงงานขาดทุน 4 แนวทาง, และจุดคุ้มทุนกรณีผลิตสินค้าหลายชนิด (Weighted Contribution Margin Ratio)</li>
                <li><strong>หน้าที่ 52-99:</strong> มูลค่าเงินตามเวลา ดอกเบี้ยเชิงเดี่ยว ดอกเบี้ยทบต้น ดอกเบี้ยแท้จริง (Effective Interest Rate) และโจทย์แบบฝึกหัดชุดใหญ่ 10 ข้อ (หน้า 91-99)</li>
                <li><strong>หน้าที่ 100-125:</strong> การแปลงกระแสเงินสดเทียบเท่า, เงินรายปียกยอด, การวิเคราะห์และเปรียบเทียบทางเลือกด้วยมูลค่าปัจจุบัน (PW Method), การหา ครน. (LCM), และต้นทุนเงินลงทุนนิรันดร์ (Capitalized Cost)</li>
            </ul>
        </div>

        <div class="card" style="border-left:4px solid var(--secondary);">
            <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem;">
                <h4 style="color:var(--primary-dark); font-family:'Kanit';">2. 481112  ตอนที่ 2  นศ.pdf & ทดแทน.pdf</h4>
                <span class="badge badge-secondary">ไฟล์บรรยาย Final</span>
            </div>
            <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:0.75rem;">ครอบคลุมเนื้อหาครึ่งหลังของวิชา ซึ่งเป็นหัวข้อที่ใช้ออกข้อสอบปลายภาค (Final Examination)</p>
            <ul style="font-size:0.88rem; padding-left:1.2rem; line-height:1.7;">
                <li><strong>การหาอัตราผลตอบแทน (IRR):</strong> นิยาม $PW = 0$, การเปิดตารางและประมาณค่าด้วยเชิงเส้น (Interpolation)</li>
                <li><strong>การวิเคราะห์เงินลงทุนส่วนเพิ่ม ($\Delta$IRR):</strong> กฎเหล็กที่ห้ามเลือกโครงการจาก IRR สูงสุดตรงๆ แต่ต้องเรียงลำดับเงินลงทุนและวิเคราะห์ผลตอบแทนส่วนเพิ่มเทียบกับ MARR</li>
                <li><strong>Benefit-Cost Ratio (B/C):</strong> การประเมินโครงการภาครัฐด้วยอัตราส่วนผลประโยชน์ต่อเงินลงทุน และการวิเคราะห์ $\Delta B / \Delta C$</li>
                <li><strong>Asset Replacement:</strong> การประเมินเพื่อเปลี่ยนเครื่องจักร/รถยนต์, กฎการตัดต้นทุนจม (Sunk Cost), วิธี Cash Flow vs Conventional</li>
                <li><strong>Decision Tree:</strong> การเขียนแผนภาพกิ่งไม้ตัดสินใจ, จุดสี่เหลี่ยม (Decision Node) vs จุดวงกลม (Chance Node), การ Rollback ค่าคาดหมาย (EMV)</li>
            </ul>
        </div>

        <div class="card" style="border-left:4px solid var(--accent);">
            <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem;">
                <h4 style="color:var(--primary-dark); font-family:'Kanit';">3. ภาษี.pdf, คาดหมาย.pdf, 1.pdf, 07 เงินรายปี A</h4>
                <span class="badge badge-warning">ไฟล์เฉพาะทาง & เฉลย</span>
            </div>
            <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:0.75rem;">ไฟล์เสริมสำหรับการฝึกทำโจทย์และตรวจสอบความถูกต้องของสูตรคำนวณ</p>
            <ul style="font-size:0.88rem; padding-left:1.2rem; line-height:1.7;">
                <li><strong>07 เงินรายปี A.pdf:</strong> อธิบายสูตร Capital Recovery (CR) 4 รูปแบบอย่างละเอียด และสาธิตให้เห็นว่าทั้ง 4 สูตรให้ค่าเท่ากันคือ 47,350 บาทสำหรับเครื่องกลึง</li>
                <li><strong>1.pdf:</strong> เฉลยการบ้านบทที่ 4 แสดงวิธีคิดการแปลงสัญญารายปี 2 วิธีอย่างละเอียด พร้อมคำตอบที่ตรงกัน</li>
                <li><strong>ภาษี.pdf (จุดระวัง):</strong> สไลด์เขียน $28,800,000 \times 30\% = 864,000$ (พิมพ์ตกเลข 0 ไปหนึ่งหลัก แท้จริงคือ $8,640,000$) แต่บรรทัดกำไรหลังหักภาษีเขียน $20,160,000$ ซึ่งคำนวณจาก $28,800,000 - 8,640,000$ ได้ถูกต้อง</li>
                <li><strong>คาดหมาย.pdf:</strong> รวมตัวอย่างคำนวณค่าคาดหมาย (EMV) ของอู่ซ่อมเรือ และโครงการสินค้าใหม่ที่มีทั้ง Annuity และ Arithmetic Gradient</li>
            </ul>
        </div>

    </div>
</section>
'''
