def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    ans = None

    while l <= r:
        mid = l + (r - l) // 2

        if target == nums[mid]:
            ans = mid

        elif target < nums[mid]:
            r = mid - 1

        elif target > nums[mid]:
            l = mid + 1

    return ans


def find_first(nums, target):
    l, r = 0, len(nums) - 1
    ans = None

    while l <= r:
        mid = l + (r - l) // 2

        if target == nums[mid]:
            ans = mid
            r = mid - 1

        elif target < nums[mid]:
            r = mid - 1

        elif target > nums[mid]:
            l = mid + 1

    return ans


def lower_bound(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if target <= nums[mid]:
            r = mid - 1

        elif target > nums[mid]:
            l = mid + 1

    return l


def find_last(nums, target):
    l, r = 0, len(nums) - 1
    ans = None

    while l <= r:
        mid = l + (r - l) // 2

        if target == nums[mid]:
            ans = mid
            l = mid + 1

        elif target < nums[mid]:
            r = mid - 1

        elif target > nums[mid]:
            l = mid + 1

    return ans


def upper_bound(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if target < nums[mid]:
            r = mid - 1

        elif target >= nums[mid]:
            l = mid + 1

    return l
