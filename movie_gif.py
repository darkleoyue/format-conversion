import moviepy.editor as mpy
 
clip = mpy.VideoFileClip('ori.mp4')

clip.write_gif('cinemagraph.gif')