import os

WORKSHEET_DIR = "worksheets"
OUTPUT_FILE = "worksheets.html"

def generate_html():
    files = [f for f in os.listdir(WORKSHEET_DIR) if f.lower().endswith(".pdf")]
    files.sort()

    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>BrillaBee Worksheets</title>
  <link rel='stylesheet' href='style.css'>
</head>
<body>
  <header class="simple-header">
    <h1>📄 Worksheets</h1>
    <p><a href="index.html" class="back-link">← Back to Home</a></p>
  </header>
  <main class="card-list">
    """
    for file in files:
        title = file.replace(".pdf", "")
        html += f"""
    <div class="worksheet-card">
      <h3>{title}</h3>
      <a href="{WORKSHEET_DIR}/{file}" target="_blank" class="download-btn">📥 Download PDF</a>
    </div>
    """
    html += """
  </main>
  <footer><p>Made by Swathi Maistry ✨</p></footer>
</body>
</html>
"""
    with open(OUTPUT_FILE, "w") as f:
        f.write(html)
    print(f"✅ Generated {OUTPUT_FILE} with {len(files)} PDFs.")

if __name__ == "__main__":
    generate_html()
