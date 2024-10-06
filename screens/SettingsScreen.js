import React, { useContext } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ScrollView } from 'react-native';
import { useAppContext } from '../utils/AppContext';

const SettingsScreen = () => {
  const { theme, toggleTheme, fontSize, changeFontSize } = useAppContext();

  return (
    <ScrollView style={[styles.container, { backgroundColor: theme === 'dark' ? '#121212' : '#f0f0f0' }]}>
      <Text style={[styles.title, { color: theme === 'dark' ? '#fff' : '#000' }]}>Settings</Text>
      
      <View style={styles.section}>
        <Text style={[styles.sectionTitle, { color: theme === 'dark' ? '#fff' : '#000' }]}>Theme</Text>
        <TouchableOpacity
          style={[styles.option, theme === 'light' && styles.selectedOption]}
          onPress={toggleTheme}
        >
          <Text style={{ color: theme === 'dark' ? '#fff' : '#000' }}>Light</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.option, theme === 'dark' && styles.selectedOption]}
          onPress={toggleTheme}
        >
          <Text style={{ color: theme === 'dark' ? '#fff' : '#000' }}>Dark</Text>
        </TouchableOpacity>
      </View>
      
      <View style={styles.section}>
        <Text style={[styles.sectionTitle, { color: theme === 'dark' ? '#fff' : '#000' }]}>Font Size</Text>
        <TouchableOpacity
          style={[styles.option, fontSize === 'small' && styles.selectedOption]}
          onPress={() => changeFontSize('small')}
        >
          <Text style={{ color: theme === 'dark' ? '#fff' : '#000' }}>Small</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.option, fontSize === 'medium' && styles.selectedOption]}
          onPress={() => changeFontSize('medium')}
        >
          <Text style={{ color: theme === 'dark' ? '#fff' : '#000' }}>Medium</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.option, fontSize === 'large' && styles.selectedOption]}
          onPress={() => changeFontSize('large')}
        >
          <Text style={{ color: theme === 'dark' ? '#fff' : '#000' }}>Large</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  section: {
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  option: {
    padding: 10,
    borderWidth: 1,
    borderColor: '#ccc',
    marginBottom: 5,
  },
  selectedOption: {
    backgroundColor: '#e0e0e0',
  },
});

export default SettingsScreen;