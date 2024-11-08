import price_info 

price_fruit = {'apple': 1.20, 'orange': 1.23, 'watermelon': 6.44, 'pineapple': 2.2, 'pear': 0.90, 'papaya': 2.95, 'pomegranate': 4.95}
quantity_fruit = {'apple': 7, 'orange': 3, 'watermelon': 3, 'pineapple': 5, 'pear': 7, 'papaya': 9, 'pomegranate': 2}

def test_total_cost_shopping():
    cost = 0
    for key in price_fruit.keys():
       if key in quantity_fruit:
           cost += price_fruit[key] * quantity_fruit[key]
    total_cost_from_code = price_info.total_cost_shopping(price_fruit, quantity_fruit)
    
    # Assert if the calculated cost matches the function output
    assert total_cost_from_code == cost
def test_cost_of_fruits():
    fruit = 'apple'
    quantity = 10
    expected_cost = price_fruit[fruit] * quantity
    
    # Get the cost from the `price_info` function
    cost_from_code = price_info.cost_of_fruits(fruit, quantity)
    
    # Assert if the calculated cost matches the function output
    assert cost_from_code == expected_cost