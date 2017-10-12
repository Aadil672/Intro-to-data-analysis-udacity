import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('/datasets/ud170/udacity-students/enrollments.csv')
daily_engagement = read_csv('/datasets/ud170/udacity-students/daily_engagement.csv')
project_submissions = read_csv('/datasets/ud170/udacity-students/project_submissions.csv')
    
### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

enrollment_num_rows = len(enrollments)
 # Replace this with your code
unique_enrollement=set() 
for enrollement in enrollments:
    unique_enrollement.add(enrollement['account_key'])
enrollment_num_unique_students = len(unique_enrollement)
print(enrollment_num_unique_students)
engagement_num_rows = len(daily_engagement)
unique_engagement=set() 
for engagement in daily_engagement:
    unique_engagement.add(engagement['acct'])
engagement_num_unique_students = len(unique_engagement)  
print(engagement_num_unique_students)
submission_num_rows = len(project_submissions)     
unique_submission=set() 
for submission in project_submissions:
    unique_submission.add(submission['account_key'])
submission_num_unique_students = len(unique_submission)  
print(submission_num_unique_students)
