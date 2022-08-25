## 경로 설정
cd siamreppoints/tools

## pretrained된 파일로 eval
 python eval.py \
	--tracker_path /home/ubuntu/nozzi/RPT/tools/results/VOT2018/siamreppoints/baseline \
	--dataset /home/ubuntu/nozzi/RPT/testing_dataset/VOT2018 \
	--tracker__prefix 'siam' \
	--num 1
