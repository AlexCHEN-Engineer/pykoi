"""
accelerate config

LOCAL_DIR=/home/ubuntu/pykoi/pykoi # change this to your local path

export PYTHONPATH=$PYTHONPATH:${LOCAL_DIR}

accelerate launch --num_machines 1  --num_processes 1 --mixed_precision fp16 ${LOCAL_DIR}/example/rlhf/demo_rl.py
"""
# accelerate launch --num_machines 1  --num_processes 1 --mixed_precision fp16 example/rlhf/demo_rl.py

import pykoi

# use huggingface sft and reward model
config = pykoi.RLHFConfig(
    base_model_path="models/rlhf_step1_sft",    #"elinas/llama-7b-hf-transformers-4.29", 
    dataset_type="huggingface", 
    dataset_name="goldmermaid/stack_exchange_rank_10k_dataset",
    dataset_subset_rl="data",
    reward_model_path="models/rlhf_step2_rw/", #"cambioml/rlhf_reward_model",
    save_freq=1,
    ppo_batch_size=32,
    ppo_epochs=4,
    total_epochs=5,
    output_dir="./models/rlhf_step3_rl",
)

rlhf_step3_rl = pykoi.RLFinetuning(config)
rlhf_step3_rl.train_and_save("./models/rlhf_step3_rl")
