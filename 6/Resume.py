from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

# ── OUTPUT PATH — apni machine pe yeh badlo ──
OUTPUT_PATH = "Humam_Resume_Updated.pdf"

# Page setup
doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=A4,
    rightMargin=15*mm,
    leftMargin=15*mm,
    topMargin=12*mm,
    bottomMargin=12*mm
)

# Colors
DARK = colors.HexColor('#1a1a2e')
ACCENT = colors.HexColor('#2563eb')
GRAY = colors.HexColor('#4b5563')
LIGHT_GRAY = colors.HexColor('#9ca3af')

# Styles
styles = getSampleStyleSheet()

name_style = ParagraphStyle('name', fontSize=22, fontName='Helvetica-Bold',
    textColor=DARK, alignment=TA_CENTER, spaceAfter=12)

title_style = ParagraphStyle('title', fontSize=11, fontName='Helvetica',
    textColor=ACCENT, alignment=TA_CENTER, spaceAfter=4)

contact_style = ParagraphStyle('contact', fontSize=8.5, fontName='Helvetica',
    textColor=GRAY, alignment=TA_CENTER, spaceAfter=8)

section_style = ParagraphStyle('section', fontSize=10, fontName='Helvetica-Bold',
    textColor=ACCENT, spaceBefore=8, spaceAfter=3)

body_style = ParagraphStyle('body', fontSize=9, fontName='Helvetica',
    textColor=DARK, spaceAfter=2, leading=13)

bullet_style = ParagraphStyle('bullet', fontSize=9, fontName='Helvetica',
    textColor=DARK, spaceAfter=2, leading=13, leftIndent=12, firstLineIndent=-8)

small_style = ParagraphStyle('small', fontSize=8.5, fontName='Helvetica',
    textColor=GRAY, spaceAfter=1)

italic_style = ParagraphStyle('italic', fontSize=9, fontName='Helvetica-Oblique',
    textColor=GRAY, spaceAfter=2)

story = []

# ════════════════════════════════
# HEADER
# ════════════════════════════════
story.append(Paragraph("Humam Ul Islam", name_style))
story.append(Paragraph("AI Engineer &nbsp;|&nbsp; Java Backend Developer", title_style))
story.append(Paragraph(
    "humam.alam19@gmail.com &nbsp;&nbsp;·&nbsp;&nbsp; +91-6397919096 &nbsp;&nbsp;·&nbsp;&nbsp; "
    "<a href='https://linkedin.com/in/humamulislam' color='#2563eb'>LinkedIn</a> &nbsp;&nbsp;·&nbsp;&nbsp; "
    "<a href='https://github.com/humamul' color='#2563eb'>GitHub</a>",
    contact_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceAfter=6))

# ════════════════════════════════
# PROFESSIONAL SUMMARY
# ════════════════════════════════
story.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT_GRAY, spaceAfter=4))
story.append(Paragraph(
    "Java Backend Developer with 2+ years of production experience building scalable microservices "
    "and distributed systems using Spring Boot. Currently specializing in AI Engineering — constructing "
    "RAG pipelines, LLM integrations, and multi-agent systems using Python, LangChain, and Spring AI. "
    "Seeking roles that bridge production-grade backend engineering with AI/LLM product development.",
    body_style))

# ════════════════════════════════
# TECHNICAL SKILLS
# ════════════════════════════════
story.append(Paragraph("TECHNICAL SKILLS", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT_GRAY, spaceAfter=4))

skills_data = [
    ["AI / ML Engineering",
     "Python, NumPy, Pandas, scikit-learn, LangChain, RAG Pipelines, "
     "Vector Databases (FAISS, ChromaDB), LLM APIs (OpenAI, Ollama), Spring AI"],
    ["Java Backend",
     "Java, Spring Boot, Spring Security, Hibernate ORM, Microservices, RESTful APIs, "
     "JWT, Feign Client, Multithreading (CAS, ReentrantLock, ThreadPool)"],
    ["Databases",
     "MySQL (RDBMS), MongoDB (NoSQL), ClickHouse (OLAP), Apache Solr"],
    ["Messaging & DevOps",
     "Apache Kafka, RazorPay Gateway, Docker, Git, Swagger / OpenAPI"],
]

for label, value in skills_data:
    row_table = Table(
        [[Paragraph(f"<b>{label}:</b>", body_style),
          Paragraph(value, body_style)]],
        colWidths=[46*mm, 134*mm]
    )
    row_table.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
        ('TOPPADDING',    (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    story.append(row_table)

# ════════════════════════════════
# PROFESSIONAL EXPERIENCE
# ════════════════════════════════
story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT_GRAY, spaceAfter=4))

def exp_header_table(left, right):
    t = Table(
        [[Paragraph(left, body_style), Paragraph(right, small_style)]],
        colWidths=[120*mm, 60*mm]
    )
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
        ('TOPPADDING',    (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('ALIGN',         (1, 0), (1, 0),   'RIGHT'),
    ]))
    return t

# --- Platform Commons ---
story.append(exp_header_table(
    "<b>Platform Commons</b> — Software Engineer",
    "Feb 2023 – Mar 2025 | Remote, India"
))

bullets_exp = [
    "<b>Multi-Tenancy Architecture:</b> Designed and maintained a high-scale multi-tenant system "
    "handling data from thousands of clients per tenant — enforced strict data isolation, reducing "
    "cross-tenant query leakage incidents to zero via session-level parameterized validation.",

    "<b>Security:</b> Mitigated critical SQL injection vulnerabilities by implementing session-level "
    "validation and parameterized queries across 15+ API endpoints.",

    "<b>Payments:</b> Integrated Razorpay API for recurring monthly donations; orchestrated "
    "asynchronous event pipelines via Feign Client and Apache Kafka, reducing payment processing "
    "latency by ~30%.",

    "<b>Big Data &amp; Analytics:</b> Architected a real-time Telemetry system using ClickHouse (OLAP), "
    "enabling analytics dashboards to query millions of events with sub-second response times.",

    "<b>Session Management:</b> Engineered cookie-based tracking for logged-out users — maintained "
    "data continuity while preserving stateless API principles across microservices.",

    "<b>Search Optimization:</b> Implemented Apache Solr indexing, improving full-text search "
    "query retrieval speed by ~40%.",

    "<b>API Documentation:</b> Automated Swagger/OpenAPI documentation across new microservices, "
    "reducing developer onboarding time significantly.",
]
for b in bullets_exp:
    story.append(Paragraph(f"• {b}", bullet_style))

# --- AI Upskilling (Gap explanation) ---
story.append(Spacer(1, 5))
story.append(exp_header_table(
    "<b>Self-Directed AI Engineering Upskilling</b>",
    "Mar 2025 – Present"
))

upskill_bullets = [
    "Building end-to-end RAG pipelines: document ingestion, semantic chunking, vector retrieval, "
    "LLM generation (LangChain + FAISS + OpenAI API)",

    "Implementing ML fundamentals hands-on: Linear/Logistic Regression, Decision Trees, "
    "Random Forest, model evaluation (Precision, Recall, F1, AUC)",

    "Studying Transformer architecture, self-attention, BERT embeddings, and "
    "sentence-transformers for semantic search",

    "Re-implementing RAG pipeline in Spring AI (Java) — bridges backend engineering "
    "with AI product development",
]
for b in upskill_bullets:
    story.append(Paragraph(f"• {b}", bullet_style))

# ════════════════════════════════
# PROJECTS
# ════════════════════════════════
story.append(Paragraph("PROJECTS", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT_GRAY, spaceAfter=4))

projects = [
    {
        "title": "RAG Pipeline System",
        "status": "In Progress — Phase 4",
        "tech": "Python · LangChain · FAISS · OpenAI API · FastAPI",
        "bullets": [
            "End-to-end retrieval-augmented generation: PDF ingestion → semantic chunking → "
            "vector indexing → LLM response generation",
            "Implementing hybrid search (keyword + vector) and reranking for improved "
            "retrieval precision",
        ]
    },
    {
        "title": "Multi-Agent Code Review System",
        "status": "Planned — Phase 6",
        "tech": "Python · CrewAI · Spring Boot · Java",
        "bullets": [
            "Three-agent pipeline: Java code analyzer → JUnit test writer → code reviewer",
            "Bridges Spring Boot production experience with modern agentic AI systems",
        ]
    },
    {
        "title": "Blog Application — Secure Content Platform",
        "status": "Completed",
        "tech": "Java · Spring Boot · Spring Security · Hibernate · MySQL · JWT",
        "bullets": [
            "JWT authentication with HttpOnly Cookies and RBAC (Admin/User) via Spring "
            "PreAuthorize — prevents XSS/CSRF attacks",
            "Scalable RESTful CRUD APIs for Blogs, Comments, Categories with standardized "
            "JSON responses",
            "One-to-Many/Many-to-Many ORM mappings with Hibernate for data integrity",
        ]
    },
]

for proj in projects:
    proj_t = Table(
        [[Paragraph(f"<b>{proj['title']}</b>", body_style),
          Paragraph(proj['status'], small_style)]],
        colWidths=[110*mm, 70*mm]
    )
    proj_t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
        ('TOPPADDING',    (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('ALIGN',         (1, 0), (1, 0),   'RIGHT'),
    ]))
    story.append(proj_t)
    story.append(Paragraph(f"<i>Tech Stack: {proj['tech']}</i>", italic_style))
    for b in proj['bullets']:
        story.append(Paragraph(f"• {b}", bullet_style))
    story.append(Spacer(1, 4))

# ════════════════════════════════
# EDUCATION
# ════════════════════════════════
story.append(Paragraph("EDUCATION", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT_GRAY, spaceAfter=4))

edu_data = [
    ["Masai School — Java Backend Development",
     "Feb 2022 – Feb 2023 | Bengaluru"],
    ["Shaheed Bhagat Singh College, Delhi University — B.Com (Honours)",
     "Jul 2018 – Jul 2021 | Delhi"],
]
for title, date in edu_data:
    edu_t = Table(
        [[Paragraph(f"<b>{title}</b>", body_style),
          Paragraph(date, small_style)]],
        colWidths=[120*mm, 60*mm]
    )
    edu_t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
        ('TOPPADDING',    (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('ALIGN',         (1, 0), (1, 0),   'RIGHT'),
    ]))
    story.append(edu_t)

# ════════════════════════════════
# BUILD PDF
# ════════════════════════════════
doc.build(story)
print(f"Resume saved to: {OUTPUT_PATH}")