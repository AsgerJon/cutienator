"""
QSizeF binding of the Qt C++
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
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMarginsF, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMarginsF = WAIT['QMarginsF']
  QSize = WAIT['QSize']


class QSizeF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSizeF: a plain Python object standing in front of
  one C++ QSizeF.

  C++ hands a QSizeF around as a copy, so every C++ QSizeF behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSizeF that has a ritual and that Python can call so
  far, 16 names in all: 'isNull', 'isEmpty', 'isValid', 'width', 'height',
  'setWidth', 'setHeight', 'transpose', 'transposed', 'scale', 'scaled',
  'expandedTo', 'boundedTo', 'grownBy', 'shrunkBy', 'toSize'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSizeF::~QSizeF()': the destructor: Python removes its C++ QSizeF
    by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 28 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QSizeF is created at the first use, not by 'QSizeF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSizeF back gives a copy the ritual made for Python,
    in a new cute QSizeF.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSizeF'

  #  Qt's '~QSizeF()'. Naming it makes this a value class: Python owns every
  #  C++ QSizeF behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QSizeFD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSizeF::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#isNull
    """
    #  bool QSizeF::isNull() const
    return self.uglySide.call('ritual_ZNK6QSizeF6isNullEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSizeF::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#isEmpty
    """
    #  bool QSizeF::isEmpty() const
    return self.uglySide.call('ritual_ZNK6QSizeF7isEmptyEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSizeF::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#isValid
    """
    #  bool QSizeF::isValid() const
    return self.uglySide.call('ritual_ZNK6QSizeF7isValidEv')

  def width(self) -> float:
    """
    Calls Qt's 'qreal QSizeF::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#width
    """
    #  qreal QSizeF::width() const
    return self.uglySide.call('ritual_ZNK6QSizeF5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QSizeF::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#height
    """
    #  qreal QSizeF::height() const
    return self.uglySide.call('ritual_ZNK6QSizeF6heightEv')

  def transposed(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QSizeF::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#transposed

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QSizeF::transposed() const
    address = self.uglySide.call('ritual_ZNK6QSizeF10transposedEv')
    return QSizeF._cuteOwning(address)

  @overload(float, float, Qt.AspectRatioMode)
  def scaled(self, w: float, h: float, mode: Qt.AspectRatioMode) -> QSizeF:
    """
    Calls Qt's 'QSizeF QSizeF::scaled(qreal w, qreal h, Qt::AspectRatioMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#scaled

    Parameters
    ----------

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    mode : Qt.AspectRatioMode
      Passed on as its number.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QSizeF::scaled(qreal w, qreal h, Qt::AspectRatioMode mode)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QSizeF6scaledEddN2Qt15AspectRatioModeE',
        w, h, mode.value,
    )
    return QSizeF._cuteOwning(address)

  @overload(THIS, Qt.AspectRatioMode)
  def scaled(self, s: QSizeF, mode: Qt.AspectRatioMode) -> QSizeF:
    """
    Calls Qt's 'QSizeF QSizeF::scaled(const QSizeF &s, Qt::AspectRatioMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#scaled

    Parameters
    ----------

    s : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    mode : Qt.AspectRatioMode
      Passed on as its number.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QSizeF::scaled(const QSizeF &s, Qt::AspectRatioMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK6QSizeF6scaledERKS_N2Qt15AspectRatioModeE',
        self._valueOf(s), mode.value,
    )
    return QSizeF._cuteOwning(address)

  @overload(THIS)
  def expandedTo(self, a0: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QSizeF::expandedTo(const QSizeF &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#expandedTo

    Parameters
    ----------

    a0 : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QSizeF::expandedTo(const QSizeF &a0) const
    address = self.uglySide.call(
        'ritual_ZNK6QSizeF10expandedToERKS_', self._valueOf(a0),
    )
    return QSizeF._cuteOwning(address)

  @overload(THIS)
  def boundedTo(self, a0: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QSizeF::boundedTo(const QSizeF &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#boundedTo

    Parameters
    ----------

    a0 : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QSizeF::boundedTo(const QSizeF &a0) const
    address = self.uglySide.call(
        'ritual_ZNK6QSizeF9boundedToERKS_', self._valueOf(a0),
    )
    return QSizeF._cuteOwning(address)

  @overload(QMarginsF)
  def grownBy(self, m: QMarginsF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QSizeF::grownBy(QMarginsF m) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#grownBy

    Parameters
    ----------

    m : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QSizeF::grownBy(QMarginsF m) const
    address = self.uglySide.call(
        'ritual_ZNK6QSizeF7grownByE9QMarginsF', self._valueOf(m),
    )
    return QSizeF._cuteOwning(address)

  @overload(QMarginsF)
  def shrunkBy(self, m: QMarginsF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QSizeF::shrunkBy(QMarginsF m) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#shrunkBy

    Parameters
    ----------

    m : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QSizeF::shrunkBy(QMarginsF m) const
    address = self.uglySide.call(
        'ritual_ZNK6QSizeF8shrunkByE9QMarginsF', self._valueOf(m),
    )
    return QSizeF._cuteOwning(address)

  def toSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSizeF::toSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#toSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSizeF::toSize() const
    address = self.uglySide.call('ritual_ZNK6QSizeF6toSizeEv')
    from . import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, w: float) -> None:
    """
    Calls Qt's 'void QSizeF::setWidth(qreal w)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#setWidth

    Parameters
    ----------

    w : float
      Passed on as it is.
    """
    #  void QSizeF::setWidth(qreal w)
    self.uglySide.call('ritual_ZN6QSizeF8setWidthEd', w)

  @overload(float)
  def setHeight(self, h: float) -> None:
    """
    Calls Qt's 'void QSizeF::setHeight(qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#setHeight

    Parameters
    ----------

    h : float
      Passed on as it is.
    """
    #  void QSizeF::setHeight(qreal h)
    self.uglySide.call('ritual_ZN6QSizeF9setHeightEd', h)

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
    Notes what was given, for Qt's 'QSizeF::QSizeF()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#QSizeF
    """
    #  QSizeF::QSizeF()
    self._noteCreation(QSizeF, lambda: Rituals.call('ritual_ZN6QSizeFC1Ev'))

  @overload(QSize)
  def __init__(self, sz: QSize) -> None:
    """
    Notes what was given, for Qt's 'QSizeF::QSizeF(const QSize &sz)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#QSizeF

    Parameters
    ----------

    sz : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QSizeF::QSizeF(const QSize &sz)
    self._noteCreation(QSizeF, lambda: Rituals.call(
        'ritual_ZN6QSizeFC1ERK5QSize', self._valueOf(sz),
    ))

  @overload(float, float)
  def __init__(self, w: float, h: float) -> None:
    """
    Notes what was given, for Qt's 'QSizeF::QSizeF(qreal w, qreal h)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#QSizeF

    Parameters
    ----------

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  QSizeF::QSizeF(qreal w, qreal h)
    self._noteCreation(QSizeF, lambda: Rituals.call(
        'ritual_ZN6QSizeFC1Edd', w, h,
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
    Calls Qt's 'void QSizeF::transpose()'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#transpose
    """
    #  void QSizeF::transpose()
    self.uglySide.call('ritual_ZN6QSizeF9transposeEv')

  @overload(float, float, Qt.AspectRatioMode)
  def scale(self, w: float, h: float, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void QSizeF::scale(qreal w, qreal h, Qt::AspectRatioMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#scale

    Parameters
    ----------

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QSizeF::scale(qreal w, qreal h, Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN6QSizeF5scaleEddN2Qt15AspectRatioModeE', w, h, mode.value,
    )

  @overload(THIS, Qt.AspectRatioMode)
  def scale(self, s: QSizeF, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void QSizeF::scale(const QSizeF &s, Qt::AspectRatioMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizef.html#scale

    Parameters
    ----------

    s : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QSizeF::scale(const QSizeF &s, Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN6QSizeF5scaleERKS_N2Qt15AspectRatioModeE',
        self._valueOf(s), mode.value,
    )
