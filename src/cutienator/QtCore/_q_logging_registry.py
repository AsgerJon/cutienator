"""
QLoggingRegistry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLoggingRegistry to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLoggingCategory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLoggingCategory = WAIT['QLoggingCategory']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLoggingRegistry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLoggingRegistry: a plain Python object standing in
  front of one C++ QLoggingRegistry.

  What exists
  -----------

  Every function of Qt's QLoggingRegistry that has a ritual and that Python
  can call so far, 5 names in all: 'unregisterCategory',
  'registerEnvironmentOverrideForCategory', 'instance', 'updateRules',
  'defaultCategoryFilter'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLoggingRegistry::registerCategory(QLoggingCategory *category,
    QtMsgType enableForLevel)': names the enum 'QtMsgType', whose class
    cannot be named here.
  - Qt's 'QLoggingCategory::CategoryFilter
    QLoggingRegistry::installFilter(QLoggingCategory::CategoryFilter
    filter)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  8 of the 15 functions Qt declares: 4 forbidden; 4 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QLoggingRegistry is created at the first use, not by
    'QLoggingRegistry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLoggingRegistry.
  - Each name of Qt's QLoggingRegistry that has no cute function yet,
    '__init__', 'defaultCategory', 'initializeRules', 'installFilter',
    'registerCategory', 'setApiRules', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QLoggingRegistry]:
    """
    Calls Qt's 'QLoggingRegistry *QLoggingRegistry::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qloggingregistry.html#instance

    Returns
    -------

    Optional[QLoggingRegistry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLoggingRegistry *QLoggingRegistry::instance()
    address = Rituals.call('ritual_ZN16QLoggingRegistry8instanceEv')
    return QLoggingRegistry._cuteAt(address)

  @staticmethod
  @overload(QLoggingCategory)
  @overload(NoneType)
  def defaultCategoryFilter(category: Optional[QLoggingCategory]) -> None:
    """
    Calls Qt's 'void QLoggingRegistry::defaultCategoryFilter(QLoggingCategory
    *category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingregistry.html#defaultCategoryFilter

    Parameters
    ----------

    category : Optional[QLoggingCategory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLoggingRegistry::defaultCategoryFilter(QLoggingCategory
    #      *category)
    Rituals.call(
        'ritual_ZN16QLoggingRegistry21defaultCategoryFilterEP16QLoggingCate'
        'gory',
        CuteMixin._addressOf(category),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLoggingRegistry'

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
    Qt's 'QLoggingRegistry::QLoggingRegistry()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'defaultLoggingCategory'; did you mean
    'defaultCategory'?.
    """
    raise NotImplementedError(
        "'QLoggingRegistry.__init__' has no cute function yet. Qt's "
        "'QLoggingRegistry::QLoggingRegistry()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'defaultLoggingCategory'; "
        "did you mean 'defaultCategory'?.")

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

  @overload(QLoggingCategory)
  @overload(NoneType)
  def unregisterCategory(self, category: Optional[QLoggingCategory]) -> None:
    """
    Calls Qt's 'void QLoggingRegistry::unregisterCategory(QLoggingCategory
    *category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingregistry.html#unregisterCategory

    Parameters
    ----------

    category : Optional[QLoggingCategory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLoggingRegistry::unregisterCategory(QLoggingCategory *category)
    self.uglySide.call(
        'ritual_ZN16QLoggingRegistry18unregisterCategoryEP16QLoggingCategor'
        'y',
        self._addressOf(category),
    )

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def registerEnvironmentOverrideForCategory(
      self,
      categoryName: Optional[str],
      environment: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void
    QLoggingRegistry::registerEnvironmentOverrideForCategory(const char
    *categoryName, const char *environment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qloggingregistry.html

    Parameters
    ----------

    categoryName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    environment : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QLoggingRegistry::registerEnvironmentOverrideForCategory(const
    #      char *categoryName, const char *environment)
    self.uglySide.call(
        'ritual_ZN16QLoggingRegistry38registerEnvironmentOverrideForCategor'
        'yEPKcS1_',
        self._bytesOf(categoryName), self._bytesOf(environment),
    )

  def updateRules(self) -> None:
    """
    Calls Qt's 'void QLoggingRegistry::updateRules()'.

    Qt's own words: https://doc.qt.io/qt-6/qloggingregistry.html#updateRules
    """
    #  void QLoggingRegistry::updateRules()
    self.uglySide.call('ritual_ZN16QLoggingRegistry11updateRulesEv')

  @staticmethod
  def defaultCategory(*__, **_) -> Never:
    """
    Qt's 'QLoggingCategory *QLoggingRegistry::defaultCategory()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'defaultLoggingCategory'; did you mean 'defaultCategory'?.
    """
    raise NotImplementedError(
        "'QLoggingRegistry.defaultCategory' has no cute function yet. Qt's "
        "'QLoggingCategory *QLoggingRegistry::defaultCategory()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'defaultLoggingCategory'; did you mean 'defaultCategory'?.")

  @staticmethod
  def initializeRules(*__, **_) -> Never:
    """
    Qt's 'void QLoggingRegistry::initializeRules()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'debugMsg'.
    """
    raise NotImplementedError(
        "'QLoggingRegistry.initializeRules' has no cute function yet. Qt's "
        "'void QLoggingRegistry::initializeRules()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'debugMsg'.")

  @staticmethod
  def installFilter(*__, **_) -> Never:
    """
    Qt's 'QLoggingCategory::CategoryFilter
    QLoggingRegistry::installFilter(QLoggingCategory::CategoryFilter
    filter)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLoggingRegistry.installFilter' has no cute function yet. Qt's "
        "'QLoggingCategory::CategoryFilter "
        "QLoggingRegistry::installFilter(QLoggingCategory::CategoryFilter "
        "filter)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def registerCategory(*__, **_) -> Never:
    """
    Qt's 'void QLoggingRegistry::registerCategory(QLoggingCategory *category,
    QtMsgType enableForLevel)': names the enum 'QtMsgType', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QLoggingRegistry.registerCategory' has no cute function yet. Qt's "
        "'void QLoggingRegistry::registerCategory(QLoggingCategory "
        "*category, QtMsgType enableForLevel)': names the enum 'QtMsgType', "
        "whose class cannot be named here.")

  @staticmethod
  def setApiRules(*__, **_) -> Never:
    """
    Qt's 'void QLoggingRegistry::setApiRules(const QString &content)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qtLoggingDebug'.
    """
    raise NotImplementedError(
        "'QLoggingRegistry.setApiRules' has no cute function yet. Qt's "
        "'void QLoggingRegistry::setApiRules(const QString &content)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qtLoggingDebug'.")
