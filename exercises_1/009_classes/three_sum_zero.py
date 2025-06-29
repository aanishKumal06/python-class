class ThreeSumZero:
    def __init__(self):
        # Direct list of numbers
        self.nums = [-1, 0, 1, 2, -1, -4]

    def find_triplets(self):
        nums = sorted(self.nums)
        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        if triplet not in result:
                            result.append(triplet)
        return result


finder = ThreeSumZero()
triplets = finder.find_triplets()

if triplets:
    print("Triplets that sum to zero:")
    for t in triplets:
        print(t)
else:
    print("No triplets found.")
