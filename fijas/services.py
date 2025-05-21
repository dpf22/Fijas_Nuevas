import requests

def get_last_results(team_name):
    search_url = f"https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t={team_name}"
    search_resp = requests.get(search_url).json()
    if not search_resp['teams']:
        return None, None

    team_id = search_resp['teams'][0]['idTeam']
    events_url = f"https://www.thesportsdb.com/api/v1/json/1/eventslast.php?id={team_id}"
    events_resp = requests.get(events_url).json()
    return search_resp['teams'][0], events_resp['results']
