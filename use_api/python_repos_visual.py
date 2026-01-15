import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call, and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
# print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict["items"]
repo_links, stars, labers = [], [], []
for repo_dict in repo_dicts:
    repo_names = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_names}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    laber = f"{owner}<br />{description}"
    labers.append(laber)

# Make visualization.
data = [
    {
        "type": "bar",
        "x": repo_links,
        "y": stars,
        "hovertext": labers,  # 这里是 hovertext，而不是 label
        "marker": {
            "color": "rgb(60, 100, 150)",
            "line": {"width": 1.5, "color": "rgb(25, 25, 25)"},
        },
        "opacity": 0.6,
    }
]

# 自定义布局, 这里的 title 是一个包含 text 和 font 的字典
my_layout = {
    "title": {
        "text": "GIHUB上最受欢迎的Python项目",  # 将 title 变为包含 text 和 font 的字典
        "font": {"size": 28},
    },
    "xaxis": {
        "title": {"text": "仓库", "font": {"size": 24}},
        "tickfont": {"size": 14},  # 这里依然是 tickfont
    },
    "yaxis": {
        "title": {"text": "星级", "font": {"size": 24}},
        "tickfont": {"size": 14},
    },
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="python_repos.html")
