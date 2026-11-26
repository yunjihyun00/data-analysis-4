import csv  # csv 읽는 거
import os
import numpy as np


def dp(name):
    """
    실행 위치가 어디든 data 폴더를 찾아 주는 작은 도우미 함수
    """
    here = os.path.dirname(os.path.abspath(__file__))
    for c in (
        os.path.join("data", name),
        os.path.join(here, "data", name),
        os.path.join(here, "..", "data", name),
    ):

        if os.path.exists(c):
            return c
        return os.path.join("data", name)


MCT = dp("10_mct_tool.csv")  # 40행 6열 오늘 쓰는 유일한 데이터 파일

# ===============================================
# 0. 리스트로는 왜 안 되나 - 곱셈이 곱셈이 아닌 장면
# ===============================================
#
# 상황) 온도 네 개를 재 뒀습니다. 전부 두배로 만들고 싶어요.
print("=" * 60)
print("[0] 리스트로 묶음 계산을 해 보면")
temps = [30, 30, 31, 29]
temps2 = [5, 6, 7, 8]
doubled = []
for t in temps:
    doubled.append(t * 2)
print(doubled)
print(temps * 2)

# 같은 일을 배열로 해 봅니다.
print("[0-1] 같은 일을 배열로")  # 배열로 만들면 , coma가 없어짐.
arr = np.array(temps)
arr2 = np.array(temps2)
print("배열:", arr)
print("arr * 2:", arr * 2)
print("arr + 5:", arr + 5)
print("화씨로 바꾸기:", arr * 1.8 + 32)
print("배열 곱 가능 ? :", arr * arr2)  # 배열끼리 곱하려면 배열의 길이가 같아야 한다.

# 그럼 for 로 하면 되는데 왜 Numpy 를 쓰나?
# for 로 한 줄이 아니라 세 줄이 들었습니다 (빈 리스트 만들기 / for / append).
# 지금은 값이 네 개라 세 줄이면 되는데, 40개여도 세 줄이고 400만 개여도 세 줄입니다.
# 줄 수가 문제가 아닙니다. 문제는 두 가지입니다.
# 1) 하고 싶은 일(두 배로)이 코드에 안 보입니다. 상 차리는 코드에 묻힙니다.
# 2) 느립니다. 400만 개를 파이선 for 로 돌리는 것과 Numpy 로 하는 것은
#    속도가 수십 배 차이 납니다. - 오늘 측정하지 않았습니다.
#    다음에 실제로 시간을 재 봅니다. 오늘은 "느리다" 까지만.

# ==========================================================
# 1. 리스트와 배열은 무엇이 다른가 - 자료형이 하나로 통일됩니다.
# ==========================================================
# 배열(array) = 같은 자료형의 숫자를 줄줄이 담아 두고,
# 묶음 전체에 계산을 한 번에 걸 수 있게 만든 그릇.
# 정식 이름은 ndarray입니다. (n차원 배열).
# 화면에 type()을 찍으면 ndarray 라고 나오는 게 그래서입니다.
#
# 비유: 반 아이들을 일으켜 세운다고 해 봅시다. for 문은 출석부를 펴고
# "김철수 일어서", "이영희 일어서..."를 40번 부르는 것이고
# 벡터화는 "다 같이 일어서" 한 번 외치는 것입니다.
# 걸리는 시간이 다릅니다. 사람이 40명이든 400명이든 400만명이든 외치는 건 한 번이죠.
#
# 벡터화: for 문으로 하나씩 돌지 않고
# 묶음 전체에 한 번에 계산을 거는 방식. arr * 2 가 벡터화입니다.
# "벡터" 라는 말에 겁먹을 필요 없습니다. 여기서는 "줄줄이 늘어선 숫자 묶음"
# 이라는 뜻이고, 수학 수업의 화살표 벡터를 떠올리지 않아도 됩니다.
print("=" * 60)
print("[1] 리스트와 배열은 무엇이 다른가")
print("type(temps): ", type(temps).__name__)
print("type(arr): ", type(arr).__name__)
print("arr.dtype: ", arr.dtype)

# 결정적인 차이 하나 - 리스트는 아무거나 섞어 담고, 배열은 못 담습니다.
box = [1, 2.5, "삼십"]
print("리스트에 섞어 담기:", box, "/ 값의 자료형:", [type(v).__name__ for v in box])

mixed = np.array([1, 2, 3.5])
print("배열에 정수와 소수를 섞으면: ", mixed, "/ dtype", mixed.dtype)

# 초보자가 가장 많이 내는 오류 - 대괄호를 빼먹는 것
# np.array(1,2,3)

# dtype(data type) = 그 배열이 담고 있는 자료형.
# int64 = 정수, float64 = 소수.


# ========================================
# 2. 규칙적인 배열 - 손으로 적지 않고 만들기
# ========================================
# 배열을 만들 때마다 값을 손으로 적을 수는 없습니다.
# 0부터 39까지 측정 순번을 만들려고 숫자 40개를 치지는 않잖아요.
# 그래서 규칙적인 배열을 만들어 주는 함수가 다섯 개 있습니다.
#
# np.arange(시작, 끝, 간격) -> 간격을 정합니다. 끝값은 안 들어갑니다.
# np.linspace(시작, 끝, 개수) -> 개수를 정합니다. 끝값이 들어갑니다.
# np.zeros(개수) -> 전부 0
# np.ones(개수) -> 전부 1
# np.full(개수, 값) -> 전부 그 값
#
# * 두 개만 기억하면 됩니다 - arange는 간격, linspace는 개수.
print("=" * 60)
print("[2] 규칙적인 배열을 한 줄로 만들기")
print("    np.arange(5)           :", np.arange(5))
print("    np.arange(0, 10, 2)    :", np.arange(0, 10, 2))
print("    np.arange(0, 1, 0.3)   :", np.arange(0, 1, 0.3))
print("    np.linspace(0, 1, 5)   :", np.linspace(0, 1, 5))
print("    np.linspace(0, 100, 5) :", np.linspace(0, 100, 5))
print("    np.zeros(3)            :", np.zeros(3))
print("    np.ones(3)             :", np.ones(3))
print("    np.full(3, 7)          :", np.full(3, 7))

# 끝 값이 들어가느냐 안 들어가느냐.
print()
print("[2-1] 끝값이 포함되나")
print("    np.arange(0, 12, 3)   :", np.arange(0, 12, 3), "<- 12 가 없습니다")
print("    np.linspace(0, 12, 5) :", np.linspace(0, 12, 5), "<- 12 가 있습니다")
print("    개수:", len(np.arange(0, 12, 3)), "개 /", len(np.linspace(0, 12, 5)), "개")
print("    dtype:", np.arange(0, 12, 3).dtype, "/", np.linspace(0, 12, 5).dtype)

# 언제 쓰나 (실무에서 자주 쓰는 순서대로)
# arange 측정, 순번, 줄 번호    오늘 씁니다.
# zeros 결과를 담을 빈 그릇을 미리 만들 때 (크기를 알고 있을 때)
# linspace: 그래프의 가로축을 매끄럽게 만들 때. (시각화 하면서 들어감)
# ones, full: 1로 채워 두고 곱해 갈 때 -> "아직 안 됐음"을 -1로 표시해 둘 때


# ==============================================
# 3. dtype - 배열 하나에는 한 가지 자료형만 (함정 1)
# ==============================================
# 1번에서 "배열은 자료형을 하나로 통일한다"고 했습니다.
# 그 성질이 조용한 사고를 하나 만듭니다. 지금 그걸 밟아 봅시다.
#
# 비유: 눈금이 1cm 단위뿐인 줄자를 떠올려 보세요.
# 2.7cm를 재면 그 자에는 2.7을 적을 자리가 없습니다. 2 라고 적게 되죠.
# 0.7이 없어진 게 아니라, 자가 그 사이를 적을 수 없는 겁니다.
# 정수 배열이 그 자입니다. 칸마다 정수만 적을 수 있어요.
# 깨지는 지점 - 사람이 그 자로 재면 보통 가까운 눈금, 즉 3으로 읽습니다.
# 그런데 파이썬은 가까운 쪽으로 안 갑니다. 소수점 아래를 그냥 떼어 2로 적어요.
# 그 차이가 4번에서 다루는 '버림과 반올림' 입니다. 지금은 "떼어 낸다" 까지만

print("=" * 60)
print("[3] 배열 하나에는 한 가지 자료형만 들어갑니다")
ints = np.array([1, 2, 3])
print("    ints        :", ints, "/ dtype", ints.dtype)
ints[0] = 2.7  # 정수 배열의 첫 칸에 소수를 넣어 봅니다
print("    ints[0] = 2.7 한 뒤:", ints, "<- 2.7 이 2 가 됐습니다")
print("    ints.dtype  :", ints.dtype, "<- 정수 배열은 끝까지 정수입니다")

flo = np.array([1.0, 2.0, 3.0])  # 같은 일을 실수 배열에 해 봅니다
flo[0] = 2.7
print("    실수 배열에 같은 일:", flo, "<- 이쪽은 2.7 이 그대로 들어갑니다")

print()
print("[3-1] 나눗셈은 자료형을 바꿉니다")
odd = np.array([7, 8])
print("    np.array([7, 8])     :", odd, "/ dtype", odd.dtype)
print("    np.array([7, 8]) / 2 :", odd / 2, "/ dtype", (odd / 2).dtype)

# =========================================================
# 4. astpe - 자료형 바꾸기. 반올림이 아니라 버림입니다. (함정2)
# =========================================================
# 3번은 '모르고 꺾인' 경우였습니다. 이번엔 일부러 바꿉니다.
# 쓰는 함수는 astype이고, 함정이 똑같은 모양으로 또 나옵니다.
print("=" * 60)
print("[4] astype - 자료형을 바꾼 새 배열을 받습니다")
raw = np.array([1.7, -1.7, 2.3, 3.9])
print("    원본          :", raw, "/ dtype", raw.dtype)
print("    astype(int)   :", raw.astype(int), "<- 1.7 이 2 가 아니라 1 입니다")
print("    np.round      :", np.round(raw), "<- 반올림은 이쪽")
print("    np.floor      :", np.floor(raw), "<- 내림은 또 다릅니다. -1.7 을 보세요")
print("    원본은 그대로 :", raw, "<- astype 은 원본을 바꾸지 않습니다")

# 비유: 온도계로 생각하면 셋이 갈립니다. 영하 1.7도를 정수로 적어야 한다면
# 버림은 0쪽으로 당겨서 -1 로 적습니다. 소수점 아래를 떼기만 하니까.
# 반올림은 가까운 쪽으로 가서 -2 로 적습니다. -1.7은 -2에 더 가깝죠.
# 내림은 늘 더 추운 쪽으로 가서 -2 로 적습니다. 항상 아래쪽이니까요.
# 깨지는 지점 - 영상 1.7도에서는 버림도 1, 내림도 1 입니다. 같아 보여요.
# 0 보다 작아질 때만 갈립니다. 그래서 양수만 보고 "같은 거네" 하면 틀립니다.
#
# 버림(astype) 소수점 아래를 그냥 떼기.
# 반올림(round) 가까운 정수로.
# 내림(floor) 작은 쪽 정수로.


# ===================================================
# 5. 배열에게 물어보는 네 가지 - shape ndim size dtype
# ===================================================
# 데이터를 받으면 가장 먼저 하는 일이 "이게 몇 줄 몇 칸인가"입니다.
# 01 단원에서 len(rows) 와 len(header)로 센 걸 기억 하실겁니다.
# NumPy 는 그걸 배열에게 직접 물어봅니다. 네 가지
#
# shape = 배열의 모양. (행 수, 열 수) 꼴의 묶음으로 나옵니다.
# *** (행, 열) *** 이렇게 들어 온다 무조건
# ndim = 차원 수, 한 줄로 늘어선 배열은 1, 표 모양은 2 입니다.
# size = 값이 모두 몇 개인가, shape의 숫자들을 곱한 값입니다.
# attribute = 함수가 아니라 "이미 가지고 있는 정보"


print("=" * 60)
print("[5] 배열에게 물어보는 네 가지")
table = np.array(
    [[30, 15.44, 4603], [30, 18.69, 4603]]
)  # 데이터 파일 앞 두 줄에서 세 칸만 떼 온 것입니다
print("    table")
print(table)
print("    table.shape :", table.shape, "<- (행, 열)")
print("    table.ndim  :", table.ndim, "<- 몇 차원인가")
print("    table.size  :", table.size, "<- 값이 모두 몇 개인가")
print("    table.dtype :", table.dtype, "<- 어떤 자료형인가")
print(
    "    검산:",
    table.shape[0],
    "x",
    table.shape[1],
    "=",
    table.shape[0] * table.shape[1],
)

print()
print("[5-1] 괄호를 붙이면")
try:
    table.shape()  # 속성에 괄호를 붙이면 터집니다
except TypeError as e:
    print("    table.shape() :", type(e).__name__, "-", e)


# =====================================================================
# 6. 모양 바꾸기 - reshape · flatten (값은 그대로, 모양만)
# =====================================================================
# 같은 12개 숫자를 한 줄로 늘어놓을 수도 있고, 3줄 4칸 표로 접을 수도 있습니다.
# 값은 그대로고 보는 모양만 바뀝니다. 그게 reshape입니다.
print("=" * 60)
print("[6] 모양 바꾸기 - 값은 그대로, 모양만")
seq = np.arange(12)
print("    seq                  :", seq)
print("    seq.reshape(3, 4)")
print(seq.reshape(3, 4))
print(
    "    seq.reshape(-1, 2).shape :", seq.reshape(-1, 2).shape, "<- -1 은 '알아서 계산'"
)
print("    reshape(3, 4).flatten()  :", seq.reshape(3, 4).flatten())
print("    원본 seq             :", seq, "<- reshape 도 원본을 바꾸지 않습니다")

print()
print("[6-1] 개수가 안 맞으면")
try:
    seq.reshape(5, 3)  # 12개를 15칸에 넣으라는 말이 됩니다
except ValueError as e:
    print("    seq.reshape(5, 3) :", type(e).__name__, "-", e)
print("    12 는 3x4, 2x6, 1x12 로는 접히고 5x3 = 15 로는 안 접힙니다")


# ==============================
# CSV 파일을 배열로 읽기 - 그리고 e+07 이 뭔가?
# ============================================
# delimiter 딜리미터 -> 칸을 나누는 글자, CSV는 쉼표
# skiprows -> 맨 위 몇 줄을 건너뛸까. 1 = 열 이름 줄을 건너뜀
# encoding = 글자를 어떤 규칙으로 읽을까?


print("=" * 60)
print("[7] CSV 파일을 배열로 읽기")
full = np.loadtxt(MCT, delimiter=",", skiprows=1, encoding="utf-8-sig")
print("    shape:", full.shape, "/ dtype:", full.dtype)
print("    앞 2줄")
print(full[:2])

# 위 결과가 눈에 안 들어옵니다. 보기 설정을 한 줄 바꿉니다.
print()
print("[7-1] 같은 배열인데 보기가 달라집니다")
np.set_printoptions(suppress=True)  # 지수 표기를 끄는 설정. 값은 안 바뀝니다
print(full[:2])

print()
print("[7-2] 열 이름은 따로 읽습니다")
with open(MCT, encoding="utf-8-sig") as f:
    head = next(csv.reader(f))  # 첫 줄만 꺼냅니다. 8단원에서 한 그 방법
print("    열 이름:", head)
print(
    "    공구번호 종류:",
    np.unique(full[:, 0]),
    "->",
    len(np.unique(full[:, 0])),
    "가지",
)

mct = np.loadtxt(
    MCT, delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5), encoding="utf-8-sig"
)
cols = head[1:]  # 열 이름도 공구번호를 뺀 5개로 맞춥니다
print("    공구번호를 뺀 배열:", mct.shape, "/ 열 이름", cols)
print("    앞 3줄")
print(mct[:3])

# 빈 칸이 있는 파일은 loadtxt 로 못 읽습니다. 지금 확인해 둡니다.
print()
print("[7-3] 빈 칸이 섞여 있으면")
sample = ["1,2,3", "4,,6"]  # 파일 대신 글자 두 줄로 흉내를 냅니다
# ★ 위 sample 이 파일 이름이 아니라 글자 두 줄인 게 눈에 걸리실 겁니다.
#   loadtxt 는 파일을 받으면 한 줄씩 꺼내 읽습니다. 그래서 '한 줄씩 꺼낼 수 있는 것'
#   이면 파일이 아니어도 받아 줍니다. 리스트도 한 줄씩 꺼낼 수 있으니 되는 거예요.
#   빈 칸이 있는 CSV 를 따로 만들지 않으려고 두 줄로 대신한 겁니다.
#   "4,,6" 의 쉼표 두 개가 붙어 있는 데를 보세요. 그 사이가 빈 칸입니다.
try:
    np.loadtxt(sample, delimiter=",")
except ValueError as e:
    print("    loadtxt    :", type(e).__name__, "-", e)
print("    genfromtxt :")
print(np.genfromtxt(sample, delimiter=","))

print("=" * 60)
# ===================================
# 실습1 - 전류 40개를 배열로 다루기
# ===================================
# [문제]
# 0번 ~ 7번에서 배운 것만 씁니다. 통계는 아직 안 씁니다.
#
# 1 - np.arange 로 측정 순번 0~39를 만드세요. 앞 5개와 뒤 3개, shape, dtype을 찍으세요.
a = np.arange(0, 40)
print(a[:5], a[-3:], a.shape, a.dtype)

# 2 - 10_mct_tool.csv에서 전류 열 (3번 열)만 배열로 읽어 앞 5개를 찍으세요.
b = np.loadtxt(MCT, delimiter=",", skiprows=1, usecols=3, encoding="utf-8-sig")
print(b[:5])

# 3 - 그 배열의 shape, ndim, size, dtype을 한 줄에 찍으세요.
print(b.shape, b.ndim, b.size, b.dtype)

# 4 - 전류 40개를 8줄 5칸으로 접고, flatten 해서 원본과 같은지 확인하세요.
c = np.arange(40)
print(c.reshape(8, 5).flatten())

# 5 - 7줄 6칸으로 접어 보고 어떤 오류가 나는지 확인하세요.
