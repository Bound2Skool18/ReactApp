import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, TouchableOpacity, FlatList, StyleSheet, Alert, Switch } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useAppContext } from '../utils/AppContext';

const NotesModal = ({ onClose, currentBook }) => {
  const [notes, setNotes] = useState([]);
  const [currentNote, setCurrentNote] = useState('');
  const [filterByCurrentBook, setFilterByCurrentBook] = useState(false);
  const { theme } = useAppContext();

  useEffect(() => {
    loadNotes();
  }, []);

  const loadNotes = async () => {
    try {
      const savedNotes = await AsyncStorage.getItem('notes');
      if (savedNotes !== null) {
        setNotes(JSON.parse(savedNotes));
      }
    } catch (error) {
      console.error('Error loading notes:', error);
    }
  };

  const saveNote = async () => {
    if (currentNote.trim() === '') {
      Alert.alert('Error', 'Note cannot be empty');
      return;
    }
    const newNote = { id: Date.now().toString(), text: currentNote, book: currentBook };
    const updatedNotes = [...notes, newNote];
    setNotes(updatedNotes);
    setCurrentNote('');
    try {
      await AsyncStorage.setItem('notes', JSON.stringify(updatedNotes));
    } catch (error) {
      console.error('Error saving note:', error);
    }
  };

  const deleteNote = async (id) => {
    const updatedNotes = notes.filter(note => note.id !== id);
    setNotes(updatedNotes);
    try {
      await AsyncStorage.setItem('notes', JSON.stringify(updatedNotes));
    } catch (error) {
      console.error('Error deleting note:', error);
    }
  };

  const filteredNotes = filterByCurrentBook ? notes.filter(note => note.book === currentBook) : notes;

  const renderItem = ({ item }) => (
    <View style={[styles.noteItem, { backgroundColor: theme === 'dark' ? '#2c3e50' : '#ecf0f1' }]}>
      <Text style={[styles.noteText, { color: theme === 'dark' ? '#fff' : '#2c3e50' }]}>{item.text}</Text>
      <Text style={[styles.noteBook, { color: theme === 'dark' ? '#bdc3c7' : '#7f8c8d' }]}>Book: {item.book}</Text>
      <TouchableOpacity onPress={() => deleteNote(item.id)} style={styles.deleteButton}>
        <Text style={styles.deleteButtonText}>Delete</Text>
      </TouchableOpacity>
    </View>
  );

  return (
    <View style={[styles.modalContainer, { backgroundColor: theme === 'dark' ? '#121212' : '#f0f0f0' }]}>
      <TouchableOpacity onPress={onClose} style={styles.closeButton}>
        <Text style={[styles.closeButtonText, { color: theme === 'dark' ? '#fff' : '#000' }]}>Close</Text>
      </TouchableOpacity>
      <TextInput
        style={[styles.input, { backgroundColor: theme === 'dark' ? '#2c3e50' : '#fff', color: theme === 'dark' ? '#fff' : '#000' }]}
        value={currentNote}
        onChangeText={setCurrentNote}
        placeholder="Enter your note here"
        placeholderTextColor={theme === 'dark' ? '#bdc3c7' : '#95a5a6'}
        multiline
      />
      <TouchableOpacity onPress={saveNote} style={styles.saveButton}>
        <Text style={styles.saveButtonText}>Save Note</Text>
      </TouchableOpacity>
      <View style={styles.filterContainer}>
        <Text style={[styles.filterText, { color: theme === 'dark' ? '#fff' : '#000' }]}>
          Filter by current book ({currentBook})
        </Text>
        <Switch
          value={filterByCurrentBook}
          onValueChange={setFilterByCurrentBook}
          trackColor={{ false: "#767577", true: "#81b0ff" }}
          thumbColor={filterByCurrentBook ? "#f5dd4b" : "#f4f3f4"}
        />
      </View>
      <FlatList
        data={filteredNotes}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        style={styles.notesList}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  modalContainer: {
    flex: 1,
    padding: 20,
    marginTop: 50,
  },
  closeButton: {
    alignSelf: 'flex-end',
    padding: 10,
  },
  closeButtonText: {
    fontSize: 18,
  },
  input: {
    height: 100,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    padding: 10,
    textAlignVertical: 'top',
  },
  saveButton: {
    backgroundColor: '#3498db',
    padding: 10,
    borderRadius: 5,
    alignItems: 'center',
    marginBottom: 20,
  },
  saveButtonText: {
    color: '#fff',
    fontSize: 16,
  },
  filterContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  filterText: {
    fontSize: 16,
  },
  notesList: {
    flex: 1,
  },
  noteItem: {
    padding: 10,
    marginBottom: 10,
    borderRadius: 5,
  },
  noteText: {
    fontSize: 16,
  },
  noteBook: {
    fontSize: 12,
    marginTop: 5,
  },
  deleteButton: {
    backgroundColor: '#e74c3c',
    padding: 5,
    borderRadius: 3,
    alignSelf: 'flex-end',
    marginTop: 5,
  },
  deleteButtonText: {
    color: '#fff',
    fontSize: 12,
  },
});

export default NotesModal;
