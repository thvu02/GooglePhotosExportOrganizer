import json
import time
import os

def getPhotoTakenTime(json_file_path):
    f = open(json_file_path)
    # return json object as dict
    data = json.load(f)
    timestamp = int(data['photoTakenTime']['timestamp'])
    formatted_time = time.strftime('%Y%m%d_%H%M%S', time.gmtime(timestamp))
    return formatted_time

def getTitle(json_file_path):
    f = open(json_file_path)
    # return json object as dict
    data = json.load(f)
    title = os.path.splitext(data['title'])[0]
    return title[:10]

def rename(root, file_path, extension, json_file_path, count):
    # rename json file or add to no json list
    if os.path.exists(json_file_path):
        # create new file names
        new_name = getPhotoTakenTime(json_file_path)
        new_json_name = f"{new_name}.json"
        new_file_name = f"{new_name}{extension}"
        # create backup file names in case of duplicate photoTakenTime btwn photos/movies
        backup_detail = getTitle(json_file_path)
        backup_json_name = f"{new_name}_{backup_detail}_{count}.json"
        backup_file_name = f"{new_name}_{backup_detail}_{count}{extension}"
        # case for where heic files have an associated mp4 file
        multi_condition = False
        if (extension.endswith(('.mov', '.png', '.heic', '.jpg', '.jpeg', '.avi', '.3gp', '.MOV', '.PNG', '.HEIC', '.JPG', '.JPEG', '.AVI', '.3GP'))) and os.path.exists(f"{os.path.splitext(file_path)[0]}.MP4"):
            multi_condition = True
            mp4_file_path = f"{os.path.splitext(file_path)[0]}.MP4"
            new_mp4_name = f"{new_name}.MP4"
            backup_mp4_name = f"{new_name}_{backup_detail}_{count}.MP4"
        elif (extension.endswith(('.mov', '.png', '.heic', '.jpg', '.jpeg', '.avi', '.3gp', '.MOV', '.PNG', '.HEIC', '.JPG', '.JPEG', '.AVI', '.3GP'))) and os.path.exists(f"{os.path.splitext(file_path)[0]}.mp4"):
            multi_condition = True
            mp4_file_path = f"{os.path.splitext(file_path)[0]}.mp4"
            new_mp4_name = f"{new_name}.mp4"
            backup_mp4_name = f"{new_name}_{backup_detail}_{count}.mp4"
        # rename files
        try:
            os.rename(json_file_path, os.path.join(root, new_json_name))
            if multi_condition == True:
                os.rename(mp4_file_path, os.path.join(root, new_mp4_name))
                count += 1
            os.rename(file_path, os.path.join(root, new_file_name))
        except:
            os.rename(json_file_path, os.path.join(root, backup_json_name))
            if multi_condition == True:
                os.rename(mp4_file_path, os.path.join(root, backup_mp4_name))
                count += 1
            os.rename(file_path, os.path.join(root, backup_file_name))
        count += 1
        return True, count
    return False, count
    
def rename_files(directory):
    no_json_files = []
    count = 0
    no_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mov', '.png', '.heic', '.jpg', '.jpeg', '.mp4', '.avi', '.3gp', '.MOV', '.PNG', '.HEIC', '.JPG', '.JPEG', '.MP4', '.AVI', '.3GP')):
                # get file path and extension
                file_path = os.path.join(root,file)
                extension = os.path.splitext(file)[1]

                # check for json file
                # for json files w (#) in name
                if file_path.find('(') != -1:
                    no_paren = os.path.splitext(file)[0][:-3]
                    paren = os.path.splitext(file)[0][-3:]
                    json_file_name = f"{no_paren}{extension}{paren}.json"
                    json_file_path = os.path.join(root, json_file_name)
                    result = rename(root, file_path, extension, json_file_path, count)
                    if result[0] == True:
                        count = result[1]
                        continue
            
                # for json file w/o photo/movie extension in file path
                json_file_name = f"{os.path.splitext(file)[0]}.json"
                json_file_path = os.path.join(root, json_file_name)
                result = rename(root, file_path, extension, json_file_path, count)
                if result[0] == True:
                    count = result[1]
                    continue

                # for json file with photo/movie extension in file path
                json_file_path = f"{file_path}.json"
                result = rename(root, file_path, extension, json_file_path, count)
                if result[0] == True:
                    count = result[1]
                    continue

                # for json file w/o photo/movie extension in file path and extra .j as in .j.json
                json_file_name = f"{os.path.splitext(file)[0]}.j.json"
                json_file_path = os.path.join(root, json_file_name)
                result = rename(root, file_path, extension, json_file_path, count)
                if result[0] == True:
                    count = result[1]
                    continue

                # for json file with photo/movie extension in file path and extra .j as in .j.json
                json_file_path = f"{file_path}.j.json"
                result = rename(root, file_path, extension, json_file_path, count)
                if result[0] == True:
                    count = result[1]
                    continue

                # for json file w/o photo/movie extension in file path and extra . as in ..json
                json_file_name = f"{os.path.splitext(file)[0]}..json"
                json_file_path = os.path.join(root, json_file_name)
                result = rename(root, file_path, extension, json_file_path, count)
                if result[0] == True:
                    count = result[1]
                    continue

                # for json file with photo/movie extension in file path and extra . as in ..json
                json_file_path = f"{file_path}..json"
                result = rename(root, file_path, extension, json_file_path, count)
                if result[0] == True:
                    count = result[1]
                    continue

                # for json file w/o photo/movie extension in file path where json file truncates file/movie name by one character
                json_file_name = f"{os.path.splitext(file)[0][:-1]}.json"
                json_file_path = os.path.join(root, json_file_name)
                result = rename(root, file_path, extension, json_file_path, count)
                if result[0] == True:
                    count = result[1]
                    continue

                # for json file with photo/movie extension in file path where json file truncates file/movie name by one character
                json_file_path = f"{file_path[:-1]}.json"
                result = rename(root, file_path, extension, json_file_path, count)
                if result[0] == True:
                    count = result[1]
                    continue

                # if there is no json file found for either scenario
                if os.path.exists(file_path):
                    no_json_files.append(file_path)
                    no_count += 1

    with open(f"{directory}_nojson.txt", 'w') as f:
        for item in no_json_files:
            f.write(f"{item}\n")
    
    print("# files renamed:", count)
    print("# files skipped:", no_count)

if __name__ == "__main__":
    # enter file path of directory
    directory = 'path_to_directory'
    rename_files(directory)
