"""
QVideoFramePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideoframe_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QVideoFramePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractVideoBuffer, QHwVideoBuffer, QVideoFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVideoFrame = WAIT['QVideoFrame']


class QVideoFramePrivate(QSharedData):
  """
  The cute side of Qt's QVideoFramePrivate: a plain Python object standing in
  front of one C++ QVideoFramePrivate.

  It is built on the cute 'QSharedData', as Qt's QVideoFramePrivate is built
  on Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVideoFramePrivate that has a ritual and that Python
  can call so far, 4 names in all: 'hwBuffer', 'hasDmaBuf', 'buffer',
  'adoptThisByVideoFrame'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoFramePrivate::~QVideoFramePrivate()': the destructor: Python
    never removes a C++ QVideoFramePrivate.
  - Qt's 'QVideoFramePrivate *QVideoFramePrivate::handle(QVideoFrame
    &frame)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 a template; 2 forbidden.

  What to expect
  --------------

  - The C++ QVideoFramePrivate is created at the first use, not by
    'QVideoFramePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVideoFramePrivate.
  - Each name of Qt's QVideoFramePrivate that has no cute function yet,
    'createFrame', 'handle', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVideoFrame)
  def hwBuffer(frame: QVideoFrame) -> Optional[QHwVideoBuffer]:
    """
    Calls Qt's 'QHwVideoBuffer *QVideoFramePrivate::hwBuffer(const
    QVideoFrame &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeprivate.html#hwBuffer

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.

    Returns
    -------

    Optional[QHwVideoBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHwVideoBuffer *QVideoFramePrivate::hwBuffer(const QVideoFrame &frame)
    address = Rituals.call(
        'ritual_ZN18QVideoFramePrivate8hwBufferERK11QVideoFrame',
        CuteMixin._valueOf(frame),
    )
    from . import QHwVideoBuffer
    return QHwVideoBuffer._cuteAt(address)

  @staticmethod
  @overload(QVideoFrame)
  def hasDmaBuf(frame: QVideoFrame) -> bool:
    """
    Calls Qt's 'bool QVideoFramePrivate::hasDmaBuf(const QVideoFrame
    &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeprivate.html#hasDmaBuf

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  bool QVideoFramePrivate::hasDmaBuf(const QVideoFrame &frame)
    return Rituals.call(
        'ritual_ZN18QVideoFramePrivate9hasDmaBufERK11QVideoFrame',
        CuteMixin._valueOf(frame),
    )

  @staticmethod
  @overload(QVideoFrame)
  def buffer(frame: QVideoFrame) -> Optional[QAbstractVideoBuffer]:
    """
    Calls Qt's 'QAbstractVideoBuffer *QVideoFramePrivate::buffer(const
    QVideoFrame &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeprivate.html#buffer

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.

    Returns
    -------

    Optional[QAbstractVideoBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractVideoBuffer *QVideoFramePrivate::buffer(const QVideoFrame
    #      &frame)
    address = Rituals.call(
        'ritual_ZN18QVideoFramePrivate6bufferERK11QVideoFrame',
        CuteMixin._valueOf(frame),
    )
    from . import QAbstractVideoBuffer
    return QAbstractVideoBuffer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoFramePrivate'

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
    'QVideoFramePrivate::QVideoFramePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeprivate.html#QVideoFramePrivate
    """
    #  QVideoFramePrivate::QVideoFramePrivate()
    self._noteCreation(QVideoFramePrivate, lambda: Rituals.call(
        'ritual_ZN18QVideoFramePrivateC1Ev',
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

  def adoptThisByVideoFrame(self) -> QVideoFrame:
    """
    Calls Qt's 'QVideoFrame QVideoFramePrivate::adoptThisByVideoFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeprivate.html#adoptThisByVideoFrame

    Returns
    -------

    QVideoFrame
      A new cute QVideoFrame around the copy Qt gave back. Python owns it.
    """
    #  QVideoFrame QVideoFramePrivate::adoptThisByVideoFrame()
    address = self.uglySide.call(
        'ritual_ZN18QVideoFramePrivate21adoptThisByVideoFrameEv',
    )
    from . import QVideoFrame
    return QVideoFrame._cuteOwning(address)

  @staticmethod
  def createFrame(*__, **_) -> Never:
    """
    Qt's 'QVideoFramePrivate::createFrame': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QVideoFramePrivate.createFrame' has no cute function yet. Qt's "
        "'QVideoFramePrivate::createFrame': a template: a pattern and no "
        "single function.")

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'QVideoFramePrivate *QVideoFramePrivate::handle(QVideoFrame
    &frame)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVideoFramePrivate.handle' has no cute function yet. Qt's "
        "'QVideoFramePrivate *QVideoFramePrivate::handle(QVideoFrame "
        "&frame)': takes a type Python has no way to hand over yet.")
