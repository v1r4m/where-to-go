# where-to-go
South Korea Randonautica

## Naver Map ...
* Use it at your own risk
* 네이버 지도 거리뷰 api는 공식 key를 받아서 쓸 수도 있긴 하지만...
* 이렇게 panorama가 static 서버에 올라와 있다. 
```
https://panorama.pstatic.net/imageV3/QZuCo1JTy4wVlylyMIvURg/P
https://panorama.pstatic.net/image/oHnufkqUAGFbhVy2EU1pJA/512/P
```
* image버전에 따라 둘이 쬠 다른데 그건 중요한건 아니긴함
* 그러니까, 좌표값을 저런 해쉬값으로 변환하는 테이블만 있으면 api인증을 우회하고 좌표값에서 가장 가까운 파노라마 이미지를 가져올 수 있다는 뜻이다. 글고 그런건 당근 있다. **세션쿠키 검증조차 없이.**
```
curl 'https://map.naver.com/p/api/panorama/nearby/127.8737772/38.2275148' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4' \
  -H 'cache-control: no-cache' \
  -H 'expires: Sat, 01 Jan 2000 00:00:00 GMT' \
  -H 'referer: https://map.naver.com/p?c=9.65,0,0,0,adh' 
```
```
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "camera_angle": [
                    0.0,
                    222.7,
                    0.0
                ],
                "heading": 328.65,
                "land_altitude": 22036,
                "description": "강원특별자치도 양구군 방산면",
                "id": "oHnufkqUAGFbhVy2EU1pJA",
                "tilt": 10.0,
                "camera_altitude": 22286,
                "photodate": "2024-06-10 10:24:54",
                "type": "3",
                "title": "평화로",
                "fov": 90
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    127.8749479,
                    38.2260051
                ]
            }
        }
    ]
}
```


## ㅎㅎ
* QZuCo1JTy4wVlylyMIvURg 참고로 이 해쉬는 이 녀석 사실 잘 꼬라보면 base64/hex 인코딩된 uuid다. 
```
data = base64.urlsafe_b64decode("QZuCo1JTy4wVlylyMIvURg==")
print(data.hex())
# 419b82a35253cb8c15972972308bd446
# 419b82a-3525-3cb8-c1597-2972308bd446
```