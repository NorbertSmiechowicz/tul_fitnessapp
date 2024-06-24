package com.FitFoodApp.web.repository;

import com.FitFoodApp.web.models.Exercise;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ExerciseRepository extends JpaRepository<Exercise, Integer> {
}
