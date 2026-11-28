"""
QQmlRoleSorter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlrolesorter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlRoleSorter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex, QObject, QPartialOrdering
  from . import QQmlRoleSorterPrivate, QQmlSortFilterProxyModel
  from . import QQmlSorterBasePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QObject = WAIT['QObject']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']
  QQmlSorterBasePrivate = WAIT['QQmlSorterBasePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlRoleSorter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlRoleSorter: a plain Python object standing in
  front of one C++ QQmlRoleSorter.

  What exists
  -----------

  Every function of Qt's QQmlRoleSorter that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'tr', 'roleName', 'setRoleName',
  'compare', 'update', 'roleNameChanged', 'd_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlRoleSorter::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlRoleSorter::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlRoleSorter::~QQmlRoleSorter()': the destructor: Python never
    removes a C++ QQmlRoleSorter.
  - Qt's 'const QQmlRoleSorterPrivate *QQmlRoleSorter::d_func() const': takes
    in Python what 'QQmlRoleSorterPrivate *QQmlRoleSorter::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlRoleSorter is created at the first use, not by
    'QQmlRoleSorter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlRoleSorter.
  - Qt tells when it has removed the C++ QQmlRoleSorter. Every call on the
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
    Calls Qt's 'QString QQmlRoleSorter::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolesorter.html#tr

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
    #  QString QQmlRoleSorter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQmlRoleSorter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlRoleSorter'

  #  A C++ QQmlRoleSorter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlRoleSorter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlRoleSorter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolesorter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlRoleSorter::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQmlRoleSorter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def roleName(self) -> str:
    """
    Calls Qt's 'const QString &QQmlRoleSorter::roleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolesorter.html#roleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QQmlRoleSorter::roleName() const
    return self.uglySide.call('ritual_ZNK14QQmlRoleSorter8roleNameEv')

  @overload(QModelIndex, QModelIndex, QQmlSortFilterProxyModel)
  @overload(QModelIndex, QModelIndex, NoneType)
  def compare(
      self,
      sourceLeft: QModelIndex,
      sourceRight: QModelIndex,
      proxyModel: Optional[QQmlSortFilterProxyModel],
  ) -> QPartialOrdering:
    """
    Calls Qt's 'QPartialOrdering QQmlRoleSorter::compare(const QModelIndex
    &sourceLeft, const QModelIndex &sourceRight, const
    QQmlSortFilterProxyModel *proxyModel) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolesorter.html#compare

    Parameters
    ----------

    sourceLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    proxyModel : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPartialOrdering
      A new cute QPartialOrdering around the copy Qt gave back. Python owns
      it.
    """
    #  QPartialOrdering QQmlRoleSorter::compare(const QModelIndex
    #      &sourceLeft, const QModelIndex &sourceRight, const
    #      QQmlSortFilterProxyModel *proxyModel) const
    ritual = (
        'ritual_ZNK14QQmlRoleSorter7compareERK11QModelIndexS2_PK24QQmlSortF'
        'ilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QQmlRoleSorter7compareERK11QModelIndexS2_PK24QQm'
          'lSortFilterProxyModel')
    address = self.uglySide.call(
        ritual,
        self._valueOf(sourceLeft), self._valueOf(sourceRight),
        self._addressOf(proxyModel),
    )
    from ..QtCore import QPartialOrdering
    return QPartialOrdering._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setRoleName(self, roleName: str) -> None:
    """
    Calls Qt's 'void QQmlRoleSorter::setRoleName(const QString &roleName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolesorter.html#setRoleName

    Parameters
    ----------

    roleName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlRoleSorter::setRoleName(const QString &roleName)
    self.uglySide.call(
        'ritual_ZN14QQmlRoleSorter11setRoleNameERK7QString', roleName,
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
    Notes what was given, for Qt's 'QQmlRoleSorter::QQmlRoleSorter(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolesorter.html#QQmlRoleSorter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlRoleSorter::QQmlRoleSorter(QObject *parent)
    self._noteCreation(QQmlRoleSorter, lambda: Rituals.call(
        'ritual_ZN14QQmlRoleSorterC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QQmlSorterBasePrivate)
  @overload(QQmlSorterBasePrivate, QObject)
  @overload(QQmlSorterBasePrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      priv: Optional[QQmlSorterBasePrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlRoleSorter::QQmlRoleSorter(QQmlSorterBasePrivate *priv, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolesorter.html#QQmlRoleSorter

    Parameters
    ----------

    priv : Optional[QQmlSorterBasePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlRoleSorter::QQmlRoleSorter(QQmlSorterBasePrivate *priv, QObject
    #      *parent)
    self._noteCreation(QQmlRoleSorter, lambda: Rituals.call(
        'ritual_ZN14QQmlRoleSorterC1EP21QQmlSorterBasePrivateP7QObject',
        self._addressOf(priv), self._addressOf(parent, 'QObject'),
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
  def update(self, a0: Optional[QQmlSortFilterProxyModel]) -> None:
    """
    Calls Qt's 'void QQmlRoleSorter::update(const QQmlSortFilterProxyModel
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolesorter.html#update

    Parameters
    ----------

    a0 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlRoleSorter::update(const QQmlSortFilterProxyModel *a0)
    ritual = 'ritual_ZN14QQmlRoleSorter6updateEPK24QQmlSortFilterProxyModel'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQmlRoleSorter6updateEPK24QQmlSortFilterProxyMode'
          'l')
    self.uglySide.call(ritual, self._addressOf(a0))

  def roleNameChanged(self) -> None:
    """
    Calls Qt's 'void QQmlRoleSorter::roleNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrolesorter.html#roleNameChanged
    """
    #  void QQmlRoleSorter::roleNameChanged()
    self.uglySide.call('ritual_ZN14QQmlRoleSorter15roleNameChangedEv')

  def d_func(self) -> Optional[QQmlRoleSorterPrivate]:
    """
    Calls Qt's 'QQmlRoleSorterPrivate *QQmlRoleSorter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolesorter.html#d_func

    Returns
    -------

    Optional[QQmlRoleSorterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlRoleSorterPrivate *QQmlRoleSorter::d_func()
    address = self.uglySide.call('ritual_ZN14QQmlRoleSorter6d_funcEv')
    from . import QQmlRoleSorterPrivate
    return QQmlRoleSorterPrivate._cuteAt(address)
