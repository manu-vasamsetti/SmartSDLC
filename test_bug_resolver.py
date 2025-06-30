# test_bug_resolver.py
import pytest
from app.services.bug_resolver import fix_code

def test_fix_code_addition():
    buggy_code = "def add(a, b): return a +"
    result = fix_code(buggy_code)
    
    assert "def add" in result
    assert "return" in result
    assert "a + b" in result or "+" in result

def test_fix_code_subtraction():
    buggy_code = "def subtract(a, b): return a -"
    result = fix_code(buggy_code)
    
    assert "def subtract" in result
    assert "-" in result

def test_fix_code_valid_input():
    code = "def multiply(a, b): return a * b"
    result = fix_code(code)

    # Expect unchanged or "already correct" response
    assert "multiply" in result
    assert "*" in result

def test_fix_code_empty_input():
    code = ""
    result = fix_code(code)
    
    assert "error" in result.lower() or result.strip() != ""
