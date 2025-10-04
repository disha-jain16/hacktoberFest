import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(frequencies):
    # Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Generate Huffman codes by traversing the tree
    def generate_codes(node, prefix, codes):
        if node is not None:
            if node.char is not None:
                codes[node.char] = prefix
            generate_codes(node.left, prefix + "0", codes)
            generate_codes(node.right, prefix + "1", codes)

    root = heap[0]
    codes = {}
    generate_codes(root, "", codes)

    return codes

# Example usage:
frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
codes = huffman_coding(frequencies)
print("Huffman Codes:", codes)
