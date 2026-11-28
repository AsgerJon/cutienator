"""
QAudioListener binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/qaudiolistener.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QQuaternion, QVector3D
  from . import QAudioEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioEngine = WAIT['QAudioEngine']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioListener(QObject):
  """
  The cute side of Qt's QAudioListener: a plain Python object standing in
  front of one C++ QAudioListener.

  It is built on the cute 'QObject', as Qt's QAudioListener is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioListener that has a ritual and that Python can
  call so far, 5 names in all: 'setPosition', 'position', 'setRotation',
  'rotation', 'engine'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAudioListener::~QAudioListener()': the destructor: Python never
    removes a C++ QAudioListener.
  - Qt's 'QAudioListenerPrivate *QAudioListener::d_func()': gives
    'QAudioListenerPrivate', which has no cute class yet.
  - Qt's 'const QAudioListenerPrivate *QAudioListener::d_func() const': gives
    'QAudioListenerPrivate', which has no cute class yet.

  What to expect
  --------------

  - The C++ QAudioListener is created at the first use, not by
    'QAudioListener(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioListener.
  - Qt tells when it has removed the C++ QAudioListener. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioListener'

  #  A C++ QAudioListener Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioListener'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QAudioListener::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiolistener.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QAudioListener::position() const
    address = self.uglySide.call('ritual_ZNK14QAudioListener8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QAudioListener::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiolistener.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QAudioListener::rotation() const
    address = self.uglySide.call('ritual_ZNK14QAudioListener8rotationEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def engine(self) -> Optional[QAudioEngine]:
    """
    Calls Qt's 'QAudioEngine *QAudioListener::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiolistener.html#engine

    Returns
    -------

    Optional[QAudioEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioEngine *QAudioListener::engine() const
    address = self.uglySide.call('ritual_ZNK14QAudioListener6engineEv')
    from . import QAudioEngine
    return QAudioEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPosition(self, pos: QVector3D) -> None:
    """
    Calls Qt's 'void QAudioListener::setPosition(QVector3D pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiolistener.html#setPosition

    Parameters
    ----------

    pos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QAudioListener::setPosition(QVector3D pos)
    self.uglySide.call(
        'ritual_ZN14QAudioListener11setPositionE9QVector3D',
        self._valueOf(pos),
    )

  @overload(QQuaternion)
  def setRotation(self, q: QQuaternion) -> None:
    """
    Calls Qt's 'void QAudioListener::setRotation(const QQuaternion &q)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiolistener.html#setRotation

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QAudioListener::setRotation(const QQuaternion &q)
    self.uglySide.call(
        'ritual_ZN14QAudioListener11setRotationERK11QQuaternion',
        self._valueOf(q),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioEngine)
  @overload(NoneType)
  def __init__(self, engine: Optional[QAudioEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QAudioListener::QAudioListener(QAudioEngine *engine)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiolistener.html#QAudioListener

    Parameters
    ----------

    engine : Optional[QAudioEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAudioListener::QAudioListener(QAudioEngine *engine)
    self._noteCreation(QAudioListener, lambda: Rituals.call(
        'ritual_ZN14QAudioListenerC1EP12QAudioEngine',
        self._addressOf(engine),
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
