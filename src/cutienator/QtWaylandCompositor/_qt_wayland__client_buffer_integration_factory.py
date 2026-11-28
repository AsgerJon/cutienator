"""
QtWayland::ClientBufferIntegrationFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegrationfactory_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::ClientBufferIntegrationFactory to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ClientBufferIntegrationFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtWayland::ClientBufferIntegrationFactory: a plain
  Python object standing in front of one C++
  QtWayland::ClientBufferIntegrationFactory.

  C++ hands a QtWayland::ClientBufferIntegrationFactory around as a copy, so
  every C++ QtWayland::ClientBufferIntegrationFactory behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtWayland::ClientBufferIntegrationFactory that has a
  ritual and that Python can call so far, 1 name in all: 'keys'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtWayland::ClientBufferIntegrationFactory::
    ~ClientBufferIntegrationFactory()': the destructor: Python removes its
    C++ QtWayland::ClientBufferIntegrationFactory by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QtWayland::ClientBufferIntegrationFactory is created at the first
    use, not by 'QtWayland::ClientBufferIntegrationFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtWayland::ClientBufferIntegrationFactory back gives
    a copy the ritual made for Python, in a new cute
    QtWayland::ClientBufferIntegrationFactory.
  - Each name of Qt's QtWayland::ClientBufferIntegrationFactory that has no
    cute function yet, 'create', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def keys() -> QStringList:
    """
    Calls Qt's 'QStringList
    QtWayland::ClientBufferIntegrationFactory::keys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-clientbufferintegrationfactory.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QtWayland::ClientBufferIntegrationFactory::keys()
    address = Rituals.call(
        'ritual_ZN9QtWayland30ClientBufferIntegrationFactory4keysEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWayland::ClientBufferIntegrationFactory'

  #  Qt's '~QtWayland::ClientBufferIntegrationFactory()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QtWayland::ClientBufferIntegrationFactory behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN9QtWayland30ClientBufferIntegrationFactoryD1Ev')

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
  def create(*__, **_) -> Never:
    """
    Qt's 'ClientBufferIntegration
    *QtWayland::ClientBufferIntegrationFactory::create(const QString &name,
    const QStringList &args)': the compiler refuses its ritual as it would be
    written here: unknown type name 'ClientBufferIntegration'; did you mean
    'QtWayland::ClientBufferIntegration'?.
    """
    raise NotImplementedError(
        "'QtWayland.ClientBufferIntegrationFactory.create' has no cute "
        "function yet. Qt's 'ClientBufferIntegration "
        "*QtWayland::ClientBufferIntegrationFactory::create(const QString "
        "&name, const QStringList &args)': the compiler refuses its ritual "
        "as it would be written here: unknown type name "
        "'ClientBufferIntegration'; did you mean "
        "'QtWayland::ClientBufferIntegration'?.")
