import requests
from datetime import datetime, timedelta

class Problem:
    def __init__(self, number, title, link, level, tags):
        self.number = number
        self.title = title
        self.link = link
        self.level = level
        self.tags = tags

# 문제 번호로 문제 정보를 얻어옵니다.
def get_problem(problem_number):
    url = f"https://solved.ac/api/v3/problem/show?problemId={problem_number}"
    
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()

        title = json_data.get('titleKo', 'Title not found')
        level = json_data.get('level', 0)
        link = f"https://www.acmicpc.net/problem/{problem_number}"
        tags = [
            name_data["name"] for tag in json_data["tags"]
            for name_data in tag["displayNames"]
            if name_data["language"] == "ko"
        ]
        return Problem(problem_number, title, link, level, tags)
    else:
        return "Problem not found"
    
# 문제 리스트를 바탕으로 마크다운 표를 만듭니다.
def make_markdown_table(problems, problem_type, week_title):
    markdown_table = "| 문제 번호 | 문제 이름 | 난이도 | 풀이 링크 | 분류 |\n"
    markdown_table += "| :-: | :-: | :-: | :-: | :-: |\n"

    for problem in problems:
        markdown_table += f"| [{problem.number}]({problem.link}) "
        markdown_table += f"| [{problem.title}]({problem.link}) "
        markdown_table += f"| <img height=\"25px\" width=\"25px\" src=\"https://static.solved.ac/tier_small/{problem.level}.svg\"/> "
        markdown_table += f"| [바로가기](https://github.com/Altu-Bitu-5/Notice/blob/main/{week_title}/{problem_type}/{problem.number}.cpp) "
        markdown_table += f"| {', '.join(problem.tags)} |\n"

    return markdown_table

# 과제 마감일 마크다운을 만듭니다.
def make_due_date_markdown(date):
    date_format = "%Y.%m.%d"
    input_date = datetime.strptime(date, date_format)
    regular_due = input_date + timedelta(days=5)
    extra_due = input_date + timedelta(days=6)

    weekday_korean = {
        0: "월",
        1: "화",
        2: "수",
        3: "목",
        4: "금",
        5: "토",
        6: "일"
    }

    markdown = f"~ {regular_due.month} / {regular_due.day} ({weekday_korean[regular_due.weekday()]}) 18:59 - 과제 제출 </br>\n"
    markdown += f"~ {extra_due.month} / {extra_due.day} ({weekday_korean[extra_due.weekday()]}) 23:59 - 추가 제출 </br>\n"

    return markdown

# 힌트 마크다운을 만듭니다.
def make_hints_markdown(hints):
    markdown = "---\n ### 힌트\n"
    for hint in hints:
        splits = hint.split()
        problem_number = int(splits[0])
        description = ' '.join(splits[1:])
        markdown += f"<details><summary>{get_problem(problem_number).title}</summary><div markdown=\"1\">&nbsp;&nbsp;&nbsp;&nbsp;{description}</div></details>\n"
    markdown += "\n---\n"
    
    return markdown

# 전체 마크다운을 만듭니다.
def make_total_markdown(week_number, algorithm_name, start_date, live_coding_problems, essential_problems, challenge_problems, hints):
    week_title = f"{week_number}_{algorithm_name}"

    markdown = f"# {algorithm_name}\n"
    markdown += "[메인으로 돌아가기](https://github.com/Altu-Bitu-5/Notice) \n## 💻 튜터링 \n### 라이브 코딩\n"
    markdown += make_markdown_table([get_problem(problem) for problem in live_coding_problems], "라이브코딩", week_title)
    markdown += "## ✏️ 과제 \n"
    markdown += "### 마감기한\n"
    markdown += make_due_date_markdown(start_date)
    markdown += "### 필수\n"
    markdown += make_markdown_table([get_problem(problem) for problem in essential_problems], "필수", week_title)
    markdown += "### 도전\n"
    markdown += make_markdown_table([get_problem(problem) for problem in challenge_problems], "도전", week_title)
    markdown += make_hints_markdown(hints)

    return markdown

############################### 입력 #####################################
# 주차 번호
week_number = input("몇주차인가요? (숫자만 입력하세요): ").zfill(2)
# 알고리즘 이름
algorithm_name = input("알고리즘 명을 입력하세요 (공백은 언더바로 대체): ")
# 강의 날짜
start_date = input("금요일 강의 날짜를 입력하세요 (2023.09.01 형식): ")
# 라이브코딩 문제
live_coding_problems = list(map(int, input("라이브 코딩 문제 번호들을 입력하세요 (공백으로 구분): ").split()))
# 과제 필수 문제
essential_problems = list(map(int, input("필수 문제 번호들을 입력하세요 (공백으로 구분): ").split()))
# 과제 도전 문제
challenge_problems = list(map(int, input("도전 문제 번호들을 입력하세요 (공백으로 구분): ").split()))
# 힌트 목록
print("힌트 5개를 다음과 같은 형식으로 각 줄에 작성해주세요. (ex. 10234 문제 조건을 꼼꼼히 확인하세요)")
hints = [input(f"{i}번 힌트를 입력하세요: ") for i in range(5)]

############################### 출력 #####################################
markdown = make_total_markdown(week_number, algorithm_name, start_date, live_coding_problems, essential_problems, challenge_problems, hints)
print(markdown)
