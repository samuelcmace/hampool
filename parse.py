import json
import re
import sys

# def parseQuestionHead(head):
#     print(head)
#
# def parseQuestionBody(body):
#     print(body)

try:
    inputFile = open(sys.argv[1], "r")
except:
    print("Error: Unable to read the specified input file.")

questions = re.split("~~", inputFile.read())
inputFile.seek(0)

print("Question #" + sys.argv[2])
print(questions[int(sys.argv[2]) - 1])
print("There are a total of " + str(len(questions)) + " in this question pool.")

# try:
#     outputFile = open(sys.argv[2], "x")
#     outputFile.write()
#     outputFile.close()
# except:
#     print("Error: Unable to create the specified output file.")

inputFile.close()
