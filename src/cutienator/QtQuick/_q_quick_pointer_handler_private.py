"""
QQuickPointerHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpointerhandler_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPointerHandlerPrivate to be private: it declares the class
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
  from typing import Never, Optional

  from ..QtGui import QEventPoint, QVector2D
  from . import QQuickItem, QQuickPointerHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QQuickItem = WAIT['QQuickItem']
  QQuickPointerHandler = WAIT['QQuickPointerHandler']
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPointerHandlerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickPointerHandlerPrivate: a plain Python object
  standing in front of one C++ QQuickPointerHandlerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickPointerHandlerPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPointerHandlerPrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func', 'get',
  'dragOverThreshold', 'onParentChanged', 'onEnabledChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPointerHandler *QQuickPointerHandlerPrivate::q_func()
    const': takes in Python what 'QQuickPointerHandler
    *QQuickPointerHandlerPrivate::q_func()' takes.
  - Qt's 'const QQuickPointerHandlerPrivate
    *QQuickPointerHandlerPrivate::get(const QQuickPointerHandler *q)': takes
    in Python what 'QQuickPointerHandlerPrivate
    *QQuickPointerHandlerPrivate::get(QQuickPointerHandler *q)' takes.
  - Qt's 'QList<QObject *>
    &QQuickPointerHandlerPrivate::deviceDeliveryTargets(const QInputDevice
    *device)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 11 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQuickPointerHandlerPrivate is created at the first use, not by
    'QQuickPointerHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPointerHandlerPrivate.
  - Each name of Qt's QQuickPointerHandlerPrivate that has no cute function
    yet, 'deviceDeliveryTargets', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickPointerHandler)
  @overload(NoneType)
  def get(
      q: Optional[QQuickPointerHandler],
  ) -> Optional[QQuickPointerHandlerPrivate]:
    """
    Calls Qt's 'QQuickPointerHandlerPrivate
    *QQuickPointerHandlerPrivate::get(QQuickPointerHandler *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandlerprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickPointerHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPointerHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPointerHandlerPrivate
    #      *QQuickPointerHandlerPrivate::get(QQuickPointerHandler *q)
    address = Rituals.call(
        'ritual_ZN27QQuickPointerHandlerPrivate3getEP20QQuickPointerHandler',
        CuteMixin._addressOf(q),
    )
    return QQuickPointerHandlerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPointerHandlerPrivate'

  #  A C++ QQuickPointerHandlerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPointerHandlerPrivate'

  #  The functions Qt calls itself that QQuickPointerHandlerPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'onParentChanged': (
          ('_ZN27QQuickPointerHandlerPrivate15onParentChangedEP10QQuickItem'
           'S1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'onEnabledChanged': (
          ('_ZN27QQuickPointerHandlerPrivate16onEnabledChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector2D)
  def dragOverThreshold(self, delta: QVector2D) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandlerPrivate::dragOverThreshold(QVector2D
    delta) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandlerprivate.html#dragOverThreshold

    Parameters
    ----------

    delta : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  bool QQuickPointerHandlerPrivate::dragOverThreshold(QVector2D delta)
    #      const
    return self.uglySide.call(
        'ritual_ZNK27QQuickPointerHandlerPrivate17dragOverThresholdE9QVecto'
        'r2D',
        self._valueOf(delta),
    )

  @overload(QEventPoint)
  def dragOverThreshold(self, point: QEventPoint) -> bool:
    """
    Calls Qt's 'bool QQuickPointerHandlerPrivate::dragOverThreshold(const
    QEventPoint &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandlerprivate.html#dragOverThreshold

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickPointerHandlerPrivate::dragOverThreshold(const QEventPoint
    #      &point) const
    return self.uglySide.call(
        'ritual_ZNK27QQuickPointerHandlerPrivate17dragOverThresholdERK11QEv'
        'entPoint',
        self._valueOf(point),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPointerHandlerPrivate::QQuickPointerHandlerPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandlerprivate.html
    """
    #  QQuickPointerHandlerPrivate::QQuickPointerHandlerPrivate()
    self._noteCreation(QQuickPointerHandlerPrivate, lambda: Rituals.call(
        'ritual_ZN27QQuickPointerHandlerPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickPointerHandler]:
    """
    Calls Qt's 'QQuickPointerHandler *QQuickPointerHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandlerprivate.html#q_func

    Returns
    -------

    Optional[QQuickPointerHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPointerHandler *QQuickPointerHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QQuickPointerHandlerPrivate6q_funcEv',
    )
    from . import QQuickPointerHandler
    return QQuickPointerHandler._cuteAt(address)

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def onParentChanged(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickPointerHandlerPrivate::onParentChanged(QQuickItem
    *a0, QQuickItem *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandlerprivate.html#onParentChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPointerHandlerPrivate::onParentChanged(QQuickItem *a0,
    #      QQuickItem *a1)
    ritual = (
        'ritual_ZN27QQuickPointerHandlerPrivate15onParentChangedEP10QQuickI'
        'temS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickPointerHandlerPrivate15onParentChangedEP10Q'
          'QuickItemS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  def onEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerHandlerPrivate::onEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerhandlerprivate.html#onEnabledChanged
    """
    #  void QQuickPointerHandlerPrivate::onEnabledChanged()
    ritual = 'ritual_ZN27QQuickPointerHandlerPrivate16onEnabledChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickPointerHandlerPrivate16onEnabledChangedEv')
    self.uglySide.call(ritual)

  @staticmethod
  def deviceDeliveryTargets(*__, **_) -> Never:
    """
    Qt's 'QList<QObject *>
    &QQuickPointerHandlerPrivate::deviceDeliveryTargets(const QInputDevice
    *device)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPointerHandlerPrivate.deviceDeliveryTargets' has no cute "
        "function yet. Qt's 'QList<QObject *> "
        "&QQuickPointerHandlerPrivate::deviceDeliveryTargets(const "
        "QInputDevice *device)': gives a type Python has no way to take yet."
    )
