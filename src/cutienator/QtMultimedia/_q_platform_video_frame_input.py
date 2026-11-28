"""
QPlatformVideoFrameInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideoframeinput_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformVideoFrameInput to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QPlatformVideoSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QMediaInputEncoderInterface, QVideoFrameFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMediaInputEncoderInterface = WAIT['QMediaInputEncoderInterface']
  QVideoFrameFormat = WAIT['QVideoFrameFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformVideoFrameInput(QPlatformVideoSource):
  """
  The cute side of Qt's QPlatformVideoFrameInput: a plain Python object
  standing in front of one C++ QPlatformVideoFrameInput.

  It is built on the cute 'QPlatformVideoSource', as Qt's
  QPlatformVideoFrameInput is built on Qt's QPlatformVideoSource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformVideoFrameInput that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'setActive',
  'isActive', 'frameFormat', 'errorString', 'encoderInterface',
  'setEncoderInterface', 'encoderUpdated'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformVideoFrameInput::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QPlatformVideoFrameInput::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformVideoFrameInput is created at the first use, not by
    'QPlatformVideoFrameInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformVideoFrameInput.
  - Qt tells when it has removed the C++ QPlatformVideoFrameInput. Every call
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
    Calls Qt's 'QString QPlatformVideoFrameInput::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideoframeinput.html#tr

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
    #  QString QPlatformVideoFrameInput::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QPlatformVideoFrameInput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformVideoFrameInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlatformVideoFrameInput::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideoframeinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformVideoFrameInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QPlatformVideoFrameInput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QPlatformVideoFrameInput::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideoframeinput.html#isActive
    """
    #  bool QPlatformVideoFrameInput::isActive() const
    return self.uglySide.call(
        'ritual_ZNK24QPlatformVideoFrameInput8isActiveEv',
    )

  def frameFormat(self) -> QVideoFrameFormat:
    """
    Calls Qt's 'QVideoFrameFormat QPlatformVideoFrameInput::frameFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideoframeinput.html#frameFormat

    Returns
    -------

    QVideoFrameFormat
      A new cute QVideoFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QVideoFrameFormat QPlatformVideoFrameInput::frameFormat() const
    address = self.uglySide.call(
        'ritual_ZNK24QPlatformVideoFrameInput11frameFormatEv',
    )
    from . import QVideoFrameFormat
    return QVideoFrameFormat._cuteOwning(address)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QPlatformVideoFrameInput::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideoframeinput.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformVideoFrameInput::errorString() const
    return self.uglySide.call(
        'ritual_ZNK24QPlatformVideoFrameInput11errorStringEv',
    )

  def encoderInterface(self) -> Optional[QMediaInputEncoderInterface]:
    """
    Calls Qt's 'QMediaInputEncoderInterface
    *QPlatformVideoFrameInput::encoderInterface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideoframeinput.html#encoderInterface

    Returns
    -------

    Optional[QMediaInputEncoderInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaInputEncoderInterface
    #      *QPlatformVideoFrameInput::encoderInterface() const
    address = self.uglySide.call(
        'ritual_ZNK24QPlatformVideoFrameInput16encoderInterfaceEv',
    )
    from . import QMediaInputEncoderInterface
    return QMediaInputEncoderInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPlatformVideoFrameInput::setActive(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideoframeinput.html#setActive

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPlatformVideoFrameInput::setActive(bool a0)
    self.uglySide.call('ritual_ZN24QPlatformVideoFrameInput9setActiveEb', a0)

  @overload(QMediaInputEncoderInterface)
  @overload(NoneType)
  def setEncoderInterface(
      self,
      encoderInterface: Optional[QMediaInputEncoderInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformVideoFrameInput::setEncoderInterface(QMediaInputEncoderInterface
    *encoderInterface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideoframeinput.html#setEncoderInterface

    Parameters
    ----------

    encoderInterface : Optional[QMediaInputEncoderInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformVideoFrameInput::setEncoderInterface(
    #      QMediaInputEncoderInterface *encoderInterface)
    self.uglySide.call(
        'ritual_ZN24QPlatformVideoFrameInput19setEncoderInterfaceEP27QMedia'
        'InputEncoderInterface',
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

  @overload()
  @overload(QVideoFrameFormat)
  def __init__(self, format: Optional[QVideoFrameFormat] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformVideoFrameInput::QPlatformVideoFrameInput(QVideoFrameFormat
    format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideoframeinput.html

    Parameters
    ----------

    format : Optional[QVideoFrameFormat]
      Passed on as a value: Qt reads the C++ QVideoFrameFormat, which stays
      Python's own. May be left out, as in Qt: a new 'QVideoFrameFormat()' is
      then passed on.
    """
    #  QPlatformVideoFrameInput::QPlatformVideoFrameInput(QVideoFrameFormat
    #      format)
    if format is None:
      from . import QVideoFrameFormat
      format = QVideoFrameFormat()
    self._noteCreation(QPlatformVideoFrameInput, lambda: Rituals.call(
        'ritual_ZN24QPlatformVideoFrameInputC1E17QVideoFrameFormat',
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
    Calls Qt's 'void QPlatformVideoFrameInput::encoderUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideoframeinput.html#encoderUpdated
    """
    #  void QPlatformVideoFrameInput::encoderUpdated()
    self.uglySide.call(
        'ritual_ZN24QPlatformVideoFrameInput14encoderUpdatedEv',
    )
