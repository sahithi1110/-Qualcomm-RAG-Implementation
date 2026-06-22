# Architecture

## Overview

The project follows a practical RAG architecture.

## Flow

1. Load approved documents
2. Clean document text
3. Split documents into chunks
4. Create embeddings
5. Store embeddings in ChromaDB
6. Search relevant chunks for a user question
7. Re-rank retrieved chunks using simple keyword overlap
8. Build a grounded prompt
9. Return an answer with source traceability
10. Run evaluation against expected source documents

## Why This Design Is Useful

This design keeps answers connected to source material. It also gives reviewers a way to check which documents were used to support the answer.

## Production Improvements

In production, I would add authentication, role-based document access, feedback scoring, LLM provider integration, monitoring dashboards, and cloud deployment.
