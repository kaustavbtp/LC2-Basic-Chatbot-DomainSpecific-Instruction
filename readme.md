<!-- -- cd .\PRJ3\ -->
<!-- .\env3\Scripts\activate
pip install -r requirements.txt
python .\app_langserve_api.py  -->

# Check python version
python --version

# check list of packages installed
pip list

# Check some specific package version which got installed
pip show <package-name>

# Activate python Environment
python -m venv env-nlp-chat
.\env-nlp-chat\Scripts\activate


# for NLTK
py -3 -m pip install nltk


# To install all the required python Packages/modules
pip install -r requirements.txt

# To install individual python Packages/Modules
pip install <module/package Name>

# To display any Install Python Package/Modules details
pip show <package_name>

# Activate the FastAPIs
uvicorn app:app --reload

# Validate the APIs and Try Out
http://127.0.0.1:8000/docs

# To execute any python file
python <fileName>.py

# To run Streamlit UI
Streamlit run <fileName>.py


# Deploy to Cloud Foundry
cf login -a <Your Subaccount API URL>


# Deploy to CF
cf push


# Test Applicaiton (Try-Out)
{
  "nlp": {
    "source": "How to create a sales order in SAP?"
  }
}

<!-- git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/kaustavbtp/LC2-Basic-Chatbot-DomainSpecific-Instruction
git push -u origin main -->