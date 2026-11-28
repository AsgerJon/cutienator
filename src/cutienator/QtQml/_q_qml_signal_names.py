"""
QQmlSignalNames binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlsignalnames_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlSignalNames to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlSignalNames(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSignalNames: a plain Python object standing in
  front of one C++ QQmlSignalNames.

  C++ hands a QQmlSignalNames around as a copy, so every C++ QQmlSignalNames
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSignalNames that has a ritual and that Python
  can call so far, 7 names in all: 'propertyNameToChangedSignalName',
  'propertyNameToChangedHandlerName', 'signalNameToHandlerName',
  'isChangedHandlerName', 'isChangedSignalName', 'isHandlerName',
  'addPrefixToPropertyName'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QByteArray
    QQmlSignalNames::propertyNameToChangedSignalName(QUtf8StringView
    property)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<QString>
    QQmlSignalNames::changedSignalNameToPropertyName(QStringView
    changeSignal)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<QByteArray>
    QQmlSignalNames::changedSignalNameToPropertyName(QUtf8StringView
    changeSignal)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<QString>
    QQmlSignalNames::changedHandlerNameToPropertyName(QStringView handler)':
    gives a type Python has no way to take yet.
  - Qt's 'std::optional<QByteArray>
    QQmlSignalNames::changedHandlerNameToPropertyName(QUtf8StringView
    handler)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<QString>
    QQmlSignalNames::handlerNameToSignalName(QStringView handler)': gives a
    type Python has no way to take yet.
  - Qt's 'std::optional<QString>
    QQmlSignalNames::changedHandlerNameToSignalName(QStringView
    changedHandler)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<QString>
    QQmlSignalNames::badHandlerNameToSignalName(QStringView handler)': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlSignalNames::~QQmlSignalNames()': the destructor: Python
    removes its C++ QQmlSignalNames by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlSignalNames is created at the first use, not by
    'QQmlSignalNames(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSignalNames back gives a copy the ritual made for
    Python, in a new cute QQmlSignalNames.
  - Each name of Qt's QQmlSignalNames that has no cute function yet,
    'badHandlerNameToSignalName', 'changedHandlerNameToPropertyName',
    'changedHandlerNameToSignalName', 'changedSignalNameToPropertyName',
    'handlerNameToSignalName', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def propertyNameToChangedSignalName(property: str) -> str:
    """
    Calls Qt's 'QString
    QQmlSignalNames::propertyNameToChangedSignalName(QStringView property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsignalnames.html

    Parameters
    ----------

    property : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSignalNames::propertyNameToChangedSignalName(QStringView
    #      property)
    return Rituals.call(
        'ritual_ZN15QQmlSignalNames31propertyNameToChangedSignalNameE11QStr'
        'ingView',
        property,
    )

  @staticmethod
  @overload(str)
  def propertyNameToChangedHandlerName(property: str) -> str:
    """
    Calls Qt's 'QString
    QQmlSignalNames::propertyNameToChangedHandlerName(QStringView property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsignalnames.html

    Parameters
    ----------

    property : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSignalNames::propertyNameToChangedHandlerName(QStringView
    #      property)
    return Rituals.call(
        'ritual_ZN15QQmlSignalNames32propertyNameToChangedHandlerNameE11QSt'
        'ringView',
        property,
    )

  @staticmethod
  @overload(str)
  def signalNameToHandlerName(signal: str) -> str:
    """
    Calls Qt's 'QString
    QQmlSignalNames::signalNameToHandlerName(QAnyStringView signal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsignalnames.html#signalNameToHandlerName

    Parameters
    ----------

    signal : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSignalNames::signalNameToHandlerName(QAnyStringView
    #      signal)
    return Rituals.call(
        'ritual_ZN15QQmlSignalNames23signalNameToHandlerNameE14QAnyStringVi'
        'ew',
        signal,
    )

  @staticmethod
  @overload(str)
  def isChangedHandlerName(signalName: str) -> bool:
    """
    Calls Qt's 'bool QQmlSignalNames::isChangedHandlerName(QStringView
    signalName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsignalnames.html#isChangedHandlerName

    Parameters
    ----------

    signalName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSignalNames::isChangedHandlerName(QStringView signalName)
    return Rituals.call(
        'ritual_ZN15QQmlSignalNames20isChangedHandlerNameE11QStringView',
        signalName,
    )

  @staticmethod
  @overload(str)
  def isChangedSignalName(signalName: str) -> bool:
    """
    Calls Qt's 'bool QQmlSignalNames::isChangedSignalName(QStringView
    signalName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsignalnames.html#isChangedSignalName

    Parameters
    ----------

    signalName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSignalNames::isChangedSignalName(QStringView signalName)
    return Rituals.call(
        'ritual_ZN15QQmlSignalNames19isChangedSignalNameE11QStringView',
        signalName,
    )

  @staticmethod
  @overload(str)
  def isHandlerName(signalName: str) -> bool:
    """
    Calls Qt's 'bool QQmlSignalNames::isHandlerName(QStringView signalName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsignalnames.html#isHandlerName

    Parameters
    ----------

    signalName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSignalNames::isHandlerName(QStringView signalName)
    return Rituals.call(
        'ritual_ZN15QQmlSignalNames13isHandlerNameE11QStringView',
        signalName,
    )

  @staticmethod
  @overload(str, str)
  def addPrefixToPropertyName(prefix: str, propertyName: str) -> str:
    """
    Calls Qt's 'QString QQmlSignalNames::addPrefixToPropertyName(QStringView
    prefix, QStringView propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsignalnames.html#addPrefixToPropertyName

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSignalNames::addPrefixToPropertyName(QStringView prefix,
    #      QStringView propertyName)
    return Rituals.call(
        'ritual_ZN15QQmlSignalNames23addPrefixToPropertyNameE11QStringViewS'
        '0_',
        prefix, propertyName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSignalNames'

  #  Qt's '~QQmlSignalNames()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlSignalNames behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QQmlSignalNamesD1Ev'

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

  @staticmethod
  def badHandlerNameToSignalName(*__, **_) -> Never:
    """
    Qt's 'std::optional<QString>
    QQmlSignalNames::badHandlerNameToSignalName(QStringView handler)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSignalNames.badHandlerNameToSignalName' has no cute function "
        "yet. Qt's 'std::optional<QString> "
        "QQmlSignalNames::badHandlerNameToSignalName(QStringView handler)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def changedHandlerNameToPropertyName(*__, **_) -> Never:
    """
    - Qt's 'std::optional<QString>
      QQmlSignalNames::changedHandlerNameToPropertyName(QStringView
      handler)': gives a type Python has no way to take yet.
    - Qt's 'std::optional<QByteArray>
      QQmlSignalNames::changedHandlerNameToPropertyName(QUtf8StringView
      handler)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSignalNames.changedHandlerNameToPropertyName' has no cute "
        "function yet. Qt's 'std::optional<QString> "
        "QQmlSignalNames::changedHandlerNameToPropertyName(QStringView "
        "handler)': gives a type Python has no way to take yet. Qt's "
        "'std::optional<QByteArray> "
        "QQmlSignalNames::changedHandlerNameToPropertyName(QUtf8StringView "
        "handler)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def changedHandlerNameToSignalName(*__, **_) -> Never:
    """
    Qt's 'std::optional<QString>
    QQmlSignalNames::changedHandlerNameToSignalName(QStringView
    changedHandler)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSignalNames.changedHandlerNameToSignalName' has no cute "
        "function yet. Qt's 'std::optional<QString> "
        "QQmlSignalNames::changedHandlerNameToSignalName(QStringView "
        "changedHandler)': gives a type Python has no way to take yet.")

  @staticmethod
  def changedSignalNameToPropertyName(*__, **_) -> Never:
    """
    - Qt's 'std::optional<QString>
      QQmlSignalNames::changedSignalNameToPropertyName(QStringView
      changeSignal)': gives a type Python has no way to take yet.
    - Qt's 'std::optional<QByteArray>
      QQmlSignalNames::changedSignalNameToPropertyName(QUtf8StringView
      changeSignal)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSignalNames.changedSignalNameToPropertyName' has no cute "
        "function yet. Qt's 'std::optional<QString> "
        "QQmlSignalNames::changedSignalNameToPropertyName(QStringView "
        "changeSignal)': gives a type Python has no way to take yet. Qt's "
        "'std::optional<QByteArray> "
        "QQmlSignalNames::changedSignalNameToPropertyName(QUtf8StringView "
        "changeSignal)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def handlerNameToSignalName(*__, **_) -> Never:
    """
    Qt's 'std::optional<QString>
    QQmlSignalNames::handlerNameToSignalName(QStringView handler)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSignalNames.handlerNameToSignalName' has no cute function "
        "yet. Qt's 'std::optional<QString> "
        "QQmlSignalNames::handlerNameToSignalName(QStringView handler)': "
        "gives a type Python has no way to take yet.")
