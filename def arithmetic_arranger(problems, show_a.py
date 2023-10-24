def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_lines = []
    bottom_lines = []
    dashes = []
    answers = []

    for problem in problems:
        num1, operator, num2 = problem.split()
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        width = max(len(num1), len(num2)) + 2
        top_lines.append(num1.rjust(width))
        bottom_lines.append(operator + num2.rjust(width - 1))
        dashes.append("-" * width)

        if show_answers:
            result = str(eval(problem))
            answers.append(result.rjust(width))

    arranged_problems = []
    arranged_problems.append('    '.join(top_lines))
    arranged_problems.append('    '.join(bottom_lines))
    arranged_problems.append('    '.join(dashes))

    if show_answers:
        arranged_problems.append('    '.join(answers))
    
    return '\n'.join(arranged_problems)


# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49",]))
#print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
