#Pandas SERIES
#pandas series is like coloumn in a table ...like and coloumn for an array
import pandas as pd
mydataset = {
     "Cars":["BMW", "Volvo", "Ford"],
     "Passings" :[3, 7, 2]
 }
 
myvar = pd.DataFrame(mydataset, index= [1,2,3])
print(myvar)
print()
#Pandas SERIES
#pandas series is like coloumn in a table ...like and coloumn for an array
import pandas as pd
arr =[1,2,3,4]
myvar = pd.Series(arr)
print(myvar)

#now if want to retrieve an specific value from the table the lable that got generated in against of each item starting from 0 i will do it like this
print()
print(myvar[0])
print()
#but we cabn create label as well
myvar =pd.Series(arr, index =[1,2,3,4])
print(myvar)


#we can also get key-value pairs as an object of series

week = {"Monday" :1,"Tuesday" : 2, "Wednesday" : 4, "Thursday" :5,  "Friday ":6, "Saturday":7}
myvar = pd.Series(week)
print(myvar)
print()


