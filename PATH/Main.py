#!/usr/bin/env python3
import sys
import io
import tokenize

WORDS = {
    # 문법 키워드
    "imp": "import",
    "fro": "from",
    "fun": "def",
    "ret": "return",
    "cla": "class",
    "whi": "while",
    "eli": "elif",
    "els": "else",
    "try": "try",
    "exc": "except",
    "fin": "finally",
    "wit": "with",
    "pas": "pass",
    "bre": "break",
    "con": "continue",
    "glo": "global",
    "non": "None",
    "tru": "True",
    "fal": "False",

    # 자주 쓰는 함수
    "pri": "print",
    "inp": "input",
    "rng": "range",
    "len": "len",
    "int": "int",
    "str": "str",
    "lis": "list",
    "dic": "dict",
    "set": "set",
    "opn": "open",
    "typ": "type",
    "sum": "sum",
    "min": "min",
    "max": "max",
    "abs": "abs",
    "chr": "chr",
    "ord": "ord",
}


def translate(source: str) -> str:
    result = []
    reader = io.StringIO(source).readline

    for token in tokenize.generate_tokens(reader):
        token_type, token_text, start, end, line = token

        if token_type == tokenize.NAME and token_text in WORDS:
            token = tokenize.TokenInfo(
                token_type,
                WORDS[token_text],
                start,
                end,
                line
            )

        result.append(token)

    return tokenize.untokenize(result)


def main():
    if len(sys.argv) < 2:
        print("사용법: python3 p3.py 파일.p3")
        print("예시: python3 p3.py test.p3")
        return

    file_path = sys.argv[1]
    show_mode = "--show" in sys.argv[2:]

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    python_code = translate(source)

    if show_mode:
        print(python_code)
        return

    old_argv = sys.argv[:]
    sys.argv = [file_path] + [arg for arg in sys.argv[2:] if arg != "--show"]

    try:
        exec(compile(python_code, file_path, "exec"), {
            "__name__": "__main__",
            "__file__": file_path,
        })
    finally:
        sys.argv = old_argv


if __name__ == "__main__":
    main()
