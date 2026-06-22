# Project Write-up

## Project Title

Enterprise RAG LLM Quality Evaluation

## Candidate

Sahithi Mogudala

## Role

AI/ML Engineer

## Objective

The objective of this project was to build a sanitized enterprise RAG system that improves LLM response quality by grounding answers in approved source documents.

## Problem

A normal LLM may answer from general knowledge and sometimes guess. In an enterprise environment, that is risky because users often need answers from internal process documents, quality notes, monitoring guides, deployment practices, and security standards.

## Solution

I built a RAG workflow that retrieves relevant document chunks before preparing the answer. This makes the answer more grounded, traceable, and easier to evaluate.

## What I Built

The project includes document loading, text cleaning, chunking with overlap, embedding generation, vector indexing with ChromaDB, hybrid retrieval with simple keyword-aware re-ranking, grounded prompt creation, demo answer generation, FastAPI endpoints, evaluation queries, PyTest tests, Docker setup, GitHub Actions workflow, and documentation.

## My Contribution

I worked on the full flow from data preparation to API testing. I designed the folder structure, built the retrieval pipeline, added evaluation logic, created API endpoints, and wrote documentation so the project can be reviewed clearly.

## Outcome

The project shows how a RAG-based AI system can reduce hallucinations, improve response accuracy, and support AI quality review. The evaluation checks whether the expected source documents are retrieved for test questions.

## Business Value

This type of project can help enterprise teams answer internal questions faster, reduce manual document search, improve AI response trust, and support quality control for AI-generated answers.

## Sanitization Note

This project uses sample documents only. It does not contain confidential company data, client data, access keys, or internal production details.
