"""
QSSGPickResultProcessResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpickresult_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGPickResultProcessResult to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSSGRenderPickResult


class QSSGPickResultProcessResult(QSSGRenderPickResult):
  """
  The cute side of Qt's QSSGPickResultProcessResult: a plain Python object
  standing in front of one C++ QSSGPickResultProcessResult.

  It is built on the cute 'QSSGRenderPickResult', as Qt's
  QSSGPickResultProcessResult is built on Qt's QSSGRenderPickResult, and has
  everything that class has.

  C++ hands a QSSGPickResultProcessResult around as a copy, so every C++
  QSSGPickResultProcessResult behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QSSGPickResultProcessResult yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGPickResultProcessResult::~QSSGPickResultProcessResult()': the
    destructor: Python removes its C++ QSSGPickResultProcessResult by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGPickResultProcessResult is created at the first use, not by
    'QSSGPickResultProcessResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGPickResultProcessResult back gives a copy the
    ritual made for Python, in a new cute QSSGPickResultProcessResult.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGPickResultProcessResult'

  #  Qt's '~QSSGPickResultProcessResult()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGPickResultProcessResult behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QSSGPickResultProcessResultD1Ev'

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

  @overload(QSSGRenderPickResult)
  def __init__(self, inSrc: QSSGRenderPickResult) -> None:
    """
    Notes what was given, for Qt's
    'QSSGPickResultProcessResult::QSSGPickResultProcessResult(const
    QSSGRenderPickResult &inSrc)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgpickresultprocessresult.html

    Parameters
    ----------

    inSrc : QSSGRenderPickResult
      Passed on as a value: Qt reads the C++ QSSGRenderPickResult, which
      stays Python's own.
    """
    #  QSSGPickResultProcessResult::QSSGPickResultProcessResult(const
    #      QSSGRenderPickResult &inSrc)
    self._noteCreation(QSSGPickResultProcessResult, lambda: Rituals.call(
        'ritual_ZN27QSSGPickResultProcessResultC1ERK20QSSGRenderPickResult',
        self._valueOf(inSrc),
    ))

  @overload(QSSGRenderPickResult, bool)
  def __init__(self, inSrc: QSSGRenderPickResult, consumed: bool) -> None:
    """
    Notes what was given, for Qt's
    'QSSGPickResultProcessResult::QSSGPickResultProcessResult(const
    QSSGRenderPickResult &inSrc, bool consumed)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgpickresultprocessresult.html

    Parameters
    ----------

    inSrc : QSSGRenderPickResult
      Passed on as a value: Qt reads the C++ QSSGRenderPickResult, which
      stays Python's own.

    consumed : bool
      Passed on as it is.
    """
    #  QSSGPickResultProcessResult::QSSGPickResultProcessResult(const
    #      QSSGRenderPickResult &inSrc, bool consumed)
    self._noteCreation(QSSGPickResultProcessResult, lambda: Rituals.call(
        'ritual_ZN27QSSGPickResultProcessResultC1ERK20QSSGRenderPickResultb',
        self._valueOf(inSrc), consumed,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGPickResultProcessResult::QSSGPickResultProcessResult()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgpickresultprocessresult.html
    """
    #  QSSGPickResultProcessResult::QSSGPickResultProcessResult()
    self._noteCreation(QSSGPickResultProcessResult, lambda: Rituals.call(
        'ritual_ZN27QSSGPickResultProcessResultC1Ev',
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
