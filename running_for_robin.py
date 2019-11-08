#import run_main
import os
import time


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # disables Tensorflow Warnings





results_path = "/run06/result06/"
res_path = results_path

style_path = "/run06/styles06/"
pattern_path = "/run06/image_input06/"

result_name= "result "

dir_path = os.path.dirname(os.path.realpath(__file__))

results_path = dir_path + results_path
style_path = dir_path + style_path
pattern_path = dir_path + pattern_path

#print(results_path)



#these initialize the lists of styles and patterns in respective folders
styles = []
#print(os.listdir(style_path))

for filename in os.listdir(style_path):
    if filename.endswith("jpg") or filename.endswith("png"):
        # Your code comes here such as
        print(filename)
        styles.append(filename)

#print(styles)

patterns = []

#print(os.listdir(pattern_path))

for filename in os.listdir(pattern_path):
    if filename.endswith("jpg") or filename.endswith("png"):
        # Your code comes here such as
        print(filename)
        patterns.append(filename)

#print(patterns)



#this gives the system the run commands
def run_helper(content, style, output_path, loss):
    run_string = "python neural_style.py --content_img "+ content + \
                 " --style_imgs " + style + \
                 " --img_output_dir " + output_path + \
                 " --style_weight " + loss +\
                 " --max_iterations 700 " + \
                 " --img_name " + result_name + loss
                 #" --verbose "  # + \
                 #" --device /cpu:0 "
    print(run_string)
    return run_string


#loss ratios to be tested

loss_ratios = ["1e8", "1e5"]
#loss_ratios = ["1e3"]

i = 0
for pattern in patterns:
    for tyyli in styles:
        for loss in loss_ratios:
            i+=1

print("_" * 40)
print("Style transfers to perform: ", i)

j = 0
dur_list = []
start_time = time.time()

for loss in loss_ratios:
    for pattern in patterns:
        for tyyli in styles:
            tyyli_path = style_path + tyyli
            content_path = pattern_path + pattern
            output_path = results_path + pattern.split(".")[0] + "_" + tyyli + "_" + loss +"_t1"
            print("_" * 10)
            print(content_path, tyyli_path, output_path, loss)
            j += 1
            inst_start_time = time.time()
            try:
                print("_"*40)
                print("   ")
                print("running style transfer  ", j ," of ", i)
                print("_" * 40)
                os.system(run_helper(content_path, tyyli_path, output_path, loss))
            except:
                print("some error happened")

            elapsed = time.time() - start_time
            inst_dur = time.time() - inst_start_time
            dur_list.append(inst_dur)
            print("_" * 40)
            print("   ")
            print("style transfer done in: ", inst_dur )
            print("elapsed time in s:", elapsed)
            average_dur = sum(dur_list) / len(dur_list)
            print("average solve time: ", average_dur)
            remaining_solves = i - j
            remaining_time = remaining_solves * average_dur
            print("remaining solves: ", remaining_solves)
            print("remaining time:", remaining_time ,"in seconds", remaining_time/60 ,"in minutes", remaining_time/60/60 ,"in hours")




            print("_" * 40)

print("_"*40)
print("   ")

git_c_mess = "git commit -m " + "\" ran style transfer " + str(i) + " times saved in" + res_path +" \""
print("commit message: ",git_c_mess)

os.system("git add . ")
os.system(git_c_mess)
os.system("git push")
