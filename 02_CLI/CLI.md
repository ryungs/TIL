# OS & Command Line Interface



## OS (Operating System) : 운영체제

- 시스템 하드웨어를 관리할 뿐 아니라 응용 소프트웨어를 실행하기 위하여 하드웨어 추상화 플랫폼과 공통 시스템 서비스를 제공하는 시스템 소프트웨어이다. 



## CLI : 명령 줄 인터페이스

**명령 줄 인터페이스**(CLI, Command line interface) 또는 **명령어 인터페이스**는 가상 터미널 또는 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식을 뜻한다. 즉, 작업 명령은 사용자가 컴퓨터 키보드 등을 통해 문자열의 형태로 입력하며, 컴퓨터로부터의 출력 역시 문자열의 형태로 주어진다.



## CLI 명령어

* pwd : 현재 위치 알려줌
* cd : 특정 디멘토리로 이동 (폴더 더블클릭과 같음)
* cd ~ : cd home , 나의 기본적인 집
* cd .. : 한단계 위로 나가겠다
* cd . 지금 내가 있는 곳, 제자리 점프와 같다
* 맨 앞에 있는 / = 내 pc



#### 리스트 관련 명령어

- ls : 파일 리스트 보여줌

- ls a : a라는 파일 보여줌

- ls a* : a로 시작하는 모든 파일 보여줌

- ls -a : 숨겨진 파일 다 보여줌
  - . 찍혀 있는 건 : 숨겨진 목록

- ls -l : 길게 보여줌

- ls -al: a와 l 기능 두개 합져서 보여줌

- ls -lh :용량을 환산해줌



#### 생성 관련 명렁어

* mkdir : make 디렉토리  (폴더 생성)
  - mkdir -p : 폴더 안에 폴더 생성
* touch : 파일 생성
* vim classmates.txt 하면 생성된 파일 수정가능



#### 지우기 관련 명령어

- mv (reverse.txt rev.txt) : 파일 이름 바꾸기 

- rm (rev.txt) : 파일 지우기 
- rm -p : 폴더 지우기 

- rm -i (rev.txt) :  확인절차 안내문 뜨고 yes 해야 삭제

- rm -f (rev.txt) : 강제로 지우기 ! 확인절차 안내문도 안 뜸!

- rm - rf : 진짜 완전 다 지운다

- rm *  : 모든 것 완전 다 지우고 싶다. 강려크
- sudo rm -rf : ....

- cp (rev.txt copy.txt) : 파일 복사

  

### > unix 운영체제 명령어

* $ : 프롬프트라는 뜻 (너의 명령을 받아들일 준비가 되어 있다)

* ctrl + c :  명령취소

* ^ (캐럿) : ctrl 뜻

* echo 가 print 문

  * echo hello 치면 hello 출력된다 
  * echo 'hello' echo "hello" 다 가능
  * echo는 standard out 이다
  * echo 'When I was a young girl' > black_parade.txt : txt 생성 후 echo 문 넣기

* man : manual, 명령어에 대한 설명문

* q : 나가기

* 좌우 키 : 진짜 좌우 이동

  상하 키 : 이전 이후 명령어 이동 (ctrl + p, n)

* ctrl + l : clear, 화면을 밀어준다

* ctrl + d : terminal 자체를 끈다

* sleep = 컴퓨터를 잠재운다. 

  * sleep 5s
  * 깨우고 싶으면 ctrl + c = 명령취소

* cat : 특정 파일에 있는 문서를 출력해주는 것

* 파일 마지막에 enter 꼭 쳐 줄 것!

* '>' 덮어쓴다

  '>>' 추가한다

  - cat line_1.txt >> song.txt

    cat line_1.txt line_2.txt >> reverse.txt 가능

* head sonnets.txt : 처음 열줄 보기

  tail sonnets.txt : 마지막 열줄 보기

* ping google.com : 서버가 죽었는지 알아볼 수 있다

* ping google.com > google.log

  tail -f google.com 

* wc sonnets.txt :  2620 줄 단어 바이트를 알려준다 (word count)

* '|'(파이프) : head sonnets.txt | wc : 파이프 앞의 표준 출력을 뒤에 있는 명령어로 알려준다

* u : page up 

* d: page doum

* / : 검색

  -g : g 검색

* shift + n : 이전검색

* n : 다음검색

* less : 파일 뷰어

* grep 

  - grep rose sonnets.txt  (rose라는 단어를  sonnets 파일에서 찾겠다)

  * grep rose sonnets.txt | wc (rose라는 단어 개수)
  * grep -i rose sonnets.txt  (case in sensitive) : 대소문자 상관 없이 rose 를 찾겠다

* ps aux : 컴퓨터에서 돌고 있는 모든 프로그램 리스트 보기

* ps aux | grep 프로세스 이름 : 프로세스를 강제로 끌 때

* top : 컴퓨터에서 가장 리소스를 많이 잡아 먹고 있는 프로그램 리스트