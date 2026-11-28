"""
QQmlAllOfFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlalloffilter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlAllOfFilter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlCompositeFilterBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QQmlAllOfFilterPrivate, QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAllOfFilter(QQmlCompositeFilterBase):
  """
  The cute side of Qt's QQmlAllOfFilter: a plain Python object standing in
  front of one C++ QQmlAllOfFilter.

  It is built on the cute 'QQmlCompositeFilterBase', as Qt's QQmlAllOfFilter
  is built on Qt's QQmlCompositeFilterBase, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQmlAllOfFilter that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr',
  'filterAcceptsRowInternal', 'filterAcceptsColumnInternal', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlAllOfFilter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlAllOfFilter::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQmlAllOfFilterPrivate *QQmlAllOfFilter::d_func() const':
    takes in Python what 'QQmlAllOfFilterPrivate *QQmlAllOfFilter::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlAllOfFilter is created at the first use, not by
    'QQmlAllOfFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlAllOfFilter.
  - Qt tells when it has removed the C++ QQmlAllOfFilter. Every call on the
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
    Calls Qt's 'QString QQmlAllOfFilter::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlalloffilter.html#tr

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
    #  QString QQmlAllOfFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQmlAllOfFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAllOfFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlAllOfFilter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlalloffilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlAllOfFilter::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQmlAllOfFilter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int, QModelIndex, QQmlSortFilterProxyModel)
  @overload(int, QModelIndex, NoneType)
  def filterAcceptsRowInternal(
      self,
      a0: int,
      a1: QModelIndex,
      a2: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlAllOfFilter::filterAcceptsRowInternal(int a0, const
    QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlalloffilter.html#filterAcceptsRowInternal

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlAllOfFilter::filterAcceptsRowInternal(int a0, const
    #      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
    ritual = (
        'ritual_ZNK15QQmlAllOfFilter24filterAcceptsRowInternalEiRK11QModelI'
        'ndexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QQmlAllOfFilter24filterAcceptsRowInternalEiRK11Q'
          'ModelIndexPK24QQmlSortFilterProxyModel')
    return self.uglySide.call(
        ritual, a0, self._valueOf(a1), self._addressOf(a2),
    )

  @overload(int, QModelIndex, QQmlSortFilterProxyModel)
  @overload(int, QModelIndex, NoneType)
  def filterAcceptsColumnInternal(
      self,
      a0: int,
      a1: QModelIndex,
      a2: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlAllOfFilter::filterAcceptsColumnInternal(int a0,
    const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlalloffilter.html#filterAcceptsColumnInternal

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlAllOfFilter::filterAcceptsColumnInternal(int a0, const
    #      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
    ritual = (
        'ritual_ZNK15QQmlAllOfFilter27filterAcceptsColumnInternalEiRK11QMod'
        'elIndexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QQmlAllOfFilter27filterAcceptsColumnInternalEiRK'
          '11QModelIndexPK24QQmlSortFilterProxyModel')
    return self.uglySide.call(
        ritual, a0, self._valueOf(a1), self._addressOf(a2),
    )

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQmlAllOfFilter::QQmlAllOfFilter(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlalloffilter.html#QQmlAllOfFilter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlAllOfFilter::QQmlAllOfFilter(QObject *parent)
    self._noteCreation(QQmlAllOfFilter, lambda: Rituals.call(
        'ritual_ZN15QQmlAllOfFilterC1EP7QObject',
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

  def d_func(self) -> Optional[QQmlAllOfFilterPrivate]:
    """
    Calls Qt's 'QQmlAllOfFilterPrivate *QQmlAllOfFilter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlalloffilter.html#d_func

    Returns
    -------

    Optional[QQmlAllOfFilterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAllOfFilterPrivate *QQmlAllOfFilter::d_func()
    address = self.uglySide.call('ritual_ZN15QQmlAllOfFilter6d_funcEv')
    from . import QQmlAllOfFilterPrivate
    return QQmlAllOfFilterPrivate._cuteAt(address)
