def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    if not nums1 and not nums2:
        return 0
    n = len(nums1)
    m = len(nums2)
    i = 0
    j = 0
    m1 = 0
    m2 = 0
    for count in range(0, (n + m) // 2 + 1):
        m2 = m1
        if i < n and j < m:
            if nums1[i] > nums2[j]:
                m1 = nums2[j]
                j += 1
            else:
                m1 = nums1[i]
                i += 1
        elif i < n:
            m1 = nums1[i]
            i += 1
        else:
            m1 = nums2[j]
            j += 1
    if (n + m) % 2 == 1:
        return float(m1)
    else:
        ans = float(m1) + float(m2)
        return ans / 2.0


"""
    newList = sorted(list(map(int, nums1 + nums2)))
    start = 0
    end = len(newList) - 1
    mid = start + (end - start) // 2
    return (
        newList[mid] if len(newList) % 2 != 0 else (newList[mid] + newList[mid + 1]) / 2
    )
"""
