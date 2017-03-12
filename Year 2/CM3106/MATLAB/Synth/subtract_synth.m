clear all;
close all;

% simple low pas filter example of subtractive synthesis

Fs = 22050;

y = synth(440,2,0.9,22050,'saw');


% play sawtooth e.g. waveform


doit = input('\nPlay Raw Sawtooth? Y/[N]:\n\n', 's');

if doit == 'y',
  figure(1)
plot(y(1:440));
sound(y,Fs);
end

%make lowpass filter and filter y


[B, A] = butter(1,0.04, 'low');


yf = filter(B,A,y);


[B, A] = butter(4,0.04, 'low');


yf2 = filter(B,A,y);

% play filtererd sawtooths


doit = input('\nPlay Low Pass Filtered (Low order) ? Y/[N]:\n\n', 's');

if doit == 'y',
figure(2)
plot(yf(1:440));
sound(yf,Fs);
end

doit = input('\nPlay Low Pass Filtered (Higher order)? Y/[N]:\n\n', 's');

if doit == 'y',
    figure(3)
plot(yf2(1:440));
sound(yf2,Fs);
end

%plot figures

doit = input('\Plot All Figures? Y/[N]:\n\n', 's');

if doit == 'y',
figure(4)
plot(y(1:440));
hold on
plot(yf(1:440),'r+');
plot(yf2(1:440),'g-');
end

