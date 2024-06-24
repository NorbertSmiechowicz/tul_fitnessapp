package com.FitFoodApp.web.models;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Entity
@Table(name = "exercises")
public class Exercise {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    @CreationTimestamp
    private LocalDateTime date;
    private String name;
    private String description;
    private String visualisationPhoto;
    private String target;
    private int load;
    private int reps;
    private int workoutTime;
    private boolean custom;

    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
}