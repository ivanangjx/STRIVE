# Copyright (c) 2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# SPDX-License-Identifier: MIT

'''
Given a directory of scenarios (.json files), visualizes them.
'''

import os, time
import configargparse
import torch

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from datasets.map_env import NuScenesMapEnv
from datasets.utils import read_adv_scenes
import datasets.nuscenes_utils as nutils
from utils.common import dict2obj, mkdir

from datetime import datetime # ivan- change time format for output directory

def parse_cfg():
    '''
    Parse given config file into a config object.
    Returns: config object and config dict
    '''
    parser = configargparse.ArgParser(formatter_class=configargparse.ArgumentDefaultsHelpFormatter,
                                      config_file_parser_class=configargparse.YAMLConfigFileParser,
                                      description='Viz sceanrios')
    # logging
    parser.add_argument('--out', type=str, default='./out/viz_scenarios_out',
                        help='Directory to save visualizations to.')

    # scenarios
    parser.add_argument('--scenarios', type=str, required=True,
                        help='Directory to load scenarios from, should contain json files')

    # dir to load map data in from
    parser.add_argument('--data_dir', type=str, default='./data/nuscenes',
                        help='Directory to load data from.')

    # viz options
    parser.add_argument('--viz_video', dest='viz_video', action='store_true', help="Whether to save video or just trajectories")
    parser.set_defaults(viz_video=False)

    args = parser.parse_args()
    config_dict = vars(args)
    # Config dict to object
    config = dict2obj(config_dict)
    
    return config, config_dict

def viz_scenario(scene, map_env, out_path,
                L=720,
                W=720,
                video=False):

    viz_out_path = out_path

    # print(viz_out_path)
    # viz_out_path = out_path + '/' + out_path

    scene_past = scene['scene_past'][:,:,:4]

    # print('scene_past -----------------------------------------------------------')
    # print(scene_past)
    # print('scene_past END -----------------------------------------------------------' +'\n')

    scene_fut = scene['scene_fut']

    # print('scene_fut -----------------------------------------------------------')
    # print(scene_fut)
    # print('scene_fut END -----------------------------------------------------------'+'\n')

    ivan_scene_fut_init = scene['scene_fut_init']

    # print('ivan_scene_fut_init -----------------------------------------------------------')
    # print(ivan_scene_fut_init)
    # print('ivan_scene_fut_init END -----------------------------------------------------------'+'\n')


    lw = scene['veh_att']

    # print('lw a.k.a veh_att -----------------------------------------------------------')
    # print(lw)
    # print('lw a.k.a veh_att -----------------------------------------------------------'+'\n')

    T = scene_past.size(1)

    # print('T = scene_past.size(1) -----------------------------------------------------------')
    # print(T)
    # print('T = scene_past.size(1) -----------------------------------------------------------'+'\n')


    crop_pos = scene_fut[0:1, T // 2, :2] # crop around ego
    centroid_states = scene_fut[:, T // 2, :2] - crop_pos
    bound_max = torch.amax(torch.abs(centroid_states)).item()# + 5.0
    bounds = [-bound_max, -bound_max, bound_max, bound_max]

    scene_traj = torch.cat([scene_past, ivan_scene_fut_init], dim=1) # ivan- combine past and future scenes


    # DO IT FOR SAFE/ INITAL SCENE TRAJECTORY ---------------------------------------------------------
    NA, NT, _ = scene_traj.size()

    map_name = scene['map']
    map_idx = map_env.map_list.index(map_name)
    crop_h = torch.Tensor([[1.0, 0.0]])
    crop_kin = torch.cat([crop_pos, crop_h], dim=1)

    # render local map crop
    map_rend = map_env.get_map_crop_pos(crop_kin,
                                        torch.tensor([map_idx], dtype=torch.long),
                                        bounds=bounds,
                                        L=L,
                                        W=W)[0]
    # transform trajectory into this cropped frame
    crop_traj, crop_lw = map_env.objs2crop(crop_kin[0],
                                            scene_traj.reshape(NA*NT, 4),
                                            lw,
                                            None,
                                            bounds=bounds,
                                            L=L,
                                            W=W)
    crop_traj = crop_traj.reshape(NA, NT, 4)


    

    nutils.ivan_out_map_json(map_rend, viz_out_path + '_safe.json',
                        crop_traj,
                        crop_lw,
                        viz_traj=True,
                        traj_markers=[False]*NA,
                        indiv=False
                        )

    nutils.viz_map_crop(map_rend, viz_out_path + '.png',
                        crop_traj,
                        crop_lw,
                        viz_traj=True,
                        traj_markers=[False]*NA, #ivan-initially this is false # change marker color 1 color to rainbow color
                        indiv=False
                        )

    nutils.ivan_viz_empty_map_crop(map_rend, viz_out_path + '_empty.png',
                        crop_traj,
                        crop_lw,
                        viz_traj=True,
                        traj_markers=[False]*NA, #ivan-initially this is false # change marker color 1 color to rainbow color
                        indiv=False
                        )

    # REPEAT FOR STRIVE ADVERSARIAL COLLISION TRAJECTORY ---------------------------------------------------------

    strive_traj = torch.cat([scene_past, scene_fut], dim=1) # ivan- combine past and future scenes

    NA, NT, _ = strive_traj.size()

    map_name = scene['map']
    map_idx = map_env.map_list.index(map_name)
    crop_h = torch.Tensor([[1.0, 0.0]])
    crop_kin = torch.cat([crop_pos, crop_h], dim=1)

    # render local map crop
    map_rend = map_env.get_map_crop_pos(crop_kin,
                                        torch.tensor([map_idx], dtype=torch.long),
                                        bounds=bounds,
                                        L=L,
                                        W=W)[0]
    # transform trajectory into this cropped frame
    crop_traj, crop_lw = map_env.objs2crop(crop_kin[0],
                                            strive_traj.reshape(NA*NT, 4),
                                            lw,
                                            None,
                                            bounds=bounds,
                                            L=L,
                                            W=W)
    crop_traj = crop_traj.reshape(NA, NT, 4)


    

    nutils.ivan_out_map_json(map_rend, viz_out_path + '_strive.json',
                        crop_traj,
                        crop_lw,
                        viz_traj=True,
                        traj_markers=[False]*NA,
                        indiv=False
                        )

    # -------------------------------------------------------------------------------------------------------------



def viz_scenario_dir(cfg):
    scenario_dir = cfg.scenarios
    out_path = cfg.out

    if not os.path.exists(scenario_dir):
        print('Could not find scenario_dir %s!' % (scenario_dir))
        exit()
    mkdir(out_path)

    scenes = read_adv_scenes(scenario_dir)
    print('Loaded:')
    print([s['name'] for s in scenes])

    # create map envrionment for visualization
    device = torch.device('cpu')
    data_path = os.path.join(cfg.data_dir, 'trainval')
    map_env = NuScenesMapEnv(data_path,
                             bounds=[-17.0, -38.5, 60.0, 38.5],
                             L=256,
                             W=256,
                            layers=['drivable_area', 'carpark_area', 'road_divider', 'lane_divider'],
                            device=device,
                            pix_per_m=8
                            )

    # visualize all scenes
    for cur_scene in scenes:
        viz_scene_path = os.path.join(out_path, cur_scene['name'])
        print(viz_scene_path)

        # mkdir(viz_scene_path)

        # print('1- json being loaded--------------------------------------------------------------')

        # print(cur_scene)
        # print(map_env)

        # print('1- json being loaded End ---------------------------------------------------------')

        viz_scenario(cur_scene, map_env, viz_scene_path, video=cfg.viz_video)

def main():
    cfg, cfg_dict = parse_cfg()

    # create output directory and logging

    # get current date and time
    now = datetime.now() 
    experiment_start_time = now.strftime("%m-%d_%H-%M-%S")

    cfg.out = cfg.out + "_" + str(experiment_start_time)
    mkdir(cfg.out)
    # save arguments used
    print('Args: ' + str(cfg_dict))

    viz_scenario_dir(cfg)

if __name__ == "__main__":
    main()