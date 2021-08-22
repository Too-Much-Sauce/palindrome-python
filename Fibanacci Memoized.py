memo = {}

def fibonacci(num):
  result = None
  if num in memo:
    result = memo[num]
  elif num == 0 or num == 1:
    result = num
  else:
    result = fibonacci(num - 1) + fibonacci(num - 2)
    memo[num] = result
  return result


def main():
  number = int(input("Enter a number to calculate the Fibonacci number: "))
  results = fibonacci(number)
  print(results)
 

main()
