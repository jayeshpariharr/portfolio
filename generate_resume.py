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
    leftMargin=32,
    rightMargin=32,
    topMargin=26,
    bottomMargin=26
)

styles = getSampleStyleSheet()

PRIMARY = colors.HexColor("#0f172a")
ACCENT = colors.HexColor("#1d4ed8")
MUTED = colors.HexColor("#475569")
LINE_COLOR = colors.HexColor("#cbd5e1")

title_style = ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=16, leading=19, textColor=PRIMARY, spaceAfter=1)
subtitle_style = ParagraphStyle('DocSubtitle', fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=ACCENT, spaceAfter=2)
contact_style = ParagraphStyle('ContactInfo', fontName='Helvetica', fontSize=7.8, leading=10, textColor=MUTED, spaceAfter=3)
summary_style = ParagraphStyle('Summary', fontName='Helvetica', fontSize=7.5, leading=9.8, textColor=colors.HexColor("#1e293b"), spaceAfter=2)
section_heading = ParagraphStyle('SectionHeading', fontName='Helvetica-Bold', fontSize=8.8, leading=11, textColor=PRIMARY, spaceBefore=3, spaceAfter=1.5, textTransform='uppercase')
role_title = ParagraphStyle('RoleTitle', fontName='Helvetica-Bold', fontSize=8.2, leading=10.5, textColor=PRIMARY)
role_meta = ParagraphStyle('RoleMeta', fontName='Helvetica-Oblique', fontSize=7.8, leading=10, textColor=MUTED, alignment=2)
bullet_style = ParagraphStyle('BulletText', fontName='Helvetica', fontSize=7.2, leading=9.4, textColor=colors.HexColor("#1e293b"), leftIndent=7, firstLineIndent=-7, spaceAfter=1)
quiet_style = ParagraphStyle('QuietBreak', fontName='Helvetica-Oblique', fontSize=7.0, leading=9, textColor=MUTED, leftIndent=7, spaceAfter=1.5)

story = []

# Header
story.append(Paragraph("JAYESH PARIHAR", title_style))
story.append(Paragraph("Aspiring Associate Product Manager &bull; B2B Marketplaces, SaaS &amp; AI Products", subtitle_style))
story.append(Paragraph("Vapi, India &bull; +91 93270 56201 &bull; pariharjayesh1092@gmail.com &bull; linkedin.com/in/jayeshparihar &bull; https://jayeshpariharr.github.io/portfolio/", contact_style))
story.append(HRFlowable(width="100%", thickness=1, color=LINE_COLOR, spaceAfter=2))

# Summary
story.append(Paragraph("<b>SUMMARY:</b> Product and business development on a 0-to-1 B2B telematics marketplace (enterprise mobility partnership under NDA): turn user research into PRDs and prototypes, lead UI 2.0 modernization, and coordinate AI assistant integration (LLM catalog grounding). Pivoted model to recurring services (FASTag) and built 8,000+ garage fulfillment network. 4 years customer-facing B2B execution across US, EMEA and APAC.", summary_style))

# Experience
story.append(Paragraph("WORK EXPERIENCE", section_heading))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=2))

# Role 1: Marketplace
t1 = Table([[Paragraph("<b>Product &amp; Business Development (Founding Team, 1 of 3)</b> &mdash; B2B Fleet-Telematics Marketplace (NDA)", role_title),
            Paragraph("Apr 2026 &ndash; Present | Freelance, Remote", role_meta)]], colWidths=[415, 133])
t1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t1)

story.append(Paragraph("&bull; Spearheaded UI 2.0 modernization: authored 12-requirement PRD (P0/P1 scope, user stories, acceptance criteria, business rules) and built clickable prototype with Claude Code (advanced search, autocomplete, Verified filter, GST checkout) adopted as UI team design reference.", bullet_style))
story.append(Paragraph("&bull; Coordinated technical integration of 'Ask AI' chatbot: owned High-Level Design (HLD) and functional catalog data mapping to eliminate hallucinations; managed API lifecycle, catalog indexing (~0ms latency), authentication protocols, and cross-team UAT testing.", bullet_style))
story.append(Paragraph("&bull; Streamlined checkout funnel with mandatory GSTIN and phone validation to eliminate dispatch/invoicing errors; revamped FASTag section and drove compliance agreement end to end with accounts and CA teams.", bullet_style))
story.append(Paragraph("&bull; Strategic business pivot: transitioned model from one-time hardware sales to recurring operational offerings (FASTag, fuel monitoring); built SI Partner Program (GTM decks, scripts) and championed service network tie-up with 8,000+ garages across India.", bullet_style))
story.append(Paragraph("&bull; Ran discovery with 50+ system integrators; platform order value reached INR 2.47 Cr across 6 months (May &ndash; Oct 2026) with existing clients, including one INR 60 lakh order.", bullet_style))

# Role 2: SDR
story.append(Spacer(1, 1))
t2 = Table([[Paragraph("<b>Sales Development Representative</b> &mdash; US B2B SaaS Client ($2.4K&ndash;$4.8K ACV Subscription Product)", role_title),
            Paragraph("Jun 2025 &ndash; Mar 2026 | Freelance, Remote", role_meta)]], colWidths=[415, 133])
t2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t2)
story.append(Paragraph("&bull; Ran continuous weekly A/B testing loops on messaging and CTAs across 2,500+ monthly touches, lifting qualified meetings 35% and reply rate 6% (both relative).", bullet_style))
story.append(Paragraph("&bull; Conducted consultative discovery with VP Sales, Directors, CMOs and C-level buyers; booked 15+ qualified meetings a month across SMB, mid-market, and enterprise accounts.", bullet_style))
story.append(Paragraph("&bull; Analyzed buyer sensitivity to subscription vs usage-based pricing models; fed friction points back to product leadership to optimize onboarding and pricing tiers.", bullet_style))

# Career break quiet note
story.append(Paragraph("<i>Career breaks: Jun &ndash; Oct 2024 and Jan &ndash; Jun 2025 (preparing for postgraduate study abroad).</i>", quiet_style))

# Role 3: Mobility Foresights
t3 = Table([[Paragraph("<b>Business Development Manager</b> &mdash; Mobility Foresights (Automotive Market Intelligence)", role_title),
            Paragraph("Oct 2024 &ndash; Jan 2025 | Remote", role_meta)]], colWidths=[415, 133])
t3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t3)
story.append(Paragraph("&bull; Closed 17 enterprise deals ($58K) and built a $324.6K pipeline across US, EMEA and APAC ($2.5K&ndash;$7.5K deal size); reached 98% of quota in 4 months.", bullet_style))
story.append(Paragraph("&bull; Led consultative discovery with senior strategy heads at Fortune 1000 accounts (Sony, Samsung, Hitachi, Siemens), mapping custom research modules to client needs.", bullet_style))

# Role 4: 99acres
story.append(Spacer(1, 1))
t4 = Table([[Paragraph("<b>Assistant Manager, Corporate Sales</b> &mdash; 99acres.com (Info Edge India Ltd)", role_title),
            Paragraph("Nov 2023 &ndash; Jun 2024 | On-site", role_meta)]], colWidths=[415, 133])
t4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t4)
story.append(Paragraph("&bull; Restructured discovery calls from feature selling to mapping product packages to customer inventory use cases, lifting quarterly quota attainment from 78% to 108%.", bullet_style))
story.append(Paragraph("&bull; Acquired 30+ net-new corporate B2B logos from scratch via targeted outbound; channeled customer feedback on listing visibility and lead workflows to regional product teams.", bullet_style))

# Role 5: BYJU'S
story.append(Spacer(1, 1))
t5 = Table([[Paragraph("<b>Business Development Associate</b> &mdash; BYJU'S (EdTech)", role_title),
            Paragraph("Nov 2022 &ndash; Aug 2023 | On-site", role_meta)]], colWidths=[415, 133])
t5.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
story.append(t5)
story.append(Paragraph("&bull; Executed 10&ndash;12 live consultative discovery and demo sessions weekly; turned recurring customer objections into a team sales playbook, raising quota attainment from 58% to 92%.", bullet_style))
story.append(Paragraph("&bull; Closed INR 29 lakh in revenue; consistently ranked in top 10 of a 50+ person sales division; trained and onboarded incoming associates on qualification frameworks.", bullet_style))

# Product Work / Coursework Capstone
story.append(Spacer(1, 1.5))
story.append(Paragraph("PRODUCT PROJECTS (Airtribe AI-First PM Program, 2026, coursework)", section_heading))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=2))

story.append(Paragraph("&bull; <b>Fireflies.ai Commitment Cards (individual capstone, concept only):</b> Interviewed 19 people across 3 companies and tested on a live client call; visibility was top breakage (8 of 19) behind a 28% resolution rate in 14 days. Ranked 14 ideas with RICE, set North Star (14-day resolution rate), documented what not to build, and delivered PRD, 17-slide deck and 6-screen Lovable prototype.", bullet_style))
story.append(Paragraph("&bull; <b>VitaFit retention:</b> Traced day 14&ndash;21 drop-off to 2 root causes; wrote streak-recovery PRD with 5% beta rollout, 6-week A/B test plan and ship/no-ship criteria.", bullet_style))
story.append(Paragraph("&bull; <b>Zomato funnel analysis:</b> Mapped 7-stage ordering funnel, ranked fixes by impact vs effort and built North Star metric tree linking 8 initiatives.", bullet_style))

# Skills & Education
story.append(Spacer(1, 1.5))
story.append(Paragraph("SKILLS &amp; EDUCATION", section_heading))
story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceAfter=2))

story.append(Paragraph("<b>AI &amp; Prototyping:</b> Prompt engineering, AI workflow design, Claude, Claude Code, ChatGPT, Gemini, AI-enabled search, LLM catalog grounding &amp; chatbot features.", bullet_style))
story.append(Paragraph("<b>Product Management:</b> User research &amp; discovery, PRDs, user stories, acceptance criteria, success metrics, RICE/MoSCoW prioritization, prototyping, A/B testing (outbound), funnel analysis.", bullet_style))
story.append(Paragraph("<b>Tools &amp; Education:</b> HubSpot, Excel/Google Sheets, Notion | Learning: Python, LLM APIs (RAG, agents) | <b>BBA (Marketing)</b>, Parul University (2019&ndash;2022) &bull; <b>AI-First PM Program</b>, Airtribe (Jul&ndash;Oct 2026).", bullet_style))

doc.build(story)
print("Built PDF successfully")
