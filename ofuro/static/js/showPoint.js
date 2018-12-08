var pointNav =  document.getElementById('pointNav');

if(localStorage.getItem('ofuroPoint')) {
    var point = localStorage.getItem('ofuroPoint');
    pointNav.innerText = point + ' ポイント';
} else {
    var point = 0;
    pointNav.innerText =  point + ' ポイント';
}
