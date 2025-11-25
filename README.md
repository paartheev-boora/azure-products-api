# Azure Products API  
A simple and scalable CRUD API built using **Azure Functions (Python)** and **Azure Cosmos DB (NoSQL)**.  
This project demonstrates serverless API development, local testing, and cloud deployment on Azure.

---

## 🚀 Project Overview

This application exposes REST APIs to manage products (Create, Read, Update, Delete).  
It is built using:

- Azure Functions (HTTP Triggers)
- Python
- Azure Cosmos DB (SQL API)
- Azure Functions Core Tools
- VS Code
- Deployment via Azure CLI

The flow:
- Develop locally  
- Test with Thunder Client/Postman  
- Deploy to Azure  
- Use Cosmos DB as backend storage  

---

## 🏗️ Architecture

```
Client (Thunder / Postman / Browser)
          |
          v
 Azure Function App (Python HTTP Triggers)
          |
          v
     Azure Cosmos DB (Products Collection)
```

---

## 📂 Project Structure

```
azure-products-api/
│
├── CreateProduct/
│   └── __init__.py
├── GetProducts/
│   └── __init__.py
├── GetProductById/
│   └── __init__.py
├── UpdateProduct/
│   └── __init__.py
├── DeleteProduct/
│   └── __init__.py
│
├── host.json
├── requirements.txt
├── local.settings.example.json
└── README.md
```

---

## ⚙️ Local Development Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/paartheev-boora/azure-products-api.git
cd azure-products-api
```

### 2️⃣ Create Virtual Environment
```sh
python -m venv .venv
```

### 3️⃣ Activate Environment (Windows CMD)
```sh
.\.venv\Scripts\activate.bat
```

### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 5️⃣ Add Local Configuration

Create a file named:

```
local.settings.json
```

Paste:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "COSMOS_CONN_STRING": "<your primary connection string>",
    "COSMOS_DB": "ProductsDB",
    "COSMOS_CONTAINER": "Products"
  }
}
```

⚠️ Do NOT commit secrets to GitHub.  
This file is ignored with `.gitignore`.  
Use `local.settings.example.json` for public reference.

---

### 6️⃣ Run the Project Locally

```sh
func start
```

Your functions run at:

```
http://localhost:7071/api/
```

---

## 🧪 API Endpoints

### 📌 1. Create Product  
**POST** `/api/CreateProduct`

#### Sample JSON:
```json
{
  "id": "p1",
  "name": "Keyboard",
  "price": 499
}
```

---

### 📌 2. Get All Products  
**GET** `/api/GetProducts`

Response:
```json
[
  {
    "id": "p1",
    "name": "Keyboard",
    "price": 499
  }
]
```

---

### 📌 3. Get Product by ID  
**GET** `/api/GetProductById/{id}`

---

### 📌 4. Update Product  
**PUT** `/api/UpdateProduct/{id}`

Sample:
```json
{
  "price": 699,
  "name": "Gaming Keyboard"
}
```

---

### 📌 5. Delete Product  
**DELETE** `/api/DeleteProduct/{id}`

---

## ☁️ Azure Deployment

### 1️⃣ Login to Azure
```sh
az login
```

### 2️⃣ Deploy to Azure Function App
```sh
func azure functionapp publish <your-function-app-name>
```

Example:
```sh
func azure functionapp publish product-api-func
```

After deployment, Azure generates public URLs like:

```
https://product-api-func.azurewebsites.net/api/CreateProduct
```

---

## 🗄️ Cosmos DB Setup

1. Create Azure Cosmos DB (NoSQL)
2. Create database:
   ```
   ProductsDB
   ```
3. Create container:
   ```
   Products
   Partition Key → /id
   ```
4. Add connection string to:
   - `local.settings.json`
   - Azure Portal → Function App → Configuration

---

## 📦 Requirements

```
azure-functions
azure-cosmos
```

---

## 🛡️ Security Notes

- Never commit real `local.settings.json`
- Use `local.settings.example.json` instead
- Store production keys in Azure Function App → Application Settings

---

## 🤝 Contributions
PRs and issues are welcome.

---

## 👨‍💻 Author
**Paartheev Boora**  
GitHub: https://github.com/paartheev-boora
