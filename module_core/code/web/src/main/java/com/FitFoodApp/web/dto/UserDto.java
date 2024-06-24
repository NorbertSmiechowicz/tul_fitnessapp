package com.FitFoodApp.web.dto;

import jakarta.annotation.Nullable;
import jakarta.validation.constraints.NotEmpty;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class UserDto {
    private Integer id;
    @NotEmpty(message = "Name is required")
    private String name;
    @NotEmpty(message = "Last name is required")
    private String lastName;
    @NotEmpty(message = "Username is required")
    private String userName;
    @NotEmpty(message = "Email is required")
    private String email;
    @NotEmpty(message = "Password is required")
    private String password;

    @Nullable
    private Integer height;
    @Nullable
    private Integer weight;
    @Nullable
    private Integer age;
    @Nullable
    private String gender;
    @Nullable
    private String lifestyle;
}
