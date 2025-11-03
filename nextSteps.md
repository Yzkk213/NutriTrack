
- When a single meal is deleted, rename each following "meal[i]" to "meal[i-1]" if they follow the same naming pattern.

- When using image recognition, remove any predicted item not found in the Edamam database before computing macros.

- V2 (Fine-tuning): fine-tune the pretrained ResNet50d (Food-101) model on the Ingredients101 dataset to recognize ingredients instead of full dishes. Save the fine-tuned model for inference.

- V3 (Multimodal): build a model combining image and text encoders (ResNet/ViT + DistilBERT/CLIP) to predict multiple food items and portion sizes jointly using cross-modal alignment.