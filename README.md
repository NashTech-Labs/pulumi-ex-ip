# pulumi using gcp-python

#### Reserving the static external ip using pulumi:


## Commands to apply the script:

1. Change the gcp project id in pulumi.dev.yaml

```
config:
  gcp:project: <gcp-project-id>
```

1. activate the virtual environment

```
$ source venv/bin/activate
```

2. Create or update the resources in a stack

```
$ pulumi up 
```
3. Destroy all existing resources in the stack

```
$ pulumi destroy
```
