from moviepy.editor import VideoFileClip

def cut_and_convert_mov_to_mp4(input_path, output_path, start_time, end_time):
    # 读取MOV视频
    clip = VideoFileClip(input_path)
    # 截取指定时间段的视频
    subclip = clip.subclip(start_time, end_time)
    # 将截取的视频写入为MP4格式
    subclip.write_videofile(output_path, codec='libx264')

# 示例用法
input_mov = "path_to_your_video.mov"  # 输入MOV文件的路径
output_mp4 = "path_to_your_output_video.mp4"  # 输出MP4文件的路径
start_time = 10  # 开始时间（以秒为单位）
end_time = 20  # 结束时间（以秒为单位）

cut_and_convert_mov_to_mp4(input_mov, output_mp4, start_time, end_time)
