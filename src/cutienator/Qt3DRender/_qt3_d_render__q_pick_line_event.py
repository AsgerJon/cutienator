"""
Qt3DRender::QPickLineEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qpicklineevent.h, Qt 6.12.0. Changes made here are lost.
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


class QPickLineEvent(Qt3DRender.QPickEvent):
  """
  The cute side of Qt's Qt3DRender::QPickLineEvent: a plain Python object
  standing in front of one C++ Qt3DRender::QPickLineEvent.

  It is built on the cute 'Qt3DRender::QPickEvent', as Qt's
  Qt3DRender::QPickLineEvent is built on Qt's Qt3DRender::QPickEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QPickLineEvent that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'edgeIndex', 'vertex1Index', 'vertex2Index'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QPickLineEvent::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QPickLineEvent::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QPickLineEvent::~QPickLineEvent()': the destructor:
    Python never removes a C++ Qt3DRender::QPickLineEvent.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::QPickLineEvent is created at the first use, not by
    'Qt3DRender::QPickLineEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QPickLineEvent.
  - Qt tells when it has removed the C++ Qt3DRender::QPickLineEvent. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DRender::QPickLineEvent::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qpicklineevent.html#tr

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
    #  QString Qt3DRender::QPickLineEvent::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QPickLineEvent2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QPickLineEvent'

  #  A C++ Qt3DRender::QPickLineEvent Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QPickLineEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QPickLineEvent::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicklineevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QPickLineEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QPickLineEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def edgeIndex(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QPickLineEvent::edgeIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicklineevent.html#edgeIndex
    """
    #  uint Qt3DRender::QPickLineEvent::edgeIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QPickLineEvent9edgeIndexEv',
    )

  def vertex1Index(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QPickLineEvent::vertex1Index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicklineevent.html#vertex1Index
    """
    #  uint Qt3DRender::QPickLineEvent::vertex1Index() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QPickLineEvent12vertex1IndexEv',
    )

  def vertex2Index(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QPickLineEvent::vertex2Index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicklineevent.html#vertex2Index
    """
    #  uint Qt3DRender::QPickLineEvent::vertex2Index() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QPickLineEvent12vertex2IndexEv',
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
    'Qt3DRender::QPickLineEvent::QPickLineEvent()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicklineevent.html#QPickLineEvent
    """
    #  Qt3DRender::QPickLineEvent::QPickLineEvent()
    self._noteCreation(QPickLineEvent, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender14QPickLineEventC1Ev',
    ))

  @overload(
      QPointF, QVector3D, QVector3D, float, int, int, int,
      Qt3DRender.QPickEvent.Buttons, int, int,
  )
  def __init__(
      self,
      position: QPointF,
      worldIntersection: QVector3D,
      localIntersection: QVector3D,
      distance: float,
      edgeIndex: int,
      vertex1Index: int,
      vertex2Index: int,
      button: Qt3DRender.QPickEvent.Buttons,
      buttons: int,
      modifiers: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QPickLineEvent::QPickLineEvent(const QPointF &position,
    const QVector3D &worldIntersection, const QVector3D &localIntersection,
    float distance, uint edgeIndex, uint vertex1Index, uint vertex2Index,
    Buttons button, int buttons, int modifiers)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicklineevent.html#QPickLineEvent

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

    edgeIndex : int
      Passed on as it is.

    vertex1Index : int
      Passed on as it is.

    vertex2Index : int
      Passed on as it is.

    button : Qt3DRender.QPickEvent.Buttons
      Passed on as its number.

    buttons : int
      Passed on as it is.

    modifiers : int
      Passed on as it is.
    """
    #  Qt3DRender::QPickLineEvent::QPickLineEvent(const QPointF &position,
    #      const QVector3D &worldIntersection, const QVector3D
    #      &localIntersection, float distance, uint edgeIndex, uint
    #      vertex1Index, uint vertex2Index, Buttons button, int buttons, int
    #      modifiers)
    self._noteCreation(QPickLineEvent, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender14QPickLineEventC1ERK7QPointFRK9QVector3DS6_f'
        'jjjNS_10QPickEvent7ButtonsEii',
        self._valueOf(position, 'QPointF'), self._valueOf(worldIntersection),
        self._valueOf(localIntersection), distance, edgeIndex, vertex1Index,
        vertex2Index, button.value, buttons, modifiers,
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
