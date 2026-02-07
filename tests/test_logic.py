import pytest
from src.core_logic import prompt_with_context_builder

def test_prompt_builder_structure():
    """Test if the prompt builder correctly formats the context and query."""
    query = "How to build Q&A?"
    docs = ["This is context segment 1.", "This is context segment 2."]
    
    prompt = prompt_with_context_builder(query, docs)
    
    # Assertions to ensure the prompt contains key elements
    assert "Context:" in prompt
    assert "Question: How to build Q&A?" in prompt
    assert "This is context segment 1." in prompt
    assert "--" in prompt  # Ensure delimiter is present

def test_empty_docs_handling():
    """Test behavior when no documents are retrieved."""
    query = "What is AI?"
    docs = []
    
    prompt = prompt_with_context_builder(query, docs)
    
    assert "Context:" in prompt
    assert "Question: What is AI?" in prompt
    # Check that it doesn't crash and remains formatted