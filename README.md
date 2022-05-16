# google-login-bypass

최신 기준 셀레니움 구글 로그인 우회 스크립트 및 예제 (Undetectable selenium google login bypass script and example)
두가지의 우회 스크립트가 준비되어 있습니다.

- main.py : undetected-chromedriver 패키지를 사용한 우회 시나리오
- other_way.py : 크롬 디버그 모드에 파이프라인을 연결하여 사용하는 우회 시나리오

## Required

```
pip install -r requirements.txt
```

## Example

- 이 스크립트는 셀레니움으로 구글 로그인 시 발생하는 로그인 오류를 우회하기 위해 만들어졌습니다.
- 기본적으로 reCAPTCHA 대응이기도 하나, 반복적으로 사용하는 경우에는 reCAPTCHA가 동작할 수 있습니다.
- 아래와 같은 오류가 발생할 때에 대응하여 사용할 수 있습니다.

![image](https://user-images.githubusercontent.com/98614666/157562373-526db685-ae97-430c-8cf3-73235b883adb.png)
