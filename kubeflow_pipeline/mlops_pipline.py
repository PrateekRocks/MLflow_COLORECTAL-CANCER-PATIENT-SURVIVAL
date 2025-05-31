import kfp
from kfp import dsl
import kfp.compiler


def  data_processing_op():
    return dsl.ContainerOp(
        name = "Model Training",
        image = "image name",
        command = ["python" , "src/data_training.py"]
    )
    
    

def  model_processing_op():
    return dsl.ContainerOp(
        name = "Model Training",
        image = "image name",
        command = ["python" , "src/model_training.py"]
    )
    

  
## Pipline starts here..

@dsl.pipeline(
    name = "MLOPS Pipeline",
    description= "This is my first ever kubefow pipline"
    )

def mlops_pipeline():
    data_processing =data_processing_op()
    model_traning = model_processing_op().after(data_processing)
    
    
## RUN

if __name__=="__main__":
    kfp.compiler.Compiler().compile(
        mlops_pipeline,"mlop_pipline.yaml  "
    )
    
    
    
    