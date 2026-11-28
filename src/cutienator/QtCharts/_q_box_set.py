"""
QBoxSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qboxset.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QPen = WAIT['QPen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxSet(QObject):
  """
  The cute side of Qt's QBoxSet: a plain Python object standing in front of
  one C++ QBoxSet.

  It is built on the cute 'QObject', as Qt's QBoxSet is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxSet that has a ritual and that Python can call
  so far, 24 names in all: 'metaObject', 'tr', 'append', 'clear', 'setLabel',
  'label', 'setValue', 'at', '__getitem__', 'count', 'setPen', 'pen',
  'setBrush', 'brush', 'clicked', 'hovered', 'pressed', 'released',
  'doubleClicked', 'penChanged', 'brushChanged', 'valuesChanged',
  'valueChanged', 'cleared'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBoxSet::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QBoxSet::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QBoxSet::~QBoxSet()': the destructor: Python never removes a C++
    QBoxSet.
  - Qt's 'void QBoxSet::append(const QList<qreal> &values)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QBoxSet &QBoxSet::operator<<(const qreal &value)': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBoxSet is created at the first use, not by 'QBoxSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxSet.
  - Qt tells when it has removed the C++ QBoxSet. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QBoxSet, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class ValuePositions(CuteNum):
    """
    The enum 'QBoxSet::ValuePositions' of Qt, with the 5 names Qt gives in
    it.
    """

    LowerExtreme = Kee[int](0)
    LowerQuartile = Kee[int](1)
    Median = Kee[int](2)
    UpperQuartile = Kee[int](3)
    UpperExtreme = Kee[int](4)

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
    Calls Qt's 'QString QBoxSet::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#tr

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
    #  QString QBoxSet::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QBoxSet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxSet'

  #  A C++ QBoxSet Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBoxSet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxSet::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxSet::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QBoxSet10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def label(self) -> str:
    """
    Calls Qt's 'QString QBoxSet::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBoxSet::label() const
    return self.uglySide.call('ritual_ZNK7QBoxSet5labelEv')

  @overload(int)
  def at(self, index: int) -> float:
    """
    Calls Qt's 'qreal QBoxSet::at(const int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBoxSet::at(const int index) const
    return self.uglySide.call('ritual_ZNK7QBoxSet2atEi', index)

  def count(self) -> int:
    """
    Calls Qt's 'int QBoxSet::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#count
    """
    #  int QBoxSet::count() const
    return self.uglySide.call('ritual_ZNK7QBoxSet5countEv')

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QBoxSet::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QBoxSet::pen() const
    address = self.uglySide.call('ritual_ZNK7QBoxSet3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QBoxSet::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QBoxSet::brush() const
    address = self.uglySide.call('ritual_ZNK7QBoxSet5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QBoxSet::setLabel(const QString label)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBoxSet::setLabel(const QString label)
    self.uglySide.call('ritual_ZN7QBoxSet8setLabelE7QString', label)

  @overload(int, float)
  def setValue(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void QBoxSet::setValue(const int index, const qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#setValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBoxSet::setValue(const int index, const qreal value)
    self.uglySide.call('ritual_ZN7QBoxSet8setValueEid', index, value)

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QBoxSet::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QBoxSet::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN7QBoxSet6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QBoxSet::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QBoxSet::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN7QBoxSet8setBrushERK6QBrush', self._valueOf(brush),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __getitem__(self, index: int) -> float:
    """
    Calls Qt's 'qreal QBoxSet::operator[](const int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#operator[]

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBoxSet::operator[](const int index) const
    return self.uglySide.call('ritual_ZNK7QBoxSetixEi', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      label: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QBoxSet::QBoxSet(const QString label,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#QBoxSet

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBoxSet::QBoxSet(const QString label, QObject *parent)
    self._noteCreation(QBoxSet, lambda: Rituals.call(
        'ritual_ZN7QBoxSetC1E7QStringP7QObject',
        label, self._addressOf(parent, 'QObject'),
    ))

  @overload(float, float, float, float, float)
  @overload(float, float, float, float, float, str)
  @overload(float, float, float, float, float, str, QObject)
  @overload(float, float, float, float, float, str, NoneType)
  def __init__(
      self,
      le: float,
      lq: float,
      m: float,
      uq: float,
      ue: float,
      label: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QBoxSet::QBoxSet(const qreal le, const
    qreal lq, const qreal m, const qreal uq, const qreal ue, const QString
    label, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#QBoxSet

    Parameters
    ----------

    le : float
      Passed on as it is.

    lq : float
      Passed on as it is.

    m : float
      Passed on as it is.

    uq : float
      Passed on as it is.

    ue : float
      Passed on as it is.

    label : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBoxSet::QBoxSet(const qreal le, const qreal lq, const qreal m, const
    #      qreal uq, const qreal ue, const QString label, QObject *parent)
    self._noteCreation(QBoxSet, lambda: Rituals.call(
        'ritual_ZN7QBoxSetC1Eddddd7QStringP7QObject',
        le, lq, m, uq, ue, label, self._addressOf(parent, 'QObject'),
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

  @overload(float)
  def append(self, value: float) -> None:
    """
    Calls Qt's 'void QBoxSet::append(const qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#append

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QBoxSet::append(const qreal value)
    self.uglySide.call('ritual_ZN7QBoxSet6appendEd', value)

  def clear(self) -> None:
    """
    Calls Qt's 'void QBoxSet::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#clear
    """
    #  void QBoxSet::clear()
    self.uglySide.call('ritual_ZN7QBoxSet5clearEv')

  def clicked(self) -> None:
    """
    Calls Qt's 'void QBoxSet::clicked()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#clicked
    """
    #  void QBoxSet::clicked()
    self.uglySide.call('ritual_ZN7QBoxSet7clickedEv')

  @overload(bool)
  def hovered(self, status: bool) -> None:
    """
    Calls Qt's 'void QBoxSet::hovered(bool status)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.
    """
    #  void QBoxSet::hovered(bool status)
    self.uglySide.call('ritual_ZN7QBoxSet7hoveredEb', status)

  def pressed(self) -> None:
    """
    Calls Qt's 'void QBoxSet::pressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#pressed
    """
    #  void QBoxSet::pressed()
    self.uglySide.call('ritual_ZN7QBoxSet7pressedEv')

  def released(self) -> None:
    """
    Calls Qt's 'void QBoxSet::released()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#released
    """
    #  void QBoxSet::released()
    self.uglySide.call('ritual_ZN7QBoxSet8releasedEv')

  def doubleClicked(self) -> None:
    """
    Calls Qt's 'void QBoxSet::doubleClicked()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#doubleClicked
    """
    #  void QBoxSet::doubleClicked()
    self.uglySide.call('ritual_ZN7QBoxSet13doubleClickedEv')

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QBoxSet::penChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#penChanged
    """
    #  void QBoxSet::penChanged()
    self.uglySide.call('ritual_ZN7QBoxSet10penChangedEv')

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QBoxSet::brushChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#brushChanged
    """
    #  void QBoxSet::brushChanged()
    self.uglySide.call('ritual_ZN7QBoxSet12brushChangedEv')

  def valuesChanged(self) -> None:
    """
    Calls Qt's 'void QBoxSet::valuesChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#valuesChanged
    """
    #  void QBoxSet::valuesChanged()
    self.uglySide.call('ritual_ZN7QBoxSet13valuesChangedEv')

  @overload(int)
  def valueChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QBoxSet::valueChanged(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#valueChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBoxSet::valueChanged(int index)
    self.uglySide.call('ritual_ZN7QBoxSet12valueChangedEi', index)

  def cleared(self) -> None:
    """
    Calls Qt's 'void QBoxSet::cleared()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxset.html#cleared
    """
    #  void QBoxSet::cleared()
    self.uglySide.call('ritual_ZN7QBoxSet7clearedEv')


#  Qt's 'QList<QBoxSet *>': the list of QBoxSet, which 'QList[QBoxSet]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QBoxSet.
QList.createKind(
    QBoxSet, 'address',
    make='ritual_list_make_QBoxSet_ptr',
    add='ritual_list_add_QBoxSet_ptr',
    size='ritual_list_size_QBoxSet_ptr',
    at='ritual_list_at_QBoxSet_ptr',
    drop='ritual_list_drop_QBoxSet_ptr',
)
