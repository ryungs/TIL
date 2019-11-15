# git

## 1. git이 뭔데?

- git은 VCS : version control system
- git은 디렉토리를 기준으로 버전관리를 하는 프로그램
- 버전관리를 위해서 쓰는 것!



# git bash 

## window에서 unix 명령어 쓰려고 설치한 프로그램



## 명령어

- pwd : 현재 내 위치 확인
- cd 문서이름 
- tap : 자동완성
- ls : 파일 리스트 확인
- ls -a : 파일 리스트 모두 보기
- rm 파일이름 : 그 파일만 제거
- rm * : 현재 위치의 모든 파일 제거
- ctrl + c : 프로그램 진짜로 끄기
- bash : git bash 껐다 켜기 (수정사항 있을 때 적용하려면 필요)
- code . : 현재 위치에서 Visul Studio Code 켜기
- git help : git에서 쓸 수 있는 기능을 다 보여줌
- which git : git이 있는지 없는지 확인
- git log : 변경사항에 대한 리스트 확인
- config : configuration 의 줄임말로 설정에 관련된 모든 것

####   

####  처음 dir을 repo 진화시키고 git push 하는 방법

- git init : dir에 git 이라는 기능을 추가
  - git 기능을 넣은 디렉토리를  repository 라고 부른다
  - git 기능을 가진 repo로 진화되면 (master) 가 붙는다
  - rm -rf .git 하면 진화되기전 디렉토리로 돌아감
    - ~~망했을 때 사용!~~
- git add 파일이름 : repo의 변경사항을 찰칵 찍음!
  * git add . : 현재 내가 있는 repo의 모든 폴더 변경사항을 찰칵 찍음!
- git commit -m '간결하고 현재형으로' : 찰칵 사진찍은 상태까지 올려줌
- git remote : 내가 어디로 올릴거야 라고 손가락질만 하는 행동
  * git remote add origin (클립보드 복사) : 제일 처음 할 때만
- gir remote -v : pull 과 push 하는 곳을 알려줌
  * fetch : 받아오는 곳
  * push : 올리는 곳
- git push 
  * git push -u origin master : 처음 push 할 때만



#### 처음 git pull 하는 방법

- 원하는 디레토리로 이동 마지막에 (master) 붙어있는지 확인
- git clone (클립보드 복사) : 처음 할 때 만 
- git pull



#### vim으로 단축명령어 만들기

- git bash에서 입력어 줄임말 만들고 싶을 때
  - bashrc : 내가 설정파일
  - touch .bashrc  -> vim . bashrc -> alias 'jn'='jupyter notebook' ->:w(저장)->:qa!(나오기)  
- cat .bachrc : 단축명령어 목록볼 때  

touch bashrc  

alias 'jn'='jupyter notebook'  > bashrc



# git hub에 백업하기

- 이제 내 컴퓨터에 사용한 git을 클라우드에 백업해보자
- 다양한 클라우드 중 우리는 'git hub'를 사용 



