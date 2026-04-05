import torch
from torchvision import models, transforms
from PIL import Image

# Load model
model = models.resnet18(pretrained=True)
model.eval()

# Load labels
with open("imagenet_classes.txt") as f:
    labels = [line.strip() for line in f.readlines()]

# Transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict(image):
    img = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img)

    probs = torch.nn.functional.softmax(outputs[0], dim=0)
    top_prob, top_idx = torch.topk(probs, 3)

    results = []
    for i in range(3):
        results.append((labels[top_idx[i]], float(top_prob[i])))

    return results