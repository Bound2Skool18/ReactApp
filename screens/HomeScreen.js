import React, { useState } from 'react';
import { View, StyleSheet, TouchableOpacity, Text, ImageBackground, ScrollView } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { Picker } from '@react-native-picker/picker';
import Icon from 'react-native-vector-icons/Ionicons';
import { useAppContext } from '../utils/AppContext';

const oldTestamentBooks = [
  'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth',
  '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra',
  'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Song of Solomon',
  'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos',
  'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi'
];

const newTestamentBooks = [
  'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians',
  'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians',
  '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter',
  '1 John', '2 John', '3 John', 'Jude', 'Revelation'
];

const HomeScreen = () => {
  const navigation = useNavigation();
  const { theme } = useAppContext();
  const [selectedOldTestamentBook, setSelectedOldTestamentBook] = useState('');
  const [selectedNewTestamentBook, setSelectedNewTestamentBook] = useState('');

  const handleReadBook = (book, testament) => {
    navigation.navigate('BibleReading', { book, testament });
  };

  const handleTakeQuiz = (book, testament) => {
    navigation.navigate('Quiz', { book, testament });
  };

  return (
    <ScrollView style={[styles.container, { backgroundColor: theme === 'dark' ? '#121212' : '#f0f0f0' }]}>
      <ImageBackground
        source={require('../assets/bible-background.jpg')}
        style={styles.header}
      >
        <Text style={styles.headerText}>Bible Study App</Text>
      </ImageBackground>
      
      <View style={[styles.quickAccessContainer, { backgroundColor: theme === 'dark' ? '#1e1e1e' : '#3498db' }]}>
        <TouchableOpacity 
          style={styles.quickAccessButton}
          onPress={() => navigation.navigate('TodaysVerse')}
        >
          <Icon name="book-outline" size={24} color="#fff" />
          <Text style={styles.quickAccessText}>Today's Verse</Text>
        </TouchableOpacity>
        <TouchableOpacity 
          style={styles.quickAccessButton}
          onPress={() => navigation.navigate('ReadingPlan')}
        >
          <Icon name="calendar-outline" size={24} color="#fff" />
          <Text style={styles.quickAccessText}>Reading Plan</Text>
        </TouchableOpacity>
        <TouchableOpacity 
          style={styles.quickAccessButton}
          onPress={() => navigation.navigate('Search')}
        >
          <Icon name="search-outline" size={24} color="#fff" />
          <Text style={styles.quickAccessText}>Search</Text>
        </TouchableOpacity>
        <TouchableOpacity 
          style={styles.quickAccessButton}
          onPress={() => navigation.navigate('Notes')}
        >
          <Icon name="create-outline" size={24} color="#fff" />
          <Text style={styles.quickAccessText}>Notes</Text>
        </TouchableOpacity>
      </View>

      <View style={[styles.testamentSection, { backgroundColor: theme === 'dark' ? '#1e1e1e' : '#fff' }]}>
        <Text style={[styles.sectionTitle, { color: theme === 'dark' ? '#fff' : '#2c3e50' }]}>Old Testament</Text>
        <Picker
          selectedValue={selectedOldTestamentBook}
          style={[styles.picker, { backgroundColor: theme === 'dark' ? '#2c3e50' : '#ecf0f1', color: theme === 'dark' ? '#fff' : '#000' }]}
          onValueChange={(itemValue) => setSelectedOldTestamentBook(itemValue)}
        >
          <Picker.Item label="Select a book" value="" />
          {oldTestamentBooks.map((book) => (
            <Picker.Item key={book} label={book} value={book} color={theme === 'dark' ? '#fff' : '#000'} />
          ))}
        </Picker>
        <View style={styles.buttonContainer}>
          <TouchableOpacity
            style={styles.button}
            onPress={() => handleReadBook(selectedOldTestamentBook, 'Old')}
            disabled={!selectedOldTestamentBook}
          >
            <Text style={styles.buttonText}>Read</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.button}
            onPress={() => handleTakeQuiz(selectedOldTestamentBook, 'Old')}
            disabled={!selectedOldTestamentBook}
          >
            <Text style={styles.buttonText}>Quiz</Text>
          </TouchableOpacity>
        </View>
      </View>

      <View style={[styles.testamentSection, { backgroundColor: theme === 'dark' ? '#1e1e1e' : '#fff' }]}>
        <Text style={[styles.sectionTitle, { color: theme === 'dark' ? '#fff' : '#2c3e50' }]}>New Testament</Text>
        <Picker
          selectedValue={selectedNewTestamentBook}
          style={[styles.picker, { backgroundColor: theme === 'dark' ? '#2c3e50' : '#ecf0f1', color: theme === 'dark' ? '#fff' : '#000' }]}
          onValueChange={(itemValue) => setSelectedNewTestamentBook(itemValue)}
        >
          <Picker.Item label="Select a book" value="" />
          {newTestamentBooks.map((book) => (
            <Picker.Item key={book} label={book} value={book} color={theme === 'dark' ? '#fff' : '#000'} />
          ))}
        </Picker>
        <View style={styles.buttonContainer}>
          <TouchableOpacity
            style={styles.button}
            onPress={() => handleReadBook(selectedNewTestamentBook, 'New')}
            disabled={!selectedNewTestamentBook}
          >
            <Text style={styles.buttonText}>Read</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.button}
            onPress={() => handleTakeQuiz(selectedNewTestamentBook, 'New')}
            disabled={!selectedNewTestamentBook}
          >
            <Text style={styles.buttonText}>Quiz</Text>
          </TouchableOpacity>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f0f0',
  },
  header: {
    height: 200,
    justifyContent: 'center',
    alignItems: 'center',
  },
  headerText: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#fff',
    textShadowColor: 'rgba(0, 0, 0, 0.75)',
    textShadowOffset: {width: -1, height: 1},
    textShadowRadius: 10
  },
  quickAccessContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    padding: 20,
    backgroundColor: '#3498db',
  },
  quickAccessButton: {
    alignItems: 'center',
  },
  quickAccessText: {
    color: '#fff',
    marginTop: 5,
  },
  testamentSection: {
    marginBottom: 20,
    padding: 20,
    backgroundColor: '#fff',
    borderRadius: 10,
    marginHorizontal: 10,
    marginTop: 10,
    elevation: 3,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 10,
    color: '#2c3e50',
  },
  picker: {
    backgroundColor: '#ecf0f1',
    marginBottom: 10,
    borderRadius: 5,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  button: {
    backgroundColor: '#2ecc71',
    padding: 15,
    borderRadius: 5,
    flex: 1,
    marginHorizontal: 5,
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 16,
  },
});

export default HomeScreen;


