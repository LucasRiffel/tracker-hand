import pafy
import cv2

url = "https://www.youtube.com/watch?v=9DRVfTFtPiM"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

capture = cv2.VideoCapture(best.url)