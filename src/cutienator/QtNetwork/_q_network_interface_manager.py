"""
QNetworkInterfaceManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkinterface_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkInterfaceManager to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QNetworkInterfaceManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkInterfaceManager: a plain Python object
  standing in front of one C++ QNetworkInterfaceManager.

  C++ hands a QNetworkInterfaceManager around as a copy, so every C++
  QNetworkInterfaceManager behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QNetworkInterfaceManager yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkInterfaceManager::~QNetworkInterfaceManager()': the
    destructor: Python removes its C++ QNetworkInterfaceManager by it, and
    has no other use for it.

  What has no ritual
  ------------------

  6 of the 8 functions Qt declares: 3 cannot be called and cannot be called
  through the meta-object and cannot be copied; 3 leans on
  'QNetworkInterfaceManager.

  What to expect
  --------------

  - The C++ QNetworkInterfaceManager is created at the first use, not by
    'QNetworkInterfaceManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkInterfaceManager back gives a copy the ritual
    made for Python, in a new cute QNetworkInterfaceManager.
  - Each name of Qt's QNetworkInterfaceManager that has no cute function yet,
    'allInterfaces', 'interfaceFromIndex', 'interfaceFromName',
    'interfaceIndexFromName', 'interfaceNameFromIndex', 'scan', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkInterfaceManager'

  #  Qt's '~QNetworkInterfaceManager()'. Naming it makes this a value class:
  #  Python owns every C++ QNetworkInterfaceManager behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QNetworkInterfaceManagerD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkInterfaceManager::QNetworkInterfaceManager()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterfacemanager.html
    """
    #  QNetworkInterfaceManager::QNetworkInterfaceManager()
    self._noteCreation(QNetworkInterfaceManager, lambda: Rituals.call(
        'ritual_ZN24QNetworkInterfaceManagerC1Ev',
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

  @staticmethod
  def allInterfaces(*__, **_) -> Never:
    """
    Qt's 'QList<QSharedDataPointer<QNetworkInterfacePrivate>>
    QNetworkInterfaceManager::allInterfaces()': leans on
    'QNetworkInterfaceManager::scan()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkInterfaceManager.allInterfaces' has no cute function yet. "
        "Qt's 'QList<QSharedDataPointer<QNetworkInterfacePrivate>> "
        "QNetworkInterfaceManager::allInterfaces()': leans on "
        "'QNetworkInterfaceManager::scan()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def interfaceFromIndex(*__, **_) -> Never:
    """
    Qt's 'QSharedDataPointer<QNetworkInterfacePrivate>
    QNetworkInterfaceManager::interfaceFromIndex(int index)': leans on
    'QNetworkInterfaceManager::scan()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkInterfaceManager.interfaceFromIndex' has no cute function "
        "yet. Qt's 'QSharedDataPointer<QNetworkInterfacePrivate> "
        "QNetworkInterfaceManager::interfaceFromIndex(int index)': leans on "
        "'QNetworkInterfaceManager::scan()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def interfaceFromName(*__, **_) -> Never:
    """
    Qt's 'QSharedDataPointer<QNetworkInterfacePrivate>
    QNetworkInterfaceManager::interfaceFromName(const QString &name)': leans
    on 'QNetworkInterfaceManager::scan()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkInterfaceManager.interfaceFromName' has no cute function "
        "yet. Qt's 'QSharedDataPointer<QNetworkInterfacePrivate> "
        "QNetworkInterfaceManager::interfaceFromName(const QString &name)': "
        "leans on 'QNetworkInterfaceManager::scan()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def interfaceIndexFromName(*__, **_) -> Never:
    """
    Qt's 'uint QNetworkInterfaceManager::interfaceIndexFromName(const QString
    &name)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNetworkInterfaceManager.interfaceIndexFromName' has no cute "
        "function yet. Qt's 'uint "
        "QNetworkInterfaceManager::interfaceIndexFromName(const QString "
        "&name)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def interfaceNameFromIndex(*__, **_) -> Never:
    """
    Qt's 'QString QNetworkInterfaceManager::interfaceNameFromIndex(uint
    index)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNetworkInterfaceManager.interfaceNameFromIndex' has no cute "
        "function yet. Qt's 'QString "
        "QNetworkInterfaceManager::interfaceNameFromIndex(uint index)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def scan(*__, **_) -> Never:
    """
    Qt's 'QList<QNetworkInterfacePrivate *>
    QNetworkInterfaceManager::scan()': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNetworkInterfaceManager.scan' has no cute function yet. Qt's "
        "'QList<QNetworkInterfacePrivate *> "
        "QNetworkInterfaceManager::scan()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")
