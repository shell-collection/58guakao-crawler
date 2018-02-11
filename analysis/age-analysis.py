import pyecharts
from analysis.db import MONGODB

coll = MONGODB().get_coll()

re = coll.aggregate([{
    '$group': {
        "_id": {
            "age": "$age"
        },
        "number": {
            "$sum": 1
        }
    }
}])

data = []

for item in re:
    age = item['_id']['age']
    num = item['number']
    data.append((
        int(age), num
    ))

data.sort()
attr = []
value = []

for val in data:
    attr.append(str(val[0])+'岁')
    value.append(val[1])

bar = pyecharts.Bar("建筑人才年龄分析")
bar.add("平均年龄", attr, value)
bar.render()
