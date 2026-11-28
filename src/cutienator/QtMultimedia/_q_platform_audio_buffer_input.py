"""
QPlatformAudioBufferInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiobufferinput_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformAudioBufferInput to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAudioBufferSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAudioFormat, QMediaInputEncoderInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioFormat = WAIT['QAudioFormat']
  QMediaInputEncoderInterface = WAIT['QMediaInputEncoderInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformAudioBufferInput(QAudioBufferSource):
  """
  The cute side of Qt's QPlatformAudioBufferInput: a plain Python object
  standing in front of one C++ QPlatformAudioBufferInput.

  It is built on the cute 'QAudioBufferSource', as Qt's
  QPlatformAudioBufferInput is built on Qt's QAudioBufferSource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformAudioBufferInput that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'audioFormat',
  'encoderInterface', 'setEncoderInterface', 'encoderUpdated'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformAudioBufferInput::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QPlatformAudioBufferInput::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformAudioBufferInput is created at the first use, not by
    'QPlatformAudioBufferInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformAudioBufferInput.
  - Qt tells when it has removed the C++ QPlatformAudioBufferInput. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPlatformAudioBufferInput::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiobufferinput.html#tr

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
    #  QString QPlatformAudioBufferInput::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QPlatformAudioBufferInput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformAudioBufferInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlatformAudioBufferInput::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiobufferinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformAudioBufferInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformAudioBufferInput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def audioFormat(self) -> QAudioFormat:
    """
    Calls Qt's 'const QAudioFormat &QPlatformAudioBufferInput::audioFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiobufferinput.html#audioFormat

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  const QAudioFormat &QPlatformAudioBufferInput::audioFormat() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformAudioBufferInput11audioFormatEv',
    )
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def encoderInterface(self) -> Optional[QMediaInputEncoderInterface]:
    """
    Calls Qt's 'QMediaInputEncoderInterface
    *QPlatformAudioBufferInput::encoderInterface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiobufferinput.html#encoderInterface

    Returns
    -------

    Optional[QMediaInputEncoderInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaInputEncoderInterface
    #      *QPlatformAudioBufferInput::encoderInterface() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformAudioBufferInput16encoderInterfaceEv',
    )
    from . import QMediaInputEncoderInterface
    return QMediaInputEncoderInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMediaInputEncoderInterface)
  @overload(NoneType)
  def setEncoderInterface(
      self,
      encoderInterface: Optional[QMediaInputEncoderInterface],
  ) -> None:
    """
    Calls Qt's 'void QPlatformAudioBufferInput::setEncoderInterface(
    QMediaInputEncoderInterface *encoderInterface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiobufferinput.html#setEncoderInterface

    Parameters
    ----------

    encoderInterface : Optional[QMediaInputEncoderInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformAudioBufferInput::setEncoderInterface(
    #      QMediaInputEncoderInterface *encoderInterface)
    self.uglySide.call(
        'ritual_ZN25QPlatformAudioBufferInput19setEncoderInterfaceEP27QMedi'
        'aInputEncoderInterface',
        self._addressOf(encoderInterface),
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

  @overload(QAudioFormat)
  def __init__(self, format: QAudioFormat) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformAudioBufferInput::QPlatformAudioBufferInput(const QAudioFormat
    &format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiobufferinput.html

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  QPlatformAudioBufferInput::QPlatformAudioBufferInput(const
    #      QAudioFormat &format)
    self._noteCreation(QPlatformAudioBufferInput, lambda: Rituals.call(
        'ritual_ZN25QPlatformAudioBufferInputC1ERK12QAudioFormat',
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

  def encoderUpdated(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioBufferInput::encoderUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiobufferinput.html#encoderUpdated
    """
    #  void QPlatformAudioBufferInput::encoderUpdated()
    self.uglySide.call(
        'ritual_ZN25QPlatformAudioBufferInput14encoderUpdatedEv',
    )
