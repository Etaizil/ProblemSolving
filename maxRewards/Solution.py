def maxRewards(rewards):
    maxSum = 0
    while True:
        maxReward = max(rewards)
        if maxReward == 0:
            break
        maxSum += maxReward
        maxIndex = rewards.index(maxReward)
        rewards[maxIndex] = 0
        rewards = [reward - 1 for reward in rewards if reward > 0]
    return maxSum
