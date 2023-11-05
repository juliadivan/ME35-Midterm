import requests
cv2_image = cv2.cvtColor(np.array(cam.raw_image), cv2.COLOR_RGB2BGR)
b,g,r = cv2.split(cv2_image)
array = g
#cam.show(array)  # shows any cv2 image in the same spot on the webpage (third image)
array = g
#cam.show(array)  # shows any cv2 image in the same spot on the webpage (third image)
print('the code is running')

array_x = len(array[0])
array_y = len(array)
print(array_x,array_y)
cropped_image = g[100:180, 100:200] #first is y direction, second is x
cam.show(cropped_image)

count_greater_than_50 = 0
count_smaller_than_or_equal_50 = 0

# Iterate through the 2D array
for row in cropped_image:
    for value in row:
        if value > 50:
            count_greater_than_50 += 1
        else:
            count_smaller_than_or_equal_50 += 1

print('count greater than 50: ', count_greater_than_50, 'count less than 50: ', count_smaller_than_or_equal_50)

color = ''

if(count_greater_than_50 > count_smaller_than_or_equal_50):
    color = 'green'
    print(color)
else:
    color = 'red'
    print(color)
