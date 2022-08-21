message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)    # Output in 1 row.
# For better look:
import pprint
pprint.pprint(count)    # Output one key and value in each row.
print((message_str := pprint.pformat(count)))   # Stored in string instead of output to screen
