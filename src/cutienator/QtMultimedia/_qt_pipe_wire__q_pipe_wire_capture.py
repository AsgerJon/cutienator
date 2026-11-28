"""
QtPipeWire::QPipeWireCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qpipewire_screencapture_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtPipeWire::QPipeWireCapture to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QPlatformSurfaceCapture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QVideoFrameFormat

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPipeWireCapture(QPlatformSurfaceCapture):
  """
  The cute side of Qt's QtPipeWire::QPipeWireCapture: a plain Python object
  standing in front of one C++ QtPipeWire::QPipeWireCapture.

  It is built on the cute 'QPlatformSurfaceCapture', as Qt's
  QtPipeWire::QPipeWireCapture is built on Qt's QPlatformSurfaceCapture, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QtPipeWire::QPipeWireCapture that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'frameFormat', 'setActiveInternal'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtPipeWire::QPipeWireCapture::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtPipeWire::QPipeWireCapture::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtPipeWire::QPipeWireCapture::~QPipeWireCapture()': the destructor:
    Python never removes a C++ QtPipeWire::QPipeWireCapture.
  - Qt's 'std::unique_ptr<QPipeWireCapture>
    QtPipeWire::QPipeWireCapture::create(Source initialSource)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 2 not a gap; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtPipeWire::QPipeWireCapture is created at the first use, not by
    'QtPipeWire::QPipeWireCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtPipeWire::QPipeWireCapture.
  - Qt tells when it has removed the C++ QtPipeWire::QPipeWireCapture. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtPipeWire::QPipeWireCapture that has no cute function
    yet, '__init__', 'create', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QtPipeWire::QPipeWireCapture::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtpipewire-qpipewirecapture.html#tr

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
    #  QString QtPipeWire::QPipeWireCapture::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10QtPipeWire16QPipeWireCapture2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPipeWire::QPipeWireCapture'

  #  A C++ QtPipeWire::QPipeWireCapture Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtPipeWire_QPipeWireCapture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtPipeWire::QPipeWireCapture::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtpipewire-qpipewirecapture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtPipeWire::QPipeWireCapture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10QtPipeWire16QPipeWireCapture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def frameFormat(self) -> QVideoFrameFormat:
    """
    Calls Qt's 'QVideoFrameFormat QtPipeWire::QPipeWireCapture::frameFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtpipewire-qpipewirecapture.html#frameFormat

    Returns
    -------

    QVideoFrameFormat
      A new cute QVideoFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QVideoFrameFormat QtPipeWire::QPipeWireCapture::frameFormat() const
    ritual = 'ritual_ZNK10QtPipeWire16QPipeWireCapture11frameFormatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QtPipeWire16QPipeWireCapture11frameFormatEv'
    address = self.uglySide.call(ritual)
    from . import QVideoFrameFormat
    return QVideoFrameFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActiveInternal(self, active: bool) -> bool:
    """
    Calls Qt's 'bool QtPipeWire::QPipeWireCapture::setActiveInternal(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtpipewire-qpipewirecapture.html#setActiveInternal

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  bool QtPipeWire::QPipeWireCapture::setActiveInternal(bool active)
    ritual = 'ritual_ZN10QtPipeWire16QPipeWireCapture17setActiveInternalEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QtPipeWire16QPipeWireCapture17setActiveInternalEb')
    return self.uglySide.call(ritual, active)

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
    Qt's 'QtPipeWire::QPipeWireCapture::QPipeWireCapture(Source
    initialSource, std::shared_ptr<QPipeWireInstance> a1)': the compiler
    refuses its ritual as it would be written here: unknown type name
    'QPipeWireInstance'; did you mean 'QtPipeWire::QPipeWireInstance'?.
    """
    raise NotImplementedError(
        "'QtPipeWire.QPipeWireCapture.__init__' has no cute function yet. "
        "Qt's 'QtPipeWire::QPipeWireCapture::QPipeWireCapture(Source "
        "initialSource, std::shared_ptr<QPipeWireInstance> a1)': the "
        "compiler refuses its ritual as it would be written here: unknown "
        "type name 'QPipeWireInstance'; did you mean "
        "'QtPipeWire::QPipeWireInstance'?.")

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
  def create(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QPipeWireCapture>
    QtPipeWire::QPipeWireCapture::create(Source initialSource)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtPipeWire.QPipeWireCapture.create' has no cute function yet. "
        "Qt's 'std::unique_ptr<QPipeWireCapture> "
        "QtPipeWire::QPipeWireCapture::create(Source initialSource)': takes "
        "a type Python has no way to hand over yet.")
