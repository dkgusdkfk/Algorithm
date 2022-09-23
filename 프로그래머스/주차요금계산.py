from datetime import datetime
import math

def solution(fees, records):
    answer = []

    in_dict = {}
    total_dict = {}

    for record in records:
        time, number, stat = record.split()
        if stat == 'IN':
            in_dict[number] = time
        elif stat == 'OUT':
            t1 = datetime.strptime(in_dict[number], "%H:%M")
            t2 = datetime.strptime(time, "%H:%M")
            if number in total_dict:
                total_dict[number] += (t2-t1).seconds // 60
            else:
                total_dict[number] = (t2 - t1).seconds // 60
            del in_dict[number]

    for number, time in in_dict.items():
        t1 = datetime.strptime(time, "%H:%M")
        t2 = datetime.strptime('23:59', "%H:%M")
        if number in total_dict:
            total_dict[number] += (t2 - t1).seconds // 60
        else:
            total_dict[number] = (t2 - t1).seconds // 60

    for time in dict(sorted(total_dict.items())).values():
        if time > fees[0]:
            fee = math.ceil((time - fees[0]) / fees[2]) * fees[3] + fees[1]
        else :
            fee = fees[1]
        answer.append(fee)

    return answer

fees =[180, 5000, 10, 600]
records =["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))