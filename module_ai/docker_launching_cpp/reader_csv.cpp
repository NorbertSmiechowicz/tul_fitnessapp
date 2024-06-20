#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <tuple>

template<typename T>
static void print(
    const std::vector<T> printable)
{
    for(const auto& element : printable)
    {
        std::cout<<element<<" ";
    }
    std::cout<<"\n";
}

template<typename T>
static void print(
    const std::vector<std::vector<T>> printable)
{
    for(const auto& row : printable){
        for(const auto& column : row)
        {
            std::cout<<column<<" ";
        }
        std::cout<<"\n";
    }
    std::cout<<"\n";
}
enum errorCode
{
    OK = 0,
    couldNotOpenFile = 1
};

std::pair<std::vector<float>, errorCode> readCSV(const std::string& filename, const char delimiter) 
{
    std::vector<float> data;
    std::ifstream file(filename);

    if (!file.is_open()) 
    {
        return std::make_pair(data, couldNotOpenFile);
    }

    std::string token;
    while (std::getline(file, token, delimiter)) 
    {
        data.push_back(std::stof(token));
    }

    file.close();
    return std::make_pair(data, OK);
}

int main(int argc, char* argv[]) 
{
    std::vector<float> csvData;
    errorCode error;
    std::tie(csvData, error) = readCSV(argv[1], ',');
    if(error)
    {
        std::cout<<"Could Not Open File: " << argv[1] << "\ndumping...\n";
        return error;
    }

    print(csvData);
    return 0;
}
