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

# 2. Pure HTML/JS Emulator Engine
# This runs completely client-side in an iframe, keeping gameplay buttery smooth.
emulator_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body {
            background-color: #0e1117; /* Matches default Streamlit dark theme */
            color: #ffffff;
            font-family: system-ui, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 700px;
        }
        #picker-container {
            text-align: center;
            padding: 40px 20px;
            border: 2px dashed #31333f;
            border-radius: 10px;
            background: #131722;
            width: 80%;
            max-width: 500px;
        }
        .btn-upload {
            display: inline-block;
            background-color: #ff4b4b; /* Streamlit Red accents */
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 15px;
        }
        input[type="file"] { display: none; }
        #game-container {
            display: none;
            width: 100%;
            height: 650px;
        }
        #game { width: 100%; height: 100%; }
    </style>
</head>
<body>

    <div id="picker-container">
        <h3>Load your NES Game</h3>
        <p style="color: #a3a8b4; font-size: 14px;">Select a .nes ROM file from your phone storage to start playing.</p>
        <label class="btn-upload">
            Choose File
            <input type="file" id="rom-file" accept=".nes">
        </label>
    </div>

    <div id="game-container">
        <div id="game"></div>
    </div>

    <script type="text/javascript">
        document.getElementById('rom-file').addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (!file) return;

            window.EJS_player = '#game';
            window.EJS_core = 'nes'; 
            window.EJS_pathtodata = 'https://cdn.emulatorjs.org/stable/data/';
            window.EJS_gameUrl = URL.createObjectURL(file); 

            document.getElementById('picker-container').style.display = 'none';
            document.getElementById('game-container').style.display = 'block';

            const loaderScript = document.createElement('script');
            loaderScript.src = 'https://cdn.emulatorjs.org/stable/data/loader.js';
            document.body.appendChild(loaderScript);
        });
    </script>
</body>
</html>
"""

# 3. Inject the HTML component into the Streamlit interface
components.html(emulator_html, height=720, scrolling=False)

st.info("💡 Note: Game files are processed locally on your device and are never uploaded to any server.")
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 15px;
            transition: background 0.2s;
        }
        .btn-upload:active { background-color: #0056b3; }
        input[type="file"] { display: none; }
        #game-container {
            display: none;
            width: 100vw;
            height: 100vh;
        }
        #game { width: 100%; height: 100%; }
    </style>
</head>
<body>

    <!-- File selection view shown on launch -->
    <div id="picker-container">
        <h2>NES Mobile Web Emulator</h2>
        <p>Tap below to select a <strong>.nes</strong> ROM file from your device storage to begin testing.</p>
        <label class="btn-upload">
            Load ROM File
            <input type="file" id="rom-file" accept=".nes">
        </label>
    </div>

    <!-- Container where the actual emulator canvas will render -->
    <div id="game-container">
        <div id="game"></div>
    </div>

    <script type="text/javascript">
        document.getElementById('rom-file').addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (!file) return;

            // 1. Establish the emulator configuration hooks
            window.EJS_player = '#game';
            window.EJS_core = 'nes'; 
            window.EJS_pathtodata = 'https://cdn.emulatorjs.org/stable/data/'; // Points directly to the CDN binaries
            window.EJS_gameUrl = URL.createObjectURL(file); // Packages the local file into a browser-readable stream

            // 2. Swap layout visibility smoothly
            document.getElementById('picker-container').style.display = 'none';
            document.getElementById('game-container').style.display = 'block';

            // 3. Dynamically append the engine loader script to execute the setup
            const loaderScript = document.createElement('script');
            loaderScript.src = 'https://cdn.emulatorjs.org/stable/data/loader.js';
            document.body.appendChild(loaderScript);
        });
    </script>
</body>
</html>
