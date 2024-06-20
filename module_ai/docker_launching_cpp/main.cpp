#include <iostream>
#include <nlohmann/json.hpp>
#include <fstream>

int main(int argc, char* argv[]) {

    std::ifstream input_file(argv[1]);

    if (!input_file.is_open()) {
        std::cerr << "Failed to open file: " << argv[1];
        return -1;
    }
    
    nlohmann::json json_data;
    input_file >> json_data;
    
    input_file.close();

    std::cout << "Parsed JSON data: " << json_data.dump(4) << "\n";
}