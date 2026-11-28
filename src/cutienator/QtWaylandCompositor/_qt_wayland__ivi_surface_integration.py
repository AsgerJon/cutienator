"""
QtWayland::IviSurfaceIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandivisurfaceintegration_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::IviSurfaceIntegration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QWaylandQuickShellIntegration

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class IviSurfaceIntegration(QWaylandQuickShellIntegration):
  """
  The cute side of Qt's QtWayland::IviSurfaceIntegration: a plain Python
  object standing in front of one C++ QtWayland::IviSurfaceIntegration.

  It is built on the cute 'QWaylandQuickShellIntegration', as Qt's
  QtWayland::IviSurfaceIntegration is built on Qt's
  QWaylandQuickShellIntegration, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtWayland::IviSurfaceIntegration that has a ritual
  and that Python can call so far, 2 names in all: 'metaObject',
  'handleIviSurfaceDestroyed'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtWayland::IviSurfaceIntegration::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QtWayland::IviSurfaceIntegration::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtWayland::IviSurfaceIntegration::~IviSurfaceIntegration()': the
    destructor: Python never removes a C++ QtWayland::IviSurfaceIntegration.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 not a gap; 2 leans on 'QtWayland.

  What to expect
  --------------

  - The C++ QtWayland::IviSurfaceIntegration is created at the first use, not
    by 'QtWayland::IviSurfaceIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWayland::IviSurfaceIntegration.
  - Qt tells when it has removed the C++ QtWayland::IviSurfaceIntegration.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtWayland::IviSurfaceIntegration that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWayland::IviSurfaceIntegration'

  #  A C++ QtWayland::IviSurfaceIntegration Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtWayland_IviSurfaceIntegration'

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
    *QtWayland::IviSurfaceIntegration::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-ivisurfaceintegration.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtWayland::IviSurfaceIntegration::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9QtWayland21IviSurfaceIntegration10metaObjectEv',
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
    Qt's 'QtWayland::IviSurfaceIntegration::IviSurfaceIntegration(
    QWaylandQuickShellSurfaceItem *item)': leans on
    'QtWayland::IviSurfaceIntegration::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtWayland.IviSurfaceIntegration.__init__' has no cute function "
        "yet. Qt's "
        "'QtWayland::IviSurfaceIntegration::IviSurfaceIntegration(QWaylandQu"
        "ickShellSurfaceItem *item)': leans on "
        "'QtWayland::IviSurfaceIntegration::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def handleIviSurfaceDestroyed(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::IviSurfaceIntegration::handleIviSurfaceDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-ivisurfaceintegration.html
    """
    #  void QtWayland::IviSurfaceIntegration::handleIviSurfaceDestroyed()
    self.uglySide.call(
        'ritual_ZN9QtWayland21IviSurfaceIntegration25handleIviSurfaceDestro'
        'yedEv',
    )
