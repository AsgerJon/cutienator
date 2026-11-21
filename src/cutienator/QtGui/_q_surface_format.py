"""
QSurfaceFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qsurfaceformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSurfaceFormatColorSpace, QSurfaceFormatFormatOption
from . import QSurfaceFormatOpenGLContextProfile
from . import QSurfaceFormatRenderableType, QSurfaceFormatSwapBehavior

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QColorSpace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorSpace = WAIT['QColorSpace']


class QSurfaceFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSurfaceFormat: a plain Python object standing in
  front of one C++ QSurfaceFormat.

  C++ hands a QSurfaceFormat around as a copy, so every C++ QSurfaceFormat
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSurfaceFormat that has a ritual and that Python can
  call so far, 38 names in all: 'setDepthBufferSize', 'depthBufferSize',
  'setStencilBufferSize', 'stencilBufferSize', 'setRedBufferSize',
  'redBufferSize', 'setGreenBufferSize', 'greenBufferSize',
  'setBlueBufferSize', 'blueBufferSize', 'setAlphaBufferSize',
  'alphaBufferSize', 'setSamples', 'samples', 'setSwapBehavior',
  'swapBehavior', 'hasAlpha', 'setProfile', 'profile', 'setRenderableType',
  'renderableType', 'setMajorVersion', 'majorVersion', 'setMinorVersion',
  'minorVersion', 'setVersion', 'stereo', 'setStereo', 'setOptions',
  'setOption', 'testOption', 'options', 'swapInterval', 'setSwapInterval',
  'colorSpace', 'setColorSpace', 'setDefaultFormat', 'defaultFormat'. It can
  be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSurfaceFormat::~QSurfaceFormat()': the destructor: Python removes
    its C++ QSurfaceFormat by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 50 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 1 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QSurfaceFormat is created at the first use, not by
    'QSurfaceFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSurfaceFormat back gives a copy the ritual made for
    Python, in a new cute QSurfaceFormat.
  """

  #  The enums Qt writes inside QSurfaceFormat, and the names Qt has for the
  #  combinations of its flags enums.
  ColorSpace = QSurfaceFormatColorSpace
  FormatOption = QSurfaceFormatFormatOption
  FormatOptions = QSurfaceFormatFormatOption
  OpenGLContextProfile = QSurfaceFormatOpenGLContextProfile
  RenderableType = QSurfaceFormatRenderableType
  SwapBehavior = QSurfaceFormatSwapBehavior

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  def setDefaultFormat(format: QSurfaceFormat) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setDefaultFormat(const QSurfaceFormat
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setDefaultFormat

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  void QSurfaceFormat::setDefaultFormat(const QSurfaceFormat &format)
    Rituals.call(
        'ritual_ZN14QSurfaceFormat16setDefaultFormatERKS_',
        CuteMixin._valueOf(format),
    )

  @staticmethod
  def defaultFormat() -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QSurfaceFormat::defaultFormat()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#defaultFormat

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QSurfaceFormat::defaultFormat()
    address = Rituals.call('ritual_ZN14QSurfaceFormat13defaultFormatEv')
    return QSurfaceFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSurfaceFormat'

  #  Qt's '~QSurfaceFormat()'. Naming it makes this a value class: Python
  #  owns every C++ QSurfaceFormat behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSurfaceFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def depthBufferSize(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::depthBufferSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#depthBufferSize
    """
    #  int QSurfaceFormat::depthBufferSize() const
    return self.uglySide.call(
        'ritual_ZNK14QSurfaceFormat15depthBufferSizeEv',
    )

  def stencilBufferSize(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::stencilBufferSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#stencilBufferSize
    """
    #  int QSurfaceFormat::stencilBufferSize() const
    return self.uglySide.call(
        'ritual_ZNK14QSurfaceFormat17stencilBufferSizeEv',
    )

  def redBufferSize(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::redBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#redBufferSize
    """
    #  int QSurfaceFormat::redBufferSize() const
    return self.uglySide.call('ritual_ZNK14QSurfaceFormat13redBufferSizeEv')

  def greenBufferSize(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::greenBufferSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#greenBufferSize
    """
    #  int QSurfaceFormat::greenBufferSize() const
    return self.uglySide.call(
        'ritual_ZNK14QSurfaceFormat15greenBufferSizeEv',
    )

  def blueBufferSize(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::blueBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#blueBufferSize
    """
    #  int QSurfaceFormat::blueBufferSize() const
    return self.uglySide.call('ritual_ZNK14QSurfaceFormat14blueBufferSizeEv')

  def alphaBufferSize(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::alphaBufferSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#alphaBufferSize
    """
    #  int QSurfaceFormat::alphaBufferSize() const
    return self.uglySide.call(
        'ritual_ZNK14QSurfaceFormat15alphaBufferSizeEv',
    )

  def samples(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::samples() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#samples
    """
    #  int QSurfaceFormat::samples() const
    return self.uglySide.call('ritual_ZNK14QSurfaceFormat7samplesEv')

  def swapBehavior(self) -> SwapBehavior:
    """
    Calls Qt's 'SwapBehavior QSurfaceFormat::swapBehavior() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#swapBehavior

    Returns
    -------

    SwapBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SwapBehavior(number)'
      gives.
    """
    #  SwapBehavior QSurfaceFormat::swapBehavior() const
    return QSurfaceFormat.SwapBehavior(self.uglySide.call(
        'ritual_ZNK14QSurfaceFormat12swapBehaviorEv',
    ))

  def hasAlpha(self) -> bool:
    """
    Calls Qt's 'bool QSurfaceFormat::hasAlpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#hasAlpha
    """
    #  bool QSurfaceFormat::hasAlpha() const
    return self.uglySide.call('ritual_ZNK14QSurfaceFormat8hasAlphaEv')

  def profile(self) -> OpenGLContextProfile:
    """
    Calls Qt's 'OpenGLContextProfile QSurfaceFormat::profile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#profile

    Returns
    -------

    OpenGLContextProfile
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'OpenGLContextProfile(number)' gives.
    """
    #  OpenGLContextProfile QSurfaceFormat::profile() const
    return QSurfaceFormat.OpenGLContextProfile(self.uglySide.call(
        'ritual_ZNK14QSurfaceFormat7profileEv',
    ))

  def renderableType(self) -> RenderableType:
    """
    Calls Qt's 'RenderableType QSurfaceFormat::renderableType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#renderableType

    Returns
    -------

    RenderableType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderableType(number)'
      gives.
    """
    #  RenderableType QSurfaceFormat::renderableType() const
    return QSurfaceFormat.RenderableType(self.uglySide.call(
        'ritual_ZNK14QSurfaceFormat14renderableTypeEv',
    ))

  def majorVersion(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::majorVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#majorVersion
    """
    #  int QSurfaceFormat::majorVersion() const
    return self.uglySide.call('ritual_ZNK14QSurfaceFormat12majorVersionEv')

  def minorVersion(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::minorVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#minorVersion
    """
    #  int QSurfaceFormat::minorVersion() const
    return self.uglySide.call('ritual_ZNK14QSurfaceFormat12minorVersionEv')

  def stereo(self) -> bool:
    """
    Calls Qt's 'bool QSurfaceFormat::stereo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#stereo
    """
    #  bool QSurfaceFormat::stereo() const
    return self.uglySide.call('ritual_ZNK14QSurfaceFormat6stereoEv')

  @overload(FormatOption)
  def testOption(self, option: FormatOption) -> bool:
    """
    Calls Qt's 'bool QSurfaceFormat::testOption(FormatOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#testOption

    Parameters
    ----------

    option : FormatOption
      Passed on as its number.
    """
    #  bool QSurfaceFormat::testOption(FormatOption option) const
    return self.uglySide.call(
        'ritual_ZNK14QSurfaceFormat10testOptionENS_12FormatOptionE',
        option.value,
    )

  def options(self) -> FormatOptions:
    """
    Calls Qt's 'QSurfaceFormat::FormatOptions QSurfaceFormat::options()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#options

    Returns
    -------

    FormatOptions
      The value standing for the combination Qt gave back.
    """
    #  QSurfaceFormat::FormatOptions QSurfaceFormat::options() const
    return QSurfaceFormat.FormatOptions(self.uglySide.call(
        'ritual_ZNK14QSurfaceFormat7optionsEv',
    ))

  def swapInterval(self) -> int:
    """
    Calls Qt's 'int QSurfaceFormat::swapInterval() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#swapInterval
    """
    #  int QSurfaceFormat::swapInterval() const
    return self.uglySide.call('ritual_ZNK14QSurfaceFormat12swapIntervalEv')

  def colorSpace(self) -> QColorSpace:
    """
    Calls Qt's 'const QColorSpace &QSurfaceFormat::colorSpace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#colorSpace

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  const QColorSpace &QSurfaceFormat::colorSpace() const
    address = self.uglySide.call('ritual_ZNK14QSurfaceFormat10colorSpaceEv')
    from . import QColorSpace
    return QColorSpace._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDepthBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setDepthBufferSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setDepthBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setDepthBufferSize(int size)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat18setDepthBufferSizeEi', size,
    )

  @overload(int)
  def setStencilBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setStencilBufferSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setStencilBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setStencilBufferSize(int size)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat20setStencilBufferSizeEi', size,
    )

  @overload(int)
  def setRedBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setRedBufferSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setRedBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setRedBufferSize(int size)
    self.uglySide.call('ritual_ZN14QSurfaceFormat16setRedBufferSizeEi', size)

  @overload(int)
  def setGreenBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setGreenBufferSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setGreenBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setGreenBufferSize(int size)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat18setGreenBufferSizeEi', size,
    )

  @overload(int)
  def setBlueBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setBlueBufferSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setBlueBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setBlueBufferSize(int size)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat17setBlueBufferSizeEi', size,
    )

  @overload(int)
  def setAlphaBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setAlphaBufferSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setAlphaBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setAlphaBufferSize(int size)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat18setAlphaBufferSizeEi', size,
    )

  @overload(int)
  def setSamples(self, numSamples: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setSamples(int numSamples)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#setSamples

    Parameters
    ----------

    numSamples : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setSamples(int numSamples)
    self.uglySide.call('ritual_ZN14QSurfaceFormat10setSamplesEi', numSamples)

  @overload(SwapBehavior)
  def setSwapBehavior(self, behavior: SwapBehavior) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setSwapBehavior(SwapBehavior behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setSwapBehavior

    Parameters
    ----------

    behavior : SwapBehavior
      Passed on as its number.
    """
    #  void QSurfaceFormat::setSwapBehavior(SwapBehavior behavior)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat15setSwapBehaviorENS_12SwapBehaviorE',
        behavior.value,
    )

  @overload(OpenGLContextProfile)
  def setProfile(self, profile: OpenGLContextProfile) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setProfile(OpenGLContextProfile
    profile)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#setProfile

    Parameters
    ----------

    profile : OpenGLContextProfile
      Passed on as its number.
    """
    #  void QSurfaceFormat::setProfile(OpenGLContextProfile profile)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat10setProfileENS_20OpenGLContextProfileE',
        profile.value,
    )

  @overload(RenderableType)
  def setRenderableType(self, type: RenderableType) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setRenderableType(RenderableType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setRenderableType

    Parameters
    ----------

    type : RenderableType
      Passed on as its number.
    """
    #  void QSurfaceFormat::setRenderableType(RenderableType type)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat17setRenderableTypeENS_14RenderableTypeE',
        type.value,
    )

  @overload(int)
  def setMajorVersion(self, majorVersion: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setMajorVersion(int majorVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setMajorVersion

    Parameters
    ----------

    majorVersion : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setMajorVersion(int majorVersion)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat15setMajorVersionEi', majorVersion,
    )

  @overload(int)
  def setMinorVersion(self, minorVersion: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setMinorVersion(int minorVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setMinorVersion

    Parameters
    ----------

    minorVersion : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setMinorVersion(int minorVersion)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat15setMinorVersionEi', minorVersion,
    )

  @overload(int, int)
  def setVersion(self, major: int, minor: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setVersion(int major, int minor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#setVersion

    Parameters
    ----------

    major : int
      Passed on as it is.

    minor : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setVersion(int major, int minor)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat10setVersionEii', major, minor,
    )

  @overload(bool)
  def setStereo(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setStereo(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#setStereo

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSurfaceFormat::setStereo(bool enable)
    self.uglySide.call('ritual_ZN14QSurfaceFormat9setStereoEb', enable)

  @overload(FormatOptions)
  def setOptions(self, options: FormatOptions) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setOptions(QSurfaceFormat::FormatOptions
    options)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#setOptions

    Parameters
    ----------

    options : FormatOptions
      Passed on as its number.
    """
    #  void QSurfaceFormat::setOptions(QSurfaceFormat::FormatOptions options)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat10setOptionsE6QFlagsINS_12FormatOptionEE',
        options.value,
    )

  @overload(FormatOption)
  @overload(FormatOption, bool)
  def setOption(self, option: FormatOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setOption(FormatOption option, bool
    on)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#setOption

    Parameters
    ----------

    option : FormatOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSurfaceFormat::setOption(FormatOption option, bool on)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat9setOptionENS_12FormatOptionEb',
        option.value, on,
    )

  @overload(int)
  def setSwapInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setSwapInterval(int interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfaceformat.html#setSwapInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QSurfaceFormat::setSwapInterval(int interval)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat15setSwapIntervalEi', interval,
    )

  @overload(QColorSpace)
  def setColorSpace(self, colorSpace: QColorSpace) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setColorSpace(const QColorSpace
    &colorSpace)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#setColorSpace

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  void QSurfaceFormat::setColorSpace(const QColorSpace &colorSpace)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat13setColorSpaceERK11QColorSpace',
        self._valueOf(colorSpace),
    )

  @overload(ColorSpace)
  def setColorSpace(self, colorSpace: ColorSpace) -> None:
    """
    Calls Qt's 'void QSurfaceFormat::setColorSpace(ColorSpace colorSpace)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#setColorSpace

    Parameters
    ----------

    colorSpace : ColorSpace
      Passed on as its number.
    """
    #  void QSurfaceFormat::setColorSpace(ColorSpace colorSpace)
    self.uglySide.call(
        'ritual_ZN14QSurfaceFormat13setColorSpaceENS_10ColorSpaceE',
        colorSpace.value,
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
    Notes what was given, for Qt's 'QSurfaceFormat::QSurfaceFormat()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#QSurfaceFormat
    """
    #  QSurfaceFormat::QSurfaceFormat()
    self._noteCreation(QSurfaceFormat, lambda: Rituals.call(
        'ritual_ZN14QSurfaceFormatC1Ev',
    ))

  @overload(FormatOptions)
  def __init__(self, options: FormatOptions) -> None:
    """
    Notes what was given, for Qt's
    'QSurfaceFormat::QSurfaceFormat(FormatOptions options)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#QSurfaceFormat

    Parameters
    ----------

    options : FormatOptions
      Passed on as its number.
    """
    #  QSurfaceFormat::QSurfaceFormat(FormatOptions options)
    self._noteCreation(QSurfaceFormat, lambda: Rituals.call(
        'ritual_ZN14QSurfaceFormatC1E6QFlagsINS_12FormatOptionEE',
        options.value,
    ))

  @overload(THIS)
  def __init__(self, other: QSurfaceFormat) -> None:
    """
    Notes what was given, for Qt's 'QSurfaceFormat::QSurfaceFormat(const
    QSurfaceFormat &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsurfaceformat.html#QSurfaceFormat

    Parameters
    ----------

    other : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  QSurfaceFormat::QSurfaceFormat(const QSurfaceFormat &other)
    self._noteCreation(QSurfaceFormat, lambda: Rituals.call(
        'ritual_ZN14QSurfaceFormatC1ERKS_', self._valueOf(other),
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
