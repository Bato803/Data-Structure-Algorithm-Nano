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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def isFromBangalore(number):
    """
    Check if a phone number comes from Bangalore.
    """
    return number.startswith("(080)")

def getAreaCodeOrPrefix(number):
    """
    Give a number, get either its prefix or area code.
    Assume the input number is not from telemarketers.
    """
    if number.startswith("("):
        pre, _ = number.split(")")
        return pre[1:]
    else:
        return number[0:4]

def partA_B(data):
    partA_res = set()
    from_Bangalore, to_Bangalore = 0., 0.
    for row in data:
        if isFromBangalore(row[0]):
            from_Bangalore += 1
            if row[1].startswith("(080)"):
                to_Bangalore += 1

            if not row[1].startswith("140"):
                partA_res.add(getAreaCodeOrPrefix(row[1]))
    return sorted(partA_res), 100*(to_Bangalore/from_Bangalore)

def run():
    partA_result, partB_result = partA_B(calls)
    print(f"The numbers called by people in Bangalore have codes:",*partA_result,sep="\n")
    print(f"{partB_result:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

run()

"""
Assume texts has m rows, and calls has n rows.

PartA:
Time Complexity: O(nlogn)
Space Complexity: O(n)

PartB:
Time Complexity: O(n)
Space Complexity: O(1)
"""
