% bell.m
%
% A Matlab script to compute a bell-like sound using frequency modulation.
%
% by Gary Scavone, McGill University, 2004.

% Signal parameters
fs = 22050;
T = 1/fs;
dur = 7.0;
t = 0:T:dur;
T60 = 1.0;
env = 0.95*exp(-t/T60);

% FM parameters
fc = 200;
fm = 280;
Imax = 10;
I = Imax.*env;

y = env.*sin(2*pi*fc*t + I.*sin(2*pi*fm*t));
plot(t, y);

sound(y, fs);

dospectrum = input('\nPlot spectrum? Y/[N]:\n\n', 's');

if dospectrum == 'Y',
  specgram(y, 512, fs, [], 256)
end
