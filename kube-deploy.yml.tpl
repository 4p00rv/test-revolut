apiVersion: apps/v1
kind: Deployment
metadata:
  name: revolut
  labels:
    app: revolut

spec:
  replicas: 2
  selector:
    matchLabels:
      app: revolut
  template:
    metadata:
      labels:
        app: revolut
    spec:
      containers:
        - name: revolut-test
          image: 4p00rv/revolut-test:${TAG}
          imagePullPolicy: "Always"
          env:
            - name: DB_URI
              valueFrom:
                secretKeyRef:
                  name: database
                  key: DB_URI
          ports:
            - containerPort: 8080
          resources:
            limits:
              cpu: 100m
            requests:
              cpu: 100m
---
apiVersion: v1
kind: Service
metadata:
  name: revolut
spec:
  selector:
    app: revolut
  ports:
    - protocol: TCP
      port: 8080
      name: web
---
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: revolut
  namespace: default
spec:
  entryPoints:
    - web
    - websecure
  routes:
  - match: Host(`revolut`)
    kind: Rule
    services:
    - name: revolut
      port: 8080
