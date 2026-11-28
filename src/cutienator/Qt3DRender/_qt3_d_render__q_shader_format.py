"""
Qt3DRender::QShaderFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qshaderformat_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QShaderFormat to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVersionNumber
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVersionNumber = WAIT['QVersionNumber']


class QShaderFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QShaderFormat: a plain Python object
  standing in front of one C++ Qt3DRender::QShaderFormat.

  C++ hands a Qt3DRender::QShaderFormat around as a copy, so every C++
  Qt3DRender::QShaderFormat behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QShaderFormat that has a ritual and that
  Python can call so far, 12 names in all: 'api', 'setApi', 'version',
  'setVersion', 'extensions', 'setExtensions', 'vendor', 'setVendor',
  'isValid', 'supports', 'shaderType', 'setShaderType'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QShaderFormat::~QShaderFormat()': the destructor:
    Python removes its C++ Qt3DRender::QShaderFormat by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::QShaderFormat is created at the first use, not by
    'Qt3DRender::QShaderFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QShaderFormat back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::QShaderFormat.
  """

  #  The enums Qt writes inside Qt3DRender::QShaderFormat, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Api(CuteNum):
    """
    The enum 'Qt3DRender::QShaderFormat::Api' of Qt, with the 7 names Qt
    gives in it.
    """

    NoApi = Kee[int](0)
    OpenGLNoProfile = Kee[int](1)
    OpenGLCoreProfile = Kee[int](2)
    OpenGLCompatibilityProfile = Kee[int](3)
    OpenGLES = Kee[int](4)
    VulkanFlavoredGLSL = Kee[int](5)
    RHI = Kee[int](6)

  class ShaderType(CuteNum):
    """
    The enum 'Qt3DRender::QShaderFormat::ShaderType' of Qt, with the 6 names
    Qt gives in it.
    """

    Vertex = Kee[int](0)
    TessellationControl = Kee[int](1)
    TessellationEvaluation = Kee[int](2)
    Geometry = Kee[int](3)
    Fragment = Kee[int](4)
    Compute = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QShaderFormat'

  #  Qt's '~Qt3DRender::QShaderFormat()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DRender::QShaderFormat behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender13QShaderFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def api(self) -> Api:
    """
    Calls Qt's 'Api Qt3DRender::QShaderFormat::api() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#api

    Returns
    -------

    Api
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Api(number)' gives.
    """
    #  Api Qt3DRender::QShaderFormat::api() const
    return QShaderFormat.Api(self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QShaderFormat3apiEv',
    ))

  def version(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber Qt3DRender::QShaderFormat::version() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#version

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber Qt3DRender::QShaderFormat::version() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QShaderFormat7versionEv',
    )
    from ..QtCore import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  def extensions(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::QShaderFormat::extensions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#extensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QShaderFormat::extensions() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QShaderFormat10extensionsEv',
    )
    return QStringList._cuteOwning(address)

  def vendor(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QShaderFormat::vendor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#vendor

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QShaderFormat::vendor() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QShaderFormat6vendorEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QShaderFormat::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#isValid
    """
    #  bool Qt3DRender::QShaderFormat::isValid() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QShaderFormat7isValidEv',
    )

  @overload(THIS)
  def supports(self, other: QShaderFormat) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QShaderFormat::supports(const QShaderFormat
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#supports

    Parameters
    ----------

    other : QShaderFormat
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderFormat, which
      stays Python's own.
    """
    #  bool Qt3DRender::QShaderFormat::supports(const QShaderFormat &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QShaderFormat8supportsERKS0_',
        self._valueOf(other),
    )

  def shaderType(self) -> ShaderType:
    """
    Calls Qt's 'ShaderType Qt3DRender::QShaderFormat::shaderType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#shaderType

    Returns
    -------

    ShaderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ShaderType(number)'
      gives.
    """
    #  ShaderType Qt3DRender::QShaderFormat::shaderType() const
    return QShaderFormat.ShaderType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QShaderFormat10shaderTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Api)
  def setApi(self, api: Api) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderFormat::setApi(Api api)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#setApi

    Parameters
    ----------

    api : Api
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderFormat::setApi(Api api)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QShaderFormat6setApiENS0_3ApiE', api.value,
    )

  @overload(QVersionNumber)
  def setVersion(self, version: QVersionNumber) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderFormat::setVersion(const
    QVersionNumber &version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#setVersion

    Parameters
    ----------

    version : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  void Qt3DRender::QShaderFormat::setVersion(const QVersionNumber
    #      &version)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QShaderFormat10setVersionERK14QVersionNumbe'
        'r',
        self._valueOf(version),
    )

  @overload(QStringList)
  def setExtensions(self, extensions: QStringList) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderFormat::setExtensions(const
    QStringList &extensions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#setExtensions

    Parameters
    ----------

    extensions : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::QShaderFormat::setExtensions(const QStringList
    #      &extensions)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QShaderFormat13setExtensionsERK5QListI7QStr'
        'ingE',
        self._valueOf(extensions),
    )

  @overload(str)
  def setVendor(self, vendor: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderFormat::setVendor(const QString
    &vendor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#setVendor

    Parameters
    ----------

    vendor : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QShaderFormat::setVendor(const QString &vendor)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QShaderFormat9setVendorERK7QString', vendor,
    )

  @overload(ShaderType)
  def setShaderType(self, shaderType: ShaderType) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderFormat::setShaderType(ShaderType
    shaderType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#setShaderType

    Parameters
    ----------

    shaderType : ShaderType
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderFormat::setShaderType(ShaderType shaderType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QShaderFormat13setShaderTypeENS0_10ShaderTy'
        'peE',
        shaderType.value,
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
    Notes what was given, for Qt's
    'Qt3DRender::QShaderFormat::QShaderFormat()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderformat.html#QShaderFormat
    """
    #  Qt3DRender::QShaderFormat::QShaderFormat()
    self._noteCreation(QShaderFormat, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender13QShaderFormatC1Ev',
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
