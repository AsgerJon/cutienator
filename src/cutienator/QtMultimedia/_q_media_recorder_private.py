"""
QMediaRecorderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qmediarecorder_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QMediaRecorderPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMediaRecorder


class QMediaRecorderPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMediaRecorderPrivate: a plain Python object standing
  in front of one C++ QMediaRecorderPrivate.

  C++ hands a QMediaRecorderPrivate around as a copy, so every C++
  QMediaRecorderPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMediaRecorderPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func',
  'msgFailedStartRecording'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMediaRecorder *QMediaRecorderPrivate::q_func() const': takes
    in Python what 'QMediaRecorder *QMediaRecorderPrivate::q_func()' takes.
  - Qt's 'QMediaRecorderPrivate::~QMediaRecorderPrivate()': the destructor:
    Python removes its C++ QMediaRecorderPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QMediaRecorderPrivate is created at the first use, not by
    'QMediaRecorderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMediaRecorderPrivate back gives a copy the ritual
    made for Python, in a new cute QMediaRecorderPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def msgFailedStartRecording() -> str:
    """
    Calls Qt's 'QString QMediaRecorderPrivate::msgFailedStartRecording()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorderprivate.html#msgFailedStartRecording

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaRecorderPrivate::msgFailedStartRecording()
    return Rituals.call(
        'ritual_ZN21QMediaRecorderPrivate23msgFailedStartRecordingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaRecorderPrivate'

  #  Qt's '~QMediaRecorderPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QMediaRecorderPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QMediaRecorderPrivateD1Ev'

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
    'QMediaRecorderPrivate::QMediaRecorderPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorderprivate.html#QMediaRecorderPrivate
    """
    #  QMediaRecorderPrivate::QMediaRecorderPrivate()
    self._noteCreation(QMediaRecorderPrivate, lambda: Rituals.call(
        'ritual_ZN21QMediaRecorderPrivateC1Ev',
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

  def q_func(self) -> Optional[QMediaRecorder]:
    """
    Calls Qt's 'QMediaRecorder *QMediaRecorderPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorderprivate.html#q_func

    Returns
    -------

    Optional[QMediaRecorder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaRecorder *QMediaRecorderPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QMediaRecorderPrivate6q_funcEv')
    from . import QMediaRecorder
    return QMediaRecorder._cuteAt(address)
