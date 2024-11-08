function generateImage() {
    var promptInput = document.getElementById('promptInput').value;
    // Call your AI model here to generate the image based on the promptInput
    // For demonstration purpose, let's assume the image URL is generated
    var imageURL = 'https://via.placeholder.com/300'; // Replace this with your actual generated image URL
    document.getElementById('generatedImage').src = imageURL;
    document.getElementById('page1').style.display = 'none';
    document.getElementById('page2').style.display = 'block';
}

function generateQR() {
    var generatedImageURL = document.getElementById('generatedImage').src;
    // Call your AI model here to generate the QR code based on the generatedImageURL
    // For demonstration purpose, let's assume the QR code URL is generated
    var qrCodeURL = 'https://api.qrserver.com/v1/create-qr-code/?data=' + encodeURIComponent(generatedImageURL);
    document.getElementById('generatedQR').src = qrCodeURL;
    document.getElementById('page2').style.display = 'none';
    document.getElementById('page3').style.display = 'block';
}

function goToPage1() {
    document.getElementById('promptInput').value = '';
    document.getElementById('page2').style.display = 'none';
    document.getElementById('page3').style.display = 'none';
    document.getElementById('page1').style.display = 'block';
}
