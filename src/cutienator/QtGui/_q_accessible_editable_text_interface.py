"""
QAccessibleEditableTextInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class QAccessibleEditableTextInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleEditableTextInterface: a plain Python
  object standing in front of one C++ QAccessibleEditableTextInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleEditableTextInterface that has a ritual
  and that Python can call so far, 3 names in all: 'deleteText',
  'insertText', 'replaceText'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QAccessibleEditableTextInterface::~QAccessibleEditableTextInterface()':
    the destructor: Python never removes a C++
    QAccessibleEditableTextInterface.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one.

  What to expect
  --------------

  - The C++ QAccessibleEditableTextInterface is created at the first use, not
    by 'QAccessibleEditableTextInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleEditableTextInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleEditableTextInterface'

  #  A C++ QAccessibleEditableTextInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleEditableTextInterface'

  #  The functions Qt calls itself that QAccessibleEditableTextInterface is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'insertText': (
          'void QAccessibleEditableTextInterface::insertText(int, const '
          'QString &)',
      ),
      'replaceText': (
          'void QAccessibleEditableTextInterface::replaceText(int, int, '
          'const QString &)',
      ),
  }

  #  The functions Qt calls itself that QAccessibleEditableTextInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'deleteText': (
          ('_ZN32QAccessibleEditableTextInterface10deleteTextEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(int, int)
  def deleteText(self, startOffset: int, endOffset: int) -> None:
    """
    Calls Qt's 'void QAccessibleEditableTextInterface::deleteText(int
    startOffset, int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleeditabletextinterface.html#deleteText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleEditableTextInterface::deleteText(int startOffset, int
    #      endOffset)
    self.uglySide.call(
        'ritual_ZN32QAccessibleEditableTextInterface10deleteTextEii',
        startOffset, endOffset,
    )

  @overload(int, str)
  def insertText(self, offset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleEditableTextInterface::insertText(int offset,
    const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleeditabletextinterface.html#insertText

    Parameters
    ----------

    offset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleEditableTextInterface::insertText(int offset, const
    #      QString &text)
    self.uglySide.call(
        'ritual_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QStrin'
        'g',
        offset, text,
    )

  @overload(int, int, str)
  def replaceText(self, startOffset: int, endOffset: int, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleEditableTextInterface::replaceText(int
    startOffset, int endOffset, const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleeditabletextinterface.html#replaceText

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleEditableTextInterface::replaceText(int startOffset,
    #      int endOffset, const QString &text)
    self.uglySide.call(
        'ritual_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QStr'
        'ing',
        startOffset, endOffset, text,
    )
