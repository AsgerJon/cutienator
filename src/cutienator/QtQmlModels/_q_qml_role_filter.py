"""
QQmlRoleFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlrolefilter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlRoleFilter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlFilterBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQmlFilterBasePrivate, QQmlRoleFilterPrivate
  from . import QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlFilterBasePrivate = WAIT['QQmlFilterBasePrivate']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlRoleFilter(QQmlFilterBase):
  """
  The cute side of Qt's QQmlRoleFilter: a plain Python object standing in
  front of one C++ QQmlRoleFilter.

  It is built on the cute 'QQmlFilterBase', as Qt's QQmlRoleFilter is built
  on Qt's QQmlFilterBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlRoleFilter that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'tr', 'roleName', 'setRoleName',
  'update', 'roleNameChanged', 'itemRole', 'd_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlRoleFilter::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlRoleFilter::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlRoleFilter::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQmlRoleFilter::~QQmlRoleFilter()': the destructor: Python never
    removes a C++ QQmlRoleFilter.
  - Qt's 'const QQmlRoleFilterPrivate *QQmlRoleFilter::d_func() const': takes
    in Python what 'QQmlRoleFilterPrivate *QQmlRoleFilter::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlRoleFilter is created at the first use, not by
    'QQmlRoleFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlRoleFilter.
  - Qt tells when it has removed the C++ QQmlRoleFilter. Every call on the
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
    Calls Qt's 'QString QQmlRoleFilter::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolefilter.html#tr

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
    #  QString QQmlRoleFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQmlRoleFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlRoleFilter'

  #  A C++ QQmlRoleFilter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlRoleFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlRoleFilter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolefilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlRoleFilter::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQmlRoleFilter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def roleName(self) -> str:
    """
    Calls Qt's 'const QString &QQmlRoleFilter::roleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolefilter.html#roleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QQmlRoleFilter::roleName() const
    return self.uglySide.call('ritual_ZNK14QQmlRoleFilter8roleNameEv')

  @overload(QQmlSortFilterProxyModel)
  @overload(NoneType)
  def itemRole(self, proxyModel: Optional[QQmlSortFilterProxyModel]) -> int:
    """
    Calls Qt's 'int QQmlRoleFilter::itemRole(const QQmlSortFilterProxyModel
    *proxyModel) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolefilter.html#itemRole

    Parameters
    ----------

    proxyModel : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlRoleFilter::itemRole(const QQmlSortFilterProxyModel
    #      *proxyModel) const
    return self.uglySide.call(
        'ritual_ZNK14QQmlRoleFilter8itemRoleEPK24QQmlSortFilterProxyModel',
        self._addressOf(proxyModel),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setRoleName(self, roleName: str) -> None:
    """
    Calls Qt's 'void QQmlRoleFilter::setRoleName(const QString &roleName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolefilter.html#setRoleName

    Parameters
    ----------

    roleName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlRoleFilter::setRoleName(const QString &roleName)
    self.uglySide.call(
        'ritual_ZN14QQmlRoleFilter11setRoleNameERK7QString', roleName,
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
    Notes what was given, for Qt's 'QQmlRoleFilter::QQmlRoleFilter(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolefilter.html#QQmlRoleFilter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlRoleFilter::QQmlRoleFilter(QObject *parent)
    self._noteCreation(QQmlRoleFilter, lambda: Rituals.call(
        'ritual_ZN14QQmlRoleFilterC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QQmlFilterBasePrivate)
  @overload(QQmlFilterBasePrivate, QObject)
  @overload(QQmlFilterBasePrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      priv: Optional[QQmlFilterBasePrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlRoleFilter::QQmlRoleFilter(QQmlFilterBasePrivate *priv, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolefilter.html#QQmlRoleFilter

    Parameters
    ----------

    priv : Optional[QQmlFilterBasePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlRoleFilter::QQmlRoleFilter(QQmlFilterBasePrivate *priv, QObject
    #      *parent)
    self._noteCreation(QQmlRoleFilter, lambda: Rituals.call(
        'ritual_ZN14QQmlRoleFilterC1EP21QQmlFilterBasePrivateP7QObject',
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
    Calls Qt's 'void QQmlRoleFilter::update(const QQmlSortFilterProxyModel
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolefilter.html#update

    Parameters
    ----------

    a0 : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlRoleFilter::update(const QQmlSortFilterProxyModel *a0)
    ritual = 'ritual_ZN14QQmlRoleFilter6updateEPK24QQmlSortFilterProxyModel'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQmlRoleFilter6updateEPK24QQmlSortFilterProxyMode'
          'l')
    self.uglySide.call(ritual, self._addressOf(a0))

  def roleNameChanged(self) -> None:
    """
    Calls Qt's 'void QQmlRoleFilter::roleNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrolefilter.html#roleNameChanged
    """
    #  void QQmlRoleFilter::roleNameChanged()
    self.uglySide.call('ritual_ZN14QQmlRoleFilter15roleNameChangedEv')

  def d_func(self) -> Optional[QQmlRoleFilterPrivate]:
    """
    Calls Qt's 'QQmlRoleFilterPrivate *QQmlRoleFilter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrolefilter.html#d_func

    Returns
    -------

    Optional[QQmlRoleFilterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlRoleFilterPrivate *QQmlRoleFilter::d_func()
    address = self.uglySide.call('ritual_ZN14QQmlRoleFilter6d_funcEv')
    from . import QQmlRoleFilterPrivate
    return QQmlRoleFilterPrivate._cuteAt(address)
