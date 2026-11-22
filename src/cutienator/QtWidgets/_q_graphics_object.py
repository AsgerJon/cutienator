"""
QGraphicsObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsObject(QObject, QGraphicsItem):
  """
  The cute side of Qt's QGraphicsObject: a plain Python object standing in
  front of one C++ QGraphicsObject.

  It is built on the cute 'QObject', as Qt's QGraphicsObject is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QGraphicsItem' as well, as Qt's QGraphicsObject is built on Qt's
  QGraphicsItem too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsObject that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'grabGesture',
  'ungrabGesture', 'event'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsObject::~QGraphicsObject()': the destructor: Python never
    removes a C++ QGraphicsObject.

  What has no ritual
  ------------------

  19 of the 25 functions Qt declares: 12 a signal; 2 takes or gives a type
  that cannot be passed yet; 2 protected; 1 a template; 1 private; 1 the
  class is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QGraphicsObject is created at the first use, not by
    'QGraphicsObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsObject.
  - Qt tells when it has removed the C++ QGraphicsObject. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QGraphicsObject::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsobject.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsObject::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QGraphicsObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsObject'

  #  Qt's QGraphicsObject is built on more than one class. The part of a C++
  #  QGraphicsObject that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QGraphicsItem': 'ritual_cast_QGraphicsObject_QGraphicsItem',
  }

  #  A C++ QGraphicsObject Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsObject::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsObject::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsObject10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(Qt.GestureType)
  @overload(Qt.GestureType, Qt.GestureFlags)
  def grabGesture(
      self,
      type: Qt.GestureType,
      flags: Qt.GestureFlags = Qt.GestureFlags(),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsObject::grabGesture(Qt::GestureType type,
    Qt::GestureFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsobject.html#grabGesture

    Parameters
    ----------

    type : Qt.GestureType
      Passed on as its number.

    flags : Qt.GestureFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.GestureFlags().
    """
    #  void QGraphicsObject::grabGesture(Qt::GestureType type,
    #      Qt::GestureFlags flags)
    self.uglySide.call(
        'ritual_ZN15QGraphicsObject11grabGestureEN2Qt11GestureTypeE6QFlagsI'
        'NS0_11GestureFlagEE',
        type.value, flags.value,
    )

  @overload(Qt.GestureType)
  def ungrabGesture(self, type: Qt.GestureType) -> None:
    """
    Calls Qt's 'void QGraphicsObject::ungrabGesture(Qt::GestureType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsobject.html#ungrabGesture

    Parameters
    ----------

    type : Qt.GestureType
      Passed on as its number.
    """
    #  void QGraphicsObject::ungrabGesture(Qt::GestureType type)
    self.uglySide.call(
        'ritual_ZN15QGraphicsObject13ungrabGestureEN2Qt11GestureTypeE',
        type.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, ev: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsObject::event(QEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsobject.html#event

    Parameters
    ----------

    ev : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsObject::event(QEvent *ev)
    return self.uglySide.call(
        'ritual_own_ZN15QGraphicsObject5eventEP6QEvent', self._addressOf(ev),
    )
