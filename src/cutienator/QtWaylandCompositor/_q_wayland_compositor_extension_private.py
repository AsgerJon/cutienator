"""
QWaylandCompositorExtensionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandcompositorextension_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandCompositorExtensionPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QWaylandCompositorExtension
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandCompositorExtension = WAIT['QWaylandCompositorExtension']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandCompositorExtensionPrivate(QObjectPrivate):
  """
  The cute side of Qt's QWaylandCompositorExtensionPrivate: a plain Python
  object standing in front of one C++ QWaylandCompositorExtensionPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QWaylandCompositorExtensionPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandCompositorExtensionPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'q_func', 'get'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWaylandCompositorExtension
    *QWaylandCompositorExtensionPrivate::q_func() const': takes in Python
    what 'QWaylandCompositorExtension
    *QWaylandCompositorExtensionPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QWaylandCompositorExtensionPrivate is created at the first use,
    not by 'QWaylandCompositorExtensionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandCompositorExtensionPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWaylandCompositorExtension)
  @overload(NoneType)
  def get(
      extension: Optional[QWaylandCompositorExtension],
  ) -> Optional[QWaylandCompositorExtensionPrivate]:
    """
    Calls Qt's 'QWaylandCompositorExtensionPrivate
    *QWaylandCompositorExtensionPrivate::get(QWaylandCompositorExtension
    *extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextensionprivate.html#get

    Parameters
    ----------

    extension : Optional[QWaylandCompositorExtension]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandCompositorExtensionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositorExtensionPrivate
    #      *QWaylandCompositorExtensionPrivate::get(
    #      QWaylandCompositorExtension *extension)
    address = Rituals.call(
        'ritual_ZN34QWaylandCompositorExtensionPrivate3getEP27QWaylandCompo'
        'sitorExtension',
        CuteMixin._addressOf(extension),
    )
    return QWaylandCompositorExtensionPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandCompositorExtensionPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandCompositorExtensionPrivate::QWaylandCompositorExtensionPrivate(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextensionprivate.html
    """
    #  QWaylandCompositorExtensionPrivate::
    #      QWaylandCompositorExtensionPrivate()
    self._noteCreation(
        QWaylandCompositorExtensionPrivate, lambda: Rituals.call(
            'ritual_ZN34QWaylandCompositorExtensionPrivateC1Ev',
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

  def q_func(self) -> Optional[QWaylandCompositorExtension]:
    """
    Calls Qt's 'QWaylandCompositorExtension
    *QWaylandCompositorExtensionPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositorextensionprivate.html#q_func

    Returns
    -------

    Optional[QWaylandCompositorExtension]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositorExtension
    #      *QWaylandCompositorExtensionPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN34QWaylandCompositorExtensionPrivate6q_funcEv',
    )
    from . import QWaylandCompositorExtension
    return QWaylandCompositorExtension._cuteAt(address)
