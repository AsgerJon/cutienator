"""
Qt3DRender::QPickEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qpickevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore
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


class QPickEvent(QObject):
  """
  The cute side of Qt's Qt3DRender::QPickEvent: a plain Python object
  standing in front of one C++ Qt3DRender::QPickEvent.

  It is built on the cute 'QObject', as Qt's Qt3DRender::QPickEvent is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QPickEvent that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'isAccepted',
  'setAccepted', 'position', 'distance', 'worldIntersection',
  'localIntersection', 'button', 'buttons', 'modifiers', 'viewport',
  'entity', 'acceptedChanged', 'd_func'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QPickEvent::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QPickEvent::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QPickEvent::~QPickEvent()': the destructor: Python
    never removes a C++ Qt3DRender::QPickEvent.
  - Qt's 'Qt3DRender::QPickEvent::QPickEvent(QObjectPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QPickEventPrivate *Qt3DRender::QPickEvent::d_func() const':
    takes in Python what 'QPickEventPrivate
    *Qt3DRender::QPickEvent::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QPickEvent is created at the first use, not by
    'Qt3DRender::QPickEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QPickEvent.
  - Qt tells when it has removed the C++ Qt3DRender::QPickEvent. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QPickEvent, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Buttons(CuteNum):
    """
    The enum 'Qt3DRender::QPickEvent::Buttons' of Qt, with the 5 names Qt
    gives in it.
    """

    LeftButton = Kee[int](1)
    RightButton = Kee[int](2)
    MiddleButton = Kee[int](4)
    BackButton = Kee[int](8)
    NoButton = Kee[int](0)

  class Modifiers(CuteNum):
    """
    The enum 'Qt3DRender::QPickEvent::Modifiers' of Qt, with the 6 names Qt
    gives in it.
    """

    NoModifier = Kee[int](0)
    ShiftModifier = Kee[int](33554432)
    ControlModifier = Kee[int](67108864)
    AltModifier = Kee[int](134217728)
    MetaModifier = Kee[int](268435456)
    KeypadModifier = Kee[int](536870912)

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
    Calls Qt's 'QString Qt3DRender::QPickEvent::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qpickevent.html#tr

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
    #  QString Qt3DRender::QPickEvent::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QPickEvent2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QPickEvent'

  #  A C++ Qt3DRender::QPickEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QPickEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QPickEvent::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QPickEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QPickEvent::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#isAccepted
    """
    #  bool Qt3DRender::QPickEvent::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent10isAcceptedEv',
    )

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF Qt3DRender::QPickEvent::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF Qt3DRender::QPickEvent::position() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent8positionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def distance(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QPickEvent::distance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#distance
    """
    #  float Qt3DRender::QPickEvent::distance() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent8distanceEv',
    )

  def worldIntersection(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QPickEvent::worldIntersection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#worldIntersection

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QPickEvent::worldIntersection() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent17worldIntersectionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def localIntersection(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QPickEvent::localIntersection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#localIntersection

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QPickEvent::localIntersection() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent17localIntersectionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def button(self) -> Buttons:
    """
    Calls Qt's 'Buttons Qt3DRender::QPickEvent::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qpickevent.html#button

    Returns
    -------

    Buttons
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Buttons(number)' gives.
    """
    #  Buttons Qt3DRender::QPickEvent::button() const
    return QPickEvent.Buttons(self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent6buttonEv',
    ))

  def buttons(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QPickEvent::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qpickevent.html#buttons
    """
    #  int Qt3DRender::QPickEvent::buttons() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender10QPickEvent7buttonsEv')

  def modifiers(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QPickEvent::modifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#modifiers
    """
    #  int Qt3DRender::QPickEvent::modifiers() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent9modifiersEv',
    )

  def viewport(self) -> Optional[Qt3DRender.QViewport]:
    """
    Calls Qt's 'QViewport *Qt3DRender::QPickEvent::viewport() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#viewport

    Returns
    -------

    Optional[Qt3DRender.QViewport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QViewport *Qt3DRender::QPickEvent::viewport() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent8viewportEv',
    )
    return Qt3DRender.QViewport._cuteAt(address)

  def entity(self) -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'Qt3DCore::QEntity *Qt3DRender::QPickEvent::entity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qpickevent.html#entity

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QEntity *Qt3DRender::QPickEvent::entity() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QPickEvent6entityEv',
    )
    return Qt3DCore.QEntity._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPickEvent::setAccepted(bool accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QPickEvent::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QPickEvent11setAcceptedEb', accepted,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'Qt3DRender::QPickEvent::QPickEvent()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#QPickEvent
    """
    #  Qt3DRender::QPickEvent::QPickEvent()
    self._noteCreation(QPickEvent, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QPickEventC1Ev',
    ))

  @overload(QPointF, QVector3D, QVector3D, float)
  def __init__(
      self,
      position: QPointF,
      worldIntersection: QVector3D,
      localIntersection: QVector3D,
      distance: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'Qt3DRender::QPickEvent::QPickEvent(const
    QPointF &position, const QVector3D &worldIntersection, const QVector3D
    &localIntersection, float distance)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#QPickEvent

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
    """
    #  Qt3DRender::QPickEvent::QPickEvent(const QPointF &position, const
    #      QVector3D &worldIntersection, const QVector3D &localIntersection,
    #      float distance)
    self._noteCreation(QPickEvent, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QPickEventC1ERK7QPointFRK9QVector3DS6_f',
        self._valueOf(position, 'QPointF'), self._valueOf(worldIntersection),
        self._valueOf(localIntersection), distance,
    ))

  @overload(QPointF, QVector3D, QVector3D, float, Buttons, int, int)
  def __init__(
      self,
      position: QPointF,
      worldIntersection: QVector3D,
      localIntersection: QVector3D,
      distance: float,
      button: Buttons,
      buttons: int,
      modifiers: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'Qt3DRender::QPickEvent::QPickEvent(const
    QPointF &position, const QVector3D &worldIntersection, const QVector3D
    &localIntersection, float distance, Buttons button, int buttons, int
    modifiers)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#QPickEvent

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

    button : Buttons
      Passed on as its number.

    buttons : int
      Passed on as it is.

    modifiers : int
      Passed on as it is.
    """
    #  Qt3DRender::QPickEvent::QPickEvent(const QPointF &position, const
    #      QVector3D &worldIntersection, const QVector3D &localIntersection,
    #      float distance, Buttons button, int buttons, int modifiers)
    self._noteCreation(QPickEvent, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QPickEventC1ERK7QPointFRK9QVector3DS6_fNS0_'
        '7ButtonsEii',
        self._valueOf(position, 'QPointF'), self._valueOf(worldIntersection),
        self._valueOf(localIntersection), distance, button.value, buttons,
        modifiers,
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

  @overload(bool)
  def acceptedChanged(self, accepted: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPickEvent::acceptedChanged(bool accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpickevent.html#acceptedChanged

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QPickEvent::acceptedChanged(bool accepted)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QPickEvent15acceptedChangedEb', accepted,
    )

  def d_func(self) -> Optional[Qt3DRender.QPickEventPrivate]:
    """
    Calls Qt's 'QPickEventPrivate *Qt3DRender::QPickEvent::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qpickevent.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QPickEventPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPickEventPrivate *Qt3DRender::QPickEvent::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QPickEvent6d_funcEv',
    )
    return Qt3DRender.QPickEventPrivate._cuteAt(address)
