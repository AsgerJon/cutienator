"""
QQmlXmlListModelRole binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlXmlListModelRole to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlXmlListModelRole(QObject):
  """
  The cute side of Qt's QQmlXmlListModelRole: a plain Python object standing
  in front of one C++ QQmlXmlListModelRole.

  It is built on the cute 'QObject', as Qt's QQmlXmlListModelRole is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlXmlListModelRole that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'name',
  'setName', 'elementName', 'setElementName', 'attributeName',
  'setAttributeName', 'isValid', 'nameChanged', 'elementNameChanged',
  'attributeNameChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlXmlListModelRole::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlXmlListModelRole::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlXmlListModelRole::~QQmlXmlListModelRole()': the destructor:
    Python never removes a C++ QQmlXmlListModelRole.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlXmlListModelRole is created at the first use, not by
    'QQmlXmlListModelRole(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlXmlListModelRole.
  - Qt tells when it has removed the C++ QQmlXmlListModelRole. Every call on
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
    Calls Qt's 'QString QQmlXmlListModelRole::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#tr

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
    #  QString QQmlXmlListModelRole::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQmlXmlListModelRole2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlXmlListModelRole'

  #  A C++ QQmlXmlListModelRole Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlXmlListModelRole'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlXmlListModelRole::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlXmlListModelRole::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlXmlListModelRole10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlXmlListModelRole::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlXmlListModelRole::name() const
    return self.uglySide.call('ritual_ZNK20QQmlXmlListModelRole4nameEv')

  def elementName(self) -> str:
    """
    Calls Qt's 'QString QQmlXmlListModelRole::elementName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#elementName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlXmlListModelRole::elementName() const
    return self.uglySide.call(
        'ritual_ZNK20QQmlXmlListModelRole11elementNameEv',
    )

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString QQmlXmlListModelRole::attributeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlXmlListModelRole::attributeName() const
    return self.uglySide.call(
        'ritual_ZNK20QQmlXmlListModelRole13attributeNameEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlXmlListModelRole::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#isValid
    """
    #  bool QQmlXmlListModelRole::isValid() const
    return self.uglySide.call('ritual_ZNK20QQmlXmlListModelRole7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlXmlListModelRole::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlXmlListModelRole::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN20QQmlXmlListModelRole7setNameERK7QString', name,
    )

  @overload(str)
  def setElementName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlXmlListModelRole::setElementName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#setElementName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlXmlListModelRole::setElementName(const QString &name)
    self.uglySide.call(
        'ritual_ZN20QQmlXmlListModelRole14setElementNameERK7QString', name,
    )

  @overload(str)
  def setAttributeName(self, attributeName: str) -> None:
    """
    Calls Qt's 'void QQmlXmlListModelRole::setAttributeName(const QString
    &attributeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#setAttributeName

    Parameters
    ----------

    attributeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlXmlListModelRole::setAttributeName(const QString
    #      &attributeName)
    self.uglySide.call(
        'ritual_ZN20QQmlXmlListModelRole16setAttributeNameERK7QString',
        attributeName,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlXmlListModelRole::QQmlXmlListModelRole()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#QQmlXmlListModelRole
    """
    #  QQmlXmlListModelRole::QQmlXmlListModelRole()
    self._noteCreation(QQmlXmlListModelRole, lambda: Rituals.call(
        'ritual_ZN20QQmlXmlListModelRoleC1Ev',
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

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModelRole::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#nameChanged
    """
    #  void QQmlXmlListModelRole::nameChanged()
    self.uglySide.call('ritual_ZN20QQmlXmlListModelRole11nameChangedEv')

  def elementNameChanged(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModelRole::elementNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#elementNameChanged
    """
    #  void QQmlXmlListModelRole::elementNameChanged()
    self.uglySide.call(
        'ritual_ZN20QQmlXmlListModelRole18elementNameChangedEv',
    )

  def attributeNameChanged(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModelRole::attributeNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelrole.html#attributeNameChanged
    """
    #  void QQmlXmlListModelRole::attributeNameChanged()
    self.uglySide.call(
        'ritual_ZN20QQmlXmlListModelRole20attributeNameChangedEv',
    )
