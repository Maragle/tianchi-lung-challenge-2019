TARGET_VOXEL_MM = [1.,1.,1.]
WINDOW_LUNG = (1500, -500) # WW, WL
WINDOW_MEDI = (350, 40) #WW, WL
BINARY_THRESHOLD_LUNG = 140 # <
BINARY_THRESHOLD_MEDI = 70 # >
BINARY_THRESHOLD_BONE = 254
PLOT_SLICES_NUM = 16

GENERATE_NEGS_PER_LUNG = 32
CUBE_SIZE = 64
CUBE_POS_SIZE = 64
CUBE_FPOS_SIZE = 64
CUBE_NEG_SIZE = 64

SEGMENT_INPUT_SHAPE = (512, 512)

THRESHOLD_VALID_CUBE = 255 * 10
NEG_RATE_BY_POS = 4
FPOS_RATE_BY_POS = 4
AUGMENTATION_RATE = 8
AUGMENTATION_MIN_OFFSET_LIMIT = 10

SLIDING_WINDOW_STEP = 16
THRESHOLD_PREDICT_NMS = 0.8

RAW_DIR = '/tf/tianchi2019/dataset/'
ANNOTATION_FILE = RAW_DIR + 'chestCT_round1_annotation.csv'
RAW_TRAIN_DIR = RAW_DIR + 'trainset/'
RAW_TEST_DIR = RAW_DIR + 'testset2/'
RAW_TEST2_DIR = RAW_DIR + 'testset2/'

PREPROCESS_DIR = '/tf/tianchi2019/preprocess/'
PREPROCESS_TRAIN_DIR = PREPROCESS_DIR + 'train/'
PREPROCESS_TEST_DIR = PREPROCESS_DIR + 'test2/'
PREPROCESS_TEST2_DIR = PREPROCESS_DIR + 'test2/'
PREPROCESS_POS_DIR = PREPROCESS_DIR + 'pos/'
PREPROCESS_FPOS_DIR = PREPROCESS_DIR + 'fpos/'
PREPROCESS_NEG_DIR = PREPROCESS_DIR + 'neg/'
PREPROCESS_SEG_DIR = PREPROCESS_DIR + 'seg/'
PREPROCESS_ANNOTATION_FILE = PREPROCESS_DIR + 'annotation.csv'
PREPROCESS_CANDIDATE_FILE = PREPROCESS_DIR + 'candidate.csv'
PREPROCESS_FALSE_POSITIVE_FILE = PREPROCESS_DIR + 'false_positive.csv'
PREPROCESS_FALSE_POSITIVE_LUNG_FILE = PREPROCESS_DIR + 'false_positive_lung_submission.csv'
PREPROCESS_FALSE_POSITIVE_MEDI_FILE = PREPROCESS_DIR + 'false_positive_medi_submission.csv'
PREPROCESS_ANNOTATION_AUG_FILE = PREPROCESS_DIR + 'annotation_aug.csv'
PREPROCESS_TRAIN_META_FILE = PREPROCESS_DIR + 'meta_train.csv'
PREPROCESS_TEST_META_FILE = PREPROCESS_DIR + 'meta_test2.csv'
PREPROCESS_TEST2_META_FILE = PREPROCESS_DIR + 'meta_test2.csv'

SUBMISSION_DIR = '/tf/tianchi2019/submission/'


