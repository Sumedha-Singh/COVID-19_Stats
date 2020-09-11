# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
from CovidClient import CovidClient

app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/metrics', methods = ['GET', 'POST'])
def covidMetrics():
    c1 = CovidClient()
    stateStats = c1.getCountryStats("India")
    #statename{type=recovered} value
    toReturn = []
    for items in stateStats:
        toReturn.append( str( items['province'] ).replace(" ","_") + '{type="death"} ' + str( items["deaths"] ).replace("None","0") )
        toReturn.append( str( items['province'] ).replace(" ","_")  + '{type="recovered"} ' + str( items["recovered"] ).replace("None","0") )
        toReturn.append(  str( items['province'] ) .replace(" ","_") + '{type="confirmed"} ' + str( items["confirmed"] ).replace("None","0") )
    toReturn = "\n".join( toReturn )
    return toReturn




# driver function
if __name__ == '__main__':

	app.run(debug = True)
