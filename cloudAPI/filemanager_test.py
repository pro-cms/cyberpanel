#!/usr/bin/env python3
"""
Simple File Manager API Test Script

Usage:
    python3 filemanager_test.py
"""

import requests
import json

def test_file_manager_api():
    """Test basic file manager API functionality"""
    
    # Configuration
    SERVER_URL = "https://your-cyberpanel-server.com"
    USERNAME = "admin"
    TOKEN = "your_api_token_here"
    DOMAIN = "example.com"
    
    api_url = f"{SERVER_URL}/cloudAPI/"
    
    def make_request(controller, **kwargs):
        """Make API request"""
        data = {
            "controller": controller,
            "serverUserName": USERNAME,
            "token": TOKEN,
            "domainName": DOMAIN,
            **kwargs
        }
        
        try:
            response = requests.post(
                api_url,
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            return response.json()
        except Exception as e:
            print(f"Request failed: {e}")
            return None
    
    print("=== File Manager API Test ===")
    
    # Test 1: List files
    print("\n1. Testing listFiles...")
    response = make_request("listFiles", path=f"/home/{DOMAIN}/public_html")
    print(f"Response: {response}")
    
    # Test 2: Create a file
    print("\n2. Testing createNewFile...")
    response = make_request("createNewFile", fileName="test_api.txt", path=f"/home/{DOMAIN}/public_html")
    print(f"Response: {response}")
    
    # Test 3: Write to file
    print("\n3. Testing writeFileContents...")
    response = make_request(
        "writeFileContents", 
        fileName="test_api.txt", 
        path=f"/home/{DOMAIN}/public_html",
        fileContents="Hello from API test!"
    )
    print(f"Response: {response}")
    
    # Test 4: Read file
    print("\n4. Testing readFileContents...")
    response = make_request("readFileContents", fileName="test_api.txt", path=f"/home/{DOMAIN}/public_html")
    print(f"Response: {response}")
    
    # Test 5: Get file info
    print("\n5. Testing getFileInfo...")
    response = make_request("getFileInfo", filePath=f"/home/{DOMAIN}/public_html/test_api.txt")
    print(f"Response: {response}")
    
    # Test 6: Delete file
    print("\n6. Testing deleteFolderOrFile...")
    response = make_request("deleteFolderOrFile", fileName="test_api.txt", path=f"/home/{DOMAIN}/public_html")
    print(f"Response: {response}")
    
    print("\n=== Test completed ===")

if __name__ == "__main__":
    test_file_manager_api()
