"""
Qt3DInput::QMouseEvent binding of the Qt C++
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

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMouseEvent(QObject):
  """
  The cute side of Qt's Qt3DInput::QMouseEvent: a plain Python object
  standing in front of one C++ Qt3DInput::QMouseEvent.

  It is built on the cute 'QObject', as Qt's Qt3DInput::QMouseEvent is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QMouseEvent that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'x', 'y',
  'wasHeld', 'button', 'buttons', 'modifiers', 'isAccepted', 'setAccepted',
  'type'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QMouseEvent::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DInput::QMouseEvent::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QMouseEvent::~QMouseEvent()': the destructor: Python
    never removes a C++ Qt3DInput::QMouseEvent.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 2 not a gap; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DInput::QMouseEvent is created at the first use, not by
    'Qt3DInput::QMouseEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QMouseEvent.
  - Qt tells when it has removed the C++ Qt3DInput::QMouseEvent. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QMouseEvent that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside Qt3DInput::QMouseEvent, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Buttons(CuteNum):
    """
    The enum 'Qt3DInput::QMouseEvent::Buttons' of Qt, with the 5 names Qt
    gives in it.
    """

    LeftButton = Kee[int](1)
    RightButton = Kee[int](2)
    MiddleButton = Kee[int](4)
    BackButton = Kee[int](8)
    NoButton = Kee[int](0)

  class Modifiers(CuteNum):
    """
    The enum 'Qt3DInput::QMouseEvent::Modifiers' of Qt, with the 6 names Qt
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
    Calls Qt's 'QString Qt3DInput::QMouseEvent::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#tr

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
    #  QString Qt3DInput::QMouseEvent::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput11QMouseEvent2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QMouseEvent'

  #  A C++ Qt3DInput::QMouseEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QMouseEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QMouseEvent::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QMouseEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QMouseEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QMouseEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#x
    """
    #  int Qt3DInput::QMouseEvent::x() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput11QMouseEvent1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QMouseEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#y
    """
    #  int Qt3DInput::QMouseEvent::y() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput11QMouseEvent1yEv')

  def wasHeld(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QMouseEvent::wasHeld() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#wasHeld
    """
    #  bool Qt3DInput::QMouseEvent::wasHeld() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput11QMouseEvent7wasHeldEv')

  def button(self) -> Buttons:
    """
    Calls Qt's 'Buttons Qt3DInput::QMouseEvent::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#button

    Returns
    -------

    Buttons
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Buttons(number)' gives.
    """
    #  Buttons Qt3DInput::QMouseEvent::button() const
    return QMouseEvent.Buttons(self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QMouseEvent6buttonEv',
    ))

  def buttons(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QMouseEvent::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#buttons
    """
    #  int Qt3DInput::QMouseEvent::buttons() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput11QMouseEvent7buttonsEv')

  def modifiers(self) -> Modifiers:
    """
    Calls Qt's 'Modifiers Qt3DInput::QMouseEvent::modifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#modifiers

    Returns
    -------

    Modifiers
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Modifiers(number)' gives.
    """
    #  Modifiers Qt3DInput::QMouseEvent::modifiers() const
    return QMouseEvent.Modifiers(self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QMouseEvent9modifiersEv',
    ))

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QMouseEvent::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#isAccepted
    """
    #  bool Qt3DInput::QMouseEvent::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QMouseEvent10isAcceptedEv',
    )

  def type(self) -> QEvent.Type:
    """
    Calls Qt's 'QEvent::Type Qt3DInput::QMouseEvent::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#type

    Returns
    -------

    QEvent.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QEvent.Type(number)'
      gives.
    """
    #  QEvent::Type Qt3DInput::QMouseEvent::type() const
    return QEvent.Type(self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QMouseEvent4typeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QMouseEvent::setAccepted(bool accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qmouseevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QMouseEvent::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput11QMouseEvent11setAcceptedEb', accepted,
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
    Qt's 'Qt3DInput::QMouseEvent::QMouseEvent(const ::QMouseEvent &e)': the
    compiler refuses its ritual as it would be written here: no matching
    constructor for initialization of 'CuteQt3DInput_QMouseEvent'.
    """
    raise NotImplementedError(
        "'Qt3DInput.QMouseEvent.__init__' has no cute function yet. Qt's "
        "'Qt3DInput::QMouseEvent::QMouseEvent(const ::QMouseEvent &e)': the "
        "compiler refuses its ritual as it would be written here: no "
        "matching constructor for initialization of "
        "'CuteQt3DInput_QMouseEvent'.")

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
