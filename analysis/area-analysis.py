import pyecharts
from analysis.db import MONGODB

coll = MONGODB().get_coll()

re = coll.aggregate([{
    '$group': {
        "_id": {
            "address": "$address"
        },
        "number": {
            "$sum": 1
        }
    }
}])

data = []

# for item in re:
#     address = item['_id']['address']
#     num = item['number']
#     data.append((
#         address, num
#     ))
#
# attr = []
# value = []
#
# for val in data:
#     attr.append(val[0])
#     value.append(val[1])
#
# pie = pyecharts.Map("建筑人才地区分布", width='1920px', height='960px')
# pie.add("地区分布", attr, value)
# pie.render()
