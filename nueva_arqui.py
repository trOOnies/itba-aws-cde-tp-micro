from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS, ECR
from diagrams.aws.devtools import Cloud9, Codecommit, Codedeploy, Codepipeline

with Diagram("Nueva Arquitectura", direction="TB", show=False):
    with Cluster("Desarrollo de arquitectura"):
        c9 = Cloud9("Entorno de Trabajo")

        with Cluster("customer"):
            ecr_cust = ECR("x:latest")
            cp_cust = Codepipeline("update-x-\nmicroservice")
            cd_cust = Codedeploy("microservices-x")
            ecs_cust = ECS("x-microservice")

        with Cluster("employee"):
            ecr_empl = ECR("x:latest")
            cp_empl = Codepipeline("update-x-\nmicroservice")
            cd_empl = Codedeploy("microservices-x")
            ecs_empl = ECS("x-microservice")

        cc_micros = Codecommit("microservices")
        cc_deploy = Codecommit("deployment")

    # Desarrollo
    c9 >> [cc_micros, cc_deploy]
    cc_deploy >> [cp_cust, cp_empl]

    c9 >> ecr_cust >> cp_cust >> cd_cust >> ecs_cust
    c9 >> ecr_empl >> cp_empl >> cd_empl >> ecs_empl

    # - (OK) AWS VPC
    # - (OK) AWS EC2: instancias, equilibrador de carga de aplicación, grupos de destino 
    # - (OK) AWS CodeCommit: repositorio 
    # - (OK) AWS CodeDeploy 
    # - (OK) AWS CodePipeline: canalización 
    # - (OK) AWS ECS: servicios, contenedores, tareas
    # - (OK) AWS ECR: repositorio. 
    # - (OK) Entorno de AWS Cloud9 
    # - (OK) AWS IAM: roles 
    # - (OK) AWS RDS
    # - (OK) AWS CloudWatch: registros 
