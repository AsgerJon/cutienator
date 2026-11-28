"""
Utils binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/utils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Utils to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QPoint
  from ..QtGui import QColor, QQuaternion, QVector3D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QPoint = WAIT['QPoint']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']


class Utils(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Utils: a plain Python object standing in front of one
  C++ Utils.

  C++ hands a Utils around as a copy, so every C++ Utils behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Utils that has a ritual and that Python can call so
  far, 8 names in all: 'getNearestPowerOfTwo', 'vectorFromColor',
  'colorFromVector', 'getSelection', 'formatLabelSprintf',
  'defaultLabelFormat', 'wrapValue', 'calculateRotation'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImage Utils::getGradientImage(QLinearGradient &gradient)': takes a
    type Python has no way to hand over yet.
  - Qt's 'ParamType Utils::preParseFormat(const QString &format, QString
    &preStr, QString &postStr, int &precision, char &formatSpec)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QString Utils::formatLabelLocalized(ParamType paramType, qreal
    value, const QLocale &locale, const QString &preStr, const QString
    &postStr, int precision, char formatSpec, const QByteArray &format)':
    takes a single letter as C has it.
  - Qt's 'ParamType Utils::mapFormatCharToParamType(char formatSpec)': takes
    a single letter as C has it.
  - Qt's 'Utils::~Utils()': the destructor: Python removes its C++ Utils by
    it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ Utils is created at the first use, not by 'Utils(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Utils back gives a copy the ritual made for Python,
    in a new cute Utils.
  - Each name of Qt's Utils that has no cute function yet,
    'formatLabelLocalized', 'getGradientImage', 'isOpenGLES',
    'mapFormatCharToParamType', 'preParseFormat', 'printTextToImage',
    'resolveStatics', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside Utils, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class ParamType(CuteNum):
    """The enum 'Utils::ParamType' of Qt, with the 4 names Qt gives in it."""

    ParamTypeUnknown = Kee[int](0)
    ParamTypeInt = Kee[int](1)
    ParamTypeUInt = Kee[int](2)
    ParamTypeReal = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def getNearestPowerOfTwo(value: int) -> int:
    """
    Calls Qt's 'GLuint Utils::getNearestPowerOfTwo(GLuint value)'.

    Qt's own words: https://doc.qt.io/qt-6/utils.html#getNearestPowerOfTwo

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  GLuint Utils::getNearestPowerOfTwo(GLuint value)
    return Rituals.call('ritual_ZN5Utils20getNearestPowerOfTwoEj', value)

  @staticmethod
  @overload(QColor)
  def vectorFromColor(color: QColor) -> QVector4D:
    """
    Calls Qt's 'QVector4D Utils::vectorFromColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/utils.html#vectorFromColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D Utils::vectorFromColor(const QColor &color)
    address = Rituals.call(
        'ritual_ZN5Utils15vectorFromColorERK6QColor',
        CuteMixin._valueOf(color),
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  @staticmethod
  @overload(QVector3D)
  def colorFromVector(colorVector: QVector3D) -> QColor:
    """
    Calls Qt's 'QColor Utils::colorFromVector(const QVector3D &colorVector)'.

    Qt's own words: https://doc.qt.io/qt-6/utils.html#colorFromVector

    Parameters
    ----------

    colorVector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Utils::colorFromVector(const QVector3D &colorVector)
    address = Rituals.call(
        'ritual_ZN5Utils15colorFromVectorERK9QVector3D',
        CuteMixin._valueOf(colorVector),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QVector4D)
  def colorFromVector(colorVector: QVector4D) -> QColor:
    """
    Calls Qt's 'QColor Utils::colorFromVector(const QVector4D &colorVector)'.

    Qt's own words: https://doc.qt.io/qt-6/utils.html#colorFromVector

    Parameters
    ----------

    colorVector : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Utils::colorFromVector(const QVector4D &colorVector)
    address = Rituals.call(
        'ritual_ZN5Utils15colorFromVectorERK9QVector4D',
        CuteMixin._valueOf(colorVector),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QPoint, int)
  def getSelection(mousepos: QPoint, height: int) -> QVector4D:
    """
    Calls Qt's 'QVector4D Utils::getSelection(QPoint mousepos, int height)'.

    Qt's own words: https://doc.qt.io/qt-6/utils.html#getSelection

    Parameters
    ----------

    mousepos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    height : int
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D Utils::getSelection(QPoint mousepos, int height)
    address = Rituals.call(
        'ritual_ZN5Utils12getSelectionE6QPointi',
        CuteMixin._valueOf(mousepos), height,
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  @staticmethod
  @overload(QByteArray, ParamType, float)
  def formatLabelSprintf(
      format: QByteArray,
      paramType: ParamType,
      value: float,
  ) -> str:
    """
    Calls Qt's 'QString Utils::formatLabelSprintf(const QByteArray &format,
    ParamType paramType, qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/utils.html#formatLabelSprintf

    Parameters
    ----------

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    paramType : ParamType
      Passed on as its number.

    value : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Utils::formatLabelSprintf(const QByteArray &format, ParamType
    #      paramType, qreal value)
    return Rituals.call(
        'ritual_ZN5Utils18formatLabelSprintfERK10QByteArrayNS_9ParamTypeEd',
        CuteMixin._valueOf(format), paramType.value, value,
    )

  @staticmethod
  def defaultLabelFormat() -> str:
    """
    Calls Qt's 'QString Utils::defaultLabelFormat()'.

    Qt's own words: https://doc.qt.io/qt-6/utils.html#defaultLabelFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Utils::defaultLabelFormat()
    return Rituals.call('ritual_ZN5Utils18defaultLabelFormatEv')

  @staticmethod
  @overload(float, float, float)
  def wrapValue(value: float, min: float, max: float) -> float:
    """
    Calls Qt's 'float Utils::wrapValue(float value, float min, float max)'.

    Qt's own words: https://doc.qt.io/qt-6/utils.html#wrapValue

    Parameters
    ----------

    value : float
      Passed on as it is.

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  float Utils::wrapValue(float value, float min, float max)
    return Rituals.call('ritual_ZN5Utils9wrapValueEfff', value, min, max)

  @staticmethod
  @overload(QVector3D)
  def calculateRotation(xyzRotations: QVector3D) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Utils::calculateRotation(const QVector3D
    &xyzRotations)'.

    Qt's own words: https://doc.qt.io/qt-6/utils.html#calculateRotation

    Parameters
    ----------

    xyzRotations : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Utils::calculateRotation(const QVector3D &xyzRotations)
    address = Rituals.call(
        'ritual_ZN5Utils17calculateRotationERK9QVector3D',
        CuteMixin._valueOf(xyzRotations),
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Utils'

  #  Qt's '~Utils()'. Naming it makes this a value class: Python owns every
  #  C++ Utils behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5UtilsD1Ev'

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

  @staticmethod
  def formatLabelLocalized(*__, **_) -> Never:
    """
    Qt's 'QString Utils::formatLabelLocalized(ParamType paramType, qreal
    value, const QLocale &locale, const QString &preStr, const QString
    &postStr, int precision, char formatSpec, const QByteArray &format)':
    takes a single letter as C has it.
    """
    raise NotImplementedError(
        "'Utils.formatLabelLocalized' has no cute function yet. Qt's "
        "'QString Utils::formatLabelLocalized(ParamType paramType, qreal "
        "value, const QLocale &locale, const QString &preStr, const QString "
        "&postStr, int precision, char formatSpec, const QByteArray "
        "&format)': takes a single letter as C has it.")

  @staticmethod
  def getGradientImage(*__, **_) -> Never:
    """
    Qt's 'QImage Utils::getGradientImage(QLinearGradient &gradient)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Utils.getGradientImage' has no cute function yet. Qt's 'QImage "
        "Utils::getGradientImage(QLinearGradient &gradient)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def isOpenGLES(*__, **_) -> Never:
    """
    Qt's 'bool Utils::isOpenGLES()': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'staticsResolved'.
    """
    raise NotImplementedError(
        "'Utils.isOpenGLES' has no cute function yet. Qt's 'bool "
        "Utils::isOpenGLES()': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'staticsResolved'.")

  @staticmethod
  def mapFormatCharToParamType(*__, **_) -> Never:
    """
    Qt's 'ParamType Utils::mapFormatCharToParamType(char formatSpec)': takes
    a single letter as C has it.
    """
    raise NotImplementedError(
        "'Utils.mapFormatCharToParamType' has no cute function yet. Qt's "
        "'ParamType Utils::mapFormatCharToParamType(char formatSpec)': "
        "takes a single letter as C has it.")

  @staticmethod
  def preParseFormat(*__, **_) -> Never:
    """
    Qt's 'ParamType Utils::preParseFormat(const QString &format, QString
    &preStr, QString &postStr, int &precision, char &formatSpec)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Utils.preParseFormat' has no cute function yet. Qt's 'ParamType "
        "Utils::preParseFormat(const QString &format, QString &preStr, "
        "QString &postStr, int &precision, char &formatSpec)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def printTextToImage(*__, **_) -> Never:
    """
    Qt's 'QImage Utils::printTextToImage(const QFont &font, const QString
    &text, const QColor &bgrColor, const QColor &txtColor, bool
    labelBackground, bool borders, int maxLabelWidth)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'staticsResolved'.
    """
    raise NotImplementedError(
        "'Utils.printTextToImage' has no cute function yet. Qt's 'QImage "
        "Utils::printTextToImage(const QFont &font, const QString &text, "
        "const QColor &bgrColor, const QColor &txtColor, bool "
        "labelBackground, bool borders, int maxLabelWidth)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'staticsResolved'.")

  @staticmethod
  def resolveStatics(*__, **_) -> Never:
    """
    Qt's 'void Utils::resolveStatics()': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'isES'.
    """
    raise NotImplementedError(
        "'Utils.resolveStatics' has no cute function yet. Qt's 'void "
        "Utils::resolveStatics()': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'isES'.")
