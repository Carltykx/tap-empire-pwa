
# Create the main HTML file with embedded PWA functionality
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#6366f1">
    <meta name="description" content="Tap Empire Infinity - Build your empire by tapping and upgrading">
    <title>Tap Empire Infinity</title>
    <link rel="manifest" href="manifest.json">
    <link rel="icon" type="image/png" href="icon-192.png">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4c1d95 100%);
            min-height: 100vh;
            color: white;
            overflow-x: hidden;
            user-select: none;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            padding: 20px 0;
            margin-bottom: 20px;
        }

        h1 {
            font-size: 2.5em;
            text-shadow: 0 0 20px rgba(99, 102, 241, 0.8);
            letter-spacing: 2px;
        }

        .coin-display {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            margin-bottom: 30px;
            border: 2px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        }

        .coin-amount {
            font-size: 3em;
            font-weight: bold;
            color: #fbbf24;
            text-shadow: 0 0 10px rgba(251, 191, 36, 0.5);
            margin-bottom: 10px;
        }

        .coin-label {
            font-size: 1.2em;
            color: #e5e7eb;
        }

        .tap-button {
            width: 250px;
            height: 250px;
            margin: 40px auto;
            background: radial-gradient(circle, #fbbf24 0%, #f59e0b 50%, #d97706 100%);
            border-radius: 50%;
            border: 8px solid #fff;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3em;
            box-shadow: 0 10px 40px rgba(251, 191, 36, 0.5);
            transition: transform 0.1s, box-shadow 0.1s;
            position: relative;
        }

        .tap-button:active {
            transform: scale(0.95);
            box-shadow: 0 5px 20px rgba(251, 191, 36, 0.7);
        }

        .tap-button::before {
            content: '💰';
            font-size: 1.2em;
        }

        .passive-income {
            text-align: center;
            margin: 20px 0;
            font-size: 1.2em;
            color: #86efac;
        }

        .upgrades-section {
            margin-top: 40px;
        }

        .upgrades-title {
            font-size: 2em;
            text-align: center;
            margin-bottom: 30px;
            color: #fbbf24;
        }

        .upgrades-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }

        @media (min-width: 768px) {
            .upgrades-grid {
                grid-template-columns: 1fr 1fr;
            }
        }

        .upgrade-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 25px;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: transform 0.2s, border-color 0.2s;
        }

        .upgrade-card:hover {
            transform: translateY(-5px);
            border-color: rgba(251, 191, 36, 0.5);
        }

        .upgrade-name {
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 10px;
            color: #fbbf24;
        }

        .upgrade-description {
            font-size: 0.9em;
            color: #d1d5db;
            margin-bottom: 15px;
        }

        .upgrade-level {
            font-size: 1.1em;
            margin-bottom: 10px;
            color: #a5b4fc;
        }

        .upgrade-cost {
            font-size: 1.2em;
            margin-bottom: 15px;
            color: #fbbf24;
            font-weight: bold;
        }

        .upgrade-button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            border: none;
            border-radius: 10px;
            color: white;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.2s;
        }

        .upgrade-button:hover:not(:disabled) {
            background: linear-gradient(135deg, #059669 0%, #047857 100%);
            transform: scale(1.05);
        }

        .upgrade-button:disabled {
            background: #4b5563;
            cursor: not-allowed;
            opacity: 0.5;
        }

        .floating-number {
            position: fixed;
            font-size: 2em;
            font-weight: bold;
            color: #fbbf24;
            pointer-events: none;
            animation: float-up 1s ease-out forwards;
            text-shadow: 0 0 10px rgba(0, 0, 0, 0.8);
        }

        @keyframes float-up {
            0% {
                opacity: 1;
                transform: translateY(0);
            }
            100% {
                opacity: 0;
                transform: translateY(-100px);
            }
        }

        .install-prompt {
            background: rgba(99, 102, 241, 0.9);
            padding: 15px;
            text-align: center;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            display: none;
            z-index: 1000;
        }

        .install-button {
            background: white;
            color: #6366f1;
            border: none;
            padding: 10px 30px;
            border-radius: 8px;
            font-size: 1em;
            font-weight: bold;
            cursor: pointer;
            margin: 10px;
        }

        .footer {
            text-align: center;
            padding: 30px 0;
            color: #9ca3af;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>EMPIRE WEALTH</h1>
        </header>

        <div class="coin-display">
            <div class="coin-amount" id="coinAmount">0</div>
            <div class="coin-label">coins</div>
        </div>

        <div class="tap-button" id="tapButton"></div>

        <div class="passive-income">
            <span id="passiveIncome">Passive Income: 0/sec</span>
        </div>

        <div class="upgrades-section">
            <h2 class="upgrades-title">Upgrades</h2>
            <div class="upgrades-grid">
                <div class="upgrade-card">
                    <div class="upgrade-name">Tap Power</div>
                    <div class="upgrade-description">Increase coins per tap</div>
                    <div class="upgrade-level">Level: <span id="tapPowerLevel">0</span></div>
                    <div class="upgrade-cost">Cost: <span id="tapPowerCost">10</span></div>
                    <button class="upgrade-button" id="tapPowerButton">Upgrade</button>
                </div>

                <div class="upgrade-card">
                    <div class="upgrade-name">Auto Tapper</div>
                    <div class="upgrade-description">Earn coins automatically per second</div>
                    <div class="upgrade-level">Level: <span id="autoTapperLevel">0</span></div>
                    <div class="upgrade-cost">Cost: <span id="autoTapperCost">50</span></div>
                    <button class="upgrade-button" id="autoTapperButton">Upgrade</button>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>Tap Empire Infinity PWA v1.0</p>
            <p>Your progress is automatically saved</p>
        </div>
    </div>

    <div class="install-prompt" id="installPrompt">
        <p>Install Tap Empire to your home screen!</p>
        <button class="install-button" id="installButton">Install App</button>
        <button class="install-button" id="dismissButton">Maybe Later</button>
    </div>

    <script>
        // Game State
        let gameState = {
            coins: 0,
            tapPower: 0,
            autoTapper: 0,
            lastSaveTime: Date.now()
        };

        // Upgrade configurations
        const upgrades = {
            tapPower: {
                baseCost: 10,
                costMultiplier: 2,
                valuePerLevel: 1
            },
            autoTapper: {
                baseCost: 50,
                costMultiplier: 2,
                valuePerLevel: 1
            }
        };

        // DOM Elements
        const coinAmountEl = document.getElementById('coinAmount');
        const tapButton = document.getElementById('tapButton');
        const passiveIncomeEl = document.getElementById('passiveIncome');
        
        const tapPowerLevelEl = document.getElementById('tapPowerLevel');
        const tapPowerCostEl = document.getElementById('tapPowerCost');
        const tapPowerButtonEl = document.getElementById('tapPowerButton');
        
        const autoTapperLevelEl = document.getElementById('autoTapperLevel');
        const autoTapperCostEl = document.getElementById('autoTapperCost');
        const autoTapperButtonEl = document.getElementById('autoTapperButton');

        // Format large numbers
        function formatNumber(num) {
            if (num >= 1000000000) return (num / 1000000000).toFixed(2) + 'B';
            if (num >= 1000000) return (num / 1000000).toFixed(2) + 'M';
            if (num >= 1000) return (num / 1000).toFixed(2) + 'K';
            return Math.floor(num).toString();
        }

        // Calculate upgrade cost
        function getUpgradeCost(upgradeType, level) {
            const config = upgrades[upgradeType];
            return Math.floor(config.baseCost * Math.pow(config.costMultiplier, level));
        }

        // Update display
        function updateDisplay() {
            coinAmountEl.textContent = formatNumber(gameState.coins);
            
            tapPowerLevelEl.textContent = gameState.tapPower;
            tapPowerCostEl.textContent = formatNumber(getUpgradeCost('tapPower', gameState.tapPower));
            
            autoTapperLevelEl.textContent = gameState.autoTapper;
            autoTapperCostEl.textContent = formatNumber(getUpgradeCost('autoTapper', gameState.autoTapper));
            
            const passiveIncome = gameState.autoTapper * upgrades.autoTapper.valuePerLevel;
            passiveIncomeEl.textContent = `Passive Income: ${formatNumber(passiveIncome)}/sec`;
            
            // Update button states
            tapPowerButtonEl.disabled = gameState.coins < getUpgradeCost('tapPower', gameState.tapPower);
            autoTapperButtonEl.disabled = gameState.coins < getUpgradeCost('autoTapper', gameState.autoTapper);
        }

        // Show floating number animation
        function showFloatingNumber(x, y, amount) {
            const floatingNum = document.createElement('div');
            floatingNum.className = 'floating-number';
            floatingNum.textContent = '+' + formatNumber(amount);
            floatingNum.style.left = x + 'px';
            floatingNum.style.top = y + 'px';
            document.body.appendChild(floatingNum);
            
            setTimeout(() => {
                floatingNum.remove();
            }, 1000);
        }

        // Handle tap
        tapButton.addEventListener('click', (e) => {
            const tapValue = 1 + (gameState.tapPower * upgrades.tapPower.valuePerLevel);
            gameState.coins += tapValue;
            updateDisplay();
            
            showFloatingNumber(e.pageX, e.pageY, tapValue);
        });

        // Handle upgrades
        tapPowerButtonEl.addEventListener('click', () => {
            const cost = getUpgradeCost('tapPower', gameState.tapPower);
            if (gameState.coins >= cost) {
                gameState.coins -= cost;
                gameState.tapPower++;
                updateDisplay();
                saveGame();
            }
        });

        autoTapperButtonEl.addEventListener('click', () => {
            const cost = getUpgradeCost('autoTapper', gameState.autoTapper);
            if (gameState.coins >= cost) {
                gameState.coins -= cost;
                gameState.autoTapper++;
                updateDisplay();
                saveGame();
            }
        });

        // Auto-generate coins from auto-tapper
        setInterval(() => {
            if (gameState.autoTapper > 0) {
                const income = gameState.autoTapper * upgrades.autoTapper.valuePerLevel;
                gameState.coins += income / 10; // Divide by 10 because we run every 100ms
                updateDisplay();
            }
        }, 100);

        // Save game
        function saveGame() {
            gameState.lastSaveTime = Date.now();
            try {
                localStorage.setItem('tapEmpireGameState', JSON.stringify(gameState));
            } catch (e) {
                console.error('Failed to save game:', e);
            }
        }

        // Load game
        function loadGame() {
            try {
                const saved = localStorage.getItem('tapEmpireGameState');
                if (saved) {
                    const loadedState = JSON.parse(saved);
                    
                    // Calculate offline progress
                    const timeAway = Date.now() - loadedState.lastSaveTime;
                    const secondsAway = timeAway / 1000;
                    const offlineIncome = Math.floor(secondsAway * loadedState.autoTapper * upgrades.autoTapper.valuePerLevel);
                    
                    gameState = loadedState;
                    gameState.coins += offlineIncome;
                    
                    if (offlineIncome > 0) {
                        alert(`Welcome back! You earned ${formatNumber(offlineIncome)} coins while you were away!`);
                    }
                }
            } catch (e) {
                console.error('Failed to load game:', e);
            }
            updateDisplay();
        }

        // Auto-save every 5 seconds
        setInterval(saveGame, 5000);

        // PWA Install Prompt
        let deferredPrompt;
        const installPrompt = document.getElementById('installPrompt');
        const installButton = document.getElementById('installButton');
        const dismissButton = document.getElementById('dismissButton');

        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            installPrompt.style.display = 'block';
        });

        installButton.addEventListener('click', async () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const { outcome } = await deferredPrompt.userChoice;
                console.log(`User response: ${outcome}`);
                deferredPrompt = null;
                installPrompt.style.display = 'none';
            }
        });

        dismissButton.addEventListener('click', () => {
            installPrompt.style.display = 'none';
        });

        // Register Service Worker
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js')
                .then(registration => {
                    console.log('Service Worker registered:', registration);
                })
                .catch(error => {
                    console.log('Service Worker registration failed:', error);
                });
        }

        // Initialize game
        window.addEventListener('load', () => {
            loadGame();
        });

        // Save before closing
        window.addEventListener('beforeunload', saveGame);
    </script>
</body>
</html>'''

print("HTML file created successfully!")
print(f"HTML file size: {len(html_content)} bytes")
