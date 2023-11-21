import streamlit as st
from pytube import YouTube


def main():
	path = st.text_input('Enter URL of any youtube video')
	option = st.selectbox(
        'Select type of download',
        ('highest_resolution', 'lowest_resolution', 'audio')
	)
	SAVE_PATH = st.text_input("Save path", value="streamlit", key="save_path")

	if st.button("download"): 
		video_object =  YouTube(path)
		st.write("Title of Video: " + str(video_object.title))
		
		if option=='audio':
			video_object.streams.get_audio_only().download(output_path=SAVE_PATH)	
		elif option=='highest_resolution':
			video_object.streams.get_highest_resolution().download(output_path=SAVE_PATH)
		elif option=='lowest_resolution':
			video_object.streams.get_lowest_resolution().download(output_path=SAVE_PATH)
	
	if st.button("view"): 
		st.video(path) 

if __name__ == '__main__':
	main()