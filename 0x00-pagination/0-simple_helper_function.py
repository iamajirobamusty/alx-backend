#!/usr/bin/python3

""" A function that takes in two argument and return a turple
"""
def index_range(page: int, page_size: int) -> Tuple[int, int]:
  page = (page - 1) * page_size
  page_size = page + page_size
  return (page, page_size)
