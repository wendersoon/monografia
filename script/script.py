#Importação de dados
import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Leitura do conjunto de dados de origem
df = pd.read_csv('/content/NoThemeTweets.csv')

#Remoção de dados desnecessários
new_data = df.drop(columns=['id', 'tweet_date', 'sentiment', 'query_used'])

#Função de remoção através de expressões regulares
def remove_mentions_hashtags_links(text):
    # Remove menções (começando com @)
    text = re.sub(r'@\w+', '', text)
    # Remove hashtags (começando com #)
    text = re.sub(r'#\w+', '', text)
    # Remove links (começando com http ou https)
    text = re.sub(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)', '', text)
    # Remove emojis
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001F900-\U0001F9FF"
        u"\U0001FA70-\U0001FAFF"
        u"\U00002500-\U00002BEF"
        u"\U0001F000-\U0001F02F"
        u"\U0001F0A0-\U0001F0FF"
        u"\U0001F018-\U0001F270"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F600-\U0001F64F"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F700-\U0001F77F"
        u"\U0001F780-\U0001F7FF"
        u"\U0001F800-\U0001F8FF"
        u"\U0001F900-\U0001F9FF"
        u"\U0001FA00-\U0001FA6F"
        u"\U0001FA70-\U0001FAFF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    # Remove emoticons
    emoticon_pattern = re.compile(r'(:\)|:\(|:/|:\)\)|:\(\(|:D|:C|:-\)|:-\()', flags=re.UNICODE)
    text = emoticon_pattern.sub(r'', text)
    # Remove caracteres especiais específicos
    text = re.sub(r'[)(:;/\\|+\-*=]', '', text)
    return text

# Aplica a função ao dataframe de tweets
new_data['tweet_text'] = new_data['tweet_text'].apply(remove_mentions_hashtags_links)

# Remove entradas duplicadas
sample_df = new_data.drop_duplicates(subset='tweet_text')

# Gera o texto único para a word cloud do conjunto 'df'
text = ' '.join(df['tweet_text'])

# Gera a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Exibe a word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Gera o texto único para a word cloud pós-processamento
text = ' '.join(sample_df['tweet_text'])

# Gera a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Exibe a word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Filtra entradas com número de caracteres igual ou superior a 30
sample_df = sample_df[sample_df['tweet_text'].str.len() >= 30]

# Seleciona 1200 entradas de forma aleatória sem reposição
sample_df = sample_df.sample(n=1200, replace=False)

sample_df.to_csv('/content/tweets_pre_avalicao.csv', index=False)