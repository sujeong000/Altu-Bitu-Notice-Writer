# Altu-Bitu-Notice-Writer

알튜비튜 튜터링 과제 공지를 위한 마크다운 문서를 자동으로 작성해주는 도구입니다.

1. **문제 정보 수집**: 주어진 문제 번호를 기반으로 Solved.ac API를 활용하여 문제 정보를 수집합니다.
2. **마크다운 표 생성**: 문제 번호 목록을 바탕으로 마크 다운 형식의 표를 생성합니다. 문제 번호, 이름, 난이도, 풀이 링크, 문제 분류 정보로 구성됩니다. 라이브코딩, 필수, 도전 문제 목록을 보여주는 용도로 사용됩니다.
3. **과제 마감일 계산**: 금요일 강의 날짜를 기준으로 과제 마감일을 계산하여 마크 다운 형식의 공지문을 생성합니다. 정규 제출은 수요일 강의 시간 전까지, 추가 제출은 목요일 자정까지로 설정되어 있습니다.


## 사용 방법
1. 터미널을 엽니다.
2. 프로그램이 저장된 디렉토리로 이동합니다.
3. 프로그램을 실행합니다. 다음 명령어를 입력하세요.
    ```
    python notice_writer.py
    ```
4. 프로그램이 실행되면 터미널에서 과제 정보를 입력을 하게 됩니다. 프롬프트에 따라 주차 번호, 해당 주차 알고리즘명, 날짜 등을 입력해주세요.
5. 프로그램이 입력을 받은 후, 마크다운 형식의 공지 내용이 출력됩니다. 이를 원하는 위치에 복사하여 사용하세요.

## 입력 예시
```Bash
몇주차인가요? (숫자만 입력하세요): 1
알고리즘 명을 입력하세요 (공백은 언더바로 대체): 정렬_맵_셋
금요일 강의 날짜를 입력하세요 (2023.09.01 형식): 2023.08.18
라이브 코딩 문제 번호들을 입력하세요 (공백으로 구분): 10825 1620 2002 2750 2751 7785
필수 문제 번호들을 입력하세요 (공백으로 구분): 1431 14425 19636
도전 문제 번호들을 입력하세요 (공백으로 구분): 1946 9375
힌트 5개를 다음과 같은 형식으로 각 줄에 작성해주세요. (ex. 10234 문제 조건을 꼼꼼히 확인하세요)
0번 힌트를 입력하세요: 1431 서류심사와 면접심사의 성적을 모두 고려해 동시에 비교하려니 힘드네요. 하나의 심사 순위만 비교하려면 어떻게 해야 할까요?
1번 힌트를 입력하세요: 14425 문자열의 개수 N, M이 꽤 크네요. 문자열을 효율적으로 관리할 수 있는 방법이 있을까요?
2번 힌트를 입력하세요: 1946 두 가지 순위를 비교하고 있어요. 동시에 비교하기보다는 하나를 고정하고 다른 하나를 비교하면 좋을 것 같아요!
3번 힌트를 입력하세요: 9375 의상의 이름과 의상의 종류 중 우리에게 필요한 입력값은 무엇일까요? 의상을 입지 않는 경우를 조심해야 할 것 같아요.
4번 힌트를 입력하세요: 19636 문제가 조금 복잡하네요! 당황하지 말고 천천히 읽어보며 코드로 구현해봅시다. C++로 풀이할 경우, ⌊−5 / 2⌋ = -3이 나오는지 꼭 확인해보세요!
```

## 공지 내용 예시

# 정렬_맵_셋
[메인으로 돌아가기](https://github.com/Altu-Bitu-5/Notice) 
## 💻 튜터링 
### 라이브 코딩
| 문제 번호 | 문제 이름 | 난이도 | 풀이 링크 | 분류 |
| :-: | :-: | :-: | :-: | :-: |
| [10825](https://www.acmicpc.net/problem/10825) | [국영수](https://www.acmicpc.net/problem/10825) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/라이브코딩/10825.cpp) | 정렬 |
| [1620](https://www.acmicpc.net/problem/1620) | [나는야 포켓몬 마스터 이다솜](https://www.acmicpc.net/problem/1620) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/라이브코딩/1620.cpp) | 자료 구조, 해시를 사용한 집합과 맵 |
| [2002](https://www.acmicpc.net/problem/2002) | [추월](https://www.acmicpc.net/problem/2002) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/라이브코딩/2002.cpp) | 자료 구조, 해시를 사용한 집합과 맵, 구현, 문자열 |
| [2750](https://www.acmicpc.net/problem/2750) | [수 정렬하기](https://www.acmicpc.net/problem/2750) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/라이브코딩/2750.cpp) | 정렬, 구현 |
| [2751](https://www.acmicpc.net/problem/2751) | [수 정렬하기 2](https://www.acmicpc.net/problem/2751) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/라이브코딩/2751.cpp) | 정렬 |
| [7785](https://www.acmicpc.net/problem/7785) | [회사에 있는 사람](https://www.acmicpc.net/problem/7785) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/라이브코딩/7785.cpp) | 자료 구조, 해시를 사용한 집합과 맵 |
## ✏️ 과제 
### 마감기한
~ 8 / 23 (수) 18:59 - 과제 제출 </br>
~ 8 / 24 (목) 23:59 - 추가 제출 </br>
### 필수
| 문제 번호 | 문제 이름 | 난이도 | 풀이 링크 | 분류 |
| :-: | :-: | :-: | :-: | :-: |
| [1431](https://www.acmicpc.net/problem/1431) | [시리얼 번호](https://www.acmicpc.net/problem/1431) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/필수/1431.cpp) | 정렬 |
| [14425](https://www.acmicpc.net/problem/14425) | [문자열 집합](https://www.acmicpc.net/problem/14425) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/필수/14425.cpp) | 자료 구조, 해시를 사용한 집합과 맵, 문자열, 트리를 사용한 집합과 맵 |
| [19636](https://www.acmicpc.net/problem/19636) | [요요 시뮬레이션](https://www.acmicpc.net/problem/19636) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/필수/19636.cpp) | 구현 |
### 도전
| 문제 번호 | 문제 이름 | 난이도 | 풀이 링크 | 분류 |
| :-: | :-: | :-: | :-: | :-: |
| [1946](https://www.acmicpc.net/problem/1946) | [신입 사원](https://www.acmicpc.net/problem/1946) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/도전/1946.cpp) | 그리디 알고리즘, 정렬 |
| [9375](https://www.acmicpc.net/problem/9375) | [패션왕 신해빈](https://www.acmicpc.net/problem/9375) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/01_정렬_맵_셋/도전/9375.cpp) | 조합론, 자료 구조, 해시를 사용한 집합과 맵, 수학 |
---
 ### 힌트
<details><summary>시리얼 번호</summary><div markdown="1">&nbsp;&nbsp;&nbsp;&nbsp;서류심사와 면접심사의 성적을 모두 고려해 동시에 비교하려니 힘드네요. 하나의 심사 순위만 비교하려면 어떻게 해야 할까요?</div></details>
<details><summary>문자열 집합</summary><div markdown="1">&nbsp;&nbsp;&nbsp;&nbsp;문자열의 개수 N, M이 꽤 크네요. 문자열을 효율적으로 관리할 수 있는 방법이 있을까요?</div></details>
<details><summary>신입 사원</summary><div markdown="1">&nbsp;&nbsp;&nbsp;&nbsp;두 가지 순위를 비교하고 있어요. 동시에 비교하기보다는 하나를 고정하고 다른 하나를 비교하면 좋을 것 같아요!</div></details>
<details><summary>패션왕 신해빈</summary><div markdown="1">&nbsp;&nbsp;&nbsp;&nbsp;의상의 이름과 의상의 종류 중 우리에게 필요한 입력값은 무엇일까요? 의상을 입지 않는 경우를 조심해야 할 것 같아요.</div></details>
<details><summary>요요 시뮬레이션</summary><div markdown="1">&nbsp;&nbsp;&nbsp;&nbsp;문제가 조금 복잡하네요! 당황하지 말고 천천히 읽어보며 코드로 구현해봅시다. C++로 풀이할 경우, ⌊−5 / 2⌋ = -3이 나오는지 꼭 확인해보세요!</div></details>

---
