let x = +prompt('input num');
if (x < -1){
	var y = Math.abs(x+1);
}
else if (-1 <= x && x <= 2){
	var y = 2*x-1;
}
else if (x > 2){
	var y = 1+(x/2);
}
alert(y);