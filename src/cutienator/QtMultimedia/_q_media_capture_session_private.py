"""
QMediaCaptureSessionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qmediacapturesession_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QMediaCaptureSessionPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMediaCaptureSession, QVideoSink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMediaCaptureSession = WAIT['QMediaCaptureSession']
  QVideoSink = WAIT['QVideoSink']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMediaCaptureSessionPrivate(QObjectPrivate):
  """
  The cute side of Qt's QMediaCaptureSessionPrivate: a plain Python object
  standing in front of one C++ QMediaCaptureSessionPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QMediaCaptureSessionPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QMediaCaptureSessionPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'get', 'q_func',
  'setVideoSink'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMediaCaptureSession *QMediaCaptureSessionPrivate::q_func()
    const': takes in Python what 'QMediaCaptureSession
    *QMediaCaptureSessionPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QMediaCaptureSessionPrivate is created at the first use, not by
    'QMediaCaptureSessionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMediaCaptureSessionPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def get(
      session: Optional[QMediaCaptureSession],
  ) -> Optional[QMediaCaptureSessionPrivate]:
    """
    Calls Qt's 'QMediaCaptureSessionPrivate
    *QMediaCaptureSessionPrivate::get(QMediaCaptureSession *session)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesessionprivate.html#get

    Parameters
    ----------

    session : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMediaCaptureSessionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSessionPrivate
    #      *QMediaCaptureSessionPrivate::get(QMediaCaptureSession *session)
    address = Rituals.call(
        'ritual_ZN27QMediaCaptureSessionPrivate3getEP20QMediaCaptureSession',
        CuteMixin._addressOf(session),
    )
    return QMediaCaptureSessionPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaCaptureSessionPrivate'

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

  @overload(QVideoSink)
  @overload(NoneType)
  def setVideoSink(self, sink: Optional[QVideoSink]) -> None:
    """
    Calls Qt's 'void QMediaCaptureSessionPrivate::setVideoSink(QVideoSink
    *sink)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesessionprivate.html#setVideoSink

    Parameters
    ----------

    sink : Optional[QVideoSink]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaCaptureSessionPrivate::setVideoSink(QVideoSink *sink)
    self.uglySide.call(
        'ritual_ZN27QMediaCaptureSessionPrivate12setVideoSinkEP10QVideoSink',
        self._addressOf(sink),
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

  def q_func(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession *QMediaCaptureSessionPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediacapturesessionprivate.html#q_func

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QMediaCaptureSessionPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QMediaCaptureSessionPrivate6q_funcEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)
