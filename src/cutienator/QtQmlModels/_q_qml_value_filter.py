"""
QQmlValueFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlvaluefilter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlValueFilter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlRoleFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex, QVariant
  from . import QQmlSortFilterProxyModel, QQmlValueFilterPrivate
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


class QQmlValueFilter(QQmlRoleFilter):
  """
  The cute side of Qt's QQmlValueFilter: a plain Python object standing in
  front of one C++ QQmlValueFilter.

  It is built on the cute 'QQmlRoleFilter', as Qt's QQmlValueFilter is built
  on Qt's QQmlRoleFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlValueFilter that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'value', 'setValue',
  'resetValue', 'filterAcceptsRowInternal', 'valueChanged', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlValueFilter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlValueFilter::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlValueFilter::~QQmlValueFilter()': the destructor: Python never
    removes a C++ QQmlValueFilter.
  - Qt's 'const QQmlValueFilterPrivate *QQmlValueFilter::d_func() const':
    takes in Python what 'QQmlValueFilterPrivate *QQmlValueFilter::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlValueFilter is created at the first use, not by
    'QQmlValueFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlValueFilter.
  - Qt tells when it has removed the C++ QQmlValueFilter. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQmlValueFilter::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluefilter.html#tr

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
    #  QString QQmlValueFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQmlValueFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlValueFilter'

  #  A C++ QQmlValueFilter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlValueFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlValueFilter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluefilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlValueFilter::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQmlValueFilter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def value(self) -> QVariant:
    """
    Calls Qt's 'const QVariant &QQmlValueFilter::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluefilter.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant &QQmlValueFilter::value() const
    address = self.uglySide.call('ritual_ZNK15QQmlValueFilter5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, QModelIndex, QQmlSortFilterProxyModel)
  @overload(int, QModelIndex, NoneType)
  def filterAcceptsRowInternal(
      self,
      row: int,
      sourceIndex: QModelIndex,
      a2: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlValueFilter::filterAcceptsRowInternal(int row, const
    QModelIndex &sourceIndex, const QQmlSortFilterProxyModel *a2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluefilter.html#filterAcceptsRowInternal

    Parameters
    ----------

    row : int
      Passed on as it is.

    sourceIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlValueFilter::filterAcceptsRowInternal(int row, const
    #      QModelIndex &sourceIndex, const QQmlSortFilterProxyModel *a2)
    #      const
    ritual = (
        'ritual_ZNK15QQmlValueFilter24filterAcceptsRowInternalEiRK11QModelI'
        'ndexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QQmlValueFilter24filterAcceptsRowInternalEiRK11Q'
          'ModelIndexPK24QQmlSortFilterProxyModel')
    return self.uglySide.call(
        ritual, row, self._valueOf(sourceIndex), self._addressOf(a2),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlValueFilter::setValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluefilter.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlValueFilter::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN15QQmlValueFilter8setValueERK8QVariant',
        self._valueOf(value),
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
    Notes what was given, for Qt's 'QQmlValueFilter::QQmlValueFilter(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluefilter.html#QQmlValueFilter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlValueFilter::QQmlValueFilter(QObject *parent)
    self._noteCreation(QQmlValueFilter, lambda: Rituals.call(
        'ritual_ZN15QQmlValueFilterC1EP7QObject',
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

  def resetValue(self) -> None:
    """
    Calls Qt's 'void QQmlValueFilter::resetValue()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluefilter.html#resetValue
    """
    #  void QQmlValueFilter::resetValue()
    self.uglySide.call('ritual_ZN15QQmlValueFilter10resetValueEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQmlValueFilter::valueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluefilter.html#valueChanged
    """
    #  void QQmlValueFilter::valueChanged()
    self.uglySide.call('ritual_ZN15QQmlValueFilter12valueChangedEv')

  def d_func(self) -> Optional[QQmlValueFilterPrivate]:
    """
    Calls Qt's 'QQmlValueFilterPrivate *QQmlValueFilter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluefilter.html#d_func

    Returns
    -------

    Optional[QQmlValueFilterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlValueFilterPrivate *QQmlValueFilter::d_func()
    address = self.uglySide.call('ritual_ZN15QQmlValueFilter6d_funcEv')
    from . import QQmlValueFilterPrivate
    return QQmlValueFilterPrivate._cuteAt(address)
