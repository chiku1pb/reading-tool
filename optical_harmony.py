import math
import re
import webbrowser
import os

def apply_cognitive_focus(raw_text):
    words = raw_text.split()
    formatted_words = []

    for word in words:
        match = re.match(r'^(\W*)([\w\-\']+)(\W*)$', word)
        if match:
            prefix, core, suffix = match.groups()
            length = len(core)
            if length == 0:
                formatted_words.append(word)
            elif length == 1:
                formatted_words.append(f"{prefix}<b>{core}</b>{suffix}")
            else:
                midpoint = math.ceil(length / 2)
                first_half = core[:midpoint]
                second_half = core[midpoint:]
                focused_word = f"{prefix}<b>{first_half}</b>{second_half}{suffix}"
                formatted_words.append(focused_word)
        else:
            formatted_words.append(word)
    return " ".join(formatted_words)

sample_text = (
    "This is chaos. Every single day, thousands of professionals and students "
    "waste countless hours staring at data exactly like this. They manually fix "
    "the casing. They hunt for keywords to bold. They try to forcefully drag raw, "
    "messy information into something that is actually readable. It drains time. "
    "It drains energy. And frankly, in 2026, it is completely unacceptable."
)

formatted_text = apply_cognitive_focus(sample_text)

# --- THE NEW INTERACTIVE FRONTEND ---
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Optical Harmony Demo</title>
    <style>
        /* Default State */
        body {{
            font-family: 'Inter', 'Helvetica Neue', sans-serif;
            background-color: #ffffff; /* Stark white */
            color: #000000; /* Stark black */
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 50px;
            transition: all 0.5s ease; /* Smooth elegant transition */
        }}
        .container {{
            max-width: 800px;
            width: 100%;
        }}
        p {{
            font-size: 20px;
            line-height: 1.5;
            transition: all 0.5s ease;
        }}
        
        /* The Jobsian Toggle Button */
        .controls {{ margin-bottom: 40px; }}
        button {{
            background: #18181b;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 30px;
            font-size: 14px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: background 0.3s ease;
        }}
        button:hover {{ background: #3f3f46; }}

        /* OPTICAL HARMONY MODE (For glasses & reading issues) */
        body.harmony-mode {{
            background-color: #F4EED8; /* Warm, anti-glare paper tone */
            color: #2C2C2C; /* Soft charcoal to stop halation */
        }}
        body.harmony-mode p {{
            line-height: 2.2; /* Breathe room for lines */
            letter-spacing: 1.5px; /* Breathe room for letters */
            word-spacing: 4px; /* Breathe room for words */
            font-size: 22px; /* Slight optical bump */
        }}
    </style>
</head>
<body>
    <div class="controls">
        <button onclick="toggleHarmony()" id="harmonyBtn">Enable Optical Harmony</button>
    </div>

    <div class="container">
        <p id="textContent">{formatted_text}</p>
    </div>

    <script>
        function toggleHarmony() {{
            var body = document.body;
            var btn = document.getElementById('harmonyBtn');
            body.classList.toggle('harmony-mode');
            
            if (body.classList.contains('harmony-mode')) {{
                btn.innerHTML = "Disable Optical Harmony";
            }} else {{
                btn.innerHTML = "Enable Optical Harmony";
            }}
        }}
    </script>
</body>
</html>
"""

file_path = os.path.abspath("vision_demo.html")
with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"File created successfully at: {file_path}")
webbrowser.open(f"file://{file_path}")