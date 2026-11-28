"""
QClipData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QClipData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect
  from . import QRegion
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']


class QClipData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QClipData: a plain Python object standing in front of
  one C++ QClipData.

  C++ hands a QClipData around as a copy, so every C++ QClipData behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QClipData that has a ritual and that Python can call
  so far, 6 names in all: 'initialize', 'clipLines', 'appendSpan',
  'setClipRect', 'setClipRegion', 'fixup'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QClipData::~QClipData()': the destructor: Python removes its C++
    QClipData by it, and has no other use for it.
  - Qt's 'QT_FT_Span *QClipData::spans()': gives 'struct QT_FT_Span_', which
    has no cute class yet.
  - Qt's 'void QClipData::appendSpans(const QT_FT_Span *s, int num)': names
    'QT_FT_Span', which has no cute class yet.

  What to expect
  --------------

  - The C++ QClipData is created at the first use, not by 'QClipData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QClipData back gives a copy the ritual made for
    Python, in a new cute QClipData.
  - Each name of Qt's QClipData that has no cute function yet, 'appendSpans',
    'spans', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QClipData, each a class in here as in C++.

  class ClipLine(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QClipData::ClipLine: a plain Python object standing
    in front of one C++ QClipData::ClipLine.

    C++ hands a QClipData::ClipLine around as a copy, so every C++
    QClipData::ClipLine behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QClipData::ClipLine yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QClipData::ClipLine::~ClipLine()': the destructor: Python removes
      its C++ QClipData::ClipLine by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QClipData::ClipLine is created at the first use, not by
      'QClipData::ClipLine(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QClipData::ClipLine back gives a copy the ritual
      made for Python, in a new cute QClipData::ClipLine.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QClipData::ClipLine'

    #  Qt's '~QClipData::ClipLine()'. Naming it makes this a value class:
    #  Python owns every C++ QClipData::ClipLine behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QClipData8ClipLineD1Ev'

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
  __qt_class__ = 'QClipData'

  #  Qt's '~QClipData()'. Naming it makes this a value class: Python owns
  #  every C++ QClipData behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QClipDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setClipRect(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QClipData::setClipRect(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipdata.html#setClipRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QClipData::setClipRect(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN9QClipData11setClipRectERK5QRect', self._valueOf(rect),
    )

  @overload(QRegion)
  def setClipRegion(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QClipData::setClipRegion(const QRegion &region)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipdata.html#setClipRegion

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QClipData::setClipRegion(const QRegion &region)
    self.uglySide.call(
        'ritual_ZN9QClipData13setClipRegionERK7QRegion',
        self._valueOf(region),
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

  @overload(int)
  def __init__(self, height: int) -> None:
    """
    Notes what was given, for Qt's 'QClipData::QClipData(int height)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qclipdata.html#QClipData

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  QClipData::QClipData(int height)
    self._noteCreation(QClipData, lambda: Rituals.call(
        'ritual_ZN9QClipDataC1Ei', height,
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void QClipData::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qclipdata.html#initialize
    """
    #  void QClipData::initialize()
    self.uglySide.call('ritual_ZN9QClipData10initializeEv')

  def clipLines(self) -> Optional[ClipLine]:
    """
    Calls Qt's 'ClipLine *QClipData::clipLines()'.

    Qt's own words: https://doc.qt.io/qt-6/qclipdata.html#clipLines

    Returns
    -------

    Optional[ClipLine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClipLine *QClipData::clipLines()
    address = self.uglySide.call('ritual_ZN9QClipData9clipLinesEv')
    return QClipData.ClipLine._cuteAt(address)

  @overload(int, int, int, int)
  def appendSpan(self, x: int, length: int, y: int, coverage: int) -> None:
    """
    Calls Qt's 'void QClipData::appendSpan(int x, int length, int y, int
    coverage)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipdata.html#appendSpan

    Parameters
    ----------

    x : int
      Passed on as it is.

    length : int
      Passed on as it is.

    y : int
      Passed on as it is.

    coverage : int
      Passed on as it is.
    """
    #  void QClipData::appendSpan(int x, int length, int y, int coverage)
    self.uglySide.call(
        'ritual_ZN9QClipData10appendSpanEiiii', x, length, y, coverage,
    )

  def fixup(self) -> None:
    """
    Calls Qt's 'void QClipData::fixup()'.

    Qt's own words: https://doc.qt.io/qt-6/qclipdata.html#fixup
    """
    #  void QClipData::fixup()
    self.uglySide.call('ritual_ZN9QClipData5fixupEv')

  @staticmethod
  def appendSpans(*__, **_) -> Never:
    """
    Qt's 'void QClipData::appendSpans(const QT_FT_Span *s, int num)': names
    'QT_FT_Span', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QClipData.appendSpans' has no cute function yet. Qt's 'void "
        "QClipData::appendSpans(const QT_FT_Span *s, int num)': names "
        "'QT_FT_Span', which has no cute class yet.")

  @staticmethod
  def spans(*__, **_) -> Never:
    """
    Qt's 'QT_FT_Span *QClipData::spans()': gives 'struct QT_FT_Span_', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QClipData.spans' has no cute function yet. Qt's 'QT_FT_Span "
        "*QClipData::spans()': gives 'struct QT_FT_Span_', which has no "
        "cute class yet.")
