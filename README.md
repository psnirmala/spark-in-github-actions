# Run Spark in Github Actions

This repository provides an example of running Apache Spark in GitHub Actions for testing purposes.

To run Spark in GitHub Actions, we have provided a workflow file named [`spark-submit.yaml`] in the `.github/workflows/` directory. This workflow file defines the steps that GitHub Actions should take to run a PySpark script using the `spark-submit` command.

The [`spark-submit.yaml`] file also specifies the matrix strategy to test the PySpark script on multiple versions of Python and Spark. In this example, the PySpark script will be tested on:

- Python 3.10, Spark 3.3.2.
- Python 3.10, Spark 3.4.0.
- Python 3.11, Spark 3.3.2.
- Python 3.11, Spark 3.4.0.

**See the Github Actions runs: <https://github.com/duyet/spark-in-github-actions/actions>**

[`spark-submit.yaml`]: .github/workflows/spark-submit.yaml
