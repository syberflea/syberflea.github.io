import requests as req


def get_top_repos():
    base_url = "https://api.github.com/search/repositories"

    # Params for the API request
    params = {
        'q': 'stars:>1000',  # Search for repositories with more than 1000 stars
        'sort': 'stars',
        'order': 'desc',
    }

    # Making the API request to search for top repos
    resp = req.get(base_url, params=params)

    if resp.status_code == 200:
        # API call successful
        results = resp.json()['items']

        print("Top Repos:")
        for repo in results[:5]:  # Display details of the top 5 repos
            print(f"\nRepo Name: {repo['name']}")
            print(f"Owner: {repo['owner']['login']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"Desc: {repo.get('description', 'No desc')}")
            print(f"URL: {repo['html_url']}")
    else:
        print(f"Failed to get top repos. Status code: {resp.status_code}")


if __name__ == '__main__':
    get_top_repos()
