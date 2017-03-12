clear all;
close all;

% simple  example of Additive synthesis


Fs = 22050;

%Create 3 sine waves of different frequencies f1,f2,f3

f1 = 440;
f2 = 500;
f3 = 620;


y1 = synth(f1,2,0.9,Fs,'sine');



doit = input('\nPlay/Plot Raw Sine y1? Y/[N]:\n\n', 's');

if doit == 'y',
figure(1)
plot(y1(1:440));
sound(y1,Fs);
end



y2 = synth(f2,2,0.9,Fs,'sine');

doit = input('\nPlay/Plot Raw Sine y2? Y/[N]:\n\n', 's');


if doit == 'y',
figure(2)
plot(y2(1:440));
sound(y2,Fs);
end


y3 = synth(f3,2,0.9,Fs,'sine');


doit = input('\nPlay/Plot Raw Sine y3? Y/[N]:\n\n', 's');


if doit == 'y',
figure(3)
plot(y3(1:440));
sound(y3,Fs);
end


%  Add Waves together

yadd = (y1 + y2 + y3)/3;


doit = input('\nPlay/Plot Additive Sines together? Y/[N]:\n\n', 's');

if doit == 'y',
figure(4)
plot(yadd(1:440));
sound(yadd,Fs);
end


