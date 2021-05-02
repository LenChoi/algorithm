def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] -= 1
    dnf = [v for v in d.items() if v > 0] # list comprehension
    answer = dnf[0]
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
solution(participant, completion)