"""
QValue3DAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qvalue3daxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstract3DAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QValue3DAxisFormatter, QValue3DAxisPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QValue3DAxisFormatter = WAIT['QtGraphs:QValue3DAxisFormatter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QValue3DAxis(QAbstract3DAxis):
  """
  The cute side of Qt's QValue3DAxis: a plain Python object standing in front
  of one C++ QValue3DAxis.

  It is built on the cute 'QAbstract3DAxis', as Qt's QValue3DAxis is built on
  Qt's QAbstract3DAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QValue3DAxis that has a ritual and that Python can
  call so far, 27 names in all: 'metaObject', 'tr', 'd_func',
  'setSegmentCount', 'segmentCount', 'setSubSegmentCount', 'subSegmentCount',
  'setLabelFormat', 'labelFormat', 'setFormatter', 'formatter',
  'setReversed', 'reversed', 'recalculate', 'gridSize', 'subGridSize',
  'gridPositionAt', 'subGridPositionAt', 'labelPositionAt', 'positionAt',
  'stringForValue', 'segmentCountChanged', 'subSegmentCountChanged',
  'labelFormatChanged', 'formatterChanged', 'reversedChanged',
  'formatterDirty'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QValue3DAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QValue3DAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QValue3DAxisPrivate *QValue3DAxis::d_func() const': takes in
    Python what 'QValue3DAxisPrivate *QValue3DAxis::d_func()' takes.
  - Qt's 'QValue3DAxis::~QValue3DAxis()': the destructor: Python never
    removes a C++ QValue3DAxis.

  What has no ritual
  ------------------

  4 of the 36 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QValue3DAxis is created at the first use, not by
    'QValue3DAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QValue3DAxis.
  - Qt tells when it has removed the C++ QValue3DAxis. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

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
    Calls Qt's 'QString QValue3DAxis::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#tr

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
    #  QString QValue3DAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QValue3DAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QValue3DAxis'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QValue3DAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QValue3DAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QValue3DAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QValue3DAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QValue3DAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def segmentCount(self) -> int:
    """
    Calls Qt's 'qsizetype QValue3DAxis::segmentCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#segmentCount
    """
    #  qsizetype QValue3DAxis::segmentCount() const
    return self.uglySide.call('ritual_ZNK12QValue3DAxis12segmentCountEv')

  def subSegmentCount(self) -> int:
    """
    Calls Qt's 'qsizetype QValue3DAxis::subSegmentCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#subSegmentCount
    """
    #  qsizetype QValue3DAxis::subSegmentCount() const
    return self.uglySide.call('ritual_ZNK12QValue3DAxis15subSegmentCountEv')

  def labelFormat(self) -> str:
    """
    Calls Qt's 'QString QValue3DAxis::labelFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#labelFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QValue3DAxis::labelFormat() const
    return self.uglySide.call('ritual_ZNK12QValue3DAxis11labelFormatEv')

  def formatter(self) -> Optional[QValue3DAxisFormatter]:
    """
    Calls Qt's 'QValue3DAxisFormatter *QValue3DAxis::formatter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#formatter

    Returns
    -------

    Optional[QValue3DAxisFormatter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxisFormatter *QValue3DAxis::formatter() const
    address = self.uglySide.call('ritual_ZNK12QValue3DAxis9formatterEv')
    from . import QValue3DAxisFormatter
    return QValue3DAxisFormatter._cuteAt(address)

  def reversed(self) -> bool:
    """
    Calls Qt's 'bool QValue3DAxis::reversed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#reversed
    """
    #  bool QValue3DAxis::reversed() const
    return self.uglySide.call('ritual_ZNK12QValue3DAxis8reversedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSegmentCount(self, count: int) -> None:
    """
    Calls Qt's 'void QValue3DAxis::setSegmentCount(qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#setSegmentCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QValue3DAxis::setSegmentCount(qsizetype count)
    self.uglySide.call('ritual_ZN12QValue3DAxis15setSegmentCountEx', count)

  @overload(int)
  def setSubSegmentCount(self, count: int) -> None:
    """
    Calls Qt's 'void QValue3DAxis::setSubSegmentCount(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxis.html#setSubSegmentCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QValue3DAxis::setSubSegmentCount(qsizetype count)
    self.uglySide.call(
        'ritual_ZN12QValue3DAxis18setSubSegmentCountEx', count,
    )

  @overload(str)
  def setLabelFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QValue3DAxis::setLabelFormat(const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#setLabelFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QValue3DAxis::setLabelFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN12QValue3DAxis14setLabelFormatERK7QString', format,
    )

  @overload(QValue3DAxisFormatter)
  @overload(NoneType)
  def setFormatter(self, formatter: Optional[QValue3DAxisFormatter]) -> None:
    """
    Calls Qt's 'void QValue3DAxis::setFormatter(QValue3DAxisFormatter
    *formatter)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#setFormatter

    Parameters
    ----------

    formatter : Optional[QValue3DAxisFormatter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QValue3DAxis::setFormatter(QValue3DAxisFormatter *formatter)
    self.uglySide.call(
        'ritual_ZN12QValue3DAxis12setFormatterEP21QValue3DAxisFormatter',
        self._addressOf(formatter),
    )

  @overload(bool)
  def setReversed(self, enable: bool) -> None:
    """
    Calls Qt's 'void QValue3DAxis::setReversed(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#setReversed

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QValue3DAxis::setReversed(bool enable)
    self.uglySide.call('ritual_ZN12QValue3DAxis11setReversedEb', enable)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QValue3DAxis::QValue3DAxis(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#QValue3DAxis

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QValue3DAxis::QValue3DAxis(QObject *parent)
    self._noteCreation(QValue3DAxis, lambda: Rituals.call(
        'ritual_ZN12QValue3DAxisC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QValue3DAxisPrivate]:
    """
    Calls Qt's 'QValue3DAxisPrivate *QValue3DAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#d_func

    Returns
    -------

    Optional[QValue3DAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxisPrivate *QValue3DAxis::d_func()
    address = self.uglySide.call('ritual_ZN12QValue3DAxis6d_funcEv')
    from . import QValue3DAxisPrivate
    return QValue3DAxisPrivate._cuteAt(address)

  def recalculate(self) -> None:
    """
    Calls Qt's 'void QValue3DAxis::recalculate()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#recalculate
    """
    #  void QValue3DAxis::recalculate()
    self.uglySide.call('ritual_ZN12QValue3DAxis11recalculateEv')

  def gridSize(self) -> int:
    """
    Calls Qt's 'qsizetype QValue3DAxis::gridSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#gridSize
    """
    #  qsizetype QValue3DAxis::gridSize()
    return self.uglySide.call('ritual_ZN12QValue3DAxis8gridSizeEv')

  def subGridSize(self) -> int:
    """
    Calls Qt's 'qsizetype QValue3DAxis::subGridSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#subGridSize
    """
    #  qsizetype QValue3DAxis::subGridSize()
    return self.uglySide.call('ritual_ZN12QValue3DAxis11subGridSizeEv')

  @overload(int)
  def gridPositionAt(self, gridLine: int) -> float:
    """
    Calls Qt's 'float QValue3DAxis::gridPositionAt(qsizetype gridLine)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#gridPositionAt

    Parameters
    ----------

    gridLine : int
      Passed on as it is.
    """
    #  float QValue3DAxis::gridPositionAt(qsizetype gridLine)
    return self.uglySide.call(
        'ritual_ZN12QValue3DAxis14gridPositionAtEx', gridLine,
    )

  @overload(int)
  def subGridPositionAt(self, gridLine: int) -> float:
    """
    Calls Qt's 'float QValue3DAxis::subGridPositionAt(qsizetype gridLine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxis.html#subGridPositionAt

    Parameters
    ----------

    gridLine : int
      Passed on as it is.
    """
    #  float QValue3DAxis::subGridPositionAt(qsizetype gridLine)
    return self.uglySide.call(
        'ritual_ZN12QValue3DAxis17subGridPositionAtEx', gridLine,
    )

  @overload(int)
  def labelPositionAt(self, index: int) -> float:
    """
    Calls Qt's 'float QValue3DAxis::labelPositionAt(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#labelPositionAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  float QValue3DAxis::labelPositionAt(qsizetype index)
    return self.uglySide.call(
        'ritual_ZN12QValue3DAxis15labelPositionAtEx', index,
    )

  @overload(float)
  def positionAt(self, x: float) -> float:
    """
    Calls Qt's 'float QValue3DAxis::positionAt(float x)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#positionAt

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QValue3DAxis::positionAt(float x)
    return self.uglySide.call('ritual_ZN12QValue3DAxis10positionAtEf', x)

  @overload(float)
  def stringForValue(self, x: float) -> str:
    """
    Calls Qt's 'QString QValue3DAxis::stringForValue(float x)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#stringForValue

    Parameters
    ----------

    x : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QValue3DAxis::stringForValue(float x)
    return self.uglySide.call('ritual_ZN12QValue3DAxis14stringForValueEf', x)

  @overload(int)
  def segmentCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QValue3DAxis::segmentCountChanged(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxis.html#segmentCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QValue3DAxis::segmentCountChanged(qsizetype count)
    self.uglySide.call(
        'ritual_ZN12QValue3DAxis19segmentCountChangedEx', count,
    )

  @overload(int)
  def subSegmentCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QValue3DAxis::subSegmentCountChanged(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxis.html#subSegmentCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QValue3DAxis::subSegmentCountChanged(qsizetype count)
    self.uglySide.call(
        'ritual_ZN12QValue3DAxis22subSegmentCountChangedEx', count,
    )

  @overload(str)
  def labelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QValue3DAxis::labelFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxis.html#labelFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QValue3DAxis::labelFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN12QValue3DAxis18labelFormatChangedERK7QString', format,
    )

  @overload(QValue3DAxisFormatter)
  @overload(NoneType)
  def formatterChanged(
      self,
      formatter: Optional[QValue3DAxisFormatter],
  ) -> None:
    """
    Calls Qt's 'void QValue3DAxis::formatterChanged(QValue3DAxisFormatter
    *formatter)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#formatterChanged

    Parameters
    ----------

    formatter : Optional[QValue3DAxisFormatter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QValue3DAxis::formatterChanged(QValue3DAxisFormatter *formatter)
    self.uglySide.call(
        'ritual_ZN12QValue3DAxis16formatterChangedEP21QValue3DAxisFormatter',
        self._addressOf(formatter),
    )

  @overload(bool)
  def reversedChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QValue3DAxis::reversedChanged(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#reversedChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QValue3DAxis::reversedChanged(bool enable)
    self.uglySide.call('ritual_ZN12QValue3DAxis15reversedChangedEb', enable)

  def formatterDirty(self) -> None:
    """
    Calls Qt's 'void QValue3DAxis::formatterDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxis.html#formatterDirty
    """
    #  void QValue3DAxis::formatterDirty()
    self.uglySide.call('ritual_ZN12QValue3DAxis14formatterDirtyEv')


#  Qt's 'QList<QValue3DAxis *>': the list of QValue3DAxis, which
#  'QList[QValue3DAxis]' gives. It is made here, so that there is one as soon
#  as there can be a QValue3DAxis.
QList.createKind(
    QValue3DAxis, 'address',
    make='ritual_list_make_QValue3DAxis_ptr',
    add='ritual_list_add_QValue3DAxis_ptr',
    size='ritual_list_size_QValue3DAxis_ptr',
    at='ritual_list_at_QValue3DAxis_ptr',
    drop='ritual_list_drop_QValue3DAxis_ptr',
)
