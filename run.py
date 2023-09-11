from methods import majority_vote, Karger_I, Karger_II, Karger_III, majority_vote_II, Karger_IV
from env import conference
import numpy as np
import random
from args import args_and_hyperparameters_toy
from matplotlib import pyplot as plt

# if "seed" in args_and_hyperparameters_toy:
#     seed = args_and_hyperparameters_toy["seed"]
#     random.seed(seed)

t = args_and_hyperparameters_toy["t"]

average_good_rate = [0, 0, 0, 0, 0, 0]
average_score = [0, 0, 0, 0, 0, 0]
average_accuracy = [0, 0, 0, 0, 0, 0]

for step in range(t):
    print("Iter ", step+1)
    seed = random.randint(0, 100000)
    random.seed(seed)
    toy_Conference1 = conference(args_and_hyperparameters_toy["Author_num"],
                                args_and_hyperparameters_toy["Reviewer_num"],
                                args_and_hyperparameters_toy["Paper_per_author"],
                                args_and_hyperparameters_toy["Review_per_paper"],
                                args_and_hyperparameters_toy["Author_dis"],
                                args_and_hyperparameters_toy["Review_dis"],
                                args_and_hyperparameters_toy["Report_dis"],
                                args_and_hyperparameters_toy["Bound"])

    toy_Conference1.assign()
    toy_Conference1.work()
    A = toy_Conference1.make_paper_review_matrix()
    score = majority_vote(A)
    rank_index = np.argsort(score)[::-1]
    accept_rate = args_and_hyperparameters_toy["Accept_rate"]
    accept_list = rank_index[:int(accept_rate*len(toy_Conference1.Papers))]

    sum_qual = 0
    for i in accept_list:
        sum_qual += toy_Conference1.Papers[i].quality
    mean_qual = sum_qual/len(accept_list)

    good_cnt = 0
    true_cnt = 0
    false_cnt = 0
    for i in accept_list:
        if toy_Conference1.Papers[i].quality == 1:
            good_cnt += 1
    for i in range(len(toy_Conference1.Papers)):
        if i in accept_list:
            res = 1
        else:
            res = -1
        if res == toy_Conference1.Papers[i].quality:
            true_cnt += 1
        else:
            false_cnt += 1
    accuracy = true_cnt/(true_cnt + false_cnt)
    good_rate = good_cnt/len(accept_list)
    print("MAJOR_I: ", mean_qual, good_rate, accuracy)
    average_good_rate[0] += good_rate
    average_score[0] += mean_qual
    average_accuracy[0] += accuracy
    

    toy_Conference2 = conference(args_and_hyperparameters_toy["Author_num"],
                                args_and_hyperparameters_toy["Reviewer_num"],
                                args_and_hyperparameters_toy["Paper_per_author"],
                                args_and_hyperparameters_toy["Review_per_paper"],
                                args_and_hyperparameters_toy["Author_dis"],
                                args_and_hyperparameters_toy["Review_dis"],
                                args_and_hyperparameters_toy["Report_dis"],
                                args_and_hyperparameters_toy["Bound"])

    toy_Conference2.assign()
    toy_Conference2.work()
    A_ = toy_Conference2.make_paper_review_matrix()
    score = Karger_I(A_, args_and_hyperparameters_toy["k_I"])
    rank_index = np.argsort(score)[::-1]
    accept_rate = args_and_hyperparameters_toy["Accept_rate"]
    accept_list = rank_index[:int(accept_rate*len(toy_Conference2.Papers))]

    sum_qual = 0
    for i in accept_list:
        sum_qual += toy_Conference2.Papers[i].quality
    mean_qual = sum_qual/len(accept_list)
    good_cnt = 0
    true_cnt = 0
    false_cnt = 0
    for i in accept_list:
        if toy_Conference2.Papers[i].quality == 1:
            good_cnt += 1
    for i in range(len(toy_Conference2.Papers)):
        if i in accept_list:
            res = 1
        else:
            res = -1
        if res == toy_Conference2.Papers[i].quality:
            true_cnt += 1
        else:
            false_cnt += 1
    accuracy = true_cnt/(true_cnt + false_cnt)
    good_rate = good_cnt/len(accept_list)
    print("KARGERI: ", mean_qual, good_rate, accuracy)
    average_good_rate[1] += good_rate
    average_score[1] += mean_qual
    average_accuracy[1] += accuracy

    toy_Conference3 = conference(args_and_hyperparameters_toy["Author_num"],
                                args_and_hyperparameters_toy["Reviewer_num"],
                                args_and_hyperparameters_toy["Paper_per_author"],
                                args_and_hyperparameters_toy["Review_per_paper"],
                                args_and_hyperparameters_toy["Author_dis"],
                                args_and_hyperparameters_toy["Review_dis"],
                                args_and_hyperparameters_toy["Report_dis"],
                                args_and_hyperparameters_toy["Bound"])

    toy_Conference3.assign()
    toy_Conference3.work()
    A_1 = toy_Conference3.make_paper_review_matrix()
    A_2 = toy_Conference3.make_reviewer_report_matrix()
    score = Karger_II(A_1, A_2, args_and_hyperparameters_toy["k_1"], args_and_hyperparameters_toy["k_2"])
    rank_index = np.argsort(score)[::-1]
    accept_rate = args_and_hyperparameters_toy["Accept_rate"]
    accept_list = rank_index[:int(accept_rate*len(toy_Conference3.Papers))]

    sum_qual = 0
    for i in accept_list:
        sum_qual += toy_Conference3.Papers[i].quality
    mean_qual = sum_qual/len(accept_list)

    good_cnt = 0
    true_cnt = 0
    false_cnt = 0
    for i in accept_list:
        if toy_Conference3.Papers[i].quality == 1:
            good_cnt += 1
    for i in range(len(toy_Conference3.Papers)):
        if i in accept_list:
            res = 1
        else:
            res = -1
        if res == toy_Conference3.Papers[i].quality:
            true_cnt += 1
        else:
            false_cnt += 1
    accuracy = true_cnt/(true_cnt + false_cnt)
    good_rate = good_cnt/len(accept_list)
    print("KARGEII: ", mean_qual, good_rate, accuracy)
    average_good_rate[2] += good_rate
    average_score[2] += mean_qual
    average_accuracy[2] += accuracy


    toy_Conference4 = conference(args_and_hyperparameters_toy["Author_num"],
                                args_and_hyperparameters_toy["Reviewer_num"],
                                args_and_hyperparameters_toy["Paper_per_author"],
                                args_and_hyperparameters_toy["Review_per_paper"],
                                args_and_hyperparameters_toy["Author_dis"],
                                args_and_hyperparameters_toy["Review_dis"],
                                args_and_hyperparameters_toy["Report_dis"],
                                args_and_hyperparameters_toy["Bound"])

    toy_Conference4.assign()
    toy_Conference4.work()
    A_1 = toy_Conference4.make_paper_review_matrix()
    A_2 = toy_Conference4.make_reviewer_report_matrix()
    score = Karger_III(A_1, A_2, args_and_hyperparameters_toy["k_1"], args_and_hyperparameters_toy["k_2"])
    rank_index = np.argsort(score)[::-1]
    accept_rate = args_and_hyperparameters_toy["Accept_rate"]
    accept_list = rank_index[:int(accept_rate*len(toy_Conference4.Papers))]

    sum_qual = 0
    for i in accept_list:
        sum_qual += toy_Conference4.Papers[i].quality
    mean_qual = sum_qual/len(accept_list)

    good_cnt = 0
    true_cnt = 0
    false_cnt = 0
    for i in accept_list:
        if toy_Conference4.Papers[i].quality == 1:
            good_cnt += 1
    for i in range(len(toy_Conference4.Papers)):
        if i in accept_list:
            res = 1
        else:
            res = -1
        if res == toy_Conference4.Papers[i].quality:
            true_cnt += 1
        else:
            false_cnt += 1
    accuracy = true_cnt/(true_cnt + false_cnt)
    good_rate = good_cnt/len(accept_list)
    print("KARGIII: ", mean_qual, good_rate, accuracy)
    average_good_rate[3] += good_rate
    average_score[3] += mean_qual
    average_accuracy[3] += accuracy

    toy_Conference5 = conference(args_and_hyperparameters_toy["Author_num"],
                                args_and_hyperparameters_toy["Reviewer_num"],
                                args_and_hyperparameters_toy["Paper_per_author"],
                                args_and_hyperparameters_toy["Review_per_paper"],
                                args_and_hyperparameters_toy["Author_dis"],
                                args_and_hyperparameters_toy["Review_dis"],
                                args_and_hyperparameters_toy["Report_dis"],
                                args_and_hyperparameters_toy["Bound"])

    toy_Conference5.assign()
    toy_Conference5.work()
    A_1 = toy_Conference5.make_paper_review_matrix()
    A_2 = toy_Conference5.make_reviewer_report_matrix()
    score = majority_vote_II(A_1, A_2)
    rank_index = np.argsort(score)[::-1]
    accept_rate = args_and_hyperparameters_toy["Accept_rate"]
    accept_list = rank_index[:int(accept_rate*len(toy_Conference5.Papers))]

    sum_qual = 0
    for i in accept_list:
        sum_qual += toy_Conference5.Papers[i].quality
    mean_qual = sum_qual/len(accept_list)

    good_cnt = 0
    true_cnt = 0
    false_cnt = 0
    for i in accept_list:
        if toy_Conference5.Papers[i].quality == 1:
            good_cnt += 1
    for i in range(len(toy_Conference5.Papers)):
        if i in accept_list:
            res = 1
        else:
            res = -1
        if res == toy_Conference5.Papers[i].quality:
            true_cnt += 1
        else:
            false_cnt += 1
    accuracy = true_cnt/(true_cnt + false_cnt)
    good_rate = good_cnt/len(accept_list)
    print("MAJORII", mean_qual, good_rate, accuracy)
    average_good_rate[4] += good_rate
    average_score[4] += mean_qual
    average_accuracy[4] += accuracy

    toy_Conference6 = conference(args_and_hyperparameters_toy["Author_num"],
                                args_and_hyperparameters_toy["Reviewer_num"],
                                args_and_hyperparameters_toy["Paper_per_author"],
                                args_and_hyperparameters_toy["Review_per_paper"],
                                args_and_hyperparameters_toy["Author_dis"],
                                args_and_hyperparameters_toy["Review_dis"],
                                args_and_hyperparameters_toy["Report_dis"],
                                args_and_hyperparameters_toy["Bound"])

    toy_Conference6.assign()
    toy_Conference6.work()
    A_1 = toy_Conference6.make_paper_review_matrix()
    A_2 = toy_Conference6.make_reviewer_report_matrix()
    score = Karger_IV(A_1, A_2, args_and_hyperparameters_toy["k_1"], args_and_hyperparameters_toy["k_2"], args_and_hyperparameters_toy["Paper_per_author"])
    rank_index = np.argsort(score)[::-1]
    accept_rate = args_and_hyperparameters_toy["Accept_rate"]
    accept_list = rank_index[:int(accept_rate*len(toy_Conference6.Papers))]

    sum_qual = 0
    for i in accept_list:
        sum_qual += toy_Conference5.Papers[i].quality
    mean_qual = sum_qual/len(accept_list)

    good_cnt = 0
    true_cnt = 0
    false_cnt = 0
    for i in accept_list:
        if toy_Conference6.Papers[i].quality == 1:
            good_cnt += 1
    for i in range(len(toy_Conference6.Papers)):
        if i in accept_list:
            res = 1
        else:
            res = -1
        if res == toy_Conference6.Papers[i].quality:
            true_cnt += 1
        else:
            false_cnt += 1
    accuracy = true_cnt/(true_cnt + false_cnt)
    good_rate = good_cnt/len(accept_list)
    print("KARGEIV", mean_qual, good_rate, accuracy)
    average_good_rate[5] += good_rate
    average_score[5] += mean_qual
    average_accuracy[5] += accuracy

for i in range(6):
    average_good_rate[i] /= t
    average_score[i] /= t
    average_accuracy[i] /= t

print("Total: ")
print("MAJOR_I: ", average_score[0], average_good_rate[0], average_accuracy[0])
print("KARGERI: ", average_score[1], average_good_rate[1], average_accuracy[1])
print("KARGEII: ", average_score[2], average_good_rate[2], average_accuracy[2])
print("KARGIII: ", average_score[3], average_good_rate[3], average_accuracy[3])  
print("MAJORII: ", average_score[4], average_good_rate[4], average_accuracy[4])
print("KARGEIV: ", average_score[5], average_good_rate[5], average_accuracy[5])