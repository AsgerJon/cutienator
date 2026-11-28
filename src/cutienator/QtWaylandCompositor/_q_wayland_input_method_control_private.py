"""
QWaylandInputMethodControlPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandinputmethodcontrol_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandInputMethodControlPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QWaylandInputMethodControl, QWaylandQtTextInputMethod
  from . import QWaylandSurface, QWaylandTextInput, QWaylandTextInputV3
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandInputMethodControlPrivate(QObjectPrivate):
  """
  The cute side of Qt's QWaylandInputMethodControlPrivate: a plain Python
  object standing in front of one C++ QWaylandInputMethodControlPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QWaylandInputMethodControlPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandInputMethodControlPrivate that has a ritual
  and that Python can call so far, 4 names in all: 'q_func', 'textInput',
  'textInputV3', 'textInputMethod'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWaylandInputMethodControl
    *QWaylandInputMethodControlPrivate::q_func() const': takes in Python what
    'QWaylandInputMethodControl *QWaylandInputMethodControlPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QWaylandInputMethodControlPrivate is created at the first use,
    not by 'QWaylandInputMethodControlPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandInputMethodControlPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandInputMethodControlPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def textInput(self) -> Optional[QWaylandTextInput]:
    """
    Calls Qt's 'QWaylandTextInput
    *QWaylandInputMethodControlPrivate::textInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrolprivate.html#textInput

    Returns
    -------

    Optional[QWaylandTextInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandTextInput *QWaylandInputMethodControlPrivate::textInput()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QWaylandInputMethodControlPrivate9textInputEv',
    )
    from . import QWaylandTextInput
    return QWaylandTextInput._cuteAt(address)

  def textInputV3(self) -> Optional[QWaylandTextInputV3]:
    """
    Calls Qt's 'QWaylandTextInputV3
    *QWaylandInputMethodControlPrivate::textInputV3() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrolprivate.html#textInputV3

    Returns
    -------

    Optional[QWaylandTextInputV3]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandTextInputV3 *QWaylandInputMethodControlPrivate::textInputV3()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QWaylandInputMethodControlPrivate11textInputV3Ev',
    )
    from . import QWaylandTextInputV3
    return QWaylandTextInputV3._cuteAt(address)

  def textInputMethod(self) -> Optional[QWaylandQtTextInputMethod]:
    """
    Calls Qt's 'QWaylandQtTextInputMethod
    *QWaylandInputMethodControlPrivate::textInputMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrolprivate.html

    Returns
    -------

    Optional[QWaylandQtTextInputMethod]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQtTextInputMethod
    #      *QWaylandInputMethodControlPrivate::textInputMethod() const
    address = self.uglySide.call(
        'ritual_ZNK33QWaylandInputMethodControlPrivate15textInputMethodEv',
    )
    from . import QWaylandQtTextInputMethod
    return QWaylandQtTextInputMethod._cuteAt(address)

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

  @overload(QWaylandSurface)
  @overload(NoneType)
  def __init__(self, surface: Optional[QWaylandSurface]) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandInputMethodControlPrivate::QWaylandInputMethodControlPrivate(
    QWaylandSurface *surface)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrolprivate.html

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandInputMethodControlPrivate::
    #      QWaylandInputMethodControlPrivate(QWaylandSurface *surface)
    self._noteCreation(
        QWaylandInputMethodControlPrivate, lambda: Rituals.call(
            'ritual_ZN33QWaylandInputMethodControlPrivateC1EP15QWaylandSurf'
            'ace',
            self._addressOf(surface),
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

  def q_func(self) -> Optional[QWaylandInputMethodControl]:
    """
    Calls Qt's 'QWaylandInputMethodControl
    *QWaylandInputMethodControlPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandinputmethodcontrolprivate.html#q_func

    Returns
    -------

    Optional[QWaylandInputMethodControl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandInputMethodControl
    #      *QWaylandInputMethodControlPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN33QWaylandInputMethodControlPrivate6q_funcEv',
    )
    from . import QWaylandInputMethodControl
    return QWaylandInputMethodControl._cuteAt(address)
