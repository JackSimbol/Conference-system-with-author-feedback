import numpy as np
import random

class Paper():
    def __init__(self, id, quality):
        self.quality = quality
        self.id = id

class Review():
    def __init__(self, id, review, target_paper_id):
        self.id = id
        self.target_paper_id = target_paper_id
        self.review = review

class Report():
    def __init__(self, report, target_review, target_paper_id):
        self.id = id
        self.report = report
        self.target_review_id = target_review
        self.target_paper_id = target_paper_id

class Author():
    def __init__(self, id, report_quality: tuple, author_quality: float, paper_num): 
        self.id = id
        self.report_quality = report_quality # report quality is a tuple of (alpha, beta)
        self.author_quality = author_quality # author quality is a float in (0, 1)
        self.papers = []
        self.reports = []
        for i in range(paper_num):
            q_eps = random.random()
            if q_eps < author_quality:
                new_paper = Paper(self.id*100+i+1, 1)
            else:
                new_paper = Paper(self.id*100+i+1, -1)
            self.papers.append(new_paper)

    def report(self, paper_id, review: int, bound: float):
        paper = self.papers[paper_id%100-1]
        if paper.quality == 1: # "accept" as ground truth
            if review == 1:
                return 1
            else: # if the real quality is 1 but the review is -1, then the author gives -1 report towards the review with prob beta
                eps = random.random()
                if eps < self.report_quality[1]:
                    return -1
                else:
                    return 1
        else: # "reject" as ground truth
            if review == 1:
                return 1
            else:
                eps = random.random()
                if eps < self.report_quality[0]:
                    return -1
                else:
                    return 1

class Reviewer():
    def __init__(self, id, review_quality):
        self.id = id
        self.review_quality = review_quality
        self.assigned = []
        self.reviews = []

    def review(self, paper_quality, boundary):
        eps = random.random()
        if eps < self.review_quality:
            return paper_quality
        else:
            return -paper_quality
    
class conference():
    def __init__(self, Author_num, Reviewer_num, paper_per_author, review_per_paper, author_dis, review_dis, report_dis, bound):
        # author_dis: 2 Ascending vectors. vector 1: cumulative prob. vector 2: author_quality 
        # review_dis: Good_quality g, Probability q. The reviewer_quality is g w.p. q; 0 w.p. (1-q). [tuple: (g, q)]
        # report_dis: normal distributions of alpha and beta [tuple: ((mu_alpha, sigma_alpha),(mu_beta, sigma_beta))]
        self.Author_num = Author_num
        self.Reviewer_num = Reviewer_num
        self.paper_per_author = paper_per_author
        self.review_per_paper = review_per_paper
        self.bound = bound
        self.Authors = []
        for i in range(Author_num):
            new_alpha = random.normalvariate(report_dis[0][0], report_dis[0][1])
            new_beta = random.normalvariate(report_dis[1][0], report_dis[1][1])
            author_eps = random.random()
            for j in range(len(author_dis[0])):
                if author_eps <= author_dis[0][j]:
                    new_quality = author_dis[1][j]
                    break                
            new_author = Author(i, (new_alpha, new_beta), new_quality, self.paper_per_author)
            self.Authors.append(new_author)
        self.Reviewers = []
        for i in range(Reviewer_num):
            review_eps = random.random()
            if review_eps < review_dis[1]:
                new_review = review_dis[0]
            else:
                new_review = 0.5
            new_reviewer = Reviewer(i, new_review)
            self.Reviewers.append(new_reviewer)
        self.Papers = []
        self.Reviews = []
        self.Reports = []
        for i in range(self.Author_num):
            self.Papers.extend(self.Authors[i].papers)
        
    def assign(self):
        # Assigning papers
        reviewer_load = [(self.Author_num*self.paper_per_author/self.review_per_paper+1) for i in range(self.Reviewer_num)]
        available_reviewers = [i for i in range(self.Reviewer_num)]
        for author in self.Authors:
            local_avai_rev = available_reviewers.copy()
            for paper in author.papers:
                reviewers = random.sample(local_avai_rev, self.review_per_paper)
                for r in reviewers:
                    self.Reviewers[r].assigned.append(paper)
                    reviewer_load[r] -= 1
                    local_avai_rev.remove(r)
                    if reviewer_load[r] <= 0:
                        available_reviewers.remove(r)

    
    def work(self):
        for reviewer in self.Reviewers:
            for i in range(len(reviewer.assigned)):
                paper = reviewer.assigned[i]
                review = reviewer.review(paper.quality, self.bound)
                new_Review = Review(reviewer.id*100+i+1, review, paper.id)
                reviewer.reviews.append(new_Review)
                self.Reviews.append(new_Review)
    
    def report(self):
        for review in self.Reviews:
            author = self.Authors[review.target_paper_id/100]
            report = author.report(review.target_paper_id, review.review, self.bound)
            new_Report = Report(report, review, review.target_paper_id)
            author.reports.append(new_Report)
            self.Reports.append(new_Report)
    
    def make_paper_review_matrix(self):
        A = np.zeros((len(self.Papers), self.Reviewer_num), dtype=int)
        for i in range(self.Reviewer_num):
            reviewer = self.Reviewers[i]
            for j in range(len(reviewer.reviews)):
                review = reviewer.reviews[j]
                paper = reviewer.assigned[j]
                A[self.Papers.index(paper), i] = review.review        
        return A
    
    def make_reviewer_report_matrix(self):
        A = np.zeros((self.Reviewer_num, self.Author_num), dtype=int)
        for i in range(self.Author_num):
            author = self.Authors[i]
            for report in author.reports:
                reviewer = report.review.id/100
                A[reviewer, i] = report.report
        return A