# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy
import traceback

"""
rewardPlotterAvg.py: Plot the mean, min, max, and standard deviation of reward
averaged over 30 runs.
"""

alg = 'ppo'
gameenv = 'mrv4w'
algname = 'PPO'
gamename = 'Montezumas Revenge'

num_runs = 5
num_episodes = 250
run_episodes = numpy.zeros(num_episodes)
run_score_lists = numpy.zeros((num_episodes, num_runs))

for curr_run in range(num_runs):
    filename = alg + '-logs/' + alg + ' ' + gameenv + ' 1e-4 no' + str(curr_run) + '.txt'
    curr_episode = 0
    with open(filename, 'r') as reader:
        try:
            curr_line = reader.readline()
            while (curr_line):
                data_list = list(curr_line.split("\t"))
                if (filename.startswith('ppo')):
                    run_episodes[curr_episode] = int((int(data_list[0]) * 10) + int(data_list[1]) + 1)
                    run_score_lists[curr_episode][curr_run] = float(data_list[5])
                else:
                    run_episodes[curr_episode] = int(data_list[0])
                    run_score_lists[curr_episode][curr_run] = float(data_list[1])
                curr_line = reader.readline()
                curr_episode += 1
        except:
            print('Problem in line: |' + curr_line + '|')
            traceback.print_exc()
            pass

run_average_scores = numpy.zeros(num_episodes)
run_max_scores = numpy.zeros(num_episodes)
run_min_scores = numpy.zeros(num_episodes)
run_std_scores = numpy.zeros(num_episodes)

for epi in range(num_episodes):
    run_average_scores[epi] = numpy.mean(run_score_lists[epi])
    run_max_scores[epi] = numpy.amax(run_score_lists[epi])
    run_min_scores[epi] = numpy.amin(run_score_lists[epi])
    run_std_scores[epi] = numpy.std(run_score_lists[epi])

plt.errorbar(run_episodes, run_average_scores,
             [run_average_scores - run_min_scores,
              run_max_scores - run_average_scores],
             lw = 0.3, fmt = 'g', label = 'Min & Max')
plt.errorbar(run_episodes, run_average_scores, run_std_scores,
             lw = 0.6, fmt = 'b', label = 'Std Dev')
plt.errorbar(run_episodes, run_average_scores, fmt='k', label='Mean')

# plt.title('DDQN Rewards over 30 Runs (mean, min, max, std)')
# plt.title('PPO Rewards over 30 Runs (mean, min, max, std)')
# plt.title('PG Rewards over 30 Runs (mean, min, max, std)')
plt.title(algname + '-' + gamename + ' Rewards over ' + str(num_runs) + ' Runs (mean, min, max, std)')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.legend(loc='upper left')
plt.grid(True)

# plt.show()

# plt.savefig('plots/DDQN Rewards over 30 Runs.png', dpi = 600)
# plt.savefig('plots/PPO Rewards over 30 Runs.png', dpi = 600)
# plt.savefig('plots/PG Rewards over 30 Runs.png', dpi = 600)
plt.savefig('plots/' + algname + '-' + gamename + ' Rewards over ' + str(num_runs) + ' Runs.png', dpi = 600)

# Ref:
# https://stackoverflow.com/questions/33328774/box-plot-with-min-max-average-and-standard-deviation


