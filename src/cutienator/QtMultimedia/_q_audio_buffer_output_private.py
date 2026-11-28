"""
QAudioBufferOutputPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qaudiobufferoutput_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAudioBufferOutputPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioFormat = WAIT['QAudioFormat']


class QAudioBufferOutputPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAudioBufferOutputPrivate: a plain Python object
  standing in front of one C++ QAudioBufferOutputPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QAudioBufferOutputPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  No function of Qt's QAudioBufferOutputPrivate yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMediaPlayer
    *QAudioBufferOutputPrivate::exchangeMediaPlayer(QAudioBufferOutput
    &output, QMediaPlayer *player)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QAudioBufferOutputPrivate is created at the first use, not by
    'QAudioBufferOutputPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioBufferOutputPrivate.
  - Each name of Qt's QAudioBufferOutputPrivate that has no cute function
    yet, 'exchangeMediaPlayer', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioBufferOutputPrivate'

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

  @overload(QAudioFormat)
  def __init__(self, format: QAudioFormat) -> None:
    """
    Notes what was given, for Qt's
    'QAudioBufferOutputPrivate::QAudioBufferOutputPrivate(const QAudioFormat
    &format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferoutputprivate.html

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  QAudioBufferOutputPrivate::QAudioBufferOutputPrivate(const
    #      QAudioFormat &format)
    self._noteCreation(QAudioBufferOutputPrivate, lambda: Rituals.call(
        'ritual_ZN25QAudioBufferOutputPrivateC1ERK12QAudioFormat',
        self._valueOf(format),
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

  @staticmethod
  def exchangeMediaPlayer(*__, **_) -> Never:
    """
    Qt's 'QMediaPlayer
    *QAudioBufferOutputPrivate::exchangeMediaPlayer(QAudioBufferOutput
    &output, QMediaPlayer *player)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QAudioBufferOutputPrivate.exchangeMediaPlayer' has no cute "
        "function yet. Qt's 'QMediaPlayer "
        "*QAudioBufferOutputPrivate::exchangeMediaPlayer(QAudioBufferOutput "
        "&output, QMediaPlayer *player)': takes a type Python has no way to "
        "hand over yet.")
