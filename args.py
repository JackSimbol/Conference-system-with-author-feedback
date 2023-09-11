import numpy as np

args_and_hyperparameters_toy = {
    "t": 100,
    "Author_num": 1600,
    "Reviewer_num": 1200,
    "Paper_per_author": 1,
    "Review_per_paper": 3,
    "Author_dis": ([0.5, 1], [0.2, 0.6]),
    "Review_dis": (0.5, 0.5),
    "Report_dis": ((0.1, 0.05), (1, 0.05)),
    "Bound": 5,
    "k_I": 3,
    "k_1": 3,
    "k_2": 3,
    "Accept_rate": 0.4
}

args_and_hyperparameters_seeker = {
    "Author_num": 800,
    "Reviewer_num": 400,
    "Paper_per_author": 3,
    "Review_per_paper": 3,
    "Author_dis": ([0.5, 1], [0.3, 0.7]),
    "Review_dis": (0.5, 0.5),
    "Report_dis": ((0.1, 0.05), (1, 0.05)),
    "Bound": 5,
    "Accept_rate": 0.5
}