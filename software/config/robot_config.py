# =========================================================
# CONFIGURATION
# =========================================================
SERIAL_PORT = "COM4"
BAUD_RATE = 115200
# BAUD_RATE = 9600
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
# Process face detection at a smaller resolution.
# This reduces CPU usage considerably.
DETECTION_SCALE = 0.5
OLLAMA_MODEL = "qwen3:0.6b"
TTS_VOICE = "en-US-AvaNeural"
TTS_RATE = "-24%"
TTS_VOLUME = "+0%"
TTS_PITCH = "+7Hz"
# Number of conversation messages kept.
MEMORY_LIMIT = 10

# =========================================================
# IMAGE PREPROCESSING
# =========================================================
ENABLE_BRIGHTNESS_CORRECTION = True
IMAGE_ALPHA = 1.25      # التباين
IMAGE_BETA = 25         # السطوع، القيمة التي اختبرتها

# =========================================================
# FACE DETECTION
# =========================================================
FACE_SCALE_FACTOR = 1.2
FACE_MIN_NEIGHBORS = 5
# Original-resolution minimum face size
# FACE_MIN_SIZE = (60, 60)
# FACE_MIN_SIZE = (50, 50)
FACE_MIN_SIZE = (40, 40)

# =========================================================
# FACE SMOOTHING
# =========================================================
# EMA_ALPHA = 0.30
EMA_ALPHA = 1.25

# =========================================================
# SERVO CONFIGURATION
# =========================================================
PAN_CENTER = 90
TILT_CENTER = 90

# PAN_MIN = 30 # 0
# PAN_MAX = 150 # 180
# TILT_MIN = 45 # 0
# TILT_MAX = 120 # 180
PAN_MIN = 50
PAN_MAX = 100
TILT_MIN = 65
TILT_MAX = 100
# Dead zones prevent tiny constant movements.
PAN_DEAD_ZONE = 25
TILT_DEAD_ZONE = 25
# Servo target response.
PAN_GAIN = 0.25
TILT_GAIN = 0.25
# Servo acceleration.
MAX_PAN_SPEED = 3.0
MAX_TILT_SPEED = 3.0
PAN_ACCELERATION = 2.0
TILT_ACCELERATION = 2.0

# =========================================================
# FACE LOST
# =========================================================
FACE_LOST_TIMEOUT = 5.0
# =========================================================
# OLED EYES
# =========================================================
EYE_X_LIMIT = 25
EYE_Y_LIMIT = 15
# =========================================================
# BLINKING
# =========================================================
BLINK_MIN_INTERVAL = 1.0
BLINK_MAX_INTERVAL = 3.7
BLINK_DURATION = 0.16
# =========================================================
# ATTENTION
# =========================================================
ATTENTION_THRESHOLD = 65
# How long the robot must see an attentive user
# before making an educational suggestion.
LEARNING_PROMPT_DELAY = 3.0
# =========================================================
# SMILE DETECTION
# =========================================================
ENABLE_SMILE_DETECTION = True
SMILE_SCALE_FACTOR = 1.25
SMILE_MIN_NEIGHBORS = 9
