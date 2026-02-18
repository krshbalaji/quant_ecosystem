async function fetchState() {
    try {
        const response = await fetch("/api/state");
        const data = await response.json();

        document.getElementById("mode").innerText = data.mode;
        document.getElementById("equity").innerText = "₹" + data.equity;
        document.getElementById("pnl").innerText = "₹" + data.pnl;
        document.getElementById("trades").innerText = data.trades;
        document.getElementById("winrate").innerText = data.winrate + "%";
        document.getElementById("regime").innerText = data.regime;

        updateEquityChart(data.equity);

    } catch (e) {
        console.log("Dashboard refresh error", e);
    }
}

setInterval(fetchState, 2000);
fetchState();

let equityHistory = [];
let labels = [];

const ctx = document.getElementById('equityChart').getContext('2d');

const equityChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Equity Curve',
            data: equityHistory,
            borderColor: '#00ffcc',
            borderWidth: 2
        }]
    },
    options: {
        animation: false,
        responsive: true
    }
});

function updateEquityChart(value) {
    const now = new Date().toLocaleTimeString();

    labels.push(now);
    equityHistory.push(value);

    if (labels.length > 50) {
        labels.shift();
        equityHistory.shift();
    }

    equityChart.update();
}

async function fetchLeaderboard() {
    const response = await fetch("/api/leaderboard");
    const data = await response.json();

    const board = document.getElementById("leaderboard");
    board.innerHTML = "";

    data.forEach(item => {
        const div = document.createElement("div");
        div.innerText = item[0] + " — " + item[1];
        board.appendChild(div);
    });
}

setInterval(fetchLeaderboard, 5000);
fetchLeaderboard();

async function fetchAI() {
    const response = await fetch("/api/ai");
    const data = await response.json();

    document.getElementById("ai-regime").innerText = "Regime: " + data.regime;
    document.getElementById("ai-suggestion").innerText = "AI Suggestion: " + data.suggestion;
}

setInterval(fetchAI, 4000);
fetchAI();
