"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def find_unique_nums(numbers, col):
    res = set()
    for row in numbers:
        number = row[col]
        res.add(number)
    return res

def find_telemarketers(texts, calls):
    text_senders = find_unique_nums(texts, 0)
    text_receivers = find_unique_nums(texts, 1)
    call_senders = find_unique_nums(calls, 0)
    call_receivers = find_unique_nums(calls, 1)

    candidates =  call_senders-call_receivers-text_senders-text_receivers

    return sorted(candidates)

def run():
    result = find_telemarketers(texts, calls)
    print(f"These numbers could be telemarketers:",*result,sep="\n")

run()


"""
Assume texts has m rows, and calls has n rows.

Time Complexity: O(n^2+m^2)
Space Complexity: O(n+m)
"""
