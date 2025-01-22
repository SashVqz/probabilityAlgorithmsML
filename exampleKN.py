import numpy as np
import random

houses = np.array([
    [100, 3, 8, 10],    
    [150, 4, 15, 5],    
    [90, 2, 5, 20],     
    [120, 3, 10, 1],    
    [110, 3, 12, 8]     
])

prices = np.array([200000, 300000, 180000, 250000, 220000])  
newHouse = np.array([120, 3, 10, 5])

distances = np.sqrt(np.sum((houses - newHouse) ** 2, axis=1))
print("Distances to each house:", distances)

k = random.choice([i for i in range(1, 11) if i % 2 != 0])
print("k:", k)

nearestNeighborIndices = np.argsort(distances)[:k]
print("Indices of the k nearest houses:", nearestNeighborIndices)

nearestNeighborPrices = prices[nearestNeighborIndices]
print("Prices of the k nearest houses:", nearestNeighborPrices)

print("Predicted price of the new house:", np.mean(nearestNeighborPrices))