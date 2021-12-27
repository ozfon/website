/* This file is: script.js */
function getID(i) {
    return document.getElementById(i);
  }

function getVal(i) {
return getID(i).value;
}

function solve() {
    var a = parseInt( getVal("a")),
        b = parseInt( getVal("b")),
        c = parseInt( getVal("c"));
        if ( isNaN(a) ) { a = 1; }
        if ( isNaN(b) ) { b = 1; }
        if ( isNaN(c) ) { c = 1; }
    var A = b*b,
        B = b-4*a*c,
        C = 2*a;
    if (B < 0) {
        B = Math.abs(B).toString() + "i"
        r1 = "(" + A.toString() + "+" + B + ")/" + C.toString()
        r2 = "(" + A.toString() + "-" + B + ")/" + C.toString()
    }
    else {
        r1 = (A+Math.sqrt(B))/C;
        r2 = (A-Math.sqrt(B))/C;
    }

    getID("s1").innerHTML = "r1 = " + r1.toString();
    getID("s2").innerHTML = "r2 = " + r2.toString();
}

var submitButton = getID("submit");
submitButton.onclick = function() {
    solve();	
};