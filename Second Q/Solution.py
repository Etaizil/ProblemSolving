def removeAnElement(nums: list[int], val: int) -> int:
        retCounter = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                retCounter += 1
                i += 1
            else:
                nums.pop(i)
        return retCounter