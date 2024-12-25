import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, -1, -1):
    print(f"{x // 3600:02}:{(x // 60) % 60:02}:{x % 60:02}.")
    time.sleep(1)

print("TIME's UP!")
