from lark import Lark
json_parser = Lark(r"""
    value: dict
         | ESCAPED_STRING
         | SIGNED_NUMBER
         | "true" | "false" | "null"

    

    dict : "{" pair ("," pair)* "}"


    pair : ESCAPED_STRING ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

     """, start='value')

# json_parser = Lark(r"""
#     value: ESCAPED_STRING  
#          | SIGNED_NUMBER
#          | "true" | "false" | "null"

    
#     %import common.ESCAPED_STRING
#     %import common.SIGNED_NUMBER
#     %import common.WS
#     %ignore WS

#     """, start='value')



text = '{"EventReceivedTime": "" ,"Vendor": "","SourceName":""}'
# text = 'scr'
# text = "Oct 11 11:27:23 myserver LEEF:2.0|Microsoft|MSExchange|2013 SP1|15345|src=10.50.1.1 dst=2.10.20.20 spt=1200"
# text = '["item0"]'
# text = {"EventReceivedTime": "item0"}
print(json_parser.parse(text).pretty())