clear all;
close all;

% simple  example of Wavetable synthesis


f1 = 440;
f2 = 500;
f3 = 620;


Fs = 22050;

%Create a single sine waves of  frequencie f1


y1 = synth(f1,1/f1,0.9,Fs,'sine');



doit = input('\nPlay/Plot Raw Sine y1 looped for 10 seconds? Y/[N]:\n\n', 's');

if doit == 'y',
figure(1)
plot(y1);
loopsound(y1,Fs,10*Fs/f1);
end

%Create a single Saw waves of  frequencie f2

y2 = synth(f2,1/f2,0.9,Fs,'saw');

doit = input('\nPlay/Plot Raw saw y2 looped for 10 seconds? Y/[N]:\n\n', 's');


if doit == 'y',
figure(2)
plot(y2);
loopsound(y2,Fs,10*Fs/f2);
end


ywave = [y1 , y2];


%doit = input('\nPlay/Plot Raw Concatenated Wave ywave for 10 seconds? Y/[N]:\n\n', 's');


%if doit == 'y',
%figure(3)
%plot(ywave);
%loopsound(ywave,Fs,10*Fs/(f1 + f2));
%end





% Create Cross fade half width of wave y1 for xfade window

xfadewidth = floor(Fs/(f1*2));
ramp1 = (0:xfadewidth)/xfadewidth;
ramp2 = 1 - ramp1;

doit = input('\nShow Crossfade Y/[N]:\n\n', 's');


if doit == 'y',
figure(4)
plot(ramp1);
hold on;
plot(ramp2,'r');
end;


%apply crossfade centered over the join of y1 and y2

pad = (Fs/f1) + (Fs/f2) - 2.5*xfadewidth;

xramp1 = [ones(1,uint16( 1.5*xfadewidth)) , ramp2, zeros(1,floor(pad))];
xramp2 = [zeros(1,uint8(1.5*xfadewidth)), ramp1, ones(1,floory(pad))];

% Create two period waveforms to fade between

ywave2 = [y1 , zeros(1,uint16(Fs/f2))];
ytemp = [zeros(1,uint16(Fs/f1)), y2];
 
ywave = ywave2;
% do xfade

% add two waves together over the period modulated by xfade ramps (recall
% .* to multiply matrices element by element NOT MATRIX mutliplication

ywave2 = xramp1(1:94).*ywave2 + xramp2(1:94).*ytemp;

doit = input('\nPlay/Plot Additive Sines together? Y/[N]:\n\n', 's');

if doit == 'y',
figure(5)

subplot(4,1,1);
plot(ywave);

hold off
%axis([0 1.5*N1 -1.1 1.1]);grid
set(gca,'fontsize',18);
ylabel('Amplitude'); 
title('Wave 1');
set(gca,'fontsize',18);

subplot(4,1,2);
plot(ytemp);
set(gca,'fontsize',18);
ylabel('Amplitude'); 
title('Wave 2'); 
set(gca,'fontsize',18);


subplot(4,1,3);
plot(xramp1);
hold on
plot(xramp2,'r')
hold off
%axis([0 1.5*N1 -1.1 1.1]);grid
set(gca,'fontsize',18);
ylabel('Amplitude'); 
title('Crossfade Masks');
set(gca,'fontsize',18);

subplot(4,1,4);
plot(ywave2);
set(gca,'fontsize',18);
ylabel('Amplitude'); 
title('WaveTable Synthesis');
set(gca,'fontsize',18);

loopsound(ywave2,Fs,20*Fs/(f1 + f2));
end


