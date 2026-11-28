"""
FaviconImageResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means FaviconImageResponse to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QQuickImageResponse

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize, QUrl
  from ..QtGui import QPixmap
  from ..QtQuick import QQuickTextureFactory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPixmap = WAIT['QPixmap']


class FaviconImageResponse(QQuickImageResponse):
  """
  The cute side of Qt's FaviconImageResponse: a plain Python object standing
  in front of one C++ FaviconImageResponse.

  It is built on the cute 'QQuickImageResponse', as Qt's FaviconImageResponse
  is built on Qt's QQuickImageResponse, and has everything that class has.

  What exists
  -----------

  Every function of Qt's FaviconImageResponse that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'textureFactory',
  'imageSource', 'requestedSize', 'isIconUrl', 'handleDone'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *FaviconImageResponse::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int FaviconImageResponse::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 1 leans on
  'FaviconImageResponse; 1 leans on 'vtable for FaviconImageResponse', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ FaviconImageResponse is created at the first use, not by
    'FaviconImageResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ FaviconImageResponse.
  - Qt tells when it has removed the C++ FaviconImageResponse. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's FaviconImageResponse that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'FaviconImageResponse'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *FaviconImageResponse::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconimageresponse.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *FaviconImageResponse::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20FaviconImageResponse10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureFactory(self) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory *FaviconImageResponse::textureFactory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconimageresponse.html#textureFactory

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory *FaviconImageResponse::textureFactory() const
    ritual = 'ritual_ZNK20FaviconImageResponse14textureFactoryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20FaviconImageResponse14textureFactoryEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)

  def imageSource(self) -> QUrl:
    """
    Calls Qt's 'const QUrl &FaviconImageResponse::imageSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconimageresponse.html#imageSource

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  const QUrl &FaviconImageResponse::imageSource() const
    address = self.uglySide.call(
        'ritual_ZNK20FaviconImageResponse11imageSourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def requestedSize(self) -> QSize:
    """
    Calls Qt's 'const QSize &FaviconImageResponse::requestedSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconimageresponse.html#requestedSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  const QSize &FaviconImageResponse::requestedSize() const
    address = self.uglySide.call(
        'ritual_ZNK20FaviconImageResponse13requestedSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isIconUrl(self) -> bool:
    """
    Calls Qt's 'bool FaviconImageResponse::isIconUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconimageresponse.html#isIconUrl
    """
    #  bool FaviconImageResponse::isIconUrl() const
    return self.uglySide.call('ritual_ZNK20FaviconImageResponse9isIconUrlEv')

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
    Qt's 'FaviconImageResponse::FaviconImageResponse(const QUrl &imageSource,
    const QSize &requestedSize, bool isIconUrl)': leans on 'vtable for
    FaviconImageResponse', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'FaviconImageResponse.__init__' has no cute function yet. Qt's "
        "'FaviconImageResponse::FaviconImageResponse(const QUrl "
        "&imageSource, const QSize &requestedSize, bool isIconUrl)': leans "
        "on 'vtable for FaviconImageResponse', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QPixmap)
  def handleDone(self, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void FaviconImageResponse::handleDone(QPixmap pixmap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconimageresponse.html#handleDone

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void FaviconImageResponse::handleDone(QPixmap pixmap)
    self.uglySide.call(
        'ritual_ZN20FaviconImageResponse10handleDoneE7QPixmap',
        self._valueOf(pixmap),
    )
