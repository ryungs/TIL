# Django -> INSTA (Project)

### 1. mton app - M:N 데이터베이스

```bash

student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ git add .

student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ git commit -m 'init project'
[master 8e1257c] init project
 1 file changed, 7 insertions(+)
 create mode 100644 07_Django/INSTA/.gitignore

student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ rm -r .git
rm: cannot remove '.git': No such file or directory

student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0

student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ pip install django==2.1.7 django-extensions ipython
Collecting django==2.1.7
  Using cached https://files.pythonhosted.org/packages/c7/87/fbd666c4f87591ae25b7bb374298e8629816e87193c4099d3608ef11fab9/Django-2.1.7-py3-none-any.whl
Collecting django-extensions
  Using cached https://files.pythonhosted.org/packages/26/66/613b34aa7246e1be223e7f539212d8972e41046ec7f2b8bc0ba3e2cfcf22/django_extensions-2.1.6-py2.py3-none-any.whl
Collecting ipython
  Using cached https://files.pythonhosted.org/packages/46/b5/ca080401b8dbde51a0f4377b4e22ce02b266340a1cda389b6dea702d06d1/ipython-7.4.0-py3-none-any.whl
Collecting pytz (from django==2.1.7)
  Using cached https://files.pythonhosted.org/packages/3d/73/fe30c2daaaa0713420d0382b16fbb761409f532c56bdcc514bf7b6262bb6/pytz-2019.1-py2.py3-none-any.whl
Collecting six>=1.2 (from django-extensions)
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting pickleshare (from ipython)
  Using cached https://files.pythonhosted.org/packages/9a/41/220f49aaea88bc6fa6cba8d05ecf24676326156c23b991e80b3f2fc24c77/pickleshare-0.7.5-py2.py3-none-any.whl
Collecting traitlets>=4.2 (from ipython)
  Using cached https://files.pythonhosted.org/packages/93/d6/abcb22de61d78e2fc3959c964628a5771e47e7cc60d53e9342e21ed6cc9a/traitlets-4.3.2-py2.py3-none-any.whl
Collecting jedi>=0.10 (from ipython)
  Using cached https://files.pythonhosted.org/packages/25/2b/1f188901be099d52d7b06f4d3b7cb9f8f09692c50697b139eaf6fa2928d8/jedi-0.13.3-py2.py3-none-any.whl
Collecting prompt-toolkit<2.1.0,>=2.0.0 (from ipython)
  Using cached https://files.pythonhosted.org/packages/f7/a7/9b1dd14ef45345f186ef69d175bdd2491c40ab1dfa4b2b3e4352df719ed7/prompt_toolkit-2.0.9-py3-none-any.whl
Collecting backcall (from ipython)
  Using cached https://files.pythonhosted.org/packages/84/71/c8ca4f5bb1e08401b916c68003acf0a0655df935d74d93bf3f3364b310e0/backcall-0.1.0.tar.gz
Collecting colorama; sys_platform == "win32" (from ipython)
  Using cached https://files.pythonhosted.org/packages/4f/a6/728666f39bfff1719fc94c481890b2106837da9318031f71a8424b662e12/colorama-0.4.1-py2.py3-none-any.whl
Requirement already satisfied: setuptools>=18.5 in c:\users\student\til\07_django\insta\venv\lib\site-packages\setuptools-40.8.0-py3.7.egg (from ipython) (40.8.0)
Collecting decorator (from ipython)
  Using cached https://files.pythonhosted.org/packages/5f/88/0075e461560a1e750a0dcbf77f1d9de775028c37a19a346a6c565a257399/decorator-4.4.0-py2.py3-none-any.whl
Collecting pygments (from ipython)
  Using cached https://files.pythonhosted.org/packages/13/e5/6d710c9cf96c31ac82657bcfb441df328b22df8564d58d0c4cd62612674c/Pygments-2.3.1-py2.py3-none-any.whl
Collecting ipython-genutils (from traitlets>=4.2->ipython)
  Using cached https://files.pythonhosted.org/packages/fa/bc/9bd3b5c2b4774d5f33b2d544f1460be9df7df2fe42f352135381c347c69a/ipython_genutils-0.2.0-py2.py3-none-any.whl
Collecting parso>=0.3.0 (from jedi>=0.10->ipython)
  Using cached https://files.pythonhosted.org/packages/a7/bd/e2f4753c5fa93932899243b4299011a757ac212e9bc8ddf062f38df4e78b/parso-0.4.0-py2.py3-none-any.whl
Collecting wcwidth (from prompt-toolkit<2.1.0,>=2.0.0->ipython)
  Using cached https://files.pythonhosted.org/packages/7e/9f/526a6947247599b084ee5232e4f9190a38f398d7300d866af3ab571a5bfe/wcwidth-0.1.7-py2.py3-none-any.whl
Installing collected packages: pytz, django, six, django-extensions, pickleshare, decorator, ipython-genutils, traitlets, parso, jedi, wcwidth, prompt-toolkit, backcall, colorama, pygments, ipython
  Running setup.py install for backcall ... done
Successfully installed backcall-0.1.0 colorama-0.4.1 decorator-4.4.0 django-2.1.7 django-extensions-2.1.6 ipython-7.4.0 ipython-genutils-0.2.0 jedi-0.13.3 parso-0.4.0 pickleshare-0.7.5 prompt-toolkit-2.0.9 pygments-2.3.1 pytz-2019.1 six-1.12.0 traitlets-4.3.2 wcwidth-0.1.7

student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ pip list
Package           Version
----------------- -------
backcall          0.1.0
colorama          0.4.1
decorator         4.4.0
Django            2.1.7
django-extensions 2.1.6
ipython           7.4.0
ipython-genutils  0.2.0
jedi              0.13.3
parso             0.4.0
pickleshare       0.7.5
pip               19.0.3
prompt-toolkit    2.0.9
Pygments          2.3.1
pytz              2019.1
setuptools        40.8.0
six               1.12.0
traitlets         4.3.2
wcwidth           0.1.7

student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ django-admin startproject insta .

student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ ls
insta  manage.py  venv

student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ django-admin startapp mton

```

```bash
student@M70324 MINGW64 ~/TIL/07_Django/INSTA (master)
$ pip install faker
```

```bash
In [3]: Hotel.dummy(n=10)

In [4]: Client.dummy(n=10)

In [5]: c = Client.objects.first()

In [6]: c
Out[6]: <Client: Client object (1)>

In [7]: h = Hotel.objects.last()

In [8]: h
Out[8]: <Hotel: Hotel object (10)>

In [9]: h.clients
Out[9]: <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0x1c2f2cc7cc0>

In [10]: h.clients.all()
Out[10]: <QuerySet []>

In [11]: h.clients.add(c)

In [12]: h.clients.all()
Out[12]: <QuerySet [<Client: Client object (1)>]>

In [13]: c.hotel_set.all()
Out[13]: <QuerySet [<Hotel: Hotel object (10)>]>

In [14]: h1 = Hotel.objects.get(id=1)

In [15]: c1 = Client.objects.get(id=1)

In [16]: c3 = Client.objects.get(id=3)

In [17]: c5 = Client.objects.get(id=5)

In [18]: c7 = Client.objects.get(id=7)



In [20]: h1.clients.add(c1)

In [21]: h1.clients.add(c3)

In [22]: h1.clients.add(c5)

In [23]: h1.clients.add(c7)


In [25]: h1.clients.all()
Out[25]: <QuerySet [<Client: Client object (1)>, <Client: Client object (3)>, <Client: Client object (5)>, <Client: Client object (7)>]>


In [28]: h1.clients.add(2,4)

In [29]: h1.clients.all()
Out[29]: <QuerySet [<Client: Client object (1)>, <Client: Client object (2)>, <Client: Client object (3)>, <Client: Client object (4)>, <Client: Client object (5)>, <Client: Client object (7)>]>


In [30]: h1.clients.remove(2)

In [31]: h1.clients.all()
Out[31]: <QuerySet [<Client: Client object (1)>, <Client: Client object (3)>, <Client: Client object (4)>, <Client: Client object (5)>, <Client: Client object (7)>]>

```



### 2. posts app - insta 구현하는 앱

- insta 폴더 밑에 바로 templates 폴더 만들어서 base.html 생성함

- setting.py 가서 'DIRS': [os.path.join(BASE_DIR, 'insta', 'templates')], 추가 해줘야함
-  pip install django-bootstrap4 -> setting.py 가서 -> app 등록에 'bootstrap4' 추가
- pip install pillow : 이미지 필드 쓰려면 반드시 필요함