#include <fstream>
#include "ArrayConfigs.hpp"

ArrayConfigs& parse(std::string& fileName)
{
    std::ifstream file(fileName);

    // Variables to generate config
    int size;
    std::vector<int> data;
    std::string type;

    std::string line;
    
}