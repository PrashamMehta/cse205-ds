class Solution:

    def heapify(self, arr, N, i):

        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
    
        if l < N and arr[largest] < arr[l]:
            largest = l
    
        if r < N and arr[largest] < arr[r]:
            largest = r
    
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
    
            self.heapify(arr, N, largest)

    def insert(self, array, newNum):
        size = len(array)
        if size == 0:
            array.append(newNum)
        else:
            array.append(newNum)
            for i in range((size//2)+1, -1, -1):
                self.heapify(array, size, i)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse = True)
        return nums[k - 1]