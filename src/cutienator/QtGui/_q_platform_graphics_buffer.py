"""
QPlatformGraphicsBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformgraphicsbuffer.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from . import QPixelFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPixelFormat = WAIT['QPixelFormat']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformGraphicsBuffer(QObject):
  """
  The cute side of Qt's QPlatformGraphicsBuffer: a plain Python object
  standing in front of one C++ QPlatformGraphicsBuffer.

  It is built on the cute 'QObject', as Qt's QPlatformGraphicsBuffer is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformGraphicsBuffer that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'isLocked',
  'lock', 'unlock', 'bindToTexture', 'bytesPerLine', 'byteCount', 'origin',
  'size', 'format', 'unlocked', 'doLock', 'doUnlock'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformGraphicsBuffer::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformGraphicsBuffer::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformGraphicsBuffer::~QPlatformGraphicsBuffer()': the
    destructor: Python never removes a C++ QPlatformGraphicsBuffer.
  - Qt's 'const uchar *QPlatformGraphicsBuffer::data() const': gives
    'unsigned char', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 2 not a gap; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QPlatformGraphicsBuffer is created at the first use, not by
    'QPlatformGraphicsBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformGraphicsBuffer.
  - Qt tells when it has removed the C++ QPlatformGraphicsBuffer. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformGraphicsBuffer that has no cute function yet,
    'data', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QPlatformGraphicsBuffer, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class AccessType(CuteFlags):
    """
    The flags enum 'QPlatformGraphicsBuffer::AccessType' of Qt, with the 5
    names Qt gives in it. Qt names the type of its combinations
    'QPlatformGraphicsBuffer::AccessTypes'.
    """

    NULL = 0x0
    SWReadAccess = 0x1
    SWWriteAccess = 0x2
    TextureAccess = 0x4
    HWCompositor = 0x8

  AccessTypes = AccessType

  class Origin(CuteNum):
    """
    The enum 'QPlatformGraphicsBuffer::Origin' of Qt, with the 2 names Qt
    gives in it.
    """

    OriginBottomLeft = Kee[int](0)
    OriginTopLeft = Kee[int](1)

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
    Calls Qt's 'QString QPlatformGraphicsBuffer::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#tr

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
    #  QString QPlatformGraphicsBuffer::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QPlatformGraphicsBuffer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformGraphicsBuffer'

  #  A C++ QPlatformGraphicsBuffer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformGraphicsBuffer'

  #  The functions Qt calls itself that QPlatformGraphicsBuffer is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'data': (
          'const uchar *QPlatformGraphicsBuffer::data() const',
          'uchar *QPlatformGraphicsBuffer::data()',
      ),
  }

  #  The functions Qt calls itself that QPlatformGraphicsBuffer is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'bindToTexture': (
          ('_ZNK23QPlatformGraphicsBuffer13bindToTextureERK5QRect',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'bytesPerLine': (
          ('_ZNK23QPlatformGraphicsBuffer12bytesPerLineEv',
           ('int', 'number', ''),
           ()),
      ),
      'origin': (
          ('_ZNK23QPlatformGraphicsBuffer6originEv',
           ('int', 'enum', 'QtGui:QPlatformGraphicsBuffer.Origin'),
           ()),
      ),
      'doLock': (
          ('_ZN23QPlatformGraphicsBuffer6doLockE6QFlagsINS_10AccessTypeEERK'
           '5QRect',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtGui:QPlatformGraphicsBuffer.AccessType'),
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'doUnlock': (
          ('_ZN23QPlatformGraphicsBuffer8doUnlockEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject *QPlatformGraphicsBuffer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformGraphicsBuffer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformGraphicsBuffer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isLocked(self) -> AccessTypes:
    """
    Calls Qt's 'AccessTypes QPlatformGraphicsBuffer::isLocked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#isLocked

    Returns
    -------

    AccessTypes
      The value standing for the combination Qt gave back.
    """
    #  AccessTypes QPlatformGraphicsBuffer::isLocked() const
    return QPlatformGraphicsBuffer.AccessTypes(self.uglySide.call(
        'ritual_ZNK23QPlatformGraphicsBuffer8isLockedEv',
    ))

  @overload()
  @overload(QRect)
  def bindToTexture(self, rect: Optional[QRect] = None) -> bool:
    """
    Calls Qt's 'bool QPlatformGraphicsBuffer::bindToTexture(const QRect
    &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#bindToTexture

    Parameters
    ----------

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  bool QPlatformGraphicsBuffer::bindToTexture(const QRect &rect) const
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    ritual = 'ritual_ZNK23QPlatformGraphicsBuffer13bindToTextureERK5QRect'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QPlatformGraphicsBuffer13bindToTextureERK5QRect')
    return self.uglySide.call(ritual, self._valueOf(rect))

  def bytesPerLine(self) -> int:
    """
    Calls Qt's 'int QPlatformGraphicsBuffer::bytesPerLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#bytesPerLine
    """
    #  int QPlatformGraphicsBuffer::bytesPerLine() const
    ritual = 'ritual_ZNK23QPlatformGraphicsBuffer12bytesPerLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QPlatformGraphicsBuffer12bytesPerLineEv'
    return self.uglySide.call(ritual)

  def byteCount(self) -> int:
    """
    Calls Qt's 'int QPlatformGraphicsBuffer::byteCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#byteCount
    """
    #  int QPlatformGraphicsBuffer::byteCount() const
    return self.uglySide.call(
        'ritual_ZNK23QPlatformGraphicsBuffer9byteCountEv',
    )

  def origin(self) -> Origin:
    """
    Calls Qt's 'Origin QPlatformGraphicsBuffer::origin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#origin

    Returns
    -------

    Origin
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Origin(number)' gives.
    """
    #  Origin QPlatformGraphicsBuffer::origin() const
    ritual = 'ritual_ZNK23QPlatformGraphicsBuffer6originEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QPlatformGraphicsBuffer6originEv'
    return QPlatformGraphicsBuffer.Origin(self.uglySide.call(ritual))

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QPlatformGraphicsBuffer::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPlatformGraphicsBuffer::size() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformGraphicsBuffer4sizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def format(self) -> QPixelFormat:
    """
    Calls Qt's 'QPixelFormat QPlatformGraphicsBuffer::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#format

    Returns
    -------

    QPixelFormat
      A new cute QPixelFormat around the copy Qt gave back. Python owns it.
    """
    #  QPixelFormat QPlatformGraphicsBuffer::format() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformGraphicsBuffer6formatEv',
    )
    from . import QPixelFormat
    return QPixelFormat._cuteOwning(address)

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

  @overload(QSize, QPixelFormat)
  def __init__(self, size: QSize, format: QPixelFormat) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformGraphicsBuffer::QPlatformGraphicsBuffer(const QSize &size,
    const QPixelFormat &format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    format : QPixelFormat
      Passed on as a value: Qt reads the C++ QPixelFormat, which stays
      Python's own.
    """
    #  QPlatformGraphicsBuffer::QPlatformGraphicsBuffer(const QSize &size,
    #      const QPixelFormat &format)
    self._noteCreation(QPlatformGraphicsBuffer, lambda: Rituals.call(
        'ritual_ZN23QPlatformGraphicsBufferC1ERK5QSizeRK12QPixelFormat',
        self._valueOf(size), self._valueOf(format),
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

  @overload(AccessTypes)
  @overload(AccessTypes, QRect)
  def lock(self, access: AccessTypes, rect: Optional[QRect] = None) -> bool:
    """
    Calls Qt's 'bool QPlatformGraphicsBuffer::lock(AccessTypes access, const
    QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#lock

    Parameters
    ----------

    access : AccessTypes
      Passed on as its number.

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  bool QPlatformGraphicsBuffer::lock(AccessTypes access, const QRect
    #      &rect)
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    return self.uglySide.call(
        'ritual_ZN23QPlatformGraphicsBuffer4lockE6QFlagsINS_10AccessTypeEER'
        'K5QRect',
        access.value, self._valueOf(rect),
    )

  def unlock(self) -> None:
    """
    Calls Qt's 'void QPlatformGraphicsBuffer::unlock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#unlock
    """
    #  void QPlatformGraphicsBuffer::unlock()
    self.uglySide.call('ritual_ZN23QPlatformGraphicsBuffer6unlockEv')

  @overload(AccessTypes)
  def unlocked(self, previousAccessTypes: AccessTypes) -> None:
    """
    Calls Qt's 'void QPlatformGraphicsBuffer::unlocked(AccessTypes
    previousAccessTypes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#unlocked

    Parameters
    ----------

    previousAccessTypes : AccessTypes
      Passed on as its number.
    """
    #  void QPlatformGraphicsBuffer::unlocked(AccessTypes
    #      previousAccessTypes)
    self.uglySide.call(
        'ritual_ZN23QPlatformGraphicsBuffer8unlockedE6QFlagsINS_10AccessTyp'
        'eEE',
        previousAccessTypes.value,
    )

  @overload(AccessTypes)
  @overload(AccessTypes, QRect)
  def doLock(
      self,
      access: AccessTypes,
      rect: Optional[QRect] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QPlatformGraphicsBuffer::doLock(AccessTypes access,
    const QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#doLock

    Parameters
    ----------

    access : AccessTypes
      Passed on as its number.

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  bool QPlatformGraphicsBuffer::doLock(AccessTypes access, const QRect
    #      &rect)
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    return self.uglySide.call(
        'ritual_ZN23QPlatformGraphicsBuffer6doLockE6QFlagsINS_10AccessTypeE'
        'ERK5QRect',
        access.value, self._valueOf(rect),
    )

  def doUnlock(self) -> None:
    """
    Calls Qt's 'void QPlatformGraphicsBuffer::doUnlock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformgraphicsbuffer.html#doUnlock
    """
    #  void QPlatformGraphicsBuffer::doUnlock()
    self.uglySide.call('ritual_ZN23QPlatformGraphicsBuffer8doUnlockEv')

  @staticmethod
  def data(*__, **_) -> Never:
    """
    - Qt's 'const uchar *QPlatformGraphicsBuffer::data() const': gives
      'unsigned char', which has no cute class yet.
    - Qt's 'uchar *QPlatformGraphicsBuffer::data()': takes or gives a type
      that cannot be passed yet: uchar *.
    """
    raise NotImplementedError(
        "'QPlatformGraphicsBuffer.data' has no cute function yet. Qt's "
        "'const uchar *QPlatformGraphicsBuffer::data() const': gives "
        "'unsigned char', which has no cute class yet. Qt's 'uchar "
        "*QPlatformGraphicsBuffer::data()': takes or gives a type that "
        "cannot be passed yet: uchar *.")
