"""
QWaylandKeymapPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandkeymap_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandKeymapPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QWaylandKeymap


class QWaylandKeymapPrivate(QObjectPrivate):
  """
  The cute side of Qt's QWaylandKeymapPrivate: a plain Python object standing
  in front of one C++ QWaylandKeymapPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QWaylandKeymapPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandKeymapPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWaylandKeymap *QWaylandKeymapPrivate::q_func() const': takes
    in Python what 'QWaylandKeymap *QWaylandKeymapPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QWaylandKeymapPrivate is created at the first use, not by
    'QWaylandKeymapPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandKeymapPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandKeymapPrivate'

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

  @overload(str, str, str, str, str)
  def __init__(
      self,
      layout: str,
      variant: str,
      options: str,
      model: str,
      rules: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandKeymapPrivate::QWaylandKeymapPrivate(const QString &layout,
    const QString &variant, const QString &options, const QString &model,
    const QString &rules)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeymapprivate.html#QWaylandKeymapPrivate

    Parameters
    ----------

    layout : str
      Passed on as it is: a QString is made of it for the call.

    variant : str
      Passed on as it is: a QString is made of it for the call.

    options : str
      Passed on as it is: a QString is made of it for the call.

    model : str
      Passed on as it is: a QString is made of it for the call.

    rules : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QWaylandKeymapPrivate::QWaylandKeymapPrivate(const QString &layout,
    #      const QString &variant, const QString &options, const QString
    #      &model, const QString &rules)
    self._noteCreation(QWaylandKeymapPrivate, lambda: Rituals.call(
        'ritual_ZN21QWaylandKeymapPrivateC1ERK7QStringS2_S2_S2_S2_',
        layout, variant, options, model, rules,
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

  def q_func(self) -> Optional[QWaylandKeymap]:
    """
    Calls Qt's 'QWaylandKeymap *QWaylandKeymapPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymapprivate.html#q_func

    Returns
    -------

    Optional[QWaylandKeymap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandKeymap *QWaylandKeymapPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QWaylandKeymapPrivate6q_funcEv')
    from . import QWaylandKeymap
    return QWaylandKeymap._cuteAt(address)
