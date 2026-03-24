def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1 
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in arr:
            index = (x // exp) % 10
            buckets[index].append(x)
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        exp *= 10
    return arr

def check(stalls, k, dist):
    cnt = 1  
    prev = stalls[0] 
    for i in range(1, len(stalls)):
        if stalls[i] - prev >= dist:
            prev = stalls[i] 
            cnt += 1
    return cnt >= k

def aggressive_cows(stalls, k):
    stalls = radix_sort(stalls)
    lo = 1
    hi = stalls[-1] - stalls[0] 
    print(f"[Крайні значення]:")
    print(f" - Найменша відстань (lo): {lo}")
    print(f" - Найбільша відстань (hi): {hi}")

    res = 0 
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if check(stalls, k, mid):
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res

def read_from_file(filename):
    try:
        with open(filename, 'r') as f:
            line1 = f.readline().split()
            if not line1: return None
            n, c = map(int, line1)
            content = f.read().split()
            stalls = [int(x) for x in content]
            
            return n, c, stalls
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return None
    