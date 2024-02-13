from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # GAZEBOのサーバーとクライアントのlaunchファイルのパスを取得
    gazebo_ros_share_path = get_package_share_directory('gazebo_ros')
    gzserver_launch_path = os.path.join(gazebo_ros_share_path, 'launch', 'gzserver.launch.py')
    gzclient_launch_path = os.path.join(gazebo_ros_share_path, 'launch', 'gzclient.launch.py')

    # ワールドファイルのパスを設定
    world_file_path = LaunchConfiguration('world', default=os.path.join(gazebo_ros_share_path, 'worlds', 'empty.world'))

    # GAZEBOのサーバーとクライアントを起動するlaunchファイルを含む
    gzserver = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(gzserver_launch_path),
                launch_arguments={'world': world_file_path}.items(),
            )

    gzclient = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(gzclient_launch_path),
            )

    # 自律搬送車両モデルを配置するノード
    spawn_entity = Node(
        package='gazebo_ros', executable='spawn_entity.py',
        arguments=['-entity', 'model', '-topic', 'robot_description'],
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=os.path.join(gazebo_ros_share_path, 'worlds', 'empty.world'),
            description='Path to the world file'),
        gzserver,
        gzclient,
        spawn_entity
    ])

