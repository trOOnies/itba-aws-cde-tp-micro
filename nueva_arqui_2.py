from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.general import User, Users
from diagrams.aws.network import ElbApplicationLoadBalancer, InternetGateway

with Diagram("Nueva Arquitectura 2", show=False):
    customers = Users("Clientes")
    employee = User("Empleado")

    with Cluster("AWS Productivo"):
        igw = InternetGateway("Internet\nGateway")
        alb = ElbApplicationLoadBalancer("microservicesLB")

        with Cluster("Capa de Aplicación"):
            ecs_cust = ECS("customer-\nmicroservice")
            ecs_empl = ECS("employee-\nmicroservice")

        rds = RDS("supplierdb")

    # Server
    [customers, employee] >> igw >> alb
    igw >> alb
    alb >> [ecs_cust, ecs_empl] >> rds

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
