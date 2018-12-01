/* 20point以上で指名代行ボタンを表示 */
if(localStorage.getItem) {
    var point = Number(localStorage.getItem('ofuroPoint'))
    if(point >= 20) {
        // 複数あるボタン全てに処理をするのでクラス名から要素を取得
        var orderBtn = document.getElementsByClassName('orderBtn');
        // 全てのボタンにstyleを適用させるため、繰り返し処理
        for(i = 0; i <= orderBtn.length; i++) {
            orderBtn[i].style.visibility = 'visible';
        }
    }
}

/* 指名代行ボタンを押したら20point消費 */
// 複数あるボタン全てに処理をするのでクラス名から要素を取得
function resetPoint() {
    var point = Number(localStorage.getItem('ofuroPoint'));
    point -= 20;
    localStorage.setItem('ofuroPoint', point);
}

// var orderBtn = document.getElementsByClassName('orderBtn');
// for(i = 0; i <= orderBtn.length; i++) {
//     // 全てのボタンにstyleを適用させるため、繰り返し処理
//     orderBtn[i].addEventListener('click', function() {
//         console.log('push')
//         var point = Number(localStorage.getItem('ofuroPoint'));
//         point -= 20;
//         localStorage.setItem('ofuroPoint', point);
//     });
// }