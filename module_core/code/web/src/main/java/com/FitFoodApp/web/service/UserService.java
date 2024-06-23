package com.FitFoodApp.web.service;

import com.FitFoodApp.web.dto.UserDto;
import com.FitFoodApp.web.models.User;

import java.util.List;

public interface UserService {
    List<UserDto> findAllUsers();
    User saveUser(User user);

    UserDto findUserById(long userId);

    void updateUser(UserDto user);
}
