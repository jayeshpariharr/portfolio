#!/usr/bin/env python3
"""
Resume PDF Generator for Jayesh Parihar - Google APM Candidate
Generates a full 1-page high-density, professional PDF resume with:
- Clickable links for header, case studies, prototypes, and artifacts
- Dedicated separate SKILLS and EDUCATION sections
- Rich, structured PRODUCT PROJECTS section
- Strict 1-page enforcement and 0 forbidden/banned words
"""

import sys
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

pdf_path = "/home/jayesh/.gemini/antigravity/scratch/jayeshpariharr.github.io/assets/resume/Jayesh_Parihar_Google_APM_Resume.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=30,
    rightMargin=30,
    topMargin=22,
    bottomMargin=22
)

# Colors
PRIMARY = colors.HexColor("#0a192f")  # Deep Executive Navy
ACCENT = colors.HexColor("#1d4ed8")   # Clean Tech Blue
MUTED = colors.HexColor("#475569")    # Slate Muted
LINE_COLOR = colors.HexColor("#cbd5e1") # Soft Border Grey
TEXT_COLOR = colors.HexColor("#1e293b") # High Contrast Charcoal

# Typography Styles
font_scale = 1.09
spacer_scale = 1.4

title_style = ParagraphStyle(
    'DocTitle',
    fontName='Helvetica-Bold',
    fontSize=16.5 * font_scale,
    leading=19.5 * font_scale,
    textColor=PRIMARY,
    spaceAfter=1
)

subtitle_style = ParagraphStyle(
    'DocSubtitle',
    fontName='Helvetica-Bold',
    fontSize=8.8 * font_scale,
    leading=11.2 * font_scale,
    textColor=ACCENT,
    spaceAfter=2
)

contact_style = ParagraphStyle(
    'ContactInfo',
    fontName='Helvetica',
    fontSize=7.6 * font_scale,
    leading=10.0 * font_scale,
    textColor=MUTED,
    spaceAfter=2.5
)

summary_style = ParagraphStyle(
    'Summary',
    fontName='Helvetica',
    fontSize=7.3 * font_scale,
    leading=9.7 * font_scale,
    textColor=TEXT_COLOR,
    spaceAfter=2
)

section_heading = ParagraphStyle(
    'SectionHeading',
    fontName='Helvetica-Bold',
    fontSize=8.5 * font_scale,
    leading=10.8 * font_scale,
    textColor=PRIMARY,
    spaceBefore=2.8 * spacer_scale,
    spaceAfter=1.6 * spacer_scale,
    textTransform='uppercase'
)

role_title = ParagraphStyle(
    'RoleTitle',
    fontName='Helvetica-Bold',
    fontSize=8.0 * font_scale,
    leading=10.2 * font_scale,
    textColor=PRIMARY
)

role_meta = ParagraphStyle(
    'RoleMeta',
    fontName='Helvetica-Oblique',
    fontSize=7.5 * font_scale,
    leading=9.8 * font_scale,
    textColor=MUTED,
    alignment=2
)

bullet_style = ParagraphStyle(
    'BulletText',
    fontName='Helvetica',
    fontSize=7.1 * font_scale,
    leading=9.3 * font_scale,
    textColor=TEXT_COLOR,
    leftIndent=7,
    firstLineIndent=-7,
    spaceAfter=1.1 * spacer_scale
)

project_sub_style = ParagraphStyle(
    'ProjectSub',
    fontName='Helvetica',
    fontSize=7.0 * font_scale,
    leading=9.1 * font_scale,
    textColor=TEXT_COLOR,
    leftIndent=7,
    firstLineIndent=-7,
    spaceAfter=1.1 * spacer_scale
)

quiet_style = ParagraphStyle(
    'QuietBreak',
    fontName='Helvetica-Oblique',
    fontSize=6.8 * font_scale,
    leading=8.8 * font_scale,
    textColor=MUTED,
    leftIndent=7,
    spaceAfter=1.2 * spacer_scale
)

skill_style = ParagraphStyle(
    'SkillText',
    fontName='Helvetica',
    fontSize=7.1 * font_scale,
    leading=9.3 * font_scale,
    textColor=TEXT_COLOR,
    spaceAfter=1.1 * spacer_scale
)

edu_style = ParagraphStyle(
    'EduText',
    fontName='Helvetica',
    fontSize=7.2 * font_scale,
    leading=9.5 * font_scale,
    textColor=TEXT_COLOR
)

edu_meta = ParagraphStyle(
    'EduMeta',
    fontName='Helvetica-Oblique',
    fontSize=7.2 * font_scale,
    leading=9.5 * font_scale,
    textColor=MUTED,
    alignment=2
)

story = []

# 1. Header
story.append(Paragraph("JAYESH PARIHAR", title_style))
story.append(Paragraph("Aspiring Associate Product Manager &bull; B2B Marketplaces, SaaS &amp; AI Products", subtitle_style))

contact_text = (
    'Vapi, India &bull; '
    '<a href="tel:+919327056201" color="#1d4ed8"><b>+91 93270 56201</b></a> &bull; '
    '<a href="mailto:pariharjayesh1092@gmail.com" color="#1d4ed8"><b>pariharjayesh1092@gmail.com</b></a> &bull; '
    '<a href="https://linkedin.com/in/jayeshparihar" color="#1d4ed8"><b>linkedin.com/in/jayeshparihar</b></a> &bull; '
    '<a href="https://jayeshpariharr.github.io/portfolio/" color="#1d4ed8"><b>jayeshpariharr.github.io/portfolio/</b></a>'
)
story.append(Paragraph(contact_text, contact_style))
story.append(HRFlowable(width="100%", thickness=1, color=LINE_COLOR, spaceAfter=2.5))

# 2. Executive Summary
story.append(Paragraph("<b>SUMMARY:</b> Product &amp; business development on a 0-to-1 B2B telematics marketplace (enterprise mobility partnership under NDA): turn customer research into PRDs and prototypes, lead UI 2.0 modernization, and coordinate AI assistant integration (LLM catalog grounding). Pivoted model to recurring services (FASTag) and built 8,000+ garage fulfillment network. 4 years customer-facing B2B execution across US, EMEA and APAC.", summary_style))

# 3. Work Experience Section
story.append(Paragraph("WORK EXPERIENCE", section_heading))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=2))

# Role 1: Marketplace
r1_title = '<b>Product &amp; Business Development (Founding Team, 1 of 3)</b> &mdash; B2B Fleet-Telematics Marketplace (NDA) [<a href="https://jayeshpariharr.github.io/portfolio/marketplace.html" color="#1d4ed8"><u>Case Study</u></a>]'
t1 = Table([[Paragraph(r1_title, role_title), Paragraph("Apr 2026 &ndash; Present | Freelance, Remote", role_meta)]], colWidths=[422, 130])
t1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t1)
story.append(Paragraph("&bull; Spearheaded UI 2.0 modernization: authored 12-requirement PRD (P0/P1 scope, user stories, acceptance criteria, business rules) and built clickable prototype with Claude Code (advanced search, autocomplete, Verified filter, GST checkout) adopted by UI team as design reference.", bullet_style))
story.append(Paragraph("&bull; Coordinated technical integration of 'Ask AI' chatbot: owned High-Level Design (HLD) and functional catalog data mapping to eliminate hallucinations; managed API lifecycle, catalog indexing (~0ms latency), authentication protocols, and cross-team UAT testing.", bullet_style))
story.append(Paragraph("&bull; Streamlined checkout funnel with mandatory GSTIN and phone validation to eliminate dispatch/invoicing errors; revamped FASTag section and drove compliance agreement end to end with accounts and CA teams.", bullet_style))
story.append(Paragraph("&bull; Strategic business pivot: transitioned model from one-time hardware sales to recurring operational offerings (FASTag, fuel monitoring); built SI Partner Program (GTM decks, scripts) and championed service network tie-up with 8,000+ garages across India.", bullet_style))
story.append(Paragraph("&bull; Ran discovery with 50+ system integrators; platform order value reached INR 2.47 Cr across 6 months (May &ndash; Oct 2026) with existing clients, including one INR 60 lakh order.", bullet_style))

# Role 2: SDR
story.append(Spacer(1, 1 * spacer_scale))
t2 = Table([[Paragraph("<b>Sales Development Representative</b> &mdash; US B2B SaaS Client ($2.4K&ndash;$4.8K ACV Subscription Product)", role_title),
            Paragraph("Jun 2025 &ndash; Mar 2026 | Freelance, Remote", role_meta)]], colWidths=[422, 130])
t2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t2)
story.append(Paragraph("&bull; Ran continuous weekly A/B testing loops on messaging and CTAs across 2,500+ monthly touches, lifting qualified meetings 35% and reply rate 6% (both relative); booked 15+ qualified meetings monthly with VP Sales, Directors, CMOs, and C-level buyers.", bullet_style))
story.append(Paragraph("&bull; Analyzed buyer sensitivity to subscription vs usage-based pricing models across target segments; fed qualitative friction points back to product leadership to optimize onboarding workflows and pricing packaging.", bullet_style))

# Career break quiet note
story.append(Paragraph("<i>Career breaks: Jun &ndash; Oct 2024 and Jan &ndash; Jun 2025 (preparing for postgraduate study abroad).</i>", quiet_style))

# Role 3: Mobility Foresights
t3 = Table([[Paragraph("<b>Business Development Manager</b> &mdash; Mobility Foresights (Automotive Market Intelligence)", role_title),
            Paragraph("Oct 2024 &ndash; Jan 2025 | Remote", role_meta)]], colWidths=[422, 130])
t3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t3)
story.append(Paragraph("&bull; Closed 17 enterprise deals ($58K) and built a $324.6K pipeline across US, EMEA and APAC ($2.5K&ndash;$7.5K deal size); reached 98% of quota in 4 months.", bullet_style))
story.append(Paragraph("&bull; Led consultative discovery with senior strategy heads at Fortune 1000 accounts (Sony, Samsung, Hitachi, Siemens), mapping custom research modules to client needs.", bullet_style))

# Role 4: 99acres
story.append(Spacer(1, 1 * spacer_scale))
t4 = Table([[Paragraph("<b>Assistant Manager, Corporate Sales</b> &mdash; 99acres.com (Info Edge India Ltd)", role_title),
            Paragraph("Nov 2023 &ndash; Jun 2024 | On-site", role_meta)]], colWidths=[422, 130])
t4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t4)
story.append(Paragraph("&bull; Restructured discovery calls from feature selling to mapping product packages to customer inventory use cases, lifting quarterly quota attainment from 78% to 108%; acquired 30+ net-new corporate B2B logos from scratch via targeted outbound.", bullet_style))
story.append(Paragraph("&bull; Channeled direct customer feedback on listing visibility algorithms and lead management workflows to regional product teams.", bullet_style))

# Role 5: BYJU'S
story.append(Spacer(1, 1 * spacer_scale))
t5 = Table([[Paragraph("<b>Business Development Associate</b> &mdash; BYJU'S (EdTech)", role_title),
            Paragraph("Nov 2022 &ndash; Aug 2023 | On-site", role_meta)]], colWidths=[422, 130])
t5.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t5)
story.append(Paragraph("&bull; Executed 10&ndash;12 live consultative discovery and demo sessions weekly; turned recurring customer objections into a team sales playbook, raising quota attainment from 58% to 92% and closing INR 29 lakh; consistently top 10 of a 50+ person sales division.", bullet_style))

# 4. Product Projects Section
story.append(Spacer(1, 1.4 * spacer_scale))
story.append(Paragraph("PRODUCT PROJECTS (AIRTRIBE AI-FIRST PM PROGRAM, 2026, COURSEWORK)", section_heading))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=2))

# Project 1: Fireflies
p1_title = '<b>Fireflies.ai Commitment Cards (Individual Capstone, Concept Only)</b> &bull; [<a href=\"https://prototype-jayeshparihar-fireflies.lovable.app/\" color=\"#1d4ed8\"><u>Interactive Prototype</u></a>] &bull; [<a href=\"https://jayeshpariharr.github.io/portfolio/assets/docs/Fireflies_Commitment_Cards_PRD.pdf\" color=\"#1d4ed8\"><u>PRD Document</u></a>] &bull; [<a href=\"https://jayeshpariharr.github.io/portfolio/fireflies.html\" color=\"#1d4ed8\"><u>Case Study</u></a>]'
story.append(Paragraph(p1_title, role_title))
story.append(Paragraph("&bull; Uncovered commitment visibility as the top user breakage (8 of 19 interviews across 3 companies) behind a 28% 14-day task resolution rate on real sales calls.", project_sub_style))
story.append(Paragraph("&bull; Ranked 14 solutions using RICE, defined North Star (14-day resolution rate, 45% target), established guardrails, authored complete PRD, 17-slide deck, and built 6-screen interactive Lovable prototype.", project_sub_style))

# Project 2: VitaFit
p2_title = '<b>VitaFit User Retention (StayFit+ &amp; Momentum PRDs)</b> &bull; [<a href=\"https://jayeshpariharr.github.io/portfolio/assets/docs/VitaFit_StayFit_PRD_Design.pdf\" color=\"#1d4ed8\"><u>StayFit+ PRD</u></a>] &bull; [<a href=\"https://jayeshpariharr.github.io/portfolio/assets/docs/VitaFit_Momentum_PRD.pdf\" color=\"#1d4ed8\"><u>Momentum PRD</u></a>]'
story.append(Paragraph(p2_title, role_title))
story.append(Paragraph("&bull; Diagnosed steep day 14&ndash;21 habit drop-off; engineered streak-recovery mechanics with a 5% beta rollout, 6-week A/B testing plan, and explicit ship/no-ship guardrails.", project_sub_style))

# Project 3: Zomato
p3_title = '<b>Zomato Tier-1 Delivery Optimization</b> &bull; [<a href=\"https://jayeshpariharr.github.io/portfolio/assets/docs/Zomato_Delivery_Optimization_Deck.pdf\" color=\"#1d4ed8\"><u>10-Slide Deck</u></a>] &bull; [<a href=\"https://jayeshpariharr.github.io/portfolio/assets/docs/Zomato_Delivery_Optimization_PRD.pdf\" color=\"#1d4ed8\"><u>PRD &amp; Metric Tree</u></a>]'
story.append(Paragraph(p3_title, role_title))
story.append(Paragraph("&bull; Deconstructed 7-stage consumer checkout funnel; mapped 8 prioritized initiatives across an impact vs effort matrix and constructed a full North Star metric tree.", project_sub_style))

# 5. Skills Section (SEPARATE)
story.append(Spacer(1, 1.4 * spacer_scale))
story.append(Paragraph("SKILLS", section_heading))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=2))
story.append(Paragraph("<b>AI &amp; Prototyping:</b> Prompt engineering, AI workflow design, Claude, Claude Code, ChatGPT, Gemini, AI-enabled search, LLM catalog grounding (~0ms latency), conversational bots.", skill_style))
story.append(Paragraph("<b>Product Management:</b> User discovery &amp; interviews, PRD writing, user stories, acceptance criteria, success metrics, RICE/MoSCoW prioritization, prototyping, outbound A/B testing, funnel analysis.", skill_style))
story.append(Paragraph("<b>Tools &amp; Analytics:</b> HubSpot, Excel/Google Sheets, Notion | Learning: Python, LLM APIs (RAG, agents).", skill_style))

# 6. Education Section (SEPARATE)
story.append(Spacer(1, 1.4 * spacer_scale))
story.append(Paragraph("EDUCATION", section_heading))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=2))

edu_table = Table([
    [Paragraph("<b>AI-First Product Manager Program</b> &mdash; Airtribe", edu_style),
     Paragraph("Jul 2026 &ndash; Oct 2026", edu_meta)],
    [Paragraph("<b>Bachelor of Business Administration (BBA - Marketing)</b> &mdash; Parul University", edu_style),
     Paragraph("2019 &ndash; 2022", edu_meta)]
], colWidths=[422, 130])
edu_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
    ('TOPPADDING', (0,0), (-1,-1), 0.5),
]))
story.append(edu_table)

doc.build(story)
print("Built PDF successfully at:", pdf_path)
