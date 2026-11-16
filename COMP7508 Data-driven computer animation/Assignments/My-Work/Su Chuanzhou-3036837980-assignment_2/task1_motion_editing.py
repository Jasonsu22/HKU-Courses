import numpy as np
from scipy.spatial.transform import Rotation as R
from scipy.spatial.transform import Slerp

from file_io import BVHMotion
from Viewer.controller import SimpleViewer
from Viewer.viewer import ShowBVHUpdate

'''
Find the betweening data between left_data and right_data
Parameters:
    - left_data: the left data
    - right_data: the right data
    - t: the number of betweening frames
    - method: the interpolation method, 'linear' or 'slerp'
Return: An array for the betweening data, 
        if return_first_key=True, then including the known left one, 
        for example, if t=9, then the result should be 9 frames including the left one
'''
def interpolation(left_data, right_data, t, method='linear', return_first_key=True):
    res = [left_data] if return_first_key else []
    '''
    TODO: Implement following functions
    Hints:
        1. The shape of data is (num_joints, 3) for position and (num_joints, 4) for rotation
        2. The rotation data is in quaternion format
        3. We use linear interpolation for position and slerp for rotation
            * The linear interpolation can be obtained by the following formula:
                data_between = left_data + (right_data - left_data) * (i / t)
        4. We use scipy.spatial.transform.Slerp to do slerp interpolation (https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Slerp.html)
            * The Slerp can be obtained by the following code:
                key_rots = R.from_quat([q1, q2])
                key_frames= [0, 1]
                slerp = Slerp(key_times, key_rots)
                new_key_frames = np.linspace(0, 1, t+1))
                interp_rots = slerp(new_key_frames)
            * The slerp in scipy doesn't support quaternion with shape (num_joints, 4), 
              so you need to take the quaternion for each joint in a loop with joint_num,
              like left_data[joint_idx], then combine them after the loop.
            * Don't take the last frame of slerp, because it is the same as the right_data
    '''
    ########## Code Start ############
    # t frames cover [left, right): i / t for i = 0 .. t-1. res already holds
    # the left key (i = 0) when return_first_key is True. The right key belongs
    # to the next segment, so it is never repeated here.
    if t <= 0:
        return np.array(res) if res else np.zeros((0,) + np.shape(left_data))

    if method == 'linear':
        for i in range(1, t):
            res.append(left_data + (right_data - left_data) * (i / t))
        return np.array(res) if res else np.zeros((0,) + np.shape(left_data))
    elif method == 'slerp':
        # Drop both ends of linspace(0, 1, t+1): 0 is the left key (already in
        # res) and 1 is the right key.
        new_key_frames = np.linspace(0.0, 1.0, t + 1)[1:-1]
        num_joints = left_data.shape[0]
        interp = np.zeros((len(new_key_frames), num_joints, 4))
        for joint_idx in range(num_joints):
            q1 = np.array(left_data[joint_idx], dtype=float)
            q2 = np.array(right_data[joint_idx], dtype=float)
            # q and -q are the same rotation; flip so Slerp takes the short arc.
            if np.dot(q1, q2) < 0.0:
                q2 = -q2
            if len(new_key_frames) > 0:
                slerp = Slerp([0.0, 1.0], R.from_quat([q1, q2]))
                interp[:, joint_idx] = slerp(new_key_frames).as_quat()
        res.extend(interp)
        return np.array(res) if res else np.zeros((0,) + np.shape(left_data))
    ########## Code End ############

def part1_key_framing(viewer, time_step, target_step):
    motion = BVHMotion('data/motion_walking.bvh')
        
    motio_length = motion.local_joint_positions.shape[0]
    keyframes = np.arange(0, motio_length, time_step)
    
    new_motion_local_positions, new_motion_local_rotations = [], []
    
    previous_frame_idx = 0
    for current_frame_idx in keyframes[1:]:
        between_local_pos = interpolation(motion.local_joint_positions[previous_frame_idx], 
                                          motion.local_joint_positions[current_frame_idx], 
                                          target_step - 1, 'linear')
        between_local_rot = interpolation(motion.local_joint_rotations[previous_frame_idx], 
                                          motion.local_joint_rotations[current_frame_idx], 
                                          target_step - 1, 'slerp')
        new_motion_local_positions.append(between_local_pos)
        new_motion_local_rotations.append(between_local_rot)
        previous_frame_idx = current_frame_idx
    
    res_motion = motion.raw_copy()
    res_motion.local_joint_positions = np.concatenate(new_motion_local_positions)
    res_motion.local_joint_rotations = np.concatenate(new_motion_local_rotations)
    
    translation, orientation = res_motion.batch_forward_kinematics()
    task = ShowBVHUpdate(viewer, res_motion.joint_name, translation, orientation)
    viewer.addTask(task.update)
    
'''
Combine two different motions into one motion
Parameters:
    - motion1: the first motion
    - motion2: the second motion
    - last_frame_index: the last frame index of the first motion
    - start_frame_indx: the start frame index of the second motion
    - between_frames: the number of frames between the two motions
    - searching_frames: the number of frames for searching the closest frame
    - method: the interpolation method, 'interpolation' or 'inertialization'
'''
def concatenate_two_motions(motion1, motion2, last_frame_index, start_frame_indx, between_frames, searching_frames=20, method='interpolation'):
    '''
    TODO: Implement following functions
    Hints:
        1. We should operation on the local joint positions and rotations
            motion.local_joint_positions: (num_frames, num_joints, 3)
            motion.local_joint_rotations: (num_frames, num_joints, 4)
        2. There are five steps in the concatenation:
            i) get the searching windows for motion 1 and motion 2 
                win_1 = motion1.local_joint_rotations[last_frame_index - searching_frames:last_frame_index + searching_frames]
                win_2 = motion2.local_joint_rotations[max(0, start_frame_indx - searching_frames):start_frame_indx + searching_frames]
            ii) find the closest frame in motion 1 searching window and motion 2 searching window
                * You can use similarity matrix in DTW (Dynamic Time Warping) to find the closest frame (motion editing slides)
                * sim_matrix is a matrix with shape (win_1.shape[0], win_2.shape[0])
                * sim_matrix[i, j] = np.linalg.norm(search_source[i] - search_target[j])
                * Find the minimum value in sim_matrix and get the corresponding index i and j
            iii) the i and j is the index for the searching window, so convert it to the index in the original motion sequence
            iv) we have the pose in motion_1(real_i) and motion_2(real_j), then we can do the interpolation
                * The interpolation should be done for the *positions* and *rotations* both
                * (Shifting) You must align the root positions of motion_2(real_j) to the root positions of motion_1(real_i)
                # The shifting is done by updating variable: motion2.local_joint_positions = motion2.local_joint_positions - ?
            v) combine the motion1, betweening, motion2 into one motion (have been provided)
        3. You can get all marks if you done above steps correctly, but bonus will be given if you can do any one of them:
            (bonus) There are N between_frames, but the root position in these frames are not considered
            (bonus) The velocity of two motions are not the same, it can give different weight to the two motions interpolation
            (bonus) The inertialization method provides the best results ref:https://theorangeduck.com/page/spring-roll-call#inertialization
            (bonus) Any way to produce more smooth and natural transitions
    
    Useful functions:
        1. The differece between two vectors: np.linalg.norm(a - b)
        2. The index of minimal value in a matrix: np.argmin(dtw)
        3. local_joint_rotations = motion.local_joint_rotations
        4. local_joint_positions = motion.local_joint_positions
        5. Visualize the dtw matrix:
            import matplotlib.pyplot as plt
            plt.imshow(dtw)
            plt.show() # You can use plt.savefig('dtw.png') to save the image
    '''
    
    ########## Code Start ############
    # ---- small helpers (kept inside the Code block on purpose) ----
    def root_yaw(quat):
        forward = R.from_quat(quat).apply(np.array([0.0, 0.0, 1.0]))
        return float(np.arctan2(forward[0], forward[2]))

    def root_velocity(positions, frame, dt, forward):
        if positions.shape[0] < 2:
            return np.zeros(3)
        if forward and frame < positions.shape[0] - 1:
            return (positions[frame + 1, 0] - positions[frame, 0]) / dt
        if not forward and frame > 0:
            return (positions[frame, 0] - positions[frame - 1, 0]) / dt
        if frame < positions.shape[0] - 1:
            return (positions[frame + 1, 0] - positions[frame, 0]) / dt
        return (positions[frame, 0] - positions[frame - 1, 0]) / dt

    def hermite_position(p0, p1, v0, v1, tau, s):
        s2, s3 = s * s, s * s * s
        h00 = 2.0 * s3 - 3.0 * s2 + 1.0
        h10 = s3 - 2.0 * s2 + s
        h01 = -2.0 * s3 + 3.0 * s2
        h11 = s3 - s2
        return h00 * p0 + h10 * (tau * v0) + h01 * p1 + h11 * (tau * v1)

    def decay_offset(offset, offset_vel, halflife, dt):
        # Critically damped spring with equilibrium at 0 (spring-roll-call).
        d = 2.0 * np.log(2.0) / halflife
        j1 = offset_vel + d * offset
        decay = np.exp(-d * dt)
        return decay * (offset + j1 * dt), decay * (offset_vel - j1 * dt * d)

    def angular_velocity(q_from, q_to, dt):
        return (R.from_quat(q_to) * R.from_quat(q_from).inv()).as_rotvec() / dt

    def inertialize(src_pos, src_rot, prev_pos, prev_rot, dst_pos, dst_rot, halflife, dt):
        '''Play dst immediately, with a decaying correction that starts at src.'''
        src_vel = (src_pos - prev_pos) / dt
        if len(dst_pos) > 1:
            dst_vel0 = (dst_pos[1] - dst_pos[0]) / dt
            dst_avel0 = angular_velocity(dst_rot[0], dst_rot[1], dt)
        else:
            dst_vel0 = np.zeros_like(src_vel)
            dst_avel0 = np.zeros((src_rot.shape[0], 3))
        off_pos = src_pos - dst_pos[0]
        off_vel = src_vel - dst_vel0
        off_rot = (R.from_quat(src_rot) * R.from_quat(dst_rot[0]).inv()).as_rotvec()
        off_avel = angular_velocity(prev_rot, src_rot, dt) - dst_avel0
        out_pos = np.empty_like(dst_pos)
        out_rot = np.empty_like(dst_rot)
        for k in range(len(dst_pos)):
            out_pos[k] = dst_pos[k] + off_pos
            out_rot[k] = (R.from_rotvec(off_rot) * R.from_quat(dst_rot[k])).as_quat()
            off_pos, off_vel = decay_offset(off_pos, off_vel, halflife, dt)
            off_rot, off_avel = decay_offset(off_rot, off_avel, halflife, dt)
        return out_pos, out_rot

    dt = 1.0 / 60.0
    n1 = motion1.local_joint_rotations.shape[0]
    n2 = motion2.local_joint_rotations.shape[0]
    n_joints = motion1.local_joint_positions.shape[1]

    # i) Search windows around the requested cut, clamped to each clip.
    s1 = max(0, last_frame_index - searching_frames)
    e1 = min(n1, last_frame_index + searching_frames)
    s2 = max(0, start_frame_indx - searching_frames)
    e2 = min(n2, start_frame_indx + searching_frames)
    search_win1 = motion1.local_joint_rotations[s1:e1].copy()
    search_win2 = motion2.local_joint_rotations[s2:e2].copy()
    # The same rotation can be stored as q or -q. Put every quaternion in
    # w >= 0 so the Euclidean distance below is a pose distance.
    search_win1[search_win1[..., 3] < 0] *= -1
    search_win2[search_win2[..., 3] < 0] *= -1

    # ii) Similarity matrix: rows are motion1 frames, columns motion2 frames.
    src = search_win1.reshape(search_win1.shape[0], -1)
    dst = search_win2.reshape(search_win2.shape[0], -1)
    sim_matrix = np.linalg.norm(src[:, None, :] - dst[None, :, :], axis=-1)

    # iii) Window indices -> original clip indices.
    min_idx = int(np.argmin(sim_matrix))
    i, j = min_idx // sim_matrix.shape[1], min_idx % sim_matrix.shape[1]
    real_i, real_j = s1 + i, s2 + j

    # iv) Shift motion2 onto motion1: cancel the heading gap, then the root
    #     position gap. Child local rotations stay untouched.
    heading = R.from_rotvec(
        np.array([0.0, root_yaw(motion1.local_joint_rotations[real_i, 0])
                  - root_yaw(motion2.local_joint_rotations[real_j, 0]), 0.0])
    )
    pivot = motion2.local_joint_positions[real_j, 0].copy()
    target = motion1.local_joint_positions[real_i, 0].copy()
    motion2.local_joint_positions = motion2.local_joint_positions.copy()
    motion2.local_joint_rotations = motion2.local_joint_rotations.copy()
    motion2.local_joint_positions[:, 0] = heading.apply(
        motion2.local_joint_positions[:, 0] - pivot) + target
    motion2.local_joint_rotations[:, 0] = (
        heading * R.from_quat(motion2.local_joint_rotations[:, 0])).as_quat()

    # v) Bridge the two poses, or inertialize so motion2 plays immediately.
    if method == 'inertialization':
        prev_i = max(real_i - 1, 0)
        halflife = max(int(between_frames), 1) / 60.0
        tail_pos, tail_rot = inertialize(
            motion1.local_joint_positions[real_i],
            motion1.local_joint_rotations[real_i],
            motion1.local_joint_positions[prev_i],
            motion1.local_joint_rotations[prev_i],
            motion2.local_joint_positions[real_j:],
            motion2.local_joint_rotations[real_j:],
            halflife, dt)
        motion2.local_joint_positions[real_j:] = tail_pos
        motion2.local_joint_rotations[real_j:] = tail_rot
        between_local_pos = np.zeros((0, n_joints, 3))
        between_local_rot = np.zeros((0, n_joints, 4))
    else:
        between_local_pos = interpolation(
            motion1.local_joint_positions[real_i],
            motion2.local_joint_positions[real_j],
            between_frames, 'linear')
        between_local_rot = interpolation(
            motion1.local_joint_rotations[real_i],
            motion2.local_joint_rotations[real_j],
            between_frames, 'slerp')
        # (bonus) After the shift both roots coincide, so a plain lerp freezes
        # the body for the whole blend. Carry the root with a cubic Hermite
        # from motion1's velocity to motion2's, then slide the rest of motion2
        # forward by the same hand-off.
        if between_frames > 0:
            v1 = root_velocity(motion1.local_joint_positions, real_i, dt, forward=False)
            v2 = root_velocity(motion2.local_joint_positions, real_j, dt, forward=True)
            tau = between_frames * dt
            p0 = between_local_pos[0, 0].copy()
            p1 = p0 + 0.5 * (v1 + v2) * tau
            for frame_i in range(between_frames):
                s = frame_i / float(between_frames)
                between_local_pos[frame_i, 0] = hermite_position(p0, p1, v1, v2, tau, s)
            motion2.local_joint_positions[real_j:, 0] += (
                p1 - motion2.local_joint_positions[real_j, 0])
    ########## Code End ############
    
    res = motion1.raw_copy()
    res.local_joint_positions = np.concatenate([motion1.local_joint_positions[:real_i],
                                                between_local_pos,
                                                motion2.local_joint_positions[real_j:]], 
                                                axis=0)
    res.local_joint_rotations = np.concatenate([motion1.local_joint_rotations[:real_i],
                                                    between_local_rot, 
                                                    motion2.local_joint_rotations[real_j:]], 
                                                    axis=0)
    return res

        
def part2_concatenate(viewer, between_frames, do_interp=True):
    walk_forward = BVHMotion('data/motion_walking.bvh')
    run_forward = BVHMotion('data/motion_running.bvh')
    run_forward.adjust_joint_name(walk_forward.joint_name)
    
    last_frame_index = 40
    start_frame_indx = 0
    
    if do_interp:
        motion = concatenate_two_motions(walk_forward, run_forward, last_frame_index, start_frame_indx, between_frames, method='interpolation')
    else:
        motion = walk_forward.raw_copy()
        motion.local_joint_positions = np.concatenate([walk_forward.local_joint_positions[:last_frame_index],
                                                       run_forward.local_joint_positions[start_frame_indx:]], 
                                                       axis=0)
        motion.local_joint_rotations = np.concatenate([walk_forward.local_joint_rotations[:last_frame_index],
                                                        run_forward.local_joint_rotations[start_frame_indx:]], 
                                                        axis=0)         
    
    translation, orientation = motion.batch_forward_kinematics()
    task = ShowBVHUpdate(viewer, motion.joint_name, translation, orientation)
    viewer.addTask(task.update)
    pass


def main():
    viewer = SimpleViewer()  
   
    part1_key_framing(viewer, 10, 10)
    # part1_key_framing(viewer, 10, 5)
    # part1_key_framing(viewer, 10, 20)
    # part1_key_framing(viewer, 10, 30)
    # part2_concatenate(viewer, between_frames=8, do_interp=False)
    # part2_concatenate(viewer, between_frames=8)  
    viewer.run()


if __name__ == '__main__':
    main()
