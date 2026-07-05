import os
import subprocess
from py4j.java_gateway import JavaGateway, GatewayParameters, launch_gateway

BASE = os.path.dirname(os.path.abspath(__file__))

JAVA_SRC = os.path.join(BASE, "java", "src")
JAVA_OUT = os.path.join(BASE, "java", "out")
PY4J_JAR = os.path.join(BASE, "lib", "py4j.jar")

subprocess.run([
    "javac",
    "-d", JAVA_OUT,
    "-cp", PY4J_JAR,
    JAVA_SRC + "/*.java"
], shell=True)

port = launch_gateway(classpath=JAVA_OUT)

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=port))

main = gateway.jvm.Main()

'''
import Graphics.Graphics as Graphics
win = Graphics.Graphics()
print(win)

need to call main.update() to update the java side 
need to call win.update(main.getPositions()) to update the window
'''