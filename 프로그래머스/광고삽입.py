def time_plus(t1, t2):
    s = (t1[2] + t2[2]) % 60
    m = (t1[1] + t2[1] + ((t1[2] + t2[2]) // 60)) % 60
    h = t1[0] + t2[0] + ((t1[1] + t2[1] + ((t1[2] + t2[2]) // 60))) // 60

    return [h, m, s]


def time_minus(t1, t2):
    if t1[2] >= t2[2]:
        s = t1[2] - t2[2]
    else:
        if t1[1] > 0:
            t1[1] -= 1
        else:
            t1[0] -= 1
            t1[1] = 59
        s = (t1[2] + 60) - t2[2]
    if t1[1] >= t2[1]:
        m = t1[1] - t2[1]
    else:
        t1[0] -= 1
        m = (t1[1] + 60) - t2[1]
    h = t1[0] - t2[0]

    return [h, m, s]


def solution(play_time, adv_time, logs):
    answer = ''

    play_time = list(map(int, play_time.split(":")))
    adv_time = list(map(int, adv_time.split(":")))

    logs = [[list(map(int, t.split(":"))) for t in list(l.split("-"))] for l in logs]
    logs.sort()

    if play_time == adv_time:
        answer = "00:00:00"
        return answer

    logs_time = []
    for l in logs:
        logs_time.append(time_minus(l[1], l[0]))

    max_time = [0, 0, 0]
    max_start = [0, 0, 0]
    time = [0, 0, 0]
    idx = 0
    while (idx < len(logs)):
        finish = time_plus(adv_time, logs[idx][0])
        if finish > play_time:
            break
        for i in range(len(logs) - idx):
            if logs[idx + i][0] >= finish:
                break
            if logs[idx + i][1] <= finish:
                time = time_plus(time, logs_time[idx + i])  # time_plus(time, time_minus(logs[idx+i][1], logs[idx+i][0]))
            else:
                time = time_plus(time, time_minus(finish, logs[idx + i][0]))

        if max_time < time:
            max_time = time
            max_start = logs[idx][0]
        time = [0, 0, 0]
        idx += 1

    answer = str(max_start[0]).zfill(2) + ":" + str(max_start[1]).zfill(2) + ":" + str(max_start[2]).zfill(2)

    return answer


logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution("02:03:55", "00:14:15", logs))
