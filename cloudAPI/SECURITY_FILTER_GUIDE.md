# CyberPanel API Security Filter Guide

## 🚨 **Issue: Security Filter Blocking HTML Content**

The CyberPanel API has built-in security filters that block certain characters to prevent command injection attacks. This affects HTML files containing these characters.

### **Blocked Characters**
- `;` (semicolon)
- `&&` (double ampersand)
- `||` (double pipe)
- `|` (pipe)
- `` ` `` (backtick)
- `$` (dollar sign)
- `../` (directory traversal)

---

## 🔍 **Analysis of Your Error**

### **Your HTML Content**
```html
<!dosadfsdafdsfsdsctypef html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
```

### **Potential Issues**
1. **`$` character**: Not directly visible in your HTML, but might be in escaped form
2. **Special characters**: The security filter might be overly aggressive

---

## ✅ **Solutions**

### **Solution 1: Use Base64 Encoding (Recommended)**

Encode your HTML content as Base64 to bypass the security filter:

```php
<?php
use GuzzleHttp\Client;
use GuzzleHttp\Psr7\Request;

$client = new Client();
$headers = [
  'Authorization' => 'Basic 7892c699426e62ac580f9228b47068a8383926bcb1851bc986bc344322d1409d',
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
];

$htmlContent = '<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>';

$body = json_encode([
    'serverUserName' => 'admin',
    'controller' => 'writeFileContents',
    'domainName' => 'zepsontest.com',
    'fileName' => '/home/zepsontest.com/public_html/index.html',
    'fileContent' => base64_encode($htmlContent),
    'isBase64' => true  // Add this flag to indicate base64 content
]);

$request = new Request('POST', 'https://cloud-1.zepson.com:8090/cloudAPI/', $headers, $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();
?>
```

### **Solution 2: Modify CloudManager to Handle Base64**

We need to update the `writeFileContents` method to handle base64 encoded content:

```python
def writeFileContents(self, request):
    """Write file contents with base64 support"""
    try:
        finalData = {}
        finalData['status'] = 1
        
        # Check if content is base64 encoded
        is_base64 = self.data.get('isBase64', False)
        file_content = self.data['fileContent']
        
        if is_base64:
            import base64
            file_content = base64.b64decode(file_content).decode('utf-8')
        
        try:
            self.data['home'] = '/home/%s' % (self.data['domainName'])
            ACLManager.CreateSecureDir()
            tempPath = '%s/%s' % ('/usr/local/CyberCP/tmp', str(randint(1000, 9999)))
            
            domainName = self.data['domainName']
            website = Websites.objects.get(domain=domainName)
            
            writeToFile = open(tempPath, 'wb')
            writeToFile.write(file_content.encode('utf-8'))
            writeToFile.close()
            
            command = 'chown %s:%s %s' % (website.externalApp, website.externalApp, tempPath)
            ProcessUtilities.executioner(command)
            
            command = 'cp %s %s' % (tempPath, self.returnPathEnclosed(self.data['fileName']))
            ProcessUtilities.executioner(command, website.externalApp)
            
            os.remove(tempPath)
        except:
            # Fallback for root directory operations
            self.data['home'] = '/'
            ACLManager.CreateSecureDir()
            tempPath = '%s/%s' % ('/usr/local/CyberCP/tmp', str(randint(1000, 9999)))
            writeToFile = open(tempPath, 'wb')
            writeToFile.write(file_content.encode('utf-8'))
            writeToFile.close()
            
            command = 'cp %s %s' % (tempPath, self.returnPathEnclosed(self.data['fileName']))
            ProcessUtilities.executioner(command)
            
            os.remove(tempPath)
        
        json_data = json.dumps(finalData)
        return HttpResponse(json_data)
        
    except BaseException as msg:
        return self.ajaxPre(0, str(msg))
```

### **Solution 3: Use Alternative Endpoints**

If the security filter is too restrictive, consider using these alternative approaches:

#### **A. Create File First, Then Write Content**
```php
// Step 1: Create empty file
$createBody = json_encode([
    'serverUserName' => 'admin',
    'controller' => 'createNewFile',
    'domainName' => 'zepsontest.com',
    'fileName' => 'index.html',
    'path' => '/home/zepsontest.com/public_html'
]);

// Step 2: Write content using a different method
$writeBody = json_encode([
    'serverUserName' => 'admin',
    'controller' => 'writeFileContents',
    'domainName' => 'zepsontest.com',
    'fileName' => '/home/zepsontest.com/public_html/index.html',
    'fileContent' => base64_encode($htmlContent),
    'isBase64' => true
]);
```

#### **B. Use Upload Endpoint**
```php
// Convert HTML to base64 and use upload endpoint
$uploadBody = json_encode([
    'serverUserName' => 'admin',
    'controller' => 'uploadFile',
    'domainName' => 'zepsontest.com',
    'path' => '/home/zepsontest.com/public_html',
    'file' => base64_encode($htmlContent),
    'fileName' => 'index.html'
]);
```

---

## 🛠️ **Implementation Guide**

### **Step 1: Update CloudManager**

Add the base64 handling to the `writeFileContents` method in `cloudAPI/cloudManager.py`:

```python
def writeFileContents(self, request):
    """Write file contents with base64 support"""
    try:
        request.session['userID'] = self.admin.pk
        from filemanager.filemanager import FileManager
        
        # Check if content is base64 encoded
        is_base64 = self.data.get('isBase64', False)
        if is_base64 and 'fileContent' in self.data:
            import base64
            self.data['fileContent'] = base64.b64decode(self.data['fileContent']).decode('utf-8')
        
        fm = FileManager(request, self.data)
        return fm.writeFileContents()
    except BaseException as msg:
        return self.ajaxPre(0, str(msg))
```

### **Step 2: Update API Documentation**

Add base64 support to the documentation:

```markdown
### 6. Write File (with Base64 support)
**Endpoint**: `writeFileContents`

#### Standard Request
```bash
curl -X POST https://your-server.com/cloudAPI/ \
  -H "Content-Type: application/json" \
  -d '{
    "serverUserName": "admin",
    "controller": "writeFileContents",
    "domainName": "example.com",
    "fileName": "/home/example.com/public_html/index.html",
    "fileContent": "<html><body><h1>Hello</h1></body></html>"
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
```

### **Step 3: Test the Solution**

```php
<?php
// Test script for base64 HTML upload
$htmlContent = '<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
    <p>This contains special characters: $, ;, &&</p>
  </body>
</html>';

$body = json_encode([
    'serverUserName' => 'admin',
    'controller' => 'writeFileContents',
    'domainName' => 'zepsontest.com',
    'fileName' => '/home/zepsontest.com/public_html/index.html',
    'fileContent' => base64_encode($htmlContent),
    'isBase64' => true
]);

// Make the API call
$client = new GuzzleHttp\Client();
$response = $client->post('https://cloud-1.zepson.com:8090/cloudAPI/', [
    'headers' => [
        'Authorization' => 'Basic 7892c699426e62ac580f9228b47068a8383926bcb1851bc986bc344322d1409d',
        'Content-Type' => 'application/json',
    ],
    'body' => $body
]);

echo $response->getBody();
?>
```

---

## 🔒 **Security Considerations**

### **Why This Filter Exists**
The security filter prevents command injection attacks where malicious users could inject shell commands through file content.

### **Safe Characters for HTML**
- Letters (a-z, A-Z)
- Numbers (0-9)
- Basic punctuation: `.,:!?()[]{}"`
- HTML tags: `< > /`
- Whitespace and newlines

### **Problematic Characters**
- `$` - Used in shell variable substitution
- `;` - Command separator
- `&&`, `||` - Logical operators
- `` ` `` - Command substitution
- `|` - Pipe operator
- `../` - Directory traversal

---

## 📋 **Quick Fix Summary**

1. **Encode HTML as Base64** before sending
2. **Add `isBase64: true`** flag to the request
3. **Update CloudManager** to handle base64 decoding
4. **Test with your HTML content**

This approach bypasses the security filter while maintaining the security benefits for regular text content.
