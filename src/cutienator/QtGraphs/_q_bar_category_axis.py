"""
QBarCategoryAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qbarcategoryaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QAbstractAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QBarCategoryAxisPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarCategoryAxis(QAbstractAxis):
  """
  The cute side of Qt's QBarCategoryAxis: a plain Python object standing in
  front of one C++ QBarCategoryAxis.

  It is built on the cute 'QAbstractAxis', as Qt's QBarCategoryAxis is built
  on Qt's QAbstractAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarCategoryAxis that has a ritual and that Python
  can call so far, 26 names in all: 'metaObject', 'tr', 'type', 'append',
  'remove', 'insert', 'replace', 'clear', 'at', 'setCategories',
  'categories', 'count', 'setLabelPosition', 'labelPosition', 'setMin',
  'min', 'setMax', 'max', 'setRange', 'categoriesChanged', 'minChanged',
  'maxChanged', 'categoryRangeChanged', 'countChanged',
  'labelPositionChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarCategoryAxis::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QBarCategoryAxis::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QBarCategoryAxis::~QBarCategoryAxis()': the destructor: Python
    never removes a C++ QBarCategoryAxis.
  - Qt's 'QBarCategoryAxis::QBarCategoryAxis(QBarCategoryAxisPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QBarCategoryAxisPrivate *QBarCategoryAxis::d_func() const':
    takes in Python what 'QBarCategoryAxisPrivate
    *QBarCategoryAxis::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 38 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBarCategoryAxis is created at the first use, not by
    'QBarCategoryAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarCategoryAxis.
  - Qt tells when it has removed the C++ QBarCategoryAxis. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QBarCategoryAxis, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LabelPosition(CuteNum, scoped=True):
    """
    The enum 'QBarCategoryAxis::LabelPosition' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Center = Kee[int](0)
    OnValue = Kee[int](1)

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
    Calls Qt's 'QString QBarCategoryAxis::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#tr

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
    #  QString QBarCategoryAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QBarCategoryAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarCategoryAxis'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QBarCategoryAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarCategoryAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarCategoryAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarCategoryAxis::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QBarCategoryAxis10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'AxisType QBarCategoryAxis::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#type

    Returns
    -------

    QAbstractAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractAxis.AxisType(number)' gives.
    """
    #  AxisType QBarCategoryAxis::type() const
    ritual = 'ritual_ZNK16QBarCategoryAxis4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QBarCategoryAxis4typeEv'
    return QAbstractAxis.AxisType(self.uglySide.call(ritual))

  @overload(int)
  def at(self, index: int) -> str:
    """
    Calls Qt's 'QString QBarCategoryAxis::at(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBarCategoryAxis::at(qsizetype index) const
    return self.uglySide.call('ritual_ZNK16QBarCategoryAxis2atEx', index)

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QBarCategoryAxis::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#count
    """
    #  qsizetype QBarCategoryAxis::count() const
    return self.uglySide.call('ritual_ZNK16QBarCategoryAxis5countEv')

  def labelPosition(self) -> LabelPosition:
    """
    Calls Qt's 'LabelPosition QBarCategoryAxis::labelPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxis.html#labelPosition

    Returns
    -------

    LabelPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LabelPosition(number)'
      gives.
    """
    #  LabelPosition QBarCategoryAxis::labelPosition() const
    return QBarCategoryAxis.LabelPosition(self.uglySide.call(
        'ritual_ZNK16QBarCategoryAxis13labelPositionEv',
    ))

  def min(self) -> str:
    """
    Calls Qt's 'QString QBarCategoryAxis::min() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#min

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBarCategoryAxis::min() const
    return self.uglySide.call('ritual_ZNK16QBarCategoryAxis3minEv')

  def max(self) -> str:
    """
    Calls Qt's 'QString QBarCategoryAxis::max() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#max

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBarCategoryAxis::max() const
    return self.uglySide.call('ritual_ZNK16QBarCategoryAxis3maxEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setCategories(self, categories: QStringList) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::setCategories(const QStringList
    &categories)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxis.html#setCategories

    Parameters
    ----------

    categories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarCategoryAxis::setCategories(const QStringList &categories)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis13setCategoriesERK5QListI7QStringE',
        self._valueOf(categories),
    )

  @overload(LabelPosition)
  def setLabelPosition(self, position: LabelPosition) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::setLabelPosition(LabelPosition
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxis.html#setLabelPosition

    Parameters
    ----------

    position : LabelPosition
      Passed on as its number.
    """
    #  void QBarCategoryAxis::setLabelPosition(LabelPosition position)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis16setLabelPositionENS_13LabelPositionE',
        position.value,
    )

  @overload(str)
  def setMin(self, minCategory: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::setMin(const QString &minCategory)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#setMin

    Parameters
    ----------

    minCategory : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::setMin(const QString &minCategory)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis6setMinERK7QString', minCategory,
    )

  @overload(str)
  def setMax(self, maxCategory: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::setMax(const QString &maxCategory)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#setMax

    Parameters
    ----------

    maxCategory : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::setMax(const QString &maxCategory)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis6setMaxERK7QString', maxCategory,
    )

  @overload(str, str)
  def setRange(self, minCategory: str, maxCategory: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::setRange(const QString &minCategory,
    const QString &maxCategory)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#setRange

    Parameters
    ----------

    minCategory : str
      Passed on as it is: a QString is made of it for the call.

    maxCategory : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::setRange(const QString &minCategory, const
    #      QString &maxCategory)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis8setRangeERK7QStringS2_',
        minCategory, maxCategory,
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
    Notes what was given, for Qt's
    'QBarCategoryAxis::QBarCategoryAxis(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxis.html#QBarCategoryAxis

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBarCategoryAxis::QBarCategoryAxis(QObject *parent)
    self._noteCreation(QBarCategoryAxis, lambda: Rituals.call(
        'ritual_ZN16QBarCategoryAxisC1EP7QObject',
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

  @overload(QStringList)
  def append(self, categories: QStringList) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::append(const QStringList
    &categories)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#append

    Parameters
    ----------

    categories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarCategoryAxis::append(const QStringList &categories)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis6appendERK5QListI7QStringE',
        self._valueOf(categories),
    )

  @overload(str)
  def append(self, category: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::append(const QString &category)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#append

    Parameters
    ----------

    category : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::append(const QString &category)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis6appendERK7QString', category,
    )

  @overload(str)
  def remove(self, category: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::remove(const QString &category)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#remove

    Parameters
    ----------

    category : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::remove(const QString &category)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis6removeERK7QString', category,
    )

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::remove(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarCategoryAxis::remove(qsizetype index)
    self.uglySide.call('ritual_ZN16QBarCategoryAxis6removeEx', index)

  @overload(int, str)
  def insert(self, index: int, category: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::insert(qsizetype index, const QString
    &category)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    category : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::insert(qsizetype index, const QString
    #      &category)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis6insertExRK7QString', index, category,
    )

  @overload(str, str)
  def replace(self, oldCategory: str, newCategory: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::replace(const QString &oldCategory,
    const QString &newCategory)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#replace

    Parameters
    ----------

    oldCategory : str
      Passed on as it is: a QString is made of it for the call.

    newCategory : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::replace(const QString &oldCategory, const
    #      QString &newCategory)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis7replaceERK7QStringS2_',
        oldCategory, newCategory,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#clear
    """
    #  void QBarCategoryAxis::clear()
    self.uglySide.call('ritual_ZN16QBarCategoryAxis5clearEv')

  def categories(self) -> QStringList:
    """
    Calls Qt's 'QStringList QBarCategoryAxis::categories()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#categories

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QBarCategoryAxis::categories()
    address = self.uglySide.call('ritual_ZN16QBarCategoryAxis10categoriesEv')
    return QStringList._cuteOwning(address)

  def categoriesChanged(self) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::categoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxis.html#categoriesChanged
    """
    #  void QBarCategoryAxis::categoriesChanged()
    self.uglySide.call('ritual_ZN16QBarCategoryAxis17categoriesChangedEv')

  @overload(str)
  def minChanged(self, min: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::minChanged(const QString &min)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#minChanged

    Parameters
    ----------

    min : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::minChanged(const QString &min)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis10minChangedERK7QString', min,
    )

  @overload(str)
  def maxChanged(self, max: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::maxChanged(const QString &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#maxChanged

    Parameters
    ----------

    max : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::maxChanged(const QString &max)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis10maxChangedERK7QString', max,
    )

  @overload(str, str)
  def categoryRangeChanged(self, min: str, max: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::categoryRangeChanged(const QString
    &min, const QString &max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxis.html#categoryRangeChanged

    Parameters
    ----------

    min : str
      Passed on as it is: a QString is made of it for the call.

    max : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxis::categoryRangeChanged(const QString &min, const
    #      QString &max)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis20categoryRangeChangedERK7QStringS2_',
        min, max,
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#countChanged
    """
    #  void QBarCategoryAxis::countChanged()
    self.uglySide.call('ritual_ZN16QBarCategoryAxis12countChangedEv')

  @overload(LabelPosition)
  def labelPositionChanged(self, position: LabelPosition) -> None:
    """
    Calls Qt's 'void QBarCategoryAxis::labelPositionChanged(LabelPosition
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxis.html#labelPositionChanged

    Parameters
    ----------

    position : LabelPosition
      Passed on as its number.
    """
    #  void QBarCategoryAxis::labelPositionChanged(LabelPosition position)
    self.uglySide.call(
        'ritual_ZN16QBarCategoryAxis20labelPositionChangedENS_13LabelPositi'
        'onE',
        position.value,
    )

  def d_func(self) -> Optional[QBarCategoryAxisPrivate]:
    """
    Calls Qt's 'QBarCategoryAxisPrivate *QBarCategoryAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxis.html#d_func

    Returns
    -------

    Optional[QBarCategoryAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarCategoryAxisPrivate *QBarCategoryAxis::d_func()
    address = self.uglySide.call('ritual_ZN16QBarCategoryAxis6d_funcEv')
    from . import QBarCategoryAxisPrivate
    return QBarCategoryAxisPrivate._cuteAt(address)
