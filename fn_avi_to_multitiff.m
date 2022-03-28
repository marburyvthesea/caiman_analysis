function [ output_args ] = fn_avi_to_multitiff(path_to_move_file)
%AVI from miniscope to mutliframe tiff
%   Input: full path to move file

[filepath,name,ext] = fileparts(path_to_move_file)

obj = VideoReader(path_to_move_file);
vid = read(obj);
frames = obj.NumberOfFrames;
imwrite(vid(:,:,:,1), strcat(filepath,name,'.tif'));
for x = 2 : frames
    imwrite(vid(:,:,:,x),strcat(filepath,name,'.tif'),'writemode', 'append');
end

end

