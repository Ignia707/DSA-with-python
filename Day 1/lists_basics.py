def main():
  natural = [i for i in range(1,10)]
  print(f"natural nums: {natural}")

  natural.insert(5, 15)
  print(f"after inserting 15: {natural}")

  natural.pop()
  natural.pop(0)
  print(f"after removing first and last: {natural}")

  print(f"Sliced to get every 2nd element: {natural[2:9:2]}")

main()