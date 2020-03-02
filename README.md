# CSCE-482 Dianoga: Trash Handler

Our project, the Dianoga Trash Handler, is a system that will automatically classify 
trash based on recyclability and make sure it ends up in the correct bin. Our 
solution aims to address challenges caused by human error (i.e. throwing trash in 
the wrong bin). It will use a camera to take a picture of a piece of trash. The 
picture will be fed into a machine learning model that will classify the trash 
based on recyclability. In the final prototype, the system will have hardware 
peripherals that direct the trash into the correct bin, for example by opening 
the trash lid or by some other mechanism that physically puts the trash into the bin.


## Getting Started

These instructions will get you a copy of the project up and running on your local 
machine for development and testing purposes. See deployment for notes on how to 
deploy the project on a live system. 

Step 1: Build Docker image (while in the repo directory)

`docker build -t capstone:v0.1 .`

Step 2: Run the container (fill in the absolute path to your repo)

`docker run --name capstone -it -v "/path/to/repo/":"/CSCE-482/" capstone:v0.1`

Step 3: Activate the environment and run the test

`conda actiavte capstone` - you should see something like 
this `(capstone) root@01f1f79e0b32:/CSCE-482#`

Next `cd /CSCE-482/` and `python predict.py` to run

## Training on GPU Cluster

These instructions will get you a copy of the project up and running on A&M's 
High Performance Research Computing (HPRC) clusters for development and testing 
purposes. See deployment for notes on how to deploy the project on a live system. 

Step 1: Login to `<username>@terra.tamu.edu` and run the commands below to set up 
the environment

```
cd $SCRATCH
module load Anaconda/3-5.0.0.1
conda create -y --name capstone python=3.6
source activate capstone
```

Step 2: Install all the required packages
```
conda install -y -c conda-forge keras=2.2.4 opencv=4.2 && \
conda install -y -c anaconda tensorflow-gpu=1.4 cudnn=6.0.21 cudatoolkit=8.0 && \
conda install -y -c powerai imageai=2.1.5
```

*can check package installation with:\* 
`conda list | grep 'cuda\|tensorflow\|opencv\|keras\|imageai'`

Step 3: Pull the repo into your home directory
```
cd ~
git clone https://github.com/Ac65943/CSCE-482-Dianoga.git
git checkout beta
```

Step 4: Submit job to cluster (make sure to adjust the memory
`#SBATCH --mem=5120M` and wall clock limit `#SBATCH --time=03:00:00`
accordingly)

`sbatch Beta01GPU.slurm`

Can see information about job with: `squeue -u <netID>`

## Running the tests

TODO

## Deployment

TODO

## Built With

* [TBD](http://www.google.com) - TBD
* [TBD](http://www.google.com) - TBD
* [TBD](https://www.google.com) -TBD 

## Authors

* **Murtaza Hakimi** - *TBD* - [MRTZA](https://github.com/MRTZA)
* **Murtaza Hakimi** - *TBD* - [Ac65943](https://github.com/Ac65943)
* **Murtaza Hakimi** - *TBD* - [Unknown](https://github.com/)
* **Murtaza Hakimi** - *TBD* - [Unknown](https://github.com/)



