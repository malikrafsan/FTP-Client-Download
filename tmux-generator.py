import sys

iteration = int(sys.argv[1])

with open("script.sh", "w") as file:
  str = "tmux new-session -d bash\n"
  
  for i in range(iteration-1):
    str += "tmux split-window -h bash\n"

  for i in range(iteration):
    str += f"tmux send -t 0:0.{i} 'python3 main.py {iteration}; exit' C-m\n"

  str += "tmux -2 attach-session -d\n"
  
  file.write(str)
