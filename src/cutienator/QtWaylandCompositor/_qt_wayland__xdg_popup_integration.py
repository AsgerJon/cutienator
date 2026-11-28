"""
QtWayland::XdgPopupIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::XdgPopupIntegration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QWaylandQuickShellIntegration

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class XdgPopupIntegration(QWaylandQuickShellIntegration):
  """
  The cute side of Qt's QtWayland::XdgPopupIntegration: a plain Python object
  standing in front of one C++ QtWayland::XdgPopupIntegration.

  It is built on the cute 'QWaylandQuickShellIntegration', as Qt's
  QtWayland::XdgPopupIntegration is built on Qt's
  QWaylandQuickShellIntegration, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtWayland::XdgPopupIntegration that has a ritual and
  that Python can call so far, 2 names in all: 'metaObject',
  'handleGeometryChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtWayland::XdgPopupIntegration::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtWayland::XdgPopupIntegration::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 not a gap; 2 leans on 'QtWayland.

  What to expect
  --------------

  - The C++ QtWayland::XdgPopupIntegration is created at the first use, not
    by 'QtWayland::XdgPopupIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWayland::XdgPopupIntegration.
  - Qt tells when it has removed the C++ QtWayland::XdgPopupIntegration.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtWayland::XdgPopupIntegration that has no cute
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
  __qt_class__ = 'QtWayland::XdgPopupIntegration'

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
    *QtWayland::XdgPopupIntegration::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgpopupintegration.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtWayland::XdgPopupIntegration::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9QtWayland19XdgPopupIntegration10metaObjectEv',
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
    Qt's 'QtWayland::XdgPopupIntegration::XdgPopupIntegration(
    QWaylandQuickShellSurfaceItem *item)': leans on
    'QtWayland::XdgPopupIntegration::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QtWayland.XdgPopupIntegration.__init__' has no cute function yet. "
        "Qt's "
        "'QtWayland::XdgPopupIntegration::XdgPopupIntegration(QWaylandQuickS"
        "hellSurfaceItem *item)': leans on "
        "'QtWayland::XdgPopupIntegration::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def handleGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgPopupIntegration::handleGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgpopupintegration.html
    """
    #  void QtWayland::XdgPopupIntegration::handleGeometryChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland19XdgPopupIntegration21handleGeometryChangedEv',
    )
