from flask import Flask, request, jsonify

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔥 ULTIMATE SMART CALCULATOR 🔥</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon-blue: #00f3ff;
            --neon-pink: #ff00ff;
            --neon-green: #39ff14;
            --neon-yellow: #ffff00;
            --neon-red: #ff073a;
            --bg-dark: #050510;
            --glass: rgba(255, 255, 255, 0.05);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: var(--bg-dark);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Orbitron', monospace;
            overflow: hidden;
            perspective: 1000px;
        }

        /* Animated Background Grid */
        .bg-grid {
            position: fixed;
            top: 0;
            left: 0;
            width: 200%;
            height: 200%;
            background-image:
                linear-gradient(rgba(0, 243, 255, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 243, 255, 0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: gridMove 20s linear infinite;
            z-index: -2;
        }

        @keyframes gridMove {
            0% { transform: translate(0, 0); }
            100% { transform: translate(-50px, -50px); }
        }

        /* Floating particles */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: var(--neon-blue);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--neon-blue);
            animation: float 15s infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) rotate(720deg); opacity: 0; }
        }

        /* Main Calculator Container */
        .calc-container {
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.1s ease-out;
        }

        .calculator {
            background: linear-gradient(145deg, rgba(20, 20, 40, 0.9), rgba(10, 10, 30, 0.95));
            border: 2px solid var(--neon-blue);
            border-radius: 25px;
            padding: 30px;
            width: 380px;
            box-shadow:
                0 0 30px rgba(0, 243, 255, 0.3),
                inset 0 0 30px rgba(0, 243, 255, 0.1);
            position: relative;
            overflow: hidden;
        }

        .calculator::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(
                45deg,
                transparent 30%,
                rgba(0, 243, 255, 0.1) 50%,
                transparent 70%
            );
            animation: shimmer 3s infinite;
        }

        @keyframes shimmer {
            0% { transform: translateX(-100%) rotate(45deg); }
            100% { transform: translateX(100%) rotate(45deg); }
        }

        /* Title */
        .title {
            text-align: center;
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--neon-blue);
            text-shadow:
                0 0 10px var(--neon-blue),
                0 0 20px var(--neon-blue),
                0 0 40px var(--neon-blue);
            margin-bottom: 20px;
            animation: titlePulse 2s ease-in-out infinite;
            position: relative;
            z-index: 1;
        }

        @keyframes titlePulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        /* Display */
        .display-wrapper {
            position: relative;
            margin-bottom: 25px;
            z-index: 1;
        }

        #display {
            width: 100%;
            height: 70px;
            background: rgba(0, 0, 0, 0.6);
            border: 2px solid var(--neon-pink);
            border-radius: 15px;
            color: var(--neon-green);
            font-family: 'Orbitron', monospace;
            font-size: 1.8rem;
            font-weight: 700;
            text-align: right;
            padding: 0 20px;
            outline: none;
            box-shadow:
                0 0 20px rgba(255, 0, 255, 0.3),
                inset 0 0 20px rgba(0, 0, 0, 0.5);
            text-shadow: 0 0 10px var(--neon-green);
            transition: all 0.3s;
        }

        #display.error {
            border-color: var(--neon-red);
            color: var(--neon-red);
            text-shadow: 0 0 10px var(--neon-red);
            animation: shake 0.5s;
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            20% { transform: translateX(-10px); }
            40% { transform: translateX(10px); }
            60% { transform: translateX(-10px); }
            80% { transform: translateX(10px); }
        }

        .display-label {
            position: absolute;
            top: -10px;
            left: 15px;
            background: var(--bg-dark);
            padding: 0 10px;
            color: var(--neon-pink);
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        /* Buttons Grid */
        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            position: relative;
            z-index: 1;
        }

        button {
            height: 65px;
            border: none;
            border-radius: 15px;
            font-family: 'Orbitron', monospace;
            font-size: 1.2rem;
            font-weight: 700;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: all 0.15s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        button::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }

        button:active::before {
            width: 300px;
            height: 300px;
        }

        button:active {
            transform: scale(0.92);
        }

        .btn-num {
            background: linear-gradient(145deg, #1a1a3e, #0f0f2e);
            color: var(--neon-blue);
            border: 1px solid rgba(0, 243, 255, 0.3);
            box-shadow:
                0 4px 15px rgba(0, 0, 0, 0.3),
                0 0 10px rgba(0, 243, 255, 0.1);
        }

        .btn-num:hover {
            background: linear-gradient(145deg, #25255a, #1a1a3e);
            box-shadow:
                0 0 20px rgba(0, 243, 255, 0.4),
                0 0 40px rgba(0, 243, 255, 0.2);
            transform: translateY(-2px);
        }

        .btn-op {
            background: linear-gradient(145deg, #3a1a5a, #2a0f4e);
            color: var(--neon-pink);
            border: 1px solid rgba(255, 0, 255, 0.3);
            box-shadow:
                0 4px 15px rgba(0, 0, 0, 0.3),
                0 0 10px rgba(255, 0, 255, 0.1);
        }

        .btn-op:hover {
            background: linear-gradient(145deg, #4a2580, #3a1a5a);
            box-shadow:
                0 0 20px rgba(255, 0, 255, 0.4),
                0 0 40px rgba(255, 0, 255, 0.2);
            transform: translateY(-2px);
        }

        .btn-eq {
            background: linear-gradient(145deg, #0a5a1a, #064e12);
            color: var(--neon-green);
            border: 1px solid rgba(57, 255, 20, 0.3);
            box-shadow:
                0 4px 15px rgba(0, 0, 0, 0.3),
                0 0 10px rgba(57, 255, 20, 0.1);
            grid-column: span 2;
        }

        .btn-eq:hover {
            background: linear-gradient(145deg, #0d7a24, #0a5a1a);
            box-shadow:
                0 0 30px rgba(57, 255, 20, 0.5),
                0 0 60px rgba(57, 255, 20, 0.3);
            transform: translateY(-2px);
        }

        .btn-clear {
            background: linear-gradient(145deg, #5a0a0a, #4e0606);
            color: var(--neon-red);
            border: 1px solid rgba(255, 7, 58, 0.3);
            box-shadow:
                0 4px 15px rgba(0, 0, 0, 0.3),
                0 0 10px rgba(255, 7, 58, 0.1);
            grid-column: span 2;
        }

        .btn-clear:hover {
            background: linear-gradient(145deg, #7a0d0d, #5a0a0a);
            box-shadow:
                0 0 20px rgba(255, 7, 58, 0.5),
                0 0 40px rgba(255, 7, 58, 0.3);
            transform: translateY(-2px);
        }

        .btn-special {
            background: linear-gradient(145deg, #5a4a0a, #4e3f06);
            color: var(--neon-yellow);
            border: 1px solid rgba(255, 255, 0, 0.3);
            font-size: 0.9rem;
        }

        .btn-special:hover {
            box-shadow: 0 0 20px rgba(255, 255, 0, 0.4);
        }

        /* Reaction Text */
        .reaction {
            text-align: center;
            margin-top: 15px;
            font-size: 0.9rem;
            min-height: 25px;
            color: var(--neon-yellow);
            text-shadow: 0 0 10px var(--neon-yellow);
            font-family: 'Press Start 2P', cursive;
            position: relative;
            z-index: 1;
        }

        /* History */
        .history-section {
            margin-top: 20px;
            max-height: 150px;
            overflow-y: auto;
            position: relative;
            z-index: 1;
        }

        .history-title {
            color: var(--neon-pink);
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-bottom: 10px;
            text-align: center;
            text-shadow: 0 0 10px var(--neon-pink);
        }

        .history-item {
            background: rgba(255, 255, 255, 0.05);
            border-left: 3px solid var(--neon-green);
            padding: 8px 12px;
            margin-bottom: 6px;
            border-radius: 0 8px 8px 0;
            font-size: 0.85rem;
            color: var(--neon-blue);
            animation: slideIn 0.3s ease-out;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        @keyframes slideIn {
            from { transform: translateX(-20px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        .history-item .result-val {
            color: var(--neon-green);
            font-weight: 700;
        }

        /* Confetti Canvas */
        #confetti-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
        }

        /* Scrollbar */
        .history-section::-webkit-scrollbar {
            width: 6px;
        }
        .history-section::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 3px;
        }
        .history-section::-webkit-scrollbar-thumb {
            background: var(--neon-blue);
            border-radius: 3px;
        }

        /* Easter egg animation for special numbers */
        .epic-mode {
            animation: epicPulse 0.5s ease-in-out infinite alternate;
        }

        @keyframes epicPulse {
            from { box-shadow: 0 0 30px var(--neon-green); }
            to { box-shadow: 0 0 60px var(--neon-yellow), 0 0 100px var(--neon-pink); }
        }

        /* Scanline effect */
        .scanlines {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                to bottom,
                rgba(255, 255, 255, 0),
                rgba(255, 255, 255, 0) 50%,
                rgba(0, 0, 0, 0.1) 50%,
                rgba(0, 0, 0, 0.1)
            );
            background-size: 100% 4px;
            pointer-events: none;
            z-index: 1000;
            opacity: 0.3;
        }

        /* Mode Toggle */
        .mode-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 100;
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid var(--neon-blue);
            color: var(--neon-blue);
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-family: 'Orbitron', monospace;
            font-size: 0.7rem;
            transition: all 0.3s;
        }
        .mode-toggle:hover {
            box-shadow: 0 0 20px var(--neon-blue);
        }
    </style>
</head>
<body>
    <div class="bg-grid"></div>
    <div class="particles" id="particles"></div>
    <div class="scanlines"></div>
    <canvas id="confetti-canvas"></canvas>

    <button class="mode-toggle" onclick="toggleSound()">🔊 Sound: ON</button>

    <div class="calc-container" id="calcContainer">
        <div class="calculator" id="calculator">
            <div class="title">🧠 ULTIMATE CALC</div>

            <div class="display-wrapper">
                <span class="display-label">Input Stream</span>
                <input id="display" readonly placeholder="0">
            </div>

            <div class="buttons">
                <button class="btn-special" onclick="press('(')">(</button>
                <button class="btn-special" onclick="press(')')">)</button>
                <button class="btn-special" onclick="press('%')">%</button>
                <button class="btn-op" onclick="press('/')">÷</button>

                <button class="btn-num" onclick="press('7')">7</button>
                <button class="btn-num" onclick="press('8')">8</button>
                <button class="btn-num" onclick="press('9')">9</button>
                <button class="btn-op" onclick="press('*')">×</button>

                <button class="btn-num" onclick="press('4')">4</button>
                <button class="btn-num" onclick="press('5')">5</button>
                <button class="btn-num" onclick="press('6')">6</button>
                <button class="btn-op" onclick="press('-')">-</button>

                <button class="btn-num" onclick="press('1')">1</button>
                <button class="btn-num" onclick="press('2')">2</button>
                <button class="btn-num" onclick="press('3')">3</button>
                <button class="btn-op" onclick="press('+')">+</button>

                <button class="btn-num" onclick="press('0')">0</button>
                <button class="btn-num" onclick="press('.')">.</button>
                <button class="btn-eq" onclick="calculate()">=</button>

                <button class="btn-clear" onclick="clearDisplay()">💥 CLEAR</button>
                <button class="btn-special" onclick="backspace()">⌫</button>
                <button class="btn-special" onclick="randomCalc()">🎲</button>
            </div>

            <div class="reaction" id="reaction"></div>

            <div class="history-section" id="history">
                <div class="history-title">📜 Battle Log</div>
            </div>
        </div>
    </div>

    <script>
    // ================= AUDIO ENGINE =================
    let audioCtx = null;
    let soundEnabled = true;

    function initAudio() {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }

    function playTone(freq, type='sine', duration=0.1, volume=0.1) {
        if (!soundEnabled || !audioCtx) return;
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.value = freq;
        gain.gain.setValueAtTime(volume, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
    }

    function playClick() { initAudio(); playTone(800, 'sine', 0.05, 0.08); }
    function playOp() { initAudio(); playTone(400, 'square', 0.08, 0.05); }
    function playClear() { initAudio(); playTone(200, 'sawtooth', 0.3, 0.1); }
    function playSuccess() {
        initAudio();
        [523, 659, 784, 1047].forEach((f, i) => setTimeout(() => playTone(f, 'sine', 0.15, 0.1), i * 80));
    }
    function playError() {
        initAudio();
        [150, 100, 80].forEach((f, i) => setTimeout(() => playTone(f, 'sawtooth', 0.2, 0.1), i * 100));
    }
    function playEpic() {
        initAudio();
        const notes = [261, 329, 392, 523, 659, 784, 1047, 1319];
        notes.forEach((f, i) => setTimeout(() => playTone(f, 'square', 0.2, 0.08), i * 60));
    }

    function toggleSound() {
        soundEnabled = !soundEnabled;
        document.querySelector('.mode-toggle').innerText = soundEnabled ? '🔊 Sound: ON' : '🔇 Sound: OFF';
    }

    // ================= PARTICLES =================
    function createParticles() {
        const container = document.getElementById('particles');
        for (let i = 0; i < 30; i++) {
            const p = document.createElement('div');
            p.className = 'particle';
            p.style.left = Math.random() * 100 + '%';
            p.style.animationDelay = Math.random() * 15 + 's';
            p.style.animationDuration = (10 + Math.random() * 10) + 's';
            const colors = ['#00f3ff', '#ff00ff', '#39ff14', '#ffff00'];
            p.style.background = colors[Math.floor(Math.random() * colors.length)];
            p.style.boxShadow = `0 0 10px ${p.style.background}`;
            container.appendChild(p);
        }
    }
    createParticles();

    // ================= CONFETTI =================
    const confettiCanvas = document.getElementById('confetti-canvas');
    const ctx = confettiCanvas.getContext('2d');
    let confetti = [];

    function resizeConfetti() {
        confettiCanvas.width = window.innerWidth;
        confettiCanvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeConfetti);
    resizeConfetti();

    function spawnConfetti(amount=100) {
        const colors = ['#00f3ff', '#ff00ff', '#39ff14', '#ffff00', '#ff073a', '#ffffff'];
        for (let i = 0; i < amount; i++) {
            confetti.push({
                x: window.innerWidth / 2,
                y: window.innerHeight / 2,
                vx: (Math.random() - 0.5) * 20,
                vy: (Math.random() - 0.5) * 20 - 5,
                size: Math.random() * 8 + 4,
                color: colors[Math.floor(Math.random() * colors.length)],
                rotation: Math.random() * 360,
                rotationSpeed: (Math.random() - 0.5) * 10,
                life: 1
            });
        }
    }

    function updateConfetti() {
        ctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
        confetti.forEach((p, i) => {
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.3;
            p.rotation += p.rotationSpeed;
            p.life -= 0.01;

            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.rotate(p.rotation * Math.PI / 180);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = p.life;
            ctx.fillRect(-p.size/2, -p.size/2, p.size, p.size);
            ctx.restore();

            if (p.life <= 0) confetti.splice(i, 1);
        });
        requestAnimationFrame(updateConfetti);
    }
    updateConfetti();

    // ================= TILT EFFECT =================
    const calcContainer = document.getElementById('calcContainer');
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 20;
        calcContainer.style.transform = `rotateY(${x}deg) rotateX(${-y}deg)`;
    });

    // ================= CALCULATOR LOGIC =================
    let current = "";
    const display = document.getElementById("display");
    const reaction = document.getElementById("reaction");
    const history = document.getElementById("history");

    const reactions = {
        normal: [
            "Nice math! 🎯", "Crunching numbers! 🔢", "Math wizard! 🧙",
            "Smooth! 😎", "Calculated! 📊", "Boom! 💥"
        ],
        big: [
            "Whoa, big number! 🤯", "Infinity called, wants its number back! 🌌",
            "That's a lot of damage! 💪", "Absolute unit! 🏔️"
        ],
        small: [
            "Tiny but mighty! 🐜", "Precision! 🔬", "Microscopic! 🦠"
        ],
        error: [
            "Oof! 💀", "Math doesn't work that way! 🤔", "Try again! 🎲",
            "Error 404: Logic not found! 🔍"
        ],
        epic: [
            "LEGENDARY! 🏆", "EPIC WIN! 🎉", "UNSTOPPABLE! 🔥",
            "GODLIKE! 👑", "INSANE! 🤩"
        ]
    };

    const epicNumbers = [69, 420, 1337, 666, 777, 9000, 80085];

    function press(val) {
        initAudio();
        if ('+-*/%'.includes(val)) playOp();
        else playClick();
        current += val;
        display.value = current;
        display.classList.remove('error');
    }

    function clearDisplay() {
        initAudio();
        playClear();
        current = "";
        display.value = "";
        display.classList.remove('error');
        reaction.innerText = "Cleared! 🧹";
    }

    function backspace() {
        initAudio();
        playClick();
        current = current.slice(0, -1);
        display.value = current;
    }

    function randomCalc() {
        initAudio();
        playClick();
        const ops = ['+', '-', '*', '/'];
        const a = Math.floor(Math.random() * 100);
        const b = Math.floor(Math.random() * 100) + 1;
        const op = ops[Math.floor(Math.random() * ops.length)];
        current = `${a}${op}${b}`;
        display.value = current;
        setTimeout(calculate, 300);
    }

    function getReaction(result) {
        if (epicNumbers.includes(Math.abs(Math.floor(result)))) return reactions.epic;
        if (result === "Error") return reactions.error;
        if (Math.abs(result) > 1000000) return reactions.big;
        if (Math.abs(result) < 0.01 && result !== 0) return reactions.small;
        return reactions.normal;
    }

    async function calculate() {
        if (!current) return;
        initAudio();

        try {
            const res = await fetch("/calc", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({input: current})
            });

            const data = await res.json();
            const result = data.result;

            if (result === "Error") {
                playError();
                display.classList.add('error');
                reaction.innerText = reactions.error[Math.floor(Math.random() * reactions.error.length)];
            } else {
                const numResult = parseFloat(result);
                const reactionPool = getReaction(numResult);
                reaction.innerText = reactionPool[Math.floor(Math.random() * reactionPool.length)];

                if (reactionPool === reactions.epic) {
                    playEpic();
                    spawnConfetti(200);
                    document.getElementById('calculator').classList.add('epic-mode');
                    setTimeout(() => document.getElementById('calculator').classList.remove('epic-mode'), 2000);
                } else if (reactionPool === reactions.big) {
                    playSuccess();
                    spawnConfetti(100);
                } else {
                    playSuccess();
                    spawnConfetti(30);
                }

                addHistory(current, result);
                current = String(result);
                display.value = current;
                display.classList.remove('error');
            }
        } catch (e) {
            playError();
            display.classList.add('error');
            reaction.innerText = "Network error! 📡💥";
        }
    }

    function addHistory(expr, result) {
        const item = document.createElement("div");
        item.className = "history-item";
        item.innerHTML = `<span>${expr}</span><span class="result-val">= ${result}</span>`;
        history.appendChild(item);
        history.scrollTop = history.scrollHeight;

        // Keep only last 10
        while (history.children.length > 11) {
            history.removeChild(history.children[1]);
        }
    }

    // Keyboard support
    document.addEventListener('keydown', (e) => {
        const key = e.key;
        if (/[0-9.\+\-\*\/\(\)%]/.test(key)) press(key);
        else if (key === 'Enter') calculate();
        else if (key === 'Escape') clearDisplay();
        else if (key === 'Backspace') backspace();
    });
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE

def parse_text(text):
    text = text.lower()
    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("times", "*")
    text = text.replace("divided by", "/")
    return text

@app.route("/calc", methods=["POST"])
def calc():
    data = request.json
    expr = parse_text(data["input"])

    try:
        result = eval(expr)
    except:
        result = "Error"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)

