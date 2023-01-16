
BASE_SCRIPT = """
<script>
var _0xa3fe = [
    "....",
];
function toNumbers(_0x4e0ex2) {
    var _0x4e0ex3 = [];
    _0x4e0ex2[_0xa3fe[1]](/(..)/g, function (_0x4e0ex2) {
        _0x4e0ex3[_0xa3fe[0]](parseInt(_0x4e0ex2, 16));
    });
    return _0x4e0ex3;
}
function toHex() {
    for (var _0x4e0ex2 = 1 == arguments[_0xa3fe[2]] && arguments[0][_0xa3fe[3]] == Array ? arguments[0] : arguments, _0x4e0ex3 = _0xa3fe[4], _0x4e0ex5 = 0; _0x4e0ex5 < _0x4e0ex2[_0xa3fe[2]]; _0x4e0ex5++) {
        _0x4e0ex3 += (16 > _0x4e0ex2[_0x4e0ex5] ? _0xa3fe[5] : _0xa3fe[4]) + _0x4e0ex2[_0x4e0ex5].toString(16);
    }
    return _0x4e0ex3[_0xa3fe[6]]();
}
var a = toNumbers(_0xa3fe[7]),
    b = toNumbers(_0xa3fe[8]),
    c = toNumbers(_0xa3fe[9]);
document[_0xa3fe[10]] = _0xa3fe[11] + toHex(slowAES[_0xa3fe[12]](c, 2, a, b)) + _0xa3fe[13];
setTimeout("location.href='https://blackrussia.online:443/';", 5000);
"""

BASE_HTML = """
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>

<body>
  <section class="baner">
    <div class="container">
      <div class="baner_container">
        <div class="baner_left">
          <h1>
            Играй в Россию <br>
            на своем смартфоне на <br>
            проекте <span>BLACK RUSSIA</span>
          </h1>
          <p>
            Мечтаешь сыграть в CRMP на своем телефоне? <br>
            Это возможно на нашем проекте: полная карта, продуманный <br>
            игровой мод, уникальный модпак с русскими и зарубежными<br>
            авто, и многое другое ждет тебя на нашем проекте.
          </p>
      </div>
    </div>
  </body>
</html>
"""
