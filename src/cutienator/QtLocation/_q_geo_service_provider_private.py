"""
QGeoServiceProviderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeoserviceprovider_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoServiceProviderPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGeoServiceProviderPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoServiceProviderPrivate: a plain Python object
  standing in front of one C++ QGeoServiceProviderPrivate.

  What exists
  -----------

  Every function of Qt's QGeoServiceProviderPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'unload'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoServiceProviderPrivate::~QGeoServiceProviderPrivate()': the
    destructor: Python never removes a C++ QGeoServiceProviderPrivate.

  What has no ritual
  ------------------

  7 of the 10 functions Qt declares: 3 leans on 'QGeoServiceProviderPrivate;
  2 a template; 2 Qt's library has no name for it, and its code in Qt's
  source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QGeoServiceProviderPrivate is created at the first use, not by
    'QGeoServiceProviderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoServiceProviderPrivate.
  - Each name of Qt's QGeoServiceProviderPrivate that has no cute function
    yet, 'features', 'filterParameterMap', 'loadMeta', 'loadPlugin',
    'loadPluginMetadata', 'manager', 'plugins', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoServiceProviderPrivate'

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
    'QGeoServiceProviderPrivate::QGeoServiceProviderPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceproviderprivate.html
    """
    #  QGeoServiceProviderPrivate::QGeoServiceProviderPrivate()
    self._noteCreation(QGeoServiceProviderPrivate, lambda: Rituals.call(
        'ritual_ZN26QGeoServiceProviderPrivateC1Ev',
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

  def unload(self) -> None:
    """
    Calls Qt's 'void QGeoServiceProviderPrivate::unload()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceproviderprivate.html#unload
    """
    #  void QGeoServiceProviderPrivate::unload()
    self.uglySide.call('ritual_ZN26QGeoServiceProviderPrivate6unloadEv')

  @staticmethod
  def features(*__, **_) -> Never:
    """
    Qt's 'QGeoServiceProviderPrivate::features': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QGeoServiceProviderPrivate.features' has no cute function yet. "
        "Qt's 'QGeoServiceProviderPrivate::features': a template: a pattern "
        "and no single function.")

  @staticmethod
  def filterParameterMap(*__, **_) -> Never:
    """
    Qt's 'void QGeoServiceProviderPrivate::filterParameterMap()': leans on
    'QGeoServiceProviderPrivate::loadPluginMetadata(QMultiHash<QString,
    QCborMap>&)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGeoServiceProviderPrivate.filterParameterMap' has no cute "
        "function yet. Qt's 'void "
        "QGeoServiceProviderPrivate::filterParameterMap()': leans on "
        "'QGeoServiceProviderPrivate::loadPluginMetadata(QMultiHash<QString,"
        " QCborMap>&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def loadMeta(*__, **_) -> Never:
    """
    Qt's 'void QGeoServiceProviderPrivate::loadMeta()': leans on
    'QGeoServiceProviderPrivate::loadPluginMetadata(QMultiHash<QString,
    QCborMap>&)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGeoServiceProviderPrivate.loadMeta' has no cute function yet. "
        "Qt's 'void QGeoServiceProviderPrivate::loadMeta()': leans on "
        "'QGeoServiceProviderPrivate::loadPluginMetadata(QMultiHash<QString,"
        " QCborMap>&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def loadPlugin(*__, **_) -> Never:
    """
    Qt's 'void QGeoServiceProviderPrivate::loadPlugin(const QVariantMap
    &parameters)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'loader'.
    """
    raise NotImplementedError(
        "'QGeoServiceProviderPrivate.loadPlugin' has no cute function yet. "
        "Qt's 'void QGeoServiceProviderPrivate::loadPlugin(const "
        "QVariantMap &parameters)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'loader'.")

  @staticmethod
  def loadPluginMetadata(*__, **_) -> Never:
    """
    Qt's 'void
    QGeoServiceProviderPrivate::loadPluginMetadata(QMultiHash<QString,
    QCborMap> &list)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'loader'.
    """
    raise NotImplementedError(
        "'QGeoServiceProviderPrivate.loadPluginMetadata' has no cute "
        "function yet. Qt's 'void "
        "QGeoServiceProviderPrivate::loadPluginMetadata(QMultiHash<QString, "
        "QCborMap> &list)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'loader'.")

  @staticmethod
  def manager(*__, **_) -> Never:
    """
    Qt's 'QGeoServiceProviderPrivate::manager': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QGeoServiceProviderPrivate.manager' has no cute function yet. "
        "Qt's 'QGeoServiceProviderPrivate::manager': a template: a pattern "
        "and no single function.")

  @staticmethod
  def plugins(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QString, QCborMap>
    QGeoServiceProviderPrivate::plugins(bool reload)': leans on
    'QGeoServiceProviderPrivate::loadPluginMetadata(QMultiHash<QString,
    QCborMap>&)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGeoServiceProviderPrivate.plugins' has no cute function yet. "
        "Qt's 'QMultiHash<QString, QCborMap> "
        "QGeoServiceProviderPrivate::plugins(bool reload)': leans on "
        "'QGeoServiceProviderPrivate::loadPluginMetadata(QMultiHash<QString,"
        " QCborMap>&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
