import React, { useState } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';

const readingPlans = [
  { id: '1', title: 'New Testament in 90 Days' },
  { id: '2', title: 'Old Testament in 180 Days' },
  { id: '3', title: 'Whole Bible in 365 Days' },
  { id: '4', title: 'Psalms in 30 Days' },
  { id: '5', title: 'Proverbs in 31 Days' },
];

const ReadingPlanScreen = () => {
  const [selectedPlan, setSelectedPlan] = useState(null);

  const renderItem = ({ item }) => (
    <TouchableOpacity
      style={[styles.planItem, selectedPlan === item.id && styles.selectedPlan]}
      onPress={() => setSelectedPlan(item.id)}
    >
      <Text style={styles.planTitle}>{item.title}</Text>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Select a Reading Plan</Text>
      <FlatList
        data={readingPlans}
        renderItem={renderItem}
        keyExtractor={item => item.id}
      />
      {selectedPlan && (
        <TouchableOpacity style={styles.startButton}>
          <Text style={styles.startButtonText}>Start Plan</Text>
        </TouchableOpacity>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f0f0f0',
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#2c3e50',
  },
  planItem: {
    backgroundColor: '#fff',
    padding: 20,
    marginBottom: 10,
    borderRadius: 5,
  },
  selectedPlan: {
    backgroundColor: '#3498db',
  },
  planTitle: {
    fontSize: 18,
    color: '#2c3e50',
  },
  startButton: {
    backgroundColor: '#2ecc71',
    padding: 15,
    borderRadius: 5,
    alignItems: 'center',
    marginTop: 20,
  },
  startButtonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
});

export default ReadingPlanScreen;
