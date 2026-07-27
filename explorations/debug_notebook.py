# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %sql
# MAGIC select * from databrickslearning.realtime.bronze_ride_events

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from databrickslearning.realtime.silver_ride_events

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from databrickslearning.realtime.gold_cacellation_analysis
