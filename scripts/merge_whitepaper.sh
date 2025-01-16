#!/bin/bash

# Create output directory if it doesn't exist
mkdir -p output

# Create or clear the whitepaper file
> output/whitepaper.md

# Function to add a file to the whitepaper with proper formatting
add_to_whitepaper() {
    echo "Adding $1..."
    
    # Add a newline before each section except the first
    if [ -s output/whitepaper.md ]; then
        echo -e "\n" >> output/whitepaper.md
    fi
    
    # Add the content
    cat "sections/$1" >> output/whitepaper.md
}

# Add files in the correct order
add_to_whitepaper "1_introduction.md"
add_to_whitepaper "2_phase1_foundation.md"
add_to_whitepaper "2_phase2_compute.md"
add_to_whitepaper "2_phase3_ai_operations.md"
add_to_whitepaper "2_phase4_network_expansion.md"
add_to_whitepaper "3_technical_architecture.md"
add_to_whitepaper "4_token_economics.md"
add_to_whitepaper "5_ai_swarms.md"
add_to_whitepaper "6_participation_framework.md"
add_to_whitepaper "7_immediate_next_steps.md"

echo "Whitepaper has been created in output/whitepaper.md"
