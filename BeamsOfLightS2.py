def binary_search_manual(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        start, end = arr[mid]

        if start <= target <= end:
            return True  # Found the target!
        elif target < start:
            high = mid - 1  # Target is in the left half
        else:
            low = mid + 1  # Target is in the right half

    return False  # Target does not exist


number_of_parking = int(input())
number_of_lights = int(input())
number_of_questions = int(input())
intervals = []
for i in range(number_of_lights):
    user_input = input()
    light_radius = list(map(int, user_input.split()))
    start = max(1, light_radius[0] - light_radius[1])
    end = min(number_of_parking, light_radius[0] + light_radius[1])
    intervals.append([start, end])

intervals.sort()
merged = []
for start, end in intervals:
    if not merged or merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

for y in range(number_of_questions):
    poop = int(input())
    result = binary_search_manual(merged, poop)
    if result == True:
        print("Y")
    else:
        print("N")