# Django Rest Framework 로그인, 회원가입 API


## HTTPie 를 활용한 예시

# Registration 회원가입 예시
> ## http POST http://127.0.0.1:8000/api/auth/register/ username=test_id password=password password2=password email=nadure@nadure.com

# login 로그인 예시(토큰 획득)

> ## http POST http://127.0.0.1:8000/api/auth/login/ username=test_id password=password

# View Test 뷰 확인
> ## http GET http://127.0.0.1:8000/api/test/ "Authorization: Token 토큰"
> 예시 )
> ### http GET http://127.0.0.1:8000/api/test/ "Authorization: Token d8ef89912cc58b41257f978c3ce2edbc3c85493e"

