"""
QSize binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qsize.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QMargins, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMargins = WAIT['QMargins']


class QSize(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSize: a plain Python object standing in front of one
  C++ QSize.

  C++ hands a QSize around as a copy, so every C++ QSize behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSize that has a ritual and that Python can call so
  far, 27 names in all: 'isNull', 'isEmpty', 'isValid', 'width', 'height',
  'setWidth', 'setHeight', 'transpose', 'transposed', 'scale', 'scaled',
  'expandedTo', 'boundedTo', 'grownBy', 'shrunkBy', '__iadd__', '__isub__',
  '__imul__', '__itruediv__', '__eq__', '__ne__', '__add__', '__sub__',
  '__mul__', '__rmul__', '__truediv__', 'toSizeF'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSize::QSize(Representation w, Representation h)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSize::~QSize()': the destructor: Python removes its C++ QSize by
    it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 35 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QSize is created at the first use, not by 'QSize(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSize back gives a copy the ritual made for Python,
    in a new cute QSize.
  - Each name of Qt's QSize that has no cute function yet, 'rheight',
    'rwidth', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSize'

  #  Qt's '~QSize()'. Naming it makes this a value class: Python owns every
  #  C++ QSize behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QSizeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSize::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#isNull
    """
    #  bool QSize::isNull() const
    return self.uglySide.call('ritual_ZNK5QSize6isNullEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSize::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#isEmpty
    """
    #  bool QSize::isEmpty() const
    return self.uglySide.call('ritual_ZNK5QSize7isEmptyEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSize::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#isValid
    """
    #  bool QSize::isValid() const
    return self.uglySide.call('ritual_ZNK5QSize7isValidEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QSize::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#width
    """
    #  int QSize::width() const
    return self.uglySide.call('ritual_ZNK5QSize5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QSize::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#height
    """
    #  int QSize::height() const
    return self.uglySide.call('ritual_ZNK5QSize6heightEv')

  def transposed(self) -> QSize:
    """
    Calls Qt's 'QSize QSize::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#transposed

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::transposed() const
    address = self.uglySide.call('ritual_ZNK5QSize10transposedEv')
    return QSize._cuteOwning(address)

  @overload(int, int, Qt.AspectRatioMode)
  def scaled(self, w: int, h: int, mode: Qt.AspectRatioMode) -> QSize:
    """
    Calls Qt's 'QSize QSize::scaled(int w, int h, Qt::AspectRatioMode mode)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#scaled

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    mode : Qt.AspectRatioMode
      Passed on as its number.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::scaled(int w, int h, Qt::AspectRatioMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize6scaledEiiN2Qt15AspectRatioModeE', w, h, mode.value,
    )
    return QSize._cuteOwning(address)

  @overload(THIS, Qt.AspectRatioMode)
  def scaled(self, s: QSize, mode: Qt.AspectRatioMode) -> QSize:
    """
    Calls Qt's 'QSize QSize::scaled(const QSize &s, Qt::AspectRatioMode mode)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#scaled

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : Qt.AspectRatioMode
      Passed on as its number.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::scaled(const QSize &s, Qt::AspectRatioMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize6scaledERKS_N2Qt15AspectRatioModeE',
        self._valueOf(s), mode.value,
    )
    return QSize._cuteOwning(address)

  @overload(THIS)
  def expandedTo(self, a0: QSize) -> QSize:
    """
    Calls Qt's 'QSize QSize::expandedTo(const QSize &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#expandedTo

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::expandedTo(const QSize &a0) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize10expandedToERKS_', self._valueOf(a0),
    )
    return QSize._cuteOwning(address)

  @overload(THIS)
  def boundedTo(self, a0: QSize) -> QSize:
    """
    Calls Qt's 'QSize QSize::boundedTo(const QSize &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#boundedTo

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::boundedTo(const QSize &a0) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize9boundedToERKS_', self._valueOf(a0),
    )
    return QSize._cuteOwning(address)

  @overload(QMargins)
  def grownBy(self, m: QMargins) -> QSize:
    """
    Calls Qt's 'QSize QSize::grownBy(QMargins m) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#grownBy

    Parameters
    ----------

    m : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::grownBy(QMargins m) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize7grownByE8QMargins', self._valueOf(m, 'QMargins'),
    )
    return QSize._cuteOwning(address)

  @overload(QMargins)
  def shrunkBy(self, m: QMargins) -> QSize:
    """
    Calls Qt's 'QSize QSize::shrunkBy(QMargins m) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#shrunkBy

    Parameters
    ----------

    m : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::shrunkBy(QMargins m) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize8shrunkByE8QMargins', self._valueOf(m, 'QMargins'),
    )
    return QSize._cuteOwning(address)

  def toSizeF(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QSize::toSizeF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#toSizeF

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QSize::toSizeF() const
    address = self.uglySide.call('ritual_ZNK5QSize7toSizeFEv')
    from . import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setWidth(self, w: int) -> None:
    """
    Calls Qt's 'void QSize::setWidth(int w)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#setWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void QSize::setWidth(int w)
    self.uglySide.call('ritual_ZN5QSize8setWidthEi', w)

  @overload(int)
  def setHeight(self, h: int) -> None:
    """
    Calls Qt's 'void QSize::setHeight(int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#setHeight

    Parameters
    ----------

    h : int
      Passed on as it is.
    """
    #  void QSize::setHeight(int h)
    self.uglySide.call('ritual_ZN5QSize9setHeightEi', h)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __iadd__(self, a0: QSize) -> QSize:
    """
    Calls Qt's 'QSize &QSize::operator+=(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator+=

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QSize &QSize::operator+=(const QSize &a0)
    self.uglySide.call('ritual_ZN5QSizepLERKS_', self._valueOf(a0))
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __isub__(self, a0: QSize) -> QSize:
    """
    Calls Qt's 'QSize &QSize::operator-=(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator-=

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QSize &QSize::operator-=(const QSize &a0)
    self.uglySide.call('ritual_ZN5QSizemIERKS_', self._valueOf(a0))
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __imul__(self, c: float) -> QSize:
    """
    Calls Qt's 'QSize &QSize::operator*=(qreal c)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator*=

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  QSize &QSize::operator*=(qreal c)
    self.uglySide.call('ritual_ZN5QSizemLEd', c)
    return self

  @overload.fallback
  def __imul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __itruediv__(self, c: float) -> QSize:
    """
    Calls Qt's 'QSize &QSize::operator/=(qreal c)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator/=

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  QSize &QSize::operator/=(qreal c)
    self.uglySide.call('ritual_ZN5QSizedVEd', c)
    return self

  @overload.fallback
  def __itruediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QSize) -> bool:
    """
    Calls Qt's 'bool operator==(const QSize &lhs, const QSize &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator==

    Parameters
    ----------

    rhs : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  bool operator==(const QSize &lhs, const QSize &rhs)
    return Rituals.call(
        'ritual_ZeqRK5QSizeS1_',
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
  def __ne__(self, rhs: QSize) -> bool:
    """
    Calls Qt's 'bool operator!=(const QSize &lhs, const QSize &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator!=

    Parameters
    ----------

    rhs : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  bool operator!=(const QSize &lhs, const QSize &rhs)
    return Rituals.call(
        'ritual_ZneRK5QSizeS1_',
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

  @overload(THIS)
  def __add__(self, s2: QSize) -> QSize:
    """
    Calls Qt's 'QSize operator+(const QSize &s1, const QSize &s2)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator+

    Parameters
    ----------

    s2 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize operator+(const QSize &s1, const QSize &s2)
    address = Rituals.call(
        'ritual_ZplRK5QSizeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(s2),
    )
    return QSize._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, s2: QSize) -> QSize:
    """
    Calls Qt's 'QSize operator-(const QSize &s1, const QSize &s2)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator-

    Parameters
    ----------

    s2 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize operator-(const QSize &s1, const QSize &s2)
    address = Rituals.call(
        'ritual_ZmiRK5QSizeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(s2),
    )
    return QSize._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __mul__(self, c: float) -> QSize:
    """
    Calls Qt's 'QSize operator*(const QSize &s, qreal c)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator*

    Parameters
    ----------

    c : float
      Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize operator*(const QSize &s, qreal c)
    address = Rituals.call(
        'ritual_ZmlRK5QSized', CuteMixin._valueOf(self), c,
    )
    return QSize._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __rmul__(self, c: float) -> QSize:
    """
    Calls Qt's 'QSize operator*(qreal c, const QSize &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator*

    Parameters
    ----------

    c : float
      Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize operator*(qreal c, const QSize &s)
    address = Rituals.call(
        'ritual_ZmldRK5QSize', c, CuteMixin._valueOf(self),
    )
    return QSize._cuteOwning(address)

  @overload.fallback
  def __rmul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __truediv__(self, c: float) -> QSize:
    """
    Calls Qt's 'QSize operator/(const QSize &s, qreal c)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#operator/

    Parameters
    ----------

    c : float
      Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize operator/(const QSize &s, qreal c)
    address = Rituals.call(
        'ritual_ZdvRK5QSized', CuteMixin._valueOf(self), c,
    )
    return QSize._cuteOwning(address)

  @overload.fallback
  def __truediv__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QSize::QSize()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#QSize
    """
    #  QSize::QSize()
    self._noteCreation(QSize, lambda: Rituals.call('ritual_ZN5QSizeC1Ev'))

  @overload(int, int)
  def __init__(self, w: int, h: int) -> None:
    """
    Notes what was given, for Qt's 'QSize::QSize(int w, int h)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#QSize

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  QSize::QSize(int w, int h)
    self._noteCreation(QSize, lambda: Rituals.call(
        'ritual_ZN5QSizeC1Eii', w, h,
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

  def transpose(self) -> None:
    """
    Calls Qt's 'void QSize::transpose()'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#transpose
    """
    #  void QSize::transpose()
    self.uglySide.call('ritual_ZN5QSize9transposeEv')

  @overload(int, int, Qt.AspectRatioMode)
  def scale(self, w: int, h: int, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void QSize::scale(int w, int h, Qt::AspectRatioMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#scale

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QSize::scale(int w, int h, Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN5QSize5scaleEiiN2Qt15AspectRatioModeE', w, h, mode.value,
    )

  @overload(THIS, Qt.AspectRatioMode)
  def scale(self, s: QSize, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void QSize::scale(const QSize &s, Qt::AspectRatioMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#scale

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QSize::scale(const QSize &s, Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN5QSize5scaleERKS_N2Qt15AspectRatioModeE',
        self._valueOf(s), mode.value,
    )

  @staticmethod
  def rheight(*__, **_) -> Never:
    """
    Qt's 'int &QSize::rheight()': takes or gives a type that cannot be passed
    yet: int &.
    """
    raise NotImplementedError(
        "'QSize.rheight' has no cute function yet. Qt's 'int "
        "&QSize::rheight()': takes or gives a type that cannot be passed "
        "yet: int &.")

  @staticmethod
  def rwidth(*__, **_) -> Never:
    """
    Qt's 'int &QSize::rwidth()': takes or gives a type that cannot be passed
    yet: int &.
    """
    raise NotImplementedError(
        "'QSize.rwidth' has no cute function yet. Qt's 'int "
        "&QSize::rwidth()': takes or gives a type that cannot be passed "
        "yet: int &.")


#  Qt's 'QList<QSize>': the list of QSize, which 'QList[QSize]' gives. It is
#  made here, so that there is one as soon as there can be a QSize.
QList.createKind(
    QSize, 'value',
    make='ritual_list_make_QSize',
    add='ritual_list_add_QSize',
    size='ritual_list_size_QSize',
    at='ritual_list_at_QSize',
    drop='ritual_list_drop_QSize',
)
