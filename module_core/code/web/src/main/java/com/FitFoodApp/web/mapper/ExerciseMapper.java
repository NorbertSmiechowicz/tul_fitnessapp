package com.FitFoodApp.web.mapper;

import com.FitFoodApp.web.dto.ExerciseDto;
import com.FitFoodApp.web.models.Exercise;

public class ExerciseMapper {
    public static Exercise mapToExercise(ExerciseDto exerciseDto) {
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

    public static ExerciseDto mapToExerciseDto(Exercise exercise) {
        return ExerciseDto.builder()
                .id(exercise.getId())
                .date(exercise.getDate())
                .name(exercise.getName())
                .description(exercise.getDescription())
                .visualisationPhoto(exercise.getVisualisationPhoto())
                .target(exercise.getTarget())
                .load(exercise.getLoad())
                .reps(exercise.getReps())
                .workoutTime(exercise.getWorkoutTime())
                .custom(exercise.isCustom())
                .build();
    }
}
