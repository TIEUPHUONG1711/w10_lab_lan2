\# W10 GitOps Canary Demo



\## Overview



Demo project gồm:



\* Flask API

\* ArgoCD GitOps

\* Argo Rollouts Canary Deployment

\* Prometheus Monitoring

\* Alertmanager Email Alerting

\* SLO Validation



\---



\## Components



\### Application



```text

src/api

```



Flask API.



\### Deployment



```text

app-api

```



\* Rollout

\* Service

\* ServiceMonitor



\### Analysis



```text

app-analysis

```



\* AnalysisTemplate



\### Alert



```text

app-alert

```



\* PrometheusRule

\* Email Secret Example



\### Common



```text

app-common

```



\* Namespace



\---



\## Quick Start



\### Install ArgoCD



```bash

kubectl create namespace argocd

```



Install ArgoCD manifests.



\---



\### Deploy Root App



```bash

kubectl apply -f argocd/root.yaml

```



\---



\## Verify Deployment



Check Applications:



```bash

kubectl get applications -n argocd

```



Check Rollout:



```bash

kubectl get rollout -n demo

```



Check Pods:



```bash

kubectl get pods -n demo

```



\---



\## Setup Email Alert



Copy example:



```bash

cp app-alert/email-secret.yaml.example app-alert/email-secret.yaml

```



Update Gmail credentials.



Apply:



```bash

kubectl apply -f app-alert/email-secret.yaml

```



\---



\## Test Scenarios



\### Test 1 — Successful Deployment



Set:



```yaml

ERROR\_RATE: "0"

```



Expected:



```text

Analysis Success

Rollout Complete

```



\---



\### Test 2 — Canary Rollback



Set:



```yaml

ERROR\_RATE: "0.15"

```



Expected:



```text

Analysis Fail

Rollback

```



\---



\### Test 3 — SLO Alert



Set:



```yaml

ERROR\_RATE: "0.10"

```



Expected:



```text

Success Rate < 95%

Alert Fired

Email Sent

```



\---



\## Sync Waves



```text

Wave -1

app-common



Wave 0

k8s-prometheus

k8s-rollout



Wave 1

app-analysis

app-alert



Wave 2

app-api

```



\---



\## Cleanup



Delete root application:



```bash

kubectl delete -f argocd/root.yaml

```



Delete namespaces:



```bash

kubectl delete ns demo

kubectl delete ns monitoring

kubectl delete ns argo-rollouts

```



