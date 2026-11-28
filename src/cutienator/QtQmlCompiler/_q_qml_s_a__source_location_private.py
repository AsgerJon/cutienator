"""
QQmlSA::SourceLocationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsasourcelocation_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlSA::SourceLocationPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQml import QQmlJS
from . import QQmlSA


class SourceLocationPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::SourceLocationPrivate: a plain Python object
  standing in front of one C++ QQmlSA::SourceLocationPrivate.

  C++ hands a QQmlSA::SourceLocationPrivate around as a copy, so every C++
  QQmlSA::SourceLocationPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::SourceLocationPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'sourceLocation',
  'createQQmlSASourceLocation', 'sizeOfSourceLocation'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSA::SourceLocationPrivate::~SourceLocationPrivate()': the
    destructor: Python removes its C++ QQmlSA::SourceLocationPrivate by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlSA::SourceLocationPrivate is created at the first use, not by
    'QQmlSA::SourceLocationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::SourceLocationPrivate back gives a copy the
    ritual made for Python, in a new cute QQmlSA::SourceLocationPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QQmlSA.SourceLocation'])
  def sourceLocation(
      sourceLocation: QQmlSA.SourceLocation,
  ) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'const QQmlJS::SourceLocation
    &QQmlSA::SourceLocationPrivate::sourceLocation(const
    QQmlSA::SourceLocation &sourceLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocationprivate.html#sourceLocation

    Parameters
    ----------

    sourceLocation : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  const QQmlJS::SourceLocation
    #      &QQmlSA::SourceLocationPrivate::sourceLocation(const
    #      QQmlSA::SourceLocation &sourceLocation)
    address = Rituals.call(
        'ritual_ZN6QQmlSA21SourceLocationPrivate14sourceLocationERKNS_14Sou'
        'rceLocationE',
        CuteMixin._valueOf(sourceLocation),
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QQmlJS.SourceLocation'])
  def createQQmlSASourceLocation(
      jsLocation: QQmlJS.SourceLocation,
  ) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'QQmlSA::SourceLocation
    QQmlSA::SourceLocationPrivate::createQQmlSASourceLocation(const
    QQmlJS::SourceLocation &jsLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocationprivate.html

    Parameters
    ----------

    jsLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlSA::SourceLocation
    #      QQmlSA::SourceLocationPrivate::createQQmlSASourceLocation(const
    #      QQmlJS::SourceLocation &jsLocation)
    address = Rituals.call(
        'ritual_ZN6QQmlSA21SourceLocationPrivate26createQQmlSASourceLocatio'
        'nERKN6QQmlJS14SourceLocationE',
        CuteMixin._valueOf(jsLocation),
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  @staticmethod
  def sizeOfSourceLocation() -> int:
    """
    Calls Qt's 'qsizetype
    QQmlSA::SourceLocationPrivate::sizeOfSourceLocation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocationprivate.html
    """
    #  qsizetype QQmlSA::SourceLocationPrivate::sizeOfSourceLocation()
    return Rituals.call(
        'ritual_ZN6QQmlSA21SourceLocationPrivate20sizeOfSourceLocationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::SourceLocationPrivate'

  #  Qt's '~QQmlSA::SourceLocationPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlSA::SourceLocationPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA21SourceLocationPrivateD1Ev'

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
