#!/usr/bin/python3

# 풀어쓰기 상태일 때, 한/영 키를 누른 것처럼 변환해주는 스크립트
# 기울여 풀어쓰기 폰트를 적용할 수 있도록 만들어준다.
# 테스트에 사용한 폰트 출저
# https://gall.dcinside.com/board/view/?id=europa&no=573662
# https://www.dropbox.com/s/vt0v0fxnqxc0z4r/NEOHPEN3.TTF?dl=0
# https://web.archive.org/web/20220116013552/https://gall.dcinside.com/board/view/?id=europa&no=573662

jamo = (
    "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ",
    "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ",
    "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ",
    "ㅋ", "ㅌ", "ㅍ", "ㅎ",
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ",
    "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ",
    "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ")

alpha = (
    'r', 'R', 'rt', 's', 'sw', 'sg', 'e',
    'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg',
    'a', 'q', 'qt', 't', 'T', 'd', 'w', 'c',
    'z', 'x', 'v', 'g',
    'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P',
    'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np',
    'nl', 'b', 'm', 'ml', 'l')

def hanyeong(inputtext):
    result = ""
    for i in inputtext:
        if i in jamo:
            result += alpha[jamo.index(i)]
        else:
            result += i
    return result

def yeonghan(inputtext):
    raise NotImplementedError

if __name__ == '__main__':
    import sys
    from functools import reduce
    # assumes utf-8 encoding input & python effectively
    # compiles it into list of unicode code points
    text = sys.stdin.read()
    if sys.argv[1:2] == ['yeong']:
            print(hanyeong(text), end='')
    else:
            print(yeonghan(text), end='')
