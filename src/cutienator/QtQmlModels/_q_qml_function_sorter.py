"""
QQmlFunctionSorter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlfunctionsorter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlFunctionSorter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex, QObject, QPartialOrdering
  from . import QQmlFunctionSorterPrivate, QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QObject = WAIT['QObject']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlFunctionSorter(QQmlParserStatus):
  """
  The cute side of Qt's QQmlFunctionSorter: a plain Python object standing in
  front of one C++ QQmlFunctionSorter.

  What exists
  -----------

  Every function of Qt's QQmlFunctionSorter that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'compare',
  'classBegin', 'componentComplete', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlFunctionSorter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlFunctionSorter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlFunctionSorter::~QQmlFunctionSorter()': the destructor: Python
    never removes a C++ QQmlFunctionSorter.
  - Qt's 'const QQmlFunctionSorterPrivate *QQmlFunctionSorter::d_func()
    const': takes in Python what 'QQmlFunctionSorterPrivate
    *QQmlFunctionSorter::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlFunctionSorter is created at the first use, not by
    'QQmlFunctionSorter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlFunctionSorter.
  - Qt tells when it has removed the C++ QQmlFunctionSorter. Every call on
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
    Calls Qt's 'QString QQmlFunctionSorter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionsorter.html#tr

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
    #  QString QQmlFunctionSorter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQmlFunctionSorter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlFunctionSorter'

  #  Qt's QQmlFunctionSorter is built on more than one class. The part of a
  #  C++ QQmlFunctionSorter that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQmlFunctionSorter_QQmlParserStatus',
  }

  #  A C++ QQmlFunctionSorter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlFunctionSorter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlFunctionSorter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionsorter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlFunctionSorter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlFunctionSorter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex, QModelIndex, QQmlSortFilterProxyModel)
  @overload(QModelIndex, QModelIndex, NoneType)
  def compare(
      self,
      a0: QModelIndex,
      a1: QModelIndex,
      a2: Optional[QQmlSortFilterProxyModel],
  ) -> QPartialOrdering:
    """
    Calls Qt's 'QPartialOrdering QQmlFunctionSorter::compare(const
    QModelIndex &a0, const QModelIndex &a1, const QQmlSortFilterProxyModel
    *a2) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionsorter.html#compare

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPartialOrdering
      A new cute QPartialOrdering around the copy Qt gave back. Python owns
      it.
    """
    #  QPartialOrdering QQmlFunctionSorter::compare(const QModelIndex &a0,
    #      const QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
    ritual = (
        'ritual_ZNK18QQmlFunctionSorter7compareERK11QModelIndexS2_PK24QQmlS'
        'ortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QQmlFunctionSorter7compareERK11QModelIndexS2_PK2'
          '4QQmlSortFilterProxyModel')
    address = self.uglySide.call(
        ritual, self._valueOf(a0), self._valueOf(a1), self._addressOf(a2),
    )
    from ..QtCore import QPartialOrdering
    return QPartialOrdering._cuteOwning(address)

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
    'QQmlFunctionSorter::QQmlFunctionSorter(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfunctionsorter.html#QQmlFunctionSorter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlFunctionSorter::QQmlFunctionSorter(QObject *parent)
    self._noteCreation(QQmlFunctionSorter, lambda: Rituals.call(
        'ritual_ZN18QQmlFunctionSorterC1EP7QObject',
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlFunctionSorter::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionsorter.html#classBegin
    """
    #  void QQmlFunctionSorter::classBegin()
    ritual = 'ritual_ZN18QQmlFunctionSorter10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQmlFunctionSorter10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlFunctionSorter::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfunctionsorter.html#componentComplete
    """
    #  void QQmlFunctionSorter::componentComplete()
    ritual = 'ritual_ZN18QQmlFunctionSorter17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQmlFunctionSorter17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQmlFunctionSorterPrivate]:
    """
    Calls Qt's 'QQmlFunctionSorterPrivate *QQmlFunctionSorter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfunctionsorter.html#d_func

    Returns
    -------

    Optional[QQmlFunctionSorterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlFunctionSorterPrivate *QQmlFunctionSorter::d_func()
    address = self.uglySide.call('ritual_ZN18QQmlFunctionSorter6d_funcEv')
    from . import QQmlFunctionSorterPrivate
    return QQmlFunctionSorterPrivate._cuteAt(address)
