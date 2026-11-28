"""
QCameraDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qcameradevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QtVideo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QSize
  from . import QCameraDevicePrivate, QCameraFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCameraDevicePrivate = WAIT['QCameraDevicePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCameraDevice(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCameraDevice: a plain Python object standing in
  front of one C++ QCameraDevice.

  C++ hands a QCameraDevice around as a copy, so every C++ QCameraDevice
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCameraDevice that has a ritual and that Python can
  call so far, 10 names in all: '__eq__', '__ne__', 'isNull', 'id',
  'description', 'isDefault', 'position', 'photoResolutions', 'videoFormats',
  'correctionAngle'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCameraDevice &QCameraDevice::operator=(const QCameraDevice
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QCameraDevice::~QCameraDevice()': the destructor: Python removes
    its C++ QCameraDevice by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QCameraDevice is created at the first use, not by
    'QCameraDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCameraDevice back gives a copy the ritual made for
    Python, in a new cute QCameraDevice.
  """

  #  The enums Qt writes inside QCameraDevice, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Position(CuteNum):
    """
    The enum 'QCameraDevice::Position' of Qt, with the 3 names Qt gives in
    it.
    """

    UnspecifiedPosition = Kee[int](0)
    BackFace = Kee[int](1)
    FrontFace = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCameraDevice'

  #  Qt's '~QCameraDevice()'. Naming it makes this a value class: Python owns
  #  every C++ QCameraDevice behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QCameraDeviceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCameraDevice::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#isNull
    """
    #  bool QCameraDevice::isNull() const
    return self.uglySide.call('ritual_ZNK13QCameraDevice6isNullEv')

  def id(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCameraDevice::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#id

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCameraDevice::id() const
    address = self.uglySide.call('ritual_ZNK13QCameraDevice2idEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def description(self) -> str:
    """
    Calls Qt's 'QString QCameraDevice::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCameraDevice::description() const
    return self.uglySide.call('ritual_ZNK13QCameraDevice11descriptionEv')

  def isDefault(self) -> bool:
    """
    Calls Qt's 'bool QCameraDevice::isDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#isDefault
    """
    #  bool QCameraDevice::isDefault() const
    return self.uglySide.call('ritual_ZNK13QCameraDevice9isDefaultEv')

  def position(self) -> Position:
    """
    Calls Qt's 'Position QCameraDevice::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#position

    Returns
    -------

    Position
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Position(number)' gives.
    """
    #  Position QCameraDevice::position() const
    return QCameraDevice.Position(self.uglySide.call(
        'ritual_ZNK13QCameraDevice8positionEv',
    ))

  def photoResolutions(self) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QCameraDevice::photoResolutions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcameradevice.html#photoResolutions

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QCameraDevice::photoResolutions() const
    address = self.uglySide.call(
        'ritual_ZNK13QCameraDevice16photoResolutionsEv',
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  def videoFormats(self) -> QList[QCameraFormat]:
    """
    Calls Qt's 'QList<QCameraFormat> QCameraDevice::videoFormats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#videoFormats

    Returns
    -------

    QList[QCameraFormat]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCameraFormat> QCameraDevice::videoFormats() const
    address = self.uglySide.call('ritual_ZNK13QCameraDevice12videoFormatsEv')
    from . import QCameraFormat
    return QList[QCameraFormat]._cuteOwning(address)

  def correctionAngle(self) -> QtVideo.Rotation:
    """
    Calls Qt's 'QtVideo::Rotation QCameraDevice::correctionAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#correctionAngle

    Returns
    -------

    QtVideo.Rotation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtVideo.Rotation(number)'
      gives.
    """
    #  QtVideo::Rotation QCameraDevice::correctionAngle() const
    return QtVideo.Rotation(self.uglySide.call(
        'ritual_ZNK13QCameraDevice15correctionAngleEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QCameraDevice) -> bool:
    """
    Calls Qt's 'bool QCameraDevice::operator==(const QCameraDevice &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#operator==

    Parameters
    ----------

    other : QCameraDevice
      Passed on as a value: Qt reads the C++ QCameraDevice, which stays
      Python's own.
    """
    #  bool QCameraDevice::operator==(const QCameraDevice &other) const
    return self.uglySide.call(
        'ritual_ZNK13QCameraDeviceeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QCameraDevice) -> bool:
    """
    Calls Qt's 'bool QCameraDevice::operator!=(const QCameraDevice &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#operator!=

    Parameters
    ----------

    other : QCameraDevice
      Passed on as a value: Qt reads the C++ QCameraDevice, which stays
      Python's own.
    """
    #  bool QCameraDevice::operator!=(const QCameraDevice &other) const
    return self.uglySide.call(
        'ritual_ZNK13QCameraDeviceneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCameraDevice::QCameraDevice()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#QCameraDevice
    """
    #  QCameraDevice::QCameraDevice()
    self._noteCreation(QCameraDevice, lambda: Rituals.call(
        'ritual_ZN13QCameraDeviceC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCameraDevice) -> None:
    """
    Notes what was given, for Qt's 'QCameraDevice::QCameraDevice(const
    QCameraDevice &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#QCameraDevice

    Parameters
    ----------

    other : QCameraDevice
      Passed on as a value: Qt reads the C++ QCameraDevice, which stays
      Python's own.
    """
    #  QCameraDevice::QCameraDevice(const QCameraDevice &other)
    self._noteCreation(QCameraDevice, lambda: Rituals.call(
        'ritual_ZN13QCameraDeviceC1ERKS_', self._valueOf(other),
    ))

  @overload(QCameraDevicePrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QCameraDevicePrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QCameraDevice::QCameraDevice(QCameraDevicePrivate *p)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcameradevice.html#QCameraDevice

    Parameters
    ----------

    p : Optional[QCameraDevicePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCameraDevice::QCameraDevice(QCameraDevicePrivate *p)
    self._noteCreation(QCameraDevice, lambda: Rituals.call(
        'ritual_ZN13QCameraDeviceC1EP20QCameraDevicePrivate',
        self._addressOf(p),
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


#  Qt's 'QList<QCameraDevice>': the list of QCameraDevice, which
#  'QList[QCameraDevice]' gives. It is made here, so that there is one as
#  soon as there can be a QCameraDevice.
QList.createKind(
    QCameraDevice, 'value',
    make='ritual_list_make_QCameraDevice',
    add='ritual_list_add_QCameraDevice',
    size='ritual_list_size_QCameraDevice',
    at='ritual_list_at_QCameraDevice',
    drop='ritual_list_drop_QCameraDevice',
)
