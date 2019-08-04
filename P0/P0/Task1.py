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
def count_unique_numbers(data):
    Hash = {}
    cnt = 0
    for row in data:
        if row[0] not in Hash:
            Hash[row[0]] = 0
            cnt += 1
        if row[1] not in Hash:
            Hash[row[1]] = 0
            cnt += 1

    return cnt

def run():
    text_cnt = count_unique_numbers(texts)
    call_cnt = count_unique_numbers(calls)
    print(f"There are {text_cnt+call_cnt} different telephone numbers in the records.")

run()
