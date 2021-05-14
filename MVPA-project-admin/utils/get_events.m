% log_fn = ''; 
% load('log_fn')


offset=0;

ev_type=[];
ev_tstamps=[];

im_idx=1;

% set events
for b=1:length(protocolConds)
    
    if protocolConds(b)==1
        for i=1:5
            ev_type=[ev_type 0];
            ev_tstamps=[ev_tstamps offset];
            offset=offset+3;
        end
    else
        for i=1:10
            ev_type=[ev_type imageSequence(i)];
            ev_tstamps=[ev_tstamps offset];
            offset=offset+configs.TR;
            im_idx=im_idx+1;
        end
    end
    
end