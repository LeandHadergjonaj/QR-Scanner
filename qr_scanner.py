#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:39:49 2024

@author: leand
"""

import cv2
import webbrowser

def decode_qr(frame, last_url):
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(frame)
    if bbox is not None and data:
        print("Data:", data)
        if data != last_url:
            webbrowser.get('safari').open(data)
            last_url = data  
        if len(bbox) > 0:
            bbox = bbox.astype(int) 
            for i in range(len(bbox)):
                start_point = tuple(bbox[i][0])
                end_point = tuple(bbox[(i+1) % len(bbox)][0])
                cv2.line(frame, start_point, end_point, color=(0, 255, 0), thickness=2)
    return last_url

def main():
    cap = cv2.VideoCapture(0)
    last_url = ""  

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        last_url = decode_qr(frame, last_url)

        cv2.imshow('QR Code Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

