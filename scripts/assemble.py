# -*- coding: utf-8 -*-
import os
import sys

from make_head_and_css import get_head_and_nav
from make_file_analysis import get_file_analysis_section
from make_theory_summary import get_theory_summary_section
from make_calculator_and_cheatsheet import get_calculator_and_cheatsheet_section
from make_problems_solutions import get_problems_and_solutions_section
from make_footer_and_js import get_footer_and_js

def build_complete_html():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_filename = os.path.join(root_dir, "สรุปวิศวกรรมเศรษฐศาสตร์_พร้อมโจทย์และเฉลย.html")
    print(f"Building {output_filename}...")
    
    parts = [
        get_head_and_nav(),
        get_file_analysis_section(),
        get_theory_summary_section(),
        get_calculator_and_cheatsheet_section(),
        get_problems_and_solutions_section(),
        get_footer_and_js()
    ]
    
    full_html = "\n".join(parts)
    
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    size_kb = os.path.getsize(output_filename) / 1024
    print(f"Successfully generated {output_filename} ({size_kb:.2f} KB, {len(full_html)} characters)")

if __name__ == "__main__":
    build_complete_html()
