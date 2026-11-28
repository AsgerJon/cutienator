"""
QGeoPositionInfoSourcePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeopositioninfosource_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGeoPositionInfoSourcePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QGeoPositionInfoSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QGeoPositionInfoSourcePrivate(QObjectPrivate):
  """
  The cute side of Qt's QGeoPositionInfoSourcePrivate: a plain Python object
  standing in front of one C++ QGeoPositionInfoSourcePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QGeoPositionInfoSourcePrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoPositionInfoSourcePrivate that has a ritual and
  that Python can call so far, 4 names in all: 'q_func',
  'setPositioningMethods', '_qt_property_interval_offset',
  '_qt_property_methods_offset'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGeoPositionInfoSource
    *QGeoPositionInfoSourcePrivate::q_func() const': takes in Python what
    'QGeoPositionInfoSource *QGeoPositionInfoSourcePrivate::q_func()' takes.
  - Qt's 'QGeoPositionInfoSourcePrivate::~QGeoPositionInfoSourcePrivate()':
    the destructor: Python never removes a C++ QGeoPositionInfoSourcePrivate.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 3 leans on
  'QGeoPositionInfoSourcePrivate; 2 Qt's library has no name for it, and its
  code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QGeoPositionInfoSourcePrivate is created at the first use, not by
    'QGeoPositionInfoSourcePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoPositionInfoSourcePrivate.
  - Each name of Qt's QGeoPositionInfoSourcePrivate that has no cute function
    yet, 'createSourceReal', 'loadFactory', 'loadPluginMetadata', 'plugins',
    'pluginsSorted', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_interval_offset() -> int:
    """
    Calls Qt's 'size_t
    QGeoPositionInfoSourcePrivate::_qt_property_interval_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosourceprivate.html
    """
    #  size_t QGeoPositionInfoSourcePrivate::_qt_property_interval_offset()
    return Rituals.call(
        'ritual_ZN29QGeoPositionInfoSourcePrivate28_qt_property_interval_of'
        'fsetEv',
    )

  @staticmethod
  def _qt_property_methods_offset() -> int:
    """
    Calls Qt's 'size_t
    QGeoPositionInfoSourcePrivate::_qt_property_methods_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosourceprivate.html
    """
    #  size_t QGeoPositionInfoSourcePrivate::_qt_property_methods_offset()
    return Rituals.call(
        'ritual_ZN29QGeoPositionInfoSourcePrivate27_qt_property_methods_off'
        'setEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPositionInfoSourcePrivate'

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

  @overload(QGeoPositionInfoSource.PositioningMethods)
  def setPositioningMethods(
      self,
      methods: QGeoPositionInfoSource.PositioningMethods,
  ) -> None:
    """
    Calls Qt's 'void QGeoPositionInfoSourcePrivate::setPositioningMethods(
    QGeoPositionInfoSource::PositioningMethods methods)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosourceprivate.html

    Parameters
    ----------

    methods : QGeoPositionInfoSource.PositioningMethods
      Passed on as its number.
    """
    #  void QGeoPositionInfoSourcePrivate::setPositioningMethods(
    #      QGeoPositionInfoSource::PositioningMethods methods)
    self.uglySide.call(
        'ritual_ZN29QGeoPositionInfoSourcePrivate21setPositioningMethodsE6Q'
        'FlagsIN22QGeoPositionInfoSource17PositioningMethodEE',
        methods.value,
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

  def q_func(self) -> Optional[QGeoPositionInfoSource]:
    """
    Calls Qt's 'QGeoPositionInfoSource
    *QGeoPositionInfoSourcePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosourceprivate.html#q_func

    Returns
    -------

    Optional[QGeoPositionInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPositionInfoSource *QGeoPositionInfoSourcePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QGeoPositionInfoSourcePrivate6q_funcEv',
    )
    return QGeoPositionInfoSource._cuteAt(address)

  @staticmethod
  def createSourceReal(*__, **_) -> Never:
    """
    Qt's 'QGeoPositionInfoSource
    *QGeoPositionInfoSourcePrivate::createSourceReal(const QCborMap &meta,
    const QVariantMap &parameters, QObject *parent)': leans on
    'QGeoPositionInfoSourcePrivate::loadFactory(QCborMap const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGeoPositionInfoSourcePrivate.createSourceReal' has no cute "
        "function yet. Qt's 'QGeoPositionInfoSource "
        "*QGeoPositionInfoSourcePrivate::createSourceReal(const QCborMap "
        "&meta, const QVariantMap &parameters, QObject *parent)': leans on "
        "'QGeoPositionInfoSourcePrivate::loadFactory(QCborMap const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def loadFactory(*__, **_) -> Never:
    """
    Qt's 'QGeoPositionInfoSourceFactory
    *QGeoPositionInfoSourcePrivate::loadFactory(const QCborMap &meta)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'loader'.
    """
    raise NotImplementedError(
        "'QGeoPositionInfoSourcePrivate.loadFactory' has no cute function "
        "yet. Qt's 'QGeoPositionInfoSourceFactory "
        "*QGeoPositionInfoSourcePrivate::loadFactory(const QCborMap "
        "&meta)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'loader'.")

  @staticmethod
  def loadPluginMetadata(*__, **_) -> Never:
    """
    Qt's 'void
    QGeoPositionInfoSourcePrivate::loadPluginMetadata(QMultiHash<QString,
    QCborMap> &list)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'loader'.
    """
    raise NotImplementedError(
        "'QGeoPositionInfoSourcePrivate.loadPluginMetadata' has no cute "
        "function yet. Qt's 'void "
        "QGeoPositionInfoSourcePrivate::loadPluginMetadata(QMultiHash<QStrin"
        "g, QCborMap> &list)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'loader'.")

  @staticmethod
  def plugins(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QString, QCborMap>
    QGeoPositionInfoSourcePrivate::plugins(bool reload)': leans on
    'QGeoPositionInfoSourcePrivate::loadPluginMetadata(QMultiHash<QString,
    QCborMap>&)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGeoPositionInfoSourcePrivate.plugins' has no cute function yet. "
        "Qt's 'QMultiHash<QString, QCborMap> "
        "QGeoPositionInfoSourcePrivate::plugins(bool reload)': leans on "
        "'QGeoPositionInfoSourcePrivate::loadPluginMetadata(QMultiHash<QStri"
        "ng, QCborMap>&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def pluginsSorted(*__, **_) -> Never:
    """
    Qt's 'QList<QCborMap> QGeoPositionInfoSourcePrivate::pluginsSorted()':
    leans on
    'QGeoPositionInfoSourcePrivate::loadPluginMetadata(QMultiHash<QString,
    QCborMap>&)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGeoPositionInfoSourcePrivate.pluginsSorted' has no cute function "
        "yet. Qt's 'QList<QCborMap> "
        "QGeoPositionInfoSourcePrivate::pluginsSorted()': leans on "
        "'QGeoPositionInfoSourcePrivate::loadPluginMetadata(QMultiHash<QStri"
        "ng, QCborMap>&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
