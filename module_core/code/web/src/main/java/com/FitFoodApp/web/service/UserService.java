package com.FitFoodApp.web.service;

import com.FitFoodApp.web.dto.UserDto;
import com.FitFoodApp.web.models.User;

import java.util.List;

public interface UserService {
    List<UserDto> findAllUsers();
    User saveUser(UserDto userDto);

    UserDto findUserById(int userId);

    void updateUser(UserDto user);

    void delete(int userId);
}
