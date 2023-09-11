import numpy as np
from methods import Karger_I, Karger_II, Karger_III
from env import conference
import numpy as np
import random
from args import args_and_hyperparameters_seeker
from matplotlib import pyplot as plt

best_k_rec = [0,0,0,0,0,0,0]
for step in range(20):
    toy_Conference = conference(args_and_hyperparameters_seeker["Author_num"],
                                    args_and_hyperparameters_seeker["Reviewer_num"],
                                    args_and_hyperparameters_seeker["Paper_per_author"],
                                    args_and_hyperparameters_seeker["Review_per_paper"],
                                    args_and_hyperparameters_seeker["Author_dis"],
                                    args_and_hyperparameters_seeker["Review_dis"],
                                    args_and_hyperparameters_seeker["Report_dis"],
                                    args_and_hyperparameters_seeker["Bound"])

    toy_Conference.assign()
    toy_Conference.work()
    A_1 = toy_Conference.make_paper_review_matrix()
    A_2 = toy_Conference.make_reviewer_report_matrix()

    max_good_rate = 0
    best_k = 0
    for k in range(7):
        score = Karger_I(A_1, k+1)
        rank_index = np.argsort(score)[::-1]
        accept_rate = args_and_hyperparameters_seeker["Accept_rate"]
        accept_list = rank_index[:int(accept_rate*len(toy_Conference.Papers))]

        sum_qual = 0
        for i in accept_list:
            sum_qual += toy_Conference.Papers[i].quality
        mean_qual = sum_qual/len(accept_list)
        good_cnt = 0
        for i in accept_list:
            if toy_Conference.Papers[i].quality == 1:
                good_cnt += 1
        good_rate = good_cnt/len(accept_list)

        if good_rate > max_good_rate:
            max_good_rate = good_rate
            best_k = k + 1
    best_k_rec[best_k-1] += 1
    
print(best_k_rec.index(max(best_k_rec))+1)
