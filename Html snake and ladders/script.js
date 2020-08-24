window.dicerolled = false;
window.x = 0;
window.pl = 0;
window.poses = [
    ['32.3%', '89.5%'], ['38%', '89.5%'], ['43.7%', '89.5%'], ['49.4%', '89.5%'], ['55.1%', '89.5%'], ['60.8%', '89.5%'], ['66.5%', '89.5%'], ['72.2%', '89.5%'], ['77.9%', '89.5%'], ['83.6%', '89.5%'],
    ['83.6%', '80.5%'], ['77.9%', '80.5%'], ['72.2%', '80.5%'], ['66.5%', '80.5%'], ['60.8%', '80.5%'], ['55.1%', '80.5%'], ['49.4%', '80.5%'], ['43.7%', '80.5%'], ['38%', '80.5%'], ['32.3%', '80.5%'],
    ['32.3%', '71.5%'], ['38%', '71.5%'], ['43.7%', '71.5%'], ['49.4%', '71.5%'], ['55.1%', '71.5%'], ['60.8%', '71.5%'], ['66.5%', '71.5%'], ['72.2%', '71.5%'], ['77.9%', '71.5%'], ['83.6%', '71.5%'],
    ['83.6%', '62.5%'], ['77.9%', '62.5%'], ['72.2%', '62.5%'], ['66.5%', '62.5%'], ['60.8%', '62.5%'], ['55.1%', '62.5%'], ['49.4%', '62.5%'], ['43.7%', '62.5%'], ['38%', '62.5%'], ['32.3%', '62.5%'],
    ['32.3%', '53.5%'], ['38%', '53.5%'], ['43.7%', '53.5%'], ['49.4%', '53.5%'], ['55.1%', '53.5%'], ['60.8%', '53.5%'], ['66.5%', '53.5%'], ['72.2%', '53.5%'], ['77.9%', '53.5%'], ['83.6%', '53.5%'],
    ['83.6%', '44.5%'], ['77.9%', '44.5%'], ['72.2%', '44.5%'], ['66.5%', '44.5%'], ['60.8%', '44.5%'], ['55.1%', '44.5%'], ['49.4%', '44.5%'], ['43.7%', '44.5%'], ['38%', '44.5%'], ['32.3%', '44.5%'],
    ['32.3%', '35.5%'], ['38%', '35.5%'], ['43.7%', '35.5%'], ['49.4%', '35.5%'], ['55.1%', '35.5%'], ['60.8%', '35.5%'], ['66.5%', '35.5%'], ['72.2%', '35.5%'], ['77.9%', '35.5%'], ['83.6%', '35.5%'],
    ['83.6%', '26.5%'], ['77.9%', '26.5%'], ['72.2%', '26.5%'], ['66.5%', '26.5%'], ['60.8%', '26.5%'], ['55.1%', '26.5%'], ['49.4%', '26.5%'], ['43.7%', '26.5%'], ['38%', '26.5%'], ['32.3%', '26.5%'],
    ['32.3%', '17.5%'], ['38%', '17.5%'], ['43.7%', '17.5%'], ['49.4%', '17.5%'], ['55.1%', '17.5%'], ['60.8%', '17.5%'], ['66.5%', '17.5%'], ['72.2%', '17.5%'], ['77.9%', '17.5%'], ['83.6%', '17.5%'],
    ['83.6%', '8.5%'], ['77.9%', '8.5%'], ['72.2%', '8.5%'], ['66.5%', '8.5%'], ['60.8%', '8.5%'], ['55.1%', '8.5%'], ['49.4%', '8.5%'], ['43.7%', '8.5%'], ['38%', '8.5%'], ['32.3%', '8.5%']
];
window.pos = poses[window.pl];
function start_game() {
    var ss = document.getElementById('startscreen');
    ss.innerHTML = '';
    ss.innerHTML = '<style>body {background-image: url(board.jpg);background-size: 92%;background-repeat: no-repeat;}</style><!--<img src="board.jpg" alt="game board" width = "900px">-->';
    ss.innerHTML += '<button id="roll" onclick="cont()">Roll Dice</button>';
    document.body.innerHTML = '<div id="h"></div><div id="q"><img src="player.png" alt="player" width="3%" id="player"></div>' + document.body.innerHTML;
    a = document.getElementById("player");
    a.style['position'] = 'absolute';
    a.style['top'] = window.pos[1];
    a.style['left'] = window.pos[0];
}
window.dices = [
    'Roll Dice',
    '<img src="1.png" alt="Roll Dice" width="100px">',
    '<img src="2.png" alt="Roll Dice" width="100px">',
    '<img src="3.png" alt="Roll Dice" width="100px">',
    '<img src="4.png" alt="Roll Dice" width="100px">',
    '<img src="5.png" alt="Roll Dice" width="100px">',
    '<img src="6.png" alt="Roll Dice" width="100px">',
];
function getpos(num) {
    return window.poses[num + 1]    
}
window.ladpos = [
    [getpos(4), getpos(56)],
    [getpos(12), getpos(50)],
    [getpos(14), getpos(55)],
    [getpos(22), getpos(58)],
    [getpos(41), getpos(79)],
    [getpos(54), getpos(88)],
];
window.snakepos = [
    [getpos(28), getpos(10)],
    [getpos(37), getpos(3)],
    [getpos(47), getpos(16)],
    [getpos(75), getpos(32)],
    [getpos(94), getpos(71)],
    [getpos(96), getpos(42)],
];
function islad(pos) {
    var ladpos = window.ladpos;
    var islad = false;
    ladpos.forEach(i => {
        if (i[0] == pos) {
            islad = true;
        }
    });
    return islad;
}
function issnake(pos) {
    var snakepos = window.snakepos;
    var issnake = false;
    snakepos.forEach(i => {
        if (i[1] == pos) {
            issnake = true;
        }
    });
    return issnake;
}
function getnextlad(pos) {
    var ladpos = window.ladpos;
    if (islad(pos)) {
        ladpos.forEach(i => {
            if (i[0] == pos) {
                pos = i[1];
            }
        });
    }
    return pos;
}
function getwheresnake(pos) {
    var snakepos = window.snakepos;
    if (issnake(pos)) {
        snakepos.forEach(i => {
            if (i[1] == pos) {
                pos = i[0];
            }
        });
    }
    return pos;
}
function cont() {
    var x = Math.floor((Math.random() * 6) + 1);
    if (x == window.x) {
        cont();
    }
    else {
        if (window.pl + x == 99) {
            document.getElementById('qwert').innerHTML = '<div id="qwerty"><a id="won" onclick="location.reload()"><h1>YOU WON</h1><br><p>click to play again</p></a></div>';
        }
        window.x = x
        y = document.getElementById('roll');
        y.innerHTML = window.dices[x];
        // alert(x);
        if (window.pl + x >= 100) {
            x = 0;
        }
        else { 
            // kk = window.pos
            // a = document.getElementById("player");
            // while (!((Number(kk[1].slice(0,-1))>Number(poses[window.pl + x][1].slice(0,-1)))&(Number(kk[0].slice(0, -1)) > Number(poses[window.pl + x][0].slice(0, -1))))) {
            //     if (!(Number(kk[0].slice(0, -1)) > Number(poses[window.pl + x][0].slice(0, -1)))) {
            //         kk[0] = toString(Number(kk[0].slice(0, -1)) + 1) + '%';
            //         a.style['left'] = kk[0];

            //     }
            //     if (!(Number(kk[1].slice(0,-1))>Number(poses[window.pl + x][1].slice(0,-1)))) {
            //         kk[1] = toString(Number(kk[1].slice(0, -1)) + 1) + '%';
            //         a.style['top'] = kk[1];
            //     }
            // }
            window.pl += x;
        }
        window.pos = poses[window.pl];
        a = document.getElementById("player");
        a.style['left'] = window.pos[0];
        a.style['top'] = window.pos[1];
    }
}
