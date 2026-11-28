"""
QQmlExtensionPlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlextensionplugin.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlExtensionInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QQmlEngine, QQmlExtensionPluginPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlExtensionPlugin(QObject, QQmlExtensionInterface):
  """
  The cute side of Qt's QQmlExtensionPlugin: a plain Python object standing
  in front of one C++ QQmlExtensionPlugin.

  It is built on the cute 'QObject', as Qt's QQmlExtensionPlugin is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlExtensionInterface' as well, as Qt's QQmlExtensionPlugin is built on
  Qt's QQmlExtensionInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlExtensionPlugin that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'd_func',
  'baseUrl', 'registerTypes', 'unregisterTypes', 'initializeEngine'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlExtensionPlugin::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlExtensionPlugin::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQmlExtensionPluginPrivate *QQmlExtensionPlugin::d_func()
    const': takes in Python what 'QQmlExtensionPluginPrivate
    *QQmlExtensionPlugin::d_func()' takes.
  - Qt's 'QQmlExtensionPlugin::~QQmlExtensionPlugin()': the destructor:
    Python never removes a C++ QQmlExtensionPlugin.

  What has no ritual
  ------------------

  5 of the 16 functions Qt declares: 2 not a gap; 2 forbidden; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open.

  What to expect
  --------------

  - The C++ QQmlExtensionPlugin is created at the first use, not by
    'QQmlExtensionPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlExtensionPlugin.
  - Qt tells when it has removed the C++ QQmlExtensionPlugin. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlExtensionPlugin that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQmlExtensionPlugin::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlextensionplugin.html#tr

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
    #  QString QQmlExtensionPlugin::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQmlExtensionPlugin2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlExtensionPlugin'

  #  Qt's QQmlExtensionPlugin is built on more than one class. The part of a
  #  C++ QQmlExtensionPlugin that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlExtensionInterface':
          'ritual_cast_QQmlExtensionPlugin_QQmlExtensionInterface',
  }

  #  A C++ QQmlExtensionPlugin Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlExtensionPlugin'

  #  The functions Qt calls itself that QQmlExtensionPlugin is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'unregisterTypes': (
          ('_ZN19QQmlExtensionPlugin15unregisterTypesEv',
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
    Calls Qt's 'const QMetaObject *QQmlExtensionPlugin::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlextensionplugin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlExtensionPlugin::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlExtensionPlugin10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def baseUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlExtensionPlugin::baseUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlextensionplugin.html#baseUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlExtensionPlugin::baseUrl() const
    address = self.uglySide.call('ritual_ZNK19QQmlExtensionPlugin7baseUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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
    Qt's 'QQmlExtensionPlugin::QQmlExtensionPlugin(QObject *parent)': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQmlExtensionPlugin.__init__' has no cute function yet. Qt's "
        "'QQmlExtensionPlugin::QQmlExtensionPlugin(QObject *parent)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  def d_func(self) -> Optional[QQmlExtensionPluginPrivate]:
    """
    Calls Qt's 'QQmlExtensionPluginPrivate *QQmlExtensionPlugin::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlextensionplugin.html#d_func

    Returns
    -------

    Optional[QQmlExtensionPluginPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlExtensionPluginPrivate *QQmlExtensionPlugin::d_func()
    address = self.uglySide.call('ritual_ZN19QQmlExtensionPlugin6d_funcEv')
    from . import QQmlExtensionPluginPrivate
    return QQmlExtensionPluginPrivate._cuteAt(address)

  @overload(str)
  @overload(NoneType)
  def registerTypes(self, uri: Optional[str]) -> None:
    """
    Calls Qt's 'void QQmlExtensionPlugin::registerTypes(const char *uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlextensionplugin.html#registerTypes

    Parameters
    ----------

    uri : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQmlExtensionPlugin::registerTypes(const char *uri)
    self.uglySide.call(
        'ritual_ZN19QQmlExtensionPlugin13registerTypesEPKc',
        self._bytesOf(uri),
    )

  def unregisterTypes(self) -> None:
    """
    Calls Qt's 'void QQmlExtensionPlugin::unregisterTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlextensionplugin.html#unregisterTypes
    """
    #  void QQmlExtensionPlugin::unregisterTypes()
    ritual = 'ritual_ZN19QQmlExtensionPlugin15unregisterTypesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlExtensionPlugin15unregisterTypesEv'
    self.uglySide.call(ritual)

  @overload(QQmlEngine, str)
  @overload(QQmlEngine, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def initializeEngine(
      self,
      engine: Optional[QQmlEngine],
      uri: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QQmlExtensionPlugin::initializeEngine(QQmlEngine
    *engine, const char *uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlextensionplugin.html#initializeEngine

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    uri : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQmlExtensionPlugin::initializeEngine(QQmlEngine *engine, const
    #      char *uri)
    self.uglySide.call(
        'ritual_ZN19QQmlExtensionPlugin16initializeEngineEP10QQmlEnginePKc',
        self._addressOf(engine), self._bytesOf(uri),
    )
