"""
QSslConfigurationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsslconfiguration_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSslConfigurationPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QSslConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslConfiguration = WAIT['QSslConfiguration']


class QSslConfigurationPrivate(QSharedData):
  """
  The cute side of Qt's QSslConfigurationPrivate: a plain Python object
  standing in front of one C++ QSslConfigurationPrivate.

  It is built on the cute 'QSharedData', as Qt's QSslConfigurationPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QSslConfigurationPrivate around as a copy, so every C++
  QSslConfigurationPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSslConfigurationPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'peerSessionWasShared'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslConfigurationPrivate::~QSslConfigurationPrivate()': the
    destructor: Python removes its C++ QSslConfigurationPrivate by it, and
    has no other use for it.

  What has no ritual
  ------------------

  6 of the 8 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QSslConfigurationPrivate.

  What to expect
  --------------

  - The C++ QSslConfigurationPrivate is created at the first use, not by
    'QSslConfigurationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslConfigurationPrivate back gives a copy the ritual
    made for Python, in a new cute QSslConfigurationPrivate.
  - Each name of Qt's QSslConfigurationPrivate that has no cute function yet,
    '__init__', 'deepCopyDefaultConfiguration', 'defaultConfiguration',
    'defaultDtlsConfiguration', 'setDefaultConfiguration',
    'setDefaultDtlsConfiguration', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSslConfiguration)
  def peerSessionWasShared(configuration: QSslConfiguration) -> bool:
    """
    Calls Qt's 'bool QSslConfigurationPrivate::peerSessionWasShared(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfigurationprivate.html#peerSessionWasShared

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  bool QSslConfigurationPrivate::peerSessionWasShared(const
    #      QSslConfiguration &configuration)
    return Rituals.call(
        'ritual_ZN24QSslConfigurationPrivate20peerSessionWasSharedERK17QSsl'
        'Configuration',
        CuteMixin._valueOf(configuration),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslConfigurationPrivate'

  #  Qt's '~QSslConfigurationPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QSslConfigurationPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QSslConfigurationPrivateD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSslConfigurationPrivate::QSslConfigurationPrivate()': leans on
    'QSslConfigurationPrivate::defaultSslOptions', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSslConfigurationPrivate.__init__' has no cute function yet. Qt's "
        "'QSslConfigurationPrivate::QSslConfigurationPrivate()': leans on "
        "'QSslConfigurationPrivate::defaultSslOptions', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
  def deepCopyDefaultConfiguration(*__, **_) -> Never:
    """
    Qt's 'void QSslConfigurationPrivate::deepCopyDefaultConfiguration(
    QSslConfigurationPrivate *config)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'globalData'.
    """
    raise NotImplementedError(
        "'QSslConfigurationPrivate.deepCopyDefaultConfiguration' has no "
        "cute function yet. Qt's 'void "
        "QSslConfigurationPrivate::deepCopyDefaultConfiguration(QSslConfigur"
        "ationPrivate *config)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'globalData'.")

  @staticmethod
  def defaultConfiguration(*__, **_) -> Never:
    """
    Qt's 'QSslConfiguration
    QSslConfigurationPrivate::defaultConfiguration()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'globalData'.
    """
    raise NotImplementedError(
        "'QSslConfigurationPrivate.defaultConfiguration' has no cute "
        "function yet. Qt's 'QSslConfiguration "
        "QSslConfigurationPrivate::defaultConfiguration()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'globalData'.")

  @staticmethod
  def defaultDtlsConfiguration(*__, **_) -> Never:
    """
    Qt's 'QSslConfiguration
    QSslConfigurationPrivate::defaultDtlsConfiguration()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'globalData'.
    """
    raise NotImplementedError(
        "'QSslConfigurationPrivate.defaultDtlsConfiguration' has no cute "
        "function yet. Qt's 'QSslConfiguration "
        "QSslConfigurationPrivate::defaultDtlsConfiguration()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'globalData'.")

  @staticmethod
  def setDefaultConfiguration(*__, **_) -> Never:
    """
    Qt's 'void QSslConfigurationPrivate::setDefaultConfiguration(const
    QSslConfiguration &configuration)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'globalData'.
    """
    raise NotImplementedError(
        "'QSslConfigurationPrivate.setDefaultConfiguration' has no cute "
        "function yet. Qt's 'void "
        "QSslConfigurationPrivate::setDefaultConfiguration(const "
        "QSslConfiguration &configuration)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'globalData'.")

  @staticmethod
  def setDefaultDtlsConfiguration(*__, **_) -> Never:
    """
    Qt's 'void QSslConfigurationPrivate::setDefaultDtlsConfiguration(const
    QSslConfiguration &configuration)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'globalData'.
    """
    raise NotImplementedError(
        "'QSslConfigurationPrivate.setDefaultDtlsConfiguration' has no cute "
        "function yet. Qt's 'void "
        "QSslConfigurationPrivate::setDefaultDtlsConfiguration(const "
        "QSslConfiguration &configuration)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'globalData'.")
