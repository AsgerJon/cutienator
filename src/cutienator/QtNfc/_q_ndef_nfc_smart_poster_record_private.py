"""
QNdefNfcSmartPosterRecordPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/6.12.0/QtNfc/private/qndefnfcsmartposterrecord_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNdefNfcSmartPosterRecordPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QSharedData


class QNdefNfcSmartPosterRecordPrivate(QSharedData):
  """
  The cute side of Qt's QNdefNfcSmartPosterRecordPrivate: a plain Python
  object standing in front of one C++ QNdefNfcSmartPosterRecordPrivate.

  It is built on the cute 'QSharedData', as Qt's
  QNdefNfcSmartPosterRecordPrivate is built on Qt's QSharedData, and has
  everything that class has.

  C++ hands a QNdefNfcSmartPosterRecordPrivate around as a copy, so every C++
  QNdefNfcSmartPosterRecordPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QNdefNfcSmartPosterRecordPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'cleanup'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QNdefNfcSmartPosterRecordPrivate::~QNdefNfcSmartPosterRecordPrivate()':
    the destructor: Python removes its C++ QNdefNfcSmartPosterRecordPrivate
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNdefNfcSmartPosterRecordPrivate is created at the first use, not
    by 'QNdefNfcSmartPosterRecordPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefNfcSmartPosterRecordPrivate back gives a copy
    the ritual made for Python, in a new cute
    QNdefNfcSmartPosterRecordPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefNfcSmartPosterRecordPrivate'

  #  Qt's '~QNdefNfcSmartPosterRecordPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QNdefNfcSmartPosterRecordPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN32QNdefNfcSmartPosterRecordPrivateD1Ev'

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
    'QNdefNfcSmartPosterRecordPrivate::QNdefNfcSmartPosterRecordPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecordprivate.html
    """
    #  QNdefNfcSmartPosterRecordPrivate::QNdefNfcSmartPosterRecordPrivate()
    self._noteCreation(
        QNdefNfcSmartPosterRecordPrivate, lambda: Rituals.call(
            'ritual_ZN32QNdefNfcSmartPosterRecordPrivateC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecordPrivate::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecordprivate.html#cleanup
    """
    #  void QNdefNfcSmartPosterRecordPrivate::cleanup()
    self.uglySide.call(
        'ritual_ZN32QNdefNfcSmartPosterRecordPrivate7cleanupEv',
    )
