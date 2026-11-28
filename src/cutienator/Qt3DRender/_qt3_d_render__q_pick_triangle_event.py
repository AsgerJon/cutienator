"""
Qt3DRender::QPickTriangleEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qpicktriangleevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPickTriangleEvent(Qt3DRender.QPickEvent):
  """
  The cute side of Qt's Qt3DRender::QPickTriangleEvent: a plain Python object
  standing in front of one C++ Qt3DRender::QPickTriangleEvent.

  It is built on the cute 'Qt3DRender::QPickEvent', as Qt's
  Qt3DRender::QPickTriangleEvent is built on Qt's Qt3DRender::QPickEvent, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QPickTriangleEvent that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'triangleIndex', 'vertex1Index', 'vertex2Index', 'vertex3Index', 'uvw',
  'd_func'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QPickTriangleEvent::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QPickTriangleEvent::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QPickTriangleEvent::~QPickTriangleEvent()': the
    destructor: Python never removes a C++ Qt3DRender::QPickTriangleEvent.
  - Qt's 'const QPickTriangleEventPrivate
    *Qt3DRender::QPickTriangleEvent::d_func() const': takes in Python what
    'QPickTriangleEventPrivate *Qt3DRender::QPickTriangleEvent::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QPickTriangleEvent is created at the first use, not
    by 'Qt3DRender::QPickTriangleEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QPickTriangleEvent.
  - Qt tells when it has removed the C++ Qt3DRender::QPickTriangleEvent.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DRender::QPickTriangleEvent::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html#tr

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
    #  QString Qt3DRender::QPickTriangleEvent::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender18QPickTriangleEvent2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QPickTriangleEvent'

  #  A C++ Qt3DRender::QPickTriangleEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QPickTriangleEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DRender::QPickTriangleEvent::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QPickTriangleEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QPickTriangleEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def triangleIndex(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QPickTriangleEvent::triangleIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html#triangleIndex
    """
    #  uint Qt3DRender::QPickTriangleEvent::triangleIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QPickTriangleEvent13triangleIndexEv',
    )

  def vertex1Index(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QPickTriangleEvent::vertex1Index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html#vertex1Index
    """
    #  uint Qt3DRender::QPickTriangleEvent::vertex1Index() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QPickTriangleEvent12vertex1IndexEv',
    )

  def vertex2Index(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QPickTriangleEvent::vertex2Index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html#vertex2Index
    """
    #  uint Qt3DRender::QPickTriangleEvent::vertex2Index() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QPickTriangleEvent12vertex2IndexEv',
    )

  def vertex3Index(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QPickTriangleEvent::vertex3Index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html#vertex3Index
    """
    #  uint Qt3DRender::QPickTriangleEvent::vertex3Index() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QPickTriangleEvent12vertex3IndexEv',
    )

  def uvw(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QPickTriangleEvent::uvw() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html#uvw

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QPickTriangleEvent::uvw() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QPickTriangleEvent3uvwEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

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
    'Qt3DRender::QPickTriangleEvent::QPickTriangleEvent()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html
    """
    #  Qt3DRender::QPickTriangleEvent::QPickTriangleEvent()
    self._noteCreation(QPickTriangleEvent, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender18QPickTriangleEventC1Ev',
    ))

  @overload(QPointF, QVector3D, QVector3D, float, int, int, int, int)
  def __init__(
      self,
      position: QPointF,
      worldIntersection: QVector3D,
      localIntersection: QVector3D,
      distance: float,
      triangleIndex: int,
      vertex1Index: int,
      vertex2Index: int,
      vertex3Index: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QPickTriangleEvent::QPickTriangleEvent(const QPointF
    &position, const QVector3D &worldIntersection, const QVector3D
    &localIntersection, float distance, uint triangleIndex, uint
    vertex1Index, uint vertex2Index, uint vertex3Index)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    worldIntersection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    localIntersection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    distance : float
      Passed on as it is.

    triangleIndex : int
      Passed on as it is.

    vertex1Index : int
      Passed on as it is.

    vertex2Index : int
      Passed on as it is.

    vertex3Index : int
      Passed on as it is.
    """
    #  Qt3DRender::QPickTriangleEvent::QPickTriangleEvent(const QPointF
    #      &position, const QVector3D &worldIntersection, const QVector3D
    #      &localIntersection, float distance, uint triangleIndex, uint
    #      vertex1Index, uint vertex2Index, uint vertex3Index)
    self._noteCreation(QPickTriangleEvent, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender18QPickTriangleEventC1ERK7QPointFRK9QVector3D'
        'S6_fjjjj',
        self._valueOf(position, 'QPointF'), self._valueOf(worldIntersection),
        self._valueOf(localIntersection), distance, triangleIndex,
        vertex1Index, vertex2Index, vertex3Index,
    ))

  @overload(
      QPointF, QVector3D, QVector3D, float, int, int, int, int,
      Qt3DRender.QPickEvent.Buttons, int, int, QVector3D,
  )
  def __init__(
      self,
      position: QPointF,
      worldIntersection: QVector3D,
      localIntersection: QVector3D,
      distance: float,
      triangleIndex: int,
      vertex1Index: int,
      vertex2Index: int,
      vertex3Index: int,
      button: Qt3DRender.QPickEvent.Buttons,
      buttons: int,
      modifiers: int,
      uvw: QVector3D,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QPickTriangleEvent::QPickTriangleEvent(const QPointF
    &position, const QVector3D &worldIntersection, const QVector3D
    &localIntersection, float distance, uint triangleIndex, uint
    vertex1Index, uint vertex2Index, uint vertex3Index, Buttons button, int
    buttons, int modifiers, const QVector3D &uvw)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    worldIntersection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    localIntersection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    distance : float
      Passed on as it is.

    triangleIndex : int
      Passed on as it is.

    vertex1Index : int
      Passed on as it is.

    vertex2Index : int
      Passed on as it is.

    vertex3Index : int
      Passed on as it is.

    button : Qt3DRender.QPickEvent.Buttons
      Passed on as its number.

    buttons : int
      Passed on as it is.

    modifiers : int
      Passed on as it is.

    uvw : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  Qt3DRender::QPickTriangleEvent::QPickTriangleEvent(const QPointF
    #      &position, const QVector3D &worldIntersection, const QVector3D
    #      &localIntersection, float distance, uint triangleIndex, uint
    #      vertex1Index, uint vertex2Index, uint vertex3Index, Buttons
    #      button, int buttons, int modifiers, const QVector3D &uvw)
    self._noteCreation(QPickTriangleEvent, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender18QPickTriangleEventC1ERK7QPointFRK9QVector3D'
        'S6_fjjjjNS_10QPickEvent7ButtonsEiiS6_',
        self._valueOf(position, 'QPointF'), self._valueOf(worldIntersection),
        self._valueOf(localIntersection), distance, triangleIndex,
        vertex1Index, vertex2Index, vertex3Index, button.value, buttons,
        modifiers, self._valueOf(uvw),
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

  def d_func(self) -> Optional[Qt3DRender.QPickTriangleEventPrivate]:
    """
    Calls Qt's 'QPickTriangleEventPrivate
    *Qt3DRender::QPickTriangleEvent::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleevent.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QPickTriangleEventPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPickTriangleEventPrivate *Qt3DRender::QPickTriangleEvent::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender18QPickTriangleEvent6d_funcEv',
    )
    return Qt3DRender.QPickTriangleEventPrivate._cuteAt(address)
