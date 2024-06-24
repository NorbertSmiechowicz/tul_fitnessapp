package com.FitFoodApp.web.controller;

import com.FitFoodApp.web.models.Exercise;
import com.FitFoodApp.web.service.ExerciseService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@Controller
public class ExerciseController {
    private ExerciseService exerciseService;

    public ExerciseController(ExerciseService exerciseService) {
        this.exerciseService = exerciseService;
    }

    @GetMapping("/exercises/{userId}/new")
    public String createExerciseForm(@PathVariable("userId") int userId, Model model) {
        Exercise exercise = new Exercise();
        model.addAttribute("userId", userId);
        model.addAttribute("exercise", exercise);
        return "exercises-create";
    }
}
