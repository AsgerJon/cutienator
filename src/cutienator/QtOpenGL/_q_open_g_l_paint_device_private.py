"""
QOpenGLPaintDevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintdevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLPaintDevicePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QOpenGLPaintDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLPaintDevice = WAIT['QOpenGLPaintDevice']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLPaintDevicePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLPaintDevicePrivate: a plain Python object
  standing in front of one C++ QOpenGLPaintDevicePrivate.

  C++ hands a QOpenGLPaintDevicePrivate around as a copy, so every C++
  QOpenGLPaintDevicePrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLPaintDevicePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'get', 'beginPaint', 'endPaint'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLPaintDevicePrivate::~QOpenGLPaintDevicePrivate()': the
    destructor: Python removes its C++ QOpenGLPaintDevicePrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLPaintDevicePrivate is created at the first use, not by
    'QOpenGLPaintDevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLPaintDevicePrivate back gives a copy the
    ritual made for Python, in a new cute QOpenGLPaintDevicePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLPaintDevice)
  @overload(NoneType)
  def get(
      dev: Optional[QOpenGLPaintDevice],
  ) -> Optional[QOpenGLPaintDevicePrivate]:
    """
    Calls Qt's 'QOpenGLPaintDevicePrivate
    *QOpenGLPaintDevicePrivate::get(QOpenGLPaintDevice *dev)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpaintdeviceprivate.html#get

    Parameters
    ----------

    dev : Optional[QOpenGLPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QOpenGLPaintDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLPaintDevicePrivate
    #      *QOpenGLPaintDevicePrivate::get(QOpenGLPaintDevice *dev)
    address = Rituals.call(
        'ritual_ZN25QOpenGLPaintDevicePrivate3getEP18QOpenGLPaintDevice',
        CuteMixin._addressOf(dev),
    )
    return QOpenGLPaintDevicePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLPaintDevicePrivate'

  #  A C++ QOpenGLPaintDevicePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLPaintDevicePrivate'

  #  The functions Qt calls itself that QOpenGLPaintDevicePrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'beginPaint': (
          ('_ZN25QOpenGLPaintDevicePrivate10beginPaintEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endPaint': (
          ('_ZN25QOpenGLPaintDevicePrivate8endPaintEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Qt's '~QOpenGLPaintDevicePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLPaintDevicePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QOpenGLPaintDevicePrivateD1Ev'

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

  @overload(QSize)
  def __init__(self, size: QSize) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLPaintDevicePrivate::QOpenGLPaintDevicePrivate(const QSize
    &size)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdeviceprivate.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QOpenGLPaintDevicePrivate::QOpenGLPaintDevicePrivate(const QSize
    #      &size)
    self._noteCreation(QOpenGLPaintDevicePrivate, lambda: Rituals.call(
        'ritual_ZN25QOpenGLPaintDevicePrivateC1ERK5QSize',
        self._valueOf(size),
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

  def beginPaint(self) -> None:
    """
    Calls Qt's 'void QOpenGLPaintDevicePrivate::beginPaint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdeviceprivate.html#beginPaint
    """
    #  void QOpenGLPaintDevicePrivate::beginPaint()
    ritual = 'ritual_ZN25QOpenGLPaintDevicePrivate10beginPaintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QOpenGLPaintDevicePrivate10beginPaintEv'
    self.uglySide.call(ritual)

  def endPaint(self) -> None:
    """
    Calls Qt's 'void QOpenGLPaintDevicePrivate::endPaint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdeviceprivate.html#endPaint
    """
    #  void QOpenGLPaintDevicePrivate::endPaint()
    ritual = 'ritual_ZN25QOpenGLPaintDevicePrivate8endPaintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QOpenGLPaintDevicePrivate8endPaintEv'
    self.uglySide.call(ritual)
