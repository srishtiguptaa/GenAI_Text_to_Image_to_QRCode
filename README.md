# GENERATE IMAGES AND QR CODE USING GENAI

## About the Project:-

Create a GenAI model that takes a text prompt and generate an image. Using that image and data that needs to be embedded in QR Code, generate an contextual QR code.

## Problem Statement:

Create application that can generate image and scannable QR Code using a Gen AI text to image model.

• There is a text prompt for which an image is needed.

• The text has to be fed to a Gen AI model for Text to Image generation.

• Using this image and QR Code data, a contextual QR has to be generated.

• Create an app that will take a prompt and QR data from user and generate and display the QR.

## Table of content:-

1. Prerequisites
2. Setup
3. Detailed Approach
4. Examples
5. Performance Comparison

### Prerequisites:

Before you begin, ensure you have the following prerequisites installed and configured:

- Generative AI Model (e.g., Stable Diffusion): For image generation.
- ControlNet Model: For integrating the QR code with the generated image.
- Google Colab: Recommended environment for running the model.
- Python Libraries: Install `numpy`, `Pillow`, `qrcode`, and any required Gen AI and ControlNet libraries.


### Setup:

1. Clone the Repository: ```bash git clone <repository-link> cd <repository-folder>```
2. Install Dependencies: Ensure all necessary libraries are installed, and set up both the Gen AI model and ControlNet environment.
3. Configure Google Colab (optional): Connect your Google Drive if needed for image or QR code storage.
4. Run the Application: Launch the script to input a prompt, generate an image, apply ControlNet, and create a contextual QR code.

### Detailed Approach:

#### Step 1: Text-to-Image Generation
- Stable Diffusion processes the text prompt and produces an image that visually represents the provided concept.
- Parameters such as `guidance_scale` can be adjusted to control the style and detail of the generated image.

#### Step 2: QR Code Creation
- Generate a QR code containing the input data (like a URL or message).
- This QR code will later be layered over the image.

#### Step 3: ControlNet Integration
- ControlNet enables enhanced blending of the QR code with the background image.
- Key parameters, such as `controlnet_conditioning_scale`, are tuned to ensure a harmonious balance between QR code visibility and aesthetic background elements, optimizing both scannability and artistic coherence.

#### Step 4: Display & Output
- The final contextual QR code is presented, featuring a unique design that represents the prompt while embedding scannable QR data.
- Upon scanning, users can view additional information, making the QR code interactive and meaningful.

### Examples:

1) Prompt: a tourist place in Abu Dabi with buildings, realistic, 8K, fantasy

   Generated Image: 
  
   ![image](https://media.github.ecodesamsung.com/user/30421/files/a96948e4-c75e-475d-99ec-94fd559c796d)
  
   Contextual QR code:
  
   ![image](https://media.github.ecodesamsung.com/user/30421/files/2704b750-7bda-4225-b03b-4ad6f2f31a93)

2) Prompt: a public party all people enjoying together, realistic, 8K, fantasy 
   
   Generated Image:
   
   ![image](https://media.github.ecodesamsung.com/user/30421/files/05fde177-3e9a-4017-b27d-9d5c9c77dad6)
   
   Contextual QR code:
   
   ![image](https://media.github.ecodesamsung.com/user/30421/files/2a32f14b-36d6-42a1-81eb-b62aa4278f60)
   
3) Prompt: a good dark background night view, realistic, 8K, fantasy 

   Generated Image:
   
   ![image](https://media.github.ecodesamsung.com/user/30421/files/afa8ec4c-bb6b-4a6b-9eda-793c8321d847)
   
   Contextual QR code:
   
   ![image](https://media.github.ecodesamsung.com/user/30421/files/45e5081c-1f7a-42ae-83ed-cc124bb079d9)

4) Prompt: a asthetic night background with moon,  realistic, 8K, fantasy

   Generated Image:
   
   ![image](https://media.github.ecodesamsung.com/user/30421/files/5f3484ab-c99d-468e-ba0e-735111598c8b)
   
   Contextual QR code:
   
   ![image](https://media.github.ecodesamsung.com/user/30421/files/7071d4c4-b5f2-4c20-929d-14892a19bd3a)


### Performance Comparison:

#### 1. Optimizing Image Generation

Generating images with models like Stable Diffusion can be resource-intensive. Here are some ways to improve performance while maintaining quality:

   - Guidance Scale:
     - Purpose: Balances prompt accuracy with creativity in image generation. Higher values create more prompt-specific images, while lower values may yield more      abstract results.
     - Tip: Experiment with a range to achieve the desired balance. Lower values can speed up generation but may reduce prompt relevance, so aim for a setting that matches your project's needs.

   - Image Resolution:
     - Purpose: Higher resolutions create detailed images but require more processing power.
     - Tip: Begin with a moderate resolution for faster testing and, if needed, upscale only the final images. This minimizes processing time while retaining quality.

   - Batch Size:
     - Purpose: Controls the number of images processed simultaneously.
     - Tip: Use a batch size of 1 on limited hardware to avoid memory overload. For setups with powerful GPUs, a slightly larger batch size can boost speed.

   - Inference Speed:
     - Purpose: Influences how quickly images are generated.
     - Tip: Use mixed-precision computation (float16) if your hardware allows, as it significantly speeds up generation without sacrificing quality.

   - Caching and Reusing Embeddings:
     - Purpose: Speeds up image generation by reusing computations for common prompts or styles.
     - Tip: For repeated prompts or themes, cache prompt embeddings to save time and reduce model load during testing phases.

#### 2. Fine-Tuning ControlNet Parameters

ControlNet plays a key role in blending the QR code with the generated image, balancing aesthetics and scannability. Adjusting ControlNet parameters can optimize both integration and QR readability:

   - ControlNet Conditioning Scale:
     - Purpose: Adjusts ControlNet’s influence on the generated image, balancing QR code visibility with the background image.
     - Tip: Start with a moderate scale and adjust to achieve the best balance. Higher values make the QR code stand out more, while lower values allow for better blending. Aim for a middle ground that maintains both visual appeal and scannability.

   - Weighting for Background Elements:
     - Purpose: Controls the QR code’s visibility relative to complex background elements.
     - Tip: For busy backgrounds, reduce ControlNet’s influence in areas around the QR code. For simpler backgrounds, increase the weight to blend the QR code more naturally.

#### 3. Balancing QR Code Visibility with Design Aesthetics

To ensure both functionality and aesthetic appeal, use these tips for optimizing the QR code’s visibility:

   - QR Code Contrast:
     - Purpose: Ensures the QR code remains recognizable by scanners against varying background colors.
     - Tip: Adjust contrast based on background color. Dark backgrounds work best with lighter QR codes, and vice versa. For added clarity, a subtle outline can help differentiate the QR code.

   - Opacity Adjustments:
     - Purpose: Softens the QR code overlay to better blend with the image.
     - Tip: Experiment with slightly reduced opacity (around 70-90%) for a subtle overlay. Find a setting where the QR remains distinct but doesn’t dominate the image.

   - Positioning and Size:
     - Purpose: Influences how well the QR code integrates without overpowering the image composition.
     - Tip: Position the QR code in less detailed areas, like corners or simpler regions, to avoid competition with complex visuals. Ensure it’s large enough for scanning but appropriately sized for the image.

#### 4. Optimizing for Colab/Local Environment

Optimizing your setup for Colab or local environments is key when resources are limited:

   - Utilize GPU Acceleration:
     - Purpose: Speeds up processing by leveraging GPU capabilities.
     - Tip: In Colab, select the GPU runtime (Runtime > Change runtime type > Hardware accelerator > GPU). On a local machine, ensure GPU drivers and libraries are up-to-date to get the best performance.

   - Memory Management:
     - Purpose: Prevents memory overloads, especially with large models.
     - Tip: Clear the cache after each generation step (`torch.cuda.empty_cache()` in PyTorch) to free memory. Lower image resolution temporarily for trials to conserve memory during testing.

   - Efficient Model Loading:
     - Purpose: Frees up resources by loading and unloading models only as needed.
     - Tip: Load each model (Stable Diffusion, ControlNet) only for its specific task and then unload to reduce memory usage.

#### 5. Adapting ControlNet for Diverse Prompts

   Different types of prompts produce varied image styles, and ControlNet adjustments help maintain quality across prompt styles:

   - Adapting for Prompt Complexity:
     - Purpose: Handles the range from minimalistic to highly detailed images.
     - Tip: For detailed prompts, reduce ControlNet’s influence in complex areas to avoid interference with the QR code. For simpler prompts, increase ControlNet’s influence for a seamless blend.

   - Adjusting for Lighting and Color in Prompts:
     - Purpose: Ensures the QR code remains readable under different lighting effects in generated images.
     - Tip: Match the QR code’s color and opacity to the image’s lighting. For darker scenes, use lighter QR codes or add a faint outline. In brighter scenes, use a darker QR code to blend naturally.



