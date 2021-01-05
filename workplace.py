def pizzaArea(boxArea):
  # write your code here
  pizza = (((boxArea ** 0.5) / 2) - 0.5)** 2 * 3.14

  return str(round(pizza, 1)) + "\n"
