"""
QQuickWebEngineTouchHandleProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginetouchhandleprovider_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineTouchHandleProvider to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QMap
from ..QtQuick import QQuickImageProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize, QUrl
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineTouchHandleProvider(QQuickImageProvider):
  """
  The cute side of Qt's QQuickWebEngineTouchHandleProvider: a plain Python
  object standing in front of one C++ QQuickWebEngineTouchHandleProvider.

  It is built on the cute 'QQuickImageProvider', as Qt's
  QQuickWebEngineTouchHandleProvider is built on Qt's QQuickImageProvider,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineTouchHandleProvider that has a ritual
  and that Python can call so far, 4 names in all: 'identifier', 'url',
  'init', 'requestImage'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QQuickWebEngineTouchHandleProvider::~QQuickWebEngineTouchHandleProvider(
    )': the destructor: Python never removes a C++
    QQuickWebEngineTouchHandleProvider.

  What to expect
  --------------

  - The C++ QQuickWebEngineTouchHandleProvider is created at the first use,
    not by 'QQuickWebEngineTouchHandleProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineTouchHandleProvider.
  - Qt tells when it has removed the C++ QQuickWebEngineTouchHandleProvider.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def identifier() -> str:
    """
    Calls Qt's 'QString QQuickWebEngineTouchHandleProvider::identifier()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchhandleprovider.html#identifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineTouchHandleProvider::identifier()
    return Rituals.call(
        'ritual_ZN34QQuickWebEngineTouchHandleProvider10identifierEv',
    )

  @staticmethod
  @overload(int)
  def url(orientation: int) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWebEngineTouchHandleProvider::url(int
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchhandleprovider.html#url

    Parameters
    ----------

    orientation : int
      Passed on as it is.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebEngineTouchHandleProvider::url(int orientation)
    address = Rituals.call(
        'ritual_ZN34QQuickWebEngineTouchHandleProvider3urlEi', orientation,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineTouchHandleProvider'

  #  A C++ QQuickWebEngineTouchHandleProvider Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineTouchHandleProvider'

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
    'QQuickWebEngineTouchHandleProvider::QQuickWebEngineTouchHandleProvider(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchhandleprovider.html
    """
    #  QQuickWebEngineTouchHandleProvider::
    #      QQuickWebEngineTouchHandleProvider()
    self._noteCreation(
        QQuickWebEngineTouchHandleProvider, lambda: Rituals.call(
            'ritual_ZN34QQuickWebEngineTouchHandleProviderC1Ev',
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

  @overload(QMap[int, QImage])
  def init(self, images: QMap[int, QImage]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineTouchHandleProvider::init(const QMap<int,
    QImage> &images)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchhandleprovider.html#init

    Parameters
    ----------

    images : QMap[int, QImage]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickWebEngineTouchHandleProvider::init(const QMap<int, QImage>
    #      &images)
    self.uglySide.call(
        'ritual_ZN34QQuickWebEngineTouchHandleProvider4initERK4QMapIi6QImag'
        'eE',
        self._valueOf(images),
    )

  @overload(str, QSize, QSize)
  @overload(str, NoneType, QSize)
  def requestImage(
      self,
      id: str,
      size: Optional[QSize],
      requestedSize: QSize,
  ) -> QImage:
    """
    Calls Qt's 'QImage QQuickWebEngineTouchHandleProvider::requestImage(const
    QString &id, QSize *size, const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchhandleprovider.html

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
    #  QImage QQuickWebEngineTouchHandleProvider::requestImage(const QString
    #      &id, QSize *size, const QSize &requestedSize)
    ritual = (
        'ritual_ZN34QQuickWebEngineTouchHandleProvider12requestImageERK7QSt'
        'ringP5QSizeRKS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QQuickWebEngineTouchHandleProvider12requestImageE'
          'RK7QStringP5QSizeRKS3_')
    address = self.uglySide.call(
        ritual, id, self._addressOf(size), self._valueOf(requestedSize),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)
