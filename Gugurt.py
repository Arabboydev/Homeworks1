a = int(input())
count = 0
for i in str(a):
  match i:
    case '0':
      count += 6
    case '1':
      count += 2
    case '2':
      count += 5
    case '3':
      count += 5
    case '4':
      count += 4
    case '5':
      count += 5
    case '6':
      count += 6
    case '7':
      count += 3
    case '8':
      count += 7
    case '9':
      count += 6
print(count)