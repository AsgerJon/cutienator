"""
QQuickDesignerSupportPropertyChanges binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportpropertychanges_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDesignerSupportPropertyChanges to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDesignerSupportPropertyChanges(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickDesignerSupportPropertyChanges: a plain Python
  object standing in front of one C++ QQuickDesignerSupportPropertyChanges.

  C++ hands a QQuickDesignerSupportPropertyChanges around as a copy, so every
  C++ QQuickDesignerSupportPropertyChanges behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QQuickDesignerSupportPropertyChanges that has a
  ritual and that Python can call so far, 9 names in all: 'detachFromState',
  'attachToState', 'targetObject', 'removeProperty', 'getProperty',
  'changeValue', 'changeExpression', 'stateObject', 'isNormalProperty'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickDesignerSupportPropertyChanges::
    ~QQuickDesignerSupportPropertyChanges()': the destructor: Python removes
    its C++ QQuickDesignerSupportPropertyChanges by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickDesignerSupportPropertyChanges is created at the first use,
    not by 'QQuickDesignerSupportPropertyChanges(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDesignerSupportPropertyChanges back gives a
    copy the ritual made for Python, in a new cute
    QQuickDesignerSupportPropertyChanges.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def detachFromState(propertyChanges: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportPropertyChanges::detachFromState(QObject
    *propertyChanges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportpropertychanges.html

    Parameters
    ----------

    propertyChanges : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportPropertyChanges::detachFromState(QObject
    #      *propertyChanges)
    Rituals.call(
        'ritual_ZN36QQuickDesignerSupportPropertyChanges15detachFromStateEP'
        '7QObject',
        CuteMixin._addressOf(propertyChanges, 'QObject'),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def attachToState(propertyChanges: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportPropertyChanges::attachToState(QObject
    *propertyChanges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportpropertychanges.html

    Parameters
    ----------

    propertyChanges : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportPropertyChanges::attachToState(QObject
    #      *propertyChanges)
    Rituals.call(
        'ritual_ZN36QQuickDesignerSupportPropertyChanges13attachToStateEP7Q'
        'Object',
        CuteMixin._addressOf(propertyChanges, 'QObject'),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def targetObject(propertyChanges: Optional[QObject]) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QQuickDesignerSupportPropertyChanges::targetObject(QObject
    *propertyChanges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportpropertychanges.html

    Parameters
    ----------

    propertyChanges : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDesignerSupportPropertyChanges::targetObject(QObject
    #      *propertyChanges)
    address = Rituals.call(
        'ritual_ZN36QQuickDesignerSupportPropertyChanges12targetObjectEP7QO'
        'bject',
        CuteMixin._addressOf(propertyChanges, 'QObject'),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @staticmethod
  @overload(QObject, QByteArray)
  @overload(NoneType, QByteArray)
  def removeProperty(
      propertyChanges: Optional[QObject],
      propertyName: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportPropertyChanges::removeProperty(QObject
    *propertyChanges, const QQuickDesignerSupport::PropertyName
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportpropertychanges.html

    Parameters
    ----------

    propertyChanges : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickDesignerSupportPropertyChanges::removeProperty(QObject
    #      *propertyChanges, const QQuickDesignerSupport::PropertyName
    #      &propertyName)
    Rituals.call(
        'ritual_ZN36QQuickDesignerSupportPropertyChanges14removePropertyEP7'
        'QObjectRK10QByteArray',
        CuteMixin._addressOf(propertyChanges, 'QObject'),
        CuteMixin._valueOf(propertyName),
    )

  @staticmethod
  @overload(QObject, QByteArray)
  @overload(NoneType, QByteArray)
  def getProperty(
      propertyChanges: Optional[QObject],
      propertyName: QByteArray,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQuickDesignerSupportPropertyChanges::getProperty(QObject
    *propertyChanges, const QQuickDesignerSupport::PropertyName
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportpropertychanges.html

    Parameters
    ----------

    propertyChanges : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickDesignerSupportPropertyChanges::getProperty(QObject
    #      *propertyChanges, const QQuickDesignerSupport::PropertyName
    #      &propertyName)
    address = Rituals.call(
        'ritual_ZN36QQuickDesignerSupportPropertyChanges11getPropertyEP7QOb'
        'jectRK10QByteArray',
        CuteMixin._addressOf(propertyChanges, 'QObject'),
        CuteMixin._valueOf(propertyName),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QObject, QByteArray, QVariant)
  @overload(NoneType, QByteArray, QVariant)
  def changeValue(
      propertyChanges: Optional[QObject],
      propertyName: QByteArray,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportPropertyChanges::changeValue(QObject
    *propertyChanges, const QQuickDesignerSupport::PropertyName
    &propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportpropertychanges.html

    Parameters
    ----------

    propertyChanges : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickDesignerSupportPropertyChanges::changeValue(QObject
    #      *propertyChanges, const QQuickDesignerSupport::PropertyName
    #      &propertyName, const QVariant &value)
    Rituals.call(
        'ritual_ZN36QQuickDesignerSupportPropertyChanges11changeValueEP7QOb'
        'jectRK10QByteArrayRK8QVariant',
        CuteMixin._addressOf(propertyChanges, 'QObject'),
        CuteMixin._valueOf(propertyName), CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(QObject, QByteArray, str)
  @overload(NoneType, QByteArray, str)
  def changeExpression(
      propertyChanges: Optional[QObject],
      propertyName: QByteArray,
      expression: str,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportPropertyChanges::changeExpression(QObject
    *propertyChanges, const QQuickDesignerSupport::PropertyName
    &propertyName, const QString &expression)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportpropertychanges.html

    Parameters
    ----------

    propertyChanges : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    expression : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickDesignerSupportPropertyChanges::changeExpression(QObject
    #      *propertyChanges, const QQuickDesignerSupport::PropertyName
    #      &propertyName, const QString &expression)
    Rituals.call(
        'ritual_ZN36QQuickDesignerSupportPropertyChanges16changeExpressionE'
        'P7QObjectRK10QByteArrayRK7QString',
        CuteMixin._addressOf(propertyChanges, 'QObject'),
        CuteMixin._valueOf(propertyName), expression,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def stateObject(propertyChanges: Optional[QObject]) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QQuickDesignerSupportPropertyChanges::stateObject(QObject
    *propertyChanges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportpropertychanges.html

    Parameters
    ----------

    propertyChanges : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDesignerSupportPropertyChanges::stateObject(QObject
    #      *propertyChanges)
    address = Rituals.call(
        'ritual_ZN36QQuickDesignerSupportPropertyChanges11stateObjectEP7QOb'
        'ject',
        CuteMixin._addressOf(propertyChanges, 'QObject'),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @staticmethod
  @overload(QByteArray)
  def isNormalProperty(propertyName: QByteArray) -> bool:
    """
    Calls Qt's 'bool
    QQuickDesignerSupportPropertyChanges::isNormalProperty(const
    QQuickDesignerSupport::PropertyName &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportpropertychanges.html

    Parameters
    ----------

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QQuickDesignerSupportPropertyChanges::isNormalProperty(const
    #      QQuickDesignerSupport::PropertyName &propertyName)
    return Rituals.call(
        'ritual_ZN36QQuickDesignerSupportPropertyChanges16isNormalPropertyE'
        'RK10QByteArray',
        CuteMixin._valueOf(propertyName),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDesignerSupportPropertyChanges'

  #  Qt's '~QQuickDesignerSupportPropertyChanges()'. Naming it makes this a
  #  value class: Python owns every C++ QQuickDesignerSupportPropertyChanges
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN36QQuickDesignerSupportPropertyChangesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
