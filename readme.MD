* This project is an API demonstration of a search engine, it just shows the backend functionality of API
* So in the search function, we use our pre computed values, which has a list of words in the summary of a book, and the counts associated with each word. Whenever a API request is made, we use these pre computed word count, and the book's summary that matches with the most number of words will be shown in the matched order accordingly.
* The searchEngine data can be prepopulated by calling populate_data method in scripts.py
* A sample data of what we are expecting is in data.json
* It serves two APIs, the first one given a query string and a maximum search limit, returns result in a JSON array
API POST URL should be something like http://127.0.0.1:8000/book/getInfo/
body is as shown below
```
{
	"query": "i wish there is a change",
	"k":3
}
```
* The second API given an array of query strings, returns the list of matched results
API POST URL should be similar to http://127.0.0.1:8000/book/getInfoList/
body should be
```
{
	"queries": ["my life change", "i love coding"],
	"k":3
}
```
