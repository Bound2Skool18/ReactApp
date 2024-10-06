import AsyncStorage from '@react-native-async-storage/async-storage';

export const saveReadingProgress = async (book, chapter) => {
  try {
    const key = `reading_progress_${book}`;
    const existingProgress = await AsyncStorage.getItem(key);
    const progress = existingProgress ? JSON.parse(existingProgress) : [];
    if (!progress.includes(chapter)) {
      progress.push(chapter);
      await AsyncStorage.setItem(key, JSON.stringify(progress));
    }
  } catch (error) {
    console.error('Error saving reading progress:', error);
  }
};

export const getReadingProgress = async (book) => {
  try {
    const key = `reading_progress_${book}`;
    const progress = await AsyncStorage.getItem(key);
    return progress ? JSON.parse(progress) : [];
  } catch (error) {
    console.error('Error getting reading progress:', error);
    return [];
  }
};

export const saveQuizProgress = async (book, score) => {
  try {
    const key = `quiz_progress_${book}`;
    await AsyncStorage.setItem(key, JSON.stringify(score));
  } catch (error) {
    console.error('Error saving quiz progress:', error);
  }
};

export const getQuizProgress = async (book) => {
  try {
    const key = `quiz_progress_${book}`;
    const score = await AsyncStorage.getItem(key);
    return score ? JSON.parse(score) : null;
  } catch (error) {
    console.error('Error getting quiz progress:', error);
    return null;
  }
};