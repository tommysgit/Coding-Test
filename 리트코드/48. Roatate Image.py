class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        sample = []
        for pair in zip(*matrix):
            pair = list(pair)
            pair.reverse()
            sample.append(pair)
        for i in range(len(sample)):
            for j in range(len(sample)):
                matrix[i][j] = sample[i][j]