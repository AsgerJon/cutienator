"""
QQuickAnimationPropertyUpdater binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAnimationPropertyUpdater to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickBulkValueUpdater

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QQuickAnimationPropertyUpdater(QQuickBulkValueUpdater):
  """
  The cute side of Qt's QQuickAnimationPropertyUpdater: a plain Python object
  standing in front of one C++ QQuickAnimationPropertyUpdater.

  It is built on the cute 'QQuickBulkValueUpdater', as Qt's
  QQuickAnimationPropertyUpdater is built on Qt's QQuickBulkValueUpdater, and
  has everything that class has.

  C++ hands a QQuickAnimationPropertyUpdater around as a copy, so every C++
  QQuickAnimationPropertyUpdater behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickAnimationPropertyUpdater that has a ritual and
  that Python can call so far, 2 names in all: 'setValue', 'debugUpdater'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickAnimationPropertyUpdater::~QQuickAnimationPropertyUpdater()':
    the destructor: Python removes its C++ QQuickAnimationPropertyUpdater by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickAnimationPropertyUpdater is created at the first use, not
    by 'QQuickAnimationPropertyUpdater(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickAnimationPropertyUpdater back gives a copy the
    ritual made for Python, in a new cute QQuickAnimationPropertyUpdater.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimationPropertyUpdater'

  #  A C++ QQuickAnimationPropertyUpdater Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimationPropertyUpdater'

  #  Qt's '~QQuickAnimationPropertyUpdater()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickAnimationPropertyUpdater behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QQuickAnimationPropertyUpdaterD1Ev'

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
    Calls Qt's 'void QQuickAnimationPropertyUpdater::setValue(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationpropertyupdater.html#setValue

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickAnimationPropertyUpdater::setValue(qreal v)
    ritual = 'ritual_ZN30QQuickAnimationPropertyUpdater8setValueEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QQuickAnimationPropertyUpdater8setValueEd'
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
    'QQuickAnimationPropertyUpdater::QQuickAnimationPropertyUpdater()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationpropertyupdater.html
    """
    #  QQuickAnimationPropertyUpdater::QQuickAnimationPropertyUpdater()
    self._noteCreation(QQuickAnimationPropertyUpdater, lambda: Rituals.call(
        'ritual_ZN30QQuickAnimationPropertyUpdaterC1Ev',
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

  @overload(QDebug, int)
  def debugUpdater(self, d: QDebug, indentLevel: int) -> None:
    """
    Calls Qt's 'void QQuickAnimationPropertyUpdater::debugUpdater(QDebug d,
    int indentLevel) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationpropertyupdater.html#debugUpdater

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    indentLevel : int
      Passed on as it is.
    """
    #  void QQuickAnimationPropertyUpdater::debugUpdater(QDebug d, int
    #      indentLevel) const
    ritual = (
        'ritual_ZNK30QQuickAnimationPropertyUpdater12debugUpdaterE6QDebugi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QQuickAnimationPropertyUpdater12debugUpdaterE6QD'
          'ebugi')
    self.uglySide.call(ritual, self._valueOf(d), indentLevel)
