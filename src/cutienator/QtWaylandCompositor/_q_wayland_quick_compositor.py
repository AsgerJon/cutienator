"""
QWaylandQuickCompositor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandquickcompositor.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QWaylandCompositor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QWaylandBufferRef, QWaylandSurfaceGrabber
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandBufferRef = WAIT['QWaylandBufferRef']
  QWaylandSurfaceGrabber = WAIT['QWaylandSurfaceGrabber']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickCompositor(QWaylandCompositor):
  """
  The cute side of Qt's QWaylandQuickCompositor: a plain Python object
  standing in front of one C++ QWaylandQuickCompositor.

  It is built on the cute 'QWaylandCompositor', as Qt's
  QWaylandQuickCompositor is built on Qt's QWaylandCompositor, and has
  everything that class has. Qt's QWaylandQuickCompositor is built on Qt's
  QQmlParserStatus as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QWaylandQuickCompositor that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'create',
  'grabSurface', 'classBegin', 'componentComplete'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandQuickCompositor::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandQuickCompositor::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQuickCompositor is created at the first use, not by
    'QWaylandQuickCompositor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickCompositor.
  - Qt tells when it has removed the C++ QWaylandQuickCompositor. Every call
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
    Calls Qt's 'QString QWaylandQuickCompositor::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickcompositor.html#tr

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
    #  QString QWaylandQuickCompositor::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QWaylandQuickCompositor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickCompositor'

  #  A C++ QWaylandQuickCompositor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandQuickCompositor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandQuickCompositor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickcompositor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandQuickCompositor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QWaylandQuickCompositor10metaObjectEv',
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
    'QWaylandQuickCompositor::QWaylandQuickCompositor(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickcompositor.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandQuickCompositor::QWaylandQuickCompositor(QObject *parent)
    self._noteCreation(QWaylandQuickCompositor, lambda: Rituals.call(
        'ritual_ZN23QWaylandQuickCompositorC1EP7QObject',
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

  def create(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickCompositor::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickcompositor.html#create
    """
    #  void QWaylandQuickCompositor::create()
    ritual = 'ritual_ZN23QWaylandQuickCompositor6createEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QWaylandQuickCompositor6createEv'
    self.uglySide.call(ritual)

  @overload(QWaylandSurfaceGrabber, QWaylandBufferRef)
  @overload(NoneType, QWaylandBufferRef)
  def grabSurface(
      self,
      grabber: Optional[QWaylandSurfaceGrabber],
      buffer: QWaylandBufferRef,
  ) -> None:
    """
    Calls Qt's 'void
    QWaylandQuickCompositor::grabSurface(QWaylandSurfaceGrabber *grabber,
    const QWaylandBufferRef &buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickcompositor.html#grabSurface

    Parameters
    ----------

    grabber : Optional[QWaylandSurfaceGrabber]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    buffer : QWaylandBufferRef
      Passed on as a value: Qt reads the C++ QWaylandBufferRef, which stays
      Python's own.
    """
    #  void QWaylandQuickCompositor::grabSurface(QWaylandSurfaceGrabber
    #      *grabber, const QWaylandBufferRef &buffer)
    ritual = (
        'ritual_ZN23QWaylandQuickCompositor11grabSurfaceEP22QWaylandSurface'
        'GrabberRK17QWaylandBufferRef')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QWaylandQuickCompositor11grabSurfaceEP22QWaylandS'
          'urfaceGrabberRK17QWaylandBufferRef')
    self.uglySide.call(
        ritual, self._addressOf(grabber), self._valueOf(buffer),
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickCompositor::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickcompositor.html#classBegin
    """
    #  void QWaylandQuickCompositor::classBegin()
    ritual = 'ritual_ZN23QWaylandQuickCompositor10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QWaylandQuickCompositor10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickCompositor::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickcompositor.html#componentComplete
    """
    #  void QWaylandQuickCompositor::componentComplete()
    ritual = 'ritual_ZN23QWaylandQuickCompositor17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QWaylandQuickCompositor17componentCompleteEv'
    self.uglySide.call(ritual)
