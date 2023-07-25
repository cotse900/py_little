def solution(N):
    binary_val = bin(N)[2:]
    max_gap_len = gap_len = 0
    count = False

    for d in binary_val:
        if d == '1':
            if count:
                max_gap_len = max(max_gap_len, gap_len)
                gap_len = 0
            count = True
        elif count:
            gap_len += 1
            
    return max_gap_len
