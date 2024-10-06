import React from 'react';
import { View, Text, FlatList, TouchableOpacity, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const API_KEY = 'YOUR_ESV_API_KEY_HERE'; // Replace with your actual API key

const newTestamentBooks = [
  'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians',
  'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians',
  '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter',
  '1 John', '2 John', '3 John', 'Jude', 'Revelation'
];

const NewTestamentScreen = () => {
  const navigation = useNavigation();

  const renderBookItem = ({ item }) => (
    <View style={styles.bookItem}>
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate('BibleReading', { book: item, testament: 'New' })}
      >
        <Text style={styles.buttonText}>Read {item}</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate('Quiz', { book: item, testament: 'New' })}
      >
        <Text style={styles.buttonText}>Take Quiz</Text>
      </TouchableOpacity>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>New Testament</Text>
      <FlatList
        data={newTestamentBooks}
        renderItem={renderBookItem}
        keyExtractor={(item) => item}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f0f0f0',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  bookItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  button: {
    backgroundColor: '#4a90e2',
    padding: 10,
    borderRadius: 5,
    flex: 1,
    marginHorizontal: 5,
  },
  buttonText: {
    color: 'white',
    textAlign: 'center',
  },
});

export default NewTestamentScreen;
