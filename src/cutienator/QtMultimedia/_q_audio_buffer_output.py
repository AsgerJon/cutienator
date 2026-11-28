"""
QAudioBufferOutput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudiobufferoutput.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAudioBuffer, QAudioBufferOutputPrivate, QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioBuffer = WAIT['QAudioBuffer']
  QAudioFormat = WAIT['QAudioFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioBufferOutput(QObject):
  """
  The cute side of Qt's QAudioBufferOutput: a plain Python object standing in
  front of one C++ QAudioBufferOutput.

  It is built on the cute 'QObject', as Qt's QAudioBufferOutput is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioBufferOutput that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'format',
  'audioBufferReceived', 'd_func'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAudioBufferOutput::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAudioBufferOutput::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAudioBufferOutput::~QAudioBufferOutput()': the destructor: Python
    never removes a C++ QAudioBufferOutput.
  - Qt's 'const QAudioBufferOutputPrivate *QAudioBufferOutput::d_func()
    const': takes in Python what 'QAudioBufferOutputPrivate
    *QAudioBufferOutput::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAudioBufferOutput is created at the first use, not by
    'QAudioBufferOutput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioBufferOutput.
  - Qt tells when it has removed the C++ QAudioBufferOutput. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QAudioBufferOutput::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobufferoutput.html#tr

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
    #  QString QAudioBufferOutput::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QAudioBufferOutput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioBufferOutput'

  #  A C++ QAudioBufferOutput Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioBufferOutput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAudioBufferOutput::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobufferoutput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAudioBufferOutput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QAudioBufferOutput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def format(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QAudioBufferOutput::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobufferoutput.html#format

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QAudioBufferOutput::format() const
    address = self.uglySide.call('ritual_ZNK18QAudioBufferOutput6formatEv')
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

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
    'QAudioBufferOutput::QAudioBufferOutput(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferoutput.html#QAudioBufferOutput

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioBufferOutput::QAudioBufferOutput(QObject *parent)
    self._noteCreation(QAudioBufferOutput, lambda: Rituals.call(
        'ritual_ZN18QAudioBufferOutputC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QAudioFormat)
  @overload(QAudioFormat, QObject)
  @overload(QAudioFormat, NoneType)
  def __init__(
      self,
      format: QAudioFormat,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAudioBufferOutput::QAudioBufferOutput(const QAudioFormat &format,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferoutput.html#QAudioBufferOutput

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioBufferOutput::QAudioBufferOutput(const QAudioFormat &format,
    #      QObject *parent)
    self._noteCreation(QAudioBufferOutput, lambda: Rituals.call(
        'ritual_ZN18QAudioBufferOutputC1ERK12QAudioFormatP7QObject',
        self._valueOf(format), self._addressOf(parent, 'QObject'),
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

  @overload(QAudioBuffer)
  def audioBufferReceived(self, buffer: QAudioBuffer) -> None:
    """
    Calls Qt's 'void QAudioBufferOutput::audioBufferReceived(const
    QAudioBuffer &buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferoutput.html#audioBufferReceived

    Parameters
    ----------

    buffer : QAudioBuffer
      Passed on as a value: Qt reads the C++ QAudioBuffer, which stays
      Python's own.
    """
    #  void QAudioBufferOutput::audioBufferReceived(const QAudioBuffer
    #      &buffer)
    self.uglySide.call(
        'ritual_ZN18QAudioBufferOutput19audioBufferReceivedERK12QAudioBuffe'
        'r',
        self._valueOf(buffer),
    )

  def d_func(self) -> Optional[QAudioBufferOutputPrivate]:
    """
    Calls Qt's 'QAudioBufferOutputPrivate *QAudioBufferOutput::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobufferoutput.html#d_func

    Returns
    -------

    Optional[QAudioBufferOutputPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioBufferOutputPrivate *QAudioBufferOutput::d_func()
    address = self.uglySide.call('ritual_ZN18QAudioBufferOutput6d_funcEv')
    from . import QAudioBufferOutputPrivate
    return QAudioBufferOutputPrivate._cuteAt(address)
