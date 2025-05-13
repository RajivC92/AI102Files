## Current available SDK - working fine 
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Replace with your actual key and endpoint
subscription_key = "AWtJ0VRUJcqEVX8Mkd2ep5HJtREnFv5az82cXMu4aDWpfNsmOQKkJQQJ99BEACYeBjFXJ3w3AAAaACOGtpci"
endpoint = "https://llser929.cognitiveservices.azure.com/"

def authenticate_client():
    return TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(subscription_key))

def key_phrases():
    client = authenticate_client()

    documents = [
        "猫は幸せ",  # Japanese
        "Fahrt nach Stuttgart und dann zum Hotel zu Fu.",  # German
        "My cat might need to see a veterinarian.",  # English
        "A mi me encanta el fútbol!"  # Spanish
    ]

    try:
        response = client.extract_key_phrases(documents=documents)

        for idx, doc in enumerate(response):
            if not doc.is_error:
                print(f"Document {idx + 1} Key Phrases:")
                for phrase in doc.key_phrases:
                    print(f"\t{phrase}")
            else:
                print(f"Document {idx + 1} Error: {doc.error}")

    except Exception as err:
        print("Encountered exception. {}".format(err))

key_phrases()

#######################################################################################################################
## Deprecated SDK below - used in the course
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

# variables to store subscription key and root URL for the Cognitive Service resource
subscription_key = "YourKey"
endpoint = "YourEndpoint"


def authenticateclient():
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)
    return text_analytics_client


def key_phrases():
    client = authenticateclient()

    try:
        documents = [
            {"id": "1", "language": "ja", "text": "猫は幸せ"},
            {"id": "2", "language": "de",
             "text": "Fahrt nach Stuttgart und dann zum Hotel zu Fu."},
            {"id": "3", "language": "en",
             "text": "My cat might need to see a veterinarian."},
            {"id": "4", "language": "es", "text": "A mi me encanta el fútbol!"}
        ]

        for document in documents:
            print(
                "Asking key-phrases on '{}' (id: {})".format(document['text'], document['id']))

        response = client.key_phrases(documents=documents)

        for document in response.documents:
            print("Document Id: ", document.id)
            print("\tKey Phrases:")
            for phrase in document.key_phrases:
                print("\t\t", phrase)

    except Exception as err:
        print("Encountered exception. {}".format(err))


key_phrases()
