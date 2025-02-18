total_land = 80 
each_plot = 80/5

# 30% of his tomato land gives him 10 tonne yield per acre.The remaining 70% of his 
# tomato land gives him 12 tonnes yield per acre. The selling price of tomatois Rs. 7 per Kg.
tomato_output = (( 0.3 * each_plot ) * 10 * 1000) + ( ( 0.3 * each_plot ) * 12 * 1000)
tomato_sales = 7 * tomato_output

#The yield of potatoes is 10 tonnes per acre. He sells each kg at Rs. 20.
potato_output = 10 * each_plot * 1000
potato_sales = potato_output * 20

#The yield of cabbage is 14 tonnes per acre. He sells each kg at Rs. 24.
cabbage_output = 14 * each_plot * 1000
cabbage_sales = cabbage_output * 24

#The yield of sunflowers is 0.7 tonnes per acre. He sells each kg at Rs. 200.
sunflowers_output = 0.7 * each_plot * 1000
sunflowers_sales = sunflowers_output * 200

#The yield of sugarcane is 45 tonnes per acre. He sells each tonne at Rs. 4,000.
sugarcane_output =  45 * each_plot 
sugarcane_sales = sugarcane_output * 4000


# Total Sales 
total_sales = tomato_sales + potato_sales + cabbage_sales + sugarcane_sales + sunflowers_output
print("Total Sales :", total_sales)

#chemical free sales
chemical_free_sales = total_sales - sugarcane_sales
print("Chemical free Sales: ", chemical_free_sales)