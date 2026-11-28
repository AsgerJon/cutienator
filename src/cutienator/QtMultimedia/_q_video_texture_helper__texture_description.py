"""
QVideoTextureHelper::TextureDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideotexturehelper_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QVideoTextureHelper::TextureDescription to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..QtGui import QRhiTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from ..QtGui import QRhi
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TextureDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVideoTextureHelper::TextureDescription: a plain
  Python object standing in front of one C++
  QVideoTextureHelper::TextureDescription.

  C++ hands a QVideoTextureHelper::TextureDescription around as a copy, so
  every C++ QVideoTextureHelper::TextureDescription behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVideoTextureHelper::TextureDescription that has a
  ritual and that Python can call so far, 8 names in all: 'rhiTextureFormat',
  'strideForWidth', 'bytesForSize', 'widthForPlane', 'heightForPlane',
  'rhiSizeScale', 'rhiPlaneSize', 'hasTextureFormat'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoTextureHelper::TextureDescription::~TextureDescription()':
    the destructor: Python removes its C++
    QVideoTextureHelper::TextureDescription by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QVideoTextureHelper::TextureDescription is created at the first
    use, not by 'QVideoTextureHelper::TextureDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVideoTextureHelper::TextureDescription back gives a
    copy the ritual made for Python, in a new cute
    QVideoTextureHelper::TextureDescription.
  """

  #  The enums Qt writes inside QVideoTextureHelper::TextureDescription, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class FallbackPolicy(CuteNum, scoped=True):
    """
    The enum 'QVideoTextureHelper::TextureDescription::FallbackPolicy' of Qt,
    with the 2 names Qt gives in it. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    Disable = Kee[int](0)
    Enable = Kee[int](1)

  class TextureFormat(CuteNum):
    """
    The enum 'QVideoTextureHelper::TextureDescription::TextureFormat' of Qt,
    with the 7 names Qt gives in it.
    """

    UnknownFormat = Kee[int](0)
    Red_8 = Kee[int](1)
    RG_8 = Kee[int](2)
    RGBA_8 = Kee[int](3)
    BGRA_8 = Kee[int](4)
    Red_16 = Kee[int](5)
    RG_16 = Kee[int](6)

  #  The classes Qt writes inside QVideoTextureHelper::TextureDescription,
  #  each a class in here as in C++.

  class SizeScale(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVideoTextureHelper::TextureDescription::SizeScale:
    a plain Python object standing in front of one C++
    QVideoTextureHelper::TextureDescription::SizeScale.

    C++ hands a QVideoTextureHelper::TextureDescription::SizeScale around as
    a copy, so every C++ QVideoTextureHelper::TextureDescription::SizeScale
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QVideoTextureHelper::TextureDescription::SizeScale
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QVideoTextureHelper::TextureDescription::SizeScale::~SizeScale()': the
      destructor: Python removes its C++
      QVideoTextureHelper::TextureDescription::SizeScale by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QVideoTextureHelper::TextureDescription::SizeScale is created
      at the first use, not by
      'QVideoTextureHelper::TextureDescription::SizeScale(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVideoTextureHelper::TextureDescription::SizeScale
      back gives a copy the ritual made for Python, in a new cute
      QVideoTextureHelper::TextureDescription::SizeScale.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVideoTextureHelper::TextureDescription::SizeScale'

    #  Qt's '~QVideoTextureHelper::TextureDescription::SizeScale()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QVideoTextureHelper::TextureDescription::SizeScale behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN19QVideoTextureHelper18TextureDescription9SizeScaleD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoTextureHelper::TextureDescription'

  #  Qt's '~QVideoTextureHelper::TextureDescription()'. Naming it makes this
  #  a value class: Python owns every C++
  #  QVideoTextureHelper::TextureDescription behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN19QVideoTextureHelper18TextureDescriptionD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QRhi)
  @overload(int, NoneType)
  @overload(int, QRhi, FallbackPolicy)
  @overload(int, NoneType, FallbackPolicy)
  def rhiTextureFormat(
      self,
      plane: int,
      rhi: Optional[QRhi],
      policy: FallbackPolicy = FallbackPolicy.Enable,
  ) -> QRhiTexture.Format:
    """
    Calls Qt's 'QRhiTexture::Format
    QVideoTextureHelper::TextureDescription::rhiTextureFormat(int plane, QRhi
    *rhi, FallbackPolicy policy) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-texturedescription.html

    Parameters
    ----------

    plane : int
      Passed on as it is.

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    policy : FallbackPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      FallbackPolicy.Enable.

    Returns
    -------

    QRhiTexture.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiTexture.Format(number)' gives.
    """
    #  QRhiTexture::Format
    #      QVideoTextureHelper::TextureDescription::rhiTextureFormat(int
    #      plane, QRhi *rhi, FallbackPolicy policy) const
    return QRhiTexture.Format(self.uglySide.call(
        'ritual_ZNK19QVideoTextureHelper18TextureDescription16rhiTextureFor'
        'matEiP4QRhiNS0_14FallbackPolicyE',
        plane, self._addressOf(rhi), policy.value,
    ))

  @overload(int)
  def strideForWidth(self, width: int) -> int:
    """
    Calls Qt's 'int
    QVideoTextureHelper::TextureDescription::strideForWidth(int width)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-texturedescription.html

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  int QVideoTextureHelper::TextureDescription::strideForWidth(int width)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QVideoTextureHelper18TextureDescription14strideForWidt'
        'hEi',
        width,
    )

  @overload(QSize)
  def bytesForSize(self, s: QSize) -> int:
    """
    Calls Qt's 'int
    QVideoTextureHelper::TextureDescription::bytesForSize(QSize s) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-texturedescription.html

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  int QVideoTextureHelper::TextureDescription::bytesForSize(QSize s)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QVideoTextureHelper18TextureDescription12bytesForSizeE'
        '5QSize',
        self._valueOf(s),
    )

  @overload(int, int)
  def widthForPlane(self, width: int, plane: int) -> int:
    """
    Calls Qt's 'int
    QVideoTextureHelper::TextureDescription::widthForPlane(int width, int
    plane) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-texturedescription.html

    Parameters
    ----------

    width : int
      Passed on as it is.

    plane : int
      Passed on as it is.
    """
    #  int QVideoTextureHelper::TextureDescription::widthForPlane(int width,
    #      int plane) const
    return self.uglySide.call(
        'ritual_ZNK19QVideoTextureHelper18TextureDescription13widthForPlane'
        'Eii',
        width, plane,
    )

  @overload(int, int)
  def heightForPlane(self, height: int, plane: int) -> int:
    """
    Calls Qt's 'int
    QVideoTextureHelper::TextureDescription::heightForPlane(int height, int
    plane) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-texturedescription.html

    Parameters
    ----------

    height : int
      Passed on as it is.

    plane : int
      Passed on as it is.
    """
    #  int QVideoTextureHelper::TextureDescription::heightForPlane(int
    #      height, int plane) const
    return self.uglySide.call(
        'ritual_ZNK19QVideoTextureHelper18TextureDescription14heightForPlan'
        'eEii',
        height, plane,
    )

  @overload(int, QRhi)
  @overload(int, NoneType)
  def rhiSizeScale(self, plane: int, rhi: Optional[QRhi]) -> SizeScale:
    """
    Calls Qt's 'SizeScale
    QVideoTextureHelper::TextureDescription::rhiSizeScale(int plane, QRhi
    *rhi) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-texturedescription.html

    Parameters
    ----------

    plane : int
      Passed on as it is.

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    SizeScale
      A new cute QVideoTextureHelper::TextureDescription::SizeScale around
      the copy Qt gave back. Python owns it.
    """
    #  SizeScale QVideoTextureHelper::TextureDescription::rhiSizeScale(int
    #      plane, QRhi *rhi) const
    address = self.uglySide.call(
        'ritual_ZNK19QVideoTextureHelper18TextureDescription12rhiSizeScaleE'
        'iP4QRhi',
        plane, self._addressOf(rhi),
    )
    return QVideoTextureHelper.TextureDescription.SizeScale._cuteOwning(address)

  @overload(QSize, int, QRhi)
  @overload(QSize, int, NoneType)
  def rhiPlaneSize(
      self,
      frameSize: QSize,
      plane: int,
      rhi: Optional[QRhi],
  ) -> QSize:
    """
    Calls Qt's 'QSize
    QVideoTextureHelper::TextureDescription::rhiPlaneSize(QSize frameSize,
    int plane, QRhi *rhi) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-texturedescription.html

    Parameters
    ----------

    frameSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    plane : int
      Passed on as it is.

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVideoTextureHelper::TextureDescription::rhiPlaneSize(QSize
    #      frameSize, int plane, QRhi *rhi) const
    address = self.uglySide.call(
        'ritual_ZNK19QVideoTextureHelper18TextureDescription12rhiPlaneSizeE'
        '5QSizeiP4QRhi',
        self._valueOf(frameSize), plane, self._addressOf(rhi),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(TextureFormat)
  def hasTextureFormat(self, format: TextureFormat) -> bool:
    """
    Calls Qt's 'bool
    QVideoTextureHelper::TextureDescription::hasTextureFormat(TextureFormat
    format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideotexturehelper-texturedescription.html

    Parameters
    ----------

    format : TextureFormat
      Passed on as its number.
    """
    #  bool QVideoTextureHelper::TextureDescription::hasTextureFormat(
    #      TextureFormat format) const
    return self.uglySide.call(
        'ritual_ZNK19QVideoTextureHelper18TextureDescription16hasTextureFor'
        'matENS0_13TextureFormatE',
        format.value,
    )

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
