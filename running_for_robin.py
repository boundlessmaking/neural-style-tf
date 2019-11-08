#import run_main
import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # disables Tensorflow Warnings





results_path = "/run05-test-2/result05/"

style_path = "/run05-test-2/styles05/"
pattern_path = "/run05-test-2/image_input05/"

result_name= "result"

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
                 " --max_iterations 120 " + \
                 " --img_name " + result_name + "_" + loss
                 #" --verbose "  # + \
                 #" --device /cpu:0 "
    print(run_string)
    return run_string


#loss ratios to be tested

#loss_ratios = ["1e6", "1e4","1e2"]
loss_ratios = ["1e4"]

i = 0
for pattern in patterns:
    for tyyli in styles:
        for loss in loss_ratios:
            i+=1

print("_" * 40)
print("Style transfers to perform: ", i)

j = 0

for pattern in patterns:
    for tyyli in styles:
        for loss in loss_ratios:
            tyyli_path = style_path + tyyli
            content_path = pattern_path + pattern
            output_path = results_path + pattern.split(".")[0] + "_" + tyyli + "_" + loss +"_t1"
            print(content_path, tyyli_path, output_path, loss)
            j += 1
            try:
                print("_"*40)
                print("   ")
                print("running style transfer  ", j ," of ", i)
                print("_" * 40)
                os.system(run_helper(content_path, tyyli_path, output_path, loss))
            except:
                print("some error happened")

git_c_mess = "git commit -m " + "\" ran style transfer " + str(i) + " times saved in" + results_path +" \""
print(git_c_mess)

os.system("git add . ")
os.system(git_c_mess)
os.system("git push")
