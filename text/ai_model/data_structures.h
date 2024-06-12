#include <iostream>
#include <vector>
#include <array>
#include <unordered_map>

namespace data
{
    struct biometrics
    {
        int age;
        int sex;
        float hight;
        float weigth;
        float base_kcal;
    };

    struct day_critical
    {
        float protein;
        float carbs;
        float fats;
        float weight;
        float kcal_burned;
        float strength_difference;
    };

    struct review 
    {
        float gains;
        float wieghtloss;
    };

    struct model_input
    {
        biometrics biometrics;
        review review;
        std::array<day_critical, 42> calendar;
    };

    struct exercise
    {
        // mandatory
        std::string name;
        std::vector<int> reps_of_set;
        // optional
        std::vector<int> weight_of_set;
        std::vector<int> time_of_set;
    };

    day_critical extract_exercises(
        std::vector<exercise> exercise_list,
        std::unordered_map<std::string, std::string> 
    )
    {
        return day_critical{};
    }
}