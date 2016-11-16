function [ new_pos ] = simulate(c_vel, c_acc, c_pos)
    acc_noise = rand()*0.2 + 0.8;
    c_acc = acc_noise * c_acc;
    
    if (abs(c_acc) > 20.0)
        c_acc = sign(c_acc) * 20.0;
    end
    
end

