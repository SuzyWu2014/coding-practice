#1 判断奇偶

只需判断最低位是否为1.

```python
if n & 1 == 1:
    return True
else:
    return False
```

#2 判断第N位是否为1

`1 << 3` 将1向左移动3位，即高位为0，低位为0; => `001000`, 与原数进行与运算后，若最终结果为0， 则第N位为0

```python
if x & (1 << n) == 0:
    return False
else:
    return True
```

#3 将第N位设置为1

```python
 y = x | (1 << n)
```

#4 将第N位设置为0

```python
y = x & ~(1 << n)
```

#5 反转第N位

```python
y = x ^ (1 << n)
```

#6 将最右边的1置0

```python
y = x & (x - 1)
```

#7 拨离最右边的1 => 找到最右边的一个1并将其他位置0
-x 即X取反后加1
```python
y = x & (-x)
```

#8 将右边第一个1后的位全置1
x - 1 会将最后一位1变成0，其后的0变成1

```python
y = x | x - 1
```

#9 拨离最右边的第一个0 => 找到最右的0,将它置1并将其他位置0
`x + 1` 最右边的0 变为1， 且之后的低位为0
```python
y = (x + 1) & (~x)
```

#10 将最右边0位置1
```
y = x | (x + 1)
```
