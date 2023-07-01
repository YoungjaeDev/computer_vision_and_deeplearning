import numpy as np

"""
numpy.prod: prod 함수는 지정된 축을 따라 배열에 있는 모든 요소의 곱을 계산하거나 축이 지정되지 않은 경우 flatten. 제품을 나타내는 단일 스칼라 값을 반환
numpy.cumprod: cumprod 함수는 지정된 축을 따라 요소의 누적 곱을 계산하거나 축이 지정되지 않은 경우 flatten. 각 요소가 해당 위치까지의 누적 곱인 배열을 반환
"""

arr = np.array([2.5, 1.5, 3.0, 4.5, 2.0, 0.5, 1.0, 3.5, 2.0, 2.5])

product = np.prod(arr)
print("Product:", product)

cumulative_product = np.cumprod(arr)
print("Cumulative Product:", cumulative_product)