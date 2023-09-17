
const express = require('express');
const app = express();
const path = require('path');

const port = 1250;

app.use(express.static(__dirname));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
  });
app.use(express.json());
const TextTranslationClient =
  require("@azure-rest/ai-translation-text").default;

const apiKey = "b1086f12e28a4e7ca0554666142fcedb";
const endpoint = "https://api.cognitive.microsofttranslator.com/";
const region = "centralindia";





async function main(inputText, tolanguage) {
    const translateCredential = {
      key: apiKey,
      region,
    };
    const translationClient = new TextTranslationClient(endpoint, translateCredential);
  
    const translateResponse = await translationClient.path("/translate").post({
      body: inputText,
      queryParameters: {
        to: tolanguage,
        from: "en",
      },
    });
  
    const translations = translateResponse.body;
    const translatedTexts = [];
  
    for (const translation of translations) {
      const translatedText = translation?.translations[0]?.text;
      if (translatedText) {
        translatedTexts.push(translatedText);
      }
    }
  
    return translatedTexts;
  }
  
  let toLanguageVariable = 'bn'
  app.post('/setToLanguage', (req, res) => {
    const { toLanguage } = req.body;
    toLanguageVariable = toLanguage;
    res.status(200).json({ message: 'Language selection stored successfully.' });
  });
  
  app.get('/translateText', async (req, res) => {
    try {
      const inputText1 = [{ text: "What is the sum of 5 + 3?" }];
      const translatedTexts = await main(inputText1, toLanguageVariable);
      res.json(translatedTexts); // Respond with the translated text as JSON
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  });

  app.get('/translateTextg', async (req, res) => {
    try {
      const inputText1 = [{ text: "What is the sum of 5 + 3?" }];
      const translatedTexts = await main(inputText1, "gu");
      res.json(translatedTexts); // Respond with the translated text as JSON
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  });
  
  app.get('/translateText1', async (req, res) => {
    try {
      const inputText2 = [{ text: "If you have 4 apples and you give 2 to your friend, how many apples do you have left?" }];
      const translatedTexts2 = await main(inputText2, toLanguageVariable);
      res.json(translatedTexts2);
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  });

  app.get('/translateText1g', async (req, res) => {
    try {
      const inputText2 = [{ text: "If you have 4 apples and you give 2 to your friend, how many apples do you have left?" }];
      const translatedTexts2 = await main(inputText2, "gu");
      res.json(translatedTexts2);
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  });
  
  app.get('/translateText2', async (req, res) => {
    try {
      const inputText3 = [{ text: "What is the missing number in this sequence: 2, 4, 6, __, 8?" }];
      const translatedTexts3 = await main(inputText3, toLanguageVariable);
      res.json(translatedTexts3);
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  });

  app.get('/translateText2g', async (req, res) => {
    try {
      const inputText3 = [{ text: "What is the missing number in this sequence: 2, 4, 6, __, 8?" }];
      const translatedTexts3 = await main(inputText3, "gu");
      res.json(translatedTexts3);
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  });
  
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });