"""
QItemModelScatterDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qitemmodelscatterdataproxy.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QScatterDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject, QRegularExpression
  from . import QItemModelScatterDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QRegularExpression = WAIT['QRegularExpression']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QItemModelScatterDataProxy(QScatterDataProxy):
  """
  The cute side of Qt's QItemModelScatterDataProxy: a plain Python object
  standing in front of one C++ QItemModelScatterDataProxy.

  It is built on the cute 'QScatterDataProxy', as Qt's
  QItemModelScatterDataProxy is built on Qt's QScatterDataProxy, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QItemModelScatterDataProxy that has a ritual and
  that Python can call so far, 52 names in all: 'metaObject', 'tr', 'd_func',
  'setItemModel', 'itemModel', 'setXPosRole', 'xPosRole', 'setYPosRole',
  'yPosRole', 'setZPosRole', 'zPosRole', 'setRotationRole', 'rotationRole',
  'setScaleRole', 'scaleRole', 'remap', 'setXPosRolePattern',
  'xPosRolePattern', 'setYPosRolePattern', 'yPosRolePattern',
  'setZPosRolePattern', 'zPosRolePattern', 'setRotationRolePattern',
  'rotationRolePattern', 'setScaleRolePattern', 'scaleRolePattern',
  'setXPosRoleReplace', 'xPosRoleReplace', 'setYPosRoleReplace',
  'yPosRoleReplace', 'setZPosRoleReplace', 'zPosRoleReplace',
  'setRotationRoleReplace', 'rotationRoleReplace', 'setScaleRoleReplace',
  'scaleRoleReplace', 'itemModelChanged', 'xPosRoleChanged',
  'yPosRoleChanged', 'zPosRoleChanged', 'rotationRoleChanged',
  'scaleRoleChanged', 'xPosRolePatternChanged', 'yPosRolePatternChanged',
  'zPosRolePatternChanged', 'rotationRolePatternChanged',
  'scaleRolePatternChanged', 'rotationRoleReplaceChanged',
  'xPosRoleReplaceChanged', 'yPosRoleReplaceChanged',
  'zPosRoleReplaceChanged', 'scaleRoleReplaceChanged'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QItemModelScatterDataProxy::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QItemModelScatterDataProxy::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QItemModelScatterDataProxyPrivate
    *QItemModelScatterDataProxy::d_func() const': takes in Python what
    'QItemModelScatterDataProxyPrivate *QItemModelScatterDataProxy::d_func()'
    takes.
  - Qt's 'QItemModelScatterDataProxy::~QItemModelScatterDataProxy()': the
    destructor: Python never removes a C++ QItemModelScatterDataProxy.

  What has no ritual
  ------------------

  4 of the 65 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QItemModelScatterDataProxy is created at the first use, not by
    'QItemModelScatterDataProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QItemModelScatterDataProxy.
  - Qt tells when it has removed the C++ QItemModelScatterDataProxy. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QItemModelScatterDataProxy::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#tr

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
    #  QString QItemModelScatterDataProxy::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QItemModelScatterDataProxy2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemModelScatterDataProxy'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QItemModelScatterDataProxy Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QItemModelScatterDataProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QItemModelScatterDataProxy::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QItemModelScatterDataProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def itemModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QItemModelScatterDataProxy::itemModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#itemModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QItemModelScatterDataProxy::itemModel() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy9itemModelEv',
    )
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def xPosRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::xPosRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#xPosRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::xPosRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy8xPosRoleEv',
    )

  def yPosRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::yPosRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#yPosRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::yPosRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy8yPosRoleEv',
    )

  def zPosRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::zPosRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#zPosRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::zPosRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy8zPosRoleEv',
    )

  def rotationRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::rotationRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#rotationRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::rotationRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy12rotationRoleEv',
    )

  def scaleRole(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::scaleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#scaleRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::scaleRole() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy9scaleRoleEv',
    )

  def xPosRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelScatterDataProxy::xPosRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#xPosRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelScatterDataProxy::xPosRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy15xPosRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def yPosRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelScatterDataProxy::yPosRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#yPosRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelScatterDataProxy::yPosRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy15yPosRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def zPosRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelScatterDataProxy::zPosRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#zPosRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelScatterDataProxy::zPosRolePattern() const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy15zPosRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def rotationRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelScatterDataProxy::rotationRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelScatterDataProxy::rotationRolePattern()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy19rotationRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def scaleRolePattern(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QItemModelScatterDataProxy::scaleRolePattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#scaleRolePattern

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QItemModelScatterDataProxy::scaleRolePattern()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy16scaleRolePatternEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def xPosRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::xPosRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#xPosRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::xPosRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy15xPosRoleReplaceEv',
    )

  def yPosRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::yPosRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#yPosRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::yPosRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy15yPosRoleReplaceEv',
    )

  def zPosRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::zPosRoleReplace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#zPosRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::zPosRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy15zPosRoleReplaceEv',
    )

  def rotationRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::rotationRoleReplace()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::rotationRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy19rotationRoleReplaceEv',
    )

  def scaleRoleReplace(self) -> str:
    """
    Calls Qt's 'QString QItemModelScatterDataProxy::scaleRoleReplace()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#scaleRoleReplace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QItemModelScatterDataProxy::scaleRoleReplace() const
    return self.uglySide.call(
        'ritual_ZNK26QItemModelScatterDataProxy16scaleRoleReplaceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setItemModel(self, itemModel: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void
    QItemModelScatterDataProxy::setItemModel(QAbstractItemModel *itemModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setItemModel

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemModelScatterDataProxy::setItemModel(QAbstractItemModel
    #      *itemModel)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy12setItemModelEP18QAbstractIt'
        'emModel',
        self._addressOf(itemModel),
    )

  @overload(str)
  def setXPosRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setXPosRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setXPosRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setXPosRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy11setXPosRoleERK7QString',
        role,
    )

  @overload(str)
  def setYPosRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setYPosRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setYPosRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setYPosRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy11setYPosRoleERK7QString',
        role,
    )

  @overload(str)
  def setZPosRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setZPosRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setZPosRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setZPosRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy11setZPosRoleERK7QString',
        role,
    )

  @overload(str)
  def setRotationRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setRotationRole(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setRotationRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setRotationRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy15setRotationRoleERK7QString',
        role,
    )

  @overload(str)
  def setScaleRole(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setScaleRole(const QString
    &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setScaleRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setScaleRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy12setScaleRoleERK7QString',
        role,
    )

  @overload(QRegularExpression)
  def setXPosRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setXPosRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setXPosRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::setXPosRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy18setXPosRolePatternERK18QReg'
        'ularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setYPosRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setYPosRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setYPosRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::setYPosRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy18setYPosRolePatternERK18QReg'
        'ularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setZPosRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setZPosRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setZPosRolePattern

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::setZPosRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy18setZPosRolePatternERK18QReg'
        'ularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setRotationRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setRotationRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::setRotationRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy22setRotationRolePatternERK18'
        'QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def setScaleRolePattern(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setScaleRolePattern(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::setScaleRolePattern(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy19setScaleRolePatternERK18QRe'
        'gularExpression',
        self._valueOf(pattern),
    )

  @overload(str)
  def setXPosRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setXPosRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setXPosRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setXPosRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy18setXPosRoleReplaceERK7QStri'
        'ng',
        replace,
    )

  @overload(str)
  def setYPosRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setYPosRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setYPosRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setYPosRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy18setYPosRoleReplaceERK7QStri'
        'ng',
        replace,
    )

  @overload(str)
  def setZPosRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setZPosRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#setZPosRoleReplace

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setZPosRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy18setZPosRoleReplaceERK7QStri'
        'ng',
        replace,
    )

  @overload(str)
  def setRotationRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setRotationRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setRotationRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy22setRotationRoleReplaceERK7Q'
        'String',
        replace,
    )

  @overload(str)
  def setScaleRoleReplace(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::setScaleRoleReplace(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::setScaleRoleReplace(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy19setScaleRoleReplaceERK7QStr'
        'ing',
        replace,
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
    'QItemModelScatterDataProxy::QItemModelScatterDataProxy(
    QAbstractItemModel *itemModel, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelScatterDataProxy::QItemModelScatterDataProxy(
    #      QAbstractItemModel *itemModel, QObject *parent)
    self._noteCreation(QItemModelScatterDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelScatterDataProxyC1EP18QAbstractItemModelP7QOb'
        'ject',
        self._addressOf(itemModel), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelScatterDataProxy::QItemModelScatterDataProxy(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelScatterDataProxy::QItemModelScatterDataProxy(QObject
    #      *parent)
    self._noteCreation(QItemModelScatterDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelScatterDataProxyC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
      xPosRole: str,
      yPosRole: str,
      zPosRole: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelScatterDataProxy::QItemModelScatterDataProxy(
    QAbstractItemModel *itemModel, const QString &xPosRole, const QString
    &yPosRole, const QString &zPosRole, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

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
    #  QItemModelScatterDataProxy::QItemModelScatterDataProxy(
    #      QAbstractItemModel *itemModel, const QString &xPosRole, const
    #      QString &yPosRole, const QString &zPosRole, QObject *parent)
    self._noteCreation(QItemModelScatterDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelScatterDataProxyC1EP18QAbstractItemModelRK7QS'
        'tringS4_S4_P7QObject',
        self._addressOf(itemModel), xPosRole, yPosRole, zPosRole,
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
      xPosRole: str,
      yPosRole: str,
      zPosRole: str,
      rotationRole: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemModelScatterDataProxy::QItemModelScatterDataProxy(
    QAbstractItemModel *itemModel, const QString &xPosRole, const QString
    &yPosRole, const QString &zPosRole, const QString &rotationRole, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    xPosRole : str
      Passed on as it is: a QString is made of it for the call.

    yPosRole : str
      Passed on as it is: a QString is made of it for the call.

    zPosRole : str
      Passed on as it is: a QString is made of it for the call.

    rotationRole : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemModelScatterDataProxy::QItemModelScatterDataProxy(
    #      QAbstractItemModel *itemModel, const QString &xPosRole, const
    #      QString &yPosRole, const QString &zPosRole, const QString
    #      &rotationRole, QObject *parent)
    self._noteCreation(QItemModelScatterDataProxy, lambda: Rituals.call(
        'ritual_ZN26QItemModelScatterDataProxyC1EP18QAbstractItemModelRK7QS'
        'tringS4_S4_S4_P7QObject',
        self._addressOf(itemModel), xPosRole, yPosRole, zPosRole,
        rotationRole, self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QItemModelScatterDataProxyPrivate]:
    """
    Calls Qt's 'QItemModelScatterDataProxyPrivate
    *QItemModelScatterDataProxy::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#d_func

    Returns
    -------

    Optional[QItemModelScatterDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemModelScatterDataProxyPrivate
    #      *QItemModelScatterDataProxy::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy6d_funcEv',
    )
    from . import QItemModelScatterDataProxyPrivate
    return QItemModelScatterDataProxyPrivate._cuteAt(address)

  @overload(str, str, str, str)
  def remap(
      self,
      xPosRole: str,
      yPosRole: str,
      zPosRole: str,
      rotationRole: str,
  ) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::remap(const QString
    &xPosRole, const QString &yPosRole, const QString &zPosRole, const
    QString &rotationRole)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#remap

    Parameters
    ----------

    xPosRole : str
      Passed on as it is: a QString is made of it for the call.

    yPosRole : str
      Passed on as it is: a QString is made of it for the call.

    zPosRole : str
      Passed on as it is: a QString is made of it for the call.

    rotationRole : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::remap(const QString &xPosRole, const
    #      QString &yPosRole, const QString &zPosRole, const QString
    #      &rotationRole)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy5remapERK7QStringS2_S2_S2_',
        xPosRole, yPosRole, zPosRole, rotationRole,
    )

  @overload(str, str, str, str, str)
  def remap(
      self,
      xPosRole: str,
      yPosRole: str,
      zPosRole: str,
      rotationRole: str,
      scaleRole: str,
  ) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::remap(const QString
    &xPosRole, const QString &yPosRole, const QString &zPosRole, const
    QString &rotationRole, const QString &scaleRole)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#remap

    Parameters
    ----------

    xPosRole : str
      Passed on as it is: a QString is made of it for the call.

    yPosRole : str
      Passed on as it is: a QString is made of it for the call.

    zPosRole : str
      Passed on as it is: a QString is made of it for the call.

    rotationRole : str
      Passed on as it is: a QString is made of it for the call.

    scaleRole : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::remap(const QString &xPosRole, const
    #      QString &yPosRole, const QString &zPosRole, const QString
    #      &rotationRole, const QString &scaleRole)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy5remapERK7QStringS2_S2_S2_S2_',
        xPosRole, yPosRole, zPosRole, rotationRole, scaleRole,
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def itemModelChanged(
      self,
      itemModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::itemModelChanged(const
    QAbstractItemModel *itemModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#itemModelChanged

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemModelScatterDataProxy::itemModelChanged(const
    #      QAbstractItemModel *itemModel)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy16itemModelChangedEPK18QAbstr'
        'actItemModel',
        self._addressOf(itemModel),
    )

  @overload(str)
  def xPosRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::xPosRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#xPosRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::xPosRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy15xPosRoleChangedERK7QString',
        role,
    )

  @overload(str)
  def yPosRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::yPosRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#yPosRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::yPosRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy15yPosRoleChangedERK7QString',
        role,
    )

  @overload(str)
  def zPosRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::zPosRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#zPosRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::zPosRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy15zPosRoleChangedERK7QString',
        role,
    )

  @overload(str)
  def rotationRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::rotationRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::rotationRoleChanged(const QString
    #      &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy19rotationRoleChangedERK7QStr'
        'ing',
        role,
    )

  @overload(str)
  def scaleRoleChanged(self, role: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::scaleRoleChanged(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html#scaleRoleChanged

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::scaleRoleChanged(const QString &role)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy16scaleRoleChangedERK7QString',
        role,
    )

  @overload(QRegularExpression)
  def xPosRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::xPosRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::xPosRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy22xPosRolePatternChangedERK18'
        'QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def yPosRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::yPosRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::yPosRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy22yPosRolePatternChangedERK18'
        'QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def zPosRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::zPosRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::zPosRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy22zPosRolePatternChangedERK18'
        'QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def rotationRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void
    QItemModelScatterDataProxy::rotationRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::rotationRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy26rotationRolePatternChangedE'
        'RK18QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(QRegularExpression)
  def scaleRolePatternChanged(self, pattern: QRegularExpression) -> None:
    """
    Calls Qt's 'void
    QItemModelScatterDataProxy::scaleRolePatternChanged(const
    QRegularExpression &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    pattern : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QItemModelScatterDataProxy::scaleRolePatternChanged(const
    #      QRegularExpression &pattern)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy23scaleRolePatternChangedERK1'
        '8QRegularExpression',
        self._valueOf(pattern),
    )

  @overload(str)
  def rotationRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void
    QItemModelScatterDataProxy::rotationRoleReplaceChanged(const QString
    &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::rotationRoleReplaceChanged(const
    #      QString &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy26rotationRoleReplaceChangedE'
        'RK7QString',
        replace,
    )

  @overload(str)
  def xPosRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::xPosRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::xPosRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy22xPosRoleReplaceChangedERK7Q'
        'String',
        replace,
    )

  @overload(str)
  def yPosRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::yPosRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::yPosRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy22yPosRoleReplaceChangedERK7Q'
        'String',
        replace,
    )

  @overload(str)
  def zPosRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void QItemModelScatterDataProxy::zPosRoleReplaceChanged(const
    QString &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::zPosRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy22zPosRoleReplaceChangedERK7Q'
        'String',
        replace,
    )

  @overload(str)
  def scaleRoleReplaceChanged(self, replace: str) -> None:
    """
    Calls Qt's 'void
    QItemModelScatterDataProxy::scaleRoleReplaceChanged(const QString
    &replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxy.html

    Parameters
    ----------

    replace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemModelScatterDataProxy::scaleRoleReplaceChanged(const QString
    #      &replace)
    self.uglySide.call(
        'ritual_ZN26QItemModelScatterDataProxy23scaleRoleReplaceChangedERK7'
        'QString',
        replace,
    )
