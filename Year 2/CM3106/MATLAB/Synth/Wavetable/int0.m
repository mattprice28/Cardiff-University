function y = int0(Wavetab, Phase, PhaseIncr);
%int0 Zero Order Interpolation of a Wavetable	

y = zeros(size(Wavetab));
N = length(Wavetab);

for k = 1:N;
	y(k) = Wavetab(floor(Phase));	% Address Wavetable
	Phase = Phase + PhaseIncr;	% Increment Phase
	if Phase>N, break, end; 	% Break Loop
end;
