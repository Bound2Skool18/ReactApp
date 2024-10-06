import AsyncStorage from '@react-native-async-storage/async-storage';

export const saveBookmark = async (book, chapter, verse) => {
  try {
    const key = 'bookmarks';
    const existingBookmarks = await AsyncStorage.getItem(key);
    const bookmarks = existingBookmarks ? JSON.parse(existingBookmarks) : [];
    bookmarks.push({ book, chapter, verse });
    await AsyncStorage.setItem(key, JSON.stringify(bookmarks));
  } catch (error) {
    console.error('Error saving bookmark:', error);
  }
};

export const getBookmarks = async () => {
  try {
    const key = 'bookmarks';
    const bookmarks = await AsyncStorage.getItem(key);
    return bookmarks ? JSON.parse(bookmarks) : [];
  } catch (error) {
    console.error('Error getting bookmarks:', error);
    return [];
  }
};

export const saveNote = async (book, chapter, verse, note) => {
  try {
    const key = `note_${book}_${chapter}_${verse}`;
    await AsyncStorage.setItem(key, note);
  } catch (error) {
    console.error('Error saving note:', error);
  }
};

export const getNote = async (book, chapter, verse) => {
  try {
    const key = `note_${book}_${chapter}_${verse}`;
    return await AsyncStorage.getItem(key);
  } catch (error) {
    console.error('Error getting note:', error);
    return null;
  }
};