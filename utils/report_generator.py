import os
from fpdf import FPDF

def generate_report(target, results, report_format, output_dir):
    if report_format == "pdf":
        generate_pdf_report(target, results, output_dir)
    elif report_format == "markdown":
        generate_markdown_report(target, results, output_dir)

def generate_pdf_report(target, results, output_dir):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, f"ReconAI Report for {target}", 0, 1, "C")
    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    for module, data in results.items():
        pdf.cell(200, 10, f"--- {module.upper()} Results ---", 0, 1, "L")
        pdf.set_font("Arial", "", 10)
        for key, value in data.items():
            pdf.multi_cell(0, 5, f"{key.replace("_", " ").title()}: {value}")
        pdf.ln(5)

    output_path = os.path.join(output_dir, f"{target}_report.pdf")
    pdf.output(output_path)
    print(f"PDF report generated: {output_path}")

def generate_markdown_report(target, results, output_dir):
    markdown_content = f"# ReconAI Report for {target}\n\n"

    for module, data in results.items():
        markdown_content += f"## {module.upper()} Results\n\n"
        for key, value in data.items():
            markdown_content += f"- **{key.replace("_", " ").title()}**: {value}\n"
        markdown_content += "\n"

    output_path = os.path.join(output_dir, f"{target}_report.md")
    with open(output_path, "w") as f:
        f.write(markdown_content)
    print(f"Markdown report generated: {output_path}")


