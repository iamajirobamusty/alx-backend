#!/usr/bin/python3

""" A function that takes in two argument and return a turple
"""
def index_range(page: int, page_size: int) -> Tuple[int, int]:
  """
    start index and an end index corresponding to the range of
    """
  # if page is 1, start at 0 and end at page_size
  # if page is 2, start at ((page-1) * page_size) and
  # end at (page_size * page)
  # if page is 3, start at ((page-1) * page_size) and
  # end at (page_size * page)
  page = (page - 1) * page_size
  page_size = page + page_size
  return (page, page_size)
