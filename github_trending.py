import datetime
import requests


def get_starting_date(days):
    return datetime.date.today() - datetime.timedelta(days=days)


def get_trending_repositories(top_size, date):
    url = 'https://api.github.com/search/repositories'
    payload = {
        'q': 'created:>={}'.format(date),
        'sort': 'stars',
        'per_page': '{}'.format(top_size),
    }
    return requests.get(url, params=payload).json()['items']


def get_open_issues_amount(full_repo_name):
    url = 'https://api.github.com/repos/{0}/issues'.format(full_repo_name)
    return len(requests.get(url).json())


def print_trending_repositories(repos):
    print('Stars Issues URL')
    for repo in top_repos:
        print('{1:>5} {0:^6} {2}'.format(
            get_open_issues_amount(repo['full_name']),
            repo['stargazers_count'],
            repo['html_url']
            )
        )


if __name__ == '__main__':
    top_size = 20
    days = 7
    try:
        top_repos = get_trending_repositories(
            top_size, get_starting_date(days)
            )
    except requests.exceptions.ConnectionError:
        print('Failed to establish connection to api.github.com')
    else:
        print_trending_repositories(top_repos)
