# SWE-bench-COMPSCI685
Repo for COMPSCI685 final project
Fine-tuning:

We have fine-tuned Gemma 2B and Gemma 7B on the [Spider](https://huggingface.co/datasets/xlangai/spider). 

To run the fine-tuning pipeline for Gemma 7B, follow along with the Spider_Gemma7b_Finetuning.ipynb notebook. 
To run the fine-tuning pipeline for Gemma 2B, follow along with the Spider_Gemma2b_Finetuning.ipynb notebook. 

* We used T4 GPU to Fine-tune both the models
* The data was loaded from Hugging Face and the models were loaded from Unsloth
* Our fine-tuned model can be accessed here:
  * [Gemma 2B](https://drive.google.com/drive/folders/1wxKIJZj61mgEf3IDu8bFtAall_ThC2Gb?usp=drive_link)
  * [Gemma7B](https://drive.google.com/drive/folders/13uOIU47VG6GX17Nybba2UV7t4URdnbd4?usp=drive_link)
 
Inference:

Batch Inferencing can be performed on Gemma 2B, 7B. Model loading codes for both the fine-tuned models and the baseline models are provided. To use the fine-tuned models, access and copy the checkpoint folders referenced above. Before running the notebook, comment out the models that are not being used and set valid output paths to continue with inference. 

Outputs:

Output csv files for both fine-tuned Gemma as well as SWE-Llama are present in `Outputs` directory.


 
  
