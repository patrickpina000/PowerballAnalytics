import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os

# Create reports folder if missing
os.makedirs("reports", exist_ok=True)

# Load data
hot_numbers = pd.read_csv("reports/top_hot_numbers.csv")
cold_numbers = pd.read_csv("reports/top_cold_numbers.csv")
emv = -1.28  # Update if needed

pdf_file = "reports/Powerball_Report.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter
styles = getSampleStyleSheet()
y_position = height - 50

# Title
c.setFont("Helvetica-Bold", 18)
c.drawString(50, y_position, "Powerball Analytics Report")
y_position -= 30

# EMV Summary
c.setFont("Helvetica", 12)
c.drawString(50, y_position, f"Estimated EMV per ticket: ${emv:.2f}")
y_position -= 30

# Add Trend Plot
plot_file = "reports/number_trends.png"
if os.path.exists(plot_file):
    c.drawImage(plot_file, 50, y_position - 300, width=500, height=300)
    y_position -= 320

# Hot Numbers Table
c.drawString(50, y_position, "Top 10 Hot Numbers")
y_position -= 20
hot_data = [hot_numbers.columns.tolist()] + hot_numbers.values.tolist()
table = Table(hot_data, colWidths=[70]*len(hot_data[0]))
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ]
    )
)
table.wrapOn(c, width, height)
table.drawOn(c, 50, y_position - (20*len(hot_data)))
y_position -= (20*len(hot_data)) + 20

# Cold Numbers Table
c.drawString(50, y_position, "Top 10 Cold Numbers")
y_position -= 20
cold_data = [cold_numbers.columns.tolist()] + cold_numbers.values.tolist()
table = Table(cold_data, colWidths=[70]*len(cold_data[0]))
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0,0), (-1,0), colors.lightcoral),
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ]
    )
)
table.wrapOn(c, width, height)
table.drawOn(c, 50, y_position - (20*len(cold_data)))

# Save PDF
c.save()
print(f"✅ PDF report generated: {pdf_file}")
