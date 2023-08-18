def containsDuplicate(nums):
    hashSet = set()

    for n in nums:
        if n in hashSet:
            return True
        hashSet.add(n)
    return False


print("Does not contain duplicate")
print(containsDuplicate([8,7,6,2,3,1]))
print("Contains duplicate")
print(containsDuplicate([8,7,6,2,3,1,1]))