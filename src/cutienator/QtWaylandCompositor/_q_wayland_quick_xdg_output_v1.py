"""
QWaylandQuickXdgOutputV1 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandquickxdgoutputv1.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QWaylandXdgOutputV1

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickXdgOutputV1(QWaylandXdgOutputV1):
  """
  The cute side of Qt's QWaylandQuickXdgOutputV1: a plain Python object
  standing in front of one C++ QWaylandQuickXdgOutputV1.

  It is built on the cute 'QWaylandXdgOutputV1', as Qt's
  QWaylandQuickXdgOutputV1 is built on Qt's QWaylandXdgOutputV1, and has
  everything that class has. Qt's QWaylandQuickXdgOutputV1 is built on Qt's
  QQmlParserStatus as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QWaylandQuickXdgOutputV1 that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandQuickXdgOutputV1::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWaylandQuickXdgOutputV1::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQuickXdgOutputV1 is created at the first use, not by
    'QWaylandQuickXdgOutputV1(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickXdgOutputV1.
  - Qt tells when it has removed the C++ QWaylandQuickXdgOutputV1. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QWaylandQuickXdgOutputV1::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickxdgoutputv1.html#tr

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
    #  QString QWaylandQuickXdgOutputV1::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QWaylandQuickXdgOutputV12trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickXdgOutputV1'

  #  A C++ QWaylandQuickXdgOutputV1 Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandQuickXdgOutputV1'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandQuickXdgOutputV1::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickxdgoutputv1.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandQuickXdgOutputV1::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QWaylandQuickXdgOutputV110metaObjectEv',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandQuickXdgOutputV1::QWaylandQuickXdgOutputV1()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickxdgoutputv1.html
    """
    #  QWaylandQuickXdgOutputV1::QWaylandQuickXdgOutputV1()
    self._noteCreation(QWaylandQuickXdgOutputV1, lambda: Rituals.call(
        'ritual_ZN24QWaylandQuickXdgOutputV1C1Ev',
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickXdgOutputV1::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickxdgoutputv1.html#classBegin
    """
    #  void QWaylandQuickXdgOutputV1::classBegin()
    ritual = 'ritual_ZN24QWaylandQuickXdgOutputV110classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QWaylandQuickXdgOutputV110classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickXdgOutputV1::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickxdgoutputv1.html#componentComplete
    """
    #  void QWaylandQuickXdgOutputV1::componentComplete()
    ritual = 'ritual_ZN24QWaylandQuickXdgOutputV117componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QWaylandQuickXdgOutputV117componentCompleteEv'
    self.uglySide.call(ritual)
