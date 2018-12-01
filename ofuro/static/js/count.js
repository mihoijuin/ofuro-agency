if (localStorage.getItem('ofuroPoint')) {
    var point = Number(localStorage.getItem('ofuroPoint'));
    point += 1;
    localStorage.setItem('ofuroPoint', point);
} else {
    localStorage.setItem('ofuroPoint', 1);
}
