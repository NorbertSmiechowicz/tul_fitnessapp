#include <iostream>
#include <vector>
#include <array>
#include <unordered_map>
#include <set>
#include <algorithm>

namespace data
{
    enum exercise_target
    {
        arms,
        legs,
    };

    struct biometrics
    {
        int age;
        int sex;
        float height;
    };

    struct day_critical
    {
        float protein;
        float fats;
        float carbs;
        float weight_diff;
        float strength_diff;
    };

    struct review 
    {
        float cum_strength_diff;
        float cum_weight_diff;
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
        exercise_target exercise_target;
        int reps;
        // optional 
        // TO GENERALIZE LATER
        int weight;
        //std::vector<int> time_of_set;
    };

    exercise update_client_performance_exercise(
        std::vector<exercise> exercise_allsets)
    {        
        exercise temp_exercise{exercise_allsets[0]};
        for(auto& set : exercise_allsets){
            temp_exercise.reps += set.reps;
        }
        return temp_exercise;
    };

    class exercise_name_filter
    {
    private:
        std::string name;
    public:
        exercise_name_filter(std::string name) : name{name} {};
        bool operator() (exercise exercise) const 
        {
            return exercise.name == name;
        }
    };

    std::set<std::string> update_client_performance(
        std::unordered_map<std::string, exercise>& old_client_performance,
        const std::vector<exercise> fresh_exercise_list
    )
    // updates existing and adds non existing entries in the client performance hashmap
    // returns names of changed entries
    {
        std::set<std::string> fresh_exercise_names{};
        for(auto& exercise_unit: fresh_exercise_list)
        {
            fresh_exercise_names.insert(exercise_unit.name);
        }

        for(auto& exercise_name: fresh_exercise_names)
        {   
            std::vector<exercise> exercise_sets{};
            std::copy_if(fresh_exercise_list.begin(), fresh_exercise_list.end(), std::back_inserter(exercise_sets), exercise_name_filter(exercise_name));
            old_client_performance[exercise_name] = update_client_performance_exercise(exercise_sets);
        }

        return fresh_exercise_names;
    }
}