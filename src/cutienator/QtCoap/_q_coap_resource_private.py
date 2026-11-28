"""
QCoapResourcePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapresource_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCoapResourcePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QSharedData


class QCoapResourcePrivate(QSharedData):
  """
  The cute side of Qt's QCoapResourcePrivate: a plain Python object standing
  in front of one C++ QCoapResourcePrivate.

  It is built on the cute 'QSharedData', as Qt's QCoapResourcePrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QCoapResourcePrivate around as a copy, so every C++
  QCoapResourcePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QCoapResourcePrivate yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapResourcePrivate::~QCoapResourcePrivate()': the destructor:
    Python removes its C++ QCoapResourcePrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QCoapResourcePrivate is created at the first use, not by
    'QCoapResourcePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCoapResourcePrivate back gives a copy the ritual
    made for Python, in a new cute QCoapResourcePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapResourcePrivate'

  #  Qt's '~QCoapResourcePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCoapResourcePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QCoapResourcePrivateD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCoapResourcePrivate::QCoapResourcePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourceprivate.html#QCoapResourcePrivate
    """
    #  QCoapResourcePrivate::QCoapResourcePrivate()
    self._noteCreation(QCoapResourcePrivate, lambda: Rituals.call(
        'ritual_ZN20QCoapResourcePrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCoapResourcePrivate) -> None:
    """
    Notes what was given, for Qt's
    'QCoapResourcePrivate::QCoapResourcePrivate(const QCoapResourcePrivate
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourceprivate.html#QCoapResourcePrivate

    Parameters
    ----------

    other : QCoapResourcePrivate
      Passed on as a value: Qt reads the C++ QCoapResourcePrivate, which
      stays Python's own.
    """
    #  QCoapResourcePrivate::QCoapResourcePrivate(const QCoapResourcePrivate
    #      &other)
    self._noteCreation(QCoapResourcePrivate, lambda: Rituals.call(
        'ritual_ZN20QCoapResourcePrivateC1ERKS_', self._valueOf(other),
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
