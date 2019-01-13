# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
 data = yaml.load(f)
 f.close()
#print(data)
# Find data type of the file
type_of_data =type(data)
print("type of data is",type_of_data) 

# In which city, and at which venue the match was played and where was it played ?
city= data['info']['city']
print("the city which match was played is",city)
 
venue= data['info']['venue']
print("venue of the match was",venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
team1=data['info']['teams'][0]
team2=data['info']['teams'][1]
print('teams are played in the tournament',team1,"and", team2)
# Which team won the toss and what was the decision of toss winner ?
toass_winner=data["info"]['toss']['winner']
toass_decision=data["info"]['toss']['decision']
print('toss win by',toass_winner)
print('decision of toss winner',toass_decision)

# Find the first bowler and first batsman who played the first ball of the first inning

first_bowler= data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
print(first_bowler)
#first_batsman= data['innings'][0]['1st innings']['deliveries'][[0][0.1]['batsman']
#print(first_batsman)
# How many deliveries were delivered in first inning ?
#deliveries_1st_innings= len(data['innings'][0]['1st innings']['deliveries'])
#print("deliverise deliverd in first innings",deliveries_1st_innings)
# How many deliveries were delivered in second inning ?
#deliveries_2nd_innings= len(data['innings'][1]['2nd innings']['deliveries'])
#print(deliveries_2nd_innings)
# Which team won and how ?
#winner= data['info']['outcome']['winner']
#how= data['info']['outcome']['by']['runs']
#print(winner, "won by",how,"runs")


