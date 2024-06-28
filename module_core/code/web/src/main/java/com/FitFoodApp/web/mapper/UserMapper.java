package com.FitFoodApp.web.mapper;

import com.FitFoodApp.web.dto.UserDto;
import com.FitFoodApp.web.models.User;

import java.util.stream.Collectors;

import static com.FitFoodApp.web.mapper.ExerciseMapper.mapToExerciseDto;

public class UserMapper {
    public static User mapToUser(UserDto userDto) {
        User user = User.builder()
                .id(userDto.getId())
                .name(userDto.getName())
                .lastName(userDto.getLastName())
                .userName(userDto.getUserName())
                .email(userDto.getEmail())
                .password(userDto.getPassword())
                .height(userDto.getHeight())
                .weight(userDto.getWeight())
                .age(userDto.getAge())
                .gender(userDto.getGender())
                .lifestyle(userDto.getLifestyle())
                .avatarPhotoUrl(userDto.getAvatarPhotoUrl())
                .build();
        return user;
    }

    public static UserDto mapToUserDto(User user) {
        UserDto userDto = UserDto.builder()
                .id(user.getId())
                .name(user.getName())
                .lastName(user.getLastName())
                .userName(user.getUserName())
                .email(user.getEmail())
                .password(user.getPassword())
                .height(user.getHeight())
                .weight(user.getWeight())
                .age(user.getAge())
                .gender(user.getGender())
                .lifestyle(user.getLifestyle())
                .avatarPhotoUrl(user.getAvatarPhotoUrl())
                .exercises(user.getExercises().stream().map((exercise) -> mapToExerciseDto(exercise)).collect(Collectors.toList()))
                .build();
        return userDto;
    }
}
