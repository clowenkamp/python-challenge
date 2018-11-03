import os
import csv

input_file = 'election_data.csv'
output_file = 'election_summary_1.txt'



csv_input_path = os.path.join('Resources', input_file)
txt_output_path = os.path.join('Resources', output_file)

candidates, total_candidates, candidate_perc, candidate_total, summaries = ([] for i in range(5))


with open(csv_input_path, mode='r', newline='') as poll_data:
    reader = csv.reader(poll_data, delimiter=',')

    next(reader)

    num_rows = 0

    for row in reader:
        total_candidates.append(row[2])
        num_rows += 1



sorted_candidates = sorted(total_candidates)

for i in range(num_rows):
    if sorted_candidates[i - 1] != sorted_candidates[i]:
        candidates.append(sorted_candidates[i])



print("\nElection Results")
print("-" * 40)
print("Total Votes:", num_rows)
print("-" * 40)


for j in range(len(candidates)):
    candidate_count = 0

    for k in range(len(sorted_candidates)):
        if candidates[j] == sorted_candidates[k]:
            candidate_count += 1

    candidate_perc.append(round(candidate_count / num_rows * 100, 1))
    candidate_total.append(candidate_count)


results = zip(candidates, candidate_perc, candidate_total)

for row in results:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
    summary = (row[0] + ": ", str(row[1]) + "%", " (" + str(row[2]) + ")")
    summaries.append(summary)


for k in range(len(candidate_perc)):
    if candidate_total[k] > candidate_total[k - 1]:
        winner = candidates[k]


print("-" * 40)
print("Winner:", winner)
print("-" * 40)
print("\n\n")


with open(txt_output_path, mode='w', newline='') as posted_summaries:
    writer = csv.writer(posted_summaries)

    writer.writerows([
        ["Election Results for: " + input_file],
        ["-" * 40],
        ["Total Votes: " + str(num_rows)],
        ["-" * 40]
    ])
    writer.writerows(summaries)
    writer.writerows([
        ["-" * 40],
        ["Winner: " + str(winner)],
        ["-" * 40]
    ])

