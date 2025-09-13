# CyberPanel File Manager API Documentation

## Base Configuration
- **Base URL**: `https://your-server.com/cloudAPI/`
- **Method**: POST
- **Content-Type**: application/json
- **Authentication**: Basic Auth with API token

## Common Headers
```bash
Authorization: Basic your_api_token
Content-Type: application/json
```

## Common Request Format
```json
{
  "serverUserName": "admin",
  "controller": "endpoint_name",
  "domainName": "example.com",
  "token": "your_api_token"
}
```

---

## 📁 File Operations

### 1. List Files
**Endpoint**: `listFiles`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "listFiles",
    "domainName": "example.com",
    "path": "/home/example.com/public_html"
  }'
```

### 2. List Files for Table
**Endpoint**: `listFilesForTable`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "listFilesForTable",
    "domainName": "example.com",
    "path": "/home/example.com/public_html"
  }'
```

### 3. Create File
**Endpoint**: `createNewFile`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "createNewFile",
    "domainName": "example.com",
    "fileName": "newfile.txt",
    "path": "/home/example.com/public_html"
  }'
```

### 4. Create Folder
**Endpoint**: `createNewFolder`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "createNewFolder",
    "domainName": "example.com",
    "folderName": "newfolder",
    "path": "/home/example.com/public_html"
  }'
```

---

## 📝 File Content Operations

### 5. Read File
**Endpoint**: `readFileContents`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "readFileContents",
    "domainName": "example.com",
    "fileName": "file.txt",
    "path": "/home/example.com/public_html"
  }'
```

### 6. Write File
**Endpoint**: `writeFileContents`

#### Standard Request
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "writeFileContents",
    "domainName": "example.com",
    "fileName": "/home/example.com/public_html/file.txt",
    "fileContent": "File content here"
  }'
```

#### Base64 Encoded Request (for HTML with special characters)
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "writeFileContents",
    "domainName": "example.com",
    "fileName": "/home/example.com/public_html/index.html",
    "fileContent": "PGh0bWw+PGJvZHk+PGgxPkhlbGxvPC9oMT48L2JvZHk+PC9odG1sPg==",
    "isBase64": true
  }'
```

### 7. Upload File
**Endpoint**: `uploadFile`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "uploadFile",
    "domainName": "example.com",
    "path": "/home/example.com/public_html",
    "file": "base64_encoded_content"
  }'
```

---

## 🗂️ File Management

### 8. Copy File/Folder
**Endpoint**: `copyFile`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "copyFile",
    "domainName": "example.com",
    "fileName": "source.txt",
    "path": "/home/example.com/public_html",
    "destinationPath": "/home/example.com/backup/"
  }'
```

### 9. Move File/Folder
**Endpoint**: `moveFile`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "moveFile",
    "domainName": "example.com",
    "fileName": "file.txt",
    "path": "/home/example.com/public_html",
    "destinationPath": "/home/example.com/moved/"
  }'
```

### 10. Rename File/Folder
**Endpoint**: `renameFile`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "renameFile",
    "domainName": "example.com",
    "fileName": "oldname.txt",
    "newFileName": "newname.txt",
    "path": "/home/example.com/public_html"
  }'
```

---

## 🗑️ Delete & Trash Operations

### 11. Delete File/Folder (Move to Trash)
**Endpoint**: `deleteFolderOrFile`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "deleteFolderOrFile",
    "domainName": "example.com",
    "path": "/home/example.com/public_html",
    "fileAndFolders": ["file1.txt", "folder1"]
  }'
```

### 12. Permanent Delete
**Endpoint**: `deleteFolderOrFile` (with skipTrash)
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "deleteFolderOrFile",
    "domainName": "example.com",
    "path": "/home/example.com/public_html",
    "fileAndFolders": ["sensitive_file.txt"],
    "skipTrash": true
  }'
```

### 13. Restore from Trash
**Endpoint**: `restoreFile`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "restoreFile",
    "domainName": "example.com",
    "fileAndFolders": ["deleted_file.txt"]
  }'
```

### 14. Get Trash Contents
**Endpoint**: `getTrashContents`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "getTrashContents",
    "domainName": "example.com"
  }'
```

### 15. Empty Trash
**Endpoint**: `emptyTrash`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "emptyTrash",
    "domainName": "example.com"
  }'
```

---

## 📦 Archive Operations

### 16. Compress Files
**Endpoint**: `compressFiles`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "compressFiles",
    "domainName": "example.com",
    "fileName": "archive.zip",
    "path": "/home/example.com/public_html",
    "files": ["file1.txt", "file2.txt"]
  }'
```

### 17. Extract Archive
**Endpoint**: `extractArchive`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "extractArchive",
    "domainName": "example.com",
    "fileName": "archive.zip",
    "path": "/home/example.com/public_html"
  }'
```

---

## 🔍 Advanced Operations

### 18. Search Files
**Endpoint**: `searchFiles`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "searchFiles",
    "domainName": "example.com",
    "searchPath": "/home/example.com/public_html",
    "searchTerm": "index",
    "searchType": "all"
  }'
```

### 19. Get File Info
**Endpoint**: `getFileInfo`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "getFileInfo",
    "domainName": "example.com",
    "filePath": "/home/example.com/public_html/file.txt"
  }'
```

### 20. Download File
**Endpoint**: `downloadFile`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "downloadFile",
    "domainName": "example.com",
    "filePath": "/home/example.com/public_html/file.txt"
  }'
```

---

## 🔐 Permission Operations

### 21. Change File Permissions
**Endpoint**: `changeFilePermissions`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "changeFilePermissions",
    "domainName": "example.com",
    "fileName": "file.txt",
    "path": "/home/example.com/public_html",
    "permissions": "644"
  }'
```

### 22. Fix File Permissions
**Endpoint**: `fixFilePermissions`
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "fixFilePermissions",
    "domainName": "example.com"
  }'
```

---

## 📊 Response Format

### Success Response
```json
{
  "status": 1,
  "data": "response_data_here"
}
```

### Error Response
```json
{
  "status": 0,
  "error_message": "Error description"
}
```

---

## 🔧 Integration Examples

### Complete File Management Workflow
```bash
# 1. List files
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "listFiles", "domainName": "example.com", "path": "/home/example.com/public_html"}'

# 2. Create a file
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "createNewFile", "domainName": "example.com", "fileName": "test.txt", "path": "/home/example.com/public_html"}'

# 3. Write content
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "writeFileContents", "domainName": "example.com", "fileName": "/home/example.com/public_html/test.txt", "fileContent": "Hello World!"}'

# 4. Read content
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "readFileContents", "domainName": "example.com", "fileName": "test.txt", "path": "/home/example.com/public_html"}'

# 5. Delete file
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "deleteFolderOrFile", "domainName": "example.com", "path": "/home/example.com/public_html", "fileAndFolders": ["test.txt"]}'
```

---

## 📋 Parameter Reference

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serverUserName` | string | Yes | Admin username (usually "admin") |
| `controller` | string | Yes | API endpoint name |
| `domainName` | string | Yes* | Domain name (*required for most operations) |
| `path` | string | Yes* | Directory path (*required for most operations) |
| `fileName` | string | Yes* | File name (*required for file operations) |
| `folderName` | string | Yes* | Folder name (*required for folder operations) |
| `fileAndFolders` | array | Yes* | Array of file/folder names (*required for delete/restore) |
| `fileContent` | string | No | File content for write operations |
| `isBase64` | boolean | No | Set to true if fileContent is base64 encoded |
| `destinationPath` | string | No | Destination path for copy/move operations |
| `newFileName` | string | No | New name for rename operations |
| `permissions` | string | No | File permissions (e.g., "644") |
| `skipTrash` | boolean | No | Skip trash for permanent delete (default: false) |
| `searchTerm` | string | No | Search term for file search |
| `searchType` | string | No | Search type: "all", "files", "folders" |
| `filePath` | string | No | Full file path for info/download operations |

---

## 🚨 Important Notes

1. **Authentication**: All requests require valid API token
2. **Path Security**: All paths are validated to prevent directory traversal
3. **Domain Ownership**: Users can only access files within their domains
4. **File Names**: Use only file names in arrays, not full paths
5. **Trash System**: Deleted files are moved to trash unless `skipTrash: true`
6. **Error Handling**: Always check `status` field in responses
7. **Rate Limiting**: Implement appropriate delays between requests

---

## 📚 Response Examples

### List Files Response
```json
{
  "status": 1,
  "0": ["app", "/home/example.com/public_html/app", true],
  "1": ["index.html", "/home/example.com/public_html/index.html", false]
}
```

### List Files for Table Response
```json
{
  "status": 1,
  "0": ["app", "app", "Apr 2 18:49", "4", "drwxr-xr-x", 1],
  "1": ["index.html", "index.html", "Jul 4 10:20", "1", "-rw-r--r--", 0]
}
```

### File Info Response
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
    "is_directory": false,
    "is_file": true
  }
}
```

### Search Files Response
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

### Trash Contents Response
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