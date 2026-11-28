"""
QQuickStylePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2/6.12.0/QtQuickControls2/private/qquickstyle_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickStylePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQuickStylePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickStylePrivate: a plain Python object standing in
  front of one C++ QQuickStylePrivate.

  C++ hands a QQuickStylePrivate around as a copy, so every C++
  QQuickStylePrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickStylePrivate that has a ritual and that Python
  can call so far, 11 names in all: 'style', 'effectiveStyleName',
  'fallbackStyle', 'isCustomStyle', 'isResolved', 'isUsingDefaultStyle',
  'init', 'reset', 'configFilePath', 'isDarkSystemTheme', 'builtInStyles'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSharedPointer<QSettings> QQuickStylePrivate::settings(const
    QString &group)': gives a type Python has no way to take yet.
  - Qt's 'const QFont *QQuickStylePrivate::readFont(const
    QSharedPointer<QSettings> &settings)': takes a type Python has no way to
    hand over yet.
  - Qt's 'const QPalette *QQuickStylePrivate::readPalette(const
    QSharedPointer<QSettings> &settings)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQuickStylePrivate::~QQuickStylePrivate()': the destructor: Python
    removes its C++ QQuickStylePrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 16 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickStylePrivate is created at the first use, not by
    'QQuickStylePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickStylePrivate back gives a copy the ritual made
    for Python, in a new cute QQuickStylePrivate.
  - Each name of Qt's QQuickStylePrivate that has no cute function yet,
    'exists', 'readFont', 'readPalette', 'settings', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def style() -> str:
    """
    Calls Qt's 'QString QQuickStylePrivate::style()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyleprivate.html#style

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStylePrivate::style()
    return Rituals.call('ritual_ZN18QQuickStylePrivate5styleEv')

  @staticmethod
  @overload(str)
  def effectiveStyleName(styleName: str) -> str:
    """
    Calls Qt's 'QString QQuickStylePrivate::effectiveStyleName(const QString
    &styleName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleprivate.html#effectiveStyleName

    Parameters
    ----------

    styleName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStylePrivate::effectiveStyleName(const QString
    #      &styleName)
    return Rituals.call(
        'ritual_ZN18QQuickStylePrivate18effectiveStyleNameERK7QString',
        styleName,
    )

  @staticmethod
  def fallbackStyle() -> str:
    """
    Calls Qt's 'QString QQuickStylePrivate::fallbackStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleprivate.html#fallbackStyle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStylePrivate::fallbackStyle()
    return Rituals.call('ritual_ZN18QQuickStylePrivate13fallbackStyleEv')

  @staticmethod
  def isCustomStyle() -> bool:
    """
    Calls Qt's 'bool QQuickStylePrivate::isCustomStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleprivate.html#isCustomStyle
    """
    #  bool QQuickStylePrivate::isCustomStyle()
    return Rituals.call('ritual_ZN18QQuickStylePrivate13isCustomStyleEv')

  @staticmethod
  def isResolved() -> bool:
    """
    Calls Qt's 'bool QQuickStylePrivate::isResolved()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyleprivate.html#isResolved
    """
    #  bool QQuickStylePrivate::isResolved()
    return Rituals.call('ritual_ZN18QQuickStylePrivate10isResolvedEv')

  @staticmethod
  def isUsingDefaultStyle() -> bool:
    """
    Calls Qt's 'bool QQuickStylePrivate::isUsingDefaultStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleprivate.html#isUsingDefaultStyle
    """
    #  bool QQuickStylePrivate::isUsingDefaultStyle()
    return Rituals.call(
        'ritual_ZN18QQuickStylePrivate19isUsingDefaultStyleEv',
    )

  @staticmethod
  def init() -> None:
    """
    Calls Qt's 'void QQuickStylePrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyleprivate.html#init
    """
    #  void QQuickStylePrivate::init()
    Rituals.call('ritual_ZN18QQuickStylePrivate4initEv')

  @staticmethod
  def reset() -> None:
    """
    Calls Qt's 'void QQuickStylePrivate::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyleprivate.html#reset
    """
    #  void QQuickStylePrivate::reset()
    Rituals.call('ritual_ZN18QQuickStylePrivate5resetEv')

  @staticmethod
  def configFilePath() -> str:
    """
    Calls Qt's 'QString QQuickStylePrivate::configFilePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleprivate.html#configFilePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStylePrivate::configFilePath()
    return Rituals.call('ritual_ZN18QQuickStylePrivate14configFilePathEv')

  @staticmethod
  def isDarkSystemTheme() -> bool:
    """
    Calls Qt's 'bool QQuickStylePrivate::isDarkSystemTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleprivate.html#isDarkSystemTheme
    """
    #  bool QQuickStylePrivate::isDarkSystemTheme()
    return Rituals.call('ritual_ZN18QQuickStylePrivate17isDarkSystemThemeEv')

  @staticmethod
  def builtInStyles() -> QStringList:
    """
    Calls Qt's 'QStringList QQuickStylePrivate::builtInStyles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleprivate.html#builtInStyles

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickStylePrivate::builtInStyles()
    address = Rituals.call('ritual_ZN18QQuickStylePrivate13builtInStylesEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStylePrivate'

  #  Qt's '~QQuickStylePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickStylePrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuickStylePrivateD1Ev'

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
  def exists(*__, **_) -> Never:
    """
    Qt's 'bool QQuickStylePrivate::exists()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickStylePrivate.exists' has no cute function yet. Qt's 'bool "
        "QQuickStylePrivate::exists()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def readFont(*__, **_) -> Never:
    """
    Qt's 'const QFont *QQuickStylePrivate::readFont(const
    QSharedPointer<QSettings> &settings)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuickStylePrivate.readFont' has no cute function yet. Qt's "
        "'const QFont *QQuickStylePrivate::readFont(const "
        "QSharedPointer<QSettings> &settings)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def readPalette(*__, **_) -> Never:
    """
    Qt's 'const QPalette *QQuickStylePrivate::readPalette(const
    QSharedPointer<QSettings> &settings)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuickStylePrivate.readPalette' has no cute function yet. Qt's "
        "'const QPalette *QQuickStylePrivate::readPalette(const "
        "QSharedPointer<QSettings> &settings)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def settings(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QSettings> QQuickStylePrivate::settings(const
    QString &group)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickStylePrivate.settings' has no cute function yet. Qt's "
        "'QSharedPointer<QSettings> QQuickStylePrivate::settings(const "
        "QString &group)': gives a type Python has no way to take yet.")
