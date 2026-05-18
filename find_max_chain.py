import sys

def radix_sort_by_length(words):
    if not words:
        return words

    max_len_val = max(len(word) for word in words)
    exp = 1
    while max_len_val // exp > 0:
        buckets = [[] for _ in range(50)]

        for word in words:
            digit = (len(word) // exp) % 10
            buckets[digit].append(word)

        words = []
        for bucket in buckets:
            words.extend(bucket)
        exp *= 10
        
    return words

def find_max_chain(words):
    if not words:
        return 0
    words = radix_sort_by_length(words)
    dp = {}
    ans = 0
    
    for word in words:
        current_best = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in dp:
                current_best = max(current_best, dp[prev] + 1)
        
        dp[word] = current_best
        if current_best > ans:
            ans = current_best
    return ans

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    words = input_data[1:n+1]

    result = find_max_chain(words)
    sys.stdout.write(str(result) + '\n')
if __name__ == "__main__":
    solve()