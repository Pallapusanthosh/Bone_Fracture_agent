from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf(data, filename="report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    def add_title(text):
        content.append(Paragraph(f"<b>{text}</b>", styles["Title"]))
        content.append(Spacer(1, 20))

    def add_section(title, text):
        content.append(Paragraph(f"<b>{title}</b>", styles["Heading2"]))
        content.append(Spacer(1, 10))
        content.append(Paragraph(text, styles["BodyText"]))
        content.append(Spacer(1, 15))

    def add_list(title, items):
        content.append(Paragraph(f"<b>{title}</b>", styles["Heading2"]))
        content.append(Spacer(1, 10))
        for item in items:
            content.append(Paragraph(f"- {item}", styles["BodyText"]))
        content.append(Spacer(1, 15))

    # 🧾 Title
    add_title("Bone Fracture Analysis Report")

    # 🧍 Patient / Scan Info
    add_section("Patient / Scan Information",
                f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 🔍 Detection Summary
    add_section("Detection Summary", data.get("summary", ""))

    # 🧠 Clinical Assessment
    add_section("Clinical Assessment",
                "This assessment is generated using AI-based analysis of fracture patterns and medical knowledge.")

    # ⚠️ Severity
    severity = data.get("severity", {})
    add_section("Severity Analysis",
                f"Level: {severity.get('level', '')}<br/>Reason: {severity.get('reason', '')}")

    # 🩺 Symptoms
    add_list("Symptoms & Observations", data.get("symptoms", []))

    # 🚨 Emergency Signs
    add_list("Emergency Indicators", data.get("emergency", []))

    # 🆘 First Aid
    add_list("Immediate First Aid", data.get("first_aid", []))

    # 💊 Treatment
    add_list("Treatment Plan", data.get("treatment", []))

    # 🔄 Recovery
    add_section("Recovery & Rehabilitation", data.get("recovery", ""))

    # ⚡ Risks (NEW SMART ADDITION)
    add_section("Risk Factors & Complications",
                "Potential risks include improper healing, stiffness, nerve damage, or chronic pain if not treated properly.")

    # 🏥 Doctor Visit
    add_section("When to Seek Immediate Care",
                "Seek immediate medical attention if severe pain, numbness, deformity, or loss of movement occurs.")

    # 🤖 AI Notes
    add_section("AI Confidence & Notes",
                "This report is generated using AI models and should be used for informational purposes only.")

    # ⚠️ Disclaimer
    add_section("Disclaimer",
                "This is not a substitute for professional medical advice. Please consult a qualified doctor.")

    doc.build(content)

    return filename