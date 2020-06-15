import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument("--seed", default=0, type=int)  # Sets Gym, PyTorch and Numpy seeds
args = parser.parse_args()

def call(cmd, printy=True):
    x = subprocess.check_output(cmd, shell=True, universal_newlines=True)
    if printy:
        print(x)
    return x

call("cp ./duckietown_rl/ddpg.py ./model.py")
call(f"cp ./duckietown_rl/pytorch_models/DDPG_{args.seed}_actor.pth ./models/model_actor.pth")
call(f"cp ./duckietown_rl/pytorch_models/DDPG_{args.seed}_critic.pth ./models/model_critic.pth")
call(f"cp ./duckietown_rl/wrappers.py ./wrappers.py")

call("dts challenges submit")