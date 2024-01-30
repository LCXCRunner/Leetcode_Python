class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        result : int = int(tokens[0])
        operators : list[str] = ["+", "-", "*", "/"]
        index : int = 0
        copy : list = tokens.copy()

        while len(copy) > 1:
            if copy[index] in operators:
                match copy[index]:
                    case "+":
                        result = int(copy[index - 2]) + int(copy[index - 1])
                        copy[index] = result
                        del copy[index - 1]
                        del copy[index - 2]
                    case "-":
                        result = int(copy[index - 2]) - int(copy[index - 1])
                        copy[index] = result
                        del copy[index - 1]
                        del copy[index - 2]
                    case "*":
                        result = int(copy[index - 2]) * int(copy[index - 1])
                        copy[index] = result
                        del copy[index - 1]
                        del copy[index - 2]
                    case "/":
                        result = int(int(copy[index - 2]) / int(copy[index - 1]))
                        copy[index] = result
                        del copy[index - 1]
                        del copy[index - 2]
                index -= 1
            else:
                index += 1
        return result

solution : Solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"]))#9
print(solution.evalRPN(["4","13","5","/","+"]))#6
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))#22
print(solution.evalRPN(["18"]))#18