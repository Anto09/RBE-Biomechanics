function [ pv ] = pid( kp, kd, ki, cursor, target, integ )
    c_pos = cursor(1);
    c_vel = cursor(2);

    t_pos = target(1);
    t_vel = target(2);
    
    prop = c_pos - t_pos;
    
end

