import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
gradebook_raw = pd.read_csv('gradebookhere.csv')
gradebook = gradebook_raw.fillna(0)

# Return the column name with 'keyward'.
def findtestname(keyward, column):
    for str in column:
        if keyward in str:
            return str
    else:
        print(f"Cannot find {keyward} in {column}")
        return None

webassigngrade = findtestname('WebAssignHomework Final Score', gradebook.columns)
quizgrade = findtestname('WeeklyQuizzes Final Score', gradebook.columns)
test1grade = findtestname('Test1', gradebook.columns)
test2grade = findtestname('Test2', gradebook.columns)
test3grade = findtestname('Test3', gradebook.columns)
finalgrade = findtestname('Final Exam', gradebook.columns)

# testdf = gradebook[[test1grade, test2grade, test3grade]]


# Convert necessary columns to numeric

gradebook[webassigngrade] = pd.to_numeric(gradebook[webassigngrade], errors='coerce')
gradebook[quizgrade] = pd.to_numeric(gradebook[quizgrade], errors='coerce')
gradebook[finalgrade] = pd.to_numeric(gradebook[finalgrade], errors='coerce')


# Calculate the course grade
# WebAssign Homework, Weekly Quizzes and attendance are out of 100 points, test 1 to test 3 and final exam are out of 50 points.
# WebAssign Homework: 15%, Weekly Quizzes: 17%, Lowest test 13%, Mediem test 16%, Highest test 19%, Final Exam: 20%
coursegrade = 'Course Grade'

gradebook[coursegrade] = (
	0.15 * 100/100 * gradebook[webassigngrade] +
	0.17 * 100/100 * gradebook[quizgrade] +
	0.2 * 100/50 * gradebook[finalgrade] +
	0.13 * 100/50 * testdf.apply(lambda row: sorted(row)[0], axis=1) +
	0.16 * 100/50 * testdf.apply(lambda row: sorted(row)[1], axis=1) +
	0.19 * 100/50 * testdf.apply(lambda row: sorted(row)[2], axis=1)
)

gradebook[['Student', coursegrade, webassigngrade, quizgrade, test1grade, test2grade, test3grade, finalgrade]].sort_values(by=coursegrade, ascending=False)

TestName_searching_keywawrd = coursegrade

testname = findtestname(TestName_searching_keywawrd, gradebook.columns)
testgrade = pd.to_numeric(gradebook[testname], errors='coerce')
testgrade.hist(bins=round(100/5), range = (0,100))
plt.title(f'{testname} histogram')
