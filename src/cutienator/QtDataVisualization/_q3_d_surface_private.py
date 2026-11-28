"""
Q3DSurfacePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dsurface_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Q3DSurfacePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstract3DGraphPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import Q3DSurface, QAbstract3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DAxis = WAIT['QtDataVisualization:QAbstract3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DSurfacePrivate(QAbstract3DGraphPrivate):
  """
  The cute side of Qt's Q3DSurfacePrivate: a plain Python object standing in
  front of one C++ Q3DSurfacePrivate.

  It is built on the cute 'QAbstract3DGraphPrivate', as Qt's
  Q3DSurfacePrivate is built on Qt's QAbstract3DGraphPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DSurfacePrivate that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'handleAxisXChanged',
  'handleAxisYChanged', 'handleAxisZChanged', 'qptr'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DSurfacePrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Q3DSurfacePrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DSurfacePrivate::~Q3DSurfacePrivate()': the destructor: Python
    never removes a C++ Q3DSurfacePrivate.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 leans on
  'Q3DSurfacePrivate.

  What to expect
  --------------

  - The C++ Q3DSurfacePrivate is created at the first use, not by
    'Q3DSurfacePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DSurfacePrivate.
  - Qt tells when it has removed the C++ Q3DSurfacePrivate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Q3DSurfacePrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DSurfacePrivate'

  #  A C++ Q3DSurfacePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DSurfacePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DSurfacePrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfaceprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DSurfacePrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17Q3DSurfacePrivate10metaObjectEv',
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
    Qt's 'Q3DSurfacePrivate::Q3DSurfacePrivate(Q3DSurface *q)': leans on
    'Q3DSurfacePrivate::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'Q3DSurfacePrivate.__init__' has no cute function yet. Qt's "
        "'Q3DSurfacePrivate::Q3DSurfacePrivate(Q3DSurface *q)': leans on "
        "'Q3DSurfacePrivate::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisXChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfacePrivate::handleAxisXChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfaceprivate.html#handleAxisXChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfacePrivate::handleAxisXChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN17Q3DSurfacePrivate18handleAxisXChangedEP15QAbstract3DAxi'
        's')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Q3DSurfacePrivate18handleAxisXChangedEP15QAbstrac'
          't3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisYChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfacePrivate::handleAxisYChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfaceprivate.html#handleAxisYChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfacePrivate::handleAxisYChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN17Q3DSurfacePrivate18handleAxisYChangedEP15QAbstract3DAxi'
        's')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Q3DSurfacePrivate18handleAxisYChangedEP15QAbstrac'
          't3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisZChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfacePrivate::handleAxisZChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfaceprivate.html#handleAxisZChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfacePrivate::handleAxisZChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN17Q3DSurfacePrivate18handleAxisZChangedEP15QAbstract3DAxi'
        's')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17Q3DSurfacePrivate18handleAxisZChangedEP15QAbstrac'
          't3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  def qptr(self) -> Optional[Q3DSurface]:
    """
    Calls Qt's 'Q3DSurface *Q3DSurfacePrivate::qptr()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfaceprivate.html#qptr

    Returns
    -------

    Optional[Q3DSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DSurface *Q3DSurfacePrivate::qptr()
    address = self.uglySide.call('ritual_ZN17Q3DSurfacePrivate4qptrEv')
    from . import Q3DSurface
    return Q3DSurface._cuteAt(address)
