# Put your function here
def  timesTable(nums):
    times_table = [[1,2,3,4,5],[2,4,6,8,10],[3,6,9,12,15],[4,8,12,16,20],[5,10,15,20,25]]
    return times_table[nums-1]
# testing
nums = int(input())
print(timesTable(nums))

