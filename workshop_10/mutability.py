nums = [1, 2, 3]

nums[0] = 7

print(nums)


# mutability
# strings are immutable
text = "123"

# text[0] = "7"
text = f"7{text[1:]}"

print(text)