cuda docker setup:
sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

docker things
to build:
sudo docker build . -t strive
after setting up:
sudo docker run -it --gpus all --runtime=nvidia -v /home/ivanAng/STRIVE:/app strive:latest

###################################################################################################################################################
#in nuscenes_dataset.py , the cfg splits are follows:

        pred_challenge_scenes = None # dict mapping scene_name -> list of instance-tok_sample-tok for each challenge split data
        if self.use_challenge_splits:
            from nuscenes.prediction import PredictHelper
            chall_split_map = {
                'train' : 'train',
                'val' : 'train_val',
                'test' : 'val'
            }
            pred_challenge_scenes, scenes, split_data = get_prediction_challenge_split(chall_split_map[self.split], dataroot=self.data_path)

###################################################################################################################################################







globalprotect connect --portal student-access.anu.edu.au


# LINKS -MIGHT BE OUTDATED ############################################
https://docs.sylabs.io/guides/3.11/user-guide/quick_start.html

https://docs.docker.com/engine/install/linux-postinstall/

#######################################################################

1. in local machine, install singlarty and go

https://docs.sylabs.io/guides/3.11/user-guide/quick_start.html


# change the go version from the quickstart lol
export VERSION=1.18.3 OS=linux ARCH=amd64 && \
  wget https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz && \
  sudo tar -C /usr/local -xzvf go$VERSION.$OS-$ARCH.tar.gz && \
  rm go$VERSION.$OS-$ARCH.tar.gz



install docker and dockerfile stuff


sudo singularity build strive.sif docker-daemon://strive:latest


# run this once in server
sbatch start.sbatch



# interative gpu shell
squeue
salloc -p gpu
ssh gpusrv-3 >> whatever appears from prev
singularity shell --nv strive.sif


scancel 142412




COMMANDS ##########################################################

singularity shell --nv strive.sif

python src/ivan_viz_empty_map.py --scenarios ./data/strive_scenarios/scenarios/test_replay/ --out ./out/viz_empty_maps --viz_video


# with split
python src/adv_scenario_gen.py --config ./configs/adv_gen_rule_based.cfg --ckpt model_ckpt/traffic_model.pth --use_challenge_splits


python src/adv_scenario_gen.py --config ./configs/adv_gen_rule_based.cfg --ckpt model_ckpt/traffic_model.pth --use_challenge_splits --split='val'







echo "# strive" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ivanangjx/strive.git
git push -u origin main


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


git add .
got commit -m ""
git push -u origin main
