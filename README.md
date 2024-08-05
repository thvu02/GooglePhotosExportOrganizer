# GooglePhotosExportOrganizer
A series of Python functions that allow users to rename photos in a MonthYearDate_HourMinSec format for easy browsing of photos/movies in chronological order outside of Google Photos

## About
Memory constraints on Google accounts prevent Google Photos from being stored with all photos/movies. Takeouts must be done occasionally to store photos/movies elsewhere, however, naming conventions prevent photos/movies from being easily searchable. This repository contains tools that enable users to simply re-organize their Google Photos Takeout contents by renaming photos/movies to MonthYearDate_HourMinSec formats for simple browsing.

## How it Works
- Clone the repository, enter the path to the parent directory which contains all your photos in the main function of rename.py, and run the script.
- The script will rename your photo/movies and will NOT create a new directory (if you wish to stay safe, create a copy of your directory before running the script).
- Two lines of output will be printed indicating how many files where/where not renamed.
- The script produces a .txt file which lists the files that were not renamed. Use this to check for and manually fix errors.

## Cases Covered
- any of the following file types: '.mov', '.png', '.heic', '.jpg', '.jpeg', '.mp4', '.avi', '.3gp', '.MOV', '.PNG', '.HEIC', '.JPG', '.JPEG', '.MP4', '.AVI', '.3GP'
- files with typical naming convention
- files with (#) in name (e.g. IMG_1234(1).jpg)
- files with file extension in json file path
- files w/o file extension in json file path
- files with extra . in file path (e.g. ..json)
- files where name of json file is truncated by one char 

## Problems
- Some photos/movies have titles that exceed file naming limits. This causes file names to get truncated and produces different file names for the same photo/movie and their associated files (e.g. abc.heic, abc.json, abcd.mp4)

## TODO
- functionality to aggregate all photos/movies in subdirectories (e.g. Photos from 2023, Photos from 2024) into one main directory
