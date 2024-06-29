package com.FitFoodApp.web.repository;

import com.FitFoodApp.web.models.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Integer> {
    Optional<User> findByUserName(String userName);
    @Query("SELECT u FROM User u WHERE u.userName LIKE CONCAT('%', :query, '%')")
    List<User> searchUsers(String query);
}
