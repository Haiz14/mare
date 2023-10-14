import os
from pathlib import Path

from errors import ProjectExists, ProjectNotFound

MARE_DIR_LOACTION = Path.home().joinpath(".mare")

def create_project(project_name):
  # create dir
  project_path = MARE_DIR_LOACTION.joinpath(project_name)

  if project_path.exists():
    raise ProjectExists(f"A project with the name '{project_name}' already exists at '{project_path}'. Please choose a different name or location.")


  project_path.mkdir()

def get_project_location(project_name):
  project_path = MARE_DIR_LOACTION.joinpath(project_name)

  if project_path.exists():
    return project_path
  raise ProjectNotFound(f"the project with the name {project_name} does not exist in path {project_path}. Please check the project name.")


def check_mare_exists():
  return MARE_DIR_LOACTION.exists()

def create_mare():
  if check_mare_exists():
    raise Exception(f"Mare dir already exists in path {MARE_DIR_LOACTION}")
  MARE_DIR_LOACTION.mkdir()

def main():
  # create_project("haiz")
  #print(check_mare_exists())
  create_mare()

if __name__ == "__main__":
  main()
