package com.FitFoodApp.web.dto;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class UserDto {
    private int id;
    private String name;
    private String lastName;
    private String userName;
    private String email;
    private String password;
}
