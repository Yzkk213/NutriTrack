import torch
from torchvision import models, transforms
from PIL import Image
import timm


model = models.resnet50("IMAGENET1K_V2")
model.eval()

# Preprocessing pipeline
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

with open("backend/ml/imagenet_classes.txt") as f:
    LABELS = [line.strip() for line in f.readlines()]

def predict_food(image_path: str, topk: int = 5):
    image = Image.open(image_path).convert("RGB")
    input_tensor = preprocess(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_tensor)
        _, indices = torch.sort(outputs, descending=True)
        top_indices = indices[0][:topk].tolist()

    predictions = [LABELS[idx] for idx in top_indices]
    return predictions
