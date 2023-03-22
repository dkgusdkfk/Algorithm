n, m = map(int, input().split())
books = sorted(list(map(int, input().split())))

minus = []
plus = []
for book in books:
    if book < 0:
            minus.append(book)
                else:
                        plus.insert(0, book)

                        result = 0
                        def solution(arr):
                            global result
                                for i in range(0, len(arr), m):
                                        result += abs(arr[i]) * 2
                                                if i + m >= len(arr):
                                                            return

                                                            solution(minus)
                                                            solution(plus)

                                                            if minus == []:
                                                                result -= plus[0]
                                                                elif plus == []:
                                                                    result += minus[0]
                                                                    else:
                                                                        result -= max(plus[0], abs(minus[0]))

                                                                        print(result)