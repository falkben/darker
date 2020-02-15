from textwrap import dedent

ORIGINAL = dedent('''\
    original first line
    original second line
    original third line
''')

CHANGE_SECOND_LINE = dedent('''\
    diff --git a/test1.txt b/test1.txt
    index 9ed6856..5a6b0d2 100644
    --- a/test1.txt
    +++ b/test1.txt
    @@ -1,3 +1,3 @@
     original first line
    -original second line
    +changed second line
     original third line
''')
