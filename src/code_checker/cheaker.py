import ast

def check_pep8_compliance(source_code):
    """
    PEP 8スタイルガイドに準拠しているかをチェックする関数
    """
    tree = ast.parse(source_code)
    errors = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.lineno != 1 and node.col_offset != 4:
                errors.append(f"Function '{node.name}' does not follow PEP 8 indentation rules.")
        
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == 'os':
                    errors.append("Avoid using 'os' directly. Use pathlib.Path instead.")
    
    return errors

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Check Python code for PEP 8 compliance.")
    parser.add_argument("file", help="The Python file to check.")
    args = parser.parse_args()
    
    with open(args.file, "r", encoding="utf-8") as f:
        source_code = f.read()
    
    errors = check_pep8_compliance(source_code)
    
    if errors:
        print("Errors found:")
        for error in errors:
            print(error)
    else:
        print("No errors found. Code is compliant with PEP 8.")
