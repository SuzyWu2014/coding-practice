# 2d matrix 特性

+ 从左到右升序
+ 从上到下生序

[
   [1,   4,  7, 11, 15],
   [2,   5,  8, 12, 19],
   [3,   6,  9, 16, 22],
   [10, 13, 14, 17, 24],
   [18, 21, 23, 26, 30]
]


对于任意位置 `a[i][j]`,
`a[0~i][0~j-1]` 均小于`a[i][j]`
`a[i, row][j, col]` 均小于`a[i][j]`

二分法缩小范围：

从 a[0][col] 开始，比其大，则比较a[1][col], 第一行可排除，比其小，则比较a[0][col-1],最后一列可排除

