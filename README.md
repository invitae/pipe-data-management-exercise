# Pipeline platform data management exercise

## Dependencies
The following dependencies are required to run this application.
- sqlite
- flask
- flask-sqlalchemy

## Get started with running and developing the app
With dependencies installed and/or your virtual environment activated, run `flask run`. You should see a line with the target URL like this

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Point your browser to that URL: http://127.0.0.1:5000/

## Explore the app
- How would you add data?
- How would you list data?

## Questions
- Data Retention
  - **Background**: This app manages pipeline data on our Network File System (NFS). Normally data is purged from disk when it is no longer useful. Usefulness is typically determined by age of the data. However, for training and R&D purposes, bioinformaticians may request certain data to be skipped from the purge process and stay on NFS longer. The current approach is to update a shared spreadsheet (CSV file) to track the data retention requests.
  - **Example CSV**:

    | Identifier | Owner (email)       | NFS Accessible Until | Explanation      |
    |------------|---------------------|----------------------|------------------|
    |       1234 | abc.def@invitae.com |           2021-01-01 | ClinGen training |
    |       5678 | ghi.jkl@invitae.com |           2222-01-01 | R&D              |
    |       9012 | mno.pqr@invitae.com |           2222-01-01 | ClinGen training |

  - **Problem**: Our team has been asked to improve the manual retention request process. What changes would you make to accomplish the same?
