

class DefaultTable(object):
    class Meta:
        fields = [1,2,3]




class LiquidTable(DefaultTable):
    Meta.fields += [5]


print LiquidTable.Meta.fields
