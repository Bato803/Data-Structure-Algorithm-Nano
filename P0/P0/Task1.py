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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
def count_unique_numbers(data, Hash):

    if Hash is None:
        Hash = {}

    cnt = 0
    for row in data:
        if row[0] not in Hash:
            Hash[row[0]] = 0
            cnt += 1
        if row[1] not in Hash:
            Hash[row[1]] = 0
            cnt += 1

    return cnt, Hash

def run():
    text_cnt, hash = count_unique_numbers(texts, None)
    call_cnt, _ = count_unique_numbers(calls, hash)
    print(f"There are {text_cnt+call_cnt} different telephone numbers in the records.")

run()

"""
Assume texts has m rows, and calls has n rows.

Time Complexity: O(m+n)
Space Complexity: O(m+n)
"""
