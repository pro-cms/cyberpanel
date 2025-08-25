# File Manager API Documentation

This document provides comprehensive documentation for the File Manager API endpoints in CyberPanel.

## Authentication

All API requests require authentication using the following headers:
- `Authorization`: Bearer token
- `Content-Type`: application/json

## Base URL
```
POST /cloudAPI/
```

## Common Request Format
```json
{
  "controller": "endpoint_name",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  ...other_parameters
}
```

## Endpoints

### 1. List Files for Table Display
**Endpoint:** `listFilesForTable`

Lists files and folders in a format suitable for table display.

**Request:**
```json
{
  "controller": "listFilesForTable",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "path": "/home/example.com/public_html"
}
```

**Response:**
```json
{
  "status": 1,
  "data": [
    {
      "name": "index.html",
      "path": "/home/example.com/public_html/index.html",
      "size": "1.2 KB",
      "type": "file",
      "permissions": "644",
      "modified": "2024-01-15T10:30:00Z"
    }
  ]
}
```

### 2. List Files
**Endpoint:** `listFiles`

Lists files and folders in a directory.

**Request:**
```json
{
  "controller": "listFiles",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "path": "/home/example.com/public_html"
}
```

### 3. Create New File
**Endpoint:** `createNewFile`

Creates a new file.

**Request:**
```json
{
  "controller": "createNewFile",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "newfile.txt",
  "path": "/home/example.com/public_html"
}
```

### 4. Create New Folder
**Endpoint:** `createNewFolder`

Creates a new folder/directory.

**Request:**
```json
{
  "controller": "createNewFolder",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "folderName": "newfolder",
  "path": "/home/example.com/public_html"
}
```

### 5. Delete File or Folder
**Endpoint:** `deleteFolderOrFile`

Deletes a file or folder (moves to trash).

**Request:**
```json
{
  "controller": "deleteFolderOrFile",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "file_to_delete.txt",
  "path": "/home/example.com/public_html"
}
```

### 6. Restore File from Trash
**Endpoint:** `restoreFile`

Restores a file from the trash.

**Request:**
```json
{
  "controller": "restoreFile",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "restored_file.txt"
}
```

### 7. Copy File or Folder
**Endpoint:** `copyFile`

Copies a file or folder to a new location.

**Request:**
```json
{
  "controller": "copyFile",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "source_file.txt",
  "path": "/home/example.com/public_html",
  "destinationPath": "/home/example.com/public_html/backup/"
}
```

### 8. Move File or Folder
**Endpoint:** `moveFile`

Moves a file or folder to a new location.

**Request:**
```json
{
  "controller": "moveFile",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "file_to_move.txt",
  "path": "/home/example.com/public_html",
  "destinationPath": "/home/example.com/public_html/moved/"
}
```

### 9. Rename File or Folder
**Endpoint:** `renameFile`

Renames a file or folder.

**Request:**
```json
{
  "controller": "renameFile",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "old_name.txt",
  "newFileName": "new_name.txt",
  "path": "/home/example.com/public_html"
}
```

### 10. Read File Contents
**Endpoint:** `readFileContents`

Reads the contents of a file.

**Request:**
```json
{
  "controller": "readFileContents",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "file_to_read.txt",
  "path": "/home/example.com/public_html"
}
```

**Response:**
```json
{
  "status": 1,
  "fileContents": "File content here...",
  "fileName": "file_to_read.txt"
}
```

### 11. Write File Contents
**Endpoint:** `writeFileContents`

Writes content to a file.

**Request:**
```json
{
  "controller": "writeFileContents",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "file_to_write.txt",
  "path": "/home/example.com/public_html",
  "fileContents": "New file content here..."
}
```

### 12. Upload File
**Endpoint:** `uploadFile`

Uploads a file to the server.

**Request:**
```json
{
  "controller": "uploadFile",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "path": "/home/example.com/public_html",
  "file": "base64_encoded_file_content"
}
```

### 13. Extract Archive
**Endpoint:** `extractArchive`

Extracts an archive file (zip, tar, etc.).

**Request:**
```json
{
  "controller": "extractArchive",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "archive.zip",
  "path": "/home/example.com/public_html"
}
```

### 14. Compress Files
**Endpoint:** `compressFiles`

Compresses files into an archive.

**Request:**
```json
{
  "controller": "compressFiles",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "compressed.zip",
  "path": "/home/example.com/public_html",
  "files": ["file1.txt", "file2.txt"]
}
```

### 15. Change File Permissions
**Endpoint:** `changeFilePermissions`

Changes file permissions.

**Request:**
```json
{
  "controller": "changeFilePermissions",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "fileName": "file.txt",
  "path": "/home/example.com/public_html",
  "permissions": "644"
}
```

### 16. Fix File Permissions
**Endpoint:** `fixFilePermissions`

Fixes file permissions for an entire domain.

**Request:**
```json
{
  "controller": "fixFilePermissions",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com"
}
```

### 17. Download File
**Endpoint:** `downloadFile`

Downloads a file from the server.

**Request:**
```json
{
  "controller": "downloadFile",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "filePath": "/home/example.com/public_html/file.txt"
}
```

### 18. Get File Information
**Endpoint:** `getFileInfo`

Gets detailed information about a file.

**Request:**
```json
{
  "controller": "getFileInfo",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "filePath": "/home/example.com/public_html/file.txt"
}
```

**Response:**
```json
{
  "status": 1,
  "file_info": {
    "name": "file.txt",
    "path": "/home/example.com/public_html/file.txt",
    "size": 1024,
    "size_human": "1.0 KB",
    "permissions": "644",
    "owner": 1000,
    "group": 1000,
    "created": "2024-01-15T10:30:00Z",
    "modified": "2024-01-15T10:30:00Z",
    "accessed": "2024-01-15T10:30:00Z",
    "is_directory": false,
    "is_file": true,
    "is_symlink": false,
    "readable": true,
    "writable": true,
    "executable": false
  }
}
```

### 19. Search Files
**Endpoint:** `searchFiles`

Searches for files and folders.

**Request:**
```json
{
  "controller": "searchFiles",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com",
  "searchPath": "/home/example.com/public_html",
  "searchTerm": "index",
  "searchType": "all"
}
```

**Parameters:**
- `searchType`: "all", "files", or "folders"

**Response:**
```json
{
  "status": 1,
  "results": [
    {
      "name": "index.html",
      "path": "/home/example.com/public_html/index.html",
      "size": 1024,
      "size_human": "1.0 KB",
      "is_directory": false,
      "modified": "2024-01-15T10:30:00Z"
    }
  ],
  "count": 1
}
```

### 20. Get Trash Contents
**Endpoint:** `getTrashContents`

Gets the contents of the trash for a domain.

**Request:**
```json
{
  "controller": "getTrashContents",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com"
}
```

**Response:**
```json
{
  "status": 1,
  "trash_items": [
    {
      "id": 1,
      "fileName": "deleted_file.txt",
      "originalPath": "/home/example.com/public_html/deleted_file.txt",
      "deleted_date": 1
    }
  ],
  "count": 1
}
```

### 21. Empty Trash
**Endpoint:** `emptyTrash`

Empties the trash for a domain.

**Request:**
```json
{
  "controller": "emptyTrash",
  "serverUserName": "admin",
  "token": "your_api_token",
  "domainName": "example.com"
}
```

**Response:**
```json
{
  "status": 1,
  "message": "Trash emptied successfully"
}
```

## Error Responses

All endpoints return error responses in the following format:

```json
{
  "status": 0,
  "error_message": "Description of the error"
}
```

## Common Error Codes

- `0`: General error
- `404`: File not found
- `403`: Permission denied
- `401`: Unauthorized access

## Security Considerations

1. **Path Validation**: All file paths are validated to prevent directory traversal attacks
2. **Domain Ownership**: Users can only access files within domains they own
3. **Permission Checks**: File operations respect file system permissions
4. **Token Authentication**: All requests require valid API tokens

## Rate Limiting

The API implements rate limiting to prevent abuse. Please implement appropriate delays between requests in your applications.

## File Size Limits

- Maximum file upload size: 100MB (configurable)
- Maximum file read size: 10MB (for text files)
- Archive extraction: Limited by available disk space

## Supported File Types

### Text Files
- .txt, .html, .css, .js, .php, .py, .java, .xml, .json, .md

### Archive Files
- .zip, .tar, .tar.gz, .tar.bz2, .rar

### Image Files
- .jpg, .jpeg, .png, .gif, .bmp, .svg

### Document Files
- .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx

## Examples

### Complete File Management Workflow

1. **List files in a directory:**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "controller": "listFiles",
    "serverUserName": "admin",
    "token": "your_token",
    "domainName": "example.com",
    "path": "/home/example.com/public_html"
  }'
```

2. **Create a new file:**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "controller": "createNewFile",
    "serverUserName": "admin",
    "token": "your_token",
    "domainName": "example.com",
    "fileName": "test.txt",
    "path": "/home/example.com/public_html"
  }'
```

3. **Write content to the file:**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "controller": "writeFileContents",
    "serverUserName": "admin",
    "token": "your_token",
    "domainName": "example.com",
    "fileName": "test.txt",
    "path": "/home/example.com/public_html",
    "fileContents": "Hello, World!"
  }'
```

4. **Read the file contents:**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "controller": "readFileContents",
    "serverUserName": "admin",
    "token": "your_token",
    "domainName": "example.com",
    "fileName": "test.txt",
    "path": "/home/example.com/public_html"
  }'
```

## Notes

- All file paths should be absolute paths
- File operations are performed as the domain's user account
- The API automatically handles file permissions and ownership
- Large file operations may take time to complete
- Always check the response status before proceeding with subsequent operations
