"""
DataChangeRelevanceFlag stands for the flags enum
'QSortFilterProxyModel::DataChangeRelevanceFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qsortfilterproxymodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class DataChangeRelevanceFlag(CuteFlags, scoped=True):
  """
  The flags enum 'QSortFilterProxyModel::DataChangeRelevanceFlag' of Qt, with
  the 4 names Qt gives in it. Qt names the type of its combinations
  'QSortFilterProxyModel::DataChangeRelevanceFlags'. C++ keeps these names
  inside the enum, so the class that holds the enum does not have them.
  """

  NotRelevant = 0x0
  RelevantForFiltering = 0x1
  RelevantForSorting = 0x2
  RelevantForFilteringAndSorting = 0x3
