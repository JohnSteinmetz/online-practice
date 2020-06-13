def two_sum(nums, target):

    targetValueDict= {}
    for index, value in enumerate(nums):
        targetValueDict[value] = index

    for index, value in enumerate(nums):
        if targetValueDict.__contains__(target - value):
            return [index, targetValueDict.get(target - value)]
   
    return []