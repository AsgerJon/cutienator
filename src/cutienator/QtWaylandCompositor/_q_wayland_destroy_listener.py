"""
QWaylandDestroyListener binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylanddestroylistener.h, Qt 6.12.0. Changes made
#  here are lost.
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


class QWaylandDestroyListener(QObject):
  """
  The cute side of Qt's QWaylandDestroyListener: a plain Python object
  standing in front of one C++ QWaylandDestroyListener.

  It is built on the cute 'QObject', as Qt's QWaylandDestroyListener is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandDestroyListener that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'tr', 'reset'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandDestroyListener::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandDestroyListener::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandDestroyListenerPrivate *QWaylandDestroyListener::d_func()':
    gives 'QWaylandDestroyListenerPrivate', which has no cute class yet.
  - Qt's 'const QWaylandDestroyListenerPrivate
    *QWaylandDestroyListener::d_func() const': gives
    'QWaylandDestroyListenerPrivate', which has no cute class yet.
  - Qt's 'void QWaylandDestroyListener::listenForDestruction(struct
    wl_resource *resource)': names 'struct wl_resource', which has no cute
    class yet.
  - Qt's 'void QWaylandDestroyListener::fired(void *data)': names 'void',
    which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandDestroyListener is created at the first use, not by
    'QWaylandDestroyListener(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandDestroyListener.
  - Qt tells when it has removed the C++ QWaylandDestroyListener. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandDestroyListener that has no cute function yet,
    'fired', 'listenForDestruction', holds a function that raises
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
    Calls Qt's 'QString QWaylandDestroyListener::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddestroylistener.html#tr

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
    #  QString QWaylandDestroyListener::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QWaylandDestroyListener2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandDestroyListener'

  #  A C++ QWaylandDestroyListener Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandDestroyListener'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandDestroyListener::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylanddestroylistener.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandDestroyListener::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QWaylandDestroyListener10metaObjectEv',
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
    'QWaylandDestroyListener::QWaylandDestroyListener(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylanddestroylistener.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandDestroyListener::QWaylandDestroyListener(QObject *parent)
    self._noteCreation(QWaylandDestroyListener, lambda: Rituals.call(
        'ritual_ZN23QWaylandDestroyListenerC1EP7QObject',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QWaylandDestroyListener::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddestroylistener.html#reset
    """
    #  void QWaylandDestroyListener::reset()
    self.uglySide.call('ritual_ZN23QWaylandDestroyListener5resetEv')

  @staticmethod
  def fired(*__, **_) -> Never:
    """
    Qt's 'void QWaylandDestroyListener::fired(void *data)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandDestroyListener.fired' has no cute function yet. Qt's "
        "'void QWaylandDestroyListener::fired(void *data)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def listenForDestruction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandDestroyListener::listenForDestruction(struct
    wl_resource *resource)': names 'struct wl_resource', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QWaylandDestroyListener.listenForDestruction' has no cute "
        "function yet. Qt's 'void "
        "QWaylandDestroyListener::listenForDestruction(struct wl_resource "
        "*resource)': names 'struct wl_resource', which has no cute class "
        "yet.")
