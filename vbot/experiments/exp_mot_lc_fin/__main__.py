import os
import sys
import time
import shutil
from math import degrees, atan2
import numpy as np


from .exp_manager import ExperimentManager
from .settings import *

from .my_imports import _prep_temp_folder, bf
from .plotter import *
from .arg_parser import VBOTParser

if __name__ == '__main__':
    ARG_PARSER = VBOTParser()
    ARGS = ARG_PARSER.args

    EXPERIMENT_SAVE_MODE_ON = 1
    WRITE_PLOT = 1 
    CONTROL_ON = 1 
    TRACKER_ON = 1 
    TRACKER_DISPLAY_ON = 1 
    USE_TRUE_KINEMATICS = 0 
    USE_REAL_CLOCK = 0 
    DRAW_OCCLUSION_BARS = 1 

    RUN_EXPERIMENT = 0 if ARGS.norun else 1
    RUN_TRACK_PLOT = 1 if ARGS.plot else 0

    RUN_VIDEO_WRITER = 0 


    if RUN_EXPERIMENT:
        EXPERIMENT_MANAGER = ExperimentManager(save_on=EXPERIMENT_SAVE_MODE_ON,
                                               write_plot=WRITE_PLOT,
                                               control_on=CONTROL_ON,
                                               tracker_on=TRACKER_ON,
                                               tracker_display_on=TRACKER_DISPLAY_ON,
                                               use_true_kin=USE_TRUE_KINEMATICS,
                                               use_real_clock=USE_REAL_CLOCK,
                                               draw_occlusion_bars=DRAW_OCCLUSION_BARS,
                                               args=ARGS)
        print(bf(f'\nExperiment started. [{time.strftime("%H:%M:%S")}]\n'))
        EXPERIMENT_MANAGER.run()

        print(bf(f'\n\nExperiment finished. [{time.strftime("%H:%M:%S")}]\n'))

    if RUN_TRACK_PLOT:
        FILE = open('plot_info.csv', 'r')
        
        # plot switches
        SHOW_ALL = 1    # set to 1 to show all plots 

        SHOW_CARTESIAN_PLOTS = 1
        SHOW_LOS_KIN_1 = 1
        SHOW_LOS_KIN_2 = 1
        SHOW_ACCELERATIONS = 1
        SHOW_TRAJECTORIES = 1
        SHOW_SPEED_HEADING = 1
        SHOW_ALTITUDE_PROFILE = 0
        SHOW_3D_TRAJECTORIES = 1
        SHOW_DELTA_TIME_PROFILE = 0
        SHOW_Y1_Y2 = 0


        TIME = []

        FP_1_X = []
        FP_1_Y = []
        FP_1_VX = []
        FP_1_VY = []
        FP_1_AX = []
        FP_1_AY = []
        FP_1_R = []
        FP_1_THETA = []
        FP_1_V_R = []
        FP_1_V_THETA = []
        FP_1_SPEED = []
        FP_1_HEADING = []
        FP_1_ACC = []
        FP_1_DELTA = []
        FP_2_X = []
        FP_2_Y = []
        FP_2_VX = []
        FP_2_VY = []
        FP_2_AX = []
        FP_2_AY = []
        FP_2_R = []
        FP_2_THETA = []
        FP_2_V_R = []
        FP_2_V_THETA = []
        FP_2_SPEED = []
        FP_2_HEADING = []
        FP_2_ACC = []
        FP_2_DELTA = []
        Y_1 = []
        Y_2 = []
        A_LAT = []
        A_LNG = []
        S = []
        C = []
        Z_W = []
        S_DOT = []
        C_DOT = []
        Z_W_DOT = []
        AZ_S = []
        AZ_C = []
        AZ_Z = []
        AZ = []

        T_1_OCCLUSION_CASE = []
        T_1_X_MEAS = []
        T_1_Y_MEAS = []
        T_1_R_MEAS = []
        T_1_THETA_MEAS = []
        T_1_X_EST = []
        T_1_Y_EST = []
        T_1_VX_EST = []
        T_1_VY_EST = []
        T_1_AX_EST = []
        T_1_AY_EST = []
        T_1_R_EST = []
        T_1_THETA_EST = []
        T_1_V_R_EST = []
        T_1_V_THETA_EST = []
        T_1_SPEED_EST = []
        T_1_BETA_EST = []
        T_1_ACC_EST = []
        T_1_DELTA_EST = []
        T_1_TRUE_R = []
        T_1_TRUE_THETA = []
        T_1_TRUE_V_R = []
        T_1_TRUE_V_THETA = []

        T_2_OCCLUSION_CASE = []
        T_2_X_MEAS = []
        T_2_Y_MEAS = []
        T_2_R_MEAS = []
        T_2_THETA_MEAS = []
        T_2_X_EST = []
        T_2_Y_EST = []
        T_2_VX_EST = []
        T_2_VY_EST = []
        T_2_AX_EST = []
        T_2_AY_EST = []
        T_2_R_EST = []
        T_2_THETA_EST = []
        T_2_V_R_EST = []
        T_2_V_THETA_EST = []
        T_2_SPEED_EST = []
        T_2_BETA_EST = []
        T_2_ACC_EST = []
        T_2_DELTA_EST = []
        T_2_TRUE_R = []
        T_2_TRUE_THETA = []
        T_2_TRUE_V_R = []
        T_2_TRUE_V_THETA = []

        T_3_OCCLUSION_CASE = []
        T_3_X_MEAS = []
        T_3_Y_MEAS = []
        T_3_R_MEAS = []
        T_3_THETA_MEAS = []
        T_3_X_EST = []
        T_3_Y_EST = []
        T_3_VX_EST = []
        T_3_VY_EST = []
        T_3_AX_EST = []
        T_3_AY_EST = []
        T_3_R_EST = []
        T_3_THETA_EST = []
        T_3_V_R_EST = []
        T_3_V_THETA_EST = []
        T_3_SPEED_EST = []
        T_3_BETA_EST = []
        T_3_ACC_EST = []
        T_3_DELTA_EST = []
        T_3_TRUE_R = []
        T_3_TRUE_THETA = []
        T_3_TRUE_V_R = []
        T_3_TRUE_V_THETA = []

        DRONE_POS_X = []
        DRONE_POS_Y = []
        DRONE_VEL_X = []
        DRONE_VEL_Y = []
        CAM_ORIGIN_X = []
        CAM_ORIGIN_Y = []
        DRONE_POS_X_W = []
        DRONE_POS_Y_W = []
        DRONE_SPEED = []
        DRONE_ALPHA = []
        C_DESIRED = []
        SCZ_IND = []
        ELLIPSE_MAJOR = []
        ELLIPSE_MINOR = []
        ELLIPSE_ROT_ANG = []
        A_LAT_LONG_DENOM = []

        # get all the data in memory
        for line in FILE.readlines():
            # skip first line (header)
            if line.split(',')[0].strip().lower()=='time':
                continue
            data = tuple(map(float, list(map(str.strip, line.strip().split(',')))))
            TIME.append(data[0])
            FP_1_X.append(data[1])
            FP_1_Y.append(data[2])
            FP_1_VX.append(data[3])
            FP_1_VY.append(data[4])
            FP_1_AX.append(data[5])
            FP_1_AY.append(data[6])
            FP_1_R.append(data[7])
            FP_1_THETA.append(data[8])
            FP_1_V_R.append(data[9])
            FP_1_V_THETA.append(data[10])
            FP_1_SPEED.append(data[11])
            FP_1_HEADING.append(data[12])
            FP_1_ACC.append(data[13])
            FP_1_DELTA.append(data[14])
            FP_2_X.append(data[15])
            FP_2_Y.append(data[16])
            FP_2_VX.append(data[17])
            FP_2_VY.append(data[18])
            FP_2_AX.append(data[19])
            FP_2_AY.append(data[20])
            FP_2_R.append(data[21])
            FP_2_THETA.append(data[22])
            FP_2_V_R.append(data[23])
            FP_2_V_THETA.append(data[24])
            FP_2_SPEED.append(data[25])
            FP_2_HEADING.append(data[26])
            FP_2_ACC.append(data[27])
            FP_2_DELTA.append(data[28])
            Y_1.append(data[29])
            Y_2.append(data[30])
            A_LAT.append(data[31])
            A_LNG.append(data[32])
            S.append(data[33])
            C.append(data[34])
            Z_W.append(data[35])
            S_DOT.append(data[36])
            C_DOT.append(data[37])
            Z_W_DOT.append(data[38])
            AZ_S.append(data[39])
            AZ_C.append(data[40])
            AZ_Z.append(data[41])
            AZ.append(data[42])
            T_1_OCCLUSION_CASE.append(data[43])
            T_1_X_MEAS.append(data[44])
            T_1_Y_MEAS.append(data[45])
            T_1_R_MEAS.append(data[46])
            T_1_THETA_MEAS.append(data[47])
            T_1_X_EST.append(data[48])
            T_1_Y_EST.append(data[49])
            T_1_VX_EST.append(data[50])
            T_1_VY_EST.append(data[51])
            T_1_AX_EST.append(data[52])
            T_1_AY_EST.append(data[53])
            T_1_R_EST.append(data[54])
            T_1_THETA_EST.append(data[55])
            T_1_V_R_EST.append(data[56])
            T_1_V_THETA_EST.append(data[57])
            T_1_SPEED_EST.append(data[58])
            T_1_BETA_EST.append(data[59])
            T_1_ACC_EST.append(data[60])
            T_1_DELTA_EST.append(data[61])
            T_1_TRUE_R.append(data[62])
            T_1_TRUE_THETA.append(data[63])
            T_1_TRUE_V_R.append(data[64])
            T_1_TRUE_V_THETA.append(data[65])
            T_2_OCCLUSION_CASE.append(data[66])
            T_2_X_MEAS.append(data[67])
            T_2_Y_MEAS.append(data[68])
            T_2_R_MEAS.append(data[69])
            T_2_THETA_MEAS.append(data[70])
            T_2_X_EST.append(data[71])
            T_2_Y_EST.append(data[72])
            T_2_VX_EST.append(data[73])
            T_2_VY_EST.append(data[74])
            T_2_AX_EST.append(data[75])
            T_2_AY_EST.append(data[76])
            T_2_R_EST.append(data[77])
            T_2_THETA_EST.append(data[78])
            T_2_V_R_EST.append(data[79])
            T_2_V_THETA_EST.append(data[80])
            T_2_SPEED_EST.append(data[81])
            T_2_BETA_EST.append(data[82])
            T_2_ACC_EST.append(data[83])
            T_2_DELTA_EST.append(data[84])
            T_2_TRUE_R.append(data[85])
            T_2_TRUE_THETA.append(data[86])
            T_2_TRUE_V_R.append(data[87])
            T_2_TRUE_V_THETA.append(data[88])
            T_3_OCCLUSION_CASE.append(data[89])
            T_3_X_MEAS.append(data[90])
            T_3_Y_MEAS.append(data[91])
            T_3_R_MEAS.append(data[92])
            T_3_THETA_MEAS.append(data[93])
            T_3_X_EST.append(data[94])
            T_3_Y_EST.append(data[95])
            T_3_VX_EST.append(data[96])
            T_3_VY_EST.append(data[97])
            T_3_AX_EST.append(data[98])
            T_3_AY_EST.append(data[99])
            T_3_R_EST.append(data[100])
            T_3_THETA_EST.append(data[101])
            T_3_V_R_EST.append(data[102])
            T_3_V_THETA_EST.append(data[103])
            T_3_SPEED_EST.append(data[104])
            T_3_BETA_EST.append(data[105])
            T_3_ACC_EST.append(data[106])
            T_3_DELTA_EST.append(data[107])
            T_3_TRUE_R.append(data[108])
            T_3_TRUE_THETA.append(data[109])
            T_3_TRUE_V_R.append(data[110])
            T_3_TRUE_V_THETA.append(data[111])
            DRONE_POS_X.append(data[112])
            DRONE_POS_Y.append(data[113])
            DRONE_VEL_X.append(data[114])
            DRONE_VEL_Y.append(data[115])
            CAM_ORIGIN_X.append(data[116])
            CAM_ORIGIN_Y.append(data[117])
            DRONE_POS_X_W.append(data[118])
            DRONE_POS_Y_W.append(data[119])
            DRONE_SPEED.append(data[120])
            DRONE_ALPHA.append(data[121])
            C_DESIRED.append(data[122])
            SCZ_IND.append(data[123])
            ELLIPSE_MAJOR.append(data[124])
            ELLIPSE_MINOR.append(data[125])
            ELLIPSE_ROT_ANG.append(data[126])
            A_LAT_LONG_DENOM.append(data[127])

        FILE.close()

        # plot
        if len(TIME) < 5:
            print('Not enough data to plot.')
            sys.exit()
        import matplotlib.pyplot as plt
        import scipy.stats as st

        _PATH = f'./sim_outputs/{time.strftime("%Y-%m-%d_%H-%M-%S")}'
        _prep_temp_folder(os.path.realpath(_PATH))

        # copy the plot_info file to the where plots figured will be saved
        shutil.copyfile('plot_info.csv', f'{_PATH}/plot_info.csv')
        plt.style.use(['seaborn-paper', 'fast'])

        los_1_plotter = LOS1DataPlotter(_PATH,
                                        TIME,
                                        T_1_TRUE_R,
                                        T_1_R_MEAS,
                                        T_1_R_EST,
                                        T_2_TRUE_R,
                                        T_2_R_MEAS,
                                        T_2_R_EST,
                                        T_3_TRUE_R,
                                        T_3_R_MEAS,
                                        T_3_R_EST,
                                        FP_1_R,
                                        FP_2_R,
                                        T_1_TRUE_THETA,
                                        T_1_THETA_MEAS,
                                        T_1_THETA_EST,
                                        T_2_TRUE_THETA,
                                        T_2_THETA_MEAS,
                                        T_2_THETA_EST,
                                        T_3_TRUE_THETA,
                                        T_3_THETA_MEAS,
                                        T_3_THETA_EST,
                                        FP_1_THETA,
                                        FP_2_THETA
                                        )

        los_1_plotter.plot()

        los_2_plotter = LOS2DataPlotter(_PATH,
                                        TIME,
                                        T_1_TRUE_V_R,
                                        T_1_V_R_EST,
                                        T_2_TRUE_V_R,
                                        T_2_V_R_EST,
                                        T_3_TRUE_V_R,
                                        T_3_V_R_EST,
                                        FP_1_V_R,
                                        FP_2_V_R,
                                        T_1_TRUE_V_THETA,
                                        T_1_V_THETA_EST,
                                        T_2_TRUE_V_THETA,
                                        T_2_V_THETA_EST,
                                        T_3_TRUE_V_THETA,
                                        T_3_V_THETA_EST,
                                        FP_1_V_THETA,
                                        FP_2_V_THETA
                                        )

        los_2_plotter.plot()

        accl_comm_plotter = AccelerationCommandDataPlotter(_PATH,
                                                           TIME,
                                                           A_LAT,
                                                           A_LNG,
                                                           AZ
                                                           )

        accl_comm_plotter.plot()

        ellipse_plotter = EllipseDataPlotter(_PATH,
                                             TIME,
                                             ELLIPSE_MAJOR,
                                             ELLIPSE_MINOR,
                                             ELLIPSE_ROT_ANG
                                             )

        ellipse_plotter.plot()

        obj_func_plotter = ObjectiveFunctionDataPlotter(_PATH,
                                                        TIME,
                                                        Y_1,
                                                        Y_2
                                                        )

        obj_func_plotter.plot()

        speeds_headings_plotter = SpeedsHeadingsDataPlotter(_PATH,
                                                            TIME,
                                                            T_1_SPEED_EST,
                                                            T_2_SPEED_EST,
                                                            T_3_SPEED_EST,
                                                            FP_1_SPEED,
                                                            FP_2_SPEED,
                                                            DRONE_SPEED,
                                                            T_1_BETA_EST,
                                                            T_2_BETA_EST,
                                                            T_3_BETA_EST,
                                                            FP_1_HEADING,
                                                            FP_2_HEADING,
                                                            DRONE_ALPHA
                                                            )

        speeds_headings_plotter.plot()

        trajectory_world_plotter = TrajectoryWorldDataPlotter(_PATH,
                                                              TIME,
                                                              T_1_X_EST,
                                                              T_1_Y_EST,
                                                              T_2_X_EST,
                                                              T_2_Y_EST,
                                                              T_3_X_EST,
                                                              T_3_Y_EST,
                                                              FP_1_X,
                                                              FP_1_Y,
                                                              FP_2_X,
                                                              FP_2_Y,
                                                              DRONE_POS_X_W,
                                                              DRONE_POS_Y_W,
                                                              )

        trajectory_world_plotter.plot()

        trajectory_camera_plotter = TrajectoryCameraDataPlotter(_PATH,
                                                               TIME,
                                                               T_1_X_EST,
                                                               T_1_Y_EST,
                                                               T_2_X_EST,
                                                               T_2_Y_EST,
                                                               T_3_X_EST,
                                                               T_3_Y_EST,
                                                               FP_1_X,
                                                               FP_1_Y,
                                                               FP_2_X,
                                                               FP_2_Y,
                                                               DRONE_POS_X_W,
                                                               DRONE_POS_Y_W,
                                                               )

        trajectory_camera_plotter.plot()

        altitude_control_plotter = AltitudeControlDataPlotter(_PATH,
                                                              TIME,
                                                              S,
                                                              C,
                                                              Z_W,
                                                              C_DESIRED
                                                              )

        altitude_control_plotter.plot()

        traj3d_plotter = Traj3DDataPlotter(_PATH,
                                                              TIME,
                                                              T_1_X_EST,
                                                              T_1_Y_EST,
                                                              T_2_X_EST,
                                                              T_2_Y_EST,
                                                              T_3_X_EST,
                                                              T_3_Y_EST,
                                                              FP_1_X,
                                                              FP_1_Y,
                                                              FP_2_X,
                                                              FP_2_Y,
                                                              DRONE_POS_X_W,
                                                              DRONE_POS_Y_W,
                                                              Z_W
                                                              )

        traj3d_plotter.plot()


        f1 ,a1 = plt.subplots()
        a1.plot(TIME, C_DOT)
        a1.grid(True, which='minor', alpha=0.1)
        a1.grid(True, which='major', alpha=0.3)
        f1.suptitle(r'$\dot{C}$')
        f1.savefig(f'{_PATH}/8_cdot.pdf')
        f1.show()

        f2 ,a2 = plt.subplots()
        a2.plot(TIME, SCZ_IND)
        a2.grid(True, which='minor', alpha=0.1)
        a2.grid(True, which='major', alpha=0.3)
        f2.suptitle(f'SCZ - 012')
        f2.savefig(f'{_PATH}/9_scz_ind.pdf')
        f2.show()

        f3 ,a3 = plt.subplots()
        a3.plot(Z_W, S)
        a3.grid(True, which='minor', alpha=0.1)
        a3.grid(True, which='major', alpha=0.3)
        a3.axis('equal')
        f3.suptitle(f'z vs S')
        f3.savefig(f'{_PATH}/10_zs.pdf')
        f3.show()

        f4 ,a4 = plt.subplots()
        a4.plot(Z_W, C)
        a4.grid(True, which='minor', alpha=0.1)
        a4.grid(True, which='major', alpha=0.3)
        a4.axis('equal')
        f4.suptitle(f'z vs C')
        f4.savefig(f'{_PATH}/11_zc.pdf')
        f4.show()


        dist_SC = [0 for _ in TIME]
        for i in range(len(TIME)):
            dist_SC[i] = (S_DES - S[i] - min(0,C_DESIRED[i] - C[i]))
        prod_SC = [0 for _ in TIME]
        for i in range(len(TIME)):
            prod_SC[i] = ((S_DES - S[i])*min(0, C_DESIRED[i] - C[i]))

        f5 ,a5 = plt.subplots()
        a5.plot(TIME, dist_SC)
        a5.grid(True, which='minor', alpha=0.1)
        a5.grid(True, which='major', alpha=0.3)
        f5.suptitle(f'dist_SC_err')
        # f5.savefig(f'{_PATH}/11_zc.pdf')
        f5.show()
        f6 ,a6 = plt.subplots()
        a6.plot(TIME, prod_SC)
        a6.grid(True, which='minor', alpha=0.1)
        a6.grid(True, which='major', alpha=0.3)
        f6.suptitle(f'prod_SC_err')
        # f6.savefig(f'{_PATH}/11_zc.pdf')
        f6.show()
        """ 
        A1 = r1*Vtheta1/V1
        A2 = r2*Vtheta2/V2
        tau_num = r1*Vr1/V1**2 - r2*Vr2/V2**2
        tau_den = A1+A2
        tau = (tau_num/tau_den)**2
        """


        # V1 = [(FP_1_V_R[i]**2 + FP_1_V_THETA[i]**2)**0.5 for i in range(len(TIME))]
        # V2 = [(FP_2_V_R[i]**2 + FP_2_V_THETA[i]**2)**0.5 for i in range(len(TIME))]

        # A1 = [FP_1_R[i]*abs(FP_1_V_THETA[i])*V2[i] for i in range(len(TIME))]
        # A2 = [FP_2_R[i]*abs(FP_2_V_THETA[i])*V1[i] for i in range(len(TIME))]
        # A1_ = [FP_1_R[i]*abs(FP_1_V_THETA[i])/V1[i] for i in range(len(TIME))]
        # A2_ = [FP_2_R[i]*abs(FP_2_V_THETA[i])/V2[i] for i in range(len(TIME))]
        # TAUD = [FP_1_R[i]*abs(FP_1_V_THETA[i])/V1[i] + FP_2_R[i]*abs(FP_2_V_THETA[i])/V2[i] for i in range(len(TIME))]

        # A4 = [0 for _ in TIME]
        # sat = 20
        # # abs (TAUD[i]) > 0.1 ? TAUD[i] : 0.1 sign(TAUD[i])
        # for i in range(len(TIME)):
        #     if abs(TAUD[i]) > sat:
        #         A4[i] = TAUD[i]
        #     else:
        #         A4[i] = sat * np.sign(TAUD[i])

        
        # #  y1 = A1**2*(1+tau*V1**2) + A2**2*(1+tau*V2**2) + 2*A1*A2*pow((1+tau*(V1**2+V2**2)+tau**2*V1**2*V2**2),0.5)-4*(a)**2
        # TAUN = [FP_1_R[i]*FP_1_V_R[i]/V1[i]**2 - FP_2_R[i]*FP_2_V_R[i]/V2[i]**2 for i in range(len(TIME))]
        # TAU = [(TAUN[i] / TAUD[i])**2 for i in range(len(TIME))]
        # # TAU2 = [(TAUN[i] / (A4[i]))**2 for i in range(len(TIME))]

        # y1 = [0 for _ in TIME]
        # for i in range(len(TIME)):
        #     y1[i] = A1[i]**2*(1+TAU[i]*V1[i]**2) + A2[i]**2*(1+TAU[i]*V2[i]**2) + 2*A1[i]*A2[i]*pow((1+TAU[i]*(V1[i]**2+V2[i]**2)+TAU[i]**2*V1[i]**2*V2[i]**2),0.5) - 4*(45)**2*V1[i]**2*V2[i]**2
        # y1_ = [0 for _ in TIME]
        # A1 = A1_
        # A2 = A2_
        # for i in range(len(TIME)):
        #     y1_[i] = A1[i]**2*(1+TAU[i]*V1[i]**2) + A2[i]**2*(1+TAU[i]*V2[i]**2) + 2*A1[i]*A2[i]*pow((1+TAU[i]*(V1[i]**2+V2[i]**2)+TAU[i]**2*V1[i]**2*V2[i]**2),0.5) - 4*(45)**2

        # signy1 = [np.sign(i) for i in y1]
        # signy1_ = [np.sign(i) for i in y1_]

        # f7 ,a7 = plt.subplots()
        # a7.plot(TIME, V1)
        # a7.plot(TIME, V2)
        # a7.grid(True, which='minor', alpha=0.1)
        # a7.grid(True, which='major', alpha=0.3)
        # f7.suptitle(f'V1 V2')
        # # f7.savefig(f'{_PATH}/11_zc.pdf')
        # f7.show()

        # f8 ,a8 = plt.subplots()
        # # a8.plot(TIME, A1)
        # # a8.plot(TIME, A2)
        # a8.plot(TIME, A1, alpha=0.7)
        # a8.plot(TIME, A2, alpha=0.7)
        # a8.grid(True, which='minor', alpha=0.1)
        # a8.grid(True, which='major', alpha=0.3)
        # f8.suptitle(f'A1 A2')
        # # f8.savefig(f'{_PATH}/11_zc.pdf')
        # f8.show()

        # f9 ,a9 = plt.subplots()
        # a9.plot(TIME, TAU)
        # a9.grid(True, which='minor', alpha=0.1)
        # a9.grid(True, which='major', alpha=0.3)
        # f9.suptitle(f'TAU')
        # # f9.savefig(f'{_PATH}/11_zc.pdf')
        # f9.show()

        # f10 ,a10 = plt.subplots()
        # a10.plot(TIME, y1)
        # a10.plot(TIME, y1_)
        # a10.grid(True, which='minor', alpha=0.1)
        # a10.grid(True, which='major', alpha=0.3)
        # f10.suptitle(f'new y1')
        # # f10.savefig(f'{_PATH}/11_zc.pdf')
        # f10.show()

        # f11 ,a11 = plt.subplots()
        # a11.plot(TIME, signy1, alpha=0.7,lw=3)
        # a11.plot(TIME, signy1_, alpha=0.9, lw=1.2)
        # a11.grid(True, which='minor', alpha=0.1)
        # a11.grid(True, which='major', alpha=0.3)
        # f11.suptitle(f'new signy1')
        # # f11.savefig(f'{_PATH}/11_zc.pdf')
        # f11.show()

        f12 ,a12 = plt.subplots()
        a12.plot(TIME, A_LAT_LONG_DENOM, alpha=0.7,lw=3)
        a12.grid(True, which='minor', alpha=0.1)
        a12.grid(True, which='major', alpha=0.3)
        f12.suptitle(f'A_LAT_LONG_DENOM')
        f12.savefig(f'{_PATH}/12_denom.pdf')
        f12.show()

        f13 ,a13 = plt.subplots()
        a13.plot(C, S)
        a13.grid(True, which='minor', alpha=0.1)
        a13.grid(True, which='major', alpha=0.3)
        a13.axis('equal')
        f13.suptitle(f'C vs S')
        f13.savefig(f'{_PATH}/13_cs.pdf')
        f13.show()

        DN = [0 for _ in TIME]
        for i in range(len(A_LAT_LONG_DENOM)):
            if abs(A_LAT_LONG_DENOM[i]) >= 10:
                DN[i] = 0#abs(1/A_LAT_LONG_DENOM[i])
            else:
                DN[i] = 1

        f14 ,a14 = plt.subplots()
        a14.plot(TIME, DN, alpha=0.7,lw=3)
        a14.grid(True, which='minor', alpha=0.1)
        a14.grid(True, which='major', alpha=0.3)
        f14.suptitle(f'A_LAT_LONG_DENOM < 10')
        f14.savefig(f'{_PATH}/14_denom_10.pdf')
        f14.show()

        X = [0 for _ in TIME]
        Y = [0 for _ in TIME]

        for i in range(len(TIME)):
            X[i] = T_1_X_MEAS[i] - T_2_X_MEAS[i]
            Y[i] = T_1_Y_MEAS[i] - T_2_Y_MEAS[i]

        f15 ,a15 = plt.subplots()
        a15.plot(TIME, X, alpha=0.7,lw=3)
        a15.plot(TIME, Y, alpha=0.7,lw=3)
        a15.grid(True, which='minor', alpha=0.1)
        a15.grid(True, which='major', alpha=0.3)
        f15.suptitle(f'T1 - T2 xy pos')
        f15.savefig(f'{_PATH}/15_t1_pos_meas.pdf')
        f15.show()

        f16 ,a16 = plt.subplots()
        # a16.plot(TIME, FP_1_X, alpha=0.7,lw=3)
        a16.plot(TIME, FP_1_Y, alpha=0.7,lw=3)
        a16.plot(TIME, FP_2_Y, alpha=0.7,lw=3)
        a16.grid(True, which='minor', alpha=0.1)
        a16.grid(True, which='major', alpha=0.3)
        f16.suptitle(f'FP_1')
        f16.savefig(f'{_PATH}/16_fp_1.pdf')
        f16.show()

        MID_X = [0 for _ in TIME]
        MID_Y = [0 for _ in TIME]

        for i in range(len(TIME)):
            MID_X[i] = (FP_1_X[i] + FP_2_X[i])/2
            MID_Y[i] = (FP_1_Y[i] + FP_2_Y[i])/2

        f17 ,a17 = plt.subplots()
        # a17.plot(TIME, MID_X, alpha=0.7,lw=3)
        a17.plot(TIME, MID_Y, alpha=0.7,lw=3)
        a17.grid(True, which='minor', alpha=0.1)
        a17.grid(True, which='major', alpha=0.3)
        f17.suptitle(f'FP_MID')
        f17.savefig(f'{_PATH}/17_fp_mid.pdf')
        f17.show()


        plt.show()

        # # -------------------------------------------------------------------------------- figure 1
        # # line of sight kinematics 1
        # if SHOW_ALL or SHOW_LOS_KIN_1:
        #     f0, axs = plt.subplots(2, 1, sharex=True, gridspec_kw={'hspace': 0.25})
        #     if SUPTITLE_ON:
        #         f0.suptitle(r'$\mathbf{Line\ of\ Sight\ Kinematics\ -\ I}$', fontsize=TITLE_FONT_SIZE)

        #     # t vs r
        #     axs[0].plot(
        #         _TIME,
        #         _MEASURED_R,
        #         color='forestgreen',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$measured\ r$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         _R,
        #         color='royalblue',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$estimated\ r$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         _TRUE_R,
        #         color='red',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$true\ r$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         [i*10 for i in _OCC_CASE],
        #         color='orange',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$case\ r$',
        #         alpha=0.9)

        #     axs[0].legend(loc='upper right')
        #     axs[0].set(ylabel=r'$r\ (m)$')
        #     axs[0].set_title(r'$\mathbf{r}$', fontsize=SUB_TITLE_FONT_SIZE)

        #     # t vs θ
        #     axs[1].plot(
        #         _TIME,
        #         _MEASURED_THETA,
        #         color='forestgreen',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$measured\ \theta$',
        #         alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         _THETA,
        #         color='royalblue',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$estimated\ \theta$',
        #         alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         _TRUE_THETA,
        #         color='red',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$true\ \theta$',
        #         alpha=0.9)

        #     axs[1].legend(loc='upper right')
        #     axs[1].set(xlabel=r'$time\ (s)$', ylabel=r'$\theta\ (^{\circ})$')
        #     axs[1].set_title(r'$\mathbf{\theta}$', fontsize=SUB_TITLE_FONT_SIZE)

        #     f0.savefig(f'{_PATH}/1_los1.png', dpi=300)
        #     f0.show()

        # # -------------------------------------------------------------------------------- figure 2
        # # line of sight kinematics 2
        # if SHOW_ALL or SHOW_LOS_KIN_2:
        #     f1, axs = plt.subplots(2, 1, sharex=True, gridspec_kw={'hspace': 0.25})
        #     if SUPTITLE_ON:
        #         f1.suptitle(r'$\mathbf{Line\ of\ Sight\ Kinematics\ -\ II}$', fontsize=TITLE_FONT_SIZE)

        #     # t vs vr
        #     axs[0].plot(
        #         _TIME,
        #         _MEASURED_V_R,
        #         color='palegreen',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$measured\ V_{r}$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         _V_R,
        #         color='royalblue',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_2,
        #         label=r'$estimated\ V_{r}$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         _TRUE_V_R,
        #         color='red',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$true\ V_{r}$',
        #         alpha=0.9)

        #     axs[0].legend(loc='upper right')
        #     axs[0].set(ylabel=r'$V_{r}\ (\frac{m}{s})$')
        #     axs[0].set_title(r'$\mathbf{V_{r}}$', fontsize=SUB_TITLE_FONT_SIZE)

        #     # t vs vtheta
        #     axs[1].plot(
        #         _TIME,
        #         _MEASURED_V_THETA,
        #         color='palegreen',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$measured\ V_{\theta}$',
        #         alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         _V_THETA,
        #         color='royalblue',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_2,
        #         label=r'$estimated\ V_{\theta}$',
        #         alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         _TRUE_V_THETA,
        #         color='red',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$true\ V_{\theta}$',
        #         alpha=0.9)

        #     axs[1].legend(loc='upper right')
        #     axs[1].set(xlabel=r'$time\ (s)$', ylabel=r'$V_{\theta}\ (\frac{m}{s})$')
        #     axs[1].set_title(r'$\mathbf{V_{\theta}}$', fontsize=SUB_TITLE_FONT_SIZE)

        #     f1.savefig(f'{_PATH}/1_los2.png', dpi=300)
        #     f1.show()

        # # -------------------------------------------------------------------------------- figure 2
        # # acceleration commands
        # if SHOW_ALL or SHOW_ACCELERATIONS:
        #     f2, axs = plt.subplots()
        #     if SUPTITLE_ON:
        #         f2.suptitle(r'$\mathbf{Acceleration\ commands}$', fontsize=TITLE_FONT_SIZE)

        #     axs.plot(
        #         _TIME,p
        #         _DRONE_ACC_LAT,
        #         color='forestgreen',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$a_{lat}$',
        #         alpha=0.9)
        #     axs.plot(
        #         _TIME,
        #         _DRONE_ACC_LNG,
        #         color='deeppink',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$a_{long}$',
        #         alpha=0.9)
        #     axs.legend()
        #     axs.set(xlabel=r'$time\ (s)$', ylabel=r'$acceleration\ (\frac{m}{s_{2}})$')

        #     f2.savefig(f'{_PATH}/2_accel.png', dpi=300)
        #     f2.show()

        # # -------------------------------------------------------------------------------- figure 3
        # # trajectories
        # if SHOW_ALL or SHOW_TRAJECTORIES:
        #     f3, axs = plt.subplots(2, 1, gridspec_kw={'hspace': 0.4})
        #     if SUPTITLE_ON:
        #         f3.suptitle(
        #             r'$\mathbf{Vehicle\ and\ UAS\ True\ Trajectories}$',
        #             fontsize=TITLE_FONT_SIZE)

        #     ndx = np.array(_DRONE_POS_X) + np.array(_CAM_ORIGIN_X)
        #     ncx = np.array(_CAR_POS_X) + np.array(_CAM_ORIGIN_X)
        #     ndy = np.array(_DRONE_POS_Y) + np.array(_CAM_ORIGIN_Y)
        #     ncy = np.array(_CAR_POS_Y) + np.array(_CAM_ORIGIN_Y)

        #     axs[0].plot(
        #         ndx,
        #         ndy,
        #         color='darkslategray',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$UAS$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         ncx,
        #         ncy,
        #         color='limegreen',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_2,
        #         label=r'$Vehicle$',
        #         alpha=0.9)
        #     axs[0].set(ylabel=r'$y\ (m)$')
        #     axs[0].set_title(r'$\mathbf{World\ frame}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs[0].legend()

        #     ndx = np.array(_DRONE_POS_X)
        #     ncx = np.array(_CAR_POS_X)
        #     ndy = np.array(_DRONE_POS_Y)
        #     ncy = np.array(_CAR_POS_Y)

        #     x_pad = (max(ncx) - min(ncx)) * 0.05
        #     y_pad = (max(ncy) - min(ncy)) * 0.05
        #     xl = max(abs(max(ncx)), abs(min(ncx))) + x_pad
        #     yl = max(abs(max(ncy)), abs(min(ncy))) + y_pad
        #     axs[1].plot(
        #         ndx,
        #         ndy,
        #         color='darkslategray',
        #         marker='+',
        #         markersize=10,
        #         label=r'$UAS$',
        #         alpha=0.7)
        #     axs[1].plot(
        #         ncx,
        #         ncy,
        #         color='limegreen',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_2,
        #         label=r'$Vehicle$',
        #         alpha=0.9)
        #     axs[1].set(xlabel=r'$x\ (m)$', ylabel=r'$y\ (m)$')
        #     axs[1].set_title(r'$\mathbf{Camera\ frame}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs[1].legend(loc='lower right')
        #     axs[1].set_xlim(-xl, xl)
        #     axs[1].set_ylim(-yl, yl)
        #     f3.savefig(f'{_PATH}/3_traj.png', dpi=300)
        #     f3.show()

        # # -------------------------------------------------------------------------------- figure 4
        # # true and estimated trajectories
        # if SHOW_ALL or SHOW_CARTESIAN_PLOTS:
        #     f4, axs = plt.subplots()
        #     if SUPTITLE_ON:
        #         f4.suptitle(
        #             r'$\mathbf{Vehicle\ True\ and\ Estimated\ Trajectories}$',
        #             fontsize=TITLE_FONT_SIZE)

        #     axs.plot(
        #         _TRACKED_CAR_POS_X,
        #         _TRACKED_CAR_POS_Y,
        #         color='darkturquoise',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$estimated\ trajectory$',
        #         alpha=0.9)
        #     axs.plot(
        #         _CAR_POS_X,
        #         _CAR_POS_Y,
        #         color='crimson',
        #         linestyle=':',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$true\ trajectory$',
        #         alpha=0.9)
        #     axs.set_title(r'$\mathbf{camera\ frame}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs.legend()
        #     axs.axis('equal')
        #     axs.set(xlabel=r'$x\ (m)$', ylabel=r'$y\ (m)$')
        #     f4.savefig(f'{_PATH}/4_traj_comp.png', dpi=300)
        #     f4.show()

        # # -------------------------------------------------------------------------------- figure 5
        # # true and tracked pos
        # if SHOW_ALL or SHOW_CARTESIAN_PLOTS:
        #     f4, axs = plt.subplots(2, 1, sharex=True, gridspec_kw={'hspace': 0.4})
        #     if SUPTITLE_ON:
        #         f4.suptitle(
        #             r'$\mathbf{Vehicle\ True\ and\ Estimated\ Positions}$',
        #             fontsize=TITLE_FONT_SIZE)

        #     axs[0].plot(
        #         _TIME,
        #         _TRACKED_CAR_POS_X,
        #         color='rosybrown',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$estimated\ x$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         _CAR_POS_X,
        #         color='red',
        #         linestyle=':',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$true\ x$',
        #         alpha=0.9)
        #     axs[0].set(ylabel=r'$x\ (m)$')
        #     axs[0].set_title(r'$\mathbf{x}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs[0].legend()
        #     axs[1].plot(
        #         _TIME,
        #         _TRACKED_CAR_POS_Y,
        #         color='mediumseagreen',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$estimated\ y$',
        #         alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         _CAR_POS_Y,
        #         color='green',
        #         linestyle=':',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$true\ y$',
        #         alpha=0.9)
        #     axs[1].set(xlabel=r'$time\ (s)$', ylabel=r'$y\ (m)$')
        #     axs[1].set_title(r'$\mathbf{y}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs[1].legend()
        #     f4.savefig(f'{_PATH}/5_pos_comp.png', dpi=300)
        #     f4.show()

        # # -------------------------------------------------------------------------------- figure 6
        # # true and tracked velocities
        # if SHOW_ALL or SHOW_CARTESIAN_PLOTS:
        #     f5, axs = plt.subplots(2, 1, sharex=True, gridspec_kw={'hspace': 0.4})
        #     if SUPTITLE_ON:
        #         f5.suptitle(
        #             r'$\mathbf{True,\ Measured\ and\ Estimated\ Vehicle\ Velocities}$',
        #             fontsize=TITLE_FONT_SIZE)

        #     axs[0].plot(
        #         _TIME,
        #         _MEASURED_CAR_VEL_X,
        #         color='paleturquoise',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$measured\ V_x$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         _TRACKED_CAR_VEL_X,
        #         color='darkturquoise',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$estimated\ V_x$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         _CAR_VEL_X,
        #         color='crimson',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_2,
        #         label=r'$true\ V_x$',
        #         alpha=0.7)
        #     axs[0].set(ylabel=r'$V_x\ (\frac{m}{s})$')
        #     axs[0].set_title(r'$\mathbf{V_x}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs[0].legend(loc='upper right')

        #     axs[1].plot(
        #         _TIME,
        #         _MEASURED_CAR_VEL_Y,
        #         color='paleturquoise',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$measured\ V_y$',
        #         alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         _TRACKED_CAR_VEL_Y,
        #         color='darkturquoise',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$estimated\ V_y$',
        #         alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         _CAR_VEL_Y,
        #         color='crimson',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_2,
        #         label=r'$true\ V_y$',
        #         alpha=0.7)
        #     axs[1].set(xlabel=r'$time\ (s)$', ylabel=r'$V_y\ (\frac{m}{s})$')
        #     axs[1].set_title(r'$\mathbf{V_y}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs[1].legend(loc='upper right')

        #     f5.savefig(f'{_PATH}/6_vel_comp.png', dpi=300)
        #     f5.show()

        # # -------------------------------------------------------------------------------- figure 7
        # # speed and heading
        # if SHOW_ALL or SHOW_SPEED_HEADING:
        #     f6, axs = plt.subplots(2, 1, sharex=True, gridspec_kw={'hspace': 0.4})
        #     if SUPTITLE_ON:
        #         f6.suptitle(
        #             r'$\mathbf{Vehicle\ and\ UAS,\ Speed\ and\ Heading}$',
        #             fontsize=TITLE_FONT_SIZE)
        #     c_speed = (CAR_INITIAL_VELOCITY[0]**2 + CAR_INITIAL_VELOCITY[1]**2)**0.5
        #     c_heading = degrees(atan2(CAR_INITIAL_VELOCITY[1], CAR_INITIAL_VELOCITY[0]))

        #     axs[0].plot(_TIME,
        #                 _CAR_SPEED,
        #                 color='lightblue',
        #                 linestyle='-',
        #                 linewidth=LINE_WIDTH_1,
        #                 label=r'$|V_{vehicle}|$',
        #                 alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         _DRONE_SPEED,
        #         color='blue',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$|V_{UAS}|$',
        #         alpha=0.9)
        #     axs[0].set(ylabel=r'$|V|\ (\frac{m}{s})$')
        #     axs[0].set_title(r'$\mathbf{speed}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs[0].legend()

        #     axs[1].plot(_TIME, _CAR_HEADING, color='lightgreen',
        #                 linestyle='-', linewidth=LINE_WIDTH_2, label=r'$\angle V_{vehicle}$', alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         _DRONE_ALPHA,
        #         color='green',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$\angle V_{UAS}$',
        #         alpha=0.9)
        #     axs[1].set(xlabel=r'$time\ (s)$', ylabel=r'$\angle V\ (^{\circ})$')
        #     axs[1].set_title(r'$\mathbf{heading}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs[1].legend()

        #     f6.savefig(f'{_PATH}/7_speed_head.png', dpi=300)
        #     f6.show()

        # # -------------------------------------------------------------------------------- figure 7
        # # altitude profile
        # if SHOW_ALL or SHOW_ALTITUDE_PROFILE:
        #     f7, axs = plt.subplots()
        #     if SUPTITLE_ON:
        #         f7.suptitle(r'$\mathbf{Altitude\ profile}$', fontsize=TITLE_FONT_SIZE)
        #     axs.plot(
        #         _TIME,
        #         _DRONE_ALTITUDE,
        #         color='darkgoldenrod',
        #         linestyle='-',
        #         linewidth=2,
        #         label=r'$altitude$',
        #         alpha=0.9)
        #     axs.set(xlabel=r'$time\ (s)$', ylabel=r'$z\ (m)$')

        #     f7.savefig(f'{_PATH}/8_alt_profile.png', dpi=300)
        #     f7.show()

        # # -------------------------------------------------------------------------------- figure 7
        # # 3D Trajectories
        # ndx = np.array(_DRONE_POS_X) + np.array(_CAM_ORIGIN_X)
        # ncx = np.array(_CAR_POS_X) + np.array(_CAM_ORIGIN_X)
        # ndy = np.array(_DRONE_POS_Y) + np.array(_CAM_ORIGIN_Y)
        # ncy = np.array(_CAR_POS_Y) + np.array(_CAM_ORIGIN_Y)

        # if SHOW_ALL or SHOW_3D_TRAJECTORIES:
        #     f8 = plt.figure()
        #     if SUPTITLE_ON:
        #         f8.suptitle(r'$\mathbf{3D\ Trajectories}$', fontsize=TITLE_FONT_SIZE)
        #     axs = f8.add_subplot(111, projection='3d')
        #     axs.plot3D(
        #         ncx,
        #         ncy,
        #         0,
        #         color='limegreen',
        #         linestyle='-',
        #         linewidth=2,
        #         label=r'$Vehicle$',
        #         alpha=0.9)
        #     axs.plot3D(
        #         ndx,
        #         ndy,
        #         _DRONE_ALTITUDE,
        #         color='darkslategray',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$UAS$',
        #         alpha=0.9)

        #     for point in zip(ndx, ndy, _DRONE_ALTITUDE):
        #         x = [point[0], point[0]]
        #         y = [point[1], point[1]]
        #         z = [point[2], 0]
        #         axs.plot3D(x, y, z, color='gainsboro', linestyle='-', linewidth=0.5, alpha=0.1)
        #     axs.plot3D(ndx, ndy, 0, color='silver', linestyle='-', linewidth=1, alpha=0.9)
        #     axs.scatter3D(ndx, ndy, _DRONE_ALTITUDE, c=_DRONE_ALTITUDE, cmap='plasma', alpha=0.3)

        #     axs.set(xlabel=r'$x\ (m)$', ylabel=r'$y\ (m)$', zlabel=r'$z\ (m)$')
        #     axs.view_init(elev=41, azim=-105)
        #     # axs.view_init(elev=47, azim=-47)
        #     axs.set_title(r'$\mathbf{World\ frame}$', fontsize=SUB_TITLE_FONT_SIZE)
        #     axs.legend()

        #     f8.savefig(f'{_PATH}/9_3D_traj.png', dpi=300)
        #     f8.show()

        # # -------------------------------------------------------------------------------- figure 7
        # # delta time
        # if SHOW_ALL or SHOW_DELTA_TIME_PROFILE:
        #     f9, axs = plt.subplots(2, 1, gridspec_kw={'hspace': 0.4})
        #     if SUPTITLE_ON:
        #         f9.suptitle(r'$\mathbf{Time\ Delay\ profile}$', fontsize=TITLE_FONT_SIZE)
        #     axs[0].plot(
        #         _TIME,
        #         _DELTA_TIME,
        #         color='darksalmon',
        #         linestyle='-',
        #         linewidth=2,
        #         label=r'$\Delta\ t$',
        #         alpha=0.9)
        #     axs[0].set(xlabel=r'$time\ (s)$', ylabel=r'$\Delta t\ (s)$')

        #     _NUM_BINS = 300
        #     _DIFF = max(_DELTA_TIME) - min(_DELTA_TIME)
        #     _BAR_WIDTH = _DIFF/_NUM_BINS if USE_REAL_CLOCK else DELTA_TIME * 0.1
        #     _RANGE = (min(_DELTA_TIME), max(_DELTA_TIME)) if USE_REAL_CLOCK else (-2*abs(DELTA_TIME), 4*abs(DELTA_TIME))
        #     _HIST = np.histogram(_DELTA_TIME, bins=_NUM_BINS, range=_RANGE, density=1) if USE_REAL_CLOCK else np.histogram(_DELTA_TIME, bins=_NUM_BINS, density=1)
        #     axs[1].bar(_HIST[1][:-1], _HIST[0]/sum(_HIST[0]), width=_BAR_WIDTH*0.9, 
        #                 color='lightsteelblue', label=r'$Frequentist\ PMF\ distribution$', alpha=0.9)
        #     if not USE_REAL_CLOCK:
        #         axs[1].set_xlim(-2*abs(DELTA_TIME), 4*abs(DELTA_TIME))
            
        #     if USE_REAL_CLOCK:
        #         _MIN, _MAX = axs[1].get_xlim()
        #         axs[1].set_xlim(_MIN, _MAX)
        #         _KDE_X = np.linspace(_MIN, _MAX, 301)
        #         _GAUSS_KER = st.gaussian_kde(_DELTA_TIME)
        #         _PDF_DELTA_T = _GAUSS_KER.pdf(_KDE_X)
        #         axs[1].plot(_KDE_X, _PDF_DELTA_T/sum(_PDF_DELTA_T), color='royalblue', linestyle='-',
        #                     linewidth=2, label=r'$Gaussian\ Kernel\ Estimate\ PDF$', alpha=0.8)
        #     axs[1].set(ylabel=r'$Probabilities$', xlabel=r'$\Delta t\ values$')
        #     axs[1].legend(loc='upper left')

        #     f9.savefig(f'{_PATH}/9_delta_time.png', dpi=300)

        #     f9.show()

        # # -------------------------------------------------------------------------------- figure 7
        # # y1, y2
        # if SHOW_ALL or SHOW_Y1_Y2:
        #     f10, axs = plt.subplots(2, 1, gridspec_kw={'hspace': 0.4})
        #     if SUPTITLE_ON:
        #         f10.suptitle(r'$\mathbf{Objectives}$', fontsize=TITLE_FONT_SIZE)
        #     axs[0].plot(
        #         _TIME,
        #         _TRUE_Y1,
        #         color='red',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$true\ y_1$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         _Y1,
        #         color='royalblue',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$estimated\ y_1$',
        #         alpha=0.9)
        #     axs[0].plot(
        #         _TIME,
        #         [K_W for _ in _TIME],
        #         color='orange',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$w_1$',
        #         alpha=0.9)
        #     axs[0].legend(loc='upper right')
        #     axs[0].set(ylabel=r'$y_1$')
        #     axs[0].set_title(r'$\mathbf{y_1}$', fontsize=SUB_TITLE_FONT_SIZE)

        #     axs[1].plot(
        #         _TIME,
        #         _TRUE_Y2,
        #         color='red',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$true\ y_2$',
        #         alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         _Y2,
        #         color='royalblue',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$estimated\ y_2$',
        #         alpha=0.9)
        #     axs[1].plot(
        #         _TIME,
        #         [0.0 for _ in _TIME],
        #         color='orange',
        #         linestyle='-',
        #         linewidth=LINE_WIDTH_1,
        #         label=r'$w_2$',
        #         alpha=0.9)

        #     axs[1].legend(loc='upper right')
        #     axs[1].set(xlabel=r'$time\ (s)$', ylabel=r'$y_2$')
        #     axs[1].set_title(r'$\mathbf{y_2}$', fontsize=SUB_TITLE_FONT_SIZE)


        #     f10.savefig(f'{_PATH}/10_objectives.png', dpi=300)

        #     f10.show()


        if not ARGS.batch:
            plt.show()

    if RUN_VIDEO_WRITER:
        EXPERIMENT_MANAGER = ExperimentManager()
        # create folder path inside ./sim_outputs
        _PATH = f'./sim_outputs/{time.strftime("%Y-%m-%d_%H-%M-%S")}'
        _prep_temp_folder(os.path.realpath(_PATH))
        VID_PATH = f'{_PATH}/sim_track_control.avi'
        print('Making video.')
        EXPERIMENT_MANAGER.make_video(VID_PATH, SIMULATOR_TEMP_FOLDER)
