def solution(board, moves):
    result=[]
    count=0
    for i in range(len(moves)):
        for j in range(len(board[0])):
            print(board[j][moves[i]-1])
            if board[j][moves[i]-1] == 0:
                continue
            else:
                if len(result)==0:
                    result.append(board[j][moves[i]-1])
                else:
                    if result[-1] == board[j][moves[i]-1]:
                        result.pop()
                        count+=2
                    else:
                        result.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break
            print(i,j)
    return count

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))