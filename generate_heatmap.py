import json
from github_contributions_canvas import GithubContributionsCalendar

def main():
    dates = json.loads(open("dates.json").read())
    cal = GithubContributionsCalendar()
    cal.add_contributions(dates)  # 默认绿色
    cal.draw("heatmap.svg")

if __name__ == "__main__":
    main()
