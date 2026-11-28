"""
QRhiTextureSubresourceUploadDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray, QPoint, QSize
  from . import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QImage = WAIT['QImage']
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']


class QRhiTextureSubresourceUploadDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiTextureSubresourceUploadDescription: a plain
  Python object standing in front of one C++
  QRhiTextureSubresourceUploadDescription.

  C++ hands a QRhiTextureSubresourceUploadDescription around as a copy, so
  every C++ QRhiTextureSubresourceUploadDescription behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiTextureSubresourceUploadDescription that has a
  ritual and that Python can call so far, 12 names in all: 'image',
  'setImage', 'data', 'setData', 'dataStride', 'setDataStride',
  'destinationTopLeft', 'setDestinationTopLeft', 'sourceSize',
  'setSourceSize', 'sourceTopLeft', 'setSourceTopLeft'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiTextureSubresourceUploadDescription::
    QRhiTextureSubresourceUploadDescription(const void *data, quint32 size)':
    names 'void', which has no cute class yet.
  - Qt's 'QRhiTextureSubresourceUploadDescription::
    ~QRhiTextureSubresourceUploadDescription()': the destructor: Python
    removes its C++ QRhiTextureSubresourceUploadDescription by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ QRhiTextureSubresourceUploadDescription is created at the first
    use, not by 'QRhiTextureSubresourceUploadDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiTextureSubresourceUploadDescription back gives a
    copy the ritual made for Python, in a new cute
    QRhiTextureSubresourceUploadDescription.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiTextureSubresourceUploadDescription'

  #  Qt's '~QRhiTextureSubresourceUploadDescription()'. Naming it makes this
  #  a value class: Python owns every C++
  #  QRhiTextureSubresourceUploadDescription behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN39QRhiTextureSubresourceUploadDescriptionD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage QRhiTextureSubresourceUploadDescription::image()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QRhiTextureSubresourceUploadDescription::image() const
    address = self.uglySide.call(
        'ritual_ZNK39QRhiTextureSubresourceUploadDescription5imageEv',
    )
    from . import QImage
    return QImage._cuteOwning(address)

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRhiTextureSubresourceUploadDescription::data()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRhiTextureSubresourceUploadDescription::data() const
    address = self.uglySide.call(
        'ritual_ZNK39QRhiTextureSubresourceUploadDescription4dataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def dataStride(self) -> int:
    """
    Calls Qt's 'quint32 QRhiTextureSubresourceUploadDescription::dataStride()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html
    """
    #  quint32 QRhiTextureSubresourceUploadDescription::dataStride() const
    return self.uglySide.call(
        'ritual_ZNK39QRhiTextureSubresourceUploadDescription10dataStrideEv',
    )

  def destinationTopLeft(self) -> QPoint:
    """
    Calls Qt's 'QPoint
    QRhiTextureSubresourceUploadDescription::destinationTopLeft() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRhiTextureSubresourceUploadDescription::destinationTopLeft()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK39QRhiTextureSubresourceUploadDescription18destinationTo'
        'pLeftEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def sourceSize(self) -> QSize:
    """
    Calls Qt's 'QSize QRhiTextureSubresourceUploadDescription::sourceSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiTextureSubresourceUploadDescription::sourceSize() const
    address = self.uglySide.call(
        'ritual_ZNK39QRhiTextureSubresourceUploadDescription10sourceSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sourceTopLeft(self) -> QPoint:
    """
    Calls Qt's 'QPoint
    QRhiTextureSubresourceUploadDescription::sourceTopLeft() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRhiTextureSubresourceUploadDescription::sourceTopLeft() const
    address = self.uglySide.call(
        'ritual_ZNK39QRhiTextureSubresourceUploadDescription13sourceTopLeft'
        'Ev',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QImage)
  def setImage(self, image: QImage) -> None:
    """
    Calls Qt's 'void QRhiTextureSubresourceUploadDescription::setImage(const
    QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QRhiTextureSubresourceUploadDescription::setImage(const QImage
    #      &image)
    self.uglySide.call(
        'ritual_ZN39QRhiTextureSubresourceUploadDescription8setImageERK6QIm'
        'age',
        self._valueOf(image),
    )

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiTextureSubresourceUploadDescription::setData(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiTextureSubresourceUploadDescription::setData(const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN39QRhiTextureSubresourceUploadDescription7setDataERK10QBy'
        'teArray',
        self._valueOf(data),
    )

  @overload(int)
  def setDataStride(self, stride: int) -> None:
    """
    Calls Qt's 'void
    QRhiTextureSubresourceUploadDescription::setDataStride(quint32 stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Parameters
    ----------

    stride : int
      Passed on as it is.
    """
    #  void QRhiTextureSubresourceUploadDescription::setDataStride(quint32
    #      stride)
    self.uglySide.call(
        'ritual_ZN39QRhiTextureSubresourceUploadDescription13setDataStrideE'
        'j',
        stride,
    )

  @overload(QPoint)
  def setDestinationTopLeft(self, p: QPoint) -> None:
    """
    Calls Qt's 'void
    QRhiTextureSubresourceUploadDescription::setDestinationTopLeft(const
    QPoint &p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRhiTextureSubresourceUploadDescription::setDestinationTopLeft(
    #      const QPoint &p)
    self.uglySide.call(
        'ritual_ZN39QRhiTextureSubresourceUploadDescription21setDestination'
        'TopLeftERK6QPoint',
        self._valueOf(p),
    )

  @overload(QSize)
  def setSourceSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void
    QRhiTextureSubresourceUploadDescription::setSourceSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiTextureSubresourceUploadDescription::setSourceSize(const
    #      QSize &size)
    self.uglySide.call(
        'ritual_ZN39QRhiTextureSubresourceUploadDescription13setSourceSizeE'
        'RK5QSize',
        self._valueOf(size),
    )

  @overload(QPoint)
  def setSourceTopLeft(self, p: QPoint) -> None:
    """
    Calls Qt's 'void
    QRhiTextureSubresourceUploadDescription::setSourceTopLeft(const QPoint
    &p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRhiTextureSubresourceUploadDescription::setSourceTopLeft(const
    #      QPoint &p)
    self.uglySide.call(
        'ritual_ZN39QRhiTextureSubresourceUploadDescription16setSourceTopLe'
        'ftERK6QPoint',
        self._valueOf(p),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QRhiTextureSubresourceUploadDescription::
    QRhiTextureSubresourceUploadDescription()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html
    """
    #  QRhiTextureSubresourceUploadDescription::
    #      QRhiTextureSubresourceUploadDescription()
    self._noteCreation(
        QRhiTextureSubresourceUploadDescription, lambda: Rituals.call(
            'ritual_ZN39QRhiTextureSubresourceUploadDescriptionC1Ev',
        ))

  @overload(QImage)
  def __init__(self, image: QImage) -> None:
    """
    Notes what was given, for Qt's 'QRhiTextureSubresourceUploadDescription::
    QRhiTextureSubresourceUploadDescription(const QImage &image)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  QRhiTextureSubresourceUploadDescription::
    #      QRhiTextureSubresourceUploadDescription(const QImage &image)
    self._noteCreation(
        QRhiTextureSubresourceUploadDescription, lambda: Rituals.call(
            'ritual_ZN39QRhiTextureSubresourceUploadDescriptionC1ERK6QImage',
            self._valueOf(image),
        ))

  @overload(QByteArray)
  def __init__(self, data: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QRhiTextureSubresourceUploadDescription::
    QRhiTextureSubresourceUploadDescription(const QByteArray &data)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturesubresourceuploaddescription.html

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QRhiTextureSubresourceUploadDescription::
    #      QRhiTextureSubresourceUploadDescription(const QByteArray &data)
    self._noteCreation(
        QRhiTextureSubresourceUploadDescription, lambda: Rituals.call(
            'ritual_ZN39QRhiTextureSubresourceUploadDescriptionC1ERK10QByte'
            'Array',
            self._valueOf(data),
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
