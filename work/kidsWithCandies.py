class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candies = max(candies)
        for count in candies:
            if count + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
