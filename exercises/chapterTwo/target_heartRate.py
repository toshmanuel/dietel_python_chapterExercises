users_age = int(input('enter age: '))
exerciseRate = int(input('enter exercise rate in percentage: '))
maximum_heart_rate = 220 - users_age
exerciseRate = exerciseRate / 100
target_heartRate = maximum_heart_rate * exerciseRate

print('target heart rate: ', target_heartRate)
