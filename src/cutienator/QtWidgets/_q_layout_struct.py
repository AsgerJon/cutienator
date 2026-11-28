"""
QLayoutStruct binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlayoutengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLayoutStruct to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class QLayoutStruct(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLayoutStruct: a plain Python object standing in
  front of one C++ QLayoutStruct.

  C++ hands a QLayoutStruct around as a copy, so every C++ QLayoutStruct
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLayoutStruct that has a ritual and that Python can
  call so far, 3 names in all: 'init', 'smartSizeHint', 'effectiveSpacer'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLayoutStruct::~QLayoutStruct()': the destructor: Python removes
    its C++ QLayoutStruct by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLayoutStruct is created at the first use, not by
    'QLayoutStruct(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLayoutStruct back gives a copy the ritual made for
    Python, in a new cute QLayoutStruct.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLayoutStruct'

  #  Qt's '~QLayoutStruct()'. Naming it makes this a value class: Python owns
  #  every C++ QLayoutStruct behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QLayoutStructD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def effectiveSpacer(self, uniformSpacer: int) -> int:
    """
    Calls Qt's 'int QLayoutStruct::effectiveSpacer(int uniformSpacer) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutstruct.html#effectiveSpacer

    Parameters
    ----------

    uniformSpacer : int
      Passed on as it is.
    """
    #  int QLayoutStruct::effectiveSpacer(int uniformSpacer) const
    return self.uglySide.call(
        'ritual_ZNK13QLayoutStruct15effectiveSpacerEi', uniformSpacer,
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

  @overload()
  @overload(int)
  @overload(int, int)
  def init(self, stretchFactor: int = 0, minSize: int = 0) -> None:
    """
    Calls Qt's 'void QLayoutStruct::init(int stretchFactor, int minSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutstruct.html#init

    Parameters
    ----------

    stretchFactor : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    minSize : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QLayoutStruct::init(int stretchFactor, int minSize)
    self.uglySide.call(
        'ritual_ZN13QLayoutStruct4initEii', stretchFactor, minSize,
    )

  def smartSizeHint(self) -> int:
    """
    Calls Qt's 'int QLayoutStruct::smartSizeHint()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutstruct.html#smartSizeHint
    """
    #  int QLayoutStruct::smartSizeHint()
    return self.uglySide.call('ritual_ZN13QLayoutStruct13smartSizeHintEv')
