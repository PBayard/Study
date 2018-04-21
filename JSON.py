import json

# JSON can contain values of only the following data types: strings, integers, floats,
# Booleans, lists, dictionaries, and NoneType . JSON cannot represent Python-specific
# objects, such as File objects, CSV Reader or Writer objects, Regex objects, or
# Selenium WebElement objects

# check quickWeather.py and

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData) # pass it a string of JSON data
print(jsonDataAsPythonValue) # JSON strig returns data as a Python dictionary. Python
# dictionaries are not ordered

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue) # translate a Python value into a string of JSON-formatted data
print(stringOfJsonData)

parsed_json = json.loads(pythonValue) # decoding then use as normal dict
print(parsed_json['isCat'])

# Get tweet
for status in tweepy.Cursor(api.followers).items(5):
    # Process the status here
    print(status)
    json_str = json.dumps(status._json) # make it string
    data = json.loads(json_str) # make it dict
    print(json.dumps(data, sort_keys=True, indent=4)) # pretty print