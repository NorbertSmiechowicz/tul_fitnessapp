package com.FitFoodApp.web.service.impl;

import com.FitFoodApp.web.dto.UserDto;
import com.FitFoodApp.web.models.User;
import com.FitFoodApp.web.repository.UserRepository;
import com.FitFoodApp.web.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class UserServiceImpl implements UserService {

    private UserRepository userRepository;

    @Autowired
    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public List<UserDto> findAllUsers() {
        List<User> users = userRepository.findAll();
        return users.stream().map((user) -> mapToUserDto(user)).collect((Collectors.toList()));
    }

    @Override
    public User saveUser(User user) {
        return userRepository.save(user);
    }

    @Override
    public UserDto findUserById(long userId) {
        User user = userRepository.findById(userId).get();
        return mapToUserDto(user) ;
    }

    @Override
    public void updateUser(UserDto userDto) {
        User user = mapToUser(userDto);
        userRepository.save(user);
    }

    private User mapToUser(UserDto user) {
        User userDto = User.builder()
                .id(user.getId())
                .name(user.getName())
                .lastName(user.getLastName())
                .userName(user.getUserName())
                .email(user.getEmail())
                .password(user.getPassword())
                .build();
        return userDto;
    }

    private UserDto mapToUserDto(User user) {
        UserDto userDto = UserDto.builder()
                .id(user.getId())
                .name(user.getName())
                .lastName(user.getLastName())
                .userName(user.getUserName())
                .email(user.getEmail())
                .password(user.getPassword())
                .build();
        return userDto;
    }
}