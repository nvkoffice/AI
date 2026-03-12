```mermaid
graph TD
    User((User))
    Input[/"User Prompt:
    'Draft an email to my boss 
    about the delay'"/]

    subgraph Orchestrator ["Orchestration Layer (Semantic Kernel / Python)"]
        Router{"Intent Router"}
        PromptBuilder["Prompt Builder"]
    end

    subgraph Memory ["Layer 2: Personal Context"]
        ProfileDB[("User Profile DB (SQL/Cosmos)")]
        VectorMem[("Long-Term Memory (Vector DB)")]
    end

    subgraph RAG ["Layer 3: Enterprise RAG"]
        DocSearch[("Azure AI Search")]
    end

    subgraph AI ["Layer 4: Generative AI"]
        LLM("Large Language Model (GPT-4o)")
    end

    User --> Input --> Router
    Router --> ProfileDB
    Router --> VectorMem
    Router --> DocSearch
    ProfileDB & VectorMem & DocSearch --> PromptBuilder
    PromptBuilder --> LLM --> User
    User --> VectorMem
