from interpreter import Interpreter
def main():
    code = """
    BEGIN
        y := 2;
        BEGIN
            a := 3;
            a := a;
            b := 10 + a + 10 * y / 4;
            c := a - b;
        END;
        x := 11;
    END.
    """
    result = Interpreter().eval(code)
    print("Result:")
    for var, value in result.items():
        print(f"{var} = {value}")
if __name__ == "__main__":
    main()
