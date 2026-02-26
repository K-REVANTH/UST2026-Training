#!/usr/bin/env python3

import sys
import os
import json
import yaml
import configparser
from jsonschema import validate, ValidationError

SCHEMA = {
    "type": "object",
    "properties": {
        "app_name": {"type": "string"},
        "port": {"type": "integer"},
        "debug": {"type": "boolean"},
        "database": {
            "type": "object",
            "properties": {
                "host": {"type": "string"},
                "port": {"type": "integer"},
            },
            "required": ["host", "port"]
        }
    },
    "required": ["app_name", "port", "database"]
}

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def load_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def load_ini(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return {section: dict(config[section]) for section in config.sections()}

def validate_config(config_data):
    try:
        validate(instance=config_data, schema=SCHEMA)
        print("\nVALIDATION SUCCESS")
        print("Configuration file is valid.")
        return True
    except ValidationError as e:
        print("\nVALIDATION FAILED")
        print("Error:", e.message)
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 config_validator.py <config_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        sys.exit(1)
    try:
        if file_path.endswith(".json"):
            config_data = load_json(file_path)
        elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
            config_data = load_yaml(file_path)
        elif file_path.endswith(".ini"):
            config_data = load_ini(file_path)
        else:
            print("Unsupported file format.")
            sys.exit(1)
        is_valid = validate_config(config_data)
        if not is_valid:
            sys.exit(1)
    except Exception as e:
        print("\nCRITICAL ERROR")
        print(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
