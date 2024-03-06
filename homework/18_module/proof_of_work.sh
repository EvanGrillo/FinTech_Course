#!/bin/bash

# Generate fallback file
if [ -z "$1"]
then
    echo "test" > test.txt
fi

filename=${1:-"test.txt"}
target_prefix=${2:-"00"}
hash_prefix=""
attempts=0

while [ "$hash_prefix" != "$target_prefix" ]; do

    # Generate timestamp, pipe to head and truncate first 32 chars
    echo "$(date +%s%N | head -c 32)" >> "$filename"
    
    # Calculate the SHA-256 hash of the file
    hash_prefix=$(shasum -a 256 "$filename" | cut -c 1-${#target_prefix})

    ((attempts++))
    
    echo "Attempt $attempts - Current hash prefix: $hash_prefix"

done

echo "Hash prefix is now: $hash_prefix"
echo "File content:"
cat "$filename"
echo "Number of attempts: $attempts"

