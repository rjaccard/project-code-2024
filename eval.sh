#!/bin/bash -l
#SBATCH --chdir /scratch/izar/<put-your-username-here>
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 1
#SBATCH --mem 4G
#SBATCH --time 2:00
#SBATCH --gres gpu:1
#SBATCH --account cs-552
#SBATCH --qos cs-552

echo "hello from $(rjaccard)"
sleep 2
echo "hello from $(rjaccard)"

