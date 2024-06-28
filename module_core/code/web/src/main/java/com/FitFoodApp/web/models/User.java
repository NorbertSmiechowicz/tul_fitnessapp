package com.FitFoodApp.web.models;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Data
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String name;
    private String lastName;
    private String userName;
    private String email;
    private String password;

    private Integer height;
    private Integer weight;
    private Integer age;
    private String gender;
    private String lifestyle;
    private String avatarPhotoUrl;

    @OneToMany(mappedBy = "user", cascade = CascadeType.REMOVE)
    private List<Exercise> exercises = new ArrayList<>();
}
