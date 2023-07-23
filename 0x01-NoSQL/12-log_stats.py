#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

if __name__ == "__main__":
    db = MongoClient()
    logs_collection = db.logs.nginx

    print("{} logs".format(logs_collection.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}"
              .format(method,
                      logs_collection.count_documents({"method": method})))
    print("{} status check"
          .format(logs_collection.count_documents(
                  {"method": "GET", "path": "/status"})))
