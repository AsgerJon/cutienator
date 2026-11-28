"""
QAbstract3DAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qabstract3daxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAbstract3DAxisPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstract3DAxis(QObject):
  """
  The cute side of Qt's QAbstract3DAxis: a plain Python object standing in
  front of one C++ QAbstract3DAxis.

  It is built on the cute 'QObject', as Qt's QAbstract3DAxis is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstract3DAxis that has a ritual and that Python
  can call so far, 44 names in all: 'metaObject', 'tr', 'd_func', 'setTitle',
  'title', 'setLabels', 'labels', 'orientation', 'type', 'setMin', 'min',
  'setMax', 'max', 'setAutoAdjustRange', 'isAutoAdjustRange',
  'setScaleLabelsByCount', 'isScaleLabelsByCount', 'setLabelSize',
  'labelSize', 'setRange', 'setLabelAutoAngle', 'labelAutoAngle',
  'setTitleVisible', 'isTitleVisible', 'setLabelsVisible', 'labelsVisible',
  'setTitleFixed', 'isTitleFixed', 'setTitleOffset', 'titleOffset',
  'titleChanged', 'labelsChanged', 'orientationChanged', 'minChanged',
  'maxChanged', 'rangeChanged', 'autoAdjustRangeChanged',
  'scaleLabelsByCountChanged', 'labelSizeChanged', 'labelAutoAngleChanged',
  'titleVisibleChanged', 'labelVisibleChanged', 'titleFixedChanged',
  'titleOffsetChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstract3DAxis::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstract3DAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QAbstract3DAxisPrivate *QAbstract3DAxis::d_func() const':
    takes in Python what 'QAbstract3DAxisPrivate *QAbstract3DAxis::d_func()'
    takes.
  - Qt's 'void QAbstract3DAxis::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QAbstract3DAxis::QAbstract3DAxis(QAbstract3DAxisPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstract3DAxis::~QAbstract3DAxis()': the destructor: Python never
    removes a C++ QAbstract3DAxis.

  What has no ritual
  ------------------

  4 of the 54 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstract3DAxis is created at the first use, not by
    'QAbstract3DAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstract3DAxis.
  - Qt tells when it has removed the C++ QAbstract3DAxis. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstract3DAxis that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QAbstract3DAxis, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AxisOrientation(CuteNum, scoped=True):
    """
    The enum 'QAbstract3DAxis::AxisOrientation' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    X = Kee[int](1)
    Y = Kee[int](2)
    Z = Kee[int](3)

  class AxisType(CuteNum, scoped=True):
    """
    The enum 'QAbstract3DAxis::AxisType' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    Category = Kee[int](1)
    Value = Kee[int](2)

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
    Calls Qt's 'QString QAbstract3DAxis::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#tr

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
    #  QString QAbstract3DAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QAbstract3DAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstract3DAxis'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QAbstract3DAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstract3DAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstract3DAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstract3DAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QAbstract3DAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QAbstract3DAxis::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstract3DAxis::title() const
    return self.uglySide.call('ritual_ZNK15QAbstract3DAxis5titleEv')

  def labels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAbstract3DAxis::labels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#labels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAbstract3DAxis::labels() const
    address = self.uglySide.call('ritual_ZNK15QAbstract3DAxis6labelsEv')
    return QStringList._cuteOwning(address)

  def orientation(self) -> AxisOrientation:
    """
    Calls Qt's 'QAbstract3DAxis::AxisOrientation
    QAbstract3DAxis::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#orientation

    Returns
    -------

    AxisOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AxisOrientation(number)'
      gives.
    """
    #  QAbstract3DAxis::AxisOrientation QAbstract3DAxis::orientation() const
    return QAbstract3DAxis.AxisOrientation(self.uglySide.call(
        'ritual_ZNK15QAbstract3DAxis11orientationEv',
    ))

  def type(self) -> AxisType:
    """
    Calls Qt's 'QAbstract3DAxis::AxisType QAbstract3DAxis::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#type

    Returns
    -------

    AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AxisType(number)' gives.
    """
    #  QAbstract3DAxis::AxisType QAbstract3DAxis::type() const
    return QAbstract3DAxis.AxisType(self.uglySide.call(
        'ritual_ZNK15QAbstract3DAxis4typeEv',
    ))

  def min(self) -> float:
    """
    Calls Qt's 'float QAbstract3DAxis::min() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#min
    """
    #  float QAbstract3DAxis::min() const
    return self.uglySide.call('ritual_ZNK15QAbstract3DAxis3minEv')

  def max(self) -> float:
    """
    Calls Qt's 'float QAbstract3DAxis::max() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#max
    """
    #  float QAbstract3DAxis::max() const
    return self.uglySide.call('ritual_ZNK15QAbstract3DAxis3maxEv')

  def isAutoAdjustRange(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DAxis::isAutoAdjustRange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#isAutoAdjustRange
    """
    #  bool QAbstract3DAxis::isAutoAdjustRange() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstract3DAxis17isAutoAdjustRangeEv',
    )

  def isScaleLabelsByCount(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DAxis::isScaleLabelsByCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#isScaleLabelsByCount
    """
    #  bool QAbstract3DAxis::isScaleLabelsByCount() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstract3DAxis20isScaleLabelsByCountEv',
    )

  def labelSize(self) -> float:
    """
    Calls Qt's 'qreal QAbstract3DAxis::labelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#labelSize
    """
    #  qreal QAbstract3DAxis::labelSize() const
    return self.uglySide.call('ritual_ZNK15QAbstract3DAxis9labelSizeEv')

  def labelAutoAngle(self) -> float:
    """
    Calls Qt's 'float QAbstract3DAxis::labelAutoAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#labelAutoAngle
    """
    #  float QAbstract3DAxis::labelAutoAngle() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstract3DAxis14labelAutoAngleEv',
    )

  def isTitleVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DAxis::isTitleVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#isTitleVisible
    """
    #  bool QAbstract3DAxis::isTitleVisible() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstract3DAxis14isTitleVisibleEv',
    )

  def labelsVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DAxis::labelsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#labelsVisible
    """
    #  bool QAbstract3DAxis::labelsVisible() const
    return self.uglySide.call('ritual_ZNK15QAbstract3DAxis13labelsVisibleEv')

  def isTitleFixed(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DAxis::isTitleFixed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#isTitleFixed
    """
    #  bool QAbstract3DAxis::isTitleFixed() const
    return self.uglySide.call('ritual_ZNK15QAbstract3DAxis12isTitleFixedEv')

  def titleOffset(self) -> float:
    """
    Calls Qt's 'float QAbstract3DAxis::titleOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#titleOffset
    """
    #  float QAbstract3DAxis::titleOffset() const
    return self.uglySide.call('ritual_ZNK15QAbstract3DAxis11titleOffsetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DAxis::setTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis8setTitleERK7QString', title,
    )

  @overload(QStringList)
  def setLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setLabels(const QStringList &labels)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#setLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QAbstract3DAxis::setLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis9setLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(float)
  def setMin(self, min: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setMin(float min)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#setMin

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setMin(float min)
    self.uglySide.call('ritual_ZN15QAbstract3DAxis6setMinEf', min)

  @overload(float)
  def setMax(self, max: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setMax(float max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#setMax

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setMax(float max)
    self.uglySide.call('ritual_ZN15QAbstract3DAxis6setMaxEf', max)

  @overload(bool)
  def setAutoAdjustRange(self, autoAdjust: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setAutoAdjustRange(bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#setAutoAdjustRange

    Parameters
    ----------

    autoAdjust : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setAutoAdjustRange(bool autoAdjust)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis18setAutoAdjustRangeEb', autoAdjust,
    )

  @overload(bool)
  def setScaleLabelsByCount(self, adjust: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setScaleLabelsByCount(bool adjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#setScaleLabelsByCount

    Parameters
    ----------

    adjust : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setScaleLabelsByCount(bool adjust)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis21setScaleLabelsByCountEb', adjust,
    )

  @overload(float)
  def setLabelSize(self, size: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setLabelSize(qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#setLabelSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setLabelSize(qreal size)
    self.uglySide.call('ritual_ZN15QAbstract3DAxis12setLabelSizeEd', size)

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setRange(float min, float max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setRange(float min, float max)
    self.uglySide.call('ritual_ZN15QAbstract3DAxis8setRangeEff', min, max)

  @overload(float)
  def setLabelAutoAngle(self, degree: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setLabelAutoAngle(float degree)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#setLabelAutoAngle

    Parameters
    ----------

    degree : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setLabelAutoAngle(float degree)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis17setLabelAutoAngleEf', degree,
    )

  @overload(bool)
  def setTitleVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setTitleVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#setTitleVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setTitleVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis15setTitleVisibleEb', visible,
    )

  @overload(bool)
  def setLabelsVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setLabelsVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#setLabelsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setLabelsVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis16setLabelsVisibleEb', visible,
    )

  @overload(bool)
  def setTitleFixed(self, fixed: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setTitleFixed(bool fixed)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#setTitleFixed

    Parameters
    ----------

    fixed : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setTitleFixed(bool fixed)
    self.uglySide.call('ritual_ZN15QAbstract3DAxis13setTitleFixedEb', fixed)

  @overload(float)
  def setTitleOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::setTitleOffset(float offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#setTitleOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::setTitleOffset(float offset)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis14setTitleOffsetEf', offset,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAbstract3DAxis::QAbstract3DAxis(QAbstract3DAxisPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstract3DAxis.__init__' has no cute function yet. Qt's "
        "'QAbstract3DAxis::QAbstract3DAxis(QAbstract3DAxisPrivate &d, "
        "QObject *parent)': takes a type Python has no way to hand over yet."
    )

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

  def d_func(self) -> Optional[QAbstract3DAxisPrivate]:
    """
    Calls Qt's 'QAbstract3DAxisPrivate *QAbstract3DAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#d_func

    Returns
    -------

    Optional[QAbstract3DAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxisPrivate *QAbstract3DAxis::d_func()
    address = self.uglySide.call('ritual_ZN15QAbstract3DAxis6d_funcEv')
    from . import QAbstract3DAxisPrivate
    return QAbstract3DAxisPrivate._cuteAt(address)

  @overload(str)
  def titleChanged(self, newTitle: str) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::titleChanged(const QString &newTitle)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#titleChanged

    Parameters
    ----------

    newTitle : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstract3DAxis::titleChanged(const QString &newTitle)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis12titleChangedERK7QString', newTitle,
    )

  def labelsChanged(self) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::labelsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#labelsChanged
    """
    #  void QAbstract3DAxis::labelsChanged()
    self.uglySide.call('ritual_ZN15QAbstract3DAxis13labelsChangedEv')

  @overload(AxisOrientation)
  def orientationChanged(self, orientation: AxisOrientation) -> None:
    """
    Calls Qt's 'void
    QAbstract3DAxis::orientationChanged(QAbstract3DAxis::AxisOrientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#orientationChanged

    Parameters
    ----------

    orientation : AxisOrientation
      Passed on as its number.
    """
    #  void QAbstract3DAxis::orientationChanged(QAbstract3DAxis::
    #      AxisOrientation orientation)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis18orientationChangedENS_15AxisOrientatio'
        'nE',
        orientation.value,
    )

  @overload(float)
  def minChanged(self, value: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::minChanged(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#minChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::minChanged(float value)
    self.uglySide.call('ritual_ZN15QAbstract3DAxis10minChangedEf', value)

  @overload(float)
  def maxChanged(self, value: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::maxChanged(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#maxChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::maxChanged(float value)
    self.uglySide.call('ritual_ZN15QAbstract3DAxis10maxChangedEf', value)

  @overload(float, float)
  def rangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::rangeChanged(float min, float max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxis.html#rangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::rangeChanged(float min, float max)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis12rangeChangedEff', min, max,
    )

  @overload(bool)
  def autoAdjustRangeChanged(self, autoAdjust: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::autoAdjustRangeChanged(bool
    autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#autoAdjustRangeChanged

    Parameters
    ----------

    autoAdjust : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::autoAdjustRangeChanged(bool autoAdjust)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis22autoAdjustRangeChangedEb', autoAdjust,
    )

  @overload(bool)
  def scaleLabelsByCountChanged(self, adjust: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::scaleLabelsByCountChanged(bool
    adjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#scaleLabelsByCountChanged

    Parameters
    ----------

    adjust : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::scaleLabelsByCountChanged(bool adjust)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis25scaleLabelsByCountChangedEb', adjust,
    )

  @overload(float)
  def labelSizeChanged(self, size: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::labelSizeChanged(qreal size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#labelSizeChanged

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::labelSizeChanged(qreal size)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis16labelSizeChangedEd', size,
    )

  @overload(float)
  def labelAutoAngleChanged(self, angle: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::labelAutoAngleChanged(float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#labelAutoAngleChanged

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::labelAutoAngleChanged(float angle)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis21labelAutoAngleChangedEf', angle,
    )

  @overload(bool)
  def titleVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::titleVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#titleVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::titleVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis19titleVisibleChangedEb', visible,
    )

  @overload(bool)
  def labelVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::labelVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#labelVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::labelVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis19labelVisibleChangedEb', visible,
    )

  @overload(bool)
  def titleFixedChanged(self, fixed: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::titleFixedChanged(bool fixed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#titleFixedChanged

    Parameters
    ----------

    fixed : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxis::titleFixedChanged(bool fixed)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis17titleFixedChangedEb', fixed,
    )

  @overload(float)
  def titleOffsetChanged(self, offset: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxis::titleOffsetChanged(float offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxis.html#titleOffsetChanged

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QAbstract3DAxis::titleOffsetChanged(float offset)
    self.uglySide.call(
        'ritual_ZN15QAbstract3DAxis18titleOffsetChangedEf', offset,
    )


#  Qt's 'QList<QAbstract3DAxis *>': the list of QAbstract3DAxis, which
#  'QList[QAbstract3DAxis]' gives. It is made here, so that there is one as
#  soon as there can be a QAbstract3DAxis.
QList.createKind(
    QAbstract3DAxis, 'address',
    make='ritual_list_make_QAbstract3DAxis_ptr',
    add='ritual_list_add_QAbstract3DAxis_ptr',
    size='ritual_list_size_QAbstract3DAxis_ptr',
    at='ritual_list_at_QAbstract3DAxis_ptr',
    drop='ritual_list_drop_QAbstract3DAxis_ptr',
)
