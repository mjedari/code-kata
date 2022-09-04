"""
https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

Given the array restaurants where  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]. You have to filter the restaurants using three filters.

The veganFriendly filter will be either true (meaning you should only include restaurants with veganFriendlyi set to true) or false (meaning you can include any restaurant). In addition, you have the filters maxPrice and maxDistance which are the maximum value for price and distance of restaurants you should consider respectively.

Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest. For restaurants with the same rating, order them by id from highest to lowest. For simplicity veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.


"""
"""
0- Zero version
"""


from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        restaurants.sort(key=lambda x: (-x[1], -x[0]))
        return [i for i, _, v, p, d in restaurants if v >= veganFriendly and p <= maxPrice and d <= maxDistance]


"""
1- First version
"""
# class Solution:
#     def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:

#         def isVeganFriendly(restaurant, veganFriendly):
#             if veganFriendly:
#                 return restaurant[2] == 1
#             return True


#         sortedRestaurants =  sorted([
#             restaurant for restaurant in restaurants
#             if isVeganFriendly(restaurant, veganFriendly)
#             and restaurant[3] <= maxPrice
#             and restaurant[4] <= maxDistance
#         ], key= lambda restaurant: (restaurant[1], restaurant[0]), reverse=True)


#         return [r[0] for r in sortedRestaurants]

"""
2- Second version
"""
# from dataclasses import dataclass

# @dataclass
# class Restaurant:
#     id: int
#     rating: int
#     veganFriendly: int
#     price: int
#     distance: int


# class Solution:
#     def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
#         restaurants = [self.createRestaurant(
#             restaurant) for restaurant in restaurants]

#         filtered_restaurants = filter(
#             lambda restaurant:
#             self.isVeganFriendly(restaurant, veganFriendly)
#             and self.isInThePriceRange(restaurant, maxPrice)
#             and self.isInTheDistance(restaurant, maxDistance),
#             restaurants
#         )

#         return [r.id for r in sorted(filtered_restaurants, key=lambda restaurant: (
#             restaurant.rating, restaurant.id), reverse=True)]

#     def createRestaurant(self, restaurant: List[int]) -> Restaurant:
#         return Restaurant(*restaurant)

#     def isVeganFriendly(self, restaurant: Restaurant, veganFriendly: int) -> bool:
#         if veganFriendly:
#             return restaurant.veganFriendly == 1
#         return True

#     def isInThePriceRange(self, restaurant: Restaurant, maxPrice: int) -> bool:
#         return restaurant.price <= maxPrice

#     def isInTheDistance(self, restaurant: Restaurant, distance: int) -> bool:
#         return restaurant.distance <= distance
