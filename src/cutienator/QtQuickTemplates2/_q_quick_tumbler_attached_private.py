"""
QQuickTumblerAttachedPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTumblerAttachedPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtQuick import QQuickItem
  from . import QQuickTumblerAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QQuickTumblerAttached = WAIT['QQuickTumblerAttached']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTumblerAttachedPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickTumblerAttachedPrivate: a plain Python object
  standing in front of one C++ QQuickTumblerAttachedPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickTumblerAttachedPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTumblerAttachedPrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func', 'get', 'init',
  'calculateDisplacement', 'emitIfDisplacementChanged'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTumblerAttached *QQuickTumblerAttachedPrivate::q_func()
    const': takes in Python what 'QQuickTumblerAttached
    *QQuickTumblerAttachedPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickTumblerAttachedPrivate is created at the first use, not by
    'QQuickTumblerAttachedPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTumblerAttachedPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickTumblerAttached)
  @overload(NoneType)
  def get(
      attached: Optional[QQuickTumblerAttached],
  ) -> Optional[QQuickTumblerAttachedPrivate]:
    """
    Calls Qt's 'QQuickTumblerAttachedPrivate
    *QQuickTumblerAttachedPrivate::get(QQuickTumblerAttached *attached)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerattachedprivate.html#get

    Parameters
    ----------

    attached : Optional[QQuickTumblerAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTumblerAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTumblerAttachedPrivate
    #      *QQuickTumblerAttachedPrivate::get(QQuickTumblerAttached
    #      *attached)
    address = Rituals.call(
        'ritual_ZN28QQuickTumblerAttachedPrivate3getEP21QQuickTumblerAttach'
        'ed',
        CuteMixin._addressOf(attached),
    )
    return QQuickTumblerAttachedPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTumblerAttachedPrivate'

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

  def q_func(self) -> Optional[QQuickTumblerAttached]:
    """
    Calls Qt's 'QQuickTumblerAttached
    *QQuickTumblerAttachedPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerattachedprivate.html#q_func

    Returns
    -------

    Optional[QQuickTumblerAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTumblerAttached *QQuickTumblerAttachedPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QQuickTumblerAttachedPrivate6q_funcEv',
    )
    from . import QQuickTumblerAttached
    return QQuickTumblerAttached._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def init(self, delegateItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTumblerAttachedPrivate::init(QQuickItem
    *delegateItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerattachedprivate.html#init

    Parameters
    ----------

    delegateItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTumblerAttachedPrivate::init(QQuickItem *delegateItem)
    self.uglySide.call(
        'ritual_ZN28QQuickTumblerAttachedPrivate4initEP10QQuickItem',
        self._addressOf(delegateItem),
    )

  def calculateDisplacement(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerAttachedPrivate::calculateDisplacement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerattachedprivate.html
    """
    #  void QQuickTumblerAttachedPrivate::calculateDisplacement()
    self.uglySide.call(
        'ritual_ZN28QQuickTumblerAttachedPrivate21calculateDisplacementEv',
    )

  @overload(float, float)
  def emitIfDisplacementChanged(
      self,
      oldDisplacement: float,
      newDisplacement: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTumblerAttachedPrivate::emitIfDisplacementChanged(qreal
    oldDisplacement, qreal newDisplacement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerattachedprivate.html

    Parameters
    ----------

    oldDisplacement : float
      Passed on as it is.

    newDisplacement : float
      Passed on as it is.
    """
    #  void QQuickTumblerAttachedPrivate::emitIfDisplacementChanged(qreal
    #      oldDisplacement, qreal newDisplacement)
    self.uglySide.call(
        'ritual_ZN28QQuickTumblerAttachedPrivate25emitIfDisplacementChanged'
        'Edd',
        oldDisplacement, newDisplacement,
    )
