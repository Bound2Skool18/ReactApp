import React, { useState, useEffect, useContext } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView, Alert } from 'react-native';
import { useNavigation, useRoute } from '@react-navigation/native';
import { AppContext } from '../utils/AppContext';
import { saveQuizProgress, getQuizProgress } from '../utils/UserProgress';
import { quizQuestions } from '../utils/quizData';

const QuizScreen = () => {
  const navigation = useNavigation();
  const route = useRoute();
  const { book, testament } = route.params;
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [showScore, setShowScore] = useState(false);
  const [difficulty, setDifficulty] = useState('medium');
  const [incorrectAnswers, setIncorrectAnswers] = useState([]);
  const { theme, fontSize } = useContext(AppContext);

  const questions = quizQuestions[book] && quizQuestions[book][difficulty] 
    ? quizQuestions[book][difficulty] 
    : [];

  useEffect(() => {
    loadQuizProgress();
  }, []);

  const loadQuizProgress = async () => {
    const savedProgress = await getQuizProgress(book);
    if (savedProgress) {
      Alert.alert(
        'Previous Score',
        `You scored ${savedProgress} on your last attempt. Do you want to try again?`,
        [
          { text: 'No', onPress: () => navigation.goBack() },
          { text: 'Yes', onPress: () => resetQuiz() }
        ]
      );
    }
  };

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setScore(0);
    setShowScore(false);
    setIncorrectAnswers([]);
  };

  const handleAnswerOptionClick = (isCorrect) => {
    if (isCorrect) {
      setScore(score + 1);
    } else {
      setIncorrectAnswers([...incorrectAnswers, currentQuestion]);
    }

    const nextQuestion = currentQuestion + 1;
    if (nextQuestion < questions.length) {
      setCurrentQuestion(nextQuestion);
    } else {
      setShowScore(true);
      saveQuizProgress(book, score + (isCorrect ? 1 : 0));
    }
  };

  const handleDifficultyChange = (newDifficulty) => {
    setDifficulty(newDifficulty);
    resetQuiz();
  };

  const reviewIncorrectAnswers = () => {
    Alert.alert(
      'Incorrect Answers',
      incorrectAnswers.map((index) => 
        `Q: ${questions[index].questionText}\nA: ${questions[index].answerOptions.find(a => a.isCorrect).answerText}`
      ).join('\n\n'),
      [{ text: 'OK' }]
    );
  };

  return (
    <ScrollView contentContainerStyle={[styles.container, { backgroundColor: theme === 'dark' ? '#333' : '#f0f0f0' }]}>
      {!showScore ? (
        <>
          <View style={styles.difficultyContainer}>
            {['easy', 'medium', 'hard'].map((d) => (
              <TouchableOpacity
                key={d}
                style={[styles.difficultyButton, difficulty === d && styles.selectedDifficulty]}
                onPress={() => handleDifficultyChange(d)}
              >
                <Text style={[styles.difficultyButtonText, { color: theme === 'dark' ? '#fff' : '#000' }]}>{d.charAt(0).toUpperCase() + d.slice(1)}</Text>
              </TouchableOpacity>
            ))}
          </View>
          <View style={styles.questionSection}>
            <Text style={[styles.questionCount, { color: theme === 'dark' ? '#fff' : '#000', fontSize: fontSize === 'small' ? 16 : fontSize === 'large' ? 20 : 18 }]}>
              Question {currentQuestion + 1}/{questions.length}
            </Text>
            <Text style={[styles.questionText, { color: theme === 'dark' ? '#fff' : '#000', fontSize: fontSize === 'small' ? 20 : fontSize === 'large' ? 24 : 22 }]}>
              {questions[currentQuestion].questionText}
            </Text>
          </View>
          <View style={styles.answerSection}>
            {questions[currentQuestion].answerOptions.map((answerOption, index) => (
              <TouchableOpacity
                key={index}
                style={[
                  styles.answerButton,
                  { backgroundColor: theme === 'dark' ? '#555' : '#4a90e2' }
                ]}
                onPress={() => handleAnswerOptionClick(answerOption.isCorrect)}
              >
                <Text style={[
                  styles.answerButtonText,
                  { fontSize: fontSize === 'small' ? 18 : fontSize === 'large' ? 22 : 20 }
                ]}>
                  {answerOption.answerText}
                </Text>
              </TouchableOpacity>
            ))}
          </View>
        </>
      ) : (
        <View style={styles.scoreSection}>
          <Text style={[styles.scoreText, { color: theme === 'dark' ? '#fff' : '#000', fontSize: fontSize === 'small' ? 22 : fontSize === 'large' ? 26 : 24 }]}>
            You scored {score} out of {questions.length}
          </Text>
          <TouchableOpacity
            style={[styles.largeButton, { backgroundColor: theme === 'dark' ? '#555' : '#4a90e2' }]}
            onPress={reviewIncorrectAnswers}
          >
            <Text style={[styles.largeButtonText, { fontSize: fontSize === 'small' ? 18 : fontSize === 'large' ? 22 : 20 }]}>
              Review Incorrect Answers
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.largeButton, { backgroundColor: theme === 'dark' ? '#555' : '#4a90e2' }]}
            onPress={resetQuiz}
          >
            <Text style={[styles.largeButtonText, { fontSize: fontSize === 'small' ? 18 : fontSize === 'large' ? 22 : 20 }]}>
              Try Again
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.largeButton, { backgroundColor: theme === 'dark' ? '#555' : '#4a90e2' }]}
            onPress={() => navigation.navigate('Home')}
          >
            <Text style={[styles.largeButtonText, { fontSize: fontSize === 'small' ? 18 : fontSize === 'large' ? 22 : 20 }]}>
              Return to Home
            </Text>
          </TouchableOpacity>
        </View>
      )}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  // ... existing styles ...
  difficultyContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 20,
  },
  difficultyButton: {
    padding: 10,
    borderRadius: 5,
    borderWidth: 1,
    borderColor: '#ccc',
  },
  selectedDifficulty: {
    backgroundColor: '#4a90e2',
  },
  difficultyButtonText: {
    fontWeight: 'bold',
  },
  answerSection: {
    width: '100%',
    marginTop: 20,
  },
  answerButton: {
    backgroundColor: '#4a90e2',
    padding: 20,
    borderRadius: 10,
    marginVertical: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  answerButtonText: {
    color: 'white',
    fontSize: 20,
    textAlign: 'center',
  },
  scoreSection: {
    alignItems: 'center',
    justifyContent: 'center',
    width: '100%',
    paddingVertical: 20,
  },
  scoreText: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  largeButton: {
    backgroundColor: '#4a90e2',
    padding: 20,
    borderRadius: 10,
    marginVertical: 10,
    width: '90%', // Make the button wider
    alignItems: 'center',
    justifyContent: 'center',
  },
  largeButtonText: {
    color: 'white',
    fontSize: 20,
    textAlign: 'center',
    fontWeight: 'bold',
  },
  // ... other styles ...
});

export default QuizScreen;