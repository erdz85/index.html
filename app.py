import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Setup page layout
st.set_page_config(
    page_title="NES Emulator Hub",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("🕹️ Retro NES Emulator")
st.caption("Built with Streamlit & EmulatorJS. Run your favorite retro tests directly in the browser.")

# 2. Safely read the HTML file from local storage
# This protects your deployment from mobile copy/paste syntax errors
html_file_path = os.path.join(os.path.dirname(__file__), "emulator.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        emulator_html = f.read()
    
    # Inject the HTML component smoothly
    components.html(emulator_html, height=720, scrolling=False)
else:
    st.error("Missing 'emulator.html' file! Please make sure it is created in the same repository folder.")

st.info("💡 Note: Game files are processed locally on your device and are never uploaded to any server.")
            border-radius: 10px;
            background: #131722;
            width: 80%;
            max-width: 500px;
        }
        .btn-upload {
            display: inline-block;
            background-color: #ff4b4b;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 15px;
        }
        input[type="file"] { display: none; }
        
        /* DEFAULT VIEW: Standard setup for vertical portrait view */
        #game-container {
            display: none;
            width: 100%;
            height: 650px;
        }
        #game { width: 100%; height: 100%; }

        /* RESPONSIVE LANDSCAPE FIX: When the phone rotates sideways, the width stretches.
           We force the core container to drop to 380px high so the bottom-anchored 
           Start, Select, and Speed utilities remain perfectly visible on screen. */
        @media (min-width: 500px) {
            #game-container {
                height: 380px !important;
            }
        }
    </style>
</head>
<body>

    <div id="picker-container">
        <h3>Load your NES Game</h3>
        <p style="color: #a3a8b4; font-size: 14px;">Select a .nes or .zip ROM file from your phone storage to start playing.</p>
        <label class="btn-upload">
            Choose File
            <input type="file" id="rom-file" accept=".nes,.zip">
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
</html>"""

# 3. Inject the HTML component into the Streamlit interface
components.html(emulator_html, height=720, scrolling=False)

st.info("💡 Note: Game files are processed locally on your device and are never uploaded to any server.")
            border-radius: 10px;
            background: #131722;
            width: 80%;
            max-width: 500px;
        }
        .btn-upload {
            display: inline-block;
            background-color: #ff4b4b;
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
            <input type="file" id="rom-file" accept=".nes,.zip">
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
</html>"""

# 3. Inject the HTML component into the Streamlit interface
components.html(emulator_html, height=720, scrolling=False)

st.info("💡 Note: Game files are processed locally on your device and are never uploaded to any server.")
