# text-similarity
checking some popular library for text similarity calculation
This project and script will use for testing text similarity with more than one library such as fuzzy, spacy etc. 
Eventually I think we will use Spaciy in production because more advance and more spohisticated, extensively using. 

## Spacy using
For use of language model need to install for all languages, means for comparison need to know languages.
python -m spacy download en_core_web_lg #for english
**all necessary language packages and multiple language, install language models**
python -m spacy download en_core_web_lg #en


**if necessary the others**
{'zh':'zh_core_web_lg',
'da':'da_core_news_lg',
....
}
The problem is here, language support is not extensive. 
Still lots of big languages not supporting, maybe multiple languae option can use into unsupporting language stuations. 
Until "REALLY" necessary to use ADVANCE text_similarity algorithm we wont use this module because need to create language model, prepare training pipelines. 

But can see quality difference in main.py and its result. 

# setup virt env and install modules
(install anaconda/conda)
(open conda)
(base) >> conda create -n text_similarity python=3.10
(new_env) python -m pip install -r requirements.txt
>> also used conda spacy setup command

# RUN options (via tasks)
In vscode under TERMINAL -> RUN TASKS ... 
- RUN main APP
- RUN lintering the codes/folders
- RUN unit-test / functional-test
- RUN auto DOCS creation

# folder structure and includes
main.py #main app
README.md # how setup etc
requirements.txt
RUN.bat # *.sh
.vscode
    - tasks.json
        {pylint main app and folders, RUN app/unit-test/fn-test}
docs/
    - user guides 
        {how to run tasks,details, app et cetera}
    - auto created docs
unit_test/
    - __init__.py
    - test_x.py #files
modules/
    - __init__.py
    - modulex.py #files
