'''
Instead of changing existing code in place, please comment out the current code and add a new comment below explaining shortcomings in the previous code and your new approach. 
This is important because we can't see the history of tested solutions in the IDE. Having meaningful iterations will provide a signal to recruiters of your ability to improve existing code/logic.

# Original code
x = ['www.a.com', 'www.b.com', 'www.c.com']
y = []
for i in x:
y.append(i.split('.')[1])
print(y)

# Output ['a','b','c']

'''


# Shortcomings in the original code:
# - The code assumes that all URLs have at least two parts separated by dots, which may not be the case for all URLs.
# - Hardcoding the index [1] assumes that the domain is always the second part, which may not hold true for all cases.

# Revised code with comments:
x = ['www.a.com', 'www.b.com', 'www.c.com']
y = []

# Revised approach:
# Instead of hardcoding the index [1], we use the last part of the split result to ensure flexibility.
for url in x:
    # Splitting the URL by dots and taking the last part as the domain
    domain = url.split('.')[-2]
    y.append(domain)

print(y)

# Output ['a','b','c']