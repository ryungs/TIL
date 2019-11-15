# django

### c9에서 django-basic 생성 Rails Tutorial 선택

- rm README.md



### semver(Semantic Versioning) 

- 정해지기 전까지는 사람들이 중구난방으로 버전을 업데이트 했다
  그래서 이제는 버전을 올릴 때 의미 있게 올리자로 정한게 Semantic Versioning

- Major.Minor.Patch
  3.6.7

- Major : 많은게 바뀌어서, 새로 코드를 짜야한다.
  Minor : 기능의 추가나 삭제가 있지만 기존 코드를 부수진 않는다
  Patch : 버그 픽스

  

#### pyenv(파이썬 버전 관리자) install 하기

- pyenv는 window 에 안깔린다 그래서 c9에서 까는거

구글에서 pyenv 검색 →  Basic GitHub Checkout  

→ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

→ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

→ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

→ bash

→ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

→ bash

→ which pyenv (pyenv 깔려있는지 확인하는 방법)

→ pyenv install 3.6.7 ( 파이썬 깔기)

→ pyenv versions ( 깔려 있는 파이썬 버전 뭔지 확인하는 방법)

→  pyenv global 3.6.8 (이제 내 컴퓨터에 쓰는 기본 파이썬을 3.6.8로 하겠다)



### chat.py

- answer = input('What\'s up?')

  print(answer)

  입력하는 값을 저장하는 코드를 짜보자

- **import csv 이용하기**

- a+ = 받아온 값을 쌓는다