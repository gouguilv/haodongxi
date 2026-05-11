
html_content = '''&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Rock Paper Scissors 🎮&lt;/title&gt;
    &lt;style&gt;
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px; }
        .container { background: white; border-radius: 24px; padding: 32px 24px; max-width: 420px; width: 100%; box-shadow: 0 20px 60px rgba(0,0,0,0.3); }
        h1 { text-align: center; color: #333; margin-bottom: 24px; font-size: 28px; }
        .mode-select { text-align: center; margin-bottom: 24px; }
        .mode-select h2 { font-size: 18px; color: #555; margin-bottom: 16px; }
        .btn-group { display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; }
        .btn { padding: 14px 28px; font-size: 16px; border: none; border-radius: 12px; cursor: pointer; transition: all 0.3s ease; font-weight: 600; }
        .btn-normal { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; }
        .btn-troll { background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%); color: white; }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.2); }
        .btn:active { transform: translateY(0); }
        .game-screen { display: none; }
        .score { display: flex; justify-content: space-around; margin-bottom: 24px; padding: 16px; background: #f5f5f5; border-radius: 12px; }
        .score-item { text-align: center; }
        .score-value { font-size: 32px; font-weight: bold; color: #667eea; }
        .score-label { font-size: 14px; color: #666; margin-top: 4px; }
        .choices { display: flex; justify-content: center; gap: 16px; margin: 24px 0; }
        .choice-btn { width: 90px; height: 90px; font-size: 48px; border: 3px solid #e0e0e0; border-radius: 50%; background: white; cursor: pointer; transition: all 0.3s ease; display: flex; align-items: center; justify-content: center; }
        .choice-btn:hover { border-color: #667eea; transform: scale(1.1); box-shadow: 0 8px 20px rgba(102,126,234,0.3); }
        .result { text-align: center; margin: 20px 0; min-height: 100px; }
        .result-text { font-size: 22px; font-weight: bold; color: #333; margin-bottom: 8px; }
        .result-detail { font-size: 16px; color: #666; }
        .back-btn { margin-top: 20px; background: #666; color: white; }
        .win { color: #11998e; }
        .lose { color: #eb3349; }
        .draw { color: #f5a623; }
        .troll-mode { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); }
        .troll-mode .container { background: #0f0f23; color: #eee; }
        .troll-mode h1 { color: #ff6b6b; }
        .troll-mode .score { background: #1a1a2e; }
        .troll-mode .score-value { color: #ff6b6b; }
        .troll-mode .choice-btn { background: #1a1a2e; border-color: #ff6b6b; color: #ff6b6b; }
        .troll-mode .choice-btn:hover { border-color: #ff4757; box-shadow: 0 8px 20px rgba(255,107,107,0.3); }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container"&gt;
        &lt;h1&gt;✊✌️🖐️&lt;/h1&gt;
        &lt;div id="menu" class="menu-screen"&gt;
            &lt;div class="mode-select"&gt;
                &lt;h2&gt;Will you mysteriously give the author $100,000?&lt;/h2&gt;
                &lt;div class="btn-group"&gt;
                    &lt;button class="btn btn-normal" onclick="startGame('normal')"&gt;Yes 😊&lt;/button&gt;
                    &lt;button class="btn btn-troll" onclick="startGame('troll')"&gt;No 😈&lt;/button&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
        &lt;div id="game" class="game-screen"&gt;
            &lt;div class="score"&gt;
                &lt;div class="score-item"&gt;
                    &lt;div class="score-value" id="playerScore"&gt;0&lt;/div&gt;
                    &lt;div class="score-label"&gt;You&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="score-item"&gt;
                    &lt;div class="score-value" id="computerScore"&gt;0&lt;/div&gt;
                    &lt;div class="score-label"&gt;Computer&lt;/div&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="choices"&gt;
                &lt;button class="choice-btn" onclick="play('rock')"&gt;✊&lt;/button&gt;
                &lt;button class="choice-btn" onclick="play('scissors')"&gt;✌️&lt;/button&gt;
                &lt;button class="choice-btn" onclick="play('paper')"&gt;🖐️&lt;/button&gt;
            &lt;/div&gt;
            &lt;div class="result" id="result"&gt;
                &lt;div class="result-text"&gt;Choose your move!&lt;/div&gt;
            &lt;/div&gt;
            &lt;div style="text-align: center;"&gt;
                &lt;button class="btn back-btn" onclick="backToMenu()"&gt;Back to Menu&lt;/button&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;
    &lt;script&gt;
        let mode = 'normal';
        let playerScore = 0;
        let computerScore = 0;
        let rounds = 0;
        const choices = ['rock', 'scissors', 'paper'];
        const emojis = { 'rock': '✊', 'scissors': '✌️', 'paper': '🖐️' };
        const names = { 'rock': 'Rock', 'scissors': 'Scissors', 'paper': 'Paper' };
        function startGame(selectedMode) {
            mode = selectedMode;
            playerScore = 0;
            computerScore = 0;
            rounds = 0;
            document.getElementById('menu').style.display = 'none';
            document.getElementById('game').style.display = 'block';
            updateScore();
            if (mode === 'troll') {
                document.body.classList.add('troll-mode');
                document.getElementById('result').innerHTML = '&lt;div class="result-text"&gt;The author is angry, you are doomed!&lt;/div&gt;';
            } else {
                document.body.classList.remove('troll-mode');
                document.getElementById('result').innerHTML = '&lt;div class="result-text"&gt;The author likes you, go play!&lt;/div&gt;';
            }
        }
        function backToMenu() {
            document.getElementById('menu').style.display = 'block';
            document.getElementById('game').style.display = 'none';
            document.body.classList.remove('troll-mode');
        }
        function play(playerChoice) {
            let computerChoice, resultText, resultDetail, resultClass;
            if (mode === 'normal') {
                computerChoice = choices[Math.floor(Math.random() * 3)];
                if (playerChoice === computerChoice) {
                    resultText = 'Draw!';
                    resultClass = 'draw';
                } else if ((playerChoice === 'rock' &amp;&amp; computerChoice === 'scissors') || (playerChoice === 'scissors' &amp;&amp; computerChoice === 'paper') || (playerChoice === 'paper' &amp;&amp; computerChoice === 'rock')) {
                    resultText = 'You win!';
                    resultClass = 'win';
                    playerScore++;
                } else {
                    resultText = 'Computer wins!';
                    resultClass = 'lose';
                    computerScore++;
                }
                resultDetail = 'You played ' + emojis[playerChoice] + ', computer played ' + emojis[computerChoice];
            } else {
                if (playerChoice === 'rock') { computerChoice = 'paper'; }
                else if (playerChoice === 'scissors') { computerChoice = 'rock'; }
                else { computerChoice = 'scissors'; }
                resultText = 'You lose!';
                resultClass = 'lose';
                computerScore++;
                rounds++;
                const trollMessages = [
                    'Computer played ' + emojis[computerChoice] + ', mad?',
                    'Haha, noob!',
                    'Is that all?',
                    'Too easy!',
                    'Go practice more!'
                ];
                resultDetail = trollMessages[Math.floor(Math.random() * trollMessages.length)];
                if (rounds % 3 === 0) {
                    setTimeout(function() { alert('You lost ' + rounds + ' times, want to choose again, buddy?'); }, 500);
                }
            }
            document.getElementById('result').innerHTML = '&lt;div class="result-text ' + resultClass + '"&gt;' + resultText + '&lt;/div&gt;&lt;div class="result-detail"&gt;' + resultDetail + '&lt;/div&gt;';
            updateScore();
        }
        function updateScore() {
            document.getElementById('playerScore').textContent = playerScore;
            document.getElementById('computerScore').textContent = computerScore;
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;'''

with open('/workspace/guessfist.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("English version saved successfully!")
