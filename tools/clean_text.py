# Module for cleaning text
# Python 2.7.14

from nltk.corpus import stopwords

# Set stopwords for functions below.
stop = stopwords.words('english')
stop.append('hello')
stop.append('hi')
stop.append('dear')
stop.append('sir')
stop.append('sirs')
stop.append('thank')
stop.append('facebook')
stop.append('twitter')
stop.append('linkedin')


def stop_clean(data_input, column):
	"""
	Function cleans text taken from dataframe by lowering all cases, removing punct and stopwords.
	
	Input:
	Data_input - Pandas Dataframe
	Column - String
	
	Output: CSV file of cleaned file for further cleaning.
	"""	
	data_input[column] = data_input[column].str.replace(r'([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})', '') # Removes emails
	data_input[column] = data_input[column].str.replace(r'<(.*?)\>', '')
	data_input[column] = data_input[column].str.replace(r'www[a-z]+', '')
	data_input[column] = data_input[column].str.replace(r'http[a-z]+', '')
	data_input[column] = data_input[column].str.replace(r'https[a-z]+', '')
	data_input[column] = data_input[column].str.replace(r'[^\w\s]', '')
	
	data_input[column] = data_input[column].str.lower().str.split()
	data_input[column] = data_input[column].apply(lambda x: [item for item in x if item not in stop])
	
	return data_input.to_csv('clean.csv', encoding='utf-8')

	
def stop_and_stem(data_input, column):
	"""
	Function cleans text taken from dataframe by lowering all cases, removing punct and stopwords.
	
	Input:
	Data_input - Pandas Dataframe
	Column - String
	
	Output: CSV file of cleaned file for further cleaning.
	"""
	from nltk.stem.snowball import SnowballStemmer
	
	data_input[column] = data_input[column].str.replace(r'([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})', '') # Removes emails
	data_input[column] = data_input[column].str.replace(r'<(.*?)\>', '')
	data_input[column] = data_input[column].str.replace(r'www[a-z]+', '')
	data_input[column] = data_input[column].str.replace(r'http[a-z]+', '')
	data_input[column] = data_input[column].str.replace(r'https[a-z]+', '')
	data_input[column] = data_input[column].str.replace(r'[^\w\s]', '')

	data_input[column] = data_input[column].str.lower().str.split()
	data_input[column] = data_input[column].apply(lambda x: [item for item in x if item not in stop])
	
	stemmer = SnowballStemmer("english")
	data_input[column] = data_input[column].apply(lambda x: [stemmer.stem(y) for y in x])
    
	return data_input.to_csv('clean.csv', encoding='utf-8')