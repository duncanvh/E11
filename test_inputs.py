import sys

print(sys.argv)

if len(sys.argv) < 2:
  print('script requires runtime int as an input')
  exit()
else:
  runtime = int(sys.argv[1])
  
count = 0
while count < runtime:
  print(count)
  count += 1 
  time.sleep(1)
