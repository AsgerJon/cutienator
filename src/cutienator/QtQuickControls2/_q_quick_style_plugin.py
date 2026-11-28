"""
QQuickStylePlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2/6.12.0/QtQuickControls2/private/qquickstyleplugin_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickStylePlugin to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlExtensionPlugin

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuickTemplates2 import QQuickTheme
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickTheme = WAIT['QQuickTheme']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStylePlugin(QQmlExtensionPlugin):
  """
  The cute side of Qt's QQuickStylePlugin: a plain Python object standing in
  front of one C++ QQuickStylePlugin.

  It is built on the cute 'QQmlExtensionPlugin', as Qt's QQuickStylePlugin is
  built on Qt's QQmlExtensionPlugin, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStylePlugin that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'name',
  'initializeTheme', 'updateTheme', 'registerTypes', 'unregisterTypes',
  'createTheme'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStylePlugin::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickStylePlugin::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickStylePlugin::~QQuickStylePlugin()': the destructor: Python
    never removes a C++ QQuickStylePlugin.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickStylePlugin is created at the first use, not by
    'QQuickStylePlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStylePlugin.
  - Qt tells when it has removed the C++ QQuickStylePlugin. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickStylePlugin::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyleplugin.html#tr

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
    #  QString QQuickStylePlugin::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickStylePlugin2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStylePlugin'

  #  A C++ QQuickStylePlugin Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStylePlugin'

  #  The functions Qt calls itself that QQuickStylePlugin is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK17QQuickStylePlugin4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'initializeTheme': (
          ('_ZN17QQuickStylePlugin15initializeThemeEP11QQuickTheme',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuickTemplates2:QQuickTheme'),
           )),
      ),
      'updateTheme': (
          ('_ZN17QQuickStylePlugin11updateThemeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickStylePlugin::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyleplugin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStylePlugin::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickStylePlugin10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickStylePlugin::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyleplugin.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStylePlugin::name() const
    return self.uglySide.call('ritual_ZNK17QQuickStylePlugin4nameEv')

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStylePlugin::QQuickStylePlugin(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleplugin.html#QQuickStylePlugin

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStylePlugin::QQuickStylePlugin(QObject *parent)
    self._noteCreation(QQuickStylePlugin, lambda: Rituals.call(
        'ritual_ZN17QQuickStylePluginC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QQuickTheme)
  @overload(NoneType)
  def initializeTheme(self, theme: Optional[QQuickTheme]) -> None:
    """
    Calls Qt's 'void QQuickStylePlugin::initializeTheme(QQuickTheme *theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleplugin.html#initializeTheme

    Parameters
    ----------

    theme : Optional[QQuickTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStylePlugin::initializeTheme(QQuickTheme *theme)
    self.uglySide.call(
        'ritual_ZN17QQuickStylePlugin15initializeThemeEP11QQuickTheme',
        self._addressOf(theme),
    )

  def updateTheme(self) -> None:
    """
    Calls Qt's 'void QQuickStylePlugin::updateTheme()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyleplugin.html#updateTheme
    """
    #  void QQuickStylePlugin::updateTheme()
    ritual = 'ritual_ZN17QQuickStylePlugin11updateThemeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickStylePlugin11updateThemeEv'
    self.uglySide.call(ritual)

  @overload(str)
  @overload(NoneType)
  def registerTypes(self, uri: Optional[str]) -> None:
    """
    Calls Qt's 'void QQuickStylePlugin::registerTypes(const char *uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleplugin.html#registerTypes

    Parameters
    ----------

    uri : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQuickStylePlugin::registerTypes(const char *uri)
    self.uglySide.call(
        'ritual_ZN17QQuickStylePlugin13registerTypesEPKc',
        self._bytesOf(uri),
    )

  def unregisterTypes(self) -> None:
    """
    Calls Qt's 'void QQuickStylePlugin::unregisterTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstyleplugin.html#unregisterTypes
    """
    #  void QQuickStylePlugin::unregisterTypes()
    ritual = 'ritual_ZN17QQuickStylePlugin15unregisterTypesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickStylePlugin15unregisterTypesEv'
    self.uglySide.call(ritual)

  @overload(str)
  def createTheme(self, name: str) -> Optional[QQuickTheme]:
    """
    Calls Qt's 'QQuickTheme *QQuickStylePlugin::createTheme(const QString
    &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyleplugin.html#createTheme

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QQuickTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTheme *QQuickStylePlugin::createTheme(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN17QQuickStylePlugin11createThemeERK7QString', name,
    )
    from ..QtQuickTemplates2 import QQuickTheme
    return QQuickTheme._cuteAt(address)
