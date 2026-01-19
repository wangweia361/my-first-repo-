import os
import logging
from flask import Flask
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 创建Flask应用实例
app = Flask(__name__)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 从环境变量读取配置
DEBUG_MODE = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes')
PORT = int(os.getenv('FLASK_RUN_PORT', '5000'))
HOST = os.getenv('FLASK_RUN_HOST', '0.0.0.0')

@app.route('/')
def hello_world():
    logger.info('访问了首页')
    return 'Hello from cto.new!'

@app.errorhandler(404)
def page_not_found(e):
    logger.warning(f'404错误: {e}')
    return '页面未找到 (404)', 404

@app.errorhandler(500)
def internal_server_error(e):
    logger.error(f'500错误: {e}')
    return '服务器内部错误 (500)', 500

if __name__ == '__main__':
    logger.info(f'启动Flask应用 - Host: {HOST}, Port: {PORT}, Debug: {DEBUG_MODE}')
    app.run(host=HOST, port=PORT, debug=DEBUG_MODE)
