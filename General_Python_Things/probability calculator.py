balls = ["blue","blue","red", "red", "green"]
no_of_balls = []
expected_balls = {"blue": 2, "red":1}
expected_no_of_balls = []
for key in expected_balls:
    no_of_balls.append(balls.count(key))

for key in expected_balls:
    expected_no_of_balls.append(expected_balls[key])

print(balls, no_of_balls, expected_balls)

if no_of_balls >= expected_no_of_balls:
    print(expected_no_of_balls)