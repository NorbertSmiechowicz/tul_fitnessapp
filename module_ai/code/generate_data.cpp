#include "data_structures.h"
#include <iostream>
#include <vector>
#include <array>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <string>
#include <nlohmann/json.hpp>
#include <fstream>

int main()
{
    /*
    {
        std::vector<data::exercise> test;
        for (int i = 0; i < 10; i++){
            for(int j = 0; j < 10; j++)
            {
                test.push_back(data::exercise{std::to_string(j),data::arms,0,0});
            }
        }
        for(auto& x : test){
            std::cout<<x.name;
        }
        std::cout<<"\n\n";

        auto test1 = data::test_update_client_performance(test);
        for(auto& x : test1){
            std::cout<<x.name;
        }
    }
    */
    /*
    {
        std::unordered_map<std::string, int> test;

        for(auto& x : test){
            std::cout<<x.second;
        }

        test["a"] = 1;
        test["b"] = 2;
        test["a"] = 3;

        for(auto& x : test){
            std::cout<<x.first<<x.second<<" ";
        }
    }
    */
    {
        std::unordered_map<std::string, data::exercise> test_map;
        auto test_exercises = [](){
            std::vector<data::exercise> temp;
            for (int i = 0; i < 3; i++){
                for(int j = 0; j < 10; j++){
                    temp.push_back(data::exercise{std::to_string(j),data::arms,0,0});
                }
            } return temp;
        }();
        
        for(auto& x : test_exercises){
            std::cout<<x.name<<" ";
        }

        std::cout<<"\n---\n";

        std::cout<<"initialized hashmap:\t";
        
        std::cout<<"\n---\n";


        data::update_client_performance(test_map, test_exercises);

        std::cout<<"edited hashmap:\t";
        for(auto& x : test_map){
            std::cout<<x.first<<" ";
        }

        std::cout<<"\n---\n";
    }

    return 0;
}