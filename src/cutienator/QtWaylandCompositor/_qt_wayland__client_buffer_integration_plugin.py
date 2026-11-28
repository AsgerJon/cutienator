"""
QtWayland::ClientBufferIntegrationPlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegrationplugin_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::ClientBufferIntegrationPlugin to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ClientBufferIntegrationPlugin(QObject):
  """
  The cute side of Qt's QtWayland::ClientBufferIntegrationPlugin: a plain
  Python object standing in front of one C++
  QtWayland::ClientBufferIntegrationPlugin.

  It is built on the cute 'QObject', as Qt's
  QtWayland::ClientBufferIntegrationPlugin is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QtWayland::ClientBufferIntegrationPlugin that has a
  ritual and that Python can call so far, 2 names in all: 'metaObject', 'tr'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtWayland::ClientBufferIntegrationPlugin::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtWayland::ClientBufferIntegrationPlugin::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtWayland::ClientBufferIntegrationPlugin::
    ~ClientBufferIntegrationPlugin()': the destructor: Python never removes a
    C++ QtWayland::ClientBufferIntegrationPlugin.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 the compiler refuses its ritual as it would be
  written here.

  What to expect
  --------------

  - The C++ QtWayland::ClientBufferIntegrationPlugin is created at the first
    use, not by 'QtWayland::ClientBufferIntegrationPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWayland::ClientBufferIntegrationPlugin.
  - Qt tells when it has removed the C++
    QtWayland::ClientBufferIntegrationPlugin. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QtWayland::ClientBufferIntegrationPlugin that has no
    cute function yet, '__init__', 'create', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QtWayland::ClientBufferIntegrationPlugin::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-clientbufferintegrationplugin.html#tr

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
    #  QString QtWayland::ClientBufferIntegrationPlugin::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QtWayland29ClientBufferIntegrationPlugin2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWayland::ClientBufferIntegrationPlugin'

  #  A C++ QtWayland::ClientBufferIntegrationPlugin Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtWayland_ClientBufferIntegrationPlugin'

  #  The functions Qt calls itself that
  #  QtWayland::ClientBufferIntegrationPlugin is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'create': (
          'ClientBufferIntegration '
          '*QtWayland::ClientBufferIntegrationPlugin::create(const QString '
          '&, const QStringList &)',
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
    *QtWayland::ClientBufferIntegrationPlugin::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-clientbufferintegrationplugin.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtWayland::ClientBufferIntegrationPlugin::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9QtWayland29ClientBufferIntegrationPlugin10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QtWayland::ClientBufferIntegrationPlugin::ClientBufferIntegrationPlugin(
    QObject *parent)': the class is abstract, so C++ cannot make one, and the
    C++ class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QtWayland.ClientBufferIntegrationPlugin.__init__' has no cute "
        "function yet. Qt's "
        "'QtWayland::ClientBufferIntegrationPlugin::ClientBufferIntegrationP"
        "lugin(QObject *parent)': the class is abstract, so C++ cannot make "
        "one, and the C++ class of ours does not fill in every function it "
        "leaves open.")

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
  def create(*__, **_) -> Never:
    """
    Qt's 'ClientBufferIntegration
    *QtWayland::ClientBufferIntegrationPlugin::create(const QString &key,
    const QStringList &paramList)': the compiler refuses its ritual as it
    would be written here: unknown type name 'ClientBufferIntegration'; did
    you mean 'QtWayland::ClientBufferIntegration'?.
    """
    raise NotImplementedError(
        "'QtWayland.ClientBufferIntegrationPlugin.create' has no cute "
        "function yet. Qt's 'ClientBufferIntegration "
        "*QtWayland::ClientBufferIntegrationPlugin::create(const QString "
        "&key, const QStringList &paramList)': the compiler refuses its "
        "ritual as it would be written here: unknown type name "
        "'ClientBufferIntegration'; did you mean "
        "'QtWayland::ClientBufferIntegration'?.")
