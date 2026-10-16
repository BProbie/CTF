# 绕过

## read覆盖

```c
read(0,s[40],sizeof(s)) // 会覆盖s末尾的\x00
```

```c
fgets(s[40],sizeof(s),stdin) // 不会覆盖s末尾的\x00 -> fgets读取输入后会追加\x00 -> 边界清晰
```



# Heap

## 前置

### 教程

```html
https://blog.csdn.net/hnytgl/article/details/161080490
```

### Chunk

```shell

```

### Bin

- tcache
- fastbin
- small bin
- large bin
- unsorted bin



## 堆覆盖

### 教程

```html
https://www.cnblogs.com/37blog/p/17808141.html
```



## UAF

### 教程

```html
https://www.cnblogs.com/37blog/p/17808141.html
```

