"""
QInputMethodEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QInputMethodEvent(QEvent):
  """
  The cute side of Qt's QInputMethodEvent: a plain Python object standing in
  front of one C++ QInputMethodEvent.

  It is built on the cute 'QEvent', as Qt's QInputMethodEvent is built on
  Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputMethodEvent that has a ritual and that Python
  can call so far, 6 names in all: 'clone', 'setCommitString',
  'preeditString', 'commitString', 'replacementStart', 'replacementLength'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInputMethodEvent::~QInputMethodEvent()': the destructor: Python
    never removes a C++ QInputMethodEvent.
  - Qt's 'bool operator==(const QInputMethodEvent::Attribute &lhs, const
    QInputMethodEvent::Attribute &rhs)': an operator between other classes,
    written inside this one.
  - Qt's 'bool operator!=(const QInputMethodEvent::Attribute &lhs, const
    QInputMethodEvent::Attribute &rhs)': an operator between other classes,
    written inside this one.

  What has no ritual
  ------------------

  6 of the 16 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QInputMethodEvent is created at the first use, not by
    'QInputMethodEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputMethodEvent.
  """

  #  The enums Qt writes inside QInputMethodEvent, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AttributeType(CuteNum):
    """
    The enum 'QInputMethodEvent::AttributeType' of Qt, with the 6 names Qt
    gives in it.
    """

    TextFormat = Kee[int](0)
    Cursor = Kee[int](1)
    Language = Kee[int](2)
    Ruby = Kee[int](3)
    Selection = Kee[int](4)
    MimeData = Kee[int](5)

  #  The classes Qt writes inside QInputMethodEvent, each a class in here as
  #  in C++.

  class Attribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QInputMethodEvent::Attribute: a plain Python object
    standing in front of one C++ QInputMethodEvent::Attribute.

    C++ hands a QInputMethodEvent::Attribute around as a copy, so every C++
    QInputMethodEvent::Attribute behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QInputMethodEvent::Attribute yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QInputMethodEvent::Attribute::Attribute(AttributeType typ, int s,
      int l, QVariant val)': names the enum
      'QInputMethodEvent::AttributeType', whose class cannot be named here.
    - Qt's 'QInputMethodEvent::Attribute::Attribute(AttributeType typ, int s,
      int l)': names the enum 'QInputMethodEvent::AttributeType', whose class
      cannot be named here.
    - Qt's 'QInputMethodEvent::Attribute::~Attribute()': the destructor:
      Python removes its C++ QInputMethodEvent::Attribute by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QInputMethodEvent::Attribute is created at the first use, not
      by 'QInputMethodEvent::Attribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QInputMethodEvent::Attribute back gives a copy the
      ritual made for Python, in a new cute QInputMethodEvent::Attribute.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QInputMethodEvent::Attribute'

    #  Qt's '~QInputMethodEvent::Attribute()'. Naming it makes this a value
    #  class: Python owns every C++ QInputMethodEvent::Attribute behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QInputMethodEvent9AttributeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputMethodEvent'

  #  A C++ QInputMethodEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QInputMethodEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QInputMethodEvent]:
    """
    Calls Qt's 'QInputMethodEvent *QInputMethodEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethodevent.html#clone

    Returns
    -------

    Optional[QInputMethodEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputMethodEvent *QInputMethodEvent::clone() const
    ritual = 'ritual_ZNK17QInputMethodEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QInputMethodEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QInputMethodEvent._cuteAt(address)

  def preeditString(self) -> str:
    """
    Calls Qt's 'const QString &QInputMethodEvent::preeditString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#preeditString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QInputMethodEvent::preeditString() const
    return self.uglySide.call(
        'ritual_ZNK17QInputMethodEvent13preeditStringEv',
    )

  def commitString(self) -> str:
    """
    Calls Qt's 'const QString &QInputMethodEvent::commitString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#commitString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QInputMethodEvent::commitString() const
    return self.uglySide.call(
        'ritual_ZNK17QInputMethodEvent12commitStringEv',
    )

  def replacementStart(self) -> int:
    """
    Calls Qt's 'int QInputMethodEvent::replacementStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#replacementStart
    """
    #  int QInputMethodEvent::replacementStart() const
    return self.uglySide.call(
        'ritual_ZNK17QInputMethodEvent16replacementStartEv',
    )

  def replacementLength(self) -> int:
    """
    Calls Qt's 'int QInputMethodEvent::replacementLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#replacementLength
    """
    #  int QInputMethodEvent::replacementLength() const
    return self.uglySide.call(
        'ritual_ZNK17QInputMethodEvent17replacementLengthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, int)
  @overload(str, int, int)
  def setCommitString(
      self,
      commitString: str,
      replaceFrom: int = 0,
      replaceLength: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QInputMethodEvent::setCommitString(const QString
    &commitString, int replaceFrom, int replaceLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#setCommitString

    Parameters
    ----------

    commitString : str
      Passed on as it is: a QString is made of it for the call.

    replaceFrom : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    replaceLength : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QInputMethodEvent::setCommitString(const QString &commitString,
    #      int replaceFrom, int replaceLength)
    self.uglySide.call(
        'ritual_ZN17QInputMethodEvent15setCommitStringERK7QStringii',
        commitString, replaceFrom, replaceLength,
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
    Notes what was given, for Qt's 'QInputMethodEvent::QInputMethodEvent()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#QInputMethodEvent
    """
    #  QInputMethodEvent::QInputMethodEvent()
    self._noteCreation(QInputMethodEvent, lambda: Rituals.call(
        'ritual_ZN17QInputMethodEventC1Ev',
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
