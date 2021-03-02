import requests

owner = "alenaPy"
repo = "devops_lab"
per_page = 100


def get_pulls(state):
    url_pulls = f'https://api.github.com/repos/{owner}/{repo}/pulls?state={state}&per_page={per_page}'
    url_main = f'https://api.github.com/search/issues?q=is:pr%20label:\"{state}\"%20repo:{owner}/{repo}&per_page={per_page}'
    url_all = f'https://api.github.com/search/issues?q=is:pr%20label:"needs%20work"%20repo:{owner}/{repo}&per_page={per_page}'
    if state in ('open', 'closed'):
        response = requests.get(url_pulls, params=state)
        pull = response.json()
    elif state in ('needs work', 'accepted'):
        response = requests.get(url_main, params=state)
        pull = response.json()['items']
    else:
        response = requests.get(url_all)
        pull = response.json()

    output = []
    for item in pull:
        output.append({'num': item['number'], 'title': item['title'], 'link': item['html_url']})
    return output
