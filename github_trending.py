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


def print_trending_repositories(repo, issues_count):
    print('{0:>5} {2:^6} {1}'.format(
        repo['stargazers_count'],
        repo['html_url'],
        issues_count
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
        exit('Failed to establish connection to api.github.com')
    print('Stars Issues URL')
    for repo in top_repos:
        print_trending_repositories(
            repo, get_open_issues_amount(repo['full_name'])
            )
