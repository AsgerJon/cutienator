"""
QAccessibleHyperlinkInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QAccessibleHyperlinkInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleHyperlinkInterface: a plain Python object
  standing in front of one C++ QAccessibleHyperlinkInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleHyperlinkInterface that has a ritual and
  that Python can call so far, 5 names in all: 'anchor', 'anchorTarget',
  'startIndex', 'endIndex', 'isValid'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleHyperlinkInterface::~QAccessibleHyperlinkInterface()':
    the destructor: Python never removes a C++ QAccessibleHyperlinkInterface.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

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

  #  A C++ QAccessibleHyperlinkInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleHyperlinkInterface'

  #  The functions Qt calls itself that QAccessibleHyperlinkInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'anchor': (
          ('_ZNK29QAccessibleHyperlinkInterface6anchorEv',
           ('address', 'text', ''),
           ()),
      ),
      'anchorTarget': (
          ('_ZNK29QAccessibleHyperlinkInterface12anchorTargetEv',
           ('address', 'text', ''),
           ()),
      ),
      'startIndex': (
          ('_ZNK29QAccessibleHyperlinkInterface10startIndexEv',
           ('int', 'number', ''),
           ()),
      ),
      'endIndex': (
          ('_ZNK29QAccessibleHyperlinkInterface8endIndexEv',
           ('int', 'number', ''),
           ()),
      ),
      'isValid': (
          ('_ZNK29QAccessibleHyperlinkInterface7isValidEv',
           ('bool', 'number', ''),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleHyperlinkInterface::QAccessibleHyperlinkInterface()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblehyperlinkinterface.html
    """
    #  QAccessibleHyperlinkInterface::QAccessibleHyperlinkInterface()
    self._noteCreation(QAccessibleHyperlinkInterface, lambda: Rituals.call(
        'ritual_ZN29QAccessibleHyperlinkInterfaceC1Ev',
    ))

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
