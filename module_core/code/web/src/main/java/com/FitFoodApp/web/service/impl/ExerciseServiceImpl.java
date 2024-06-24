package com.FitFoodApp.web.service.impl;

import com.FitFoodApp.web.dto.ExerciseDto;
import com.FitFoodApp.web.models.Exercise;
import com.FitFoodApp.web.models.User;
import com.FitFoodApp.web.repository.ExerciseRepository;
import com.FitFoodApp.web.repository.UserRepository;
import com.FitFoodApp.web.service.ExerciseService;
import org.springframework.stereotype.Service;

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

    private Exercise mapToExercise(ExerciseDto exerciseDto) {
        return Exercise.builder()
                .id(exerciseDto.getId())
                .date(exerciseDto.getDate())
                .name(exerciseDto.getName())
                .description(exerciseDto.getDescription())
                .visualisationPhoto(exerciseDto.getVisualisationPhoto())
                .target(exerciseDto.getTarget())
                .load(exerciseDto.getLoad())
                .reps(exerciseDto.getReps())
                .workoutTime(exerciseDto.getWorkoutTime())
                .custom(exerciseDto.isCustom())
                .build();
    }
}
