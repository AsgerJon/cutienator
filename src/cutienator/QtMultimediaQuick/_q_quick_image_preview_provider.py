"""
QQuickImagePreviewProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickimagepreviewprovider_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickImagePreviewProvider to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickImageProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize, QUuid
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QSize = WAIT['QSize']
  QUuid = WAIT['QUuid']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickImagePreviewProvider(QQuickImageProvider):
  """
  The cute side of Qt's QQuickImagePreviewProvider: a plain Python object
  standing in front of one C++ QQuickImagePreviewProvider.

  It is built on the cute 'QQuickImageProvider', as Qt's
  QQuickImagePreviewProvider is built on Qt's QQuickImageProvider, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImagePreviewProvider that has a ritual and
  that Python can call so far, 3 names in all: 'requestImage',
  'registerPreview', 'cleanupInstance'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickImagePreviewProvider::~QQuickImagePreviewProvider()': the
    destructor: Python never removes a C++ QQuickImagePreviewProvider.

  What to expect
  --------------

  - The C++ QQuickImagePreviewProvider is created at the first use, not by
    'QQuickImagePreviewProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImagePreviewProvider.
  - Qt tells when it has removed the C++ QQuickImagePreviewProvider. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QUuid, str, QImage)
  def registerPreview(captureInstance: QUuid, id: str, a2: QImage) -> None:
    """
    Calls Qt's 'void QQuickImagePreviewProvider::registerPreview(QUuid
    captureInstance, QString id, QImage a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagepreviewprovider.html#registerPreview

    Parameters
    ----------

    captureInstance : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.

    id : str
      Passed on as it is: a QString is made of it for the call.

    a2 : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QQuickImagePreviewProvider::registerPreview(QUuid
    #      captureInstance, QString id, QImage a2)
    Rituals.call(
        'ritual_ZN26QQuickImagePreviewProvider15registerPreviewE5QUuid7QStr'
        'ing6QImage',
        CuteMixin._valueOf(captureInstance), id, CuteMixin._valueOf(a2),
    )

  @staticmethod
  @overload(QUuid)
  def cleanupInstance(captureInstance: QUuid) -> None:
    """
    Calls Qt's 'void QQuickImagePreviewProvider::cleanupInstance(QUuid
    captureInstance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagepreviewprovider.html#cleanupInstance

    Parameters
    ----------

    captureInstance : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.
    """
    #  void QQuickImagePreviewProvider::cleanupInstance(QUuid
    #      captureInstance)
    Rituals.call(
        'ritual_ZN26QQuickImagePreviewProvider15cleanupInstanceE5QUuid',
        CuteMixin._valueOf(captureInstance),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImagePreviewProvider'

  #  A C++ QQuickImagePreviewProvider Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImagePreviewProvider'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickImagePreviewProvider::QQuickImagePreviewProvider()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagepreviewprovider.html
    """
    #  QQuickImagePreviewProvider::QQuickImagePreviewProvider()
    self._noteCreation(QQuickImagePreviewProvider, lambda: Rituals.call(
        'ritual_ZN26QQuickImagePreviewProviderC1Ev',
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
    Calls Qt's 'QImage QQuickImagePreviewProvider::requestImage(const QString
    &id, QSize *size, const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagepreviewprovider.html#requestImage

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
    #  QImage QQuickImagePreviewProvider::requestImage(const QString &id,
    #      QSize *size, const QSize &requestedSize)
    ritual = (
        'ritual_ZN26QQuickImagePreviewProvider12requestImageERK7QStringP5QS'
        'izeRKS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickImagePreviewProvider12requestImageERK7QStri'
          'ngP5QSizeRKS3_')
    address = self.uglySide.call(
        ritual, id, self._addressOf(size), self._valueOf(requestedSize),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)
