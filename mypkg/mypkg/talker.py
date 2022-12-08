import rclpy  #ROS2のクライアントのためのライブラリ
from rclpy.node import Node  #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.msg import Int16 #通信の方を指定
 
rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)   #パブリッシャのオブジェクト作成
n = 0

def cb():
    global n
    msg = Int16()   #メッセージの「オブジェクト」
    msg.data = n
    pub.publish(msg)
    n += 1
 
node.create_timer(0.5, cb)
rclpy.spin(node)
