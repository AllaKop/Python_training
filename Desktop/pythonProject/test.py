nums = [1,2,3,4,5]

n = len(nums)

left_products = [1] * n
right_products = [1] * n
result = [1] * n

print (n, left_products, right_products, result)

for i in range(1, n):
    left_products[i] = left_products[i - 1] * nums[i - 1]

print(left_products)
