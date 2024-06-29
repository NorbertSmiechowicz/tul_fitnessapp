package com.FitFoodApp.web.controller;

import com.FitFoodApp.web.dto.ExerciseDto;
import com.FitFoodApp.web.models.Exercise;
import com.FitFoodApp.web.service.ExerciseService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller
public class ExerciseController {
    private ExerciseService exerciseService;

    public ExerciseController(ExerciseService exerciseService) {
        this.exerciseService = exerciseService;
    }

    @GetMapping("/exercises/{exerciseId}")
    public String ViewEvent(@PathVariable("exerciseId") Integer exerciseId, Model model) {
        ExerciseDto exerciseDto = exerciseService.findByExerciseId(exerciseId);
        model.addAttribute("exercise", exerciseDto);
        return "exercises-detail";
    }

    @GetMapping("/exercises")
    public String exerciseList(Model model) {
        List<ExerciseDto> exercises = exerciseService.findAllExercises();
        model.addAttribute("exercises", exercises);
        return "exercises-list";
    }

    @GetMapping("/exercises/{userId}/new")
    public String createExerciseForm(@PathVariable("userId") int userId, Model model) {
        Exercise exercise = new Exercise();
        model.addAttribute("userId", userId);
        model.addAttribute("exercise", exercise);
        return "exercises-create";
    }

    @PostMapping("/exercises/{userId}")
    public String createExercise(@PathVariable("userId") int userId,
                                 @ModelAttribute("exercise") ExerciseDto exerciseDto,
                                 Model model) {
        exerciseService.createExercise(userId, exerciseDto);
        return "redirect:/users/" + userId;
    }
}
