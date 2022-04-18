from pathlib import Path
import _common_functions as cf

def name_score(name, position):
  return (sum([ord(char)-64 for char in name])) * position

def main():
  current_working_file = str(Path(__file__).parent.resolve())
  with open(current_working_file + "/22_names.txt", "r+") as file:
    content = file.read()
    sorted_content = [elt for elt in content.split('","')]
    sorted_content.sort()
    total = sum([name_score(sorted_content[i], i+1) for i in range(len(sorted_content))])

  return total

print(cf.average_running_time(100, main))
# Average running time of main() for 100 tests:
# 0.05832753419876099 seconds