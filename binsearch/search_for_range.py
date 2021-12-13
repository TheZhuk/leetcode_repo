class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Функция возвращает массив с индексами начала и конца последовательности заданного числа.
        Если число не найдено в массиве, возвращает [-1, -1]

        Example:
        1.
        nums = [1, 3, 3, 5, 5, 5, 7]
        target = 5
        output: [3, 5]

        2.
        nums = [1, 3, 3, 5, 5, 5, 7]
        target = 6
        output: [-1, -1]

        :param nums: - массив целых чисел
        :param target: - число, последовательность которого мы ищем
        :return: - массив индексов начала и конца
        """
        result = [-1, -1]
        if len(nums) == 0:
            return result

        def binsearch_left(nums: list(int), target: int) -> int:
            l, r = 0, len(nums) - 1
            res = -1

            while l <= r:
                m = (r + l) // 2
                if nums[m] == target:
                    res = m
                    r = m - 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return res

        def binsearch_right(nums: list(int), target: int) -> int:
            l, r = 0, len(nums) - 1
            res = -1

            while l <= r:
                m = (r + l) // 2
                if nums[m] == target:
                    res = m
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return res

        result[0] = binsearch_left(nums, target)
        result[1] = binsearch_right(nums, target)
        return result