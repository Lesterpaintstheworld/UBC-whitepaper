# UBC Burn & Fee Flow Diagram

```mermaid
graph TD
    %% Revenue Burns
    A[Swarm Revenue] --> B[Convert to UBC]
    B --> C[50% Burned]
    B --> D[50% to Shareholders]

    %% Weekly System Burns
    E[Unstaked COMPUTE] --> F[Weekly Conversion]
    F --> G[50% COMPUTE Burned]
    F --> H[50% COMPUTE Sold for UBC]

    %% Trading Fees
    I[5% Trading Fee] --> J[2% Partner Fee]
    I --> K[1% Platform Fee]
    I --> L[2% Investor Fee]
    
    %% Fee Distribution
    J --> M[Weekly Partner Distribution]
    K --> N[Platform Operations]
    L --> O{Claimed within 30 days?}
    O -->|Yes| P[To UBC Traders/Holders]
    O -->|No| Q[Community Development Fund]

    %% Community Development Fund Usage
    Q --> R[Swarm Development Grants]
    Q --> S[Educational Content Creation]

    style C fill:#ff6666
    style G fill:#ff6666
    style Q fill:#66ff66
```

This diagram shows:
1. Revenue Burns
2. Weekly System Burns
3. Trading Fee Structure (5% total)
4. Fee Distribution Paths
5. Community Development Fund Usage

Red boxes indicate permanent burns, green indicates community reinvestment.
