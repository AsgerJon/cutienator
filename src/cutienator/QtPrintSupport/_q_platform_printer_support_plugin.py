"""
QPlatformPrinterSupportPlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/qpa/qplatformprintplugin.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPlatformPrinterSupport

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformPrinterSupportPlugin(QObject):
  """
  The cute side of Qt's QPlatformPrinterSupportPlugin: a plain Python object
  standing in front of one C++ QPlatformPrinterSupportPlugin.

  It is built on the cute 'QObject', as Qt's QPlatformPrinterSupportPlugin is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformPrinterSupportPlugin that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr', 'create',
  'get'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformPrinterSupportPlugin::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QPlatformPrinterSupportPlugin::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformPrinterSupportPlugin::~QPlatformPrinterSupportPlugin()':
    the destructor: Python never removes a C++ QPlatformPrinterSupportPlugin.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformPrinterSupportPlugin is created at the first use, not by
    'QPlatformPrinterSupportPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformPrinterSupportPlugin.
  - Qt tells when it has removed the C++ QPlatformPrinterSupportPlugin. Every
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
    Calls Qt's 'QString QPlatformPrinterSupportPlugin::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupportplugin.html#tr

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
    #  QString QPlatformPrinterSupportPlugin::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QPlatformPrinterSupportPlugin2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def get() -> Optional[QPlatformPrinterSupport]:
    """
    Calls Qt's 'QPlatformPrinterSupport
    *QPlatformPrinterSupportPlugin::get()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupportplugin.html#get

    Returns
    -------

    Optional[QPlatformPrinterSupport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformPrinterSupport *QPlatformPrinterSupportPlugin::get()
    address = Rituals.call('ritual_ZN29QPlatformPrinterSupportPlugin3getEv')
    from . import QPlatformPrinterSupport
    return QPlatformPrinterSupport._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformPrinterSupportPlugin'

  #  A C++ QPlatformPrinterSupportPlugin Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformPrinterSupportPlugin'

  #  The functions Qt calls itself that QPlatformPrinterSupportPlugin is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN29QPlatformPrinterSupportPlugin6createERK7QString',
           ('address', 'address', 'QtPrintSupport:QPlatformPrinterSupport'),
           (
               ('address', 'text', ''),
           )),
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
    Calls Qt's 'const QMetaObject
    *QPlatformPrinterSupportPlugin::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupportplugin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformPrinterSupportPlugin::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QPlatformPrinterSupportPlugin10metaObjectEv',
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
    'QPlatformPrinterSupportPlugin::QPlatformPrinterSupportPlugin(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupportplugin.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlatformPrinterSupportPlugin::QPlatformPrinterSupportPlugin(QObject
    #      *parent)
    self._noteCreation(QPlatformPrinterSupportPlugin, lambda: Rituals.call(
        'ritual_ZN29QPlatformPrinterSupportPluginC1EP7QObject',
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

  @overload(str)
  def create(self, key: str) -> Optional[QPlatformPrinterSupport]:
    """
    Calls Qt's 'QPlatformPrinterSupport
    *QPlatformPrinterSupportPlugin::create(const QString &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupportplugin.html#create

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPlatformPrinterSupport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformPrinterSupport *QPlatformPrinterSupportPlugin::create(const
    #      QString &key)
    address = self.uglySide.call(
        'ritual_ZN29QPlatformPrinterSupportPlugin6createERK7QString', key,
    )
    from . import QPlatformPrinterSupport
    return QPlatformPrinterSupport._cuteAt(address)
