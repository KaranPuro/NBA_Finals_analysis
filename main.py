# start off by assigning a value to the dictionary
nba_2010_results = {'Year':'2010', 'Team Won':'Lakers','Team Lost':'Celtics',"SeriesRecord":"4-3","FinalsMVP":"Kobe"}

# using the hard brackets, it allows you to incorporate the list into the dictionary, by use of key value replacement
nba_2010_results["Losers"] = ['Paul P, Kevin G']
nba_2010_results["Winners"] = ['Kobe B, Pau G']
nba_2010_results["Leading Scorer"] = ['Kobe, 28.6ppg']

nba_2011_results = {"Year":"2011","TeamWon":"Mavericks","TeamLost":"Heat","SeriesRecord":"4-2","FinalsMVP":"Dirk"}

nba_2011_results["Losers"] = ["Lebron J, Dwayne W"]
nba_2011_results["Winners"] = ["Dirk N, Jason T"]
nba_2011_results["Leading Scorer"] = ["Dwayne, 26.5ppg"]

nba_2012_results = {"Year":"2012","TeamWon":"Heat","TeamLost":"Thunder","SeriesRecord":"4-1","FinalsMVP":"Lebron"}

nba_2012_results["Losers"] = ["Kevin D, Russ W"]
nba_2012_results["Winners"] = ["Lebron J, Dwayne W"]
nba_2012_results["Leading Scorer"] = ["Kevin, 30.6ppg"]

nba_2013_results = {"Year":"2013","TeamWon":"Heat","TeamLost":"Spurs","SeriesRecord":"4-3","FinalsMVP":"Lebron"}

nba_2013_results["Losers"] = ["Tim D, Tony P"]
nba_2013_results["Winners"] = ["Lebron J, Dwayne W"]
nba_2013_results["Leading Scorer"] = ["Lebron, 25.3ppg"]

nba_2014_results = {"Year":"2014","TeamWon":"Spurs","TeamLost":"Heat","SeriesRecord":"4-1","FinalsMVP":"Kawhi"}
nba_2014_results["Losers"] = ["Lebron J, Dwayne W"]
nba_2014_results["Winners"] = ["Kawhi L, Tim D"]
nba_2014_results["Leading Scorer"] = ["Lebron J, 28.3ppg"]

nba_2015_results = {"Year":"2015","TeamWon":"Warriors","TeamLost":"Cavaliers","SeriesRecord":"4-2","FinalsMVP":"Iguodola"}

nba_2015_results["Losers"] = ["Lebron J, Matt D"]
nba_2015_results["Winners"] = ["Andre I, Steph C"]
nba_2015_results["Leading Scorer"] = ["Lebron J, 35.8ppg"]
# after you repeat the process and define all your dictionaries, combine them into a singular variable for ease of use
nba_finals_results = [nba_2010_results,nba_2011_results,nba_2012_results,nba_2013_results,nba_2014_results,nba_2015_results]
# use 'for' 'in' to properly organize code
for item in nba_finals_results:
    print(item)


print('the point of this analysis is to show the NBA finals opponents through the years and to designate the fluctuation in competition \nduring that span.')

# \n was used so i could skip to the next line
