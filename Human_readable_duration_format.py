# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    last_result: str = ""
    class_dict = {"year": 31536000, "day": 86400, "hour": 3600, "minute": 60, "second": 1}
    variables = ["year", "day", "hour", "minute", "second"]
    if seconds == 0:
        return "now"

    def solution(types):
        if seconds >= class_dict[types]:
            x = seconds // class_dict[types]
            left_overs = seconds % class_dict[types]
            if x > 1:
                result = f"{x} {types}s"
                return result, left_overs
            if x == 1:
                result = f"{x} {types}"
                return result, left_overs

    for items in variables:
        if solution(items) is None:
            continue
        else:
            last_result += solution(items)[0] + " "
            seconds = solution(items)[1]

    a = last_result.split()
    if len(a) > 2 and ("second" or "seconds" in a):
        a[len(a) - 3] += " and"
        for i in range(len(a) - 5, 0, -2):
            a[i] += ","
    last_result = " ".join(a)
    return last_result
