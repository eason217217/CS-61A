def convert(s: str, numRows: int) -> str:
    ans = [[] for _ in range(numRows)]
    final_ans = ''
    pattern = 2 * numRows - 2
    for i in range(len(s)):
        if i % pattern < numRows:
            ans[i % pattern].append(s[i])
        else:
            ans[numRows - 1 - (i % pattern - numRows + 1)].append(s[i])
    for i in ans:
        for j in i:
            final_ans += j
    return final_ans

ref = convert( "PAYPALISHIRING", 3)
print(ref)
