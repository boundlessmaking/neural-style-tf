#import run_main
import os
import time
import datetime
import random


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # disables Tensorflow Warnings





results_path = "/run07-test/result07/"
res_path = results_path

style_path = "/run07-test/styles07/"
pattern_path = "/run07-test/image_input07/"

result_name= "result_"

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
def run_helper(content, style, output_path, loss,iterations,style_name,content_name):
    run_string = "python neural_style.py --content_img "+ content + \
                 " --style_imgs " + style + \
                 " --img_output_dir " + output_path + \
                 " --style_weight " + loss +\
                 " --max_iterations "+ iterations + \
                 " --img_name " + result_name + content_name + "-" + style_name + "_lo-" +loss+ "_it-" + iterations
                 #" --verbose "  # + \
                 #" --device /cpu:0 "
    print(run_string)
    return run_string


#loss ratios to be tested

loss_ratios = ["1e6", "2e1","3e6","1e9","1e2"]
#loss_ratios = ["1e3"]
#iterations = [1000,2100,700,500,900,400,950]
iterations = ["100","21","70","50","90","40","95"]

num_of_trans = 4

i = 0
for pattern in patterns:
    for tyyli in styles:
        for loss in loss_ratios:
            i+=1

k = 0
for depth_style in styles:
    k += num_of_trans
print("number of transfers to do: ",k)

print("_" * 40)
#print("Style transfers to perform: ", i)

j = 0
dur_list = []
start_time = time.time()

for depth_style in styles:
    rand_content = random.sample(patterns, num_of_trans)
    print("random content chosen: ", rand_content)
    for cont_pattern in rand_content:
        rand_iteration = random.choice(iterations)
        rand_loss = random.choice(loss_ratios)

        d_style_path = style_path + depth_style
        content_path = pattern_path + cont_pattern
        output_path = results_path[:-1] + \
                      cont_pattern.split(".")[0] + \
                      "-" + depth_style.split(".")[0] + \
                      "_lo-" + rand_loss + \
                      "_it-" + rand_iteration
        j += 1
        inst_start_time = time.time()
        try:
            print("_" * 40)
            print("   ")
            print("running style transfer  ", j, " of ", k)
            print("loss: ", rand_loss, "    iterations: ", rand_iteration)
            print("_" * 40)
            os.system(run_helper(
                content_path,
                d_style_path,
                output_path,
                rand_loss,
                rand_iteration,
                depth_style.split(".")[0],
                cont_pattern.split(".")[0]))
        except:
            print("some error happened")

        elapsed = time.time() - start_time
        inst_dur = time.time() - inst_start_time
        dur_list.append(inst_dur)
        print("_" * 60)
        print("   ")
        print("style transfer done in: ", inst_dur)
        print("elapsed time in s:", elapsed)
        average_dur = sum(dur_list) / len(dur_list)
        print("average solve time: ", average_dur)
        remaining_solves = k - j
        remaining_time = remaining_solves * average_dur
        remaining_time = datetime.timedelta(seconds=remaining_time)
        print("remaining solves: ", remaining_solves)
        print("estimated remaining time:", remaining_time)
        print("_" * 40)

'''
for iteration in iterations:
    for loss in loss_ratios:
        for pattern in patterns:
            for tyyli in styles:
                tyyli_path = style_path + tyyli
                content_path = pattern_path + pattern
                output_path = results_path[:-1] + \
                              pattern.split(".")[0] + \
                              "-" + tyyli.split(".")[0] + \
                              "_lo-" + loss + \
                              "_it-" + iteration



                #print("_" * 10)
                print(content_path, tyyli_path, output_path, loss)
                j += 1
                inst_start_time = time.time()
                try:
                    print("_"*40)
                    print("   ")
                    print("running style transfer  ", j ," of ", i)
                    print("loss: ", loss, "    iterations: ", iteration)
                    print("_" * 40)
                    os.system(run_helper(
                        content_path,
                        tyyli_path,
                        output_path,
                        loss,
                        iteration,
                        tyyli.split(".")[0],
                        pattern.split(".")[0]))
                except:
                    print("some error happened")

                elapsed = time.time() - start_time
                inst_dur = time.time() - inst_start_time
                dur_list.append(inst_dur)
                print("_" * 60)
                print("   ")
                print("style transfer done in: ", inst_dur )
                print("elapsed time in s:", elapsed)
                average_dur = sum(dur_list) / len(dur_list)
                print("average solve time: ", average_dur)
                remaining_solves = i - j
                remaining_time = remaining_solves * average_dur
                remaining_time = datetime.timedelta(seconds=remaining_time)
                print("remaining solves: ", remaining_solves)
                print("estimated remaining time:", remaining_time )
                print("_" * 40)
'''

print("_"*40)
print("   ")

git_c_mess = "git commit -m " + "\" ran style transfer " + str(i) + " times saved in" + res_path +" \""
print("commit message: ",git_c_mess)

os.system("git add . ")
os.system(git_c_mess)
os.system("git push")
