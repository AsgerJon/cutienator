"""
QSize binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from cutienator.cute._cute_mixin import CuteMixin
from cutienator.cute._meta_cute import MetaCute
from cutienator.occult._ugly import Ugly
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional, Tuple


class QSize(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSize: a plain Python object standing in front
  of one C++ QSize, which holds a width and a height.

    size = QSize(3, 4)
    size.width()                           # 3
    wide = size.expandedTo(QSize(5, 1))    # a new QSize
    wide.width(), wide.height()            # 5, 4

  This is the first value class written out from its ritual file. It is
  written by hand, in the shape a program is meant to write the others
  in.

  What a value class is
  ---------------------

  C++ hands a QSize around as a copy, where it hands a QObject around
  by its address. So every C++ QSize behind a cute QSize is Python's
  own: nothing in C++ knows of it.

  - 'QSize(3, 4)' makes one.
  - A function giving a QSize back, as 'expandedTo', gives a copy the
    ritual made for Python, in a new cute QSize.
  - A function taking a QSize, as 'expandedTo' again, is handed the
    address of Python's own, which Qt reads and copies if it keeps it.
  - When the cute QSize goes, its C++ QSize is removed, by the ritual
    named in '__delete_ritual__' below. As the program ends nothing is
    removed.

  What exists
  -----------

  Every function of Qt's QSize that has a ritual and takes and gives
  nothing but numbers and QSize, 13 names in all: 'isNull', 'isEmpty',
  'isValid', 'width', 'height', 'setWidth', 'setHeight', 'transpose',
  'transposed', 'scale', 'scaled', 'expandedTo' and 'boundedTo'.
  Creation takes a width and a height, or nothing.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'grownBy(QMargins m)' and 'shrunkBy(QMargins m)'. They take a
    QMargins, which has no cute class yet.
  - Qt's 'toSizeF()'. It gives a QSizeF, which has no cute class yet.
  - Qt's '~QSize()'. Python removes its C++ QSize by it, and has no
    other use for it.

  What has no ritual yet
  ----------------------

  7 of the 27 functions Qt declares: 'rwidth' and 'rheight', which give
  the number itself to be changed in place, and '+=', '-=', '*=' and
  '/=', which give the QSize itself back. Comparing two with '==' and
  adding two with '+' are no functions of the class in Qt, and are not
  there either.

  What to expect
  --------------

  - The C++ QSize is created at the first use, not by 'QSize(3, 4)'.
  - An enum of Qt is taken as its number: 'scaled(5, 5, 1)' is Qt's
    'Qt::KeepAspectRatio'.
  - A wrong argument is refused in Python, with 'DispatchException',
    and never reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Qt's '~QSize()'. Naming it makes this a value class: Python owns
  #  every C++ QSize behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QSizeD1Ev'

  #  Fallback Variables

  #  Private Variables
  #  The width and the height given to the constructor, kept until the
  #  C++ object is created. None when nothing was given.
  __given_size__: Optional[Tuple[int, int]] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _createUglySide(self, ) -> None:
    """
    Creates the C++ QSize and the Ugly standing for it, which removes
    the C++ QSize when it goes itself.

    'CuteMixin' calls this at the first read of 'uglySide'. The C++
    QSize is created with what was given to 'QSize(...)'.
    """
    if self.__given_size__ is None:
      #  QSize::QSize()
      address = Rituals.call('ritual_ZN5QSizeC1Ev')
    else:
      #  QSize::QSize(int w, int h)
      address = Rituals.call('ritual_ZN5QSizeC1Eii', *self.__given_size__)
    ugly = Ugly()
    ugly.setAddress(address)
    ugly.setDeleteRitual(self.__delete_ritual__)
    ugly.setCuteSide(self)
    self.__ugly_side__ = ugly

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

  @overload(int, int, int)
  def scaled(self, w: int, h: int, mode: int) -> QSize:
    """
    Calls Qt's 'QSize QSize::scaled(int w, int h, Qt::AspectRatioMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#scaled

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    mode : int
      The number of a 'Qt::AspectRatioMode', as 1 for
      'Qt::KeepAspectRatio'. Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::scaled(int w, int h, Qt::AspectRatioMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize6scaledEiiN2Qt15AspectRatioModeE', w, h, mode,
    )
    return QSize._cuteOwning(address)

  @overload(THIS, int)
  def scaled(self, s: QSize, mode: int) -> QSize:
    """
    Calls Qt's 'QSize QSize::scaled(const QSize &s, Qt::AspectRatioMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#scaled

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays
      Python's own.

    mode : int
      The number of a 'Qt::AspectRatioMode', as 1 for
      'Qt::KeepAspectRatio'. Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::scaled(const QSize &s, Qt::AspectRatioMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize6scaledERKS_N2Qt15AspectRatioModeE',
        self._valueOf(s), mode,
    )
    return QSize._cuteOwning(address)

  @overload(THIS)
  def expandedTo(self, otherSize: QSize) -> QSize:
    """
    Calls Qt's 'QSize QSize::expandedTo(const QSize &) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#expandedTo

    Parameters
    ----------

    otherSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::expandedTo(const QSize &) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize10expandedToERKS_', self._valueOf(otherSize),
    )
    return QSize._cuteOwning(address)

  @overload(THIS)
  def boundedTo(self, otherSize: QSize) -> QSize:
    """
    Calls Qt's 'QSize QSize::boundedTo(const QSize &) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#boundedTo

    Parameters
    ----------

    otherSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSize::boundedTo(const QSize &) const
    address = self.uglySide.call(
        'ritual_ZNK5QSize9boundedToERKS_', self._valueOf(otherSize),
    )
    return QSize._cuteOwning(address)

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes that nothing was given, for Qt's 'QSize::QSize()', which is
    called at the first use and makes a QSize that is not valid.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#QSize
    """
    self.__given_size__ = None

  @overload(int, int)
  def __init__(self, w: int, h: int) -> None:
    """
    Notes the width and the height for Qt's 'QSize::QSize(int w, int
    h)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#QSize

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    self.__given_size__ = (w, h)

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

  @overload(int, int, int)
  def scale(self, w: int, h: int, mode: int) -> None:
    """
    Calls Qt's 'void QSize::scale(int w, int h, Qt::AspectRatioMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#scale

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    mode : int
      The number of a 'Qt::AspectRatioMode', as 1 for
      'Qt::KeepAspectRatio'. Passed on as it is.
    """
    #  void QSize::scale(int w, int h, Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN5QSize5scaleEiiN2Qt15AspectRatioModeE', w, h, mode,
    )

  @overload(THIS, int)
  def scale(self, s: QSize, mode: int) -> None:
    """
    Calls Qt's 'void QSize::scale(const QSize &s, Qt::AspectRatioMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsize.html#scale

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays
      Python's own.

    mode : int
      The number of a 'Qt::AspectRatioMode', as 1 for
      'Qt::KeepAspectRatio'. Passed on as it is.
    """
    #  void QSize::scale(const QSize &s, Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN5QSize5scaleERKS_N2Qt15AspectRatioModeE',
        self._valueOf(s), mode,
    )
