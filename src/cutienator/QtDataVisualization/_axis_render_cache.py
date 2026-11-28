"""
AxisRenderCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/axisrendercache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means AxisRenderCache to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject, QStringList
from . import QAbstract3DAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QValue3DAxisFormatter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QValue3DAxisFormatter = WAIT['QtDataVisualization:QValue3DAxisFormatter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AxisRenderCache(QObject):
  """
  The cute side of Qt's AxisRenderCache: a plain Python object standing in
  front of one C++ AxisRenderCache.

  It is built on the cute 'QObject', as Qt's AxisRenderCache is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AxisRenderCache that has a ritual and that Python
  can call so far, 41 names in all: 'metaObject', 'setType', 'type', 'title',
  'labels', 'setMin', 'min', 'setMax', 'max', 'setSegmentCount',
  'segmentCount', 'setSubSegmentCount', 'subSegmentCount', 'setLabelFormat',
  'labelFormat', 'setReversed', 'reversed', 'setFormatter', 'formatter',
  'setCtrlFormatter', 'ctrlFormatter', 'gridLinePosition', 'gridLineCount',
  'labelPosition', 'labelCount', 'updateAllPositions', 'positionsDirty',
  'markPositionsDirty', 'setTranslate', 'translate', 'setScale', 'scale',
  'positionAt', 'labelAutoRotation', 'setLabelAutoRotation',
  'isTitleVisible', 'setTitleVisible', 'isTitleFixed', 'setTitleFixed',
  'clearLabels', 'maxLabelWidth'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AxisRenderCache::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int AxisRenderCache::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'AxisRenderCache::~AxisRenderCache()': the destructor: Python never
    removes a C++ AxisRenderCache.
  - Qt's 'LabelItem &AxisRenderCache::titleItem()': gives a type Python has
    no way to take yet.
  - Qt's 'QList<LabelItem *> &AxisRenderCache::labelItems()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  10 of the 56 functions Qt declares: 4 leans on 'Utils; 2 not a gap; 2
  forbidden; 2 leans on 'AxisRenderCache.

  What to expect
  --------------

  - The C++ AxisRenderCache is created at the first use, not by
    'AxisRenderCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AxisRenderCache.
  - Qt tells when it has removed the C++ AxisRenderCache. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's AxisRenderCache that has no cute function yet,
    '__init__', 'labelItems', 'setDrawer', 'setLabels', 'setTitle',
    'titleItem', 'updateTextures', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AxisRenderCache'

  #  A C++ AxisRenderCache Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AxisRenderCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *AxisRenderCache::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AxisRenderCache::metaObject() const
    address = self.uglySide.call('ritual_ZNK15AxisRenderCache10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstract3DAxis.AxisType:
    """
    Calls Qt's 'QAbstract3DAxis::AxisType AxisRenderCache::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#type

    Returns
    -------

    QAbstract3DAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstract3DAxis.AxisType(number)' gives.
    """
    #  QAbstract3DAxis::AxisType AxisRenderCache::type() const
    return QAbstract3DAxis.AxisType(self.uglySide.call(
        'ritual_ZNK15AxisRenderCache4typeEv',
    ))

  def title(self) -> str:
    """
    Calls Qt's 'const QString &AxisRenderCache::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &AxisRenderCache::title() const
    return self.uglySide.call('ritual_ZNK15AxisRenderCache5titleEv')

  def labels(self) -> QStringList:
    """
    Calls Qt's 'const QStringList &AxisRenderCache::labels() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#labels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList &AxisRenderCache::labels() const
    address = self.uglySide.call('ritual_ZNK15AxisRenderCache6labelsEv')
    return QStringList._cuteOwning(address)

  def min(self) -> float:
    """
    Calls Qt's 'float AxisRenderCache::min() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#min
    """
    #  float AxisRenderCache::min() const
    return self.uglySide.call('ritual_ZNK15AxisRenderCache3minEv')

  def max(self) -> float:
    """
    Calls Qt's 'float AxisRenderCache::max() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#max
    """
    #  float AxisRenderCache::max() const
    return self.uglySide.call('ritual_ZNK15AxisRenderCache3maxEv')

  def segmentCount(self) -> int:
    """
    Calls Qt's 'int AxisRenderCache::segmentCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#segmentCount
    """
    #  int AxisRenderCache::segmentCount() const
    return self.uglySide.call('ritual_ZNK15AxisRenderCache12segmentCountEv')

  def subSegmentCount(self) -> int:
    """
    Calls Qt's 'int AxisRenderCache::subSegmentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#subSegmentCount
    """
    #  int AxisRenderCache::subSegmentCount() const
    return self.uglySide.call(
        'ritual_ZNK15AxisRenderCache15subSegmentCountEv',
    )

  def labelFormat(self) -> str:
    """
    Calls Qt's 'const QString &AxisRenderCache::labelFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#labelFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &AxisRenderCache::labelFormat() const
    return self.uglySide.call('ritual_ZNK15AxisRenderCache11labelFormatEv')

  def reversed(self) -> bool:
    """
    Calls Qt's 'bool AxisRenderCache::reversed() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#reversed
    """
    #  bool AxisRenderCache::reversed() const
    return self.uglySide.call('ritual_ZNK15AxisRenderCache8reversedEv')

  def formatter(self) -> Optional[QValue3DAxisFormatter]:
    """
    Calls Qt's 'QValue3DAxisFormatter *AxisRenderCache::formatter() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#formatter

    Returns
    -------

    Optional[QValue3DAxisFormatter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxisFormatter *AxisRenderCache::formatter() const
    address = self.uglySide.call('ritual_ZNK15AxisRenderCache9formatterEv')
    from . import QValue3DAxisFormatter
    return QValue3DAxisFormatter._cuteAt(address)

  def ctrlFormatter(self) -> Optional[QValue3DAxisFormatter]:
    """
    Calls Qt's 'QValue3DAxisFormatter *AxisRenderCache::ctrlFormatter()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#ctrlFormatter

    Returns
    -------

    Optional[QValue3DAxisFormatter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxisFormatter *AxisRenderCache::ctrlFormatter() const
    address = self.uglySide.call(
        'ritual_ZNK15AxisRenderCache13ctrlFormatterEv',
    )
    from . import QValue3DAxisFormatter
    return QValue3DAxisFormatter._cuteAt(address)

  def positionsDirty(self) -> bool:
    """
    Calls Qt's 'bool AxisRenderCache::positionsDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#positionsDirty
    """
    #  bool AxisRenderCache::positionsDirty() const
    return self.uglySide.call(
        'ritual_ZNK15AxisRenderCache14positionsDirtyEv',
    )

  def labelAutoRotation(self) -> float:
    """
    Calls Qt's 'float AxisRenderCache::labelAutoRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#labelAutoRotation
    """
    #  float AxisRenderCache::labelAutoRotation() const
    return self.uglySide.call(
        'ritual_ZNK15AxisRenderCache17labelAutoRotationEv',
    )

  def isTitleVisible(self) -> bool:
    """
    Calls Qt's 'bool AxisRenderCache::isTitleVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#isTitleVisible
    """
    #  bool AxisRenderCache::isTitleVisible() const
    return self.uglySide.call(
        'ritual_ZNK15AxisRenderCache14isTitleVisibleEv',
    )

  def isTitleFixed(self) -> bool:
    """
    Calls Qt's 'bool AxisRenderCache::isTitleFixed() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#isTitleFixed
    """
    #  bool AxisRenderCache::isTitleFixed() const
    return self.uglySide.call('ritual_ZNK15AxisRenderCache12isTitleFixedEv')

  @overload(QStringList)
  def maxLabelWidth(self, labels: QStringList) -> int:
    """
    Calls Qt's 'int AxisRenderCache::maxLabelWidth(const QStringList &labels)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#maxLabelWidth

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  int AxisRenderCache::maxLabelWidth(const QStringList &labels) const
    return self.uglySide.call(
        'ritual_ZNK15AxisRenderCache13maxLabelWidthERK5QListI7QStringE',
        self._valueOf(labels),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstract3DAxis.AxisType)
  def setType(self, type: QAbstract3DAxis.AxisType) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setType(QAbstract3DAxis::AxisType
    type)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#setType

    Parameters
    ----------

    type : QAbstract3DAxis.AxisType
      Passed on as its number.
    """
    #  void AxisRenderCache::setType(QAbstract3DAxis::AxisType type)
    self.uglySide.call(
        'ritual_ZN15AxisRenderCache7setTypeEN15QAbstract3DAxis8AxisTypeE',
        type.value,
    )

  @overload(float)
  def setMin(self, min: float) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setMin(float min)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#setMin

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void AxisRenderCache::setMin(float min)
    self.uglySide.call('ritual_ZN15AxisRenderCache6setMinEf', min)

  @overload(float)
  def setMax(self, max: float) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setMax(float max)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#setMax

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void AxisRenderCache::setMax(float max)
    self.uglySide.call('ritual_ZN15AxisRenderCache6setMaxEf', max)

  @overload(int)
  def setSegmentCount(self, count: int) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setSegmentCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#setSegmentCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void AxisRenderCache::setSegmentCount(int count)
    self.uglySide.call(
        'ritual_ZN15AxisRenderCache15setSegmentCountEi', count,
    )

  @overload(int)
  def setSubSegmentCount(self, count: int) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setSubSegmentCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#setSubSegmentCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void AxisRenderCache::setSubSegmentCount(int count)
    self.uglySide.call(
        'ritual_ZN15AxisRenderCache18setSubSegmentCountEi', count,
    )

  @overload(str)
  def setLabelFormat(self, format: str) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setLabelFormat(const QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#setLabelFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void AxisRenderCache::setLabelFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN15AxisRenderCache14setLabelFormatERK7QString', format,
    )

  @overload(bool)
  def setReversed(self, enable: bool) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setReversed(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#setReversed

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void AxisRenderCache::setReversed(bool enable)
    self.uglySide.call('ritual_ZN15AxisRenderCache11setReversedEb', enable)

  @overload(QValue3DAxisFormatter)
  @overload(NoneType)
  def setFormatter(self, formatter: Optional[QValue3DAxisFormatter]) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setFormatter(QValue3DAxisFormatter
    *formatter)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#setFormatter

    Parameters
    ----------

    formatter : Optional[QValue3DAxisFormatter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AxisRenderCache::setFormatter(QValue3DAxisFormatter *formatter)
    self.uglySide.call(
        'ritual_ZN15AxisRenderCache12setFormatterEP21QValue3DAxisFormatter',
        self._addressOf(formatter),
    )

  @overload(QValue3DAxisFormatter)
  @overload(NoneType)
  def setCtrlFormatter(
      self,
      formatter: Optional[QValue3DAxisFormatter],
  ) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setCtrlFormatter(QValue3DAxisFormatter
    *formatter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#setCtrlFormatter

    Parameters
    ----------

    formatter : Optional[QValue3DAxisFormatter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AxisRenderCache::setCtrlFormatter(QValue3DAxisFormatter
    #      *formatter)
    self.uglySide.call(
        'ritual_ZN15AxisRenderCache16setCtrlFormatterEP21QValue3DAxisFormat'
        'ter',
        self._addressOf(formatter),
    )

  @overload(float)
  def setTranslate(self, translate: float) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setTranslate(float translate)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#setTranslate

    Parameters
    ----------

    translate : float
      Passed on as it is.
    """
    #  void AxisRenderCache::setTranslate(float translate)
    self.uglySide.call(
        'ritual_ZN15AxisRenderCache12setTranslateEf', translate,
    )

  @overload(float)
  def setScale(self, scale: float) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setScale(float scale)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#setScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void AxisRenderCache::setScale(float scale)
    self.uglySide.call('ritual_ZN15AxisRenderCache8setScaleEf', scale)

  @overload(float)
  def setLabelAutoRotation(self, angle: float) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setLabelAutoRotation(float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#setLabelAutoRotation

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void AxisRenderCache::setLabelAutoRotation(float angle)
    self.uglySide.call(
        'ritual_ZN15AxisRenderCache20setLabelAutoRotationEf', angle,
    )

  @overload(bool)
  def setTitleVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setTitleVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#setTitleVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void AxisRenderCache::setTitleVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN15AxisRenderCache15setTitleVisibleEb', visible,
    )

  @overload(bool)
  def setTitleFixed(self, fixed: bool) -> None:
    """
    Calls Qt's 'void AxisRenderCache::setTitleFixed(bool fixed)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#setTitleFixed

    Parameters
    ----------

    fixed : bool
      Passed on as it is.
    """
    #  void AxisRenderCache::setTitleFixed(bool fixed)
    self.uglySide.call('ritual_ZN15AxisRenderCache13setTitleFixedEb', fixed)

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
    Qt's 'AxisRenderCache::AxisRenderCache()': leans on
    'AxisRenderCache::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderCache.__init__' has no cute function yet. Qt's "
        "'AxisRenderCache::AxisRenderCache()': leans on "
        "'AxisRenderCache::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(int)
  def gridLinePosition(self, index: int) -> float:
    """
    Calls Qt's 'float AxisRenderCache::gridLinePosition(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#gridLinePosition

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  float AxisRenderCache::gridLinePosition(int index)
    return self.uglySide.call(
        'ritual_ZN15AxisRenderCache16gridLinePositionEi', index,
    )

  def gridLineCount(self) -> int:
    """
    Calls Qt's 'int AxisRenderCache::gridLineCount()'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#gridLineCount
    """
    #  int AxisRenderCache::gridLineCount()
    return self.uglySide.call('ritual_ZN15AxisRenderCache13gridLineCountEv')

  @overload(int)
  def labelPosition(self, index: int) -> float:
    """
    Calls Qt's 'float AxisRenderCache::labelPosition(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#labelPosition

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  float AxisRenderCache::labelPosition(int index)
    return self.uglySide.call(
        'ritual_ZN15AxisRenderCache13labelPositionEi', index,
    )

  def labelCount(self) -> int:
    """
    Calls Qt's 'int AxisRenderCache::labelCount()'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#labelCount
    """
    #  int AxisRenderCache::labelCount()
    return self.uglySide.call('ritual_ZN15AxisRenderCache10labelCountEv')

  def updateAllPositions(self) -> None:
    """
    Calls Qt's 'void AxisRenderCache::updateAllPositions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#updateAllPositions
    """
    #  void AxisRenderCache::updateAllPositions()
    self.uglySide.call('ritual_ZN15AxisRenderCache18updateAllPositionsEv')

  def markPositionsDirty(self) -> None:
    """
    Calls Qt's 'void AxisRenderCache::markPositionsDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisrendercache.html#markPositionsDirty
    """
    #  void AxisRenderCache::markPositionsDirty()
    self.uglySide.call('ritual_ZN15AxisRenderCache18markPositionsDirtyEv')

  def translate(self) -> float:
    """
    Calls Qt's 'float AxisRenderCache::translate()'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#translate
    """
    #  float AxisRenderCache::translate()
    return self.uglySide.call('ritual_ZN15AxisRenderCache9translateEv')

  def scale(self) -> float:
    """
    Calls Qt's 'float AxisRenderCache::scale()'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#scale
    """
    #  float AxisRenderCache::scale()
    return self.uglySide.call('ritual_ZN15AxisRenderCache5scaleEv')

  @overload(float)
  def positionAt(self, value: float) -> float:
    """
    Calls Qt's 'float AxisRenderCache::positionAt(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#positionAt

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  float AxisRenderCache::positionAt(float value)
    return self.uglySide.call(
        'ritual_ZN15AxisRenderCache10positionAtEf', value,
    )

  def clearLabels(self) -> None:
    """
    Calls Qt's 'void AxisRenderCache::clearLabels()'.

    Qt's own words: https://doc.qt.io/qt-6/axisrendercache.html#clearLabels
    """
    #  void AxisRenderCache::clearLabels()
    self.uglySide.call('ritual_ZN15AxisRenderCache11clearLabelsEv')

  @staticmethod
  def labelItems(*__, **_) -> Never:
    """
    Qt's 'QList<LabelItem *> &AxisRenderCache::labelItems()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'AxisRenderCache.labelItems' has no cute function yet. Qt's "
        "'QList<LabelItem *> &AxisRenderCache::labelItems()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setDrawer(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderCache::setDrawer(Drawer *drawer)': leans on
    'Utils::printTextToImage(QFont const&, QString const&, QColor const&,
    QColor const&, bool, bool, int)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderCache.setDrawer' has no cute function yet. Qt's 'void "
        "AxisRenderCache::setDrawer(Drawer *drawer)': leans on "
        "'Utils::printTextToImage(QFont const&, QString const&, QColor "
        "const&, QColor const&, bool, bool, int)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setLabels(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderCache::setLabels(const QStringList &labels)': leans
    on 'Utils::printTextToImage(QFont const&, QString const&, QColor const&,
    QColor const&, bool, bool, int)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderCache.setLabels' has no cute function yet. Qt's 'void "
        "AxisRenderCache::setLabels(const QStringList &labels)': leans on "
        "'Utils::printTextToImage(QFont const&, QString const&, QColor "
        "const&, QColor const&, bool, bool, int)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setTitle(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderCache::setTitle(const QString &title)': leans on
    'Utils::printTextToImage(QFont const&, QString const&, QColor const&,
    QColor const&, bool, bool, int)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderCache.setTitle' has no cute function yet. Qt's 'void "
        "AxisRenderCache::setTitle(const QString &title)': leans on "
        "'Utils::printTextToImage(QFont const&, QString const&, QColor "
        "const&, QColor const&, bool, bool, int)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def titleItem(*__, **_) -> Never:
    """
    Qt's 'LabelItem &AxisRenderCache::titleItem()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'AxisRenderCache.titleItem' has no cute function yet. Qt's "
        "'LabelItem &AxisRenderCache::titleItem()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def updateTextures(*__, **_) -> Never:
    """
    Qt's 'void AxisRenderCache::updateTextures()': leans on
    'Utils::printTextToImage(QFont const&, QString const&, QColor const&,
    QColor const&, bool, bool, int)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisRenderCache.updateTextures' has no cute function yet. Qt's "
        "'void AxisRenderCache::updateTextures()': leans on "
        "'Utils::printTextToImage(QFont const&, QString const&, QColor "
        "const&, QColor const&, bool, bool, int)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
