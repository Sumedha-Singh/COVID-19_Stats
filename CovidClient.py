import http.client
import json

class CovidClient:
    def getCountryStats(self, countryName ):
        conn = http.client.HTTPSConnection( "covid-19-coronavirus-statistics.p.rapidapi.com" )

        headers = {
            'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
            'x-rapidapi-key': "37fc70bf1bmshaaccc7416b5b592p12729ajsnf46842bb0828"
        }

        conn.request( "GET","/v1/stats?country="+ countryName,headers=headers )

        res = conn.getresponse()
        data = res.read():q!






        stats = json.loads(data)
        stateStats = stats ["data"] ["covid19Stats"]

        for items in stateStats:
            print(str(items['province']) + "{type=death}" + str(items["deaths"]))
            print( str( items ['province'] ) + "{type=recovered}" + str( items ["recovered"] ) )
            print( str( items ['province'] ) + "{type=total}" + str( items ["confirmed"] ) )

        return stateStats

