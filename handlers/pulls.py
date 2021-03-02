import requests

owner = "alenaPy"
repo = "devops_lab"
per_page = 100
url_pulls = f'https://api.github.com/repos/{owner}/{repo}/pulls'
url1 = f'https://api.github.com/search/issues?q=is:pr%20label:"accepted"\
                    %20repo:{owner}/{repo}&per_page={per_page}'
url2 = f'https://api.github.com/search/issues?q=is:pr%20label:"needs%20work"\
                  %20repo:{owner}/{repo}&per_page={per_page}'


def get_pulls(state):
    pull = requests.get(url_pulls)
    if state == "closed" or state == "open":
        pull = requests.get(url_pulls, params={'state': '{0}'.format(state), 'per_page': 100})
    if state == "needs work":
        pull = requests.get(url2, params=per_page)
        return pull.json()["items"]
    if state == "accepted":
        pull = requests.get(url1, params=per_page)
        return pull.json()["items"]
    return pull.json()
