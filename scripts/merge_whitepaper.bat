@echo off
setlocal

:: Create output directory if it doesn't exist
if not exist output mkdir output

:: Clear or create the whitepaper file
type nul > output\whitepaper.md

:: Add each file to the whitepaper
echo Adding introduction...
type 1_introduction.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding phase 1...
type 2_phase1_foundation.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding phase 2...
type 2_phase2_compute.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding phase 3...
type 2_phase3_ai_operations.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding phase 4...
type 2_phase4_network_expansion.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding technical architecture...
type 3_technical_architecture.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding token economics...
type 4_token_economics.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding AI swarms...
type 5_ai_swarms.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding participation framework...
type 6_participation_framework.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding immediate next steps...
type 7_immediate_next_steps.md >> output\whitepaper.md

echo Whitepaper has been created in output\whitepaper.md
pause
