import timeit, statistics

t=timeit.Timer("shortest_path","import shortest_path")


print("Calling timeit for 5 passes, each pass is 1000 calls timed cumulatively")
results=t.repeat(5,1000)
for i, item in enumerate(results):
    print(i, "\t", item)
print("Average execution time over 5 passes is:",format(statistics.mean(results),'.4f'))
print("\nSame example, but using range to show how the number of passes arg effects cpu usage ")
for i in range(25000,100001,25000):

    results=t.repeat(5,i)
    print("timeit number value is = ",i,"Average execution time:",format(statistics.mean(results),'.4f'))