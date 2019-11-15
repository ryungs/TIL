# Django-CRUD  프로젝트 생성

## c9 Terminal

```
ryungs:~/workspace $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

ryungs:~/workspace $ pyenv install 3.6.8
bash: pyenv: command not found
ryungs:~/workspace $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
ryungs:~/workspace $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
ryungs:~/workspace $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
ryungs:~/workspace $ bash
ryungs:~/workspace $ pyenv -v
pyenv 1.2.9-2-g6309aaf2
ryungs:~/workspace $ pyenv install 3.6.8

ryungs:~/workspace $ pyenv global 3.6.8

ryungs:~/workspace $ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
Cloning into '/home/ubuntu/.pyenv/plugins/pyenv-virtualenv'...
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 2051 (delta 6), reused 2 (delta 1), pack-reused 2034
Receiving objects: 100% (2051/2051), 587.89 KiB | 1.05 MiB/s, done.
Resolving deltas: 100% (1395/1395), done.
ryungs:~/workspace $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
ryungs:~/workspace $ bash
ryungs:~/workspace $ pyenv virtualenv 3.6.8 django_env
Looking in links: /tmp/tmpi1dvxjde
Requirement already satisfied: setuptools in /home/ubuntu/.pyenv/versions/3.6.8/envs/django_env/lib/python3.6/site-packages (40.6.2)
Requirement already satisfied: pip in /home/ubuntu/.pyenv/versions/3.6.8/envs/django_env/lib/python3.6/site-packages (18.1)
ryungs:~/workspace $ pyenv versions
  system
* 3.6.8 (set by /home/ubuntu/.pyenv/version)
  3.6.8/envs/django_env
  django_env
ryungs:~/workspace $ pip install django
Collecting django
  Downloading https://files.pythonhosted.org/packages/36/50/078a42b4e9bedb94efd3e0278c0eb71650ed9672cdc91bd5542953bec17f/Django-2.1.5-py3-none-any.whl (7.3MB)
    100% |████████████████████████████████| 7.3MB 4.0MB/s 
Collecting pytz (from django)
  Downloading https://files.pythonhosted.org/packages/61/28/1d3920e4d1d50b19bc5d24398a7cd85cc7b9a75a490570d5a30c57622d34/pytz-2018.9-py2.py3-none-any.whl (510kB)
    100% |████████████████████████████████| 512kB 17.1MB/s 
Installing collected packages: pytz, django
Successfully installed django-2.1.5 pytz-2018.9
You are using pip version 18.1, however version 19.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
ryungs:~/workspace $ pip list
Package    Version
---------- -------
Django     2.1.5  
pip        18.1   
pytz       2018.9 
setuptools 40.6.2 
You are using pip version 18.1, however version 19.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
ryungs:~/workspace $ django-admin startproject crud
ryungs:~/workspace $ mv crud CRUD
ryungs:~/workspace $ pyenv virtualenv 3.6.8 crud
Looking in links: /tmp/tmpclkh7kuu
Requirement already satisfied: setuptools in /home/ubuntu/.pyenv/versions/3.6.8/envs/crud/lib/python3.6/site-packages (40.6.2)
Requirement already satisfied: pip in /home/ubuntu/.pyenv/versions/3.6.8/envs/crud/lib/python3.6/site-packages (18.1)
ryungs:~/workspace $ pyenv versions
  system
* 3.6.8 (set by /home/ubuntu/.pyenv/version)
  3.6.8/envs/crud
  3.6.8/envs/django_env
  crud
  django_env
ryungs:~/workspace $ cd CRUD
ryungs:~/workspace/CRUD $ pwd
/home/ubuntu/workspace/CRUD
ryungs:~/workspace/CRUD $ pyenv versions
  system
* 3.6.8 (set by /home/ubuntu/.pyenv/version)
  3.6.8/envs/crud
  3.6.8/envs/django_env
  crud
  django_env
ryungs:~/workspace/CRUD $ pyenv local crud
(crud) ryungs:~/workspace/CRUD $ pip install django
Collecting django
  Using cached https://files.pythonhosted.org/packages/36/50/078a42b4e9bedb94efd3e0278c0eb71650ed9672cdc91bd5542953bec17f/Django-2.1.5-py3-none-any.whl
Collecting pytz (from django)
  Using cached https://files.pythonhosted.org/packages/61/28/1d3920e4d1d50b19bc5d24398a7cd85cc7b9a75a490570d5a30c57622d34/pytz-2018.9-py2.py3-none-any.whl
Installing collected packages: pytz, django
Successfully installed django-2.1.5 pytz-2018.9
You are using pip version 18.1, however version 19.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(crud) ryungs:~/workspace/CRUD $ pip install django-extensions
Collecting django-extensions
  Downloading https://files.pythonhosted.org/packages/e4/56/6a854a56732f7cb6a0393b8a32ae8a37b82b004e638b7b2f153b66733ce5/django_extensions-2.1.4-py2.py3-none-any.whl (217kB)
    100% |████████████████████████████████| 225kB 7.0MB/s 
Collecting six>=1.2 (from django-extensions)
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Installing collected packages: six, django-extensions
Successfully installed django-extensions-2.1.4 six-1.12.0
You are using pip version 18.1, however version 19.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(crud) ryungs:~/workspace/CRUD $ pip list
Package           Version
----------------- -------
Django            2.1.5  
django-extensions 2.1.4  
pip               18.1   
pytz              2018.9 
setuptools        40.6.2 
six               1.12.0 
You are using pip version 18.1, however version 19.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(crud) ryungs:~/workspace/CRUD $ pip install ipython
Collecting ipython
  Downloading https://files.pythonhosted.org/packages/f0/b4/a9ea018c73a84ee6280b2e94a1a6af8d63e45903eac2da0640fa63bca4db/ipython-7.2.0-py3-none-any.whl (765kB)
    100% |████████████████████████████████| 768kB 17.7MB/s 
Collecting backcall (from ipython)
  Downloading https://files.pythonhosted.org/packages/84/71/c8ca4f5bb1e08401b916c68003acf0a0655df935d74d93bf3f3364b310e0/backcall-0.1.0.tar.gz
Collecting pexpect; sys_platform != "win32" (from ipython)
  Downloading https://files.pythonhosted.org/packages/89/e6/b5a1de8b0cc4e07ca1b305a4fcc3f9806025c1b651ea302646341222f88b/pexpect-4.6.0-py2.py3-none-any.whl (57kB)
    100% |████████████████████████████████| 61kB 15.6MB/s 
Collecting jedi>=0.10 (from ipython)
  Downloading https://files.pythonhosted.org/packages/c2/bc/54d53f5bc4658380d0eca9055d72be4df45e5bfd91a4bac97da224a92553/jedi-0.13.2-py2.py3-none-any.whl (177kB)
    100% |████████████████████████████████| 184kB 23.2MB/s 
Collecting traitlets>=4.2 (from ipython)
  Downloading https://files.pythonhosted.org/packages/93/d6/abcb22de61d78e2fc3959c964628a5771e47e7cc60d53e9342e21ed6cc9a/traitlets-4.3.2-py2.py3-none-any.whl (74kB)
    100% |████████████████████████████████| 81kB 21.5MB/s 
Collecting pickleshare (from ipython)
  Downloading https://files.pythonhosted.org/packages/9a/41/220f49aaea88bc6fa6cba8d05ecf24676326156c23b991e80b3f2fc24c77/pickleshare-0.7.5-py2.py3-none-any.whl
Collecting pygments (from ipython)
  Downloading https://files.pythonhosted.org/packages/13/e5/6d710c9cf96c31ac82657bcfb441df328b22df8564d58d0c4cd62612674c/Pygments-2.3.1-py2.py3-none-any.whl (849kB)
    100% |████████████████████████████████| 849kB 18.2MB/s 
Collecting decorator (from ipython)
  Downloading https://files.pythonhosted.org/packages/f1/cd/7c8240007e9716b14679bc217a1baefa4432aa30394f7e2ec40a52b1a708/decorator-4.3.2-py2.py3-none-any.whl
Requirement already satisfied: setuptools>=18.5 in /home/ubuntu/.pyenv/versions/3.6.8/envs/crud/lib/python3.6/site-packages (from ipython) (40.6.2)
Collecting prompt-toolkit<2.1.0,>=2.0.0 (from ipython)
  Downloading https://files.pythonhosted.org/packages/65/c2/e676da701cda11b32ff42eceb44aa7d8934b597d604bb5e94c0283def064/prompt_toolkit-2.0.8-py3-none-any.whl (342kB)
    100% |████████████████████████████████| 348kB 23.5MB/s 
Collecting ptyprocess>=0.5 (from pexpect; sys_platform != "win32"->ipython)
  Downloading https://files.pythonhosted.org/packages/d1/29/605c2cc68a9992d18dada28206eeada56ea4bd07a239669da41674648b6f/ptyprocess-0.6.0-py2.py3-none-any.whl
Collecting parso>=0.3.0 (from jedi>=0.10->ipython)
  Downloading https://files.pythonhosted.org/packages/49/f6/5108eb2c490c57d7ca3ac013e03e5c50f195aa1749b17a1fe553d63a37c2/parso-0.3.2-py2.py3-none-any.whl (93kB)
    100% |████████████████████████████████| 102kB 18.1MB/s 
Requirement already satisfied: six in /home/ubuntu/.pyenv/versions/3.6.8/envs/crud/lib/python3.6/site-packages (from traitlets>=4.2->ipython) (1.12.0)
Collecting ipython-genutils (from traitlets>=4.2->ipython)
  Downloading https://files.pythonhosted.org/packages/fa/bc/9bd3b5c2b4774d5f33b2d544f1460be9df7df2fe42f352135381c347c69a/ipython_genutils-0.2.0-py2.py3-none-any.whl
Collecting wcwidth (from prompt-toolkit<2.1.0,>=2.0.0->ipython)
  Downloading https://files.pythonhosted.org/packages/7e/9f/526a6947247599b084ee5232e4f9190a38f398d7300d866af3ab571a5bfe/wcwidth-0.1.7-py2.py3-none-any.whl
Installing collected packages: backcall, ptyprocess, pexpect, parso, jedi, ipython-genutils, decorator, traitlets, pickleshare, pygments, wcwidth, prompt-toolkit, ipython
  Running setup.py install for backcall ... done
Successfully installed backcall-0.1.0 decorator-4.3.2 ipython-7.2.0 ipython-genutils-0.2.0 jedi-0.13.2 parso-0.3.2 pexpect-4.6.0 pickleshare-0.7.5 prompt-toolkit-2.0.8 ptyprocess-0.6.0 pygments-2.3.1 traitlets-4.3.2 wcwidth-0.1.7
You are using pip version 18.1, however version 19.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(crud) ryungs:~/workspace/CRUD $ pip list
Package           Version
----------------- -------
backcall          0.1.0  
decorator         4.3.2  
Django            2.1.5  
django-extensions 2.1.4  
ipython           7.2.0  
ipython-genutils  0.2.0  
jedi              0.13.2 
parso             0.3.2  
pexpect           4.6.0  
pickleshare       0.7.5  
pip               18.1   
prompt-toolkit    2.0.8  
ptyprocess        0.6.0  
Pygments          2.3.1  
pytz              2018.9 
setuptools        40.6.2 
six               1.12.0 
traitlets         4.3.2  
wcwidth           0.1.7  
You are using pip version 18.1, however version 19.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(crud) ryungs:~/workspace/CRUD $ pyenv local 3.6.8
ryungs:~/workspace/CRUD $ pyenv local crud
(crud) ryungs:~/workspace/CRUD $ django-admin startapp menupan
(crud) ryungs:~/workspace/CRUD $ 
```



```django


pyenv local crud # 이 프로젝트는 crud 가상 환경을 쓰겠다
- 모든 프로젝트마다 가상환경을 만들고 각각 관리하는게 이상적이다
```



# Django-DJANGO_FROM 프로젝트 생성

make

resolve_url  새로 써봄

forms.py 새로 만들어 봄