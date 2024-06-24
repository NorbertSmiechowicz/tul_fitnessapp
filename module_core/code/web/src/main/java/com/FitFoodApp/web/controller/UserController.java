package com.FitFoodApp.web.controller;

import com.FitFoodApp.web.models.User;
import jakarta.validation.Valid;
import org.springframework.ui.Model;
import com.FitFoodApp.web.dto.UserDto;
import com.FitFoodApp.web.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller
public class UserController {
    private UserService userService;

    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/users")
    public String listUsers(Model model) {
        List<UserDto> users = userService.findAllUsers();
        model.addAttribute("users", users);
        return "users-list.html";
    }

    @GetMapping("/users/{userId}")
    public String clubDetail(@PathVariable("userId") int userId, Model model) {
        UserDto userDto = userService.findUserById(userId);
        model.addAttribute("user", userDto);
        return "users-detail";
    }

    @GetMapping("/users/new")
    public String createUserForm(Model model) {
        User user = new User();
        model.addAttribute("user", user);
        return "users-create";
    }

    @PostMapping("/users/new")
    public String saveUser(@Valid @ModelAttribute("user") UserDto userDto, BindingResult result, Model model) {
        if (result.hasErrors()) {
            model.addAttribute("user", userDto);
            return "users-create";
        }
        userService.saveUser(userDto);
        return "redirect:/users";
    }

    @GetMapping("/users/{userId}/edit")
    public String editUserForm(@PathVariable("userId") int userId, Model model) {
        UserDto user = userService.findUserById(userId);
        model.addAttribute("user", user);
        return "users-edit";
    }

    @PostMapping("/users/{userId}/edit")
    public String updateUser(@PathVariable("userId") int userId,
                             @Valid @ModelAttribute("user") UserDto user,
                             BindingResult result) {
        if(result.hasErrors()) {
            return "users-edit";
        }
        user.setId(userId);
        userService.updateUser(user);
        return "redirect:/users";
    }
}
