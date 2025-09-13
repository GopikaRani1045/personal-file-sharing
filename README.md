
A **serverless file-sharing application** built with **AWS Lambda, API Gateway, and S3**, with a simple **frontend in HTML, CSS, and JavaScript**.  
This project allows users to securely **upload and download files** via API endpoints without directly exposing the S3 bucket.

---

## ⚡ Features
- 🔒 **Secure File Storage** using Amazon S3  
- 🖥️ **Frontend Web App** (HTML, CSS, JS)  
- 🌐 **REST API** with AWS API Gateway  
- ⚙️ **Lambda Functions** for file upload & download  
- 🛠️ **CORS Configured** to work with the browser  
- 📑 Documentation included (\`/docs\` folder)  

---

## 🏗️ Architecture
1. **Frontend** → Calls API Gateway endpoints  
2. **API Gateway** → Triggers Lambda functions  
3. **Lambda Functions** → Handle file upload/download logic  
4. **Amazon S3** → Stores the actual files  

---

## 📦 Project Structure
\`\`\`
personal-file-sharing/
│
├── backend/                  # Lambda functions
│   ├── upload_lambda.py
│   └── download_lambda.py
│
├── frontend/                 # Client-side code
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── docs/                     # Documentation
│   └── Personal_File_Sharing_Project_With_Cover.pdf
│
└── README.md                 # Project guide
\`\`\`

---

## 🚀 Setup Instructions

### 1. Backend (AWS)
- Create an **S3 bucket** in AWS  
- Create an **IAM Role** with S3 + Lambda permissions  
- Deploy the \`upload_lambda.py\` and \`download_lambda.py\` functions  
- Connect them to **API Gateway** endpoints (\`/upload\`, \`/download\`)  
- Enable **CORS** for both endpoints  

### 2. Frontend
- Place your files in \`/frontend\`  
- Update \`script.js\` with your API Gateway URLs:  
  \`\`\`javascript
  const uploadUrl = \"https://<api-id>.execute-api.<region>.amazonaws.com/dev/upload\";
  const downloadUrl = \"https://<api-id>.execute-api.<region>.amazonaws.com/dev/download\";
  \`\`\`

- Open \`index.html\` in a browser → Upload & download files 🎉  

---

## 🧪 Testing
- Test **Lambda functions** with AWS Console test events  
- Test APIs with **Postman**  
- Use the **frontend** for real file sharing  

---

## 🛠️ Errors Faced & Fixes
- ❌ *CORS error in browser* → ✅ Fixed by enabling CORS in API Gateway  
- ❌ *Internal Server Error* → ✅ Debugged by adding \`queryStringParameters\` in test event  
- ❌ *Push rejected in GitHub* → ✅ Solved using \`git pull --rebase\`  

---

## 📸 Screenshots
(Add your screenshots here later — frontend upload/download, S3 bucket view, Postman tests)

---

## ✨ Author
👩‍💻 **Gopika Rani**  
📅 2025  
" > README.md

# 3. Stage the new README
git add README.md

# 4. Commit changes
git commit -m "Added detailed README.md with project documentation"

# 5. Push to GitHub
git push origin main

