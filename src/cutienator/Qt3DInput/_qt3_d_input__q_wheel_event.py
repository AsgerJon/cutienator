"""
Qt3DInput::QWheelEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qmouseevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QEvent, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWheelEvent(QObject):
  """
  The cute side of Qt's Qt3DInput::QWheelEvent: a plain Python object
  standing in front of one C++ Qt3DInput::QWheelEvent.

  It is built on the cute 'QObject', as Qt's Qt3DInput::QWheelEvent is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QWheelEvent that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'x', 'y',
  'angleDelta', 'buttons', 'modifiers', 'isAccepted', 'setAccepted', 'type'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QWheelEvent::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DInput::QWheelEvent::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QWheelEvent::~QWheelEvent()': the destructor: Python
    never removes a C++ Qt3DInput::QWheelEvent.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 2 not a gap; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DInput::QWheelEvent is created at the first use, not by
    'Qt3DInput::QWheelEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QWheelEvent.
  - Qt tells when it has removed the C++ Qt3DInput::QWheelEvent. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QWheelEvent that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside Qt3DInput::QWheelEvent, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Buttons(CuteNum):
    """
    The enum 'Qt3DInput::QWheelEvent::Buttons' of Qt, with the 5 names Qt
    gives in it.
    """

    LeftButton = Kee[int](1)
    RightButton = Kee[int](2)
    MiddleButton = Kee[int](4)
    BackButton = Kee[int](8)
    NoButton = Kee[int](0)

  class Modifiers(CuteNum):
    """
    The enum 'Qt3DInput::QWheelEvent::Modifiers' of Qt, with the 6 names Qt
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
    Calls Qt's 'QString Qt3DInput::QWheelEvent::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#tr

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
    #  QString Qt3DInput::QWheelEvent::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput11QWheelEvent2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QWheelEvent'

  #  A C++ Qt3DInput::QWheelEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QWheelEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QWheelEvent::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QWheelEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QWheelEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QWheelEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#x
    """
    #  int Qt3DInput::QWheelEvent::x() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput11QWheelEvent1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QWheelEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#y
    """
    #  int Qt3DInput::QWheelEvent::y() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput11QWheelEvent1yEv')

  def angleDelta(self) -> QPoint:
    """
    Calls Qt's 'QPoint Qt3DInput::QWheelEvent::angleDelta() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#angleDelta

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Qt3DInput::QWheelEvent::angleDelta() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QWheelEvent10angleDeltaEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def buttons(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QWheelEvent::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#buttons
    """
    #  int Qt3DInput::QWheelEvent::buttons() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput11QWheelEvent7buttonsEv')

  def modifiers(self) -> Modifiers:
    """
    Calls Qt's 'Modifiers Qt3DInput::QWheelEvent::modifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#modifiers

    Returns
    -------

    Modifiers
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Modifiers(number)' gives.
    """
    #  Modifiers Qt3DInput::QWheelEvent::modifiers() const
    return QWheelEvent.Modifiers(self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QWheelEvent9modifiersEv',
    ))

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QWheelEvent::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#isAccepted
    """
    #  bool Qt3DInput::QWheelEvent::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QWheelEvent10isAcceptedEv',
    )

  def type(self) -> QEvent.Type:
    """
    Calls Qt's 'QEvent::Type Qt3DInput::QWheelEvent::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#type

    Returns
    -------

    QEvent.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QEvent.Type(number)'
      gives.
    """
    #  QEvent::Type Qt3DInput::QWheelEvent::type() const
    return QEvent.Type(self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QWheelEvent4typeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QWheelEvent::setAccepted(bool accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qwheelevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QWheelEvent::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput11QWheelEvent11setAcceptedEb', accepted,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DInput::QWheelEvent::QWheelEvent(const ::QWheelEvent &e)': the
    compiler refuses its ritual as it would be written here: no matching
    constructor for initialization of 'CuteQt3DInput_QWheelEvent'.
    """
    raise NotImplementedError(
        "'Qt3DInput.QWheelEvent.__init__' has no cute function yet. Qt's "
        "'Qt3DInput::QWheelEvent::QWheelEvent(const ::QWheelEvent &e)': the "
        "compiler refuses its ritual as it would be written here: no "
        "matching constructor for initialization of "
        "'CuteQt3DInput_QWheelEvent'.")

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
