# Workflow positionement sfeirien

## General
- Cdp: Grégory Lecygne
- affected: Andresse Njeungoue, 
- Dev: Andresse Njeungoue
- Specs: https://docs.google.com/document/d/1fp5Jyums9M2-WTMDTkeVRtREHPpQKQMbFGJ7K6RLbCA/edit?ts=5beaecd5

## GCP
- project: workflow positionement sfeirien
- scope: intern

# Qu'est ce que c'est (technos)

Application web AppEngine / Python 2.7 / Flask / Angular, React / APIs Google (Admin SDK)[Cloud storage]

# Qu'est ce que ça fait

cf specs dans le google doc's .

# Installation

```bash
./tasks/setup.sh <path to Gcloud appengine sdk>
```

# Execution

```bash
source venv/bin/activate
dev_appserver.py api.yaml dispatch.yaml
# ... then
deactivate
```

# Deploiement

```bash
./tasks/deploy.sh <dev|production|acceptance> <version>
```

