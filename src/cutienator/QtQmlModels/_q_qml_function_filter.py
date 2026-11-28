"""
QQmlFunctionFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlfunctionfilter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlFunctionFilter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus
from . import QQmlFilterBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QQmlFunctionFilterPrivate, QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlFunctionFilter(QQmlFilterBase, QQmlParserStatus):
  """
  The cute side of Qt's QQmlFunctionFilter: a plain Python object standing in
  front of one C++ QQmlFunctionFilter.

  It is built on the cute 'QQmlFilterBase', as Qt's QQmlFunctionFilter is
  built on Qt's QQmlFilterBase, and has everything that class has. It is
  built on the cute 'QQmlParserStatus' as well, as Qt's QQmlFunctionFilter is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlFunctionFilter that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr',
  'filterAcceptsRowInternal', 'update', 'classBegin', 'componentComplete',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlFunctionFilter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlFunctionFilter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlFunctionFilter::~QQmlFunctionFilter()': the destructor: Python
    never removes a C++ QQmlFunctionFilter.
  - Qt's 'const QQmlFunctionFilterPrivate *QQmlFunctionFilter::d_func()
    const': takes in Python what 'QQmlFunctionFilterPrivate
    *QQmlFunctionFilter::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlFunctionFilter is created at the first use, not by
    'QQmlFunctionFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlFunctionFilter.
  - Qt tells when it has removed the C++ QQmlFunctionFilter. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlFunctionFilter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionfilter.html#tr

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
    #  QString QQmlFunctionFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQmlFunctionFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlFunctionFilter'

  #  Qt's QQmlFunctionFilter is built on more than one class. The part of a
  #  C++ QQmlFunctionFilter that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQmlFunctionFilter_QQmlParserStatus',
  }

  #  A C++ QQmlFunctionFilter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlFunctionFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlFunctionFilter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlFunctionFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlFunctionFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int, QModelIndex, QQmlSortFilterProxyModel)
  @overload(int, QModelIndex, NoneType)
  def filterAcceptsRowInternal(
      self,
      row: int,
      sourceIndex: QModelIndex,
      a2: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlFunctionFilter::filterAcceptsRowInternal(int row,
    const QModelIndex &sourceIndex, const QQmlSortFilterProxyModel *a2)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfunctionfilter.html#filterAcceptsRowInternal

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
    #  bool QQmlFunctionFilter::filterAcceptsRowInternal(int row, const
    #      QModelIndex &sourceIndex, const QQmlSortFilterProxyModel *a2)
    #      const
    ritual = (
        'ritual_ZNK18QQmlFunctionFilter24filterAcceptsRowInternalEiRK11QMod'
        'elIndexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QQmlFunctionFilter24filterAcceptsRowInternalEiRK'
          '11QModelIndexPK24QQmlSortFilterProxyModel')
    return self.uglySide.call(
        ritual, row, self._valueOf(sourceIndex), self._addressOf(a2),
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
    Notes what was given, for Qt's
    'QQmlFunctionFilter::QQmlFunctionFilter(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfunctionfilter.html#QQmlFunctionFilter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlFunctionFilter::QQmlFunctionFilter(QObject *parent)
    self._noteCreation(QQmlFunctionFilter, lambda: Rituals.call(
        'ritual_ZN18QQmlFunctionFilterC1EP7QObject',
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

  @overload(QQmlSortFilterProxyModel)
  @overload(NoneType)
  def update(self, proxyModel: Optional[QQmlSortFilterProxyModel]) -> None:
    """
    Calls Qt's 'void QQmlFunctionFilter::update(const
    QQmlSortFilterProxyModel *proxyModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionfilter.html#update

    Parameters
    ----------

    proxyModel : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlFunctionFilter::update(const QQmlSortFilterProxyModel
    #      *proxyModel)
    ritual = (
        'ritual_ZN18QQmlFunctionFilter6updateEPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQmlFunctionFilter6updateEPK24QQmlSortFilterProxy'
          'Model')
    self.uglySide.call(ritual, self._addressOf(proxyModel))

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlFunctionFilter::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionfilter.html#classBegin
    """
    #  void QQmlFunctionFilter::classBegin()
    ritual = 'ritual_ZN18QQmlFunctionFilter10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQmlFunctionFilter10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlFunctionFilter::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfunctionfilter.html#componentComplete
    """
    #  void QQmlFunctionFilter::componentComplete()
    ritual = 'ritual_ZN18QQmlFunctionFilter17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQmlFunctionFilter17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQmlFunctionFilterPrivate]:
    """
    Calls Qt's 'QQmlFunctionFilterPrivate *QQmlFunctionFilter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionfilter.html#d_func

    Returns
    -------

    Optional[QQmlFunctionFilterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlFunctionFilterPrivate *QQmlFunctionFilter::d_func()
    address = self.uglySide.call('ritual_ZN18QQmlFunctionFilter6d_funcEv')
    from . import QQmlFunctionFilterPrivate
    return QQmlFunctionFilterPrivate._cuteAt(address)
