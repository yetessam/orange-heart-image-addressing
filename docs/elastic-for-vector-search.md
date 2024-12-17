# 'How to Build a Real-Time RAG-Enabled AI Chatbot with Flink, Elastic, OpenAI, and LangChain' webinar notes

## Summary

Webinar on how to combine multiple search methods and content sources using fully supporter connections and feeds into a single platform which then uses Elastic to do searching, retrieval augemented generation (RAG) so that your chatbot can be updated real-time while simulatneously caching.   That last bit with the caching helps reduce the compute costs,  huge number of asynchrnous updates from all the various content sources (both internal/external) and the continual need to filter/personalize/store content, refinine search etc. 

The webinar has one specific stock symbol's price being pulled in real time.  That's the simplest use case, but for the case of real financial data, there could be heaps of connectors, setting up the SQL statements etc.

## Vector Search

From https://www.elastic.co/what-is/vector-search:

> Vector search leverages machine learning (ML) to capture the meaning and context of unstructured data, including text and images, transforming it into a numeric representation. Frequently used for semantic search, vector search finds similar data using approximate nearest neighbor (ANN) algorithms. Compared to traditional keyword search, vector search yields more relevant results and executes faster.
Vector search is more than text-matching, it allows semantics search can match terminology.
 need the keywords.

Similar images, audio or multi-modal models that combine text and image in one training model.

Can fine tune your models and domain for your industry and fine tune in. vector search.

Vector search has input media, send it into a embedding dense vector model and run through multiple layers to find the text using semantic search...

Output is dense vector representation, store it into a vector database such as Elastic so it's searchable.

During query time, run the query through the SAME embedding model, and you run vector search to find documents that are hopefully most relevant, (nearest neighbour or approximate nearest neighbour).

## Elasticsearch 

Specifically with Elasticsearch, you want to think about many facets.. speed, all the other search engine capabilities that search has provided including full text search,  roles, confidential vs public facing, geo region search, chunking and re-ranking.

Why use Elastic as the vector data base?   Already one of the most popular search engines, 12 years of experience, already combine multiple search methodologies, nested vector storage so that large docs are chunks and you can have nested vectors that allows you have some of the metadata stored together for large documents.    Dense vectors need to be cached in RAM and they already have caching models to save RAM and try to do more efficient storage methods.

BBQ Better Binary Quantization to create more efficiency and oversampling to help speed up retrievel time.


Once you have the search results you pass it to the LLM prompted to improve the LLM response.

## Elasticsearch _infererence API

New API that allows for a search followed up by reranking after retrieval.
Multi stage retrieval gives you the documents and then you have a second stage to do re-ranking, which gives better results.

A Perform lexical search 
B Then pass that to the semantic reranking model to get better results.

In step B, you can pass the content to one of many services to do the reranking. 

Semantic search chunks the documents for you and then manages the context. 

## Sources  
How to Build a Real-Time RAG-Enabled AI Chatbot with Flink, Elastic, OpenAI, and LangChain webinar presented by Confluent, Dec 17, 2024

## Resources  

- [Github Repo](https://github.com/gopi0518/docschatbot)
- [Gen AI](https://www.confluent.io/generative-ai/)
- [Flink AI Inference Model for RAG]https://www.confluent.io/blog/mastering-real-time-retrieval-augmented-generation-rag-with-flink/

