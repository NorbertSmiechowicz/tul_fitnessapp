package com.FitFoodApp.web.service.impl;

import com.FitFoodApp.web.dto.UserDto;
import com.FitFoodApp.web.models.User;
import com.FitFoodApp.web.repository.UserRepository;
import com.FitFoodApp.web.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

import static com.FitFoodApp.web.mapper.UserMapper.mapToUser;
import static com.FitFoodApp.web.mapper.UserMapper.mapToUserDto;

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
    public User saveUser(UserDto userDto) {
        User user = mapToUser(userDto);
        return userRepository.save(user);
    }

    @Override
    public UserDto findUserById(int userId) {
        User user = userRepository.findById(userId).get();
        return mapToUserDto(user) ;
    }

    @Override
    public void updateUser(UserDto userDto) {
        User user = mapToUser(userDto);
        userRepository.save(user);
    }

    @Override
    public void delete(int userId) {
        userRepository.deleteById(userId);
    }

    @Override
    public List<UserDto> searchUsers(String query) {
        List<User> users = userRepository.searchUsers(query);
        return users.stream().map(user -> mapToUserDto(user)).collect((Collectors.toList()));
    }
}
