"""
QQuickPathAnimationUpdater binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPathAnimationUpdater to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QQuickBulkValueUpdater


class QQuickPathAnimationUpdater(QQuickBulkValueUpdater):
  """
  The cute side of Qt's QQuickPathAnimationUpdater: a plain Python object
  standing in front of one C++ QQuickPathAnimationUpdater.

  It is built on the cute 'QQuickBulkValueUpdater', as Qt's
  QQuickPathAnimationUpdater is built on Qt's QQuickBulkValueUpdater, and has
  everything that class has.

  C++ hands a QQuickPathAnimationUpdater around as a copy, so every C++
  QQuickPathAnimationUpdater behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickPathAnimationUpdater that has a ritual and
  that Python can call so far, 1 name in all: 'setValue'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickPathAnimationUpdater::~QQuickPathAnimationUpdater()': the
    destructor: Python removes its C++ QQuickPathAnimationUpdater by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuickPathAnimationUpdater is created at the first use, not by
    'QQuickPathAnimationUpdater(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickPathAnimationUpdater back gives a copy the
    ritual made for Python, in a new cute QQuickPathAnimationUpdater.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathAnimationUpdater'

  #  A C++ QQuickPathAnimationUpdater Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPathAnimationUpdater'

  #  Qt's '~QQuickPathAnimationUpdater()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickPathAnimationUpdater behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQuickPathAnimationUpdaterD1Ev'

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

  @overload(float)
  def setValue(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickPathAnimationUpdater::setValue(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimationupdater.html#setValue

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickPathAnimationUpdater::setValue(qreal v)
    ritual = 'ritual_ZN26QQuickPathAnimationUpdater8setValueEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuickPathAnimationUpdater8setValueEd'
    self.uglySide.call(ritual, v)

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
    'QQuickPathAnimationUpdater::QQuickPathAnimationUpdater()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimationupdater.html
    """
    #  QQuickPathAnimationUpdater::QQuickPathAnimationUpdater()
    self._noteCreation(QQuickPathAnimationUpdater, lambda: Rituals.call(
        'ritual_ZN26QQuickPathAnimationUpdaterC1Ev',
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
