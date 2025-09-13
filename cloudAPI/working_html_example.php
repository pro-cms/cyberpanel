<?php
/**
 * Working example for writing HTML files to CyberPanel API
 * This example handles the security filter issue by using base64 encoding
 */

use GuzzleHttp\Client;
use GuzzleHttp\Psr7\Request;

// Your HTML content
$htmlContent = '<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
    <p>This HTML contains special characters that would be blocked by security filters.</p>
  </body>
</html>';

// Method 1: Using Base64 Encoding (Recommended)
function writeHtmlWithBase64($htmlContent, $domainName, $fileName) {
    $client = new Client();
    $headers = [
        'Authorization' => 'Basic 7892c699426e62ac580f9228b47068a8383926bcb1851bc986bc344322d1409d',
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    ];
    
    $body = json_encode([
        'serverUserName' => 'admin',
        'controller' => 'writeFileContents',
        'domainName' => $domainName,
        'fileName' => $fileName,
        'fileContent' => base64_encode($htmlContent),
        'isBase64' => true
    ]);
    
    $request = new Request('POST', 'https://cloud-1.zepson.com:8090/cloudAPI/', $headers, $body);
    $res = $client->sendAsync($request)->wait();
    
    return json_decode($res->getBody(), true);
}

// Method 2: Using Upload Endpoint
function writeHtmlWithUpload($htmlContent, $domainName, $path) {
    $client = new Client();
    $headers = [
        'Authorization' => 'Basic 7892c699426e62ac580f9228b47068a8383926bcb1851bc986bc344322d1409d',
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    ];
    
    $body = json_encode([
        'serverUserName' => 'admin',
        'controller' => 'uploadFile',
        'domainName' => $domainName,
        'path' => $path,
        'file' => base64_encode($htmlContent),
        'fileName' => 'index.html'
    ]);
    
    $request = new Request('POST', 'https://cloud-1.zepson.com:8090/cloudAPI/', $headers, $body);
    $res = $client->sendAsync($request)->wait();
    
    return json_decode($res->getBody(), true);
}

// Method 3: Two-step process (Create + Write)
function writeHtmlTwoStep($htmlContent, $domainName, $path) {
    $client = new Client();
    $headers = [
        'Authorization' => 'Basic 7892c699426e62ac580f9228b47068a8383926bcb1851bc986bc344322d1409d',
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    ];
    
    // Step 1: Create empty file
    $createBody = json_encode([
        'serverUserName' => 'admin',
        'controller' => 'createNewFile',
        'domainName' => $domainName,
        'fileName' => 'index.html',
        'path' => $path
    ]);
    
    $createRequest = new Request('POST', 'https://cloud-1.zepson.com:8090/cloudAPI/', $headers, $createBody);
    $createRes = $client->sendAsync($createRequest)->wait();
    $createResult = json_decode($createRes->getBody(), true);
    
    if ($createResult['status'] !== 1) {
        return $createResult;
    }
    
    // Step 2: Write content using base64
    $writeBody = json_encode([
        'serverUserName' => 'admin',
        'controller' => 'writeFileContents',
        'domainName' => $domainName,
        'fileName' => $path . '/index.html',
        'fileContent' => base64_encode($htmlContent),
        'isBase64' => true
    ]);
    
    $writeRequest = new Request('POST', 'https://cloud-1.zepson.com:8090/cloudAPI/', $headers, $writeBody);
    $writeRes = $client->sendAsync($writeRequest)->wait();
    
    return json_decode($writeRes->getBody(), true);
}

// Usage examples
try {
    // Example 1: Using base64 encoding (Recommended)
    echo "Method 1: Base64 Encoding\n";
    $result1 = writeHtmlWithBase64(
        $htmlContent, 
        'zepsontest.com', 
        '/home/zepsontest.com/public_html/index.html'
    );
    echo "Result: " . json_encode($result1) . "\n\n";
    
    // Example 2: Using upload endpoint
    echo "Method 2: Upload Endpoint\n";
    $result2 = writeHtmlWithUpload(
        $htmlContent, 
        'zepsontest.com', 
        '/home/zepsontest.com/public_html'
    );
    echo "Result: " . json_encode($result2) . "\n\n";
    
    // Example 3: Two-step process
    echo "Method 3: Two-step Process\n";
    $result3 = writeHtmlTwoStep(
        $htmlContent, 
        'zepsontest.com', 
        '/home/zepsontest.com/public_html'
    );
    echo "Result: " . json_encode($result3) . "\n\n";
    
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

// Helper function to encode HTML for API
function encodeHtmlForApi($htmlContent) {
    return [
        'fileContent' => base64_encode($htmlContent),
        'isBase64' => true
    ];
}

// Helper function to decode HTML from API
function decodeHtmlFromApi($base64Content) {
    return base64_decode($base64Content);
}

// Example of handling different HTML content types
$htmlExamples = [
    'simple' => '<h1>Hello World</h1>',
    'complex' => '<!DOCTYPE html><html><head><title>Test</title></head><body><h1>Hello $world!</h1><script>console.log("test");</script></body></html>',
    'with_special_chars' => '<p>Price: $100; Discount: 50% && Free shipping</p>'
];

foreach ($htmlExamples as $type => $html) {
    echo "Encoding $type HTML:\n";
    $encoded = encodeHtmlForApi($html);
    echo "Base64: " . $encoded['fileContent'] . "\n";
    echo "Decoded: " . decodeHtmlFromApi($encoded['fileContent']) . "\n\n";
}
?>
