"""
QNonContiguousByteDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNonContiguousByteDevice to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNonContiguousByteDevice(QObject):
  """
  The cute side of Qt's QNonContiguousByteDevice: a plain Python object
  standing in front of one C++ QNonContiguousByteDevice.

  It is built on the cute 'QObject', as Qt's QNonContiguousByteDevice is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNonContiguousByteDevice that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr',
  'advanceReadPointer', 'atEnd', 'pos', 'reset', 'size', 'readyRead',
  'readProgress'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNonContiguousByteDevice::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QNonContiguousByteDevice::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const char *QNonContiguousByteDevice::readPointer(qint64
    maximumLength, qint64 &len)': takes a number to change where it is.
  - Qt's 'QNonContiguousByteDevice::~QNonContiguousByteDevice()': the
    destructor: Python never removes a C++ QNonContiguousByteDevice.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QNonContiguousByteDevice is created at the first use, not by
    'QNonContiguousByteDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNonContiguousByteDevice.
  - Qt tells when it has removed the C++ QNonContiguousByteDevice. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNonContiguousByteDevice that has no cute function yet,
    '__init__', 'readPointer', holds a function that raises
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
    Calls Qt's 'QString QNonContiguousByteDevice::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnoncontiguousbytedevice.html#tr

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
    #  QString QNonContiguousByteDevice::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QNonContiguousByteDevice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNonContiguousByteDevice'

  #  A C++ QNonContiguousByteDevice Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNonContiguousByteDevice'

  #  The functions Qt calls itself that QNonContiguousByteDevice is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'readPointer': (
          'const char *QNonContiguousByteDevice::readPointer(qint64, '
          'qint64 &)',
      ),
  }

  #  The functions Qt calls itself that QNonContiguousByteDevice is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'advanceReadPointer': (
          ('_ZN24QNonContiguousByteDevice18advanceReadPointerEx',
           ('bool', 'number', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'atEnd': (
          ('_ZNK24QNonContiguousByteDevice5atEndEv',
           ('bool', 'number', ''),
           ()),
      ),
      'pos': (
          ('_ZNK24QNonContiguousByteDevice3posEv',
           ('long long', 'number', ''),
           ()),
      ),
      'reset': (
          ('_ZN24QNonContiguousByteDevice5resetEv',
           ('bool', 'number', ''),
           ()),
      ),
      'size': (
          ('_ZNK24QNonContiguousByteDevice4sizeEv',
           ('long long', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNonContiguousByteDevice::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNonContiguousByteDevice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QNonContiguousByteDevice10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QNonContiguousByteDevice::atEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevice.html#atEnd
    """
    #  bool QNonContiguousByteDevice::atEnd() const
    return self.uglySide.call('ritual_ZNK24QNonContiguousByteDevice5atEndEv')

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QNonContiguousByteDevice::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnoncontiguousbytedevice.html#pos
    """
    #  qint64 QNonContiguousByteDevice::pos() const
    ritual = 'ritual_ZNK24QNonContiguousByteDevice3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QNonContiguousByteDevice3posEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QNonContiguousByteDevice::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnoncontiguousbytedevice.html#size
    """
    #  qint64 QNonContiguousByteDevice::size() const
    return self.uglySide.call('ritual_ZNK24QNonContiguousByteDevice4sizeEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNonContiguousByteDevice::QNonContiguousByteDevice()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QNonContiguousByteDevice.__init__' has no cute function yet. Qt's "
        "'QNonContiguousByteDevice::QNonContiguousByteDevice()': the class "
        "is abstract, so C++ cannot make one, and the C++ class of ours "
        "does not fill in every function it leaves open.")

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

  @overload(int)
  def advanceReadPointer(self, amount: int) -> bool:
    """
    Calls Qt's 'bool QNonContiguousByteDevice::advanceReadPointer(qint64
    amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevice.html#advanceReadPointer

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  bool QNonContiguousByteDevice::advanceReadPointer(qint64 amount)
    return self.uglySide.call(
        'ritual_ZN24QNonContiguousByteDevice18advanceReadPointerEx', amount,
    )

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QNonContiguousByteDevice::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevice.html#reset
    """
    #  bool QNonContiguousByteDevice::reset()
    return self.uglySide.call('ritual_ZN24QNonContiguousByteDevice5resetEv')

  def readyRead(self) -> None:
    """
    Calls Qt's 'void QNonContiguousByteDevice::readyRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevice.html#readyRead
    """
    #  void QNonContiguousByteDevice::readyRead()
    self.uglySide.call('ritual_ZN24QNonContiguousByteDevice9readyReadEv')

  @overload(int, int)
  def readProgress(self, current: int, total: int) -> None:
    """
    Calls Qt's 'void QNonContiguousByteDevice::readProgress(qint64 current,
    qint64 total)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevice.html#readProgress

    Parameters
    ----------

    current : int
      Passed on as it is.

    total : int
      Passed on as it is.
    """
    #  void QNonContiguousByteDevice::readProgress(qint64 current, qint64
    #      total)
    self.uglySide.call(
        'ritual_ZN24QNonContiguousByteDevice12readProgressExx',
        current, total,
    )

  @staticmethod
  def readPointer(*__, **_) -> Never:
    """
    Qt's 'const char *QNonContiguousByteDevice::readPointer(qint64
    maximumLength, qint64 &len)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QNonContiguousByteDevice.readPointer' has no cute function yet. "
        "Qt's 'const char *QNonContiguousByteDevice::readPointer(qint64 "
        "maximumLength, qint64 &len)': takes a number to change where it is."
    )
