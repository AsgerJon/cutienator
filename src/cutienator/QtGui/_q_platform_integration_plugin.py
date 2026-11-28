"""
QPlatformIntegrationPlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformintegrationplugin.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPlatformIntegration

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformIntegrationPlugin(QObject):
  """
  The cute side of Qt's QPlatformIntegrationPlugin: a plain Python object
  standing in front of one C++ QPlatformIntegrationPlugin.

  It is built on the cute 'QObject', as Qt's QPlatformIntegrationPlugin is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformIntegrationPlugin that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject', 'tr', 'create'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformIntegrationPlugin::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QPlatformIntegrationPlugin::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformIntegrationPlugin::~QPlatformIntegrationPlugin()': the
    destructor: Python never removes a C++ QPlatformIntegrationPlugin.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformIntegrationPlugin is created at the first use, not by
    'QPlatformIntegrationPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformIntegrationPlugin.
  - Qt tells when it has removed the C++ QPlatformIntegrationPlugin. Every
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
    Calls Qt's 'QString QPlatformIntegrationPlugin::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformintegrationplugin.html#tr

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
    #  QString QPlatformIntegrationPlugin::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QPlatformIntegrationPlugin2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformIntegrationPlugin'

  #  A C++ QPlatformIntegrationPlugin Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformIntegrationPlugin'

  #  The functions Qt calls itself that QPlatformIntegrationPlugin is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'create': (
          'QPlatformIntegration *QPlatformIntegrationPlugin::create(const '
          'QString &, const QStringList &)',
          'QPlatformIntegration *QPlatformIntegrationPlugin::create(const '
          'QString &, const QStringList &, int &, char **)',
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
    Calls Qt's 'const QMetaObject *QPlatformIntegrationPlugin::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegrationplugin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformIntegrationPlugin::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QPlatformIntegrationPlugin10metaObjectEv',
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
    'QPlatformIntegrationPlugin::QPlatformIntegrationPlugin(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegrationplugin.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlatformIntegrationPlugin::QPlatformIntegrationPlugin(QObject
    #      *parent)
    self._noteCreation(QPlatformIntegrationPlugin, lambda: Rituals.call(
        'ritual_ZN26QPlatformIntegrationPluginC1EP7QObject',
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

  @overload(str, QStringList)
  def create(
      self,
      key: str,
      paramList: QStringList,
  ) -> Optional[QPlatformIntegration]:
    """
    Calls Qt's 'QPlatformIntegration
    *QPlatformIntegrationPlugin::create(const QString &key, const QStringList
    &paramList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegrationplugin.html#create

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    paramList : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QPlatformIntegration]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformIntegration *QPlatformIntegrationPlugin::create(const QString
    #      &key, const QStringList &paramList)
    address = self.uglySide.call(
        'ritual_ZN26QPlatformIntegrationPlugin6createERK7QStringRK5QListIS0'
        '_E',
        key, self._valueOf(paramList),
    )
    from . import QPlatformIntegration
    return QPlatformIntegration._cuteAt(address)

  @overload(str, QStringList, list)
  def create(
      self,
      key: str,
      paramList: QStringList,
      argv: list,
  ) -> Optional[QPlatformIntegration]:
    """
    Calls Qt's 'QPlatformIntegration
    *QPlatformIntegrationPlugin::create(const QString &key, const QStringList
    &paramList, int &argc, char **argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegrationplugin.html#create

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    paramList : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    argv : list
      The texts the program was started with, as 'sys.argv'. Passed on as Qt
      takes them: how many they are, and where the first one is.

    Returns
    -------

    Optional[QPlatformIntegration]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformIntegration *QPlatformIntegrationPlugin::create(const QString
    #      &key, const QStringList &paramList, int &argc, char **argv)
    address = self.uglySide.call(
        'ritual_ZN26QPlatformIntegrationPlugin6createERK7QStringRK5QListIS0'
        '_ERiPPc',
        key, self._valueOf(paramList), *self._startTextsOf(argv),
    )
    from . import QPlatformIntegration
    return QPlatformIntegration._cuteAt(address)
