# Change File Permissions API Documentation

## Overview

The `changeFilePermissions` API endpoint allows you to change file and directory permissions for files within a website's directory structure. This is different from `fixFilePermissions` which applies standard permissions to an entire domain.

## API Endpoint

**URL:** `https://your-domain.com:8090/cloudAPI/`  
**Method:** `POST`  
**Content-Type:** `application/json`

## Authentication

Include your API token in the Authorization header:
```
Authorization: YOUR_API_TOKEN
```

## Request Parameters

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `controller` | string | Must be `"changeFilePermissions"` |
| `serverUserName` | string | CyberPanel username (usually "admin") |
| `domainName` | string | Domain name that owns the file/directory |
| `basePath` | string | Base directory path (usually `/home/domain.com/public_html`) |
| `permissionsPath` | string | Relative path to the file/directory from basePath |
| `newPermissions` | string | New permissions in octal format (e.g., "755", "644") |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `recursive` | integer | 0 | Set to 1 to apply permissions recursively to subdirectories |

## Permission Values

### Common Permission Combinations

| Octal | Binary | Permissions | Description |
|-------|--------|-------------|-------------|
| 755 | rwxr-xr-x | Owner: read/write/execute, Group & Others: read/execute | Standard for directories |
| 644 | rw-r--r-- | Owner: read/write, Group & Others: read only | Standard for files |
| 600 | rw------- | Owner: read/write, Group & Others: no access | Private files |
| 777 | rwxrwxrwx | Full permissions for everyone | **Not recommended** |
| 700 | rwx------ | Owner: full access, Group & Others: no access | Private directories |

### Permission Breakdown

Each digit represents permissions for:
1. **First digit**: Owner (user) permissions
2. **Second digit**: Group permissions  
3. **Third digit**: Other (world) permissions

Each digit is calculated as:
- **4** = Read permission
- **2** = Write permission
- **1** = Execute permission

Add values together: `4+2+1=7` (full permissions), `4+2=6` (read+write), `4+1=5` (read+execute)

## Request Examples

### Example 1: Change Single File Permissions

```bash
curl --location 'https://your-domain.com:8090/cloudAPI/' \
--header 'Authorization: YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "serverUserName": "admin",
    "controller": "changeFilePermissions",
    "domainName": "example.com",
    "basePath": "/home/example.com/public_html",
    "permissionsPath": "index.php",
    "newPermissions": "644",
    "recursive": 0
}'
```

### Example 2: Change Directory Permissions Recursively

```bash
curl --location 'https://your-domain.com:8090/cloudAPI/' \
--header 'Authorization: YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "serverUserName": "admin",
    "controller": "changeFilePermissions",
    "domainName": "example.com",
    "basePath": "/home/example.com/public_html",
    "permissionsPath": "uploads",
    "newPermissions": "755",
    "recursive": 1
}'
```

### Example 3: Change Multiple Files (requires separate calls)

```bash
# File 1
curl --location 'https://your-domain.com:8090/cloudAPI/' \
--header 'Authorization: YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "serverUserName": "admin",
    "controller": "changeFilePermissions",
    "domainName": "example.com",
    "basePath": "/home/example.com/public_html",
    "permissionsPath": "config.php",
    "newPermissions": "600"
}'

# File 2
curl --location 'https://your-domain.com:8090/cloudAPI/' \
--header 'Authorization: YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "serverUserName": "admin",
    "controller": "changeFilePermissions",
    "domainName": "example.com",
    "basePath": "/home/example.com/public_html",
    "permissionsPath": "scripts/backup.sh",
    "newPermissions": "755"
}'
```

## Response Format

### Success Response

```json
{
    "status": 1,
    "error_message": "None"
}
```

### Error Response

```json
{
    "status": 0,
    "error_message": "Error description here"
}
```

## Common Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Website not found" | Domain doesn't exist in CyberPanel | Verify domain name is correct |
| "Permission denied" | Insufficient privileges | Ensure API user has admin rights |
| "File not found" | File/directory doesn't exist | Check file path is correct |
| "Invalid permissions" | Invalid octal permission format | Use valid 3-digit octal (e.g., "755") |
| "Path traversal detected" | Path contains ".." | Use absolute paths within domain directory |

## Security Considerations

### Path Security
- All paths are validated to prevent directory traversal attacks
- Files must be within the domain's home directory (`/home/domain.com/`)
- Paths containing `..` are rejected

### Permission Limits
- Changes are executed as the website's user (not root)
- Cannot change ownership, only permissions
- Limited to files owned by the website user

### Access Control
- Requires valid API authentication
- User must have ownership of the domain
- ACL permissions are enforced

## Best Practices

### 1. **Standard Web Permissions**
```bash
# PHP/HTML files
"newPermissions": "644"

# Directories
"newPermissions": "755"

# Configuration files (sensitive)
"newPermissions": "600"

# Executable scripts
"newPermissions": "755"
```

### 2. **Batch Operations**
For multiple files, consider using `fixFilePermissions` instead, which applies standard permissions to the entire domain.

### 3. **Recursive Usage**
Use `recursive: 1` carefully on large directories as it can take time and affect many files.

### 4. **Verification**
After changing permissions, you can verify using the `getFileInfo` API to check the current permissions.

## Related APIs

- **`fixFilePermissions`**: Applies standard permissions to entire domain
- **`getFileInfo`**: Get detailed file information including current permissions
- **`listFiles`**: List files with permission information

## Implementation Notes

### Technical Details
- Uses `chmod` command internally
- Executed as the website's user account
- Supports both files and directories
- Recursive option uses `chmod -R`

### Path Construction
The actual file path is constructed as: `basePath + '/' + permissionsPath`

Example:
- `basePath`: `/home/example.com/public_html`
- `permissionsPath`: `uploads/image.jpg`
- **Final path**: `/home/example.com/public_html/uploads/image.jpg`

### Limitations
- Cannot change file ownership (use `fixFilePermissions` for that)
- Cannot set permissions outside domain directory
- Recursive operations may timeout on very large directories
- Changes are immediate and cannot be undone via API

## Troubleshooting

### Common Issues

1. **Permission Changes Not Taking Effect**
   - Verify the file exists at the specified path
   - Check that the API user owns the domain
   - Ensure the website user has access to the file

2. **Path Errors**
   - Use absolute paths starting with `/home/domain.com/`
   - Ensure no typos in domain name or file path
   - Check file/directory actually exists

3. **Recursive Operations Failing**
   - Large directories may timeout
   - Some subdirectories might have different ownership
   - Consider using `fixFilePermissions` for comprehensive fixes

### Debug Steps

1. **Verify domain exists**: Use `fetchWebsites` API
2. **Check file exists**: Use `listFiles` or `getFileInfo` API
3. **Test with simple file first**: Try changing a single file before directories
4. **Check current permissions**: Use `getFileInfo` to see current state

## Example Workflows

### Workflow 1: Secure Configuration File
```bash
# Make config file readable only by owner
curl --location 'https://your-domain.com:8090/cloudAPI/' \
--header 'Authorization: YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "serverUserName": "admin",
    "controller": "changeFilePermissions",
    "domainName": "example.com",
    "basePath": "/home/example.com/public_html",
    "permissionsPath": "wp-config.php",
    "newPermissions": "600"
}'
```

### Workflow 2: Make Script Executable
```bash
# Make shell script executable
curl --location 'https://your-domain.com:8090/cloudAPI/' \
--header 'Authorization: YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "serverUserName": "admin",
    "controller": "changeFilePermissions",
    "domainName": "example.com",
    "basePath": "/home/example.com/public_html",
    "permissionsPath": "scripts/deploy.sh",
    "newPermissions": "755"
}'
```

### Workflow 3: Fix Upload Directory
```bash
# Ensure upload directory is writable
curl --location 'https://your-domain.com:8090/cloudAPI/' \
--header 'Authorization: YOUR_API_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "serverUserName": "admin",
    "controller": "changeFilePermissions",
    "domainName": "example.com",
    "basePath": "/home/example.com/public_html",
    "permissionsPath": "wp-content/uploads",
    "newPermissions": "755",
    "recursive": 1
}'
```

This API provides granular control over file permissions while maintaining security through path validation and user privilege enforcement.
