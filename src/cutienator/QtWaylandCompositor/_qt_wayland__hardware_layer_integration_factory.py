"""
QtWayland::HardwareLayerIntegrationFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlhardwarelayerintegrationfactory_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::HardwareLayerIntegrationFactory to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QtWayland

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class HardwareLayerIntegrationFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtWayland::HardwareLayerIntegrationFactory: a plain
  Python object standing in front of one C++
  QtWayland::HardwareLayerIntegrationFactory.

  C++ hands a QtWayland::HardwareLayerIntegrationFactory around as a copy, so
  every C++ QtWayland::HardwareLayerIntegrationFactory behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtWayland::HardwareLayerIntegrationFactory that has
  a ritual and that Python can call so far, 2 names in all: 'keys', 'create'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtWayland::HardwareLayerIntegrationFactory::
    ~HardwareLayerIntegrationFactory()': the destructor: Python removes its
    C++ QtWayland::HardwareLayerIntegrationFactory by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QtWayland::HardwareLayerIntegrationFactory is created at the
    first use, not by 'QtWayland::HardwareLayerIntegrationFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtWayland::HardwareLayerIntegrationFactory back gives
    a copy the ritual made for Python, in a new cute
    QtWayland::HardwareLayerIntegrationFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def keys() -> QStringList:
    """
    Calls Qt's 'QStringList
    QtWayland::HardwareLayerIntegrationFactory::keys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-hardwarelayerintegrationfactory.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QtWayland::HardwareLayerIntegrationFactory::keys()
    address = Rituals.call(
        'ritual_ZN9QtWayland31HardwareLayerIntegrationFactory4keysEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str, QStringList)
  def create(
      name: str,
      args: QStringList,
  ) -> Optional[QtWayland.HardwareLayerIntegration]:
    """
    Calls Qt's 'HardwareLayerIntegration
    *QtWayland::HardwareLayerIntegrationFactory::create(const QString &name,
    const QStringList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-hardwarelayerintegrationfactory.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    args : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QtWayland.HardwareLayerIntegration]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  HardwareLayerIntegration
    #      *QtWayland::HardwareLayerIntegrationFactory::create(const QString
    #      &name, const QStringList &args)
    address = Rituals.call(
        'ritual_ZN9QtWayland31HardwareLayerIntegrationFactory6createERK7QSt'
        'ringRK5QListIS1_E',
        name, CuteMixin._valueOf(args),
    )
    return QtWayland.HardwareLayerIntegration._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWayland::HardwareLayerIntegrationFactory'

  #  Qt's '~QtWayland::HardwareLayerIntegrationFactory()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QtWayland::HardwareLayerIntegrationFactory behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN9QtWayland31HardwareLayerIntegrationFactoryD1Ev')

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
