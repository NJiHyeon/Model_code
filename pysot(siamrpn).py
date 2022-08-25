## 환경 및 경로 설정
conda activate pysot
cd py
export cd=$PWD
export PYTHONPATH=$PWD:$PYTHONPATH
cd experiments/siamrpn_r50_l234_dwxcorr_8gpu


## Training code
# 먼저 nvidia-smi로 GPU 학습이 가능한지 확인
nvidia-smi
# 훈련중이라면 필요없는거 kill
kill -9 PID
CUDA_VISIBLE_DEVICES=0,1,2
python -m torch.distributed.launch \
    --nproc_per_node=8 \
    --master_port=2333 \
    ../../tools/train.py --cfg config.yaml


## Training code
# 아직까지 체크포인트 11~20번까지 모두 훈련되지 않았기 때문에 일단 11번만 테스트
# (원래코드)
START=10
END=20
seq $START 1 $END | \
    xargs -I {} echo "snapshot/checkpoint_e{}.pth" | \
    xargs -I {} \ 
    python -u ../../tools/test.py \
        --snapshot {} \
	--config config.yaml \
	--dataset VOT2018 2>&1 | tee logs/test_dataset.log

# (체크포인트 11번만 테스트하는 코드)
python -u ../../tools/test.py \
        --snapshot snapshot/checkpoint_e11.pth \
	--config config.yaml \
	--dataset VOT2018 2>&1 | tee logs/test_dataset.log


## Evaluation code
python ../../tools/eval.py 	 \
	--tracker_path ./results \ # result path
	--dataset VOT2018        \ # dataset name
	--num 4 		 \ # number thread to eval
	--tracker_prefix 'ch*'   # tracker_name
