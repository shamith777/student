import sys
#Check if correct number of argurment
if len(sys.argv)i=3:
  print("Usuage: python student.py <name>")
  sys.exit(1)
#sys.argy(0) is always the programname
  script_name = sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]

print("Script name:",script_name)
print("Student Name:",name)
print("Roll No.:",rollno)
