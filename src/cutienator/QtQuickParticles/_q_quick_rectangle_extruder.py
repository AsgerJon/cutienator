"""
QQuickRectangleExtruder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickrectangleextruder_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRectangleExtruder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickParticleExtruder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRectangleExtruder(QQuickParticleExtruder):
  """
  The cute side of Qt's QQuickRectangleExtruder: a plain Python object
  standing in front of one C++ QQuickRectangleExtruder.

  It is built on the cute 'QQuickParticleExtruder', as Qt's
  QQuickRectangleExtruder is built on Qt's QQuickParticleExtruder, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRectangleExtruder that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'extrude',
  'contains', 'fill', 'fillChanged', 'setFill'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRectangleExtruder::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickRectangleExtruder::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickRectangleExtruder is created at the first use, not by
    'QQuickRectangleExtruder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRectangleExtruder.
  - Qt tells when it has removed the C++ QQuickRectangleExtruder. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickRectangleExtruder::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleextruder.html#tr

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
    #  QString QQuickRectangleExtruder::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickRectangleExtruder2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRectangleExtruder'

  #  A C++ QQuickRectangleExtruder Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRectangleExtruder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRectangleExtruder::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleextruder.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRectangleExtruder::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickRectangleExtruder10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fill(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleExtruder::fill() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangleextruder.html#fill
    """
    #  bool QQuickRectangleExtruder::fill() const
    return self.uglySide.call('ritual_ZNK23QQuickRectangleExtruder4fillEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFill(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleExtruder::setFill(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleextruder.html#setFill

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickRectangleExtruder::setFill(bool arg)
    self.uglySide.call('ritual_ZN23QQuickRectangleExtruder7setFillEb', arg)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRectangleExtruder::QQuickRectangleExtruder(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleextruder.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRectangleExtruder::QQuickRectangleExtruder(QObject *parent)
    self._noteCreation(QQuickRectangleExtruder, lambda: Rituals.call(
        'ritual_ZN23QQuickRectangleExtruderC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QRectF)
  def extrude(self, a0: QRectF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickRectangleExtruder::extrude(const QRectF &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleextruder.html#extrude

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickRectangleExtruder::extrude(const QRectF &a0)
    ritual = 'ritual_ZN23QQuickRectangleExtruder7extrudeERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickRectangleExtruder7extrudeERK6QRectF'
    address = self.uglySide.call(ritual, self._valueOf(a0))
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRectF, QPointF)
  def contains(self, bounds: QRectF, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickRectangleExtruder::contains(const QRectF &bounds,
    const QPointF &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleextruder.html#contains

    Parameters
    ----------

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickRectangleExtruder::contains(const QRectF &bounds, const
    #      QPointF &point)
    ritual = (
        'ritual_ZN23QQuickRectangleExtruder8containsERK6QRectFRK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickRectangleExtruder8containsERK6QRectFRK7QPoi'
          'ntF')
    return self.uglySide.call(
        ritual, self._valueOf(bounds), self._valueOf(point, 'QPointF'),
    )

  @overload(bool)
  def fillChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangleExtruder::fillChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleextruder.html#fillChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickRectangleExtruder::fillChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangleExtruder11fillChangedEb', arg,
    )
