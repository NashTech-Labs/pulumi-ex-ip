
import pulumi
import pulumi_gcp as gcp

ip_address = gcp.compute.Address("ng-ip",region="us-central1")