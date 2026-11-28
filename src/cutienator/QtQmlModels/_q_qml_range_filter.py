"""
QQmlRangeFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlrangefilter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlRangeFilter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlRoleFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex, QVariant
  from . import QQmlRangeFilterPrivate, QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlRangeFilter(QQmlRoleFilter):
  """
  The cute side of Qt's QQmlRangeFilter: a plain Python object standing in
  front of one C++ QQmlRangeFilter.

  It is built on the cute 'QQmlRoleFilter', as Qt's QQmlRangeFilter is built
  on Qt's QQmlRoleFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlRangeFilter that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'tr', 'minimum',
  'setMinimum', 'resetMinimum', 'maximum', 'setMaximum', 'resetMaximum',
  'exclusive', 'filterAcceptsRowInternal', 'minimumChanged',
  'maximumChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlRangeFilter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlRangeFilter::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlRangeFilter::~QQmlRangeFilter()': the destructor: Python never
    removes a C++ QQmlRangeFilter.
  - Qt's 'const QQmlRangeFilterPrivate *QQmlRangeFilter::d_func() const':
    takes in Python what 'QQmlRangeFilterPrivate *QQmlRangeFilter::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlRangeFilter is created at the first use, not by
    'QQmlRangeFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlRangeFilter.
  - Qt tells when it has removed the C++ QQmlRangeFilter. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The classes Qt writes inside QQmlRangeFilter, each a class in here as in
  #  C++.

  class RangeExclusiveBoundary(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlRangeFilter::RangeExclusiveBoundary: a plain
    Python object standing in front of one C++
    QQmlRangeFilter::RangeExclusiveBoundary.

    C++ hands a QQmlRangeFilter::RangeExclusiveBoundary around as a copy, so
    every C++ QQmlRangeFilter::RangeExclusiveBoundary behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlRangeFilter::RangeExclusiveBoundary yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQmlRangeFilter::RangeExclusiveBoundary::~RangeExclusiveBoundary()':
      the destructor: Python removes its C++
      QQmlRangeFilter::RangeExclusiveBoundary by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQmlRangeFilter::RangeExclusiveBoundary is created at the first
      use, not by 'QQmlRangeFilter::RangeExclusiveBoundary(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlRangeFilter::RangeExclusiveBoundary back gives
      a copy the ritual made for Python, in a new cute
      QQmlRangeFilter::RangeExclusiveBoundary.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlRangeFilter::RangeExclusiveBoundary'

    #  Qt's '~QQmlRangeFilter::RangeExclusiveBoundary()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQmlRangeFilter::RangeExclusiveBoundary behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN15QQmlRangeFilter22RangeExclusiveBoundaryD1Ev')

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
    Calls Qt's 'QString QQmlRangeFilter::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#tr

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
    #  QString QQmlRangeFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQmlRangeFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QVariant)
  def exclusive(value: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlRangeFilter::exclusive(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#exclusive

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlRangeFilter::exclusive(const QVariant &value)
    address = Rituals.call(
        'ritual_ZN15QQmlRangeFilter9exclusiveERK8QVariant',
        CuteMixin._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlRangeFilter'

  #  A C++ QQmlRangeFilter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlRangeFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlRangeFilter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlRangeFilter::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQmlRangeFilter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minimum(self) -> QVariant:
    """
    Calls Qt's 'const QVariant &QQmlRangeFilter::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#minimum

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant &QQmlRangeFilter::minimum() const
    address = self.uglySide.call('ritual_ZNK15QQmlRangeFilter7minimumEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def maximum(self) -> QVariant:
    """
    Calls Qt's 'const QVariant &QQmlRangeFilter::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#maximum

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant &QQmlRangeFilter::maximum() const
    address = self.uglySide.call('ritual_ZNK15QQmlRangeFilter7maximumEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, QModelIndex, QQmlSortFilterProxyModel)
  @overload(int, QModelIndex, NoneType)
  def filterAcceptsRowInternal(
      self,
      row: int,
      sourceParent: QModelIndex,
      proxyModel: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlRangeFilter::filterAcceptsRowInternal(int row, const
    QModelIndex &sourceParent, const QQmlSortFilterProxyModel *proxyModel)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrangefilter.html#filterAcceptsRowInternal

    Parameters
    ----------

    row : int
      Passed on as it is.

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    proxyModel : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlRangeFilter::filterAcceptsRowInternal(int row, const
    #      QModelIndex &sourceParent, const QQmlSortFilterProxyModel
    #      *proxyModel) const
    ritual = (
        'ritual_ZNK15QQmlRangeFilter24filterAcceptsRowInternalEiRK11QModelI'
        'ndexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QQmlRangeFilter24filterAcceptsRowInternalEiRK11Q'
          'ModelIndexPK24QQmlSortFilterProxyModel')
    return self.uglySide.call(
        ritual,
        row, self._valueOf(sourceParent), self._addressOf(proxyModel),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setMinimum(self, minimum: QVariant) -> None:
    """
    Calls Qt's 'void QQmlRangeFilter::setMinimum(const QVariant &minimum)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#setMinimum

    Parameters
    ----------

    minimum : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlRangeFilter::setMinimum(const QVariant &minimum)
    self.uglySide.call(
        'ritual_ZN15QQmlRangeFilter10setMinimumERK8QVariant',
        self._valueOf(minimum),
    )

  @overload(QVariant)
  def setMaximum(self, maximum: QVariant) -> None:
    """
    Calls Qt's 'void QQmlRangeFilter::setMaximum(const QVariant &maximum)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#setMaximum

    Parameters
    ----------

    maximum : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlRangeFilter::setMaximum(const QVariant &maximum)
    self.uglySide.call(
        'ritual_ZN15QQmlRangeFilter10setMaximumERK8QVariant',
        self._valueOf(maximum),
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
    Notes what was given, for Qt's 'QQmlRangeFilter::QQmlRangeFilter(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrangefilter.html#QQmlRangeFilter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlRangeFilter::QQmlRangeFilter(QObject *parent)
    self._noteCreation(QQmlRangeFilter, lambda: Rituals.call(
        'ritual_ZN15QQmlRangeFilterC1EP7QObject',
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

  def resetMinimum(self) -> None:
    """
    Calls Qt's 'void QQmlRangeFilter::resetMinimum()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#resetMinimum
    """
    #  void QQmlRangeFilter::resetMinimum()
    self.uglySide.call('ritual_ZN15QQmlRangeFilter12resetMinimumEv')

  def resetMaximum(self) -> None:
    """
    Calls Qt's 'void QQmlRangeFilter::resetMaximum()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#resetMaximum
    """
    #  void QQmlRangeFilter::resetMaximum()
    self.uglySide.call('ritual_ZN15QQmlRangeFilter12resetMaximumEv')

  def minimumChanged(self) -> None:
    """
    Calls Qt's 'void QQmlRangeFilter::minimumChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrangefilter.html#minimumChanged
    """
    #  void QQmlRangeFilter::minimumChanged()
    self.uglySide.call('ritual_ZN15QQmlRangeFilter14minimumChangedEv')

  def maximumChanged(self) -> None:
    """
    Calls Qt's 'void QQmlRangeFilter::maximumChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrangefilter.html#maximumChanged
    """
    #  void QQmlRangeFilter::maximumChanged()
    self.uglySide.call('ritual_ZN15QQmlRangeFilter14maximumChangedEv')

  def d_func(self) -> Optional[QQmlRangeFilterPrivate]:
    """
    Calls Qt's 'QQmlRangeFilterPrivate *QQmlRangeFilter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrangefilter.html#d_func

    Returns
    -------

    Optional[QQmlRangeFilterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlRangeFilterPrivate *QQmlRangeFilter::d_func()
    address = self.uglySide.call('ritual_ZN15QQmlRangeFilter6d_funcEv')
    from . import QQmlRangeFilterPrivate
    return QQmlRangeFilterPrivate._cuteAt(address)
