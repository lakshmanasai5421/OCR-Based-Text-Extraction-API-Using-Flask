<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["file"])) {
    $file = $_FILES["file"];
    $filePath = $file["tmp_name"];
    $fileType = mime_content_type($filePath);

    // Determine API endpoint based on file type
    if (strpos($fileType, "image") !== false) {
        $url = "http://127.0.0.1:5000/extract/image";
    } elseif (strpos($fileType, "pdf") !== false) {
        $url = "http://127.0.0.1:5000/extract/pdf";
    } else {
        die("Unsupported file type.");
    }

    // Prepare file for upload
    $curl = curl_init();
    $postFields = [
        'file' => new CURLFile($filePath, $fileType, $file["name"])
    ];

    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_POST => true,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POSTFIELDS => $postFields
    ]);

    $response = curl_exec($curl);
    $error = curl_error($curl);
    curl_close($curl);

    if ($error) {
        echo "cURL Error: " . $error;
    } else {
        $result = json_decode($response, true);
        echo "<h2>Extracted Text:</h2>";
        echo "<pre>" . htmlspecialchars($result["text"]) . "</pre>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Extraction Client</title>
</head>
<body>
    <h2>Upload an Image or PDF for Text Extraction</h2>
    <form action="" method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload & Extract</button>
    </form>
</body>
</html>
