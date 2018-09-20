import datetime
import requests


def get_date(period):
    return datetime.date.today() - datetime.timedelta(days=period)


def get_trending_repositories(top_size, date):
    url = 'https://api.github.com/search/repositories'
    payload = {
        'q': 'created:>={}'.format(date),
        'sort': 'stars',
        'per_page': '{}'.format(top_size),
    }
    return requests.get(url, params=payload).json()['items']


def print_trending_repositories(repos):
    print('Stars Issues URL')
    for item in top_repos:
        print('{0:>5} {1:^6} {2}'.format(
            item['stargazers_count'],
            item['open_issues_count'],
            item['html_url']
            )
        )


if __name__ == '__main__':
    top_size = 20
    period = 7
    try:
        top_repos = get_trending_repositories(top_size, get_date(period))
    except requests.exceptions.ConnectionError:
        print('Failed to establish connection to api.github.com')
    else:
        print_trending_repositories(top_repos)
