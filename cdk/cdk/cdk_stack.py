import decouple
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
)
from constructs import Construct
from decouple import config

"""
This class is for provisioning an ec2 instance using cdk for use with the aspen apps and nginx reverse proxy 
"""
class CdkStack(Stack):
    """
    Initial constructor for the CdkStack class which inherits from the base cdk class
    return: None
    """
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # name to prepend to resource names and tags
        name = "Aspen"
        # name of the ssh key pair on aws to use with the instance, if env variable empty then none will be used
        key_name = config('KEY')
        # region to deploy instance, if env variable empty then us-west-2 will be used
        region = config('REGION') if config('REGION') != "" else "us-west-2"
        # ip4 to use on ingress rules, if env variable empty the all hosts will be allowed
        ip = config('IP4') if config('IP4') != "" else "0.0.0.0/0"
        # use the Ubuntu 20.04 ami for the ec2 instance
        ami = "ami-0ee8244746ec5d6d4"

        # use the previously defined ami and region for the ec2 instance
        machine_image = ec2.MachineImage.generic_linux({
            region: ami
        })

        # use the t2.micro instance type
        instance_type = ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO)

        # set up the vpc to use for the ec2 instance with public subnets
        vpc = ec2.Vpc(self, "{}_VPC".format(name),
                      cidr="10.0.0.0/16",
                      subnet_configuration=[ec2.SubnetConfiguration(
                          subnet_type=ec2.SubnetType.PUBLIC,
                          name="Ingress",
                          cidr_mask=24
                      )]
                      )

        # create the security group
        security_group = ec2.SecurityGroup(self, "{}_SG".format(name), vpc=vpc)

        # add a security group rule for ssh if the ssh keypair name was defined on the previously defined ip
        if key_name != "":
            security_group.add_ingress_rule(
                ec2.Peer.ipv4(ip),
                ec2.Port.tcp(22),
                'allow ssh from {}'.format(ip)
            )

        # add a security group rule for http on the previously defined ip
        security_group.add_ingress_rule(
            ec2.Peer.ipv4(ip),
            ec2.Port.tcp(80),
            'allow http from {}'.format(ip)
        )

        # add a security group rule for https on the previously defined ip
        security_group.add_ingress_rule(
            ec2.Peer.ipv4(ip),
            ec2.Port.tcp(443),
            'allow https from {}'.format(ip)
        )

        # provision the instance using the previously set parameters
        instance = ec2.Instance(self, "{}_Instance".format(name),
                     vpc=vpc,
                     vpc_subnets=ec2.SubnetSelection(
                         subnet_type=ec2.SubnetType.PUBLIC
                     ),
                     security_group=security_group,
                     instance_type=instance_type,
                     machine_image=machine_image,
                     block_devices=[ec2.BlockDevice(
                         device_name="/dev/sda1",
                         volume=ec2.BlockDeviceVolume.ebs(8)
                     )],
                     key_name=key_name,
                     )

        # import the user-data script and add it to the instance to run at startup
        file_path = "./cdk/user-data.sh"
        with open(file_path) as f:
            user_data = f.read()

        instance.add_user_data(user_data)