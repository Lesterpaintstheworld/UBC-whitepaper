@echo off
setlocal

:: Clear or create the whitepaper file
type nul > output\whitepaper.md

:: Add each file to the whitepaper
echo Adding introduction...
type sections\1_introduction.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding phase 1...
type sections\2_phase1_foundation.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding phase 2...
type sections\2_phase2_compute.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding phase 3...
type sections\2_phase3_ai_operations.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding phase 4...
type sections\2_phase4_network_expansion.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding technical architecture...
type sections\3_technical_architecture.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding token economics...
type sections\4_token_economics.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding AI swarms...
type sections\5_ai_swarms.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding participation framework...
type sections\6_participation_framework.md >> output\whitepaper.md
echo. >> output\whitepaper.md

echo Adding immediate next steps...
type sections\7_immediate_next_steps.md >> output\whitepaper.md

echo Whitepaper has been created in output\whitepaper.md
pause
