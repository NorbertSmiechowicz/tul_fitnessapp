package com.FitFoodApp.web.service;

import com.FitFoodApp.web.dto.ExerciseDto;
import com.FitFoodApp.web.models.Exercise;

import java.util.List;

public interface ExerciseService {
    void createExercise(int userId, ExerciseDto exerciseDto);
    List<ExerciseDto> findAllExercises();
}
