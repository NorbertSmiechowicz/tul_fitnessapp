package com.FitFoodApp.web.service.impl;

import com.FitFoodApp.web.dto.ExerciseDto;
import com.FitFoodApp.web.models.Exercise;
import com.FitFoodApp.web.models.User;
import com.FitFoodApp.web.repository.ExerciseRepository;
import com.FitFoodApp.web.repository.UserRepository;
import com.FitFoodApp.web.service.ExerciseService;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

import static com.FitFoodApp.web.mapper.ExerciseMapper.mapToExercise;
import static com.FitFoodApp.web.mapper.ExerciseMapper.mapToExerciseDto;

@Service
public class ExerciseServiceImpl implements ExerciseService {
    private ExerciseRepository exerciseRepository;
    private UserRepository userRepository;

    public ExerciseServiceImpl(ExerciseRepository exerciseRepository, UserRepository userRepository) {
        this.exerciseRepository = exerciseRepository;
        this.userRepository = userRepository;
    }

    @Override
    public void createExercise(int userId, ExerciseDto exerciseDto) {
        User user = userRepository.findById(userId).get();
        Exercise exercise = mapToExercise(exerciseDto);
        exercise.setUser(user);
        exerciseRepository.save(exercise);
    }

    @Override
    public List<ExerciseDto> findAllExercises() {
        List<Exercise> exercises = exerciseRepository.findAll();
        return exercises.stream().map(exercise -> mapToExerciseDto(exercise)).collect(Collectors.toList());
    }

    @Override
    public ExerciseDto findByExerciseId(Integer exerciseId) {
        Exercise exercise = exerciseRepository.findById(exerciseId).get();
        return mapToExerciseDto(exercise);
    }

}
