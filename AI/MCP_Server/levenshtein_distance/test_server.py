"""
Test script for the Levenshtein Distance MCP Server
This script demonstrates the functionality of all available tools.
"""

# Import the functions directly for testing
import sys
import os
sys.path.append(os.path.dirname(__file__))

from main import (
    calculate_levenshtein_distance,
    levenshtein_distance_with_matrix,
    levenshtein_similarity_ratio,
    find_closest_match,
    edit_operations
)

def test_basic_distance():
    """Test basic distance calculation"""
    print("=== Basic Distance Calculation ===")
    
    test_cases = [
        ("cat", "bat"),
        ("kitten", "sitting"),
        ("hello", "jello"),
        ("test", ""),
        ("", "abc"),
        ("same", "same")
    ]
    
    for str1, str2 in test_cases:
        distance = calculate_levenshtein_distance(str1, str2)
        print(f"'{str1}' → '{str2}': {distance}")
    print()

def test_matrix_analysis():
    """Test detailed matrix analysis"""
    print("=== Matrix Analysis ===")
    
    result = levenshtein_distance_with_matrix("cat", "dog")
    print(f"String 1: {result['str1']}")
    print(f"String 2: {result['str2']}")
    print(f"Distance: {result['distance']}")
    print(f"Analysis: {result['analysis']}")
    print("Matrix:")
    for row in result['matrix']:
        print("  ", row)
    print()

def test_similarity_ratio():
    """Test similarity ratio calculation"""
    print("=== Similarity Ratios ===")
    
    test_cases = [
        ("hello", "jello"),
        ("python", "java"),
        ("abc", "abc"),
        ("test", "best"),
        ("", "")
    ]
    
    for str1, str2 in test_cases:
        ratio = levenshtein_similarity_ratio(str1, str2)
        print(f"'{str1}' vs '{str2}': {ratio:.2%}")
    print()

def test_closest_match():
    """Test finding closest match"""
    print("=== Closest Match Finding ===")
    
    target = "test"
    candidates = ["best", "rest", "nest", "west", "toast", "taste"]
    
    result = find_closest_match(target, candidates)
    print(f"Target: '{result['target']}'")
    print(f"Best match: '{result['best_match']}' (distance: {result['best_distance']}, similarity: {result['best_similarity']:.2%})")
    print("\nAll matches:")
    for match in result['all_matches']:
        print(f"  '{match['candidate']}': distance={match['distance']}, similarity={match['similarity']:.2%}")
    print()

def test_edit_operations():
    """Test edit operations tracing"""
    print("=== Edit Operations ===")
    
    test_cases = [
        ("cat", "dog"),
        ("kitten", "sitting"),
        ("abc", "def")
    ]
    
    for str1, str2 in test_cases:
        result = edit_operations(str1, str2)
        print(f"Transform '{result['str1']}' → '{result['str2']}' (distance: {result['distance']})")
        print("Operations:")
        for i, op in enumerate(result['operations'], 1):
            print(f"  {i}. {op}")
        print()

def run_all_tests():
    """Run all test functions"""
    print("🧪 Testing Levenshtein Distance MCP Server Functions")
    print("=" * 60)
    
    test_basic_distance()
    test_matrix_analysis()
    test_similarity_ratio()
    test_closest_match()
    test_edit_operations()
    
    print("✅ All tests completed successfully!")

if __name__ == "__main__":
    run_all_tests()
