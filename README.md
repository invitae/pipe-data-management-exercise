# Pipeline platform data management exercise

## Install requirements
There is no installment needed for this app. You only need to install the following dependencies.
- sqlite
- flask
- flask-sqlalchemy

## Get started with running and developing the app
With dependencies install and/or your virtual environment activated, run `flask run`. You should see a line with the target URL like this

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

So point your browser to that URL: http://127.0.0.1:5000/

## Explore the app
- How would you add data?
- How would you list data?

## Questions
- Pin data on NFS to avoid scheduled data purge
  - **Backgroud**: this app manages pipeline data on our Network File System (NFS). Normally data all have their lifecycle and will be purged from the disk when they age. However, for various purpopse such as training, R&D, bioinformatician may request certain data to skip purge and stay on NFS longer, which we can _"Pin"_. We got communications from them and keep these info on a Google sheet. This process is currently manual.
  - **Problem**: how can we improve the pin process and potentially automate pin info communication and storage.
