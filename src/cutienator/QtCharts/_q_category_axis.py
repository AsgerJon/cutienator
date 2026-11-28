"""
QCategoryAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qcategoryaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QAbstractAxis, QValueAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QCategoryAxisPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCategoryAxis(QValueAxis):
  """
  The cute side of Qt's QCategoryAxis: a plain Python object standing in
  front of one C++ QCategoryAxis.

  It is built on the cute 'QValueAxis', as Qt's QCategoryAxis is built on
  Qt's QValueAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCategoryAxis that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'type', 'append',
  'remove', 'replaceLabel', 'startValue', 'setStartValue', 'endValue',
  'categoriesLabels', 'count', 'labelsPosition', 'setLabelsPosition',
  'categoriesChanged', 'labelsPositionChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCategoryAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QCategoryAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCategoryAxis::~QCategoryAxis()': the destructor: Python never
    removes a C++ QCategoryAxis.
  - Qt's 'QCategoryAxis::QCategoryAxis(QCategoryAxisPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QCategoryAxisPrivate *QCategoryAxis::d_func() const': takes
    in Python what 'QCategoryAxisPrivate *QCategoryAxis::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCategoryAxis is created at the first use, not by
    'QCategoryAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCategoryAxis.
  - Qt tells when it has removed the C++ QCategoryAxis. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QCategoryAxis, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AxisLabelsPosition(CuteNum):
    """
    The enum 'QCategoryAxis::AxisLabelsPosition' of Qt, with the 2 names Qt
    gives in it.
    """

    AxisLabelsPositionCenter = Kee[int](0)
    AxisLabelsPositionOnValue = Kee[int](1)

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
    Calls Qt's 'QString QCategoryAxis::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#tr

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
    #  QString QCategoryAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QCategoryAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCategoryAxis'

  #  A C++ QCategoryAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCategoryAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCategoryAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCategoryAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QCategoryAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'AxisType QCategoryAxis::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#type

    Returns
    -------

    QAbstractAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractAxis.AxisType(number)' gives.
    """
    #  AxisType QCategoryAxis::type() const
    ritual = 'ritual_ZNK13QCategoryAxis4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QCategoryAxis4typeEv'
    return QAbstractAxis.AxisType(self.uglySide.call(ritual))

  @overload()
  @overload(str)
  def startValue(self, categoryLabel: str = '') -> float:
    """
    Calls Qt's 'qreal QCategoryAxis::startValue(const QString &categoryLabel)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#startValue

    Parameters
    ----------

    categoryLabel : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  qreal QCategoryAxis::startValue(const QString &categoryLabel) const
    return self.uglySide.call(
        'ritual_ZNK13QCategoryAxis10startValueERK7QString', categoryLabel,
    )

  @overload(str)
  def endValue(self, categoryLabel: str) -> float:
    """
    Calls Qt's 'qreal QCategoryAxis::endValue(const QString &categoryLabel)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#endValue

    Parameters
    ----------

    categoryLabel : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qreal QCategoryAxis::endValue(const QString &categoryLabel) const
    return self.uglySide.call(
        'ritual_ZNK13QCategoryAxis8endValueERK7QString', categoryLabel,
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QCategoryAxis::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#count
    """
    #  int QCategoryAxis::count() const
    return self.uglySide.call('ritual_ZNK13QCategoryAxis5countEv')

  def labelsPosition(self) -> AxisLabelsPosition:
    """
    Calls Qt's 'QCategoryAxis::AxisLabelsPosition
    QCategoryAxis::labelsPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#labelsPosition

    Returns
    -------

    AxisLabelsPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AxisLabelsPosition(number)' gives.
    """
    #  QCategoryAxis::AxisLabelsPosition QCategoryAxis::labelsPosition()
    #      const
    return QCategoryAxis.AxisLabelsPosition(self.uglySide.call(
        'ritual_ZNK13QCategoryAxis14labelsPositionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setStartValue(self, min: float) -> None:
    """
    Calls Qt's 'void QCategoryAxis::setStartValue(qreal min)'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#setStartValue

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QCategoryAxis::setStartValue(qreal min)
    self.uglySide.call('ritual_ZN13QCategoryAxis13setStartValueEd', min)

  @overload(AxisLabelsPosition)
  def setLabelsPosition(self, position: AxisLabelsPosition) -> None:
    """
    Calls Qt's 'void
    QCategoryAxis::setLabelsPosition(QCategoryAxis::AxisLabelsPosition
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategoryaxis.html#setLabelsPosition

    Parameters
    ----------

    position : AxisLabelsPosition
      Passed on as its number.
    """
    #  void
    #      QCategoryAxis::setLabelsPosition(QCategoryAxis::AxisLabelsPosition
    #      position)
    self.uglySide.call(
        'ritual_ZN13QCategoryAxis17setLabelsPositionENS_18AxisLabelsPositio'
        'nE',
        position.value,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QCategoryAxis::QCategoryAxis(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#QCategoryAxis

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCategoryAxis::QCategoryAxis(QObject *parent)
    self._noteCreation(QCategoryAxis, lambda: Rituals.call(
        'ritual_ZN13QCategoryAxisC1EP7QObject',
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

  @overload(str, float)
  def append(self, label: str, categoryEndValue: float) -> None:
    """
    Calls Qt's 'void QCategoryAxis::append(const QString &label, qreal
    categoryEndValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#append

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    categoryEndValue : float
      Passed on as it is.
    """
    #  void QCategoryAxis::append(const QString &label, qreal
    #      categoryEndValue)
    self.uglySide.call(
        'ritual_ZN13QCategoryAxis6appendERK7QStringd',
        label, categoryEndValue,
    )

  @overload(str)
  def remove(self, label: str) -> None:
    """
    Calls Qt's 'void QCategoryAxis::remove(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#remove

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCategoryAxis::remove(const QString &label)
    self.uglySide.call('ritual_ZN13QCategoryAxis6removeERK7QString', label)

  @overload(str, str)
  def replaceLabel(self, oldLabel: str, newLabel: str) -> None:
    """
    Calls Qt's 'void QCategoryAxis::replaceLabel(const QString &oldLabel,
    const QString &newLabel)'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#replaceLabel

    Parameters
    ----------

    oldLabel : str
      Passed on as it is: a QString is made of it for the call.

    newLabel : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCategoryAxis::replaceLabel(const QString &oldLabel, const
    #      QString &newLabel)
    self.uglySide.call(
        'ritual_ZN13QCategoryAxis12replaceLabelERK7QStringS2_',
        oldLabel, newLabel,
    )

  def categoriesLabels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCategoryAxis::categoriesLabels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategoryaxis.html#categoriesLabels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCategoryAxis::categoriesLabels()
    address = self.uglySide.call(
        'ritual_ZN13QCategoryAxis16categoriesLabelsEv',
    )
    return QStringList._cuteOwning(address)

  def categoriesChanged(self) -> None:
    """
    Calls Qt's 'void QCategoryAxis::categoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategoryaxis.html#categoriesChanged
    """
    #  void QCategoryAxis::categoriesChanged()
    self.uglySide.call('ritual_ZN13QCategoryAxis17categoriesChangedEv')

  @overload(AxisLabelsPosition)
  def labelsPositionChanged(self, position: AxisLabelsPosition) -> None:
    """
    Calls Qt's 'void
    QCategoryAxis::labelsPositionChanged(QCategoryAxis::AxisLabelsPosition
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategoryaxis.html#labelsPositionChanged

    Parameters
    ----------

    position : AxisLabelsPosition
      Passed on as its number.
    """
    #  void QCategoryAxis::labelsPositionChanged(QCategoryAxis::
    #      AxisLabelsPosition position)
    self.uglySide.call(
        'ritual_ZN13QCategoryAxis21labelsPositionChangedENS_18AxisLabelsPos'
        'itionE',
        position.value,
    )

  def d_func(self) -> Optional[QCategoryAxisPrivate]:
    """
    Calls Qt's 'QCategoryAxisPrivate *QCategoryAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxis.html#d_func

    Returns
    -------

    Optional[QCategoryAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategoryAxisPrivate *QCategoryAxis::d_func()
    address = self.uglySide.call('ritual_ZN13QCategoryAxis6d_funcEv')
    from . import QCategoryAxisPrivate
    return QCategoryAxisPrivate._cuteAt(address)
