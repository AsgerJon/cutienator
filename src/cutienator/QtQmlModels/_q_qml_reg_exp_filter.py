"""
QQmlRegExpFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlregexpfilter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlRegExpFilter to be private: it declares the class in a header
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

  from ..QtCore import QMetaObject, QModelIndex, QRegularExpression
  from . import QQmlRegExpFilterPrivate, QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']
  QRegularExpression = WAIT['QRegularExpression']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlRegExpFilter(QQmlRoleFilter):
  """
  The cute side of Qt's QQmlRegExpFilter: a plain Python object standing in
  front of one C++ QQmlRegExpFilter.

  It is built on the cute 'QQmlRoleFilter', as Qt's QQmlRegExpFilter is built
  on Qt's QQmlRoleFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlRegExpFilter that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'regExp', 'setRegExp',
  'filterAcceptsRowInternal', 'regExpChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlRegExpFilter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlRegExpFilter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQmlRegExpFilterPrivate *QQmlRegExpFilter::d_func() const':
    takes in Python what 'QQmlRegExpFilterPrivate
    *QQmlRegExpFilter::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlRegExpFilter is created at the first use, not by
    'QQmlRegExpFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlRegExpFilter.
  - Qt tells when it has removed the C++ QQmlRegExpFilter. Every call on the
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
    Calls Qt's 'QString QQmlRegExpFilter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlregexpfilter.html#tr

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
    #  QString QQmlRegExpFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQmlRegExpFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlRegExpFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlRegExpFilter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlregexpfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlRegExpFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlRegExpFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def regExp(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression QQmlRegExpFilter::regExp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlregexpfilter.html#regExp

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QQmlRegExpFilter::regExp() const
    address = self.uglySide.call('ritual_ZNK16QQmlRegExpFilter6regExpEv')
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  @overload(int, QModelIndex, QQmlSortFilterProxyModel)
  @overload(int, QModelIndex, NoneType)
  def filterAcceptsRowInternal(
      self,
      row: int,
      sourceParent: QModelIndex,
      proxyModel: Optional[QQmlSortFilterProxyModel],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlRegExpFilter::filterAcceptsRowInternal(int row,
    const QModelIndex &sourceParent, const QQmlSortFilterProxyModel
    *proxyModel) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlregexpfilter.html#filterAcceptsRowInternal

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
    #  bool QQmlRegExpFilter::filterAcceptsRowInternal(int row, const
    #      QModelIndex &sourceParent, const QQmlSortFilterProxyModel
    #      *proxyModel) const
    ritual = (
        'ritual_ZNK16QQmlRegExpFilter24filterAcceptsRowInternalEiRK11QModel'
        'IndexPK24QQmlSortFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QQmlRegExpFilter24filterAcceptsRowInternalEiRK11'
          'QModelIndexPK24QQmlSortFilterProxyModel')
    return self.uglySide.call(
        ritual,
        row, self._valueOf(sourceParent), self._addressOf(proxyModel),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRegularExpression)
  def setRegExp(self, regExp: QRegularExpression) -> None:
    """
    Calls Qt's 'void QQmlRegExpFilter::setRegExp(const QRegularExpression
    &regExp)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlregexpfilter.html#setRegExp

    Parameters
    ----------

    regExp : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QQmlRegExpFilter::setRegExp(const QRegularExpression &regExp)
    self.uglySide.call(
        'ritual_ZN16QQmlRegExpFilter9setRegExpERK18QRegularExpression',
        self._valueOf(regExp),
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
    'QQmlRegExpFilter::QQmlRegExpFilter(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlregexpfilter.html#QQmlRegExpFilter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlRegExpFilter::QQmlRegExpFilter(QObject *parent)
    self._noteCreation(QQmlRegExpFilter, lambda: Rituals.call(
        'ritual_ZN16QQmlRegExpFilterC1EP7QObject',
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

  def regExpChanged(self) -> None:
    """
    Calls Qt's 'void QQmlRegExpFilter::regExpChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlregexpfilter.html#regExpChanged
    """
    #  void QQmlRegExpFilter::regExpChanged()
    self.uglySide.call('ritual_ZN16QQmlRegExpFilter13regExpChangedEv')

  def d_func(self) -> Optional[QQmlRegExpFilterPrivate]:
    """
    Calls Qt's 'QQmlRegExpFilterPrivate *QQmlRegExpFilter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlregexpfilter.html#d_func

    Returns
    -------

    Optional[QQmlRegExpFilterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlRegExpFilterPrivate *QQmlRegExpFilter::d_func()
    address = self.uglySide.call('ritual_ZN16QQmlRegExpFilter6d_funcEv')
    from . import QQmlRegExpFilterPrivate
    return QQmlRegExpFilterPrivate._cuteAt(address)
