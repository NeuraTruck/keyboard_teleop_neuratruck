from launch import LaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir, Command
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    
    # ワールドファイルのパスを設定
    world_file_path = os.path.join('/home/taisyu/neuratruck_ws/src/keyboard_teleop_neuratruck/worlds', 'test.world')

    # GAZEBOのサーバーとクライアントのlaunchファイルのパスを取得
#    gazebo_ros_share_path = get_package_share_directory('gazebo_ros')
#    gzserver_launch_path = os.path.join(gazebo_ros_share_path, 'launch', 'gzserver.launch.py')
#    gzclient_launch_path = os.path.join(gazebo_ros_share_path, 'launch', 'gzclient.launch.py')

    # ワールドファイルのパスを渡すためのLaunchArgumentを定義
#    declare_world_arg = DeclareLaunchArgument(
#        'world', default_value=world_file_path,
#        description='Path to the world file.'
#    )
    # GAZEBOのサーバーとクライアントを起動するlaunchファイルを含む
#    gzserver = IncludeLaunchDescription(
#                PythonLaunchDescriptionSource(gzserver_launch_path),
#                launch_arguments={'world': LaunchConfiguration('world')}.items(),
#            )

#    gzclient = IncludeLaunchDescription(
#                PythonLaunchDescriptionSource(gzclient_launch_path),
#            )

    sdf_file_path = os.path.join(get_package_share_directory('keyboard_teleop'), 'model', 'truck03', 'model.sdf')
    
    # Gazeboを直接起動するコマンドを構築
    gazebo_cmd = ExecuteProcess(
        cmd=[
            'gazebo',
            '--verbose',
            world_file_path,
            '-s', 'libgazebo_ros_init.so',
            '-s', 'libgazebo_ros_factory.so'
        ],
        output='screen'
    )
            
    # 自律搬送車両モデルを配置するノード
    spawn_entity = Node(
            package='gazebo_ros', executable='spawn_entity.py',
            arguments=['-entity', 'truck03', '-file', sdf_file_path],
            output='screen'
    )

    return LaunchDescription([
        gazebo_cmd,
#        declare_world_arg,
#        gzserver,
#        gzclient,
        spawn_entity
    ])

