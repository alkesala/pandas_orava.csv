import pandas

data = pandas.read_csv("orava.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel)
print(red_squirrel)
print(black_squirrel)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel]

}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

