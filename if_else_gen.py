def match_gen(match_case: str, code1:str, code2:str) -> str:
    return f"""
"{match_case}"
%== 
? // 1 or 0
(   // then 
{code1}
) : // else if
(
    !   // drop bool data
{code2}
)
    """


def main():
    print(
    "!!",
    match_gen(
            "+",

            "\"plus\"\n"
            "print",
    match_gen(
            "-",

            "\"minus\"\n"
            "print",

            "\"otherwise\""
            "\nprint",
    )
    )
    )

main()
