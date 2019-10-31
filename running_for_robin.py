import run_main
import os





results_path = ""

style_path = "/home/liiru/ai/tensorflow-style-transfer-master/hyper/styles/"
pattern_path = "/home/liiru/ai/tensorflow-style-transfer-master/hyper/patterns/"



#these initialize the lists of styles and patterns in respective folders
styles = []

for filename in os.listdir(style_path):
    if filename.endswith("jpeg") or filename.endswith("jpg"):
        # Your code comes here such as
        print(filename)
        styles.append(filename)

patterns = []

for filename in os.listdir(pattern_path):
    if filename.endswith("jpeg") or filename.endswith("jpg"):
        # Your code comes here such as
        print(filename)
        patterns.append(filename)




#this gives the system the run commands
def run_helper(content, style, output_path, loss):
    run_string = "python neural_style.py --content_img "+ content + " --style_imgs " + style + " --img_output_dir " + output_path + " --loss_ratio " + loss +" --num_iter 50" + " --content_loss_function 3"
    return run_string


#loss ratios to be tested
loss_ratios = ["1e6","1e4","1e2","1","1e-2","1e-4","1e-6"]


#run this to do the stuff
for pattern in patterns:
    for tyyli in styles:
        for loss in loss_ratios:
            tyyli_path = style_path + tyyli
            content_path = pattern_path + pattern
            output_path = results_path + pattern.split(".")[0] + "_" + tyyli + "_" + loss +"_t1"
            try:
                os.system(run_helper(content_path, tyyli_path, output_path, loss))
            except:
                print("some error happened")
