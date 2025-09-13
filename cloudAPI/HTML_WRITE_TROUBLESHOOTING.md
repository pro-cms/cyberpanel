# HTML File Write Troubleshooting Guide

## 🚨 **Issue: writeFileContents Fails When Saving HTML Files**

### **Root Cause**
The API documentation had incorrect parameter names, causing confusion when integrating with the `writeFileContents` endpoint.

### **The Problem**
- **Documentation showed**: `fileContents` (plural)
- **Actual implementation expects**: `fileContent` (singular)
- **File path format**: Must be full path, not separate `path` + `fileName`

---

## ✅ **Correct Implementation**

### **1. Correct Parameter Names**
```json
{
  "serverUserName": "admin",
  "controller": "writeFileContents",
  "domainName": "example.com",
  "fileName": "/home/example.com/public_html/index.html",
  "fileContent": "<html><body><h1>Hello World!</h1></body></html>"
}
```

### **2. Key Differences from Documentation**
| ❌ **Wrong** | ✅ **Correct** |
|-------------|----------------|
| `"fileContents"` | `"fileContent"` |
| `"fileName": "file.html"` + `"path": "/home/..."` | `"fileName": "/home/.../file.html"` |
| Separate path and filename | Full file path in fileName |

---

## 🔧 **Working Examples**

### **Example 1: Create HTML File**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "writeFileContents",
    "domainName": "example.com",
    "fileName": "/home/example.com/public_html/index.html",
    "fileContent": "<!DOCTYPE html><html><head><title>My Page</title></head><body><h1>Welcome!</h1></body></html>"
  }'
```

### **Example 2: Update HTML File**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "writeFileContents",
    "domainName": "example.com",
    "fileName": "/home/example.com/public_html/contact.html",
    "fileContent": "<!DOCTYPE html><html><head><title>Contact</title></head><body><h1>Contact Us</h1><p>Email: info@example.com</p></body></html>"
  }'
```

### **Example 3: Create PHP File with HTML**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "writeFileContents",
    "domainName": "example.com",
    "fileName": "/home/example.com/public_html/dashboard.php",
    "fileContent": "<?php echo \"<h1>Dashboard</h1>\"; ?>"
  }'
```

---

## 🐛 **Common Errors and Solutions**

### **Error 1: "fileContent not found"**
```json
{
  "status": 0,
  "error_message": "KeyError: 'fileContent'"
}
```
**Solution**: Use `fileContent` (singular), not `fileContents` (plural)

### **Error 2: "File not found"**
```json
{
  "status": 0,
  "error_message": "File not found"
}
```
**Solution**: Use full file path in `fileName` parameter

### **Error 3: "Permission denied"**
```json
{
  "status": 0,
  "error_message": "Permission denied"
}
```
**Solution**: Ensure the file path is within the domain's home directory

---

## 📋 **Complete HTML File Management Workflow**

### **Step 1: Create HTML File**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "writeFileContents",
    "domainName": "example.com",
    "fileName": "/home/example.com/public_html/index.html",
    "fileContent": "<!DOCTYPE html><html><head><title>Home</title></head><body><h1>Welcome to My Site</h1></body></html>"
  }'
```

### **Step 2: Read HTML File**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "readFileContents",
    "domainName": "example.com",
    "fileName": "index.html",
    "path": "/home/example.com/public_html"
  }'
```

### **Step 3: Update HTML File**
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "writeFileContents",
    "domainName": "example.com",
    "fileName": "/home/example.com/public_html/index.html",
    "fileContent": "<!DOCTYPE html><html><head><title>Updated Home</title></head><body><h1>Welcome to My Updated Site</h1><p>This is the updated content!</p></body></html>"
  }'
```

---

## 🔍 **Debugging Tips**

### **1. Check Parameter Names**
- ✅ `fileContent` (singular)
- ❌ `fileContents` (plural)

### **2. Check File Path Format**
- ✅ `"fileName": "/home/example.com/public_html/file.html"`
- ❌ `"fileName": "file.html"` + `"path": "/home/example.com/public_html"`

### **3. Check HTML Content Encoding**
- Ensure HTML content is properly escaped in JSON
- Use double quotes for HTML attributes
- Escape special characters if needed

### **4. Verify Domain Ownership**
- Ensure the file path is within `/home/{domain}/`
- Check that the domain exists in CyberPanel

---

## 🚀 **Best Practices**

### **1. HTML Content Handling**
```javascript
// JavaScript example
const htmlContent = `
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>`;

const data = {
    serverUserName: "admin",
    controller: "writeFileContents",
    domainName: "example.com",
    fileName: "/home/example.com/public_html/index.html",
    fileContent: htmlContent
};
```

### **2. Error Handling**
```javascript
fetch('/cloudAPI/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(result => {
    if (result.status === 1) {
        console.log('File saved successfully');
    } else {
        console.error('Error:', result.error_message);
    }
})
.catch(error => {
    console.error('Request failed:', error);
});
```

### **3. File Path Validation**
```javascript
function validateFilePath(domainName, fileName) {
    const expectedPath = `/home/${domainName}/`;
    return fileName.startsWith(expectedPath);
}

// Usage
if (validateFilePath('example.com', '/home/example.com/public_html/index.html')) {
    // Proceed with API call
} else {
    console.error('Invalid file path');
}
```

---

## 📚 **Updated API Reference**

### **writeFileContents Endpoint**
- **Method**: POST
- **Controller**: `writeFileContents`
- **Required Parameters**:
  - `serverUserName`: "admin"
  - `domainName`: Domain name
  - `fileName`: Full file path (e.g., "/home/example.com/public_html/file.html")
  - `fileContent`: HTML content as string
- **Response**: `{"status": 1}` on success

### **Example Request**
```json
{
  "serverUserName": "admin",
  "controller": "writeFileContents",
  "domainName": "example.com",
  "fileName": "/home/example.com/public_html/index.html",
  "fileContent": "<!DOCTYPE html><html><head><title>Test</title></head><body><h1>Hello</h1></body></html>"
}
```

This guide should resolve all HTML file writing issues with the CyberPanel File Manager API.
