import streamlit as st
import streamlit.components.v1 as components

# 1. Setup page layout
st.set_page_config(
    page_title="NES Emulator Hub",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("🕹️ Retro NES Emulator")
st.caption("Built with Streamlit & EmulatorJS. Run your favorite retro tests directly in the browser.")

# 2. Complete HTML/JS/CSS Stack with Custom Sidebar Button Relocation
html_lines = [
    "<!DOCTYPE html>",
    "<html>",
    "<head>",
    '    <meta charset="UTF-8">',
    '    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">',
    "    <style>",
    "        body { background-color: #0e1117; color: #ffffff; font-family: system-ui, sans-serif; margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; }",
    "        #picker-container { text-align: center; padding: 40px 20px; border: 2px dashed #31333f; border-radius: 10px; background: #131722; width: 80%; max-width: 500px; }",
    "        .btn-upload { display: inline-block; background-color: #ff4b4b; color: white; padding: 12px 24px; border-radius: 8px; font-weight: 600; cursor: pointer; margin-top: 15px; }",
    '        input[type="file"] { display: none; }',
    "        #game-container { display: none; width: 100%; height: 650px; }",
    "        #game { width: 100%; height: 100%; }",
    "",
    "        /* LANDSCAPE CORRECTIONS */",
    "        @media (min-width: 500px) {",
    "            #game-container { height: 380px !important; }",
    "",
    "            /* Reset the default center-clumping layout styles applied by the engine */",
    "            .ejs-sidebar-move {",
    "                position: absolute !important;",
    "                transform: none !important;",
    "                top: auto !important;",
    "                bottom: 15px !important;",
    "                z-index: 999999 !important;",
    "            }",
    "",
    "            /* Securely tuck Select & Start into the bottom-left black bar */",
    '            [data-control="select"] { left: 20px !important; }',
    '            [data-control="start"] { left: 90px !important; }',
    "",
    "            /* Securely tuck Fast & Slow into the bottom-right black bar */",
    '            [data-control="fast"] { right: 90px !important; left: auto !important; }',
    '            [data-control="slow"] { right: 20px !important; left: auto !important; }',
    "        }",
    "    </style>",
    "</head>",
    "<body>",
    "",
    '    <div id="picker-container">',
    "        <h3>Load your NES Game</h3>",
    '        <p style="color: #a3a8b4; font-size: 14px;">Select a .nes or .zip ROM file from your phone storage to start playing.</p>',
    '        <label class="btn-upload">Choose File<input type="file" id="rom-file" accept=".nes,.zip"></label>',
    "    </div>",
    "",
    '    <div id="game-container"><div id="game"></div></div>',
    "",
    '    <script type="text/javascript">',
    "        document.getElementById('rom-file').addEventListener('change', function(e) {",
    "            const file = e.target.files[0];",
    "            if (!file) return;",
    "            ",
    "            window.EJS_player = '#game';",
    "            window.EJS_core = 'nes';",
    "            window.EJS_pathtodata = 'https://cdn.emulatorjs.org/stable/data/';",
    "            window.EJS_gameUrl = URL.createObjectURL(file);",
    "            ",
    "            document.getElementById('picker-container').style.display = 'none';",
    "            document.getElementById('game-container').style.display = 'block';",
    "            ",
    "            const loaderScript = document.createElement('script');",
    "            loaderScript.src = 'https://cdn.emulatorjs.org/stable/data/loader.js';",
    "            document.body.appendChild(loaderScript);",
    "",
    "            // Background scanner to find the text buttons and apply our sidebar layout",
    "            setInterval(() => {",
    "                const gameDiv = document.getElementById('game');",
    "                if (!gameDiv) return;",
    "                const elements = gameDiv.getElementsByTagName('*');",
    "                for (let el of elements) {",
    "                    const txt = (el.textContent || el.innerText || '').trim();",
    "                    if (['Start', 'Select', 'Fast', 'Slow'].includes(txt)) {",
    "                        el.classList.add('ejs-sidebar-move');",
    "                        el.setAttribute('data-control', txt.toLowerCase());",
    "                    }",
    "                }",
    "            }, 500);",
    "        });",
    "    </script>",
    "</body>",
    "</html>"
]

# 3. Compile and play layout inside Streamlit
emulator_html = "\n".join(html_lines)
components.html(emulator_html, height=720, scrolling=False)

st.info("💡 Note: Game files are processed locally on your device and are never uploaded to any server.")
