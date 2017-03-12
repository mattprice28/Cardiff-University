%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%	looping.m
%	course material for "Digital Sound Processing"
%	demonstrates the effect of looping on wavetables
%	which consitute not an exact period of the signal
%	(C) R. Rabenstein
%	Nov. 1999
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

figure(1)

fa	= 44100;
M	= 100;
f	= fa/M;
Om	= 2*pi/M;

N1	= M;
k1	= 0:N1-1;
y1 	= sin(Om*k1);
yl1	= []; 

for l=1:60
    yl1 = [yl1,y1]; 
end;

Yl1	= abs(fftshift(fft(yl1)));
Omega1	= (-length(Yl1)/2:length(Yl1)/2-1)/length(Yl1);

N2	= 1.5*M;
k2	= 0:N2-1;
y2 = sin(Om*k2);
yl2	= []; for l=1:40, yl2 = [yl2,y2]; end;
Yl2	= abs(fftshift(fft(yl2)));
Omega2	= (-length(Yl2)/2:length(Yl2)/2-1)/length(Yl2);



subplot(2,3,1)
plot(k1,y1);
axis([0 1.5*N1 -1.1 1.1]);grid
set(gca,'fontsize',18);
ylabel('Amplitude'); 
title('Abtastwerte');
set(gca,'fontsize',18);

subplot(2,3,2)
plot(yl1);
axis([0 6*N1 -1.1 1.1]);grid
title('Abtastwerte');
set(gca,'fontsize',18);

subplot(2,3,3)
plot(Omega1,Yl1/30/N1);
axis([-0.002 0.025 -0.1 1.1]);grid
title('Frequency in 2\pi');
set(gca,'fontsize',18);

subplot(2,3,4)
plot(k2,y2);
axis([0 N2 -1.1 1.1]);grid
set(gca,'fontsize',18);
ylabel('Amplitude'); 
set(gca,'fontsize',18);

subplot(2,3,5)
plot(yl2);
axis([0 4*N2 -1.1 1.1]);grid
set(gca,'fontsize',18);
%xl = xlabel('Abtastwerte');
set(gca,'fontsize',18);

subplot(2,3,6)
plot(Omega2,Yl2/20/N2);
axis([-0.002 0.025 -0.1 1.1]);grid
set(gca,'fontsize',18);
%xl = xlabel('Frequency in \pi');

sound(yl1,fa);
sound(yl2,fa);

 set(gcf,'Paperunits','centimeters')
 set(gcf,'PaperPosition',[0 -1 24 10])
 print -depsc  'looping.eps'


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
