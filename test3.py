from lark import Lark
parser = Lark('''?sum: product
                     | sum "+" product   -> add
                     | sum "-" product   -> sub

                 ?product: item
                     | product "*" item  -> mul
                     | product "/" item  -> div

                 ?item: NUMBER           -> number
                      | "-" item         -> neg
                      | "(" sum ")"

                 %import common.NUMBER
                 %import common.WS
                 %ignore WS
         ''', start='sum')

print(parser.parse("1+1"))