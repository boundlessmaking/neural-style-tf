#import run_main
import os





results_path = "/Users/robin1/Projects/AI_Depth_maps/python_style_transf/neural-style-tf/image_output/result03/"

style_path = "/Users/robin1/Projects/AI_Depth_maps/python_style_transf/neural-style-tf/styles03/"
pattern_path = "/Users/robin1/Projects/AI_Depth_maps/python_style_transf/neural-style-tf/image_input/"



#these initialize the lists of styles and patterns in respective folders
styles = []
print(os.listdir(style_path))

for filename in os.listdir(style_path):
    if filename.endswith("jpg") or filename.endswith("png"):
        # Your code comes here such as
        print(filename)
        styles.append(filename)

print(styles)

patterns = []

print(os.listdir(pattern_path))

for filename in os.listdir(pattern_path):
    if filename.endswith("jpg") or filename.endswith("png"):
        # Your code comes here such as
        print(filename)
        patterns.append(filename)

print(patterns)


#this gives the system the run commands
def run_helper(content, style, output_path, loss):
    run_string = "python neural_style.py --content_img "+ content + " --style_imgs " + style + " --img_output_dir " + output_path + " --style_weight " + loss +" --max_iterations 1000" + " --device /cpu:0 "
    print(run_string)
    return run_string


#loss ratios to be tested
loss_ratios = ["1e4","1e2","1","1e-2","1e-4"]


#run this to do the stuff
for pattern in patterns:
    for tyyli in styles:
        for loss in loss_ratios:
            tyyli_path = style_path + tyyli
            content_path = pattern_path + pattern
            output_path = results_path + pattern.split(".")[0] + "_" + tyyli + "_" + loss +"_t1"
            print(content_path, tyyli_path, output_path, loss)
            try:
                print("running files")
                os.system(run_helper(content_path, tyyli_path, output_path, loss))
            except:
                print("some error happened")
