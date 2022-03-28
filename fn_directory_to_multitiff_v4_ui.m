function [ output_args ] = fn_directory_to_multitiff_v4_ui()
%AVI from miniscope to mutliframe tiff
%   Input: full path to move file

dirpath = uigetdir ; 
input_movie_start = '0'; 
input_movie_end = '1';
parallel = false; 

addpath(genpath(dirpath)); 

movie_start = str2num(input_movie_start);
movie_end = str2num(input_movie_end);

disp('movie start');
disp(movie_start);
disp('movie end'); 
disp(movie_end); 




%loop through videos  
if parallel == true
   
    disp('processing in parallel');

    parfor x = movie_start:movie_end
	disp(x);	
        fn_avi_to_multitiff(strcat(dirpath, '\', num2str(x), '.avi'));
    end
    
else

    disp('parellel off');

    for x = movie_start:movie_end
	disp(x);
        fn_avi_to_multitiff(strcat(dirpath, '\', num2str(x), '.avi'));

    end    
end

