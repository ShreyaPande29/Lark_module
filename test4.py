from lark import Lark
import json
from lark.reconstruct import Reconstructor


def test_json_example():
        test_json = '''
            {
                "Hostname" : myserver',
                "empty_array"  : [],
                "booleans"     : { "YES" : true, "NO" : false },
                "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ],
                "strings"      : [ "This", [ "And" , "That", "And a \\"b" ] ],
                "nothing"      : null
            }
        '''

        json_grammar = r"""
            ?start: value

            ?value: object
                  | array
                  | string
                  | SIGNED_NUMBER      -> number
                  | "true"             -> true
                  | "false"            -> false
                  | "null"             -> null
                  

            array  : "[" [value ("," value)*] "]"
            object : "{" [pair ("," pair)*] "}"
            pair   : string ":" value

            string : ESCAPED_STRING

            %import common.ESCAPED_STRING
            %import common.SIGNED_NUMBER
            %import common.WS

            %ignore WS
        """

        json_parser = Lark(json_grammar, parser='lalr', maybe_placeholders=False)
        tree = json_parser.parse(test_json)

        new_json = Reconstructor(json_parser).reconstruct(tree)
        # self.assertEqual(json.loads(new_json), json.loads(test_json)) 
        print(new_json)

test_json_example()
# def main(s, out_fn):
#     graphviz_setup()
#     project_root = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../"))
#     fld = os.path.normpath(project_root + "./mappyfile")
#     gf = os.path.join(fld, "mapfile.lalr.g")
#     grammar_text = open(gf).read()

#     g = Lark(grammar_text, parser="lalr", lexer="contextual")
#     t = g.parse(s)
#     print(t)
#     pydot__tree_to_png(t, os.path.join(project_root, "docs/images", out_fn))
#     print(t.pretty()) 