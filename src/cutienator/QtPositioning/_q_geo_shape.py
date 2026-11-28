"""
QGeoShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeoshape.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug
  from . import QGeoCoordinate, QGeoRectangle, QGeoShapePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoShapePrivate = WAIT['QGeoShapePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoShape(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoShape: a plain Python object standing in front of
  one C++ QGeoShape.

  C++ hands a QGeoShape around as a copy, so every C++ QGeoShape behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoShape that has a ritual and that Python can call
  so far, 13 names in all: 'type', 'isValid', 'isEmpty', 'contains',
  'boundingGeoRectangle', 'center', '__eq__', '__ne__', 'toString', 'equals',
  'd_func', '__rlshift__', 'debugStreaming'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoShape::~QGeoShape()': the destructor: Python removes its C++
    QGeoShape by it, and has no other use for it.
  - Qt's 'QGeoShape &QGeoShape::operator=(const QGeoShape &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'const QGeoShapePrivate *QGeoShape::d_func() const': takes in Python
    what 'QGeoShapePrivate *QGeoShape::d_func()' takes.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const QGeoShape
    &shape)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &stream, QGeoShape &shape)': an
    operator between other classes, written inside this one.
  - Qt's 'QDataStream &QGeoShape::dataStreamOut(QDataStream &stream, const
    QGeoShape &shape)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &QGeoShape::dataStreamIn(QDataStream &stream, QGeoShape
    &shape)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 26 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoShape is created at the first use, not by 'QGeoShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoShape back gives a copy the ritual made for
    Python, in a new cute QGeoShape.
  - Each name of Qt's QGeoShape that has no cute function yet,
    'dataStreamIn', 'dataStreamOut', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGeoShape, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ShapeType(CuteNum):
    """
    The enum 'QGeoShape::ShapeType' of Qt, with the 5 names Qt gives in it.
    """

    UnknownType = Kee[int](0)
    RectangleType = Kee[int](1)
    CircleType = Kee[int](2)
    PathType = Kee[int](3)
    PolygonType = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(lhs: QGeoShape, rhs: QGeoShape) -> bool:
    """
    Calls Qt's 'bool QGeoShape::equals(const QGeoShape &lhs, const QGeoShape
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#equals

    Parameters
    ----------

    lhs : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    rhs : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  bool QGeoShape::equals(const QGeoShape &lhs, const QGeoShape &rhs)
    return Rituals.call(
        'ritual_ZN9QGeoShape6equalsERKS_S1_',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  @staticmethod
  @overload(QDebug, THIS)
  def debugStreaming(dbg: QDebug, shape: QGeoShape) -> QDebug:
    """
    Calls Qt's 'QDebug QGeoShape::debugStreaming(QDebug dbg, const QGeoShape
    &shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#debugStreaming

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QGeoShape::debugStreaming(QDebug dbg, const QGeoShape &shape)
    address = Rituals.call(
        'ritual_ZN9QGeoShape14debugStreamingE6QDebugRKS_',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(shape),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoShape'

  #  Qt's '~QGeoShape()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoShape behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QGeoShapeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> ShapeType:
    """
    Calls Qt's 'ShapeType QGeoShape::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#type

    Returns
    -------

    ShapeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ShapeType(number)' gives.
    """
    #  ShapeType QGeoShape::type() const
    return QGeoShape.ShapeType(self.uglySide.call(
        'ritual_ZNK9QGeoShape4typeEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoShape::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#isValid
    """
    #  bool QGeoShape::isValid() const
    return self.uglySide.call('ritual_ZNK9QGeoShape7isValidEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGeoShape::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#isEmpty
    """
    #  bool QGeoShape::isEmpty() const
    return self.uglySide.call('ritual_ZNK9QGeoShape7isEmptyEv')

  @overload(QGeoCoordinate)
  def contains(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoShape::contains(const QGeoCoordinate &coordinate)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#contains

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoShape::contains(const QGeoCoordinate &coordinate) const
    return self.uglySide.call(
        'ritual_ZNK9QGeoShape8containsERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  def boundingGeoRectangle(self) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoShape::boundingGeoRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoshape.html#boundingGeoRectangle

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoShape::boundingGeoRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK9QGeoShape20boundingGeoRectangleEv',
    )
    from . import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoShape::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoShape::center() const
    address = self.uglySide.call('ritual_ZNK9QGeoShape6centerEv')
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QGeoShape::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoShape::toString() const
    return self.uglySide.call('ritual_ZNK9QGeoShape8toStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoShape) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoShape &lhs, const QGeoShape &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#operator==

    Parameters
    ----------

    rhs : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  bool operator==(const QGeoShape &lhs, const QGeoShape &rhs)
    return Rituals.call(
        'ritual_ZeqRK9QGeoShapeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QGeoShape) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoShape &lhs, const QGeoShape &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#operator!=

    Parameters
    ----------

    rhs : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  bool operator!=(const QGeoShape &lhs, const QGeoShape &rhs)
    return Rituals.call(
        'ritual_ZneRK9QGeoShapeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QGeoShape &shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QGeoShape &shape)
    address = Rituals.call(
        'ritual_Zls6QDebugRK9QGeoShape',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGeoShape::QGeoShape()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#QGeoShape
    """
    #  QGeoShape::QGeoShape()
    self._noteCreation(QGeoShape, lambda: Rituals.call(
        'ritual_ZN9QGeoShapeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoShape) -> None:
    """
    Notes what was given, for Qt's 'QGeoShape::QGeoShape(const QGeoShape
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#QGeoShape

    Parameters
    ----------

    other : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  QGeoShape::QGeoShape(const QGeoShape &other)
    self._noteCreation(QGeoShape, lambda: Rituals.call(
        'ritual_ZN9QGeoShapeC1ERKS_', self._valueOf(other),
    ))

  @overload(QGeoShapePrivate)
  @overload(NoneType)
  def __init__(self, d: Optional[QGeoShapePrivate]) -> None:
    """
    Notes what was given, for Qt's 'QGeoShape::QGeoShape(QGeoShapePrivate
    *d)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#QGeoShape

    Parameters
    ----------

    d : Optional[QGeoShapePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGeoShape::QGeoShape(QGeoShapePrivate *d)
    self._noteCreation(QGeoShape, lambda: Rituals.call(
        'ritual_ZN9QGeoShapeC1EP16QGeoShapePrivate', self._addressOf(d),
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

  def d_func(self) -> Optional[QGeoShapePrivate]:
    """
    Calls Qt's 'QGeoShapePrivate *QGeoShape::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoshape.html#d_func

    Returns
    -------

    Optional[QGeoShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoShapePrivate *QGeoShape::d_func()
    address = self.uglySide.call('ritual_ZN9QGeoShape6d_funcEv')
    from . import QGeoShapePrivate
    return QGeoShapePrivate._cuteAt(address)

  @staticmethod
  def dataStreamIn(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QGeoShape::dataStreamIn(QDataStream &stream, QGeoShape
    &shape)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoShape.dataStreamIn' has no cute function yet. Qt's "
        "'QDataStream &QGeoShape::dataStreamIn(QDataStream &stream, "
        "QGeoShape &shape)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def dataStreamOut(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QGeoShape::dataStreamOut(QDataStream &stream, const
    QGeoShape &shape)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoShape.dataStreamOut' has no cute function yet. Qt's "
        "'QDataStream &QGeoShape::dataStreamOut(QDataStream &stream, const "
        "QGeoShape &shape)': takes a type Python has no way to hand over "
        "yet.")
