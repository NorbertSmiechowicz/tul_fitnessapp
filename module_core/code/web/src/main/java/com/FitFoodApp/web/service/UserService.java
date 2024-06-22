package com.FitFoodApp.web.service;

import com.FitFoodApp.web.dto.UserDto;

import java.util.List;

public interface UserService {
    List<UserDto> findAllUsers();
}
