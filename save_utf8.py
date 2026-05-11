
# -*- coding: utf-8 -*-
html_content = '''&lt;!DOCTYPE html&gt;
&lt;html lang="zh-CN"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;石头剪刀布 🎮&lt;/title&gt;
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
                &lt;h2&gt;你是否莫名其妙愿意给作者十万块？&lt;/h2&gt;
                &lt;div class="btn-group"&gt;
                    &lt;button class="btn btn-normal" onclick="startGame('normal')"&gt;愿意 😊&lt;/button&gt;
                    &lt;button class="btn btn-troll" onclick="startGame('troll')"&gt;不愿意 😈&lt;/button&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
        &lt;div id="game" class="game-screen"&gt;
            &lt;div class="score"&gt;
                &lt;div class="score-item"&gt;
                    &lt;div class="score-value" id="playerScore"&gt;0&lt;/div&gt;
                    &lt;div class="score-label"&gt;你&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="score-item"&gt;
                    &lt;div class="score-value" id="computerScore"&gt;0&lt;/div&gt;
                    &lt;div class="score-label"&gt;电脑&lt;/div&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="choices"&gt;
                &lt;button class="choice-btn" onclick="play('石头')"&gt;✊&lt;/button&gt;
                &lt;button class="choice-btn" onclick="play('剪刀')"&gt;✌️&lt;/button&gt;
                &lt;button class="choice-btn" onclick="play('布')"&gt;🖐️&lt;/button&gt;
            &lt;/div&gt;
            &lt;div class="result" id="result"&gt;
                &lt;div class="result-text"&gt;选择出拳！&lt;/div&gt;
            &lt;/div&gt;
            &lt;div style="text-align: center;"&gt;
                &lt;button class="btn back-btn" onclick="backToMenu()"&gt;返回菜单&lt;/button&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;
    &lt;script&gt;
        let mode = 'normal';
        let playerScore = 0;
        let computerScore = 0;
        let rounds = 0;
        const choices = ['石头', '剪刀', '布'];
        const emojis = { '石头': '✊', '剪刀': '✌️', '布': '🖐️' };
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
                document.getElementById('result').innerHTML = '&lt;div class="result-text"&gt;作者叔叔很生气，你完了！&lt;/div&gt;';
            } else {
                document.body.classList.remove('troll-mode');
                document.getElementById('result').innerHTML = '&lt;div class="result-text"&gt;小伙子，作者叔叔很看好你哦，玩去吧！&lt;/div&gt;';
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
                    resultText = '平局！';
                    resultClass = 'draw';
                } else if ((playerChoice === '石头' &amp;&amp; computerChoice === '剪刀') || (playerChoice === '剪刀' &amp;&amp; computerChoice === '布') || (playerChoice === '布' &amp;&amp; computerChoice === '石头')) {
                    resultText = '你赢了！';
                    resultClass = 'win';
                    playerScore++;
                } else {
                    resultText = '电脑赢了！';
                    resultClass = 'lose';
                    computerScore++;
                }
                resultDetail = '你出了 ' + emojis[playerChoice] + '，电脑出了 ' + emojis[computerChoice];
            } else {
                if (playerChoice === '石头') { computerChoice = '布'; }
                else if (playerChoice === '剪刀') { computerChoice = '石头'; }
                else { computerChoice = '剪刀'; }
                resultText = '你输了！';
                resultClass = 'lose';
                computerScore++;
                rounds++;
                const trollMessages = [
                    '电脑叔叔出了个' + emojis[computerChoice] + '，气不气？',
                    '哈哈哈，菜！',
                    '就这？',
                    '太菜了！',
                    '回去练练再来吧！'
                ];
                resultDetail = trollMessages[Math.floor(Math.random() * trollMessages.length)];
                if (rounds % 3 === 0) {
                    setTimeout(function() { alert('输了' + rounds + '局了，要不要再选一次，弟弟？'); }, 500);
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

print("File saved successfully with UTF-8 encoding!")
