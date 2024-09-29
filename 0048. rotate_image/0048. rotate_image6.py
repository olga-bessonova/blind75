def rotate(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right  # since it's a square matrix

            # Store the top left value temporarily
            top_left = matrix[top][left + i]

            # Move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # Assign top left value to top right
            matrix[top + i][right] = top_left

        # Move the boundaries inward
        left += 1
        right -= 1

    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))
