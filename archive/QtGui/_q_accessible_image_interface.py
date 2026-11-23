"""
QAccessibleImageInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint, QSize


class QAccessibleImageInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleImageInterface: a plain Python object
  standing in front of one C++ QAccessibleImageInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleImageInterface that has a ritual and that
  Python can call so far, 3 names in all: 'imageDescription', 'imageSize',
  'imagePosition'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleImageInterface::~QAccessibleImageInterface()': the
    destructor: Python never removes a C++ QAccessibleImageInterface.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one.

  What to expect
  --------------

  - The C++ QAccessibleImageInterface is created at the first use, not by
    'QAccessibleImageInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleImageInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleImageInterface'

  #  A C++ QAccessibleImageInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleImageInterface'

  #  The functions Qt calls itself that QAccessibleImageInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'imageDescription': (
          ('_ZNK25QAccessibleImageInterface16imageDescriptionEv',
           ('address', 'text', ''),
           ()),
      ),
      'imageSize': (
          ('_ZNK25QAccessibleImageInterface9imageSizeEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
      'imagePosition': (
          ('_ZNK25QAccessibleImageInterface13imagePositionEv',
           ('address', 'value', 'QtCore:QPoint'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def imageDescription(self) -> str:
    """
    Calls Qt's 'QString QAccessibleImageInterface::imageDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleimageinterface.html#imageDescription

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleImageInterface::imageDescription() const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleImageInterface16imageDescriptionEv',
    )

  def imageSize(self) -> QSize:
    """
    Calls Qt's 'QSize QAccessibleImageInterface::imageSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleimageinterface.html#imageSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAccessibleImageInterface::imageSize() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleImageInterface9imageSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def imagePosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAccessibleImageInterface::imagePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleimageinterface.html#imagePosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAccessibleImageInterface::imagePosition() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleImageInterface13imagePositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

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
