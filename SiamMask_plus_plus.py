## 환경 및 경로 설정
conda activate siammask_pp
cd smpp
export smpp=$PWD
export cd=$PWD
export PYTHONPATH=$PWD:$PYTHONPATH
cd experiments/simmask_sharp


## Test&Evaluation code
# 20개를 모두 평가하고 싶을때
bash test_all.sh -s 1 -e 20 -d VOT2022 -g 2

# 체크포인트 12를 평가하고 싶을때
bash test_all.sh -s 1 -e 1 -d VOT2022 -g 2
bash testrpn_all.sh -s 1 -e 12 -d VOT2022 -g 2

# 중요! (단 simmask_sharp/test/VOT2019 파일에서 이미 테스트한 파일들이 있을수도 있으므로 파일 이름을 바꾸고 돌리기)
