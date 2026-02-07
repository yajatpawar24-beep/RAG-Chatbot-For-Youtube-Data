import pytest
from unittest.mock import MagicMock, patch
from src.pipeline import rag_pipeline

@patch('src.pipeline.retrieve')
@patch('src.pipeline.generate_answer')
def test_full_rag_pipeline_flow(mock_generate, mock_retrieve):
    """
    Test the integration of the RAG pipeline:
    Ensures that retrieved documents are correctly passed to the generator.
    """
    # 1. Setup Mock Data
    mock_query = "How to build next-level Q&A?"
    mock_docs = ["Segment about ODQA pipelines."]
    mock_sources = [("Video Title", "https://youtu.be/example")]
    mock_answer = "You build it using an ODQA pipeline."

    # 2. Configure Mocks
    mock_retrieve.return_index = (mock_docs, mock_sources)
    mock_generate.return_value = mock_answer

    # 3. Execute Pipeline
    result = rag_pipeline(mock_query)

    # 4. Assertions
    # Verify the answer is present in the final output
    assert "You build it using an ODQA pipeline." in result
    # Verify sources are appended
    assert "Sources:" in result
    assert "Video Title" in result
    
    # Verify the internal calls were made with the correct query
    mock_retrieve.assert_called_once()
    assert mock_retrieve.call_args[0][0] == mock_query