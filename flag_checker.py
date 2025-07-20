import os
import hashlib
import zipfile
import tarfile
import re

def check_file(filepath):
    """
    CTF flag checker that validates files based on metadata timing requirements.
    Only returns flag if there are exactly 3 metadata entries with timing "2023:01:01 00:00:00"
    """
    try:
        # Read file content
        with open(filepath, 'rb') as f:
            content = f.read()
        
        # Convert to text for analysis
        try:
            text_content = content.decode('utf-8', errors='ignore')
        except:
            text_content = str(content)
        
        # Check for metadata with specific timing pattern
        timing_pattern = r'2023:01:01 00:00:00'
        timing_matches = re.findall(timing_pattern, text_content)
        
        # Count exact matches
        exact_count = len(timing_matches)
        
        if exact_count == 3:
            # Exactly 3 metadata entries with the required timing - return flag
            return 'CTF{3_perfect_timestamps_found}'
        elif exact_count > 3:
            # More than 3 - ask to try again
            raise Exception(f"Found {exact_count} metadata entries with timing 2023:01:01 00:00:00. Need exactly 3. Please try again.")
        elif exact_count > 0 and exact_count < 3:
            # Less than 3 but some found - ask to try again
            raise Exception(f"Found only {exact_count} metadata entries with timing 2023:01:01 00:00:00. Need exactly 3. Please try again.")
        else:
            # No timing metadata found - ask to try again
            raise Exception("No metadata entries with timing 2023:01:01 00:00:00 found. Need exactly 3. Please try again.")
        
    except Exception as e:
        # Re-raise the exception so it gets displayed as an error message
        raise e
