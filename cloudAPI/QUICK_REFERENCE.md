# CyberPanel File Manager API - Quick Reference

## 🚀 Quick Start

**Base URL**: `https://your-server.com/cloudAPI/`
**Method**: POST
**Content-Type**: application/json

## 📋 All Endpoints

| # | Endpoint | Purpose | Key Parameters |
|---|----------|---------|----------------|
| 1 | `listFiles` | List files/folders | `path` |
| 2 | `listFilesForTable` | List for table display | `path` |
| 3 | `createNewFile` | Create file | `fileName`, `path` |
| 4 | `createNewFolder` | Create folder | `folderName`, `path` |
| 5 | `readFileContents` | Read file content | `fileName`, `path` |
| 6 | `writeFileContents` | Write file content | `fileName` (full path), `fileContent` |
| 7 | `uploadFile` | Upload file | `path`, `file` |
| 8 | `copyFile` | Copy file/folder | `fileName`, `path`, `destinationPath` |
| 9 | `moveFile` | Move file/folder | `fileName`, `path`, `destinationPath` |
| 10 | `renameFile` | Rename file/folder | `fileName`, `newFileName`, `path` |
| 11 | `deleteFolderOrFile` | Delete (to trash) | `fileAndFolders`, `path` |
| 12 | `deleteFolderOrFile` | Permanent delete | `fileAndFolders`, `path`, `skipTrash: true` |
| 13 | `restoreFile` | Restore from trash | `fileAndFolders` |
| 14 | `getTrashContents` | List trash items | - |
| 15 | `emptyTrash` | Empty trash | - |
| 16 | `compressFiles` | Create archive | `fileName`, `path`, `files` |
| 17 | `extractArchive` | Extract archive | `fileName`, `path` |
| 18 | `searchFiles` | Search files | `searchPath`, `searchTerm`, `searchType` |
| 19 | `getFileInfo` | Get file details | `filePath` |
| 20 | `downloadFile` | Download file | `filePath` |
| 21 | `changeFilePermissions` | Change permissions | `fileName`, `path`, `permissions` |
| 22 | `fixFilePermissions` | Fix all permissions | - |

## 🔧 Common Request Template

```json
{
  "serverUserName": "admin",
  "controller": "endpoint_name",
  "domainName": "example.com",
  "path": "/home/example.com/public_html",
  "token": "your_api_token"
}
```

## 📊 Response Format

**Success**: `{"status": 1, "data": "..."}`
**Error**: `{"status": 0, "error_message": "..."}`

## 🎯 Common Use Cases

### Create & Write File
```bash
# Create
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "createNewFile", "domainName": "example.com", "fileName": "test.txt", "path": "/home/example.com/public_html"}'

# Write
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "writeFileContents", "domainName": "example.com", "fileName": "/home/example.com/public_html/test.txt", "fileContent": "Hello World!"}'
```

### Delete & Restore
```bash
# Delete (to trash)
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "deleteFolderOrFile", "domainName": "example.com", "path": "/home/example.com/public_html", "fileAndFolders": ["test.txt"]}'

# Restore
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "restoreFile", "domainName": "example.com", "fileAndFolders": ["test.txt"]}'
```

### Search Files
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{"serverUserName": "admin", "controller": "searchFiles", "domainName": "example.com", "searchPath": "/home/example.com/public_html", "searchTerm": "index", "searchType": "all"}'
```

## ⚠️ Important Notes

- Always include `serverUserName: "admin"`
- Use `domainName` for domain-specific operations
- `fileAndFolders` expects array of file names (not full paths)
- Check `status` field in all responses
- Deleted files go to trash unless `skipTrash: true`

## 🔗 Full Documentation

See `cloudAPI/file-manager.md` for complete documentation with examples.
