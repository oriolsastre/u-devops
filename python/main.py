print("Hello world")

# Variable string
skill="DevOps"
print(skill)

# Integer
NUM=123
print(NUM)

# List []
tools=["Jenkins", "Docker", "K8s", "Terraform", 90]
print(tools)
print(tools[1]) # Docker
print(tools[1:4]) # Docker, K8s, Terraform
print(tools[1:4][1]) # K8s

# Tuple ()
tools2=("Jenkins", "Docker", "K8s", "Terraform", 90)
print(tools2)
print(tools2[-2]) # Terraform

# Dictionary {} clau: valor
devops={
    "skill": "DevOps",
    "Year": 2024,
    "Tech": {
        "Cloud": "AWS",
        "Containers": "K8s",
        "CICD": "Jenkins",
        "GitOps": ["GitLab", "ArgoCD", "Tekton"]
    }
}
print(devops)
print(devops["Year"])
