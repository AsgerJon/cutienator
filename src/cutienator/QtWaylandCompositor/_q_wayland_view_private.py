"""
QWaylandViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandview_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QWaylandView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandView = WAIT['QWaylandView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandViewPrivate(QObjectPrivate):
  """
  The cute side of Qt's QWaylandViewPrivate: a plain Python object standing
  in front of one C++ QWaylandViewPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QWaylandViewPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandViewPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func', 'get',
  'clearFrontBuffer'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWaylandView *QWaylandViewPrivate::q_func() const': takes in
    Python what 'QWaylandView *QWaylandViewPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QWaylandViewPrivate.

  What to expect
  --------------

  - The C++ QWaylandViewPrivate is created at the first use, not by
    'QWaylandViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandViewPrivate.
  - Each name of Qt's QWaylandViewPrivate that has no cute function yet,
    'markSurfaceAsDestroyed', 'setSurface', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWaylandView)
  @overload(NoneType)
  def get(view: Optional[QWaylandView]) -> Optional[QWaylandViewPrivate]:
    """
    Calls Qt's 'QWaylandViewPrivate *QWaylandViewPrivate::get(QWaylandView
    *view)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandviewprivate.html#get

    Parameters
    ----------

    view : Optional[QWaylandView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandViewPrivate *QWaylandViewPrivate::get(QWaylandView *view)
    address = Rituals.call(
        'ritual_ZN19QWaylandViewPrivate3getEP12QWaylandView',
        CuteMixin._addressOf(view),
    )
    return QWaylandViewPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandViewPrivate'

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
    'QWaylandViewPrivate::QWaylandViewPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandviewprivate.html#QWaylandViewPrivate
    """
    #  QWaylandViewPrivate::QWaylandViewPrivate()
    self._noteCreation(QWaylandViewPrivate, lambda: Rituals.call(
        'ritual_ZN19QWaylandViewPrivateC1Ev',
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

  def q_func(self) -> Optional[QWaylandView]:
    """
    Calls Qt's 'QWaylandView *QWaylandViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandviewprivate.html#q_func

    Returns
    -------

    Optional[QWaylandView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandView *QWaylandViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QWaylandViewPrivate6q_funcEv')
    from . import QWaylandView
    return QWaylandView._cuteAt(address)

  def clearFrontBuffer(self) -> None:
    """
    Calls Qt's 'void QWaylandViewPrivate::clearFrontBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandviewprivate.html#clearFrontBuffer
    """
    #  void QWaylandViewPrivate::clearFrontBuffer()
    self.uglySide.call('ritual_ZN19QWaylandViewPrivate16clearFrontBufferEv')

  @staticmethod
  def markSurfaceAsDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QWaylandViewPrivate::markSurfaceAsDestroyed(QWaylandSurface
    *surface)': leans on 'QWaylandViewPrivate::setSurface(QWaylandSurface*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QWaylandViewPrivate.markSurfaceAsDestroyed' has no cute function "
        "yet. Qt's 'void "
        "QWaylandViewPrivate::markSurfaceAsDestroyed(QWaylandSurface "
        "*surface)': leans on "
        "'QWaylandViewPrivate::setSurface(QWaylandSurface*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setSurface(*__, **_) -> Never:
    """
    Qt's 'void QWaylandViewPrivate::setSurface(QWaylandSurface *newSurface)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: incomplete type 'QWaylandSurfacePrivate'
    named in nested name specifier.
    """
    raise NotImplementedError(
        "'QWaylandViewPrivate.setSurface' has no cute function yet. Qt's "
        "'void QWaylandViewPrivate::setSurface(QWaylandSurface "
        "*newSurface)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: incomplete type "
        "'QWaylandSurfacePrivate' named in nested name specifier.")
