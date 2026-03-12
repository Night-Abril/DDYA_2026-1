#Codigo trabajado en Hacker Rank: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem?isFullScreen=true
q = int(input())

stack1 = []
stack2 = []

for _ in range(q):

    query = list(map(int, input().split()))

    if query[0] == 1:

        stack1.append(query[1])

    elif query[0] == 2:

        if not stack2:
            while stack1:
                stack2.append(stack1.pop())

        stack2.pop()

    elif query[0] == 3:

        if not stack2:
            while stack1:
                stack2.append(stack1.pop())

        print(stack2[-1])