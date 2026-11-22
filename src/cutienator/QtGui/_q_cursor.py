"""
QCursor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qcursor.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
  from . import QBitmap, QPixmap, QScreen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBitmap = WAIT['QBitmap']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QScreen = WAIT['QScreen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCursor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCursor: a plain Python object standing in front of
  one C++ QCursor.

  C++ hands a QCursor around as a copy, so every C++ QCursor behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCursor that has a ritual and that Python can call
  so far, 10 names in all: 'shape', 'setShape', 'bitmap', 'mask', 'pixmap',
  'hotSpot', 'pos', 'setPos', '__eq__', '__ne__'. It can be made from Python,
  in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCursor::~QCursor()': the destructor: Python removes its C++
    QCursor by it, and has no other use for it.
  - Qt's 'QVariant QCursor::operator QVariant() const': an operator Python
    has no name for.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QCursor is created at the first use, not by 'QCursor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCursor back gives a copy the ritual made for Python,
    in a new cute QCursor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload()
  def pos() -> QPoint:
    """
    Calls Qt's 'QPoint QCursor::pos()'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QCursor::pos()
    address = Rituals.call('ritual_ZN7QCursor3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @staticmethod
  @overload(QScreen)
  @overload(NoneType)
  def pos(screen: Optional[QScreen]) -> QPoint:
    """
    Calls Qt's 'QPoint QCursor::pos(const QScreen *screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#pos

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QCursor::pos(const QScreen *screen)
    address = Rituals.call(
        'ritual_ZN7QCursor3posEPK7QScreen', CuteMixin._addressOf(screen),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @staticmethod
  @overload(int, int)
  def setPos(x: int, y: int) -> None:
    """
    Calls Qt's 'void QCursor::setPos(int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#setPos

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QCursor::setPos(int x, int y)
    Rituals.call('ritual_ZN7QCursor6setPosEii', x, y)

  @staticmethod
  @overload(QScreen, int, int)
  @overload(NoneType, int, int)
  def setPos(screen: Optional[QScreen], x: int, y: int) -> None:
    """
    Calls Qt's 'void QCursor::setPos(QScreen *screen, int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#setPos

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QCursor::setPos(QScreen *screen, int x, int y)
    Rituals.call(
        'ritual_ZN7QCursor6setPosEP7QScreenii',
        CuteMixin._addressOf(screen), x, y,
    )

  @staticmethod
  @overload(QPoint)
  def setPos(p: QPoint) -> None:
    """
    Calls Qt's 'void QCursor::setPos(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#setPos

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QCursor::setPos(const QPoint &p)
    Rituals.call('ritual_ZN7QCursor6setPosERK6QPoint', CuteMixin._valueOf(p))

  @staticmethod
  @overload(QScreen, QPoint)
  @overload(NoneType, QPoint)
  def setPos(screen: Optional[QScreen], p: QPoint) -> None:
    """
    Calls Qt's 'void QCursor::setPos(QScreen *screen, const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#setPos

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QCursor::setPos(QScreen *screen, const QPoint &p)
    Rituals.call(
        'ritual_ZN7QCursor6setPosEP7QScreenRK6QPoint',
        CuteMixin._addressOf(screen), CuteMixin._valueOf(p),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCursor'

  #  Qt's '~QCursor()'. Naming it makes this a value class: Python owns every
  #  C++ QCursor behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QCursorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def shape(self) -> Qt.CursorShape:
    """
    Calls Qt's 'Qt::CursorShape QCursor::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#shape

    Returns
    -------

    Qt.CursorShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CursorShape(number)'
      gives.
    """
    #  Qt::CursorShape QCursor::shape() const
    return Qt.CursorShape(self.uglySide.call('ritual_ZNK7QCursor5shapeEv'))

  @overload(Qt.ReturnByValueConstant)
  def bitmap(self, a0: Qt.ReturnByValueConstant) -> QBitmap:
    """
    Calls Qt's 'QBitmap QCursor::bitmap(Qt::ReturnByValueConstant a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#bitmap

    Parameters
    ----------

    a0 : Qt.ReturnByValueConstant
      Passed on as its number.

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QCursor::bitmap(Qt::ReturnByValueConstant a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QCursor6bitmapEN2Qt21ReturnByValueConstantE', a0.value,
    )
    from . import QBitmap
    return QBitmap._cuteOwning(address)

  @overload()
  def bitmap(self) -> QBitmap:
    """
    Calls Qt's 'QBitmap QCursor::bitmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#bitmap

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QCursor::bitmap() const
    address = self.uglySide.call('ritual_ZNK7QCursor6bitmapEv')
    from . import QBitmap
    return QBitmap._cuteOwning(address)

  @overload(Qt.ReturnByValueConstant)
  def mask(self, a0: Qt.ReturnByValueConstant) -> QBitmap:
    """
    Calls Qt's 'QBitmap QCursor::mask(Qt::ReturnByValueConstant a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#mask

    Parameters
    ----------

    a0 : Qt.ReturnByValueConstant
      Passed on as its number.

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QCursor::mask(Qt::ReturnByValueConstant a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QCursor4maskEN2Qt21ReturnByValueConstantE', a0.value,
    )
    from . import QBitmap
    return QBitmap._cuteOwning(address)

  @overload()
  def mask(self) -> QBitmap:
    """
    Calls Qt's 'QBitmap QCursor::mask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#mask

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QCursor::mask() const
    address = self.uglySide.call('ritual_ZNK7QCursor4maskEv')
    from . import QBitmap
    return QBitmap._cuteOwning(address)

  def pixmap(self) -> QPixmap:
    """
    Calls Qt's 'QPixmap QCursor::pixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#pixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QCursor::pixmap() const
    address = self.uglySide.call('ritual_ZNK7QCursor6pixmapEv')
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  def hotSpot(self) -> QPoint:
    """
    Calls Qt's 'QPoint QCursor::hotSpot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#hotSpot

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QCursor::hotSpot() const
    address = self.uglySide.call('ritual_ZNK7QCursor7hotSpotEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.CursorShape)
  def setShape(self, newShape: Qt.CursorShape) -> None:
    """
    Calls Qt's 'void QCursor::setShape(Qt::CursorShape newShape)'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#setShape

    Parameters
    ----------

    newShape : Qt.CursorShape
      Passed on as its number.
    """
    #  void QCursor::setShape(Qt::CursorShape newShape)
    self.uglySide.call(
        'ritual_ZN7QCursor8setShapeEN2Qt11CursorShapeE', newShape.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCursor) -> bool:
    """
    Calls Qt's 'bool operator==(const QCursor &lhs, const QCursor &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#operator==

    Parameters
    ----------

    rhs : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  bool operator==(const QCursor &lhs, const QCursor &rhs)
    return Rituals.call(
        'ritual_ZeqRK7QCursorS1_',
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
  def __ne__(self, rhs: QCursor) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCursor &lhs, const QCursor &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#operator!=

    Parameters
    ----------

    rhs : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  bool operator!=(const QCursor &lhs, const QCursor &rhs)
    return Rituals.call(
        'ritual_ZneRK7QCursorS1_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCursor::QCursor()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#QCursor
    """
    #  QCursor::QCursor()
    self._noteCreation(QCursor, lambda: Rituals.call(
        'ritual_ZN7QCursorC1Ev',
    ))

  @overload(Qt.CursorShape)
  def __init__(self, shape: Qt.CursorShape) -> None:
    """
    Notes what was given, for Qt's 'QCursor::QCursor(Qt::CursorShape shape)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#QCursor

    Parameters
    ----------

    shape : Qt.CursorShape
      Passed on as its number.
    """
    #  QCursor::QCursor(Qt::CursorShape shape)
    self._noteCreation(QCursor, lambda: Rituals.call(
        'ritual_ZN7QCursorC1EN2Qt11CursorShapeE', shape.value,
    ))

  @overload(QBitmap, QBitmap)
  @overload(QBitmap, QBitmap, int)
  @overload(QBitmap, QBitmap, int, int)
  def __init__(
      self,
      bitmap: QBitmap,
      mask: QBitmap,
      hotX: int = -1,
      hotY: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCursor::QCursor(const QBitmap &bitmap,
    const QBitmap &mask, int hotX, int hotY)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#QCursor

    Parameters
    ----------

    bitmap : QBitmap
      Passed on as a value: Qt reads the C++ QBitmap, which stays Python's
      own.

    mask : QBitmap
      Passed on as a value: Qt reads the C++ QBitmap, which stays Python's
      own.

    hotX : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    hotY : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QCursor::QCursor(const QBitmap &bitmap, const QBitmap &mask, int hotX,
    #      int hotY)
    self._noteCreation(QCursor, lambda: Rituals.call(
        'ritual_ZN7QCursorC1ERK7QBitmapS2_ii',
        self._valueOf(bitmap), self._valueOf(mask), hotX, hotY,
    ))

  @overload(QPixmap)
  @overload(QPixmap, int)
  @overload(QPixmap, int, int)
  def __init__(
      self,
      pixmap: QPixmap,
      hotX: int = -1,
      hotY: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCursor::QCursor(const QPixmap &pixmap,
    int hotX, int hotY)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#QCursor

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    hotX : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    hotY : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QCursor::QCursor(const QPixmap &pixmap, int hotX, int hotY)
    self._noteCreation(QCursor, lambda: Rituals.call(
        'ritual_ZN7QCursorC1ERK7QPixmapii',
        self._valueOf(pixmap), hotX, hotY,
    ))

  @overload(THIS)
  def __init__(self, cursor: QCursor) -> None:
    """
    Notes what was given, for Qt's 'QCursor::QCursor(const QCursor &cursor)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcursor.html#QCursor

    Parameters
    ----------

    cursor : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  QCursor::QCursor(const QCursor &cursor)
    self._noteCreation(QCursor, lambda: Rituals.call(
        'ritual_ZN7QCursorC1ERKS_', self._valueOf(cursor),
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
