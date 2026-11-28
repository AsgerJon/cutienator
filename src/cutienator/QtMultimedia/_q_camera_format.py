"""
QCameraFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qcameradevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QVideoFrameFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDebug, QSize
  from . import QCameraFormatPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCameraFormatPrivate = WAIT['QCameraFormatPrivate']
  QDebug = WAIT['QDebug']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCameraFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCameraFormat: a plain Python object standing in
  front of one C++ QCameraFormat.

  C++ hands a QCameraFormat around as a copy, so every C++ QCameraFormat
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCameraFormat that has a ritual and that Python can
  call so far, 8 names in all: 'pixelFormat', 'resolution', 'minFrameRate',
  'maxFrameRate', 'isNull', '__eq__', '__ne__', '__rlshift__'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCameraFormat &QCameraFormat::operator=(const QCameraFormat
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QCameraFormat::~QCameraFormat()': the destructor: Python removes
    its C++ QCameraFormat by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QCameraFormat is created at the first use, not by
    'QCameraFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCameraFormat back gives a copy the ritual made for
    Python, in a new cute QCameraFormat.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCameraFormat'

  #  Qt's '~QCameraFormat()'. Naming it makes this a value class: Python owns
  #  every C++ QCameraFormat behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QCameraFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixelFormat(self) -> QVideoFrameFormat.PixelFormat:
    """
    Calls Qt's 'QVideoFrameFormat::PixelFormat QCameraFormat::pixelFormat()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#pixelFormat

    Returns
    -------

    QVideoFrameFormat.PixelFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QVideoFrameFormat.PixelFormat(number)' gives.
    """
    #  QVideoFrameFormat::PixelFormat QCameraFormat::pixelFormat() const
    return QVideoFrameFormat.PixelFormat(self.uglySide.call(
        'ritual_ZNK13QCameraFormat11pixelFormatEv',
    ))

  def resolution(self) -> QSize:
    """
    Calls Qt's 'QSize QCameraFormat::resolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#resolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCameraFormat::resolution() const
    address = self.uglySide.call('ritual_ZNK13QCameraFormat10resolutionEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minFrameRate(self) -> float:
    """
    Calls Qt's 'float QCameraFormat::minFrameRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#minFrameRate
    """
    #  float QCameraFormat::minFrameRate() const
    return self.uglySide.call('ritual_ZNK13QCameraFormat12minFrameRateEv')

  def maxFrameRate(self) -> float:
    """
    Calls Qt's 'float QCameraFormat::maxFrameRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#maxFrameRate
    """
    #  float QCameraFormat::maxFrameRate() const
    return self.uglySide.call('ritual_ZNK13QCameraFormat12maxFrameRateEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCameraFormat::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#isNull
    """
    #  bool QCameraFormat::isNull() const
    return self.uglySide.call('ritual_ZNK13QCameraFormat6isNullEv')

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
  def __eq__(self, other: QCameraFormat) -> bool:
    """
    Calls Qt's 'bool QCameraFormat::operator==(const QCameraFormat &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#operator==

    Parameters
    ----------

    other : QCameraFormat
      Passed on as a value: Qt reads the C++ QCameraFormat, which stays
      Python's own.
    """
    #  bool QCameraFormat::operator==(const QCameraFormat &other) const
    return self.uglySide.call(
        'ritual_ZNK13QCameraFormateqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QCameraFormat) -> bool:
    """
    Calls Qt's 'bool QCameraFormat::operator!=(const QCameraFormat &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#operator!=

    Parameters
    ----------

    other : QCameraFormat
      Passed on as a value: Qt reads the C++ QCameraFormat, which stays
      Python's own.
    """
    #  bool QCameraFormat::operator!=(const QCameraFormat &other) const
    return self.uglySide.call(
        'ritual_ZNK13QCameraFormatneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QCameraFormat &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QCameraFormat &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK13QCameraFormat',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QCameraFormat::QCameraFormat()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#QCameraFormat
    """
    #  QCameraFormat::QCameraFormat()
    self._noteCreation(QCameraFormat, lambda: Rituals.call(
        'ritual_ZN13QCameraFormatC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCameraFormat) -> None:
    """
    Notes what was given, for Qt's 'QCameraFormat::QCameraFormat(const
    QCameraFormat &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#QCameraFormat

    Parameters
    ----------

    other : QCameraFormat
      Passed on as a value: Qt reads the C++ QCameraFormat, which stays
      Python's own.
    """
    #  QCameraFormat::QCameraFormat(const QCameraFormat &other)
    self._noteCreation(QCameraFormat, lambda: Rituals.call(
        'ritual_ZN13QCameraFormatC1ERKS_', self._valueOf(other),
    ))

  @overload(QCameraFormatPrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QCameraFormatPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QCameraFormat::QCameraFormat(QCameraFormatPrivate *p)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformat.html#QCameraFormat

    Parameters
    ----------

    p : Optional[QCameraFormatPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCameraFormat::QCameraFormat(QCameraFormatPrivate *p)
    self._noteCreation(QCameraFormat, lambda: Rituals.call(
        'ritual_ZN13QCameraFormatC1EP20QCameraFormatPrivate',
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


#  Qt's 'QList<QCameraFormat>': the list of QCameraFormat, which
#  'QList[QCameraFormat]' gives. It is made here, so that there is one as
#  soon as there can be a QCameraFormat.
QList.createKind(
    QCameraFormat, 'value',
    make='ritual_list_make_QCameraFormat',
    add='ritual_list_add_QCameraFormat',
    size='ritual_list_size_QCameraFormat',
    at='ritual_list_at_QCameraFormat',
    drop='ritual_list_drop_QCameraFormat',
)
