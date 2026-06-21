\# Alert Configuration



\## 1. Create Email Secret



Copy example file:



```powershell

copy email-secret.yaml.example email-secret.yaml

```



Edit the file and update:



\* smtp\_username

\* smtp\_password

\* smtp\_from



Example:



```yaml

smtp\_username: your-email@gmail.com

smtp\_password: your-gmail-app-password

smtp\_from: your-email@gmail.com

```



\---



\## 2. Apply Secret



```powershell

kubectl apply -f email-secret.yaml

```



Verify:



```powershell

kubectl get secret -n monitoring

```



\---



\## 3. Verify PrometheusRule



```powershell

kubectl get prometheusrule -n demo

```



Expected:



```text

api-slo-rules

```



\---



\## 4. Verify Alertmanager



```powershell

kubectl get pods -n monitoring

```



Expected:



```text

alertmanager-\*

```



\---



\## 5. Test Alert



Increase application error rate.



Example:



```yaml

ERROR\_RATE: "0.10"

```



Generate traffic and wait for Prometheus evaluation.



Expected:



```text

Success Rate < 95%

↓

Alert Fired

↓

Email Sent

```



\---



\## 6. Cleanup



Delete secret:



```powershell

kubectl delete -f email-secret.yaml

```



