"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def calculate_time(data):

    Hash = {}
    for row in data:
        Hash[row[0]] = Hash.get(row[0], 0) + int(row[3])
        Hash[row[1]] = Hash.get(row[1], 0) + int(row[3])

    return Hash

def find_max(hash):
    cur_max = float("-inf")
    max_key = None
    for key in hash:
        if hash[key] > cur_max:
            cur_max = hash[key]
            max_key = key
    return cur_max, max_key

def run():
    hash = calculate_time(calls)
    res, key = find_max(hash)
    print(f"{key} spent the longest time, {res} seconds, on the phone during September 2016.")
    return

run()

"""
Assume texts has m rows, and calls has n rows.

Time Complexity: O(n)
Space Complexity: O(n)
"""
