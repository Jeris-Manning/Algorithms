#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    classic = [["rock"], ["paper"], ["scissors"]]
    if n == 0:
        return [[]]
    if n == 1:
        return [["rock"], ["paper"], ["scissors"]]

    move_list = []

    for tools in (rock_paper_scissors(n-1)):
       move_list += [tools + classic[0]]
       move_list += [tools + classic[1]]
       move_list += [tools + classic[2]]

    return move_list

print(rock_paper_scissors(4))




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')



