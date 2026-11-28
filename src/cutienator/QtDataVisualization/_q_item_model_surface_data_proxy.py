"""
QItemModelSurfaceDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qitemmodelsurfacedataproxy.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QSurfaceDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject, QRegularExpression
  from . import QItemModelSurfaceDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QRegularExpression = WAIT['QRegularExpression']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QItemModelSurfaceDataProxy(QSurfaceDataProxy):
  """
  The cute side of Qt's QItemModelSurfaceDataProxy: a plain Python object
  standing in front of one C++ QItemModelSurfaceDataProxy.

  It is built on the cute 'QSurfaceDataProxy', as Qt's
  QItemModelSurfaceDataProxy is built on Qt's QSurfaceDataProxy, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QItemModelSurfaceDataProxy that has a ritual and
  that Python can call so far, 73 names in all: 'metaObject', 'tr',
  'setItemModel', 'itemModel', 'setRowRole', 'rowRole', 'setColumnRole',
  'columnRole', 'setXPosRole', 'xPosRole', 'setYPosRole', 'yPosRole',
  'setZPosRole', 'zPosRole', 'setRowCategories', 'rowCategories',
  'setColumnCategories', 'columnCategories', 'setUseModelCategories',
  'useModelCategories', 'setAutoRowCategories', 'autoRowCategories',
  'setAutoColumnCategories', 'autoColumnCategories', 'remap',
  'rowCategoryIndex', 'columnCategoryIndex', 'setRowRolePattern',
  'rowRolePattern', 'setColumnRolePattern', 'columnRolePattern',
  'setXPosRolePattern', 'xPosRolePattern', 'setYPosRolePattern',
  'yPosRolePattern', 'setZPosRolePattern', 'zPosRolePattern',
  'setRowRoleReplace', 'rowRoleReplace', 'setColumnRoleReplace',
  'columnRoleReplace', 'setXPosRoleReplace', 'xPosRoleReplace',
  'setYPosRoleReplace', 'yPosRoleReplace', 'setZPosRoleReplace',
  'zPosRoleReplace', 'setMultiMatchBehavior', 'multiMatchBehavior',
  'itemModelChanged', 'rowRoleChanged', 'columnRoleChanged',
  'xPosRoleChanged', 'yPosRoleChanged', 'zPosRoleChanged',
  'rowCategoriesChanged', 'columnCategoriesChanged',
  'useModelCategoriesChanged', 'autoRowCategoriesChanged',
  'autoColumnCategoriesChanged', 'rowRolePatternChanged',
  'columnRolePatternChanged', 'xPosRolePatternChanged',
  'yPosRolePatternChanged', 'zPosRolePatternChanged',
  'rowRoleReplaceChanged', 'columnRoleReplaceChanged',
  'xPosRoleReplaceChanged', 'yPosRoleReplaceChanged',
  'zPosRoleReplaceChanged', 'multiMatchBehaviorChanged', 'dptr', 'dptrc'. It
  can be made from Python, in 7 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QItemModelSurfaceDataProxy::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QItemModelSurfaceDataProxy::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QItemModelSurfaceDataProxy::~QItemModelSurfaceDataProxy()': the
    destructor: Python never removes a C++ QItemModelSurfaceDataProxy.

  What has no ritual
  ------------------

  4 of the 87 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QItemModelSurfaceDataProxy is created at the first use, not by
    'QItemModelSurfaceDataProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QItemModelSurfaceDataProxy.
  - Qt tells when it has removed the C++ QItemModelSurfaceDataProxy. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QItemModelSurfaceDataProxy, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class MultiMatchBehavior(CuteNum):
    """
    The enum 'QItemModelSurfaceDataProxy::MultiMatchBehavior' of Qt, with the
    4 names Qt gives in it.
    """

    MMBFirst = Kee[int](0)
    MMBLast = Kee[int](1)
    MMBAverage = Kee[int](2)
    MMBCumulativeY = Kee[int](3)

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
    Calls Qt's 'QString QItemModelSurfaceDataProxy::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#tr

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
    #  QString QItemModelSurfaceDataProxy::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QItemModelSurfaceDataProxy2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemModelSurfaceDataProxy'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QItemModelSurfaceDataProxy Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QItemModelSurfaceDataProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QItemModelSurfaceDataProxy::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QItemModelSurfaceDataProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def itemModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QItemModelSurfaceDataProxy::itemModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#itemModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QItemModelSurfaceDataProxy::itemModel() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy9itemModelEv',
    )
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def rowRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::rowRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#rowRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::rowRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy7rowRoleEv',
    )

  def columnRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::columnRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#columnRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::columnRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy10columnRoleEv',
    )

  def xPosRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::xPosRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#xPosRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::xPosRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy8xPosRoleEv',
    )

  def yPosRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::yPosRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#yPosRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::yPosRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy8yPosRoleEv',
    )

  def zPosRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::zPosRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#zPosRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::zPosRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy8zPosRoleEv',
    )

  def rowCategories(self) -> QStringList:
    """
    Calls Qt's 'QStringList QItemModelSurfaceDataProxy::rowCategories()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#rowCategories

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QItemModelSurfaceDataProxy::rowCategories() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy13rowCategoriesEv',
    )
    return QStringList._cuteOwning(address)

  def columnCategories(self) -> QStringList:
    """
    Calls Qt's 'QStringList QItemModelSurfaceDataProxy::columnCategories()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#columnCategories

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QItemModelSurfaceDataProxy::columnCategories() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy16columnCategoriesEv',
    )
    return QStringList._cuteOwning(address)

  def useModelCategories(self) -> bool:
    """
    Calls Qt's 'bool QItemModelSurfaceDataProxy::useModelCategories() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#useModelCategories
    """
    #  bool QItemModelSurfaceDataProxy::useModelCategories() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy18useModelCategoriesEv',
    )

  def autoRowCategories(self) -> bool:
    """
    Calls Qt's 'bool QItemModelSurfaceDataProxy::autoRowCategories() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#autoRowCategories
    """
    #  bool QItemModelSurfaceDataProxy::autoRowCategories() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy17autoRowCategoriesEv',
    )

  def autoColumnCategories(self) -> bool:
    """
    Calls Qt's 'bool QItemModelSurfaceDataProxy::autoColumnCategories()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html
    """
    #  bool QItemModelSurfaceDataProxy::autoColumnCategories() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy20autoColumnCategoriesEv',
    )

  def rowRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelSurfaceDataProxy::rowRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#rowRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelSurfaceDataProxy::rowRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy14rowRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def columnRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelSurfaceDataProxy::columnRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#columnRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelSurfaceDataProxy::columnRolePattern()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy17columnRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def xPosRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelSurfaceDataProxy::xPosRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#xPosRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelSurfaceDataProxy::xPosRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy15xPosRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def yPosRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelSurfaceDataProxy::yPosRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#yPosRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelSurfaceDataProxy::yPosRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy15yPosRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def zPosRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelSurfaceDataProxy::zPosRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#zPosRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelSurfaceDataProxy::zPosRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy15zPosRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def rowRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::rowRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#rowRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::rowRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy14rowRoleReplaceEv',
    )

  def columnRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::columnRoleReplace()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#columnRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::columnRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy17columnRoleReplaceEv',
    )

  def xPosRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::xPosRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#xPosRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::xPosRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy15xPosRoleReplaceEv',
    )

  def yPosRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::yPosRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#yPosRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::yPosRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy15yPosRoleReplaceEv',
    )

  def zPosRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelSurfaceDataProxy::zPosRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#zPosRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelSurfaceDataProxy::zPosRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy15zPosRoleReplaceEv',
    )

  def multiMatchBehavior(self) -> MultiMatchBehavior:
    """
    Calls Qt's 'MultiMatchBehavior
    QItemModelSurfaceDataProxy::multiMatchBehavior() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#multiMatchBehavior

    Returns
    -------

    MultiMatchBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'MultiMatchBehavior(number)' gives.
    """
    #  MultiMatchBehavior QItemModelSurfaceDataProxy::multiMatchBehavior()
    #      const
    return QItemModelSurfaceDataProxy.MultiMatchBehavior(self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy18multiMatchBehaviorEv',
    ))

  def dptrc(self) -> Optional[QItemModelSurfaceDataProxyPrivate]:
    """
    Calls Qt's 'const QItemModelSurfaceDataProxyPrivate
    *QItemModelSurfaceDataProxy::dptrc() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#dptrc

    Returns
    -------

    Optional[QItemModelSurfaceDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QItemModelSurfaceDataProxyPrivate
    #      *QItemModelSurfaceDataProxy::dptrc() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelSurfaceDataProxy5dptrcEv',
    )
    from . import QItemModelSurfaceDataProxyPrivate
    return QItemModelSurfaceDataProxyPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setItemModel(self, itemModel: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void
    QItemModelSurfaceDataProxy::setItemModel(QAbstractItemModel *itemModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setItemModel

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemModelSurfaceDataProxy::setItemModel(QAbstractItemModel
    #      *itemModel)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy12setItemModelEP18QAbstractIt'
        'emModel',
        self._addressOf(itemModel),
    )

  @overload(str)
  def setRowRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setRowRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setRowRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setRowRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy10setRowRoleERK7QString', role,
    )

  @overload(str)
  def setColumnRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setColumnRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setColumnRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setColumnRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy13setColumnRoleERK7QString',
        role,
    )

  @overload(str)
  def setXPosRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setXPosRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setXPosRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setXPosRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy11setXPosRoleERK7QString',
        role,
    )

  @overload(str)
  def setYPosRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setYPosRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setYPosRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setYPosRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy11setYPosRoleERK7QString',
        role,
    )

  @overload(str)
  def setZPosRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setZPosRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setZPosRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setZPosRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy11setZPosRoleERK7QString',
        role,
    )

  @overload(QStringList)
  def setRowCategories(self, categories: QStringList) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setRowCategories(const
    QStringList &categories)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setRowCategories

    Parameters
    ----------

    categories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QItemModelSurfaceDataProxy::setRowCategories(const QStringList
    #      &categories)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy16setRowCategoriesERK5QListI7'
        'QStringE',
        self._valueOf(categories),
    )

  @overload(QStringList)
  def setColumnCategories(self, categories: QStringList) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setColumnCategories(const
    QStringList &categories)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    categories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QItemModelSurfaceDataProxy::setColumnCategories(const QStringList
    #      &categories)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy19setColumnCategoriesERK5QLis'
        'tI7QStringE',
        self._valueOf(categories),
    )

  @overload(bool)
  def setUseModelCategories(self, enable: bool) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setUseModelCategories(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelSurfaceDataProxy::setUseModelCategories(bool enable)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy21setUseModelCategoriesEb',
        enable,
    )

  @overload(bool)
  def setAutoRowCategories(self, enable: bool) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setAutoRowCategories(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelSurfaceDataProxy::setAutoRowCategories(bool enable)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy20setAutoRowCategoriesEb',
        enable,
    )

  @overload(bool)
  def setAutoColumnCategories(self, enable: bool) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setAutoColumnCategories(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelSurfaceDataProxy::setAutoColumnCategories(bool enable)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy23setAutoColumnCategoriesEb',
        enable,
    )

  @overload(QRegularExpression)
  def setRowRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setRowRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setRowRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::setRowRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy17setRowRolePatternERK18QRegu'
        'larExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setColumnRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setColumnRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::setColumnRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy20setColumnRolePatternERK18QR'
        'egularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setXPosRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setXPosRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setXPosRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::setXPosRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy18setXPosRolePatternERK18QReg'
        'ularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setYPosRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setYPosRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setYPosRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::setYPosRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy18setYPosRolePatternERK18QReg'
        'ularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setZPosRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setZPosRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setZPosRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::setZPosRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy18setZPosRolePatternERK18QReg'
        'ularExpression',
        self._valueOf(pattern),
    )

  @overload(str)
  def setRowRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setRowRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setRowRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setRowRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy17setRowRoleReplaceERK7QStrin'
        'g',
        replace,
    )

  @overload(str)
  def setColumnRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setColumnRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setColumnRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy20setColumnRoleReplaceERK7QSt'
        'ring',
        replace,
    )

  @overload(str)
  def setXPosRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setXPosRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setXPosRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setXPosRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy18setXPosRoleReplaceERK7QStri'
        'ng',
        replace,
    )

  @overload(str)
  def setYPosRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setYPosRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setYPosRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setYPosRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy18setYPosRoleReplaceERK7QStri'
        'ng',
        replace,
    )

  @overload(str)
  def setZPosRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::setZPosRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#setZPosRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::setZPosRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy18setZPosRoleReplaceERK7QStri'
        'ng',
        replace,
    )

  @overload(MultiMatchBehavior)
  def setMultiMatchBehavior(self, behavior: MultiMatchBehavior) -> None:
    """
    Calls Qt's 'void
    QItemModelSurfaceDataProxy::setMultiMatchBehavior(MultiMatchBehavior
    behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    behavior : MultiMatchBehavior
      Passed on as its number.
    """
    #  void QItemModelSurfaceDataProxy::setMultiMatchBehavior(
    #      MultiMatchBehavior behavior)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy21setMultiMatchBehaviorENS_18'
        'MultiMatchBehaviorE',
        behavior.value,
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

  @overload(QAbstractItemModel)
  @overload(QAbstractItemModel, QObject)
  @overload(QAbstractItemModel, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      itemModel: Optional[QAbstractItemModel],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    QAbstractItemModel *itemModel, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    #      QAbstractItemModel *itemModel, QObject *parent)
    self._noteCreation(QItemModelSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelP7QOb'
        'ject',
        self._addressOf(itemModel), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(QObject
    #      *parent)
    self._noteCreation(QItemModelSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelSurfaceDataProxyC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QAbstractItemModel, str)
  @overload(NoneType, str)
  @overload(QAbstractItemModel, str, QObject)
  @overload(QAbstractItemModel, str, NoneType)
  @overload(NoneType, str, QObject)
  @overload(NoneType, str, NoneType)
  def __init__(
      self,
      itemModel: Optional[QAbstractItemModel],
      yPosRole: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    QAbstractItemModel *itemModel, const QString &yPosRole, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    yPosRole : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    #      QAbstractItemModel *itemModel, const QString &yPosRole, QObject
    #      *parent)
    self._noteCreation(QItemModelSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QS'
        'tringP7QObject',
        self._addressOf(itemModel), yPosRole, self._addressOf(parent,
        'QObject'),
    ))

  @overload(QAbstractItemModel, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QAbstractItemModel, str, str, str, QObject)
  @overload(QAbstractItemModel, str, str, str, NoneType)
  @overload(NoneType, str, str, str, QObject)
  @overload(NoneType, str, str, str, NoneType)
  def __init__(
      self,
      itemModel: Optional[QAbstractItemModel],
      rowRole: str,
      columnRole: str,
      yPosRole: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    QAbstractItemModel *itemModel, const QString &rowRole, const QString
    &columnRole, const QString &yPosRole, QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    yPosRole : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    #      QAbstractItemModel *itemModel, const QString &rowRole, const
    #      QString &columnRole, const QString &yPosRole, QObject *parent)
    self._noteCreation(QItemModelSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QS'
        'tringS4_S4_P7QObject',
        self._addressOf(itemModel), rowRole, columnRole, yPosRole,
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QAbstractItemModel, str, str, str, str, str)
  @overload(NoneType, str, str, str, str, str)
  @overload(QAbstractItemModel, str, str, str, str, str, QObject)
  @overload(QAbstractItemModel, str, str, str, str, str, NoneType)
  @overload(NoneType, str, str, str, str, str, QObject)
  @overload(NoneType, str, str, str, str, str, NoneType)
  def __init__(
      self,
      itemModel: Optional[QAbstractItemModel],
      rowRole: str,
      columnRole: str,
      xPosRole: str,
      yPosRole: str,
      zPosRole: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    QAbstractItemModel *itemModel, const QString &rowRole, const QString
    &columnRole, const QString &xPosRole, const QString &yPosRole, const
    QString &zPosRole, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    xPosRole : str
      Passed on as it is: a QString is made of it for the call.

    yPosRole : str
      Passed on as it is: a QString is made of it for the call.

    zPosRole : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    #      QAbstractItemModel *itemModel, const QString &rowRole, const
    #      QString &columnRole, const QString &xPosRole, const QString
    #      &yPosRole, const QString &zPosRole, QObject *parent)
    self._noteCreation(QItemModelSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QS'
        'tringS4_S4_S4_S4_P7QObject',
        self._addressOf(itemModel), rowRole, columnRole, xPosRole, yPosRole,
        zPosRole, self._addressOf(parent, 'QObject'),
    ))

  @overload(QAbstractItemModel, str, str, str, QStringList, QStringList)
  @overload(NoneType, str, str, str, QStringList, QStringList)
  @overload(
      QAbstractItemModel, str, str, str, QStringList, QStringList, QObject,
  )
  @overload(
      QAbstractItemModel, str, str, str, QStringList, QStringList, NoneType,
  )
  @overload(NoneType, str, str, str, QStringList, QStringList, QObject)
  @overload(NoneType, str, str, str, QStringList, QStringList, NoneType)
  def __init__(
      self,
      itemModel: Optional[QAbstractItemModel],
      rowRole: str,
      columnRole: str,
      yPosRole: str,
      rowCategories: QStringList,
      columnCategories: QStringList,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    QAbstractItemModel *itemModel, const QString &rowRole, const QString
    &columnRole, const QString &yPosRole, const QStringList &rowCategories,
    const QStringList &columnCategories, QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    yPosRole : str
      Passed on as it is: a QString is made of it for the call.

    rowCategories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    columnCategories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    #      QAbstractItemModel *itemModel, const QString &rowRole, const
    #      QString &columnRole, const QString &yPosRole, const QStringList
    #      &rowCategories, const QStringList &columnCategories, QObject
    #      *parent)
    self._noteCreation(QItemModelSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QS'
        'tringS4_S4_RK5QListIS2_ES8_P7QObject',
        self._addressOf(itemModel), rowRole, columnRole, yPosRole,
        self._valueOf(rowCategories), self._valueOf(columnCategories),
        self._addressOf(parent, 'QObject'),
    ))

  @overload(
      QAbstractItemModel, str, str, str, str, str, QStringList, QStringList,
  )
  @overload(NoneType, str, str, str, str, str, QStringList, QStringList)
  @overload(
      QAbstractItemModel, str, str, str, str, str, QStringList, QStringList,
      QObject,
  )
  @overload(
      QAbstractItemModel, str, str, str, str, str, QStringList, QStringList,
      NoneType,
  )
  @overload(
      NoneType, str, str, str, str, str, QStringList, QStringList, QObject,
  )
  @overload(
      NoneType, str, str, str, str, str, QStringList, QStringList, NoneType,
  )
  def __init__(
      self,
      itemModel: Optional[QAbstractItemModel],
      rowRole: str,
      columnRole: str,
      xPosRole: str,
      yPosRole: str,
      zPosRole: str,
      rowCategories: QStringList,
      columnCategories: QStringList,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    QAbstractItemModel *itemModel, const QString &rowRole, const QString
    &columnRole, const QString &xPosRole, const QString &yPosRole, const
    QString &zPosRole, const QStringList &rowCategories, const QStringList
    &columnCategories, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    xPosRole : str
      Passed on as it is: a QString is made of it for the call.

    yPosRole : str
      Passed on as it is: a QString is made of it for the call.

    zPosRole : str
      Passed on as it is: a QString is made of it for the call.

    rowCategories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    columnCategories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelSurfaceDataProxy::QItemModelSurfaceDataProxy(
    #      QAbstractItemModel *itemModel, const QString &rowRole, const
    #      QString &columnRole, const QString &xPosRole, const QString
    #      &yPosRole, const QString &zPosRole, const QStringList
    #      &rowCategories, const QStringList &columnCategories, QObject
    #      *parent)
    self._noteCreation(QItemModelSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelSurfaceDataProxyC1EP18QAbstractItemModelRK7QS'
        'tringS4_S4_S4_S4_RK5QListIS2_ES8_P7QObject',
        self._addressOf(itemModel), rowRole, columnRole, xPosRole, yPosRole,
        zPosRole, self._valueOf(rowCategories),
        self._valueOf(columnCategories), self._addressOf(parent, 'QObject'),
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

  @overload(str, str, str, str, str, QStringList, QStringList)
  def remap(
      self,
      rowRole: str,
      columnRole: str,
      xPosRole: str,
      yPosRole: str,
      zPosRole: str,
      rowCategories: QStringList,
      columnCategories: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::remap(const QString
    &rowRole, const QString &columnRole, const QString &xPosRole, const
    QString &yPosRole, const QString &zPosRole, const QStringList
    &rowCategories, const QStringList &columnCategories)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#remap

    Parameters
    ----------

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    xPosRole : str
      Passed on as it is: a QString is made of it for the call.

    yPosRole : str
      Passed on as it is: a QString is made of it for the call.

    zPosRole : str
      Passed on as it is: a QString is made of it for the call.

    rowCategories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    columnCategories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QItemModelSurfaceDataProxy::remap(const QString &rowRole, const
    #      QString &columnRole, const QString &xPosRole, const QString
    #      &yPosRole, const QString &zPosRole, const QStringList
    #      &rowCategories, const QStringList &columnCategories)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy5remapERK7QStringS2_S2_S2_S2_'
        'RK5QListIS0_ES6_',
        rowRole, columnRole, xPosRole, yPosRole, zPosRole,
        self._valueOf(rowCategories), self._valueOf(columnCategories),
    )

  @overload(str)
  def rowCategoryIndex(self, category: str) -> int:
    """
    Calls Qt's 'int QItemModelSurfaceDataProxy::rowCategoryIndex(const
    QString &category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#rowCategoryIndex

    Parameters
    ----------

    category : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QItemModelSurfaceDataProxy::rowCategoryIndex(const QString
    #      &category)
    return self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy16rowCategoryIndexERK7QString',
        category,
    )

  @overload(str)
  def columnCategoryIndex(self, category: str) -> int:
    """
    Calls Qt's 'int QItemModelSurfaceDataProxy::columnCategoryIndex(const
    QString &category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    category : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QItemModelSurfaceDataProxy::columnCategoryIndex(const QString
    #      &category)
    return self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy19columnCategoryIndexERK7QStr'
        'ing',
        category,
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def itemModelChanged(
      self,
      itemModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::itemModelChanged(const
    QAbstractItemModel *itemModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#itemModelChanged

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemModelSurfaceDataProxy::itemModelChanged(const
    #      QAbstractItemModel *itemModel)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy16itemModelChangedEPK18QAbstr'
        'actItemModel',
        self._addressOf(itemModel),
    )

  @overload(str)
  def rowRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::rowRoleChanged(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#rowRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::rowRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy14rowRoleChangedERK7QString',
        role,
    )

  @overload(str)
  def columnRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::columnRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#columnRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::columnRoleChanged(const QString
    #      &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy17columnRoleChangedERK7QStrin'
        'g',
        role,
    )

  @overload(str)
  def xPosRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::xPosRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#xPosRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::xPosRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy15xPosRoleChangedERK7QString',
        role,
    )

  @overload(str)
  def yPosRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::yPosRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#yPosRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::yPosRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy15yPosRoleChangedERK7QString',
        role,
    )

  @overload(str)
  def zPosRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::zPosRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#zPosRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::zPosRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy15zPosRoleChangedERK7QString',
        role,
    )

  def rowCategoriesChanged(self) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::rowCategoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html
    """
    #  void QItemModelSurfaceDataProxy::rowCategoriesChanged()
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy20rowCategoriesChangedEv',
    )

  def columnCategoriesChanged(self) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::columnCategoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html
    """
    #  void QItemModelSurfaceDataProxy::columnCategoriesChanged()
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy23columnCategoriesChangedEv',
    )

  @overload(bool)
  def useModelCategoriesChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QItemModelSurfaceDataProxy::useModelCategoriesChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelSurfaceDataProxy::useModelCategoriesChanged(bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy25useModelCategoriesChangedEb',
        enable,
    )

  @overload(bool)
  def autoRowCategoriesChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QItemModelSurfaceDataProxy::autoRowCategoriesChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelSurfaceDataProxy::autoRowCategoriesChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy24autoRowCategoriesChangedEb',
        enable,
    )

  @overload(bool)
  def autoColumnCategoriesChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QItemModelSurfaceDataProxy::autoColumnCategoriesChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelSurfaceDataProxy::autoColumnCategoriesChanged(bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy27autoColumnCategoriesChanged'
        'Eb',
        enable,
    )

  @overload(QRegularExpression)
  def rowRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::rowRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::rowRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy21rowRolePatternChangedERK18Q'
        'RegularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def columnRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void
    QItemModelSurfaceDataProxy::columnRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::columnRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy24columnRolePatternChangedERK'
        '18QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def xPosRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::xPosRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::xPosRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy22xPosRolePatternChangedERK18'
        'QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def yPosRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::yPosRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::yPosRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy22yPosRolePatternChangedERK18'
        'QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def zPosRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::zPosRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelSurfaceDataProxy::zPosRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy22zPosRolePatternChangedERK18'
        'QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(str)
  def rowRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::rowRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::rowRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy21rowRoleReplaceChangedERK7QS'
        'tring',
        replace,
    )

  @overload(str)
  def columnRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void
    QItemModelSurfaceDataProxy::columnRoleReplaceChanged(const QString
    &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::columnRoleReplaceChanged(const
    #      QString &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy24columnRoleReplaceChangedERK'
        '7QString',
        replace,
    )

  @overload(str)
  def xPosRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::xPosRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::xPosRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy22xPosRoleReplaceChangedERK7Q'
        'String',
        replace,
    )

  @overload(str)
  def yPosRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::yPosRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::yPosRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy22yPosRoleReplaceChangedERK7Q'
        'String',
        replace,
    )

  @overload(str)
  def zPosRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelSurfaceDataProxy::zPosRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelSurfaceDataProxy::zPosRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy22zPosRoleReplaceChangedERK7Q'
        'String',
        replace,
    )

  @overload(MultiMatchBehavior)
  def multiMatchBehaviorChanged(self, behavior: MultiMatchBehavior) -> None:
    """
    Calls Qt's 'void
    QItemModelSurfaceDataProxy::multiMatchBehaviorChanged(MultiMatchBehavior
    behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html

    Parameters
    ----------

    behavior : MultiMatchBehavior
      Passed on as its number.
    """
    #  void QItemModelSurfaceDataProxy::multiMatchBehaviorChanged(
    #      MultiMatchBehavior behavior)
    self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy25multiMatchBehaviorChangedEN'
        'S_18MultiMatchBehaviorE',
        behavior.value,
    )

  def dptr(self) -> Optional[QItemModelSurfaceDataProxyPrivate]:
    """
    Calls Qt's 'QItemModelSurfaceDataProxyPrivate
    *QItemModelSurfaceDataProxy::dptr()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxy.html#dptr

    Returns
    -------

    Optional[QItemModelSurfaceDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemModelSurfaceDataProxyPrivate *QItemModelSurfaceDataProxy::dptr()
    address = self.uglySide.call(
        'ritual_ZN26QItemModelSurfaceDataProxy4dptrEv',
    )
    from . import QItemModelSurfaceDataProxyPrivate
    return QItemModelSurfaceDataProxyPrivate._cuteAt(address)
