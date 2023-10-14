#!/bin/bash
echo "=== Computing phonetic variations of the input names"
./phonetic_variation.py
echo "=== Appending initials to the names"
./preprocess.py
echo "=== Computing numerology values for the names"
./numerology.py
echo "========================================"
echo "=    Results written to names.txt      ="
echo "========================================"

# Remove temporary files
rm phonetic_variations.txt initials_appended.txt
