"""
QItemModelBarDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qitemmodelbardataproxy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QBarDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject, QRegularExpression
  from . import QItemModelBarDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QRegularExpression = WAIT['QRegularExpression']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QItemModelBarDataProxy(QBarDataProxy):
  """
  The cute side of Qt's QItemModelBarDataProxy: a plain Python object
  standing in front of one C++ QItemModelBarDataProxy.

  It is built on the cute 'QBarDataProxy', as Qt's QItemModelBarDataProxy is
  built on Qt's QBarDataProxy, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QItemModelBarDataProxy that has a ritual and that
  Python can call so far, 63 names in all: 'metaObject', 'tr', 'd_func',
  'setItemModel', 'itemModel', 'setRowRole', 'rowRole', 'setColumnRole',
  'columnRole', 'setValueRole', 'valueRole', 'setRotationRole',
  'rotationRole', 'setRowCategories', 'rowCategories', 'setColumnCategories',
  'columnCategories', 'setUseModelCategories', 'useModelCategories',
  'setAutoRowCategories', 'autoRowCategories', 'setAutoColumnCategories',
  'autoColumnCategories', 'remap', 'rowCategoryIndex', 'columnCategoryIndex',
  'setRowRolePattern', 'rowRolePattern', 'setColumnRolePattern',
  'columnRolePattern', 'setValueRolePattern', 'valueRolePattern',
  'setRotationRolePattern', 'rotationRolePattern', 'setRowRoleReplace',
  'rowRoleReplace', 'setColumnRoleReplace', 'columnRoleReplace',
  'setValueRoleReplace', 'valueRoleReplace', 'setRotationRoleReplace',
  'rotationRoleReplace', 'setMultiMatchBehavior', 'multiMatchBehavior',
  'itemModelChanged', 'rowRoleChanged', 'columnRoleChanged',
  'valueRoleChanged', 'rotationRoleChanged', 'rowCategoriesChanged',
  'columnCategoriesChanged', 'useModelCategoriesChanged',
  'autoRowCategoriesChanged', 'autoColumnCategoriesChanged',
  'rowRolePatternChanged', 'columnRolePatternChanged',
  'valueRolePatternChanged', 'rotationRolePatternChanged',
  'rowRoleReplaceChanged', 'columnRoleReplaceChanged',
  'valueRoleReplaceChanged', 'rotationRoleReplaceChanged',
  'multiMatchBehaviorChanged'. It can be made from Python, in 7 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QItemModelBarDataProxy::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QItemModelBarDataProxy::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QItemModelBarDataProxyPrivate
    *QItemModelBarDataProxy::d_func() const': takes in Python what
    'QItemModelBarDataProxyPrivate *QItemModelBarDataProxy::d_func()' takes.
  - Qt's 'QItemModelBarDataProxy::~QItemModelBarDataProxy()': the destructor:
    Python never removes a C++ QItemModelBarDataProxy.

  What has no ritual
  ------------------

  4 of the 78 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QItemModelBarDataProxy is created at the first use, not by
    'QItemModelBarDataProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QItemModelBarDataProxy.
  - Qt tells when it has removed the C++ QItemModelBarDataProxy. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QItemModelBarDataProxy, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class MultiMatchBehavior(CuteNum, scoped=True):
    """
    The enum 'QItemModelBarDataProxy::MultiMatchBehavior' of Qt, with the 4
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    First = Kee[int](0)
    Last = Kee[int](1)
    Average = Kee[int](2)
    Cumulative = Kee[int](3)

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
    Calls Qt's 'QString QItemModelBarDataProxy::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#tr

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
    #  QString QItemModelBarDataProxy::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QItemModelBarDataProxy2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemModelBarDataProxy'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QItemModelBarDataProxy Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QItemModelBarDataProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QItemModelBarDataProxy::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QItemModelBarDataProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def itemModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QItemModelBarDataProxy::itemModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#itemModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QItemModelBarDataProxy::itemModel() const
    address = self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy9itemModelEv',
    )
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def rowRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelBarDataProxy::rowRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rowRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelBarDataProxy::rowRole() const
    return self.uglySide.call('ritual_ZNK22QItemModelBarDataProxy7rowRoleEv')

  def columnRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelBarDataProxy::columnRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#columnRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelBarDataProxy::columnRole() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy10columnRoleEv',
    )

  def valueRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelBarDataProxy::valueRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#valueRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelBarDataProxy::valueRole() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy9valueRoleEv',
    )

  def rotationRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelBarDataProxy::rotationRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rotationRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelBarDataProxy::rotationRole() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy12rotationRoleEv',
    )

  def rowCategories(self) -> QStringList:
    """
    Calls Qt's 'QStringList QItemModelBarDataProxy::rowCategories() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rowCategories

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QItemModelBarDataProxy::rowCategories() const
    address = self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy13rowCategoriesEv',
    )
    return QStringList._cuteOwning(address)

  def columnCategories(self) -> QStringList:
    """
    Calls Qt's 'QStringList QItemModelBarDataProxy::columnCategories()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#columnCategories

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QItemModelBarDataProxy::columnCategories() const
    address = self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy16columnCategoriesEv',
    )
    return QStringList._cuteOwning(address)

  def useModelCategories(self) -> bool:
    """
    Calls Qt's 'bool QItemModelBarDataProxy::useModelCategories() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#useModelCategories
    """
    #  bool QItemModelBarDataProxy::useModelCategories() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy18useModelCategoriesEv',
    )

  def autoRowCategories(self) -> bool:
    """
    Calls Qt's 'bool QItemModelBarDataProxy::autoRowCategories() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#autoRowCategories
    """
    #  bool QItemModelBarDataProxy::autoRowCategories() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy17autoRowCategoriesEv',
    )

  def autoColumnCategories(self) -> bool:
    """
    Calls Qt's 'bool QItemModelBarDataProxy::autoColumnCategories() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#autoColumnCategories
    """
    #  bool QItemModelBarDataProxy::autoColumnCategories() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy20autoColumnCategoriesEv',
    )

  def rowRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression QItemModelBarDataProxy::rowRolePattern()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rowRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelBarDataProxy::rowRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy14rowRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def columnRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelBarDataProxy::columnRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#columnRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelBarDataProxy::columnRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy17columnRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def valueRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression QItemModelBarDataProxy::valueRolePattern()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#valueRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelBarDataProxy::valueRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy16valueRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def rotationRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelBarDataProxy::rotationRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rotationRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelBarDataProxy::rotationRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy19rotationRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def rowRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelBarDataProxy::rowRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rowRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelBarDataProxy::rowRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy14rowRoleReplaceEv',
    )

  def columnRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelBarDataProxy::columnRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#columnRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelBarDataProxy::columnRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy17columnRoleReplaceEv',
    )

  def valueRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelBarDataProxy::valueRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#valueRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelBarDataProxy::valueRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy16valueRoleReplaceEv',
    )

  def rotationRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelBarDataProxy::rotationRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rotationRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelBarDataProxy::rotationRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy19rotationRoleReplaceEv',
    )

  def multiMatchBehavior(self) -> MultiMatchBehavior:
    """
    Calls Qt's 'QItemModelBarDataProxy::MultiMatchBehavior
    QItemModelBarDataProxy::multiMatchBehavior() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#multiMatchBehavior

    Returns
    -------

    MultiMatchBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'MultiMatchBehavior(number)' gives.
    """
    #  QItemModelBarDataProxy::MultiMatchBehavior
    #      QItemModelBarDataProxy::multiMatchBehavior() const
    return QItemModelBarDataProxy.MultiMatchBehavior(self.uglySide.call(
        'ritual_ZNK22QItemModelBarDataProxy18multiMatchBehaviorEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setItemModel(self, itemModel: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setItemModel(QAbstractItemModel
    *itemModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setItemModel

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemModelBarDataProxy::setItemModel(QAbstractItemModel
    #      *itemModel)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy12setItemModelEP18QAbstractItemMo'
        'del',
        self._addressOf(itemModel),
    )

  @overload(str)
  def setRowRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setRowRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setRowRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::setRowRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy10setRowRoleERK7QString', role,
    )

  @overload(str)
  def setColumnRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setColumnRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setColumnRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::setColumnRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy13setColumnRoleERK7QString', role,
    )

  @overload(str)
  def setValueRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setValueRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setValueRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::setValueRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy12setValueRoleERK7QString', role,
    )

  @overload(str)
  def setRotationRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setRotationRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setRotationRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::setRotationRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy15setRotationRoleERK7QString',
        role,
    )

  @overload(QStringList)
  def setRowCategories(self, categories: QStringList) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setRowCategories(const
    QStringList &categories)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setRowCategories

    Parameters
    ----------

    categories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QItemModelBarDataProxy::setRowCategories(const QStringList
    #      &categories)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy16setRowCategoriesERK5QListI7QStr'
        'ingE',
        self._valueOf(categories),
    )

  @overload(QStringList)
  def setColumnCategories(self, categories: QStringList) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setColumnCategories(const
    QStringList &categories)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setColumnCategories

    Parameters
    ----------

    categories : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QItemModelBarDataProxy::setColumnCategories(const QStringList
    #      &categories)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy19setColumnCategoriesERK5QListI7Q'
        'StringE',
        self._valueOf(categories),
    )

  @overload(bool)
  def setUseModelCategories(self, enable: bool) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setUseModelCategories(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setUseModelCategories

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelBarDataProxy::setUseModelCategories(bool enable)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy21setUseModelCategoriesEb', enable,
    )

  @overload(bool)
  def setAutoRowCategories(self, enable: bool) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setAutoRowCategories(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setAutoRowCategories

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelBarDataProxy::setAutoRowCategories(bool enable)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy20setAutoRowCategoriesEb', enable,
    )

  @overload(bool)
  def setAutoColumnCategories(self, enable: bool) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setAutoColumnCategories(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelBarDataProxy::setAutoColumnCategories(bool enable)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy23setAutoColumnCategoriesEb',
        enable,
    )

  @overload(QRegularExpression)
  def setRowRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setRowRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setRowRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelBarDataProxy::setRowRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy17setRowRolePatternERK18QRegularE'
        'xpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setColumnRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setColumnRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setColumnRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelBarDataProxy::setColumnRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy20setColumnRolePatternERK18QRegul'
        'arExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setValueRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setValueRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setValueRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelBarDataProxy::setValueRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy19setValueRolePatternERK18QRegula'
        'rExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setRotationRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setRotationRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setRotationRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelBarDataProxy::setRotationRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy22setRotationRolePatternERK18QReg'
        'ularExpression',
        self._valueOf(pattern),
    )

  @overload(str)
  def setRowRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setRowRoleReplace(const QString
    &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setRowRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::setRowRoleReplace(const QString &replace)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy17setRowRoleReplaceERK7QString',
        replace,
    )

  @overload(str)
  def setColumnRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setColumnRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setColumnRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::setColumnRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy20setColumnRoleReplaceERK7QString',
        replace,
    )

  @overload(str)
  def setValueRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setValueRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setValueRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::setValueRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy19setValueRoleReplaceERK7QString',
        replace,
    )

  @overload(str)
  def setRotationRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::setRotationRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setRotationRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::setRotationRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy22setRotationRoleReplaceERK7QStri'
        'ng',
        replace,
    )

  @overload(MultiMatchBehavior)
  def setMultiMatchBehavior(self, behavior: MultiMatchBehavior) -> None:
    """
    Calls Qt's 'void
    QItemModelBarDataProxy::setMultiMatchBehavior(QItemModelBarDataProxy::
    MultiMatchBehavior behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#setMultiMatchBehavior

    Parameters
    ----------

    behavior : MultiMatchBehavior
      Passed on as its number.
    """
    #  void QItemModelBarDataProxy::setMultiMatchBehavior(
    #      QItemModelBarDataProxy::MultiMatchBehavior behavior)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy21setMultiMatchBehaviorENS_18Mult'
        'iMatchBehaviorE',
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
    'QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    *itemModel, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#QItemModelBarDataProxy

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    #      *itemModel, QObject *parent)
    self._noteCreation(QItemModelBarDataProxy, lambda: Rituals.call(
        'ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelP7QObject',
        self._addressOf(itemModel), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelBarDataProxy::QItemModelBarDataProxy(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#QItemModelBarDataProxy

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelBarDataProxy::QItemModelBarDataProxy(QObject *parent)
    self._noteCreation(QItemModelBarDataProxy, lambda: Rituals.call(
        'ritual_ZN22QItemModelBarDataProxyC1EP7QObject',
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
      valueRole: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    *itemModel, const QString &valueRole, QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#QItemModelBarDataProxy

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    valueRole : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    #      *itemModel, const QString &valueRole, QObject *parent)
    self._noteCreation(QItemModelBarDataProxy, lambda: Rituals.call(
        'ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStrin'
        'gP7QObject',
        self._addressOf(itemModel), valueRole, self._addressOf(parent,
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
      valueRole: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    *itemModel, const QString &rowRole, const QString &columnRole, const
    QString &valueRole, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#QItemModelBarDataProxy

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    valueRole : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    #      *itemModel, const QString &rowRole, const QString &columnRole,
    #      const QString &valueRole, QObject *parent)
    self._noteCreation(QItemModelBarDataProxy, lambda: Rituals.call(
        'ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStrin'
        'gS4_S4_P7QObject',
        self._addressOf(itemModel), rowRole, columnRole, valueRole,
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QAbstractItemModel, str, str, str, str)
  @overload(NoneType, str, str, str, str)
  @overload(QAbstractItemModel, str, str, str, str, QObject)
  @overload(QAbstractItemModel, str, str, str, str, NoneType)
  @overload(NoneType, str, str, str, str, QObject)
  @overload(NoneType, str, str, str, str, NoneType)
  def __init__(
      self,
      itemModel: Optional[QAbstractItemModel],
      rowRole: str,
      columnRole: str,
      valueRole: str,
      rotationRole: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    *itemModel, const QString &rowRole, const QString &columnRole, const
    QString &valueRole, const QString &rotationRole, QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#QItemModelBarDataProxy

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    valueRole : str
      Passed on as it is: a QString is made of it for the call.

    rotationRole : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    #      *itemModel, const QString &rowRole, const QString &columnRole,
    #      const QString &valueRole, const QString &rotationRole, QObject
    #      *parent)
    self._noteCreation(QItemModelBarDataProxy, lambda: Rituals.call(
        'ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStrin'
        'gS4_S4_S4_P7QObject',
        self._addressOf(itemModel), rowRole, columnRole, valueRole,
        rotationRole, self._addressOf(parent, 'QObject'),
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
      valueRole: str,
      rowCategories: QStringList,
      columnCategories: QStringList,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    *itemModel, const QString &rowRole, const QString &columnRole, const
    QString &valueRole, const QStringList &rowCategories, const QStringList
    &columnCategories, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#QItemModelBarDataProxy

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    valueRole : str
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
    #  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    #      *itemModel, const QString &rowRole, const QString &columnRole,
    #      const QString &valueRole, const QStringList &rowCategories, const
    #      QStringList &columnCategories, QObject *parent)
    self._noteCreation(QItemModelBarDataProxy, lambda: Rituals.call(
        'ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStrin'
        'gS4_S4_RK5QListIS2_ES8_P7QObject',
        self._addressOf(itemModel), rowRole, columnRole, valueRole,
        self._valueOf(rowCategories), self._valueOf(columnCategories),
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QAbstractItemModel, str, str, str, str, QStringList, QStringList)
  @overload(NoneType, str, str, str, str, QStringList, QStringList)
  @overload(
      QAbstractItemModel, str, str, str, str, QStringList, QStringList,
      QObject,
  )
  @overload(
      QAbstractItemModel, str, str, str, str, QStringList, QStringList,
      NoneType,
  )
  @overload(NoneType, str, str, str, str, QStringList, QStringList, QObject)
  @overload(NoneType, str, str, str, str, QStringList, QStringList, NoneType)
  def __init__(
      self,
      itemModel: Optional[QAbstractItemModel],
      rowRole: str,
      columnRole: str,
      valueRole: str,
      rotationRole: str,
      rowCategories: QStringList,
      columnCategories: QStringList,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    *itemModel, const QString &rowRole, const QString &columnRole, const
    QString &valueRole, const QString &rotationRole, const QStringList
    &rowCategories, const QStringList &columnCategories, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#QItemModelBarDataProxy

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    valueRole : str
      Passed on as it is: a QString is made of it for the call.

    rotationRole : str
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
    #  QItemModelBarDataProxy::QItemModelBarDataProxy(QAbstractItemModel
    #      *itemModel, const QString &rowRole, const QString &columnRole,
    #      const QString &valueRole, const QString &rotationRole, const
    #      QStringList &rowCategories, const QStringList &columnCategories,
    #      QObject *parent)
    self._noteCreation(QItemModelBarDataProxy, lambda: Rituals.call(
        'ritual_ZN22QItemModelBarDataProxyC1EP18QAbstractItemModelRK7QStrin'
        'gS4_S4_S4_RK5QListIS2_ES8_P7QObject',
        self._addressOf(itemModel), rowRole, columnRole, valueRole,
        rotationRole, self._valueOf(rowCategories),
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

  def d_func(self) -> Optional[QItemModelBarDataProxyPrivate]:
    """
    Calls Qt's 'QItemModelBarDataProxyPrivate
    *QItemModelBarDataProxy::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#d_func

    Returns
    -------

    Optional[QItemModelBarDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemModelBarDataProxyPrivate *QItemModelBarDataProxy::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy6d_funcEv',
    )
    from . import QItemModelBarDataProxyPrivate
    return QItemModelBarDataProxyPrivate._cuteAt(address)

  @overload(str, str, str, str, QStringList, QStringList)
  def remap(
      self,
      rowRole: str,
      columnRole: str,
      valueRole: str,
      rotationRole: str,
      rowCategories: QStringList,
      columnCategories: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::remap(const QString &rowRole,
    const QString &columnRole, const QString &valueRole, const QString
    &rotationRole, const QStringList &rowCategories, const QStringList
    &columnCategories)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#remap

    Parameters
    ----------

    rowRole : str
      Passed on as it is: a QString is made of it for the call.

    columnRole : str
      Passed on as it is: a QString is made of it for the call.

    valueRole : str
      Passed on as it is: a QString is made of it for the call.

    rotationRole : str
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
    #  void QItemModelBarDataProxy::remap(const QString &rowRole, const
    #      QString &columnRole, const QString &valueRole, const QString
    #      &rotationRole, const QStringList &rowCategories, const QStringList
    #      &columnCategories)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy5remapERK7QStringS2_S2_S2_RK5QLis'
        'tIS0_ES6_',
        rowRole, columnRole, valueRole, rotationRole,
        self._valueOf(rowCategories), self._valueOf(columnCategories),
    )

  @overload(str)
  def rowCategoryIndex(self, category: str) -> int:
    """
    Calls Qt's 'qsizetype QItemModelBarDataProxy::rowCategoryIndex(const
    QString &category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rowCategoryIndex

    Parameters
    ----------

    category : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qsizetype QItemModelBarDataProxy::rowCategoryIndex(const QString
    #      &category)
    return self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy16rowCategoryIndexERK7QString',
        category,
    )

  @overload(str)
  def columnCategoryIndex(self, category: str) -> int:
    """
    Calls Qt's 'qsizetype QItemModelBarDataProxy::columnCategoryIndex(const
    QString &category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#columnCategoryIndex

    Parameters
    ----------

    category : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qsizetype QItemModelBarDataProxy::columnCategoryIndex(const QString
    #      &category)
    return self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy19columnCategoryIndexERK7QString',
        category,
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def itemModelChanged(
      self,
      itemModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::itemModelChanged(const
    QAbstractItemModel *itemModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#itemModelChanged

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemModelBarDataProxy::itemModelChanged(const QAbstractItemModel
    #      *itemModel)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy16itemModelChangedEPK18QAbstractI'
        'temModel',
        self._addressOf(itemModel),
    )

  @overload(str)
  def rowRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::rowRoleChanged(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rowRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::rowRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy14rowRoleChangedERK7QString', role,
    )

  @overload(str)
  def columnRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::columnRoleChanged(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#columnRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::columnRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy17columnRoleChangedERK7QString',
        role,
    )

  @overload(str)
  def valueRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::valueRoleChanged(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#valueRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::valueRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy16valueRoleChangedERK7QString',
        role,
    )

  @overload(str)
  def rotationRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::rotationRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rotationRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::rotationRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy19rotationRoleChangedERK7QString',
        role,
    )

  def rowCategoriesChanged(self) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::rowCategoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rowCategoriesChanged
    """
    #  void QItemModelBarDataProxy::rowCategoriesChanged()
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy20rowCategoriesChangedEv',
    )

  def columnCategoriesChanged(self) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::columnCategoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html
    """
    #  void QItemModelBarDataProxy::columnCategoriesChanged()
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy23columnCategoriesChangedEv',
    )

  @overload(bool)
  def useModelCategoriesChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::useModelCategoriesChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelBarDataProxy::useModelCategoriesChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy25useModelCategoriesChangedEb',
        enable,
    )

  @overload(bool)
  def autoRowCategoriesChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::autoRowCategoriesChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelBarDataProxy::autoRowCategoriesChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy24autoRowCategoriesChangedEb',
        enable,
    )

  @overload(bool)
  def autoColumnCategoriesChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::autoColumnCategoriesChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QItemModelBarDataProxy::autoColumnCategoriesChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy27autoColumnCategoriesChangedEb',
        enable,
    )

  @overload(QRegularExpression)
  def rowRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::rowRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rowRolePatternChanged

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelBarDataProxy::rowRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy21rowRolePatternChangedERK18QRegu'
        'larExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def columnRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::columnRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelBarDataProxy::columnRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy24columnRolePatternChangedERK18QR'
        'egularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def valueRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::valueRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelBarDataProxy::valueRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy23valueRolePatternChangedERK18QRe'
        'gularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def rotationRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::rotationRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelBarDataProxy::rotationRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy26rotationRolePatternChangedERK18'
        'QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(str)
  def rowRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::rowRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html#rowRoleReplaceChanged

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::rowRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy21rowRoleReplaceChangedERK7QStrin'
        'g',
        replace,
    )

  @overload(str)
  def columnRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::columnRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::columnRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy24columnRoleReplaceChangedERK7QSt'
        'ring',
        replace,
    )

  @overload(str)
  def valueRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::valueRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::valueRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy23valueRoleReplaceChangedERK7QStr'
        'ing',
        replace,
    )

  @overload(str)
  def rotationRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::rotationRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelBarDataProxy::rotationRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy26rotationRoleReplaceChangedERK7Q'
        'String',
        replace,
    )

  @overload(MultiMatchBehavior)
  def multiMatchBehaviorChanged(self, behavior: MultiMatchBehavior) -> None:
    """
    Calls Qt's 'void QItemModelBarDataProxy::multiMatchBehaviorChanged(
    QItemModelBarDataProxy::MultiMatchBehavior behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxy.html

    Parameters
    ----------

    behavior : MultiMatchBehavior
      Passed on as its number.
    """
    #  void QItemModelBarDataProxy::multiMatchBehaviorChanged(
    #      QItemModelBarDataProxy::MultiMatchBehavior behavior)
    self.uglySide.call(
        'ritual_ZN22QItemModelBarDataProxy25multiMatchBehaviorChangedENS_18'
        'MultiMatchBehaviorE',
        behavior.value,
    )
