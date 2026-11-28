"""
QQuickImageProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickimageprovider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQml import QQmlImageProviderBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QImage, QPixmap
  from . import QQuickTextureFactory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickImageProvider(QQmlImageProviderBase):
  """
  The cute side of Qt's QQuickImageProvider: a plain Python object standing
  in front of one C++ QQuickImageProvider.

  It is built on the cute 'QQmlImageProviderBase', as Qt's
  QQuickImageProvider is built on Qt's QQmlImageProviderBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImageProvider that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'imageType',
  'flags', 'requestImage', 'requestPixmap', 'requestTexture'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickImageProvider::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickImageProvider::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickImageProvider::~QQuickImageProvider()': the destructor:
    Python never removes a C++ QQuickImageProvider.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickImageProvider is created at the first use, not by
    'QQuickImageProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImageProvider.
  - Qt tells when it has removed the C++ QQuickImageProvider. Every call on
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
    Calls Qt's 'QString QQuickImageProvider::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageprovider.html#tr

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
    #  QString QQuickImageProvider::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickImageProvider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImageProvider'

  #  A C++ QQuickImageProvider Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImageProvider'

  #  The functions Qt calls itself that QQuickImageProvider is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'requestImage': (
          ('_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3_',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QSize'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'requestPixmap': (
          ('_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QSizeRKS3_',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QSize'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'requestTexture': (
          ('_ZN19QQuickImageProvider14requestTextureERK7QStringP5QSizeRKS3_',
           ('address', 'address', 'QtQuick:QQuickTextureFactory'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QSize'),
               ('address', 'value', 'QtCore:QSize'),
           )),
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
    Calls Qt's 'const QMetaObject *QQuickImageProvider::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickImageProvider::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickImageProvider10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def imageType(self) -> QQmlImageProviderBase.ImageType:
    """
    Calls Qt's 'ImageType QQuickImageProvider::imageType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageprovider.html#imageType

    Returns
    -------

    QQmlImageProviderBase.ImageType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlImageProviderBase.ImageType(number)' gives.
    """
    #  ImageType QQuickImageProvider::imageType() const
    ritual = 'ritual_ZNK19QQuickImageProvider9imageTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickImageProvider9imageTypeEv'
    return QQmlImageProviderBase.ImageType(self.uglySide.call(ritual))

  def flags(self) -> QQmlImageProviderBase.Flags:
    """
    Calls Qt's 'Flags QQuickImageProvider::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageprovider.html#flags

    Returns
    -------

    QQmlImageProviderBase.Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QQuickImageProvider::flags() const
    ritual = 'ritual_ZNK19QQuickImageProvider5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickImageProvider5flagsEv'
    return QQmlImageProviderBase.Flags(self.uglySide.call(ritual))

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

  @overload(QQmlImageProviderBase.ImageType)
  @overload(QQmlImageProviderBase.ImageType, QQmlImageProviderBase.Flags)
  def __init__(
      self,
      type: QQmlImageProviderBase.ImageType,
      flags: QQmlImageProviderBase.Flags = QQmlImageProviderBase.Flags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickImageProvider::QQuickImageProvider(ImageType type, Flags flags)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovider.html#QQuickImageProvider

    Parameters
    ----------

    type : QQmlImageProviderBase.ImageType
      Passed on as its number.

    flags : QQmlImageProviderBase.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlImageProviderBase.Flags().
    """
    #  QQuickImageProvider::QQuickImageProvider(ImageType type, Flags flags)
    self._noteCreation(QQuickImageProvider, lambda: Rituals.call(
        'ritual_ZN19QQuickImageProviderC1EN21QQmlImageProviderBase9ImageTyp'
        'eE6QFlagsINS0_4FlagEE',
        type.value, flags.value,
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

  @overload(str, QSize, QSize)
  @overload(str, NoneType, QSize)
  def requestImage(
      self,
      id: str,
      size: Optional[QSize],
      requestedSize: QSize,
  ) -> QImage:
    """
    Calls Qt's 'QImage QQuickImageProvider::requestImage(const QString &id,
    QSize *size, const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovider.html#requestImage

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    size : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickImageProvider::requestImage(const QString &id, QSize
    #      *size, const QSize &requestedSize)
    ritual = (
        'ritual_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3'
        '_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickImageProvider12requestImageERK7QStringP5QSi'
          'zeRKS3_')
    address = self.uglySide.call(
        ritual, id, self._addressOf(size), self._valueOf(requestedSize),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(str, QSize, QSize)
  @overload(str, NoneType, QSize)
  def requestPixmap(
      self,
      id: str,
      size: Optional[QSize],
      requestedSize: QSize,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QQuickImageProvider::requestPixmap(const QString &id,
    QSize *size, const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovider.html#requestPixmap

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    size : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QQuickImageProvider::requestPixmap(const QString &id, QSize
    #      *size, const QSize &requestedSize)
    ritual = (
        'ritual_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QSizeRKS'
        '3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QS'
          'izeRKS3_')
    address = self.uglySide.call(
        ritual, id, self._addressOf(size), self._valueOf(requestedSize),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(str, QSize, QSize)
  @overload(str, NoneType, QSize)
  def requestTexture(
      self,
      id: str,
      size: Optional[QSize],
      requestedSize: QSize,
  ) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory
    *QQuickImageProvider::requestTexture(const QString &id, QSize *size,
    const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovider.html#requestTexture

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    size : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory *QQuickImageProvider::requestTexture(const
    #      QString &id, QSize *size, const QSize &requestedSize)
    ritual = (
        'ritual_ZN19QQuickImageProvider14requestTextureERK7QStringP5QSizeRK'
        'S3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickImageProvider14requestTextureERK7QStringP5Q'
          'SizeRKS3_')
    address = self.uglySide.call(
        ritual, id, self._addressOf(size), self._valueOf(requestedSize),
    )
    from . import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)
