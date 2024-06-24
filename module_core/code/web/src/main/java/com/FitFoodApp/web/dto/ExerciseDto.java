package com.FitFoodApp.web.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;

import java.time.LocalDateTime;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class ExerciseDto {
    private int id;
    private LocalDateTime date;
    private String name;
    private String description;
    private String visualisationPhoto;
    private String target;
    private int load;
    private int reps;
    private int workoutTime;
    private boolean custom;
}
