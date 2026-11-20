# -*- coding: utf-8 -*-

def get_head_and_nav():
    return r'''<!DOCTYPE html>
<html lang="th" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>สรุปวิชาการวิเคราะห์ทางเศรษฐศาสตร์วิศวกรรม (Engineering Economic Analysis) ฉบับสมบูรณ์ พร้อมโจทย์และเฉลย</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=Kanit:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- MathJax 3 -->
    <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true
      },
      options: {
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root {
            --navy-950: #081221;
            --navy-900: #0B192C;
            --navy-800: #13294B;
            --navy-700: #1E3A6D;
            --gold-500: #C8A24A;
            --gold-400: #DFBE6F;
            --gold-100: #FBF5E6;
            --primary: #13294B;
            --primary-light: #2563EB;
            --primary-dark: #0B192C;
            --secondary: #0F766E;
            --secondary-light: #14B8A6;
            --accent: #C8A24A;
            --danger: #DC2626;
            --success: #059669;

            --bg-main: #F5F7FA;
            --bg-card: #FFFFFF;
            --bg-subtle: #F8FAFC;
            --bg-elevated: #FFFFFF;
            --text-main: #1E293B;
            --text-heading: #0B192C;
            --text-muted: #64748B;
            --border-color: rgba(15, 23, 42, 0.09);
            --border-strong: rgba(15, 23, 42, 0.16);

            --shadow-xs: 0 1px 2px rgba(11, 25, 44, 0.04);
            --shadow-sm: 0 2px 8px rgba(11, 25, 44, 0.05), 0 1px 2px rgba(11, 25, 44, 0.03);
            --shadow: 0 10px 28px -6px rgba(11, 25, 44, 0.08), 0 4px 10px -4px rgba(11, 25, 44, 0.04);
            --shadow-lg: 0 20px 44px -12px rgba(11, 25, 44, 0.14);
            --radius-sm: 10px;
            --radius-md: 16px;
            --radius-lg: 22px;
            --font-scale: 1;
        }

        [data-theme="dark"] {
            --primary: #93C5FD;
            --primary-light: #60A5FA;
            --primary-dark: #F1F5F9;
            --secondary: #2DD4BF;
            --secondary-light: #5EEAD4;
            --accent: #E2C275;
            --danger: #F87171;
            --success: #34D399;

            --bg-main: #0A101D;
            --bg-card: #111A2C;
            --bg-subtle: #162238;
            --bg-elevated: #1A2842;
            --text-main: #E2E8F0;
            --text-heading: #F8FAFC;
            --text-muted: #94A3B8;
            --border-color: rgba(148, 163, 184, 0.15);
            --border-strong: rgba(148, 163, 184, 0.28);

            --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.35);
            --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.35);
            --shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
            --shadow-lg: 0 24px 48px rgba(0, 0, 0, 0.55);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
            font-size: calc(16px * var(--font-scale));
        }

        body {
            font-family: 'IBM Plex Sans Thai', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-main);
            color: var(--text-main);
            line-height: 1.82;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            transition: background-color 0.25s ease, color 0.25s ease;
        }

        /* Reading Progress Bar */
        .reading-progress-track {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            z-index: 1200;
            background: transparent;
            pointer-events: none;
        }

        .reading-progress-bar {
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, var(--gold-500), var(--gold-400), #2DD4BF);
            transition: width 0.08s linear;
            box-shadow: 0 0 10px rgba(200, 162, 74, 0.55);
        }

        /* Top Glassmorphic Navbar */
        .top-navbar {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(11, 25, 44, 0.88);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            color: #F8FAFC;
            padding: 0.7rem 1.75rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            border-bottom: 1px solid rgba(200, 162, 74, 0.25);
            box-shadow: 0 8px 24px rgba(8, 18, 33, 0.18);
        }

        .navbar-brand {
            font-family: 'Kanit', sans-serif;
            font-size: 1.15rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.65rem;
            letter-spacing: 0.2px;
            color: #FFFFFF;
            text-decoration: none;
            white-space: nowrap;
        }

        .brand-emblem {
            width: 34px;
            height: 34px;
            border-radius: 10px;
            background: linear-gradient(135deg, var(--gold-500), #9A7426);
            color: var(--navy-950);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1.05rem;
            font-weight: 700;
            box-shadow: 0 4px 12px rgba(200, 162, 74, 0.35);
        }

        .navbar-menu {
            display: flex;
            gap: 0.35rem;
            align-items: center;
            flex-wrap: wrap;
        }

        .nav-link {
            color: rgba(241, 245, 249, 0.82);
            text-decoration: none;
            font-size: 0.86rem;
            font-weight: 500;
            padding: 0.42rem 0.85rem;
            border-radius: 9999px;
            transition: all 0.2s ease;
            white-space: nowrap;
        }

        .nav-link:hover, .nav-link.active {
            color: #FFFFFF;
            background: rgba(255, 255, 255, 0.12);
        }

        .nav-link.active {
            color: var(--gold-400);
            background: rgba(200, 162, 74, 0.16);
            box-shadow: inset 0 0 0 1px rgba(200, 162, 74, 0.35);
        }

        .nav-utilities {
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }

        .util-btn {
            background: rgba(255, 255, 255, 0.08);
            color: #F1F5F9;
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 9999px;
            padding: 0.38rem 0.75rem;
            font-family: 'IBM Plex Sans Thai', sans-serif;
            font-size: 0.82rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            white-space: nowrap;
        }

        .util-btn:hover {
            background: rgba(200, 162, 74, 0.22);
            border-color: rgba(200, 162, 74, 0.5);
            color: #FFFFFF;
        }

        /* Editorial Luxury Hero Header */
        .hero-header {
            background:
                radial-gradient(circle at 18% 20%, rgba(200, 162, 74, 0.22) 0%, transparent 45%),
                radial-gradient(circle at 84% 78%, rgba(20, 184, 166, 0.20) 0%, transparent 48%),
                linear-gradient(145deg, #07111F 0%, #0E223D 52%, #132F4C 100%);
            color: #FFFFFF;
            padding: 4.25rem 2rem 4.75rem 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            border-bottom: 1px solid rgba(200, 162, 74, 0.28);
        }

        .hero-header::before {
            content: '';
            position: absolute;
            inset: 0;
            background-image:
                linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            mask-image: radial-gradient(circle at center, black 40%, transparent 85%);
            pointer-events: none;
        }

        .hero-inner {
            max-width: 960px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(200, 162, 74, 0.14);
            color: var(--gold-400);
            backdrop-filter: blur(8px);
            padding: 0.4rem 1.15rem;
            border-radius: 9999px;
            font-size: 0.82rem;
            letter-spacing: 0.6px;
            margin-bottom: 1.25rem;
            font-weight: 600;
            border: 1px solid rgba(200, 162, 74, 0.45);
        }

        .hero-title {
            font-family: 'Kanit', sans-serif;
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 0.65rem;
            letter-spacing: -0.01em;
            background: linear-gradient(180deg, #FFFFFF 35%, #E8D5A7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-course-sub {
            font-family: 'Kanit', sans-serif;
            font-size: 1.22rem;
            font-weight: 400;
            color: #CBD5E1;
            margin-bottom: 1rem;
            letter-spacing: 0.2px;
        }

        .hero-subtitle {
            font-size: 1.02rem;
            color: rgba(226, 232, 240, 0.84);
            max-width: 760px;
            margin: 0 auto 2rem auto;
            font-weight: 300;
            line-height: 1.75;
        }

        .hero-actions {
            display: flex;
            justify-content: center;
            gap: 0.85rem;
            flex-wrap: wrap;
            margin-bottom: 2.5rem;
        }

        .hero-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.72rem 1.45rem;
            border-radius: 9999px;
            font-family: 'Kanit', sans-serif;
            font-size: 0.95rem;
            font-weight: 500;
            text-decoration: none;
            transition: all 0.22s cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        .hero-btn-primary {
            background: linear-gradient(135deg, var(--gold-500), #B58B34);
            color: var(--navy-950);
            box-shadow: 0 10px 24px rgba(200, 162, 74, 0.35);
            font-weight: 600;
        }

        .hero-btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 28px rgba(200, 162, 74, 0.45);
            filter: brightness(1.06);
        }

        .hero-btn-ghost {
            background: rgba(255, 255, 255, 0.08);
            color: #F8FAFC;
            border: 1px solid rgba(255, 255, 255, 0.22);
            backdrop-filter: blur(8px);
        }

        .hero-btn-ghost:hover {
            background: rgba(255, 255, 255, 0.16);
            transform: translateY(-2px);
        }

        .hero-stats {
            display: grid;
            grid-template-columns: repeat(4, minmax(130px, 1fr));
            gap: 1rem;
            max-width: 780px;
            margin: 0 auto;
        }

        .stat-item {
            background: rgba(255, 255, 255, 0.06);
            backdrop-filter: blur(12px);
            padding: 1rem 1.15rem;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.14);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .stat-item:hover {
            transform: translateY(-3px);
            border-color: rgba(200, 162, 74, 0.45);
        }

        .stat-num {
            font-size: 1.75rem;
            font-weight: 700;
            font-family: 'JetBrains Mono', 'Kanit', sans-serif;
            color: var(--gold-400);
            line-height: 1.2;
        }

        .stat-label {
            font-size: 0.8rem;
            color: rgba(226, 232, 240, 0.82);
            margin-top: 0.25rem;
        }

        /* Page Shell: Sticky TOC Sidebar + Main Content */
        .page-shell {
            max-width: 1460px;
            margin: 0 auto;
            padding: 2rem 1.5rem 3rem 1.5rem;
            display: grid;
            grid-template-columns: 270px minmax(0, 1fr);
            gap: 2rem;
            align-items: start;
        }

        .sidebar-toc {
            position: sticky;
            top: 5.25rem;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.25rem;
            box-shadow: var(--shadow-sm);
            max-height: calc(100vh - 6.5rem);
            overflow-y: auto;
        }

        .sidebar-toc::-webkit-scrollbar {
            width: 5px;
        }
        .sidebar-toc::-webkit-scrollbar-thumb {
            background: var(--border-strong);
            border-radius: 9999px;
        }

        .toc-heading {
            font-family: 'Kanit', sans-serif;
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.9px;
            color: var(--accent);
            font-weight: 600;
            margin-bottom: 0.85rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .toc-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }

        .toc-link {
            display: flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.5rem 0.7rem;
            border-radius: 10px;
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.86rem;
            font-weight: 500;
            transition: all 0.18s ease;
            border-left: 2px solid transparent;
        }

        .toc-link:hover {
            background: var(--bg-subtle);
            color: var(--text-heading);
        }

        .toc-link.active {
            background: rgba(200, 162, 74, 0.12);
            color: var(--text-heading);
            border-left-color: var(--gold-500);
            font-weight: 600;
        }

        .toc-sublist {
            list-style: none;
            margin: 0.25rem 0 0.5rem 0.85rem;
            padding-left: 0.75rem;
            border-left: 1px dashed var(--border-strong);
            display: flex;
            flex-direction: column;
            gap: 0.15rem;
        }

        .toc-sublink {
            display: block;
            padding: 0.3rem 0.55rem;
            border-radius: 8px;
            font-size: 0.78rem;
            color: var(--text-muted);
            text-decoration: none;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            transition: all 0.15s ease;
        }

        .toc-sublink:hover, .toc-sublink.active {
            color: var(--secondary);
            background: var(--bg-subtle);
        }

        .sidebar-progress-box {
            margin-top: 1.15rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border-color);
        }

        .progress-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-bottom: 0.45rem;
            font-weight: 500;
        }

        .progress-track {
            height: 8px;
            background: var(--bg-subtle);
            border-radius: 9999px;
            overflow: hidden;
            border: 1px solid var(--border-color);
        }

        .progress-fill {
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, var(--secondary), var(--gold-500));
            border-radius: 9999px;
            transition: width 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        .main-container {
            min-width: 0;
            width: 100%;
            padding: 0;
            margin: 0;
        }

        /* Section Cards */
        section.card {
            background: var(--bg-card);
            border-radius: var(--radius-lg);
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow);
            padding: 2.25rem;
            margin-bottom: 2.25rem;
            scroll-margin-top: 5.5rem;
            transition: background-color 0.25s ease, border-color 0.25s ease;
        }

        #files.card {
            margin-top: 0 !important;
        }

        .card {
            background: var(--bg-card);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-sm);
            padding: 1.65rem;
            margin-bottom: 1.5rem;
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
        }

        /* Nested Chapter Cards inside Theory Section */
        #theory > .card {
            background: var(--bg-subtle) !important;
            border: 1px solid var(--border-color) !important;
            border-left: 4px solid var(--gold-500) !important;
            border-radius: var(--radius-md) !important;
            padding: 1.75rem !important;
            margin-bottom: 1.6rem !important;
            scroll-margin-top: 5.5rem;
        }

        #theory > .card:hover {
            box-shadow: var(--shadow);
            border-color: var(--border-strong) !important;
        }

        #theory > .card > h3 {
            font-family: 'Kanit', sans-serif !important;
            font-size: 1.32rem !important;
            color: var(--text-heading) !important;
            margin-bottom: 0.85rem !important;
            padding-bottom: 0.55rem;
            border-bottom: 1px solid var(--border-color);
            line-height: 1.35;
        }

        /* Chapter Quick-Jump Pills */
        .chapter-pills-bar {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-bottom: 1.75rem;
            padding: 0.9rem 1rem;
            background: var(--bg-subtle);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
        }

        .chapter-pill {
            display: inline-flex;
            align-items: center;
            padding: 0.35rem 0.78rem;
            border-radius: 9999px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            text-decoration: none;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.18s ease;
        }

        .chapter-pill:hover {
            background: var(--navy-800);
            color: #FFFFFF;
            border-color: var(--navy-800);
            transform: translateY(-1px);
        }

        /* Section Headings */
        .section-header {
            margin-bottom: 1.75rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .section-title {
            font-family: 'Kanit', sans-serif;
            font-size: 1.72rem;
            font-weight: 600;
            color: var(--text-heading);
            display: flex;
            align-items: center;
            gap: 0.65rem;
            line-height: 1.3;
        }

        .section-desc {
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-top: 0.35rem;
        }

        /* Badges */
        .badge {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.72rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.2px;
        }

        .badge-primary { background: rgba(37, 99, 235, 0.12); color: #1D4ED8; }
        .badge-secondary { background: rgba(15, 118, 110, 0.12); color: #0F766E; }
        .badge-warning { background: rgba(200, 162, 74, 0.18); color: #92660A; }
        .badge-danger { background: rgba(220, 38, 38, 0.12); color: #B91C1C; }
        .badge-success { background: rgba(5, 150, 105, 0.13); color: #047857; }

        [data-theme="dark"] .badge-primary { background: rgba(96, 165, 250, 0.18); color: #93C5FD; }
        [data-theme="dark"] .badge-secondary { background: rgba(45, 212, 191, 0.16); color: #5EEAD4; }
        [data-theme="dark"] .badge-warning { background: rgba(226, 194, 117, 0.18); color: #FDE68A; }
        [data-theme="dark"] .badge-danger { background: rgba(248, 113, 113, 0.18); color: #FCA5A5; }
        [data-theme="dark"] .badge-success { background: rgba(52, 211, 153, 0.18); color: #6EE7B7; }

        /* Tables */
        .data-table-container {
            overflow-x: auto;
            background: var(--bg-card);
            border-radius: 14px;
            border: 1px solid var(--border-color);
            margin: 1.35rem 0;
            box-shadow: var(--shadow-xs);
        }

        table.data-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.91rem;
            text-align: left;
        }

        table.data-table th {
            background: var(--bg-subtle);
            color: var(--text-heading);
            padding: 0.95rem 1.05rem;
            font-family: 'Kanit', sans-serif;
            font-weight: 600;
            font-size: 0.88rem;
            border-bottom: 1.5px solid var(--border-strong);
            white-space: nowrap;
        }

        table.data-table td {
            padding: 0.9rem 1.05rem;
            border-bottom: 1px solid var(--border-color);
            vertical-align: top;
            color: var(--text-main);
        }

        table.data-table tbody tr:last-child td {
            border-bottom: none;
        }

        table.data-table tbody tr:hover td {
            background: rgba(200, 162, 74, 0.05);
        }

        /* Formulas & Callouts */
        .formula-box {
            background: linear-gradient(135deg, rgba(15, 118, 110, 0.05) 0%, rgba(200, 162, 74, 0.05) 100%);
            border: 1px solid rgba(15, 118, 110, 0.18);
            border-left: 4px solid var(--secondary);
            padding: 1.2rem 1.4rem;
            border-radius: 12px;
            margin: 1.15rem 0;
            font-size: 0.96rem;
            overflow-x: auto;
        }

        .formula-title {
            font-family: 'Kanit', sans-serif;
            font-weight: 600;
            color: var(--secondary);
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.45rem;
            font-size: 1rem;
        }

        .callout-box {
            background: rgba(37, 99, 235, 0.05);
            border: 1px solid rgba(37, 99, 235, 0.16);
            border-left: 4px solid var(--primary-light);
            padding: 1.15rem 1.35rem;
            border-radius: 12px;
            margin: 1.15rem 0;
        }

        .callout-warning {
            background: rgba(200, 162, 74, 0.09);
            border: 1px solid rgba(200, 162, 74, 0.28);
            border-left: 4px solid var(--gold-500);
        }

        .callout-danger {
            background: rgba(220, 38, 38, 0.06);
            border: 1px solid rgba(220, 38, 38, 0.22);
            border-left: 4px solid var(--danger);
        }

        mjx-container[display="true"] {
            overflow-x: auto;
            overflow-y: hidden;
            padding: 0.35rem 0;
        }

        /* Interactive Calculator */
        .calculator-container {
            background: linear-gradient(145deg, var(--bg-subtle) 0%, var(--bg-card) 100%);
            border: 1px solid var(--border-strong);
            border-radius: var(--radius-md);
            padding: 1.85rem;
            margin: 1.5rem 0 0.5rem 0;
            box-shadow: var(--shadow-sm);
        }

        .calc-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 1.15rem;
            margin-top: 1.25rem;
        }

        .calc-input-group label {
            display: block;
            font-size: 0.86rem;
            font-weight: 600;
            color: var(--text-heading);
            margin-bottom: 0.4rem;
        }

        .calc-input-group input, .calc-input-group select {
            width: 100%;
            padding: 0.68rem 0.95rem;
            border-radius: 10px;
            border: 1.5px solid var(--border-strong);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.98rem;
            background: var(--bg-card);
            color: var(--text-heading);
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .calc-input-group input:focus, .calc-input-group select:focus {
            outline: none;
            border-color: var(--gold-500);
            box-shadow: 0 0 0 3px rgba(200, 162, 74, 0.2);
        }

        .calc-results-box {
            background: transparent;
            padding: 0;
            border: none;
            margin-top: 1.5rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(175px, 1fr));
            gap: 0.95rem;
            text-align: left;
        }

        .calc-res-item {
            background: var(--bg-card);
            padding: 1rem 1.05rem;
            border-radius: 14px;
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-xs);
            cursor: pointer;
            transition: all 0.2s ease;
            position: relative;
        }

        .calc-res-item:hover {
            transform: translateY(-2px);
            border-color: var(--gold-500);
            box-shadow: var(--shadow-sm);
        }

        .calc-res-label {
            font-size: 0.74rem;
            color: var(--text-muted);
            font-weight: 600;
            letter-spacing: 0.2px;
        }

        .calc-res-val {
            font-size: 1.32rem;
            font-weight: 700;
            color: var(--text-heading);
            font-family: 'JetBrains Mono', monospace;
            margin-top: 0.28rem;
            font-variant-numeric: tabular-nums;
        }

        .calc-res-money {
            font-size: 0.8rem;
            font-family: 'JetBrains Mono', 'IBM Plex Sans Thai', sans-serif;
            color: var(--secondary);
            font-weight: 600;
            margin-top: 0.28rem;
            padding-top: 0.28rem;
            border-top: 1px dashed var(--border-color);
        }

        /* Filter & Search Controls */
        .problems-toolbar {
            background: var(--bg-subtle);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.15rem;
            margin-bottom: 1.5rem;
        }

        .filter-controls {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 0;
            align-items: center;
        }

        .search-box {
            flex: 1 1 100%;
            min-width: 240px;
            padding: 0.72rem 1.1rem;
            border-radius: 12px;
            border: 1.5px solid var(--border-strong);
            font-family: 'IBM Plex Sans Thai', sans-serif;
            font-size: 0.95rem;
            background: var(--bg-card);
            color: var(--text-main);
            margin-bottom: 0.55rem;
            transition: all 0.2s ease;
        }

        .search-box:focus {
            outline: none;
            border-color: var(--gold-500);
            box-shadow: 0 0 0 3px rgba(200, 162, 74, 0.2);
        }

        .filter-btn {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 0.42rem 0.92rem;
            border-radius: 9999px;
            font-family: 'IBM Plex Sans Thai', sans-serif;
            font-size: 0.83rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.18s ease;
        }

        .filter-btn:hover {
            border-color: var(--gold-500);
            color: var(--text-heading);
        }

        .filter-btn.active {
            background: var(--navy-800);
            color: #FFFFFF;
            border-color: var(--navy-800);
            box-shadow: 0 4px 12px rgba(19, 41, 75, 0.22);
        }

        [data-theme="dark"] .filter-btn.active {
            background: var(--gold-500);
            color: var(--navy-950);
            border-color: var(--gold-500);
            font-weight: 600;
        }

        .problems-status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin: 1rem 0 1.25rem 0;
            font-size: 0.86rem;
            color: var(--text-muted);
        }

        /* Problem Cards */
        .problem-card {
            background: var(--bg-card);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            margin-bottom: 1.25rem;
            box-shadow: var(--shadow-sm);
            overflow: hidden;
            transition: all 0.22s ease;
        }

        .problem-card:hover {
            box-shadow: var(--shadow);
            border-color: var(--border-strong);
        }

        .problem-card.completed {
            border-left: 4px solid var(--success);
        }

        .problem-header {
            padding: 1.15rem 1.45rem;
            background: var(--bg-subtle);
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            cursor: pointer;
            user-select: none;
            transition: background 0.18s ease;
        }

        .problem-header:hover {
            background: rgba(200, 162, 74, 0.07);
        }

        .problem-title-area {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            flex-wrap: wrap;
        }

        .problem-num {
            background: linear-gradient(135deg, var(--navy-900), var(--navy-700));
            color: var(--gold-400);
            padding: 0.26rem 0.7rem;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.8rem;
            font-family: 'JetBrains Mono', monospace;
            letter-spacing: 0.3px;
        }

        .problem-title {
            font-family: 'Kanit', sans-serif;
            font-weight: 500;
            font-size: 1.08rem;
            color: var(--text-heading);
        }

        .problem-header-right {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-shrink: 0;
        }

        .done-check-btn {
            background: var(--bg-card);
            border: 1px solid var(--border-strong);
            color: var(--text-muted);
            padding: 0.3rem 0.72rem;
            border-radius: 9999px;
            font-family: 'IBM Plex Sans Thai', sans-serif;
            font-size: 0.76rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.18s ease;
            white-space: nowrap;
        }

        .done-check-btn:hover {
            border-color: var(--success);
            color: var(--success);
        }

        .done-check-btn.is-done {
            background: var(--success);
            border-color: var(--success);
            color: #FFFFFF;
        }

        .chevron-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            font-size: 0.8rem;
            transition: transform 0.25s ease, background 0.2s ease;
        }

        .problem-card.is-open .chevron-icon {
            transform: rotate(180deg);
            background: var(--navy-800);
            color: var(--gold-400);
            border-color: var(--navy-800);
        }

        .problem-body {
            padding: 1.45rem;
        }

        .problem-question {
            font-size: 1rem;
            line-height: 1.82;
            margin-bottom: 1.25rem;
            color: var(--text-main);
            background: var(--bg-subtle);
            padding: 1.2rem 1.35rem;
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }

        .solution-toggle-btn {
            background: linear-gradient(135deg, var(--navy-800), var(--navy-700));
            color: #FFFFFF;
            border: 1px solid rgba(200, 162, 74, 0.35);
            padding: 0.58rem 1.25rem;
            border-radius: 10px;
            font-family: 'IBM Plex Sans Thai', sans-serif;
            font-size: 0.88rem;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s ease;
            box-shadow: var(--shadow-xs);
        }

        .solution-toggle-btn:hover {
            transform: translateY(-1px);
            box-shadow: var(--shadow-sm);
            filter: brightness(1.12);
        }

        .solution-content {
            display: none;
            margin-top: 1.35rem;
            padding-top: 1.35rem;
            border-top: 1.5px dashed var(--border-strong);
        }

        .solution-content.active {
            display: block;
            animation: slideFadeIn 0.28s cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        @keyframes slideFadeIn {
            from { opacity: 0; transform: translateY(-8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .step-block {
            margin-bottom: 1rem;
            padding: 1.05rem 1.25rem;
            background: var(--bg-subtle);
            border-radius: 12px;
            border: 1px solid var(--border-color);
            border-left: 3.5px solid var(--primary-light);
            overflow-x: auto;
        }

        .step-title {
            font-family: 'Kanit', sans-serif;
            font-weight: 600;
            color: var(--text-heading);
            margin-bottom: 0.4rem;
            font-size: 0.98rem;
        }

        .answer-box {
            background: linear-gradient(135deg, rgba(5, 150, 105, 0.09) 0%, rgba(200, 162, 74, 0.08) 100%);
            border: 1.5px solid var(--success);
            padding: 1.15rem 1.35rem;
            border-radius: 12px;
            color: var(--text-heading);
            margin-top: 1.15rem;
            font-size: 1rem;
            font-weight: 500;
        }

        .answer-highlight {
            font-size: 1.18rem;
            font-weight: 700;
            color: var(--success);
            font-family: 'Kanit', sans-serif;
        }

        .pitfall-box {
            background: rgba(220, 38, 38, 0.06);
            border: 1px solid rgba(220, 38, 38, 0.22);
            border-left: 4px solid var(--danger);
            padding: 0.95rem 1.15rem;
            border-radius: 10px;
            margin-top: 0.95rem;
            font-size: 0.91rem;
            color: var(--text-main);
        }

        .empty-state {
            text-align: center;
            padding: 3rem 1.5rem;
            color: var(--text-muted);
            background: var(--bg-subtle);
            border-radius: var(--radius-md);
            border: 1px dashed var(--border-strong);
            display: none;
        }

        /* Dark mode overrides for legacy inline styles in content sections */
        [data-theme="dark"] [style*="background:white"],
        [data-theme="dark"] [style*="background: white"],
        [data-theme="dark"] [style*="background:#ffffff"],
        [data-theme="dark"] [style*="background:#fafafa"] {
            background: var(--bg-elevated) !important;
            border-color: var(--border-color) !important;
            color: var(--text-main) !important;
        }
        [data-theme="dark"] [style*="background:#fefce8"],
        [data-theme="dark"] [style*="background:#fffbeb"] {
            background: rgba(200, 162, 74, 0.12) !important;
            border-color: rgba(200, 162, 74, 0.35) !important;
        }
        [data-theme="dark"] [style*="background:#fff1f2"] {
            background: rgba(220, 38, 38, 0.12) !important;
            border-color: rgba(248, 113, 113, 0.35) !important;
        }
        [data-theme="dark"] [style*="background:#eff6ff"] {
            background: rgba(59, 130, 246, 0.12) !important;
            border-color: rgba(96, 165, 250, 0.35) !important;
        }
        [data-theme="dark"] [style*="background:#f0fdf4"],
        [data-theme="dark"] [style*="background:#ecfdf5"] {
            background: rgba(16, 185, 129, 0.12) !important;
            border-color: rgba(52, 211, 153, 0.35) !important;
        }
        [data-theme="dark"] [style*="color:#4c0519"],
        [data-theme="dark"] [style*="color:#78350f"],
        [data-theme="dark"] [style*="color:#1e3a8a"],
        [data-theme="dark"] [style*="color:#14532d"],
        [data-theme="dark"] [style*="color:#1e293b"],
        [data-theme="dark"] [style*="color:#334155"] {
            color: var(--text-main) !important;
        }
        [data-theme="dark"] [style*="color:#991b1b"] { color: #FCA5A5 !important; }
        [data-theme="dark"] [style*="color:#92400e"],
        [data-theme="dark"] [style*="color:#b45309"] { color: #FCD34D !important; }
        [data-theme="dark"] [style*="color:#1e40af"] { color: #93C5FD !important; }
        [data-theme="dark"] [style*="color:#166534"],
        [data-theme="dark"] [style*="color:#0f766e"] { color: #5EEAD4 !important; }

        /* Floating Back to Top & Toast */
        .back-to-top {
            position: fixed;
            bottom: 1.75rem;
            right: 1.75rem;
            width: 46px;
            height: 46px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--navy-900), var(--navy-700));
            color: var(--gold-400);
            border: 1px solid rgba(200, 162, 74, 0.45);
            box-shadow: var(--shadow-lg);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.15rem;
            opacity: 0;
            pointer-events: none;
            transform: translateY(12px);
            transition: all 0.25s ease;
            z-index: 950;
        }

        .back-to-top.visible {
            opacity: 1;
            pointer-events: auto;
            transform: translateY(0);
        }

        .back-to-top:hover {
            transform: translateY(-3px);
            background: var(--gold-500);
            color: var(--navy-950);
        }

        .toast-notice {
            position: fixed;
            bottom: 1.75rem;
            left: 50%;
            transform: translateX(-50%) translateY(20px);
            background: var(--navy-900);
            color: #FFFFFF;
            border: 1px solid rgba(200, 162, 74, 0.5);
            padding: 0.65rem 1.25rem;
            border-radius: 9999px;
            font-size: 0.86rem;
            font-weight: 500;
            box-shadow: var(--shadow-lg);
            opacity: 0;
            pointer-events: none;
            transition: all 0.25s ease;
            z-index: 1300;
        }

        .toast-notice.show {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }

        /* Footer */
        footer {
            background: linear-gradient(180deg, #0B192C 0%, #060E1A 100%);
            color: #94A3B8;
            padding: 3.5rem 2rem 2.5rem 2rem;
            text-align: center;
            font-size: 0.9rem;
            margin-top: 2rem;
            border-top: 1px solid rgba(200, 162, 74, 0.25);
        }

        footer a { color: var(--gold-400); text-decoration: none; }
        footer a:hover { text-decoration: underline; }

        /* Responsive Breakpoints */
        @media (max-width: 1200px) {
            .page-shell {
                grid-template-columns: 1fr;
                padding: 1.5rem 1rem 2.5rem 1rem;
            }
            .sidebar-toc {
                display: none;
            }
        }

        @media (max-width: 820px) {
            .top-navbar {
                padding: 0.65rem 1rem;
                flex-wrap: wrap;
            }
            .navbar-menu {
                display: none;
            }
            .hero-header {
                padding: 3rem 1.25rem 3.25rem 1.25rem;
            }
            .hero-stats {
                grid-template-columns: repeat(2, 1fr);
            }
            section.card {
                padding: 1.35rem;
                border-radius: 16px;
            }
            .problem-header {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        /* Print styles */
        @media print {
            .top-navbar, .sidebar-toc, .reading-progress-track, .problems-toolbar,
            .solution-toggle-btn, .back-to-top, .toast-notice, .hero-actions,
            .chapter-pills-bar, .done-check-btn, .chevron-icon, .calculator-container {
                display: none !important;
            }
            .page-shell {
                display: block !important;
                padding: 0 !important;
            }
            .solution-content {
                display: block !important;
            }
            body {
                background: white !important;
                color: black !important;
            }
            section.card, .card, .problem-card {
                box-shadow: none !important;
                border: 1px solid #cbd5e1 !important;
                break-inside: avoid;
            }
        }
    </style>
</head>
<body>

<div class="reading-progress-track"><div class="reading-progress-bar" id="readingProgress"></div></div>

<header class="top-navbar">
    <a href="#" class="navbar-brand">
        <span class="brand-emblem">Σ</span>
        <span>4801112 เศรษฐศาสตร์วิศวกรรม</span>
    </a>
    <nav class="navbar-menu" id="topNavMenu">
        <a href="#files" class="nav-link">วิเคราะห์ไฟล์</a>
        <a href="#theory" class="nav-link">สรุป 10 บท</a>
        <a href="#calculator" class="nav-link">คำนวณแฟกเตอร์</a>
        <a href="#problems" class="nav-link">โจทย์ 27 ข้อ</a>
        <a href="#tips" class="nav-link">กับดักข้อสอบ</a>
    </nav>
    <div class="nav-utilities">
        <button class="util-btn" onclick="adjustFontSize(-0.06)" title="ลดขนาดตัวอักษร">A-</button>
        <button class="util-btn" onclick="adjustFontSize(0.06)" title="เพิ่มขนาดตัวอักษร">A+</button>
        <button class="util-btn" id="themeToggleBtn" onclick="toggleTheme()" title="สลับโหมดสว่าง/มืด">🌙 โหมดมืด</button>
        <button class="util-btn" onclick="window.print()" title="พิมพ์หรือบันทึกเป็น PDF">🖨️ PDF</button>
    </div>
</header>

<div class="hero-header">
    <div class="hero-inner">
        <span class="hero-badge">✦ EXECUTIVE STUDY EDITION • คู่มือเตรียมสอบฉบับสมบูรณ์ 2026</span>
        <h1 class="hero-title">การวิเคราะห์ทางเศรษฐศาสตร์วิศวกรรม</h1>
        <h2 class="hero-course-sub">Engineering Economic Analysis (รหัสวิชา 4801112 / 4811112)</h2>
        <p class="hero-subtitle">สรุปเนื้อหาเชิงลึกครบทั้ง 10 บทเรียน วิเคราะห์โครงสร้างเอกสารทั้งหมดในชุดวิชา คลังสูตรพร้อมเครื่องคำนวณแฟกเตอร์ดอกเบี้ยแบบเรียลไทม์ และคลังโจทย์พร้อมเฉลยละเอียดทีละขั้นตอน</p>

        <div class="hero-actions">
            <a href="#theory" class="hero-btn hero-btn-primary">📖 เริ่มอ่านสรุป 10 บท</a>
            <a href="#calculator" class="hero-btn hero-btn-ghost">🧮 เครื่องคำนวณแฟกเตอร์</a>
            <a href="#problems" class="hero-btn hero-btn-ghost">📝 ฝึกทำโจทย์ 27 ข้อ</a>
        </div>

        <div class="hero-stats">
            <div class="stat-item">
                <div class="stat-num">9</div>
                <div class="stat-label">ไฟล์เอกสารอ้างอิง</div>
            </div>
            <div class="stat-item">
                <div class="stat-num">10</div>
                <div class="stat-label">บทเรียนครอบคลุม</div>
            </div>
            <div class="stat-item">
                <div class="stat-num">27</div>
                <div class="stat-label">โจทย์พร้อมเฉลยละเอียด</div>
            </div>
            <div class="stat-item">
                <div class="stat-num">100%</div>
                <div class="stat-label">ตรวจสอบความถูกต้อง</div>
            </div>
        </div>
    </div>
</div>

<div class="page-shell">
    <aside class="sidebar-toc" aria-label="สารบัญเนื้อหา">
        <div class="toc-heading">
            <span>สารบัญเนื้อหา</span>
            <span style="font-size:0.72rem; opacity:0.75;">TOC</span>
        </div>
        <ul class="toc-list" id="sidebarTocList">
            <li><a href="#files" class="toc-link" data-section="files">📁 1. วิเคราะห์ไฟล์ (9 ไฟล์)</a></li>
            <li>
                <a href="#theory" class="toc-link" data-section="theory">📚 2. สรุปเนื้อหา 10 บท</a>
                <ul class="toc-sublist" id="chapterSubToc"></ul>
            </li>
            <li><a href="#calculator" class="toc-link" data-section="calculator">🧮 3. เครื่องคำนวณแฟกเตอร์</a></li>
            <li><a href="#problems" class="toc-link" data-section="problems">📝 4. โจทย์และเฉลย (27 ข้อ)</a></li>
            <li><a href="#tips" class="toc-link" data-section="tips">🎯 5. กับดักข้อสอบ & เทคนิค</a></li>
        </ul>

        <div class="sidebar-progress-box">
            <div class="progress-meta">
                <span>ความคืบหน้าการทำโจทย์</span>
                <strong id="sidebarProgressText" style="color:var(--text-heading);">0 / 27</strong>
            </div>
            <div class="progress-track">
                <div class="progress-fill" id="sidebarProgressBar"></div>
            </div>
        </div>
    </aside>

    <main class="main-container">
'''
