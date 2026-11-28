"""
QQuickImageProviderWithOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickImageProviderWithOptions to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQml import QQmlImageProviderBase
from . import QQuickAsyncImageProvider, QQuickImageProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QSize
  from ..QtGui import QImage, QPixmap
  from . import QQuickImageProviderOptions, QQuickImageResponse
  from . import QQuickTextureFactory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQuickImageProviderOptions = WAIT['QQuickImageProviderOptions']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickImageProviderWithOptions(QQuickAsyncImageProvider):
  """
  The cute side of Qt's QQuickImageProviderWithOptions: a plain Python object
  standing in front of one C++ QQuickImageProviderWithOptions.

  It is built on the cute 'QQuickAsyncImageProvider', as Qt's
  QQuickImageProviderWithOptions is built on Qt's QQuickAsyncImageProvider,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImageProviderWithOptions that has a ritual and
  that Python can call so far, 6 names in all: 'requestImage',
  'requestPixmap', 'requestTexture', 'requestImageResponse', 'loadSize',
  'checkedCast'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuickImageProviderWithOptions is created at the first use, not
    by 'QQuickImageProviderWithOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImageProviderWithOptions.
  - Qt tells when it has removed the C++ QQuickImageProviderWithOptions.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSize, QSize, QByteArray, QQuickImageProviderOptions)
  @overload(QSize, QSize, QByteArray, QQuickImageProviderOptions, float)
  def loadSize(
      originalSize: QSize,
      requestedSize: QSize,
      format: QByteArray,
      options: QQuickImageProviderOptions,
      devicePixelRatio: float = 1.0,
  ) -> QSize:
    """
    Calls Qt's 'QSize QQuickImageProviderWithOptions::loadSize(const QSize
    &originalSize, const QSize &requestedSize, const QByteArray &format,
    const QQuickImageProviderOptions &options, qreal devicePixelRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html#loadSize

    Parameters
    ----------

    originalSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    options : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.

    devicePixelRatio : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickImageProviderWithOptions::loadSize(const QSize
    #      &originalSize, const QSize &requestedSize, const QByteArray
    #      &format, const QQuickImageProviderOptions &options, qreal
    #      devicePixelRatio)
    address = Rituals.call(
        'ritual_ZN30QQuickImageProviderWithOptions8loadSizeERK5QSizeS2_RK10'
        'QByteArrayRK26QQuickImageProviderOptionsd',
        CuteMixin._valueOf(originalSize), CuteMixin._valueOf(requestedSize),
        CuteMixin._valueOf(format), CuteMixin._valueOf(options),
        devicePixelRatio,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @staticmethod
  @overload(QQuickImageProvider)
  @overload(NoneType)
  def checkedCast(
      provider: Optional[QQuickImageProvider],
  ) -> Optional[QQuickImageProviderWithOptions]:
    """
    Calls Qt's 'QQuickImageProviderWithOptions
    *QQuickImageProviderWithOptions::checkedCast(QQuickImageProvider
    *provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html#checkedCast

    Parameters
    ----------

    provider : Optional[QQuickImageProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickImageProviderWithOptions]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImageProviderWithOptions
    #      *QQuickImageProviderWithOptions::checkedCast(QQuickImageProvider
    #      *provider)
    address = Rituals.call(
        'ritual_ZN30QQuickImageProviderWithOptions11checkedCastEP19QQuickIm'
        'ageProvider',
        CuteMixin._addressOf(provider),
    )
    return QQuickImageProviderWithOptions._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImageProviderWithOptions'

  #  A C++ QQuickImageProviderWithOptions Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImageProviderWithOptions'

  #  The functions Qt calls itself that QQuickImageProviderWithOptions is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'requestImage': (
          ('_ZN30QQuickImageProviderWithOptions12requestImageERK7QStringP5Q'
           'SizeRKS3_RK26QQuickImageProviderOptions',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QSize'),
               ('address', 'value', 'QtCore:QSize'),
               ('address', 'value', 'QtQuick:QQuickImageProviderOptions'),
           )),
      ),
      'requestPixmap': (
          ('_ZN30QQuickImageProviderWithOptions13requestPixmapERK7QStringP5'
           'QSizeRKS3_RK26QQuickImageProviderOptions',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QSize'),
               ('address', 'value', 'QtCore:QSize'),
               ('address', 'value', 'QtQuick:QQuickImageProviderOptions'),
           )),
      ),
      'requestTexture': (
          ('_ZN30QQuickImageProviderWithOptions14requestTextureERK7QStringP'
           '5QSizeRKS3_RK26QQuickImageProviderOptions',
           ('address', 'address', 'QtQuick:QQuickTextureFactory'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QSize'),
               ('address', 'value', 'QtCore:QSize'),
               ('address', 'value', 'QtQuick:QQuickImageProviderOptions'),
           )),
      ),
      'requestImageResponse': (
          ('_ZN30QQuickImageProviderWithOptions20requestImageResponseERK7QS'
           'tringRK5QSizeRK26QQuickImageProviderOptions',
           ('address', 'address', 'QtQuick:QQuickImageResponse'),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QSize'),
               ('address', 'value', 'QtQuick:QQuickImageProviderOptions'),
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
    'QQuickImageProviderWithOptions::QQuickImageProviderWithOptions(ImageType
    type, Flags flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html

    Parameters
    ----------

    type : QQmlImageProviderBase.ImageType
      Passed on as its number.

    flags : QQmlImageProviderBase.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlImageProviderBase.Flags().
    """
    #  QQuickImageProviderWithOptions::QQuickImageProviderWithOptions(
    #      ImageType type, Flags flags)
    self._noteCreation(QQuickImageProviderWithOptions, lambda: Rituals.call(
        'ritual_ZN30QQuickImageProviderWithOptionsC1EN21QQmlImageProviderBa'
        'se9ImageTypeE6QFlagsINS0_4FlagEE',
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
    Calls Qt's 'QImage QQuickImageProviderWithOptions::requestImage(const
    QString &id, QSize *size, const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html#requestImage

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
    #  QImage QQuickImageProviderWithOptions::requestImage(const QString &id,
    #      QSize *size, const QSize &requestedSize)
    ritual = (
        'ritual_ZN30QQuickImageProviderWithOptions12requestImageERK7QString'
        'P5QSizeRKS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickImageProviderWithOptions12requestImageERK7Q'
          'StringP5QSizeRKS3_')
    address = self.uglySide.call(
        ritual, id, self._addressOf(size), self._valueOf(requestedSize),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(str, QSize, QSize, QQuickImageProviderOptions)
  @overload(str, NoneType, QSize, QQuickImageProviderOptions)
  def requestImage(
      self,
      id: str,
      size: Optional[QSize],
      requestedSize: QSize,
      options: QQuickImageProviderOptions,
  ) -> QImage:
    """
    Calls Qt's 'QImage QQuickImageProviderWithOptions::requestImage(const
    QString &id, QSize *size, const QSize &requestedSize, const
    QQuickImageProviderOptions &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html#requestImage

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    size : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickImageProviderWithOptions::requestImage(const QString &id,
    #      QSize *size, const QSize &requestedSize, const
    #      QQuickImageProviderOptions &options)
    ritual = (
        'ritual_ZN30QQuickImageProviderWithOptions12requestImageERK7QString'
        'P5QSizeRKS3_RK26QQuickImageProviderOptions')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickImageProviderWithOptions12requestImageERK7Q'
          'StringP5QSizeRKS3_RK26QQuickImageProviderOptions')
    address = self.uglySide.call(
        ritual,
        id, self._addressOf(size), self._valueOf(requestedSize),
        self._valueOf(options),
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
    Calls Qt's 'QPixmap QQuickImageProviderWithOptions::requestPixmap(const
    QString &id, QSize *size, const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html#requestPixmap

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
    #  QPixmap QQuickImageProviderWithOptions::requestPixmap(const QString
    #      &id, QSize *size, const QSize &requestedSize)
    ritual = (
        'ritual_ZN30QQuickImageProviderWithOptions13requestPixmapERK7QStrin'
        'gP5QSizeRKS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickImageProviderWithOptions13requestPixmapERK7'
          'QStringP5QSizeRKS3_')
    address = self.uglySide.call(
        ritual, id, self._addressOf(size), self._valueOf(requestedSize),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(str, QSize, QSize, QQuickImageProviderOptions)
  @overload(str, NoneType, QSize, QQuickImageProviderOptions)
  def requestPixmap(
      self,
      id: str,
      size: Optional[QSize],
      requestedSize: QSize,
      options: QQuickImageProviderOptions,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QQuickImageProviderWithOptions::requestPixmap(const
    QString &id, QSize *size, const QSize &requestedSize, const
    QQuickImageProviderOptions &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html#requestPixmap

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    size : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QQuickImageProviderWithOptions::requestPixmap(const QString
    #      &id, QSize *size, const QSize &requestedSize, const
    #      QQuickImageProviderOptions &options)
    ritual = (
        'ritual_ZN30QQuickImageProviderWithOptions13requestPixmapERK7QStrin'
        'gP5QSizeRKS3_RK26QQuickImageProviderOptions')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickImageProviderWithOptions13requestPixmapERK7'
          'QStringP5QSizeRKS3_RK26QQuickImageProviderOptions')
    address = self.uglySide.call(
        ritual,
        id, self._addressOf(size), self._valueOf(requestedSize),
        self._valueOf(options),
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
    *QQuickImageProviderWithOptions::requestTexture(const QString &id, QSize
    *size, const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html#requestTexture

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
    #  QQuickTextureFactory
    #      *QQuickImageProviderWithOptions::requestTexture(const QString &id,
    #      QSize *size, const QSize &requestedSize)
    ritual = (
        'ritual_ZN30QQuickImageProviderWithOptions14requestTextureERK7QStri'
        'ngP5QSizeRKS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickImageProviderWithOptions14requestTextureERK'
          '7QStringP5QSizeRKS3_')
    address = self.uglySide.call(
        ritual, id, self._addressOf(size), self._valueOf(requestedSize),
    )
    from . import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)

  @overload(str, QSize, QSize, QQuickImageProviderOptions)
  @overload(str, NoneType, QSize, QQuickImageProviderOptions)
  def requestTexture(
      self,
      id: str,
      size: Optional[QSize],
      requestedSize: QSize,
      options: QQuickImageProviderOptions,
  ) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory
    *QQuickImageProviderWithOptions::requestTexture(const QString &id, QSize
    *size, const QSize &requestedSize, const QQuickImageProviderOptions
    &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html#requestTexture

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    size : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory
    #      *QQuickImageProviderWithOptions::requestTexture(const QString &id,
    #      QSize *size, const QSize &requestedSize, const
    #      QQuickImageProviderOptions &options)
    ritual = (
        'ritual_ZN30QQuickImageProviderWithOptions14requestTextureERK7QStri'
        'ngP5QSizeRKS3_RK26QQuickImageProviderOptions')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickImageProviderWithOptions14requestTextureERK'
          '7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions')
    address = self.uglySide.call(
        ritual,
        id, self._addressOf(size), self._valueOf(requestedSize),
        self._valueOf(options),
    )
    from . import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)

  @overload(str, QSize)
  def requestImageResponse(
      self,
      id: str,
      requestedSize: QSize,
  ) -> Optional[QQuickImageResponse]:
    """
    Calls Qt's 'QQuickImageResponse
    *QQuickImageProviderWithOptions::requestImageResponse(const QString &id,
    const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    Optional[QQuickImageResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImageResponse
    #      *QQuickImageProviderWithOptions::requestImageResponse(const
    #      QString &id, const QSize &requestedSize)
    ritual = (
        'ritual_ZN30QQuickImageProviderWithOptions20requestImageResponseERK'
        '7QStringRK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickImageProviderWithOptions20requestImageRespo'
          'nseERK7QStringRK5QSize')
    address = self.uglySide.call(ritual, id, self._valueOf(requestedSize))
    from . import QQuickImageResponse
    return QQuickImageResponse._cuteAt(address)

  @overload(str, QSize, QQuickImageProviderOptions)
  def requestImageResponse(
      self,
      id: str,
      requestedSize: QSize,
      options: QQuickImageProviderOptions,
  ) -> Optional[QQuickImageResponse]:
    """
    Calls Qt's 'QQuickImageResponse
    *QQuickImageProviderWithOptions::requestImageResponse(const QString &id,
    const QSize &requestedSize, const QQuickImageProviderOptions &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageproviderwithoptions.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.

    Returns
    -------

    Optional[QQuickImageResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImageResponse
    #      *QQuickImageProviderWithOptions::requestImageResponse(const
    #      QString &id, const QSize &requestedSize, const
    #      QQuickImageProviderOptions &options)
    ritual = (
        'ritual_ZN30QQuickImageProviderWithOptions20requestImageResponseERK'
        '7QStringRK5QSizeRK26QQuickImageProviderOptions')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickImageProviderWithOptions20requestImageRespo'
          'nseERK7QStringRK5QSizeRK26QQuickImageProviderOptions')
    address = self.uglySide.call(
        ritual, id, self._valueOf(requestedSize), self._valueOf(options),
    )
    from . import QQuickImageResponse
    return QQuickImageResponse._cuteAt(address)
