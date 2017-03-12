%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%	pitch.m
%	course material for "Digital Sound Processing"
%	demonstrates pitch shifting of a wavetable with 
%	0th and 1st order interpolation
%	(C) R. Rabenstein
%	Nov. 1999
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

figure(1)


fa	= 44100;
M	= 100;
f	= fa/M;
Om	= 2*pi/M;
n	= 100;
N	= n*M;
k	= 0:N-1;

Wavetable 	= sin(Om*k);


PhaseIncr	= 2^(1/12);	% one semitone up
Phase		= 1;

y0 = int0(Wavetable, Phase, PhaseIncr);
y1 = int1(Wavetable, Phase, PhaseIncr);


disp('_______________________'), disp(' ')
disp('Pitch Shifting Example')
disp('_______________________'), disp(' ')
disp('Wavetable')
sound(Wavetable,fa)	
disp('one semitone up')
disp('zero order interpolation')
sound(y0,fa)
disp('first order interpolation')
sound(y1,fa)
disp('end')
disp('_______________________')





subplot(2,1,1)
stem(k,Wavetable);
axis([14.5 20.5 0.75 1.1]);grid
set(gca,'fontsize',18);
% ylabel('Amplitude'); 
title('Wavetable');
set(gca,'fontsize',18);

subplot(2,1,2)
stem(k,y0,'b'); hold on;
stem(k,y1,'r'); hold off;
axis([14.5 20.5 0.75 1.1]);grid
set(gca,'fontsize',18);
% ylabel('Amplitude'); 
title('Interpolation: 0 (blau), 1 (rot)');
set(gca,'fontsize',18);


 set(gcf,'Paperunits','centimeters')
 set(gcf,'PaperPosition',[0 0 10 14])
 print -depsc  'pitch.eps'
 




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
