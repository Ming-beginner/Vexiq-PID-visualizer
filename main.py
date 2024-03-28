import matplotlib.pyplot as plt


def read_input():
  file_url = open("data/file.txt", "r").read()
  angle = []
  time = []
  input_file = open(file_url, "r")
  for line in input_file:
    a, t = map(float, line.split())
    angle.append(a)
    time.append(t)

  return [angle, time]

def main():
  angle, time = read_input()
  plt.plot(time, angle)
  plt.yticks([0, 45, 90])
  plt.xlabel('time')
  plt.ylabel('angle')
  plt.show()
  pass

if __name__ == '__main__': 
  main()