import  matplotlib.pyplot as plt
import  csv

win_by_runs=[]
player_of_match=[]

with open('matche.csv','r') as csvfile:
    plots =csv.reader(csvfile,delimiter=',')
    for column in plots:
        
        win_by_runs.append((column[10]))
        player_of_match.append((column[12]))

#plt.plot(open_price_y1,close_price_y2 ,label='Loaded from file!')

plt.bar(win_by_runs,player_of_match,label='bar plot')
plt.xlabel('win_by_runs(scale= 1:10-20)')  
plt.ylabel('player_of_match')

plt.title('matches')
plt.legend()
plt.show()