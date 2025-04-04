#pragma once

void bubble(std::vector<int> data)
{
    for(int i=0;i<data.size()-1;i++)
    {
        for(int j=0;j<data.size()-i-1;j++)
        {
            if(data[j] > data[j+1])
            {
                int temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
            }
        }
    }
}