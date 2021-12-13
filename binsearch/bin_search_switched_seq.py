class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Поиск минимума при возможном развороте массива в рандомной точке.
        :param nums: - массив чисел
        :return: - наименьший элемент массива
        """
        # задаём границы поиска
        l, r = 0, len(nums) - 1
        #проверка наличия элементов в массиве
        if len(nums) == 0:
            return -1
        #если массив состоит из одного элемента
        if l == r:
            return nums[l]
        #если список отсортирован
        if nums[l] < nums[r]:
            return nums[l]
        #бинпоиск
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            if nums[m] < nums[m - 1]:
                return nums[m]
            if nums[m] > nums[0]:
                l = m + 1
            else:
                r = m - 1