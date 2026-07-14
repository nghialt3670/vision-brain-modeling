# Vision Models

| Space | Model | Content Captured | Used For |
|-------|-------|-----------------|---------|
| **Pixel space** | — | Raw pixel values | Low-level metrics (SSIM, PixCorr) |
| **CNN feature space** | AlexNet, ResNet | Hierarchical visual features | Cortical encoding models |
| **CLIP image space** | CLIP ViT | Semantic + perceptual | Brain encoder target, retrieval |
| **CLIP text space** | CLIP text | Semantic language | Brain-to-text / captioning |
| **VAE latent space** | SD VAE | Low-level structure | Reconstruction decoder initialization |
| **DINOv2 feature space** | DINOv2 | Spatial semantics | Spatial decoding and layout mapping |
| **LLM embedding space** | LLaMA, GPT | Language semantics | Direct brain-to-text generation |
