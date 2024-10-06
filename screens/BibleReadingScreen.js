import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, StyleSheet, TouchableOpacity, ActivityIndicator, TextInput, Alert, Modal } from 'react-native';
import { useNavigation, useRoute } from '@react-navigation/native';
import { saveReadingProgress } from '../utils/UserProgress';
import { saveBookmark, saveNote, getNote } from '../utils/Bookmarks';
import NotesModal from '../components/NotesModal';

const BibleReadingScreen = () => {
  const navigation = useNavigation();
  const route = useRoute();
  const { book, testament } = route.params;
  const [content, setContent] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [note, setNote] = useState('');
  const [isNotesModalVisible, setIsNotesModalVisible] = useState(false);

  useEffect(() => {
    fetchBibleContent();
    saveReadingProgress(book, 1); // Assuming we're always loading chapter 1
    loadNote();
  }, [book]);

  const loadNote = async () => {
    const savedNote = await getNote(book, 1, 1); // Assuming we're always on chapter 1, verse 1
    if (savedNote) {
      setNote(savedNote);
    }
  };

  const handleBookmark = () => {
    saveBookmark(book, 1, 1); // Assuming we're always on chapter 1, verse 1
    Alert.alert('Bookmark saved!');
  };

  const handleSaveNote = () => {
    saveNote(book, 1, 1, note); // Assuming we're always on chapter 1, verse 1
    Alert.alert('Note saved!');
  };

  const fetchBibleContent = async () => {
    setIsLoading(true);
    setError(null);
    try {
      console.log(`Fetching content for ${book}`);
      const passage = `${book} 1`; // This requests the first chapter of the book
      const response = await fetch(
        `https://labs.bible.org/api/?passage=${encodeURIComponent(passage)}&type=text`
      );
      console.log('Response status:', response.status);
      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
      }
      let text = await response.text();
      console.log('Received text length:', text.length);
      if (text.trim().length === 0) {
        throw new Error('Received empty response from API');
      }
      // Remove HTML tags
      text = text.replace(/<\/?[^>]+(>|$)/g, "");
      setContent(text);
    } catch (error) {
      console.error('Error fetching Bible content:', error);
      setError(`Error loading content: ${error.message}. Please try again later.`);
    } finally {
      setIsLoading(false);
    }
  };

  const handleFinishReading = () => {
    navigation.navigate('Quiz', { book, testament });
  };

  if (isLoading) {
    return (
      <View style={styles.container}>
        <ActivityIndicator size="large" color="#0000ff" />
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.container}>
        <Text style={styles.errorText}>{error}</Text>
        <TouchableOpacity style={styles.retryButton} onPress={fetchBibleContent}>
          <Text style={styles.retryButtonText}>Retry</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{book}</Text>
      <ScrollView style={styles.contentContainer}>
        <Text style={styles.content}>{content}</Text>
      </ScrollView>
      <TouchableOpacity style={styles.button} onPress={handleBookmark}>
        <Text style={styles.buttonText}>Bookmark</Text>
      </TouchableOpacity>
      <TextInput
        style={styles.noteInput}
        multiline
        value={note}
        onChangeText={setNote}
        placeholder="Add a note..."
      />
      <TouchableOpacity style={styles.button} onPress={handleSaveNote}>
        <Text style={styles.buttonText}>Save Note</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.finishButton} onPress={handleFinishReading}>
        <Text style={styles.finishButtonText}>Finish Reading</Text>
      </TouchableOpacity>
      <Modal
        visible={isNotesModalVisible}
        animationType="slide"
        transparent={true}
        onRequestClose={() => setIsNotesModalVisible(false)}
      >
        <NotesModal 
          onClose={() => setIsNotesModalVisible(false)}
          currentBook={book}
        />
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f0f0f0',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  contentContainer: {
    flex: 1,
    backgroundColor: 'white',
    borderRadius: 10,
    padding: 15,
  },
  content: {
    fontSize: 16,
    lineHeight: 24,
  },
  finishButton: {
    backgroundColor: '#4a90e2',
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    marginTop: 20,
  },
  finishButtonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  errorText: {
    color: 'red',
    fontSize: 16,
    textAlign: 'center',
    marginBottom: 20,
  },
  retryButton: {
    backgroundColor: '#4a90e2',
    padding: 10,
    borderRadius: 5,
    alignSelf: 'center',
  },
  retryButtonText: {
    color: 'white',
    fontSize: 16,
  },
  button: {
    backgroundColor: '#4a90e2',
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    marginTop: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  noteInput: {
    backgroundColor: 'white',
    borderRadius: 10,
    padding: 15,
    marginTop: 20,
    fontSize: 16,
    lineHeight: 24,
  },
});

export default BibleReadingScreen;
