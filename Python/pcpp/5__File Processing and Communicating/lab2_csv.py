import csv

l_results = [] 


with open('.\\5__File Processing and Communicating\\exam_results.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        l_results.append(row)

exam_results = []

for matiere in ['Maths', 'Physics' , 'Biology']:

    min_matiere = min(p['Score'] for p in l_results if p['Exam Name'] == matiere)
    max_matiere = max(p['Score'] for p in l_results if p['Exam Name'] == matiere)
    fail_matiere = len([p for p in l_results if p['Exam Name'] == matiere and p['Grade'] == 'Fail'])
    nb_passed_exams = len([p for p in l_results if p['Exam Name'] == matiere and p['Grade'] == 'Pass'])
    nb_candidates = len(set([p['Candidate ID'] for p in l_results if p['Exam Name'] == matiere]))

    exam_results.append([matiere,min_matiere,str(max_matiere),str(fail_matiere), str(nb_passed_exams), str(nb_candidates)])

  
with open('exam_results.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONE)
    writer.writerow(['Exam Name','Number of Candidates','Number of Passed Exams','Number of Failed Exams','Best Score','Worst Score'])
    
    for result in exam_results:
        print(','.join(result))
        writer.writerow(result)



''' 
Exam Name,Candidate ID,Score,Grade
Maths,C000007,44,Fail
Physics,C000001,50,Fail
Biology,C000001,30,Fail
Maths,C000005,50,Fail
Biology,C000002,45,Fail
Physics,C000006,66,Fail
Maths,C000009,74,Pass
Maths,C000010,74,Pass
Biology,C000003,70,Pass
Maths,C000012,55,Fail
Maths,C000013,33,Fail
Biology,C000004,88,Pass
Maths,C000014,90,Pass
Maths,C000005,82,Pass
Biology,C000011,23,Fail
Maths,C000008,44,Fail
Maths,C000008,54,Fail
Physics,C000003,54,Fail




Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score
Maths,8,4,6,90,33
Physics,3,0,3,66,50
Biology,5,2,3,88,23

'''