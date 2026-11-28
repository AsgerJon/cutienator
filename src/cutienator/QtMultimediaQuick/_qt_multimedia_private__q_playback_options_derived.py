"""
QtMultimediaPrivate::QPlaybackOptionsDerived binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquicktypes_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::QPlaybackOptionsDerived to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtMultimedia import QPlaybackOptions


class QPlaybackOptionsDerived(QPlaybackOptions):
  """
  The cute side of Qt's QtMultimediaPrivate::QPlaybackOptionsDerived: a plain
  Python object standing in front of one C++
  QtMultimediaPrivate::QPlaybackOptionsDerived.

  It is built on the cute 'QPlaybackOptions', as Qt's
  QtMultimediaPrivate::QPlaybackOptionsDerived is built on Qt's
  QPlaybackOptions, and has everything that class has.

  C++ hands a QtMultimediaPrivate::QPlaybackOptionsDerived around as a copy,
  so every C++ QtMultimediaPrivate::QPlaybackOptionsDerived behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtMultimediaPrivate::QPlaybackOptionsDerived that
  has a ritual and that Python can call so far, 3 names in all:
  'networkTimeoutMs', 'setNetworkTimeoutMs', 'resetNetworkTimeoutMs'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QtMultimediaPrivate::QPlaybackOptionsDerived::qt_qmlMarker_foreign()':
    one of Qt's own inner workings.
  - Qt's 'void
    QtMultimediaPrivate::QPlaybackOptionsDerived::qt_qmlMarker_extended()':
    one of Qt's own inner workings.
  - Qt's
    'QtMultimediaPrivate::QPlaybackOptionsDerived::~QPlaybackOptionsDerived(
    )': the destructor: Python removes its C++
    QtMultimediaPrivate::QPlaybackOptionsDerived by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 9 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QtMultimediaPrivate::QPlaybackOptionsDerived is created at the
    first use, not by 'QtMultimediaPrivate::QPlaybackOptionsDerived(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMultimediaPrivate::QPlaybackOptionsDerived back
    gives a copy the ritual made for Python, in a new cute
    QtMultimediaPrivate::QPlaybackOptionsDerived.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMultimediaPrivate::QPlaybackOptionsDerived'

  #  Qt's '~QtMultimediaPrivate::QPlaybackOptionsDerived()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QtMultimediaPrivate::QPlaybackOptionsDerived behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN19QtMultimediaPrivate23QPlaybackOptionsDerivedD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def networkTimeoutMs(self) -> int:
    """
    Calls Qt's 'qint64
    QtMultimediaPrivate::QPlaybackOptionsDerived::networkTimeoutMs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qplaybackoptionsderived.html
    """
    #  qint64
    #      QtMultimediaPrivate::QPlaybackOptionsDerived::networkTimeoutMs()
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate23QPlaybackOptionsDerived16networkT'
        'imeoutMsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setNetworkTimeoutMs(self, timeout: int) -> None:
    """
    Calls Qt's 'void
    QtMultimediaPrivate::QPlaybackOptionsDerived::setNetworkTimeoutMs(qint64
    timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qplaybackoptionsderived.html

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void
    #      QtMultimediaPrivate::QPlaybackOptionsDerived::setNetworkTimeoutMs(
    #      qint64 timeout)
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate23QPlaybackOptionsDerived19setNetwor'
        'kTimeoutMsEx',
        timeout,
    )

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

  def resetNetworkTimeoutMs(self) -> None:
    """
    Calls Qt's 'void
    QtMultimediaPrivate::QPlaybackOptionsDerived::resetNetworkTimeoutMs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qplaybackoptionsderived.html
    """
    #  void QtMultimediaPrivate::QPlaybackOptionsDerived::
    #      resetNetworkTimeoutMs()
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate23QPlaybackOptionsDerived21resetNetw'
        'orkTimeoutMsEv',
    )
