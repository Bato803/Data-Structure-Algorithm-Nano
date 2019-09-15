import sys
from collections import Counter
import heapq

class Node(object):

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __le__(self, other):
        if other is None:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.freq<=other.freq
    
    def __gt__(self, other):
        if other is None:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.freq>other.freq


def make_heap(heap, freqs):

    for key in freqs:
        node = Node(key, freqs[key])
        heapq.heappush(heap, node)

def merge_nodes(heap):

    while(len(heap)>1):
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq+node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

def make_codes_helper(root, current_code, codes, reverse_mapping):
    
    if not root:
        return 
    
    if root.char is not None:
        codes[root.char] = current_code
        reverse_mapping[current_code] = root.char

    make_codes_helper(root.left, current_code+"0", codes, reverse_mapping)
    make_codes_helper(root.right, current_code+"1", codes, reverse_mapping)


def make_codes(heap, codes, reverse_mapping):
    root = heapq.heappop(heap)
    cur_code = ""
    make_codes_helper(root, cur_code, codes, reverse_mapping)

def get_encoded_text(data, codes):
    encoded_text = ""
    for character in data:
        encoded_text += codes[character]

    return encoded_text

def huffman_encoding(data):
    
    Frequency_table = Counter(data)
    Heap = []
    Codes = {}
    Reverse_mapping = {}

    make_heap(Heap, Frequency_table)

    merge_nodes(Heap)

    make_codes(Heap, Codes, Reverse_mapping)

    encoded_text = get_encoded_text(data, Codes)

    return encoded_text, Reverse_mapping
        

def huffman_decoding(data,reverse_mapping):
    
    bits = ""
    res = ""

    for bit in data:
        bits += bit
        if bits in reverse_mapping:
            character = reverse_mapping[bits]
            res += character
            bits = ""

    return res

def test(a_great_sentence):

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":

    tst1 = "The bird is the word"
    tst2 = "A rich comparison method may return the singleton NotImplemented if it does not implement the operation for a given pair of arguments. By convention, False and True are returned for a successful comparison. However, these methods can return any value, so if the comparison operator is used in a Boolean context (e.g., in the condition of an if statement), Python will call bool() on the value to determine if the result is true or false."
    tst3 = "Special read-only attributes: tb_frame points to the execution frame of the current level; tb_lineno gives the line number where the exception occurred; tb_lasti indicates the precise instruction. The line number and last instruction in the traceback may differ from the line number of its frame object if the exception occurred in a try statement with no matching except clause or with a finally clause."


    test(tst1)
    print(100*"=")
    test(tst2)
    print(100*"=")
    test(tst3)
    






















