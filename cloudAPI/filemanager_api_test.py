#!/usr/bin/env python3
"""
File Manager API Test Script

This script demonstrates how to use the File Manager API endpoints
in CyberPanel. It provides examples of common file operations.

Usage:
    python3 filemanager_api_test.py

Requirements:
    - requests library: pip install requests
    - Valid CyberPanel API credentials
"""

import requests
import json
import base64
import os
from datetime import datetime

class CyberPanelFileManagerAPI:
    def __init__(self, server_url, username, token, domain):
        """
        Initialize the API client
        
        Args:
            server_url (str): CyberPanel server URL (e.g., https://your-server.com)
            username (str): Admin username
            token (str): API token
            domain (str): Domain name to work with
        """
        self.server_url = server_url.rstrip('/')
        self.username = username
        self.token = token
        self.domain = domain
        self.api_url = f"{self.server_url}/cloudAPI/"
        
    def _make_request(self, controller, **kwargs):
        """
        Make a request to the CyberPanel API
        
        Args:
            controller (str): API controller name
            **kwargs: Additional parameters for the request
            
        Returns:
            dict: API response
        """
        data = {
            "controller": controller,
            "serverUserName": self.username,
            "token": self.token,
            "domainName": self.domain,
            **kwargs
        }
        
        try:
            response = requests.post(
                self.api_url,
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
    
    def list_files(self, path="/home/example.com/public_html"):
        """List files in a directory"""
        print(f"\n=== Listing files in {path} ===")
        response = self._make_request("listFiles", path=path)
        if response and response.get('status') == 1:
            print("Files found:")
            for item in response.get('data', []):
                print(f"  - {item['name']} ({item['type']}) - {item['size']}")
        else:
            print(f"Failed to list files: {response}")
        return response
    
    def create_file(self, filename, path="/home/example.com/public_html"):
        """Create a new file"""
        print(f"\n=== Creating file {filename} ===")
        response = self._make_request("createNewFile", fileName=filename, path=path)
        if response and response.get('status') == 1:
            print(f"File {filename} created successfully")
        else:
            print(f"Failed to create file: {response}")
        return response
    
    def write_file(self, filename, content, path="/home/example.com/public_html"):
        """Write content to a file"""
        print(f"\n=== Writing content to {filename} ===")
        response = self._make_request(
            "writeFileContents", 
            fileName=filename, 
            path=path, 
            fileContents=content
        )
        if response and response.get('status') == 1:
            print(f"Content written to {filename} successfully")
        else:
            print(f"Failed to write file: {response}")
        return response
    
    def read_file(self, filename, path="/home/example.com/public_html"):
        """Read content from a file"""
        print(f"\n=== Reading content from {filename} ===")
        response = self._make_request("readFileContents", fileName=filename, path=path)
        if response and response.get('status') == 1:
            content = response.get('fileContents', '')
            print(f"File content:\n{content}")
        else:
            print(f"Failed to read file: {response}")
        return response
    
    def create_folder(self, foldername, path="/home/example.com/public_html"):
        """Create a new folder"""
        print(f"\n=== Creating folder {foldername} ===")
        response = self._make_request("createNewFolder", folderName=foldername, path=path)
        if response and response.get('status') == 1:
            print(f"Folder {foldername} created successfully")
        else:
            print(f"Failed to create folder: {response}")
        return response
    
    def copy_file(self, filename, destination_path, source_path="/home/example.com/public_html"):
        """Copy a file to a new location"""
        print(f"\n=== Copying {filename} to {destination_path} ===")
        response = self._make_request(
            "copyFile", 
            fileName=filename, 
            path=source_path, 
            destinationPath=destination_path
        )
        if response and response.get('status') == 1:
            print(f"File {filename} copied successfully")
        else:
            print(f"Failed to copy file: {response}")
        return response
    
    def move_file(self, filename, destination_path, source_path="/home/example.com/public_html"):
        """Move a file to a new location"""
        print(f"\n=== Moving {filename} to {destination_path} ===")
        response = self._make_request(
            "moveFile", 
            fileName=filename, 
            path=source_path, 
            destinationPath=destination_path
        )
        if response and response.get('status') == 1:
            print(f"File {filename} moved successfully")
        else:
            print(f"Failed to move file: {response}")
        return response
    
    def rename_file(self, old_name, new_name, path="/home/example.com/public_html"):
        """Rename a file"""
        print(f"\n=== Renaming {old_name} to {new_name} ===")
        response = self._make_request(
            "renameFile", 
            fileName=old_name, 
            newFileName=new_name, 
            path=path
        )
        if response and response.get('status') == 1:
            print(f"File renamed from {old_name} to {new_name} successfully")
        else:
            print(f"Failed to rename file: {response}")
        return response
    
    def delete_file(self, filename, path="/home/example.com/public_html"):
        """Delete a file (moves to trash)"""
        print(f"\n=== Deleting {filename} ===")
        response = self._make_request("deleteFolderOrFile", fileName=filename, path=path)
        if response and response.get('status') == 1:
            print(f"File {filename} deleted successfully (moved to trash)")
        else:
            print(f"Failed to delete file: {response}")
        return response
    
    def get_file_info(self, filepath):
        """Get detailed information about a file"""
        print(f"\n=== Getting file info for {filepath} ===")
        response = self._make_request("getFileInfo", filePath=filepath)
        if response and response.get('status') == 1:
            file_info = response.get('file_info', {})
            print(f"File: {file_info.get('name')}")
            print(f"Size: {file_info.get('size_human')}")
            print(f"Permissions: {file_info.get('permissions')}")
            print(f"Modified: {file_info.get('modified')}")
            print(f"Type: {'Directory' if file_info.get('is_directory') else 'File'}")
        else:
            print(f"Failed to get file info: {response}")
        return response
    
    def search_files(self, search_term, search_path="/home/example.com/public_html", search_type="all"):
        """Search for files"""
        print(f"\n=== Searching for '{search_term}' in {search_path} ===")
        response = self._make_request(
            "searchFiles", 
            searchPath=search_path, 
            searchTerm=search_term, 
            searchType=search_type
        )
        if response and response.get('status') == 1:
            results = response.get('results', [])
            print(f"Found {len(results)} results:")
            for result in results:
                print(f"  - {result['name']} ({result['path']})")
        else:
            print(f"Failed to search files: {response}")
        return response
    
    def get_trash_contents(self):
        """Get contents of trash"""
        print(f"\n=== Getting trash contents ===")
        response = self._make_request("getTrashContents")
        if response and response.get('status') == 1:
            trash_items = response.get('trash_items', [])
            print(f"Found {len(trash_items)} items in trash:")
            for item in trash_items:
                print(f"  - {item['fileName']} (was at {item['originalPath']})")
        else:
            print(f"Failed to get trash contents: {response}")
        return response
    
    def restore_file(self, filename):
        """Restore a file from trash"""
        print(f"\n=== Restoring {filename} from trash ===")
        response = self._make_request("restoreFile", fileName=filename)
        if response and response.get('status') == 1:
            print(f"File {filename} restored successfully")
        else:
            print(f"Failed to restore file: {response}")
        return response
    
    def empty_trash(self):
        """Empty the trash"""
        print(f"\n=== Emptying trash ===")
        response = self._make_request("emptyTrash")
        if response and response.get('status') == 1:
            print("Trash emptied successfully")
        else:
            print(f"Failed to empty trash: {response}")
        return response
    
    def change_permissions(self, filename, permissions, path="/home/example.com/public_html"):
        """Change file permissions"""
        print(f"\n=== Changing permissions for {filename} to {permissions} ===")
        response = self._make_request(
            "changeFilePermissions", 
            fileName=filename, 
            path=path, 
            permissions=permissions
        )
        if response and response.get('status') == 1:
            print(f"Permissions changed for {filename} successfully")
        else:
            print(f"Failed to change permissions: {response}")
        return response
    
    def compress_files(self, archive_name, files, path="/home/example.com/public_html"):
        """Compress files into an archive"""
        print(f"\n=== Compressing files into {archive_name} ===")
        response = self._make_request(
            "compressFiles", 
            fileName=archive_name, 
            path=path, 
            files=files
        )
        if response and response.get('status') == 1:
            print(f"Files compressed into {archive_name} successfully")
        else:
            print(f"Failed to compress files: {response}")
        return response
    
    def extract_archive(self, filename, path="/home/example.com/public_html"):
        """Extract an archive file"""
        print(f"\n=== Extracting {filename} ===")
        response = self._make_request("extractArchive", fileName=filename, path=path)
        if response and response.get('status') == 1:
            print(f"Archive {filename} extracted successfully")
        else:
            print(f"Failed to extract archive: {response}")
        return response

def main():
    """Main function to demonstrate API usage"""
    
    # Configuration - Update these values
    SERVER_URL = "https://your-cyberpanel-server.com"
    USERNAME = "admin"
    TOKEN = "your_api_token_here"
    DOMAIN = "example.com"
    
    # Create API client
    api = CyberPanelFileManagerAPI(SERVER_URL, USERNAME, TOKEN, DOMAIN)
    
    # Update paths to use the actual domain
    base_path = f"/home/{DOMAIN}/public_html"
    
    print("=== CyberPanel File Manager API Test ===")
    print(f"Server: {SERVER_URL}")
    print(f"Domain: {DOMAIN}")
    print(f"Base Path: {base_path}")
    
    try:
        # Test basic file operations
        print("\n" + "="*50)
        print("TESTING BASIC FILE OPERATIONS")
        print("="*50)
        
        # 1. List files
        api.list_files(base_path)
        
        # 2. Create a test file
        test_filename = f"test_file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        api.create_file(test_filename, base_path)
        
        # 3. Write content to the file
        test_content = f"""This is a test file created by the API at {datetime.now()}.
        
This file contains:
- Multiple lines
- Special characters: !@#$%^&*()
- Numbers: 1234567890
- Unicode: ñáéíóú

End of test content."""
        api.write_file(test_filename, test_content, base_path)
        
        # 4. Read the file back
        api.read_file(test_filename, base_path)
        
        # 5. Get file information
        api.get_file_info(f"{base_path}/{test_filename}")
        
        # 6. Create a test folder
        test_folder = f"test_folder_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        api.create_folder(test_folder, base_path)
        
        # 7. Copy the file to the new folder
        api.copy_file(test_filename, f"{base_path}/{test_folder}/", base_path)
        
        # 8. List files in the new folder
        api.list_files(f"{base_path}/{test_folder}")
        
        # 9. Rename the copied file
        new_filename = f"renamed_{test_filename}"
        api.rename_file(test_filename, new_filename, f"{base_path}/{test_folder}")
        
        # 10. Move the renamed file back to the main directory
        api.move_file(new_filename, base_path, f"{base_path}/{test_folder}")
        
        # 11. Search for files
        api.search_files("test", base_path)
        
        # 12. Change file permissions
        api.change_permissions(test_filename, "644", base_path)
        
        # Test trash operations
        print("\n" + "="*50)
        print("TESTING TRASH OPERATIONS")
        print("="*50)
        
        # 13. Delete the test file (moves to trash)
        api.delete_file(test_filename, base_path)
        
        # 14. Check trash contents
        api.get_trash_contents()
        
        # 15. Restore the file from trash
        api.restore_file(test_filename)
        
        # 16. List files again to confirm restoration
        api.list_files(base_path)
        
        # Test archive operations
        print("\n" + "="*50)
        print("TESTING ARCHIVE OPERATIONS")
        print("="*50)
        
        # 17. Create another test file for compression
        test_file2 = f"test_file2_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        api.create_file(test_file2, base_path)
        api.write_file(test_file2, "This is test file 2 content", base_path)
        
        # 18. Compress files
        archive_name = f"test_archive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        files_to_compress = [test_filename, test_file2]
        api.compress_files(archive_name, files_to_compress, base_path)
        
        # 19. List files to see the archive
        api.list_files(base_path)
        
        # 20. Extract the archive
        api.extract_archive(archive_name, base_path)
        
        # 21. List files after extraction
        api.list_files(base_path)
        
        # Cleanup
        print("\n" + "="*50)
        print("CLEANUP")
        print("="*50)
        
        # Delete test files
        api.delete_file(test_filename, base_path)
        api.delete_file(test_file2, base_path)
        api.delete_file(archive_name, base_path)
        api.delete_file(test_folder, base_path)
        
        # Empty trash
        api.empty_trash()
        
        print("\n=== Test completed successfully! ===")
        
    except Exception as e:
        print(f"\nError during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
