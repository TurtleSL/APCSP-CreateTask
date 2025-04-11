#pragma once

#include <vector>

void insertion(std::vector<int> data)
{
    for(int i=1;i<data.size();i++)
    {   
        for(int j=0;j<i;j++)
        {
            if((i-1-j) >= 0) //Out of bounds prevention
                if(data[i] > data[i-1-j])
                {
                    int temp = data[i];
                    data[i] = data[i-1-j];
                    data[i-1-j] = temp;
                }
        }
    }
}