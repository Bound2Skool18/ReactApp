import React from 'react';
import { TouchableOpacity } from 'react-native';
import { NavigationContainer, DefaultTheme, DarkTheme } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { createStackNavigator } from '@react-navigation/stack';
import Icon from 'react-native-vector-icons/Ionicons';
import { AppProvider, useAppContext } from './utils/AppContext';

import HomeScreen from './screens/HomeScreen';
import BibleReadingScreen from './screens/BibleReadingScreen';
import QuizScreen from './screens/QuizScreen';
import SearchScreen from './screens/SearchScreen';
import SettingsScreen from './screens/SettingsScreen';
import ReadingPlanScreen from './screens/ReadingPlanScreen';
import TodaysVerseScreen from './screens/TodaysVerseScreen';
import NotesScreen from './screens/NotesScreen';

const Drawer = createDrawerNavigator();
const Stack = createStackNavigator();

const customLightTheme = {
  ...DefaultTheme,
  colors: {
    ...DefaultTheme.colors,
    primary: '#3498db',
    background: '#f0f0f0',
    card: '#fff',
    text: '#2c3e50',
  },
};

const customDarkTheme = {
  ...DarkTheme,
  colors: {
    ...DarkTheme.colors,
    primary: '#3498db',
    background: '#121212',
    card: '#1e1e1e',
    text: '#ffffff',
  },
};

const MainStack = () => {
  const { theme } = useAppContext();
  
  return (
    <Stack.Navigator>
      <Stack.Screen 
        name="HomeScreen" 
        component={HomeScreen}
        options={({ navigation }) => ({
          title: 'Bible Study App',
          headerLeft: () => (
            <TouchableOpacity onPress={() => navigation.openDrawer()}>
              <Icon name="menu" size={24} color={theme === 'dark' ? '#fff' : '#000'} style={{ marginLeft: 10 }} />
            </TouchableOpacity>
          ),
        })}
      />
      <Stack.Screen name="BibleReading" component={BibleReadingScreen} />
      <Stack.Screen name="Quiz" component={QuizScreen} />
      <Stack.Screen name="Search" component={SearchScreen} />
      <Stack.Screen name="ReadingPlan" component={ReadingPlanScreen} />
      <Stack.Screen name="TodaysVerse" component={TodaysVerseScreen} />
      <Stack.Screen name="Notes" component={NotesScreen} />
    </Stack.Navigator>
  );
};

const AppContent = () => {
  const { theme } = useAppContext();
  
  return (
    <NavigationContainer theme={theme === 'dark' ? customDarkTheme : customLightTheme}>
      <Drawer.Navigator initialRouteName="Home">
        <Drawer.Screen 
          name="Home" 
          component={MainStack}
          options={{ headerShown: false }}
        />
        <Drawer.Screen name="Notes" component={NotesScreen} />
        <Drawer.Screen name="Settings" component={SettingsScreen} />
      </Drawer.Navigator>
    </NavigationContainer>
  );
};

const App = () => (
  <AppProvider>
    <AppContent />
  </AppProvider>
);

export default App;
