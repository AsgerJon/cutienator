"""
QColormap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qcolormap.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QColormap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColormap: a plain Python object standing in front of
  one C++ QColormap.

  C++ hands a QColormap around as a copy, so every C++ QColormap behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColormap that has a ritual and that Python can call
  so far, 9 names in all: 'initialize', 'cleanup', 'instance', 'mode',
  'depth', 'size', 'pixel', 'colorAt', 'colormap'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColormap::~QColormap()': the destructor: Python removes its C++
    QColormap by it, and has no other use for it.
  - Qt's 'QColormap &QColormap::operator=(const QColormap &colormap)':
    assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QColormap is created at the first use, not by 'QColormap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColormap back gives a copy the ritual made for
    Python, in a new cute QColormap.
  """

  #  The enums Qt writes inside QColormap, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum):
    """The enum 'QColormap::Mode' of Qt, with the 3 names Qt gives in it."""

    Direct = Kee[int](0)
    Indexed = Kee[int](1)
    Gray = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def initialize() -> None:
    """
    Calls Qt's 'void QColormap::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#initialize
    """
    #  void QColormap::initialize()
    Rituals.call('ritual_ZN9QColormap10initializeEv')

  @staticmethod
  def cleanup() -> None:
    """
    Calls Qt's 'void QColormap::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#cleanup
    """
    #  void QColormap::cleanup()
    Rituals.call('ritual_ZN9QColormap7cleanupEv')

  @staticmethod
  @overload()
  @overload(int)
  def instance(screen: int = -1) -> QColormap:
    """
    Calls Qt's 'QColormap QColormap::instance(int screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#instance

    Parameters
    ----------

    screen : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QColormap
      A new cute QColormap around the copy Qt gave back. Python owns it.
    """
    #  QColormap QColormap::instance(int screen)
    address = Rituals.call('ritual_ZN9QColormap8instanceEi', screen)
    return QColormap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColormap'

  #  Qt's '~QColormap()'. Naming it makes this a value class: Python owns
  #  every C++ QColormap behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QColormapD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mode(self) -> Mode:
    """
    Calls Qt's 'Mode QColormap::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#mode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  Mode QColormap::mode() const
    return QColormap.Mode(self.uglySide.call('ritual_ZNK9QColormap4modeEv'))

  def depth(self) -> int:
    """
    Calls Qt's 'int QColormap::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#depth
    """
    #  int QColormap::depth() const
    return self.uglySide.call('ritual_ZNK9QColormap5depthEv')

  def size(self) -> int:
    """
    Calls Qt's 'int QColormap::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#size
    """
    #  int QColormap::size() const
    return self.uglySide.call('ritual_ZNK9QColormap4sizeEv')

  @overload(QColor)
  def pixel(self, color: QColor) -> int:
    """
    Calls Qt's 'uint QColormap::pixel(const QColor &color) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#pixel

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  uint QColormap::pixel(const QColor &color) const
    return self.uglySide.call(
        'ritual_ZNK9QColormap5pixelERK6QColor', self._valueOf(color),
    )

  @overload(int)
  def colorAt(self, pixel: int) -> QColor:
    """
    Calls Qt's 'const QColor QColormap::colorAt(uint pixel) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#colorAt

    Parameters
    ----------

    pixel : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor QColormap::colorAt(uint pixel) const
    address = self.uglySide.call('ritual_ZNK9QColormap7colorAtEj', pixel)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def colormap(self) -> QList[QColor]:
    """
    Calls Qt's 'const QList<QColor> QColormap::colormap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#colormap

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QColor> QColormap::colormap() const
    address = self.uglySide.call('ritual_ZNK9QColormap8colormapEv')
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

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

  @overload(THIS)
  def __init__(self, colormap: QColormap) -> None:
    """
    Notes what was given, for Qt's 'QColormap::QColormap(const QColormap
    &colormap)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#QColormap

    Parameters
    ----------

    colormap : QColormap
      Passed on as a value: Qt reads the C++ QColormap, which stays Python's
      own.
    """
    #  QColormap::QColormap(const QColormap &colormap)
    self._noteCreation(QColormap, lambda: Rituals.call(
        'ritual_ZN9QColormapC1ERKS_', self._valueOf(colormap),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QColormap::QColormap()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolormap.html#QColormap
    """
    #  QColormap::QColormap()
    self._noteCreation(QColormap, lambda: Rituals.call(
        'ritual_ZN9QColormapC1Ev',
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
