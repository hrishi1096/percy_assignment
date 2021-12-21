# Percy_assignment
Percy Technical Assignment


# Structure of the repo
This repo has a `develop` branch and a `staging` branch.

* `develop` branch has test for the Browserstack [production website](https://www.browserstack.com)
* `staging` branch has test for the Browserstack [non production website](https://k8s.bsstag.com)

# Running the tests on percy

```
git clone git@github.com:hrishi1096/percy_assignment.git
export PERCY_TOKEN = [your-percy-token]
git checkout staging
PERCY_BRANCH=staging PERCY_TARGET_BRANCH=develop npx percy exec -- pytest comparison.py
```

