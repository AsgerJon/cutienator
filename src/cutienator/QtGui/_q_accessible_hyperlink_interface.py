"""
QAccessibleHyperlinkInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute


class QAccessibleHyperlinkInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleHyperlinkInterface: a plain Python object
  standing in front of one C++ QAccessibleHyperlinkInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleHyperlinkInterface that has a ritual and
  that Python can call so far, 5 names in all: 'anchor', 'anchorTarget',
  'startIndex', 'endIndex', 'isValid'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleHyperlinkInterface::~QAccessibleHyperlinkInterface()':
    the destructor: Python never removes a C++ QAccessibleHyperlinkInterface.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one.

  What to expect
  --------------

  - The C++ QAccessibleHyperlinkInterface is created at the first use, not by
    'QAccessibleHyperlinkInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleHyperlinkInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleHyperlinkInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def anchor(self) -> str:
    """
    Calls Qt's 'QString QAccessibleHyperlinkInterface::anchor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblehyperlinkinterface.html#anchor

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleHyperlinkInterface::anchor() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleHyperlinkInterface6anchorEv',
    )

  def anchorTarget(self) -> str:
    """
    Calls Qt's 'QString QAccessibleHyperlinkInterface::anchorTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblehyperlinkinterface.html#anchorTarget

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleHyperlinkInterface::anchorTarget() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleHyperlinkInterface12anchorTargetEv',
    )

  def startIndex(self) -> int:
    """
    Calls Qt's 'int QAccessibleHyperlinkInterface::startIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblehyperlinkinterface.html#startIndex
    """
    #  int QAccessibleHyperlinkInterface::startIndex() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleHyperlinkInterface10startIndexEv',
    )

  def endIndex(self) -> int:
    """
    Calls Qt's 'int QAccessibleHyperlinkInterface::endIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblehyperlinkinterface.html#endIndex
    """
    #  int QAccessibleHyperlinkInterface::endIndex() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleHyperlinkInterface8endIndexEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleHyperlinkInterface::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblehyperlinkinterface.html#isValid
    """
    #  bool QAccessibleHyperlinkInterface::isValid() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleHyperlinkInterface7isValidEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
