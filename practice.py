print("Hey there, i'm ur daily task regulator or u can call me inspector. \n lets only start with 3 tasks for now")
task1=input("pls enter your 1st task:")
task2=input("pls enter your 2nd task:")
task3=input("pls enter your 3rd task:")
incompletelist=[task1,task2,task3]
completedlist=[]
print("please answer the following questions with yes or no")
task1resp=input("so did u complete {}:".format(task1))
if(task1resp=="yes"):
    print("thats nice")
    completedlist.append(task1)
    incompletelist.remove(task1)
else:
    print("hm hm cpmplete it without fail")

task2resp=input("so did u complete {}:".format(task2))
if(task2resp=="yes"):
    print("thats nice")
    completedlist.append(task2)
    incompletelist.remove(task2)
else:
    print("hm hm cpmplete it without fail")

task3resp=input("so did u complete {}:".format(task3))
if(task3resp=="yes"):
    print("thats nice")
    completedlist.append(task3)
    incompletelist.remove(task3)
else:
    print("hm hm cpmplete it without fail")

print("so the list of tasks u need to do yet are:",incompletelist)
print("and the list of tasks u completed are:", completedlist)

print(" come on, you can do it")