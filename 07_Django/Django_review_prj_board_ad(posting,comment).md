# Django_review_prj > board_ad(posting,comment)

### review_prj > board_ad



#### 1. db 날리기

```bash
python manage.py migrate (앱이름)board_ad zero
```

- 모델 꼬이면 db 날리고 새로 해라 



#### 2. 모델을 수정했으면 무조건 makemigrations 하세요



#### 3. time stamp

- 보통 게시글에 다 들어감

```python
# timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
```

- created_at 의 auto_now_add=True는 제일 처음 시간만 저장
- update_at 의 auto_now=True는 제일 처음부터 이후 수정한 시간 모두 저장
- created_at 의 auto_now_add 와 update_at 의 auto_now=True가 다르면 수정됨



#### 4. views.py → import 'get_object_or_404'

- 이걸 써야 진짜 id가 없을 때 404 에러 페이지를 내준다

-  views.py → import 'get_list_or_404' 를 쓸 수 없는 이유는 이걸 쓰면 리스트가 없으면 주조건 404에러를 낸다