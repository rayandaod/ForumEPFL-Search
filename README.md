# Forum EPFL Search

This is a Python script retrieving companies/startups/NGOs that _should_ match your interests based on pre-defined requirements. It is basically supposed to be a better search engine than the one provided in forum-epfl.ch .

Note: This was created during the 2023 edition of the Forum. It might require some adjustments in order to work for the following editions.

## Getting started

1. Clone this repository

```
git clone blabla
cd blabla
```

2. Install dependencies (python evironment recommended)

```pip install -r requirements.txt```

3. If you want to run the scripts again, they will need credentials to access the company lists and infos. You should therefore save your Forum EPFL credentials as environment variables under the names `FORUM_EMAIL` and `FORUM_PASSWORD`. Note: this is not the most secure way of storing these information, but it's definitely better than hardcoding them lol.

````
export FORUM_EMAIL=[your_email]
export FORUM_PASSWORDL=[your_password]
``````
   
4. If you chose to follow step 3 above, you should run 
   
   ```python login.py```
   
   It should print `<Response [200]>`

## Usage

You can either run the scripts again, or use the existing ones. If you choose the latter, please skip to Step x.

### Step 1 - Retrieve first-level informations
```python get_list.py```

The result is saved in `output/output1_list.json`

### Step 2 - Retrieve detailed informations
```python get_details.py```

The result is saved in `output/output2_details.json`

### Step 3 - Set your criteria
TODO

### Step 4 - Search for your dream companies
TODO

## Roadmap and ideas
- Get company names and links
    - Also get if they are a startup or a company or NGO/IGO
- Get descriptions
    - Either Get particular html content by inspecting tags
    - Or feed the html page to an LLM and ask to gather everything describing the company
- Ask the user their criterions
    - Company or startup or NGO/IGO
    - Particular day?
    - Skills they have
    - Level of filtering:
        - All companies that could need someone in that domain based on the description
        - Companies explicitly looking for people in that domain
- Build a prompt based on the criterions
- Run the LLM on each company description and output a yes/no answer

Other ideas:
- Additional search if the company gave a link to a job listing page
- Get some statistics on companies/startups that were present (by sector, etc)