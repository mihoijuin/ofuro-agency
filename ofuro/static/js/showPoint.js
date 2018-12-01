var pointNav =  document.getElementById('pointNav');

if(localStorage.getItem('ofuroPoint')) {
    var point = localStorage.getItem('ofuroPoint');
    pointNav.innerText = 'お風呂POINT： ' + point;
} else {
    var point = 0;
    pointNav.innerText = 'お風呂POINT：' + point;
}
