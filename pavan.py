def solution(input_from_question):
    mid = len(input_from_question)//2
    if len(input_from_question) > 1:
        left = mid-1
        right = mid+1
        while left >= 0 and right < len(input_from_question):
            if input_from_question[left] == input_from_question[right]:
                left -= 1
                right += 1
            else:
                return input_from_question[left+1:right]
        return input_from_question[left+1:right]
    else:
        return input_from_question


print(solution("sa"))
