from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
)
from constructs import Construct


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        name = "Aspen"
        key = "default"

        # The code that defines your stack goes here

        vpc = ec2.Vpc(self, "{}_VPC".format(name),
                      cidr="10.0.0.0/16",
                      subnet_configuration=[ec2.SubnetConfiguration(
                          subnet_type=ec2.SubnetType.PUBLIC,
                          name="Ingress",
                          cidr_mask=24
                      )]
                      )

        security_group = ec2.SecurityGroup(self, "{}_SG".format(name), vpc=vpc)

        # my_security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "allow ssh access from the world")
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            'allow ssh from anywhere'
        )

        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            'allow http from anywhere'
        )

        instance_type = ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO)

        ami = "ami-0ee8244746ec5d6d4"

        machine_image = ec2.MachineImage.generic_linux({
            "us-west-2": ami
        })

        ec2.Instance(self, "{}_Instance".format(name),
                     vpc=vpc,
                     security_group=security_group,
                     instance_type=instance_type,
                     machine_image=machine_image,
                     block_devices=[ec2.BlockDevice(
                         device_name="/dev/sda1",
                         volume=ec2.BlockDeviceVolume.ebs(8)
                     )],
                     keyName=key
                     )

