function y = int1(Wavetab, Phase, PhaseIncr);
%int1 First Order Interpolation of a Wavetable	

y = zeros(size(Wavetab));
N = length(Wavetab);

for k = 1:N;
	frac = Phase-floor(Phase);
	y(k) = Wavetab(floor(Phase))*(1-frac) +...
	       Wavetab(floor(Phase)+1)*frac;	% Address Wavetable
	Phase = Phase + PhaseIncr;		% Increment Phase
	if Phase>N-1, break, end; 		% Break Loop
end;
