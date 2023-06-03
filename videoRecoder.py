import sys
import time
import keyboard
from screen_recorder_sdk import screen_recorder

def read_config():
    config = {}
    
    try:
        with open('config.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(':')
                config[key.strip()] = value.strip()
    except FileNotFoundError:
        print('Config file not found. Using default values.')
    
    return config

def main():
    # Enable dev logger
    screen_recorder.enable_dev_log()
    
    params = screen_recorder.RecorderParams()
    
    # Initialize the screen recorder
    screen_recorder.init_resources(params)
    
    # Take a screenshot and save it 
    screen_recorder.get_screenshot(5).save('sample.png')
    print('Screenshot taken')
    
    # Read configuration values
    config = read_config()
    
    # Adjust the desired framerate and bitrate values
    framerate = int(config.get('FPS', '60'))
    bitrate = int(config.get('bitrate', '25000000')) 
    save_name = config.get('file save name', 'sample.mp4')
    
    # Start video recording
    print('Video Started')
    screen_recorder.start_video_recording(save_name, framerate, bitrate, True)
    
    # Monitor the F7 key for stopping the recording
    while True:
        if keyboard.is_pressed('F7'):
            # Stop the recording
            screen_recorder.stop_video_recording()
            print('Video Stopped')
            break
    
    # Clean up resources
    screen_recorder.free_resources()

if __name__ == "__main__":
    main()
