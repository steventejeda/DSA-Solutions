class SparseVector:
    def __init__(self, nums):
        self.nums = []

        for i, n in enumerate(nums):
            self.nums.append((i, n))
    
    def dotProduct(self, vec):
        dot_product = 0
        i = j = 0 

        while i < len(self.nums) and j < len(vec.nums): 
            num_index, num_val = self.nums[i]
            vec_index, vec_val = vec.nums[j]

            if num_index == vec_index:
                dot_product += (num_val * vec_val)
                i += 1
                j += 1
            elif num_index > vec_index:
                j += 1
            else:
                i += 1 
        return dot_product

ob1, ob2 = SparseVector([1,0,0,2,3]), SparseVector([0,3,0,4,0])
print(ob1.dotProduct(ob2))