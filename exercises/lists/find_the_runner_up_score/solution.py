#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = sorted(dict.fromkeys(arr))
    print(arr[-2])
