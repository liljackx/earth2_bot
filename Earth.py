import json
import requests
from bs4 import BeautifulSoup

class Earth(object):

    def __init__(self):
        self.base_uri = "https://app.earth2.io/graphql"
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.284",
        }
        self.loggedCookies = self._load_cookies()
        self.s = requests.Session()
        self.s.cookies.set(**self.loggedCookies)
        self.user_data = self._get_curr_user_infos()

    def _load_cookies(self, filename="./cookies.json"):
        with open(filename, 'r') as jsonCookies:
            return json.load(jsonCookies)

    def _exec(self, query):
        return self.s.post(
            self.base_uri,
            headers=self.headers,
            data={"query":query}
        ).json()

    def _get_curr_user_infos(self):
        page = self.s.get("https://app.earth2.io/#profile")
        soup = BeautifulSoup(page.content, "html.parser")
        s = soup.findAll('script')
        script_tag = s[-1:][0]
        json_dict = str(script_tag).split("riot.auth0user = ")[1].split("static_url")[0].strip().replace("'", '"')
        data = u'{}'.format(json_dict)
        return json.loads(data)

    def get_user_infos(self):
        return self.user_data

    # Provo a comprare
    # tildIds => id celle che vogliamo acquistare
    def tryPayement(self, tileIds):
        query = 'mutation { buyNewLandfield( tiles: ' + tileIds + ', center: "55.014038 24.982635", description: "Dubai", location: "Dubai, Dubai, United Arab Emirates", promoCodeId: "undefined" ) { landfield { id, thumbnail, description, location, forSale, price, center, tileIndexes, owner { username }, transactionSet { price, timeStr, previousOwner { username, } owner { username, } } } } }'
        response = self._exec(query)
        return response

e = Earth()
e._get_curr_user_infos()