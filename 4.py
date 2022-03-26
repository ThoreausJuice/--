#!/usr/bin/env python3

# 右手法则小老鼠（带记忆）

# 构建5×5不通迷宫
import numpy as np

# 迷宫总房间数
n = 25

# 构建R矩阵
R = np.ones((n,n), np.int32)
R *= -1

# 全通设定
for i in range(0,n):
	if i-5 >= 0:
		R[i,i-5] = 0
		R[i-5,i] = 0
	if i+5 <= 24:
		R[i,i+5] = 0
		R[i+5,i] = 0
	if (i-1)%5 != 4:
		R[i,i-1] = 0
		R[i-1,i] = 0
	if (i+1)%5 != 0:
		R[i,i+1] = 0
		R[i+1,i] = 0

# 关闭终点设定
R[23,24] = -1
R[19,24] = -1
R[24,24] = 100

# 路径记录
Way = []

# 出入口设定
Export = 24
Entrance = 0

# 右手法则设定
def The_right_hand_rule(last, now):
	if now != Entrance:
		if now-last == 5:
			if now-1 >= 0 and R[now,now-1] != -1 and Way.count(now-1) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now-1)
			elif now+5 <= 24 and R[now,now+5] != -1 and Way.count(now+5) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now+5)
			elif now+1 <= 24 and R[now,now+1] != -1 and Way.count(now+1) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now+1)
			else:
				Way.append(now)
				return The_right_hand_rule(now, last)
		if now-last == 1:
			if now+5 <= 24 and R[now,now+5] != -1 and Way.count(now+5) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now+5)
			elif now+1 <= 24 and R[now,now+1] != -1 and Way.count(now+1) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now+1)
			elif now-5 >= 0 and R[now,now-5] != -1 and Way.count(now-5) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now-5)
			else:
				Way.append(now)
				return The_right_hand_rule(now, last)
		if now-last == -5:
			if now+1 <= 24 and R[now,now+1] != -1 and Way.count(now+1) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now+1)
			elif now-5 >= 0 and R[now,now-5] != -1 and Way.count(now-5) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now-5)
			elif now-1 >= 0 and R[now,now-1] != -1 and Way.count(now-1) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now-1)
			else:
				Way.append(now)
				return The_right_hand_rule(now, last)
		if now-last == -1:
			if now-5 >= 0 and R[now,now-5] != -1 and Way.count(now-5) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now-5)
			elif now-1 >= 0 and R[now,now-1] != -1 and Way.count(now-1) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now-1)
			elif now+5 <= 24 and R[now,now+5] != -1 and Way.count(now+5) == 0:
				Way.append(now)
				return The_right_hand_rule(now, now+5)
			else:
				Way.append(now)
				return The_right_hand_rule(now, last)
	elif now == Export:
		Way.append(now)
		return 
	else:
		Way.append(now)
		return The_right_hand_rule(now, last)

Way.append(Entrance)
The_right_hand_rule(Entrance, 5)
print(Way)

if Way[0] == Way[len(Way)-1]:
	print("此迷宫将回归起点")
else:
	print("该迷宫能够走向终点")