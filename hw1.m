clear 
clc          

%                 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20    1   22   23   24   25   26   27   28   29   30  
target_data_1 = [0.0, 0.0, 0.2, 0.6, 1.7, 2.6, 3.1, 4.6, 3.9, 3.5, 2.4, 2.9, 1.4, 1.7, 4.5, 5.7, 6.5, 7.8, 8.2, 8.4, 8.5, 6.1, 5.4, 4.9, 4.1, 4.0, 3.8, 5.2, 5.6, 5.5, 2.3];
target_data_2 = [1.1, 0.2, 0.4, 0.5, 0.1, 0.3, 0.7, 1.9, 3.7, 5.2, 7.9, 9.8, 6.2, 4.8, 3.0, 2.0, 1.3, 0.5, 0.3, 0.4, 0.6, 0.8, 1.8, 3.5, 5.1, 7.8, 9.4, 9.6, 9.7, 8.9, 1.1];

% data set 1 test
target_vel_1 = zeros(1,size(target_data_1,2));
for i = 1:size(target_data_1,2)
    if (i == 1)
        target_vel_1(i) = target_data_1(i)/0.01;
    else
        target_vel_1(i) = (target_data_1(i) - target_data_1(i-1))/0.01; %assume milliseconds
    end
end

target_vel_1