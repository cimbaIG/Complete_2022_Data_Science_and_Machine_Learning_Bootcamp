# My solution
def top_three(scores: list) -> list:
    scores.sort(reverse=True)
    top_scores = []
    
    top_scores = scores[:3]
    
    # Leave this line alone
    return top_scores

print(top_three([14, 982, 123, 2222, 345, 53, 288, 26]))

# Udemy solution
def top_three(scores):
    scores = scores
    top_scores = []
    
    # Solution
    scores.sort()
    list_size = len(scores)
    top_scores = [scores[list_size-1], scores[list_size-2], scores[list_size-3]]
    
    # Leave this line alone
    return top_scores