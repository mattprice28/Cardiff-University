% wood.m
%
% A Matlab script to compute a wood-like sound using frequency modulation.
%
% by Gary Scavone, McGill University, 2004.

% Signal parameters
fs = 22050;
T = 1/fs;
dur = 0.2;
t = 0:T:dur;
T60 = 0.1*dur;
env1 = exp(-t/T60);
env2 = 1.0 - t./(0.2*dur);
env2 = env2 .* (1.0 + sign(env2))/2.0;

% FM parameters
fc = 80;
fm = 55;
Imax = 25;
I = Imax.*env2;

y = env1.*sin(2*pi*fc*t + I.*sin(2*pi*fm*t));
plot(t, y);

sound(y, fs);

dospectrum = input('\nPlot spectrum? Y/[N]:\n\n', 's');

if dospectrum == 'Y',
  specgram(y, 512, fs, [], 256)
end
