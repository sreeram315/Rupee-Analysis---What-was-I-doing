import re

string = '''1.986476 – 31 days
Feb 1.947907 – 28 days
Mar 1.993128 – 31 days
Apr 2.101425 – 30 days
May 2.012182 – 31 days
Jun 1.953999 – 30 days
Jul 1.874192 – 31 days
Aug 1.839630 – 31 days
Sep 1.835907 – 30 days
Oct 1.846257 – 31 days
Nov 1.838955 – 30 days
Dec 1.848063 – 31 days
'''

nums = re.findall(r"([-+]*\d+\.\d+|[-+]*\d+)", string)
for num in nums:
	if float(num) <= 31:
		nums.remove(num)
for i in range(len(nums)):
	nums[i] = float(nums[i])
print(sum(nums)/len(nums))