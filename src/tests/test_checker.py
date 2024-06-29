from code_checker.checker import check_pep8_compliance # type: ignore

def test_check_pep8_compliance():
    source_code = """
def example_function():
    print("Hello, World!")
"""
    errors = check_pep8_compliance(source_code)
    assert len(errors) == 0, f"Errors found: {errors}"

if __name__ == "__main__":
    test_check_pep8_compliance()
    print("All tests passed!")
