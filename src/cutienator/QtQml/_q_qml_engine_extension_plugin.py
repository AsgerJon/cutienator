"""
QQmlEngineExtensionPlugin binding of the Qt C++
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
from . import QQmlEngineExtensionInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlEngineExtensionPlugin(QObject, QQmlEngineExtensionInterface):
  """
  The cute side of Qt's QQmlEngineExtensionPlugin: a plain Python object
  standing in front of one C++ QQmlEngineExtensionPlugin.

  It is built on the cute 'QObject', as Qt's QQmlEngineExtensionPlugin is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlEngineExtensionInterface' as well, as Qt's
  QQmlEngineExtensionPlugin is built on Qt's QQmlEngineExtensionInterface
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlEngineExtensionPlugin that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'tr',
  'initializeEngine'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlEngineExtensionPlugin::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQmlEngineExtensionPlugin::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlEngineExtensionPlugin::~QQmlEngineExtensionPlugin()': the
    destructor: Python never removes a C++ QQmlEngineExtensionPlugin.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlEngineExtensionPlugin is created at the first use, not by
    'QQmlEngineExtensionPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlEngineExtensionPlugin.
  - Qt tells when it has removed the C++ QQmlEngineExtensionPlugin. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlEngineExtensionPlugin::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineextensionplugin.html#tr

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
    #  QString QQmlEngineExtensionPlugin::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQmlEngineExtensionPlugin2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlEngineExtensionPlugin'

  #  Qt's QQmlEngineExtensionPlugin is built on more than one class. The part
  #  of a C++ QQmlEngineExtensionPlugin that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlEngineExtensionInterface':
          'ritual_cast_QQmlEngineExtensionPlugin_QQmlEngineExtensionInterface',
  }

  #  A C++ QQmlEngineExtensionPlugin Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlEngineExtensionPlugin'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlEngineExtensionPlugin::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineextensionplugin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlEngineExtensionPlugin::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlEngineExtensionPlugin10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    'QQmlEngineExtensionPlugin::QQmlEngineExtensionPlugin(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineextensionplugin.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlEngineExtensionPlugin::QQmlEngineExtensionPlugin(QObject *parent)
    self._noteCreation(QQmlEngineExtensionPlugin, lambda: Rituals.call(
        'ritual_ZN25QQmlEngineExtensionPluginC1EP7QObject',
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
    Calls Qt's 'void QQmlEngineExtensionPlugin::initializeEngine(QQmlEngine
    *engine, const char *uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineextensionplugin.html#initializeEngine

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    uri : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQmlEngineExtensionPlugin::initializeEngine(QQmlEngine *engine,
    #      const char *uri)
    self.uglySide.call(
        'ritual_ZN25QQmlEngineExtensionPlugin16initializeEngineEP10QQmlEngi'
        'nePKc',
        self._addressOf(engine), self._bytesOf(uri),
    )
