"""
QColor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qcolor.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt
from ._q_rgba64 import QRgba64
from ._q_color_name_format import NameFormat
from ._q_color_spec import Spec

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColor: a plain Python object standing in front of
  one C++ QColor.

  C++ hands a QColor around as a copy, so every C++ QColor behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColor that has a ritual and that Python can call so
  far, 78 names in all: 'fromString', 'isValid', 'name', 'setNamedColor',
  'spec', 'alpha', 'setAlpha', 'alphaF', 'setAlphaF', 'red', 'green', 'blue',
  'setRed', 'setGreen', 'setBlue', 'redF', 'greenF', 'blueF', 'setRedF',
  'setGreenF', 'setBlueF', 'setRgb', 'setRgbF', 'rgba64', 'setRgba64',
  'rgba', 'setRgba', 'rgb', 'hue', 'saturation', 'hsvHue', 'hsvSaturation',
  'value', 'hueF', 'saturationF', 'hsvHueF', 'hsvSaturationF', 'valueF',
  'setHsv', 'setHsvF', 'cyan', 'magenta', 'yellow', 'black', 'cyanF',
  'magentaF', 'yellowF', 'blackF', 'setCmyk', 'setCmykF', 'hslHue',
  'hslSaturation', 'lightness', 'hslHueF', 'hslSaturationF', 'lightnessF',
  'setHsl', 'setHslF', 'toRgb', 'toHsv', 'toCmyk', 'toHsl', 'toExtendedRgb',
  'convertTo', 'fromRgb', 'fromRgba', 'fromRgbF', 'fromRgba64', 'fromHsv',
  'fromHsvF', 'fromCmyk', 'fromCmykF', 'fromHsl', 'fromHslF', 'lighter',
  'darker', 'isValidColor', 'isValidColorName'. It can be made from Python,
  in 9 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColor::QColor(QStringView name)': takes in Python what
    'QColor::QColor(const QString &name)' takes.
  - Qt's 'QColor::QColor(QLatin1StringView name)': names 'QLatin1String',
    which has no cute class yet.
  - Qt's 'void QColor::setNamedColor(QStringView name)': takes in Python what
    'void QColor::setNamedColor(const QString &name)' takes.
  - Qt's 'void QColor::setNamedColor(QLatin1StringView name)': names
    'QLatin1String', which has no cute class yet.
  - Qt's 'void QColor::getRgb(int *r, int *g, int *b, int *a) const': takes a
    number to change where it is.
  - Qt's 'void QColor::getRgbF(float *r, float *g, float *b, float *a)
    const': takes a number to change where it is.
  - Qt's 'void QColor::getHsv(int *h, int *s, int *v, int *a) const': takes a
    number to change where it is.
  - Qt's 'void QColor::getHsvF(float *h, float *s, float *v, float *a)
    const': takes a number to change where it is.
  - Qt's 'void QColor::getCmyk(int *c, int *m, int *y, int *k, int *a)
    const': takes a number to change where it is.
  - Qt's 'void QColor::getCmykF(float *c, float *m, float *y, float *k, float
    *a) const': takes a number to change where it is.
  - Qt's 'void QColor::getHsl(int *h, int *s, int *l, int *a) const': takes a
    number to change where it is.
  - Qt's 'void QColor::getHslF(float *h, float *s, float *l, float *a)
    const': takes a number to change where it is.
  - Qt's 'bool QColor::operator==(const QColor &c) const': an operator, which
    is not reflected yet.
  - Qt's 'bool QColor::operator!=(const QColor &c) const': an operator, which
    is not reflected yet.
  - Qt's 'QVariant QColor::operator QVariant() const': an operator, which is
    not reflected yet.
  - Qt's 'bool QColor::isValidColor(QStringView a0)': takes in Python what
    'bool QColor::isValidColor(const QString &name)' takes.
  - Qt's 'bool QColor::isValidColor(QLatin1StringView a0)': names
    'QLatin1String', which has no cute class yet.
  - Qt's 'QColor::~QColor()': the destructor: Python removes its C++ QColor
    by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 112 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 private.

  What to expect
  --------------

  - The C++ QColor is created at the first use, not by 'QColor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColor back gives a copy the ritual made for Python,
    in a new cute QColor.
  """

  #  The enums Qt writes inside QColor, and the names Qt has for the
  #  combinations of its flags enums.
  NameFormat = NameFormat
  Spec = Spec

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def fromString(name: str) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromString(QAnyStringView name)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromString

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromString(QAnyStringView name)
    address = Rituals.call(
        'ritual_ZN6QColor10fromStringE14QAnyStringView', name,
    )
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromRgb(rgb: int) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromRgb(QRgb rgb)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromRgb

    Parameters
    ----------

    rgb : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromRgb(QRgb rgb)
    address = Rituals.call('ritual_ZN6QColor7fromRgbEj', rgb)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(int, int, int)
  @overload(int, int, int, int)
  def fromRgb(r: int, g: int, b: int, a: int = 255) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromRgb(int r, int g, int b, int a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromRgb

    Parameters
    ----------

    r : int
      Passed on as it is.

    g : int
      Passed on as it is.

    b : int
      Passed on as it is.

    a : int
      Passed on as it is. May be left out, as in Qt: it is then 255.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromRgb(int r, int g, int b, int a)
    address = Rituals.call('ritual_ZN6QColor7fromRgbEiiii', r, g, b, a)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromRgba(rgba: int) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromRgba(QRgb rgba)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromRgba

    Parameters
    ----------

    rgba : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromRgba(QRgb rgba)
    address = Rituals.call('ritual_ZN6QColor8fromRgbaEj', rgba)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(float, float, float)
  @overload(float, float, float, float)
  def fromRgbF(r: float, g: float, b: float, a: float = 1.0) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromRgbF(float r, float g, float b, float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromRgbF

    Parameters
    ----------

    r : float
      Passed on as it is.

    g : float
      Passed on as it is.

    b : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromRgbF(float r, float g, float b, float a)
    address = Rituals.call('ritual_ZN6QColor8fromRgbFEffff', r, g, b, a)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(int, int, int, int)
  def fromRgba64(r: int, g: int, b: int, a: int) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromRgba64(ushort r, ushort g, ushort b,
    ushort a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromRgba64

    Parameters
    ----------

    r : int
      Passed on as it is.

    g : int
      Passed on as it is.

    b : int
      Passed on as it is.

    a : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromRgba64(ushort r, ushort g, ushort b, ushort a)
    address = Rituals.call('ritual_ZN6QColor10fromRgba64Etttt', r, g, b, a)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QRgba64)
  def fromRgba64(rgba: QRgba64) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromRgba64(QRgba64 rgba)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromRgba64

    Parameters
    ----------

    rgba : QRgba64
      Passed on as a value: Qt reads the C++ QRgba64, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromRgba64(QRgba64 rgba)
    address = Rituals.call(
        'ritual_ZN6QColor10fromRgba64E7QRgba64', CuteMixin._valueOf(rgba),
    )
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(int, int, int)
  @overload(int, int, int, int)
  def fromHsv(h: int, s: int, v: int, a: int = 255) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromHsv(int h, int s, int v, int a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromHsv

    Parameters
    ----------

    h : int
      Passed on as it is.

    s : int
      Passed on as it is.

    v : int
      Passed on as it is.

    a : int
      Passed on as it is. May be left out, as in Qt: it is then 255.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromHsv(int h, int s, int v, int a)
    address = Rituals.call('ritual_ZN6QColor7fromHsvEiiii', h, s, v, a)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(float, float, float)
  @overload(float, float, float, float)
  def fromHsvF(h: float, s: float, v: float, a: float = 1.0) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromHsvF(float h, float s, float v, float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromHsvF

    Parameters
    ----------

    h : float
      Passed on as it is.

    s : float
      Passed on as it is.

    v : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromHsvF(float h, float s, float v, float a)
    address = Rituals.call('ritual_ZN6QColor8fromHsvFEffff', h, s, v, a)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(int, int, int, int)
  @overload(int, int, int, int, int)
  def fromCmyk(c: int, m: int, y: int, k: int, a: int = 255) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromCmyk(int c, int m, int y, int k, int a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromCmyk

    Parameters
    ----------

    c : int
      Passed on as it is.

    m : int
      Passed on as it is.

    y : int
      Passed on as it is.

    k : int
      Passed on as it is.

    a : int
      Passed on as it is. May be left out, as in Qt: it is then 255.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromCmyk(int c, int m, int y, int k, int a)
    address = Rituals.call('ritual_ZN6QColor8fromCmykEiiiii', c, m, y, k, a)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(float, float, float, float)
  @overload(float, float, float, float, float)
  def fromCmykF(
      c: float,
      m: float,
      y: float,
      k: float,
      a: float = 1.0,
  ) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromCmykF(float c, float m, float y, float k,
    float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromCmykF

    Parameters
    ----------

    c : float
      Passed on as it is.

    m : float
      Passed on as it is.

    y : float
      Passed on as it is.

    k : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromCmykF(float c, float m, float y, float k, float a)
    address = Rituals.call('ritual_ZN6QColor9fromCmykFEfffff', c, m, y, k, a)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(int, int, int)
  @overload(int, int, int, int)
  def fromHsl(h: int, s: int, l: int, a: int = 255) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromHsl(int h, int s, int l, int a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromHsl

    Parameters
    ----------

    h : int
      Passed on as it is.

    s : int
      Passed on as it is.

    l : int
      Passed on as it is.

    a : int
      Passed on as it is. May be left out, as in Qt: it is then 255.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromHsl(int h, int s, int l, int a)
    address = Rituals.call('ritual_ZN6QColor7fromHslEiiii', h, s, l, a)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(float, float, float)
  @overload(float, float, float, float)
  def fromHslF(h: float, s: float, l: float, a: float = 1.0) -> QColor:
    """
    Calls Qt's 'QColor QColor::fromHslF(float h, float s, float l, float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#fromHslF

    Parameters
    ----------

    h : float
      Passed on as it is.

    s : float
      Passed on as it is.

    l : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::fromHslF(float h, float s, float l, float a)
    address = Rituals.call('ritual_ZN6QColor8fromHslFEffff', h, s, l, a)
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(str)
  def isValidColor(name: str) -> bool:
    """
    Calls Qt's 'bool QColor::isValidColor(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#isValidColor

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QColor::isValidColor(const QString &name)
    return Rituals.call('ritual_ZN6QColor12isValidColorERK7QString', name)

  @staticmethod
  @overload(str)
  def isValidColorName(a0: str) -> bool:
    """
    Calls Qt's 'bool QColor::isValidColorName(QAnyStringView a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#isValidColorName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QColor::isValidColorName(QAnyStringView a0)
    return Rituals.call(
        'ritual_ZN6QColor16isValidColorNameE14QAnyStringView', a0,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColor'

  #  Qt's '~QColor()'. Naming it makes this a value class: Python owns every
  #  C++ QColor behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QColorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QColor::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#isValid
    """
    #  bool QColor::isValid() const
    return self.uglySide.call('ritual_ZNK6QColor7isValidEv')

  @overload()
  @overload(NameFormat)
  def name(self, format: NameFormat = NameFormat.HexRgb) -> str:
    """
    Calls Qt's 'QString QColor::name(NameFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#name

    Parameters
    ----------

    format : NameFormat
      Passed on as its number. May be left out, as in Qt: it is then
      NameFormat.HexRgb.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QColor::name(NameFormat format) const
    return self.uglySide.call(
        'ritual_ZNK6QColor4nameENS_10NameFormatE', format.value,
    )

  def spec(self) -> Spec:
    """
    Calls Qt's 'Spec QColor::spec() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#spec

    Returns
    -------

    Spec
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Spec(number)' gives.
    """
    #  Spec QColor::spec() const
    return Spec(self.uglySide.call('ritual_ZNK6QColor4specEv'))

  def alpha(self) -> int:
    """
    Calls Qt's 'int QColor::alpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#alpha
    """
    #  int QColor::alpha() const
    return self.uglySide.call('ritual_ZNK6QColor5alphaEv')

  def alphaF(self) -> float:
    """
    Calls Qt's 'float QColor::alphaF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#alphaF
    """
    #  float QColor::alphaF() const
    return self.uglySide.call('ritual_ZNK6QColor6alphaFEv')

  def red(self) -> int:
    """
    Calls Qt's 'int QColor::red() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#red
    """
    #  int QColor::red() const
    return self.uglySide.call('ritual_ZNK6QColor3redEv')

  def green(self) -> int:
    """
    Calls Qt's 'int QColor::green() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#green
    """
    #  int QColor::green() const
    return self.uglySide.call('ritual_ZNK6QColor5greenEv')

  def blue(self) -> int:
    """
    Calls Qt's 'int QColor::blue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#blue
    """
    #  int QColor::blue() const
    return self.uglySide.call('ritual_ZNK6QColor4blueEv')

  def redF(self) -> float:
    """
    Calls Qt's 'float QColor::redF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#redF
    """
    #  float QColor::redF() const
    return self.uglySide.call('ritual_ZNK6QColor4redFEv')

  def greenF(self) -> float:
    """
    Calls Qt's 'float QColor::greenF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#greenF
    """
    #  float QColor::greenF() const
    return self.uglySide.call('ritual_ZNK6QColor6greenFEv')

  def blueF(self) -> float:
    """
    Calls Qt's 'float QColor::blueF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#blueF
    """
    #  float QColor::blueF() const
    return self.uglySide.call('ritual_ZNK6QColor5blueFEv')

  def rgba64(self) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QColor::rgba64() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#rgba64

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QColor::rgba64() const
    address = self.uglySide.call('ritual_ZNK6QColor6rgba64Ev')
    return QRgba64._cuteOwning(address)

  def rgba(self) -> int:
    """
    Calls Qt's 'QRgb QColor::rgba() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#rgba
    """
    #  QRgb QColor::rgba() const
    return self.uglySide.call('ritual_ZNK6QColor4rgbaEv')

  def rgb(self) -> int:
    """
    Calls Qt's 'QRgb QColor::rgb() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#rgb
    """
    #  QRgb QColor::rgb() const
    return self.uglySide.call('ritual_ZNK6QColor3rgbEv')

  def hue(self) -> int:
    """
    Calls Qt's 'int QColor::hue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hue
    """
    #  int QColor::hue() const
    return self.uglySide.call('ritual_ZNK6QColor3hueEv')

  def saturation(self) -> int:
    """
    Calls Qt's 'int QColor::saturation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#saturation
    """
    #  int QColor::saturation() const
    return self.uglySide.call('ritual_ZNK6QColor10saturationEv')

  def hsvHue(self) -> int:
    """
    Calls Qt's 'int QColor::hsvHue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hsvHue
    """
    #  int QColor::hsvHue() const
    return self.uglySide.call('ritual_ZNK6QColor6hsvHueEv')

  def hsvSaturation(self) -> int:
    """
    Calls Qt's 'int QColor::hsvSaturation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hsvSaturation
    """
    #  int QColor::hsvSaturation() const
    return self.uglySide.call('ritual_ZNK6QColor13hsvSaturationEv')

  def value(self) -> int:
    """
    Calls Qt's 'int QColor::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#value
    """
    #  int QColor::value() const
    return self.uglySide.call('ritual_ZNK6QColor5valueEv')

  def hueF(self) -> float:
    """
    Calls Qt's 'float QColor::hueF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hueF
    """
    #  float QColor::hueF() const
    return self.uglySide.call('ritual_ZNK6QColor4hueFEv')

  def saturationF(self) -> float:
    """
    Calls Qt's 'float QColor::saturationF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#saturationF
    """
    #  float QColor::saturationF() const
    return self.uglySide.call('ritual_ZNK6QColor11saturationFEv')

  def hsvHueF(self) -> float:
    """
    Calls Qt's 'float QColor::hsvHueF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hsvHueF
    """
    #  float QColor::hsvHueF() const
    return self.uglySide.call('ritual_ZNK6QColor7hsvHueFEv')

  def hsvSaturationF(self) -> float:
    """
    Calls Qt's 'float QColor::hsvSaturationF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hsvSaturationF
    """
    #  float QColor::hsvSaturationF() const
    return self.uglySide.call('ritual_ZNK6QColor14hsvSaturationFEv')

  def valueF(self) -> float:
    """
    Calls Qt's 'float QColor::valueF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#valueF
    """
    #  float QColor::valueF() const
    return self.uglySide.call('ritual_ZNK6QColor6valueFEv')

  def cyan(self) -> int:
    """
    Calls Qt's 'int QColor::cyan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#cyan
    """
    #  int QColor::cyan() const
    return self.uglySide.call('ritual_ZNK6QColor4cyanEv')

  def magenta(self) -> int:
    """
    Calls Qt's 'int QColor::magenta() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#magenta
    """
    #  int QColor::magenta() const
    return self.uglySide.call('ritual_ZNK6QColor7magentaEv')

  def yellow(self) -> int:
    """
    Calls Qt's 'int QColor::yellow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#yellow
    """
    #  int QColor::yellow() const
    return self.uglySide.call('ritual_ZNK6QColor6yellowEv')

  def black(self) -> int:
    """
    Calls Qt's 'int QColor::black() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#black
    """
    #  int QColor::black() const
    return self.uglySide.call('ritual_ZNK6QColor5blackEv')

  def cyanF(self) -> float:
    """
    Calls Qt's 'float QColor::cyanF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#cyanF
    """
    #  float QColor::cyanF() const
    return self.uglySide.call('ritual_ZNK6QColor5cyanFEv')

  def magentaF(self) -> float:
    """
    Calls Qt's 'float QColor::magentaF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#magentaF
    """
    #  float QColor::magentaF() const
    return self.uglySide.call('ritual_ZNK6QColor8magentaFEv')

  def yellowF(self) -> float:
    """
    Calls Qt's 'float QColor::yellowF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#yellowF
    """
    #  float QColor::yellowF() const
    return self.uglySide.call('ritual_ZNK6QColor7yellowFEv')

  def blackF(self) -> float:
    """
    Calls Qt's 'float QColor::blackF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#blackF
    """
    #  float QColor::blackF() const
    return self.uglySide.call('ritual_ZNK6QColor6blackFEv')

  def hslHue(self) -> int:
    """
    Calls Qt's 'int QColor::hslHue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hslHue
    """
    #  int QColor::hslHue() const
    return self.uglySide.call('ritual_ZNK6QColor6hslHueEv')

  def hslSaturation(self) -> int:
    """
    Calls Qt's 'int QColor::hslSaturation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hslSaturation
    """
    #  int QColor::hslSaturation() const
    return self.uglySide.call('ritual_ZNK6QColor13hslSaturationEv')

  def lightness(self) -> int:
    """
    Calls Qt's 'int QColor::lightness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#lightness
    """
    #  int QColor::lightness() const
    return self.uglySide.call('ritual_ZNK6QColor9lightnessEv')

  def hslHueF(self) -> float:
    """
    Calls Qt's 'float QColor::hslHueF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hslHueF
    """
    #  float QColor::hslHueF() const
    return self.uglySide.call('ritual_ZNK6QColor7hslHueFEv')

  def hslSaturationF(self) -> float:
    """
    Calls Qt's 'float QColor::hslSaturationF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#hslSaturationF
    """
    #  float QColor::hslSaturationF() const
    return self.uglySide.call('ritual_ZNK6QColor14hslSaturationFEv')

  def lightnessF(self) -> float:
    """
    Calls Qt's 'float QColor::lightnessF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#lightnessF
    """
    #  float QColor::lightnessF() const
    return self.uglySide.call('ritual_ZNK6QColor10lightnessFEv')

  def toRgb(self) -> QColor:
    """
    Calls Qt's 'QColor QColor::toRgb() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#toRgb

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::toRgb() const
    address = self.uglySide.call('ritual_ZNK6QColor5toRgbEv')
    return QColor._cuteOwning(address)

  def toHsv(self) -> QColor:
    """
    Calls Qt's 'QColor QColor::toHsv() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#toHsv

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::toHsv() const
    address = self.uglySide.call('ritual_ZNK6QColor5toHsvEv')
    return QColor._cuteOwning(address)

  def toCmyk(self) -> QColor:
    """
    Calls Qt's 'QColor QColor::toCmyk() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#toCmyk

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::toCmyk() const
    address = self.uglySide.call('ritual_ZNK6QColor6toCmykEv')
    return QColor._cuteOwning(address)

  def toHsl(self) -> QColor:
    """
    Calls Qt's 'QColor QColor::toHsl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#toHsl

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::toHsl() const
    address = self.uglySide.call('ritual_ZNK6QColor5toHslEv')
    return QColor._cuteOwning(address)

  def toExtendedRgb(self) -> QColor:
    """
    Calls Qt's 'QColor QColor::toExtendedRgb() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#toExtendedRgb

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::toExtendedRgb() const
    address = self.uglySide.call('ritual_ZNK6QColor13toExtendedRgbEv')
    return QColor._cuteOwning(address)

  @overload(Spec)
  def convertTo(self, colorSpec: Spec) -> QColor:
    """
    Calls Qt's 'QColor QColor::convertTo(Spec colorSpec) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#convertTo

    Parameters
    ----------

    colorSpec : Spec
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::convertTo(Spec colorSpec) const
    address = self.uglySide.call(
        'ritual_ZNK6QColor9convertToENS_4SpecE', colorSpec.value,
    )
    return QColor._cuteOwning(address)

  @overload()
  @overload(int)
  def lighter(self, f: int = 150) -> QColor:
    """
    Calls Qt's 'QColor QColor::lighter(int f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#lighter

    Parameters
    ----------

    f : int
      Passed on as it is. May be left out, as in Qt: it is then 150.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::lighter(int f) const
    address = self.uglySide.call('ritual_ZNK6QColor7lighterEi', f)
    return QColor._cuteOwning(address)

  @overload()
  @overload(int)
  def darker(self, f: int = 200) -> QColor:
    """
    Calls Qt's 'QColor QColor::darker(int f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#darker

    Parameters
    ----------

    f : int
      Passed on as it is. May be left out, as in Qt: it is then 200.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColor::darker(int f) const
    address = self.uglySide.call('ritual_ZNK6QColor6darkerEi', f)
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setNamedColor(self, name: str) -> None:
    """
    Calls Qt's 'void QColor::setNamedColor(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setNamedColor

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QColor::setNamedColor(const QString &name)
    self.uglySide.call('ritual_ZN6QColor13setNamedColorERK7QString', name)

  @overload(int)
  def setAlpha(self, alpha: int) -> None:
    """
    Calls Qt's 'void QColor::setAlpha(int alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setAlpha

    Parameters
    ----------

    alpha : int
      Passed on as it is.
    """
    #  void QColor::setAlpha(int alpha)
    self.uglySide.call('ritual_ZN6QColor8setAlphaEi', alpha)

  @overload(float)
  def setAlphaF(self, alpha: float) -> None:
    """
    Calls Qt's 'void QColor::setAlphaF(float alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setAlphaF

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QColor::setAlphaF(float alpha)
    self.uglySide.call('ritual_ZN6QColor9setAlphaFEf', alpha)

  @overload(int)
  def setRed(self, red: int) -> None:
    """
    Calls Qt's 'void QColor::setRed(int red)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setRed

    Parameters
    ----------

    red : int
      Passed on as it is.
    """
    #  void QColor::setRed(int red)
    self.uglySide.call('ritual_ZN6QColor6setRedEi', red)

  @overload(int)
  def setGreen(self, green: int) -> None:
    """
    Calls Qt's 'void QColor::setGreen(int green)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setGreen

    Parameters
    ----------

    green : int
      Passed on as it is.
    """
    #  void QColor::setGreen(int green)
    self.uglySide.call('ritual_ZN6QColor8setGreenEi', green)

  @overload(int)
  def setBlue(self, blue: int) -> None:
    """
    Calls Qt's 'void QColor::setBlue(int blue)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setBlue

    Parameters
    ----------

    blue : int
      Passed on as it is.
    """
    #  void QColor::setBlue(int blue)
    self.uglySide.call('ritual_ZN6QColor7setBlueEi', blue)

  @overload(float)
  def setRedF(self, red: float) -> None:
    """
    Calls Qt's 'void QColor::setRedF(float red)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setRedF

    Parameters
    ----------

    red : float
      Passed on as it is.
    """
    #  void QColor::setRedF(float red)
    self.uglySide.call('ritual_ZN6QColor7setRedFEf', red)

  @overload(float)
  def setGreenF(self, green: float) -> None:
    """
    Calls Qt's 'void QColor::setGreenF(float green)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setGreenF

    Parameters
    ----------

    green : float
      Passed on as it is.
    """
    #  void QColor::setGreenF(float green)
    self.uglySide.call('ritual_ZN6QColor9setGreenFEf', green)

  @overload(float)
  def setBlueF(self, blue: float) -> None:
    """
    Calls Qt's 'void QColor::setBlueF(float blue)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setBlueF

    Parameters
    ----------

    blue : float
      Passed on as it is.
    """
    #  void QColor::setBlueF(float blue)
    self.uglySide.call('ritual_ZN6QColor8setBlueFEf', blue)

  @overload(int, int, int)
  @overload(int, int, int, int)
  def setRgb(self, r: int, g: int, b: int, a: int = 255) -> None:
    """
    Calls Qt's 'void QColor::setRgb(int r, int g, int b, int a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setRgb

    Parameters
    ----------

    r : int
      Passed on as it is.

    g : int
      Passed on as it is.

    b : int
      Passed on as it is.

    a : int
      Passed on as it is. May be left out, as in Qt: it is then 255.
    """
    #  void QColor::setRgb(int r, int g, int b, int a)
    self.uglySide.call('ritual_ZN6QColor6setRgbEiiii', r, g, b, a)

  @overload(int)
  def setRgb(self, rgb: int) -> None:
    """
    Calls Qt's 'void QColor::setRgb(QRgb rgb)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setRgb

    Parameters
    ----------

    rgb : int
      Passed on as it is.
    """
    #  void QColor::setRgb(QRgb rgb)
    self.uglySide.call('ritual_ZN6QColor6setRgbEj', rgb)

  @overload(float, float, float)
  @overload(float, float, float, float)
  def setRgbF(self, r: float, g: float, b: float, a: float = 1.0) -> None:
    """
    Calls Qt's 'void QColor::setRgbF(float r, float g, float b, float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setRgbF

    Parameters
    ----------

    r : float
      Passed on as it is.

    g : float
      Passed on as it is.

    b : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  void QColor::setRgbF(float r, float g, float b, float a)
    self.uglySide.call('ritual_ZN6QColor7setRgbFEffff', r, g, b, a)

  @overload(QRgba64)
  def setRgba64(self, rgba: QRgba64) -> None:
    """
    Calls Qt's 'void QColor::setRgba64(QRgba64 rgba)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setRgba64

    Parameters
    ----------

    rgba : QRgba64
      Passed on as a value: Qt reads the C++ QRgba64, which stays Python's
      own.
    """
    #  void QColor::setRgba64(QRgba64 rgba)
    self.uglySide.call(
        'ritual_ZN6QColor9setRgba64E7QRgba64', self._valueOf(rgba),
    )

  @overload(int)
  def setRgba(self, rgba: int) -> None:
    """
    Calls Qt's 'void QColor::setRgba(QRgb rgba)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setRgba

    Parameters
    ----------

    rgba : int
      Passed on as it is.
    """
    #  void QColor::setRgba(QRgb rgba)
    self.uglySide.call('ritual_ZN6QColor7setRgbaEj', rgba)

  @overload(int, int, int)
  @overload(int, int, int, int)
  def setHsv(self, h: int, s: int, v: int, a: int = 255) -> None:
    """
    Calls Qt's 'void QColor::setHsv(int h, int s, int v, int a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setHsv

    Parameters
    ----------

    h : int
      Passed on as it is.

    s : int
      Passed on as it is.

    v : int
      Passed on as it is.

    a : int
      Passed on as it is. May be left out, as in Qt: it is then 255.
    """
    #  void QColor::setHsv(int h, int s, int v, int a)
    self.uglySide.call('ritual_ZN6QColor6setHsvEiiii', h, s, v, a)

  @overload(float, float, float)
  @overload(float, float, float, float)
  def setHsvF(self, h: float, s: float, v: float, a: float = 1.0) -> None:
    """
    Calls Qt's 'void QColor::setHsvF(float h, float s, float v, float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setHsvF

    Parameters
    ----------

    h : float
      Passed on as it is.

    s : float
      Passed on as it is.

    v : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  void QColor::setHsvF(float h, float s, float v, float a)
    self.uglySide.call('ritual_ZN6QColor7setHsvFEffff', h, s, v, a)

  @overload(int, int, int, int)
  @overload(int, int, int, int, int)
  def setCmyk(self, c: int, m: int, y: int, k: int, a: int = 255) -> None:
    """
    Calls Qt's 'void QColor::setCmyk(int c, int m, int y, int k, int a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setCmyk

    Parameters
    ----------

    c : int
      Passed on as it is.

    m : int
      Passed on as it is.

    y : int
      Passed on as it is.

    k : int
      Passed on as it is.

    a : int
      Passed on as it is. May be left out, as in Qt: it is then 255.
    """
    #  void QColor::setCmyk(int c, int m, int y, int k, int a)
    self.uglySide.call('ritual_ZN6QColor7setCmykEiiiii', c, m, y, k, a)

  @overload(float, float, float, float)
  @overload(float, float, float, float, float)
  def setCmykF(
      self,
      c: float,
      m: float,
      y: float,
      k: float,
      a: float = 1.0,
  ) -> None:
    """
    Calls Qt's 'void QColor::setCmykF(float c, float m, float y, float k,
    float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setCmykF

    Parameters
    ----------

    c : float
      Passed on as it is.

    m : float
      Passed on as it is.

    y : float
      Passed on as it is.

    k : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  void QColor::setCmykF(float c, float m, float y, float k, float a)
    self.uglySide.call('ritual_ZN6QColor8setCmykFEfffff', c, m, y, k, a)

  @overload(int, int, int)
  @overload(int, int, int, int)
  def setHsl(self, h: int, s: int, l: int, a: int = 255) -> None:
    """
    Calls Qt's 'void QColor::setHsl(int h, int s, int l, int a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setHsl

    Parameters
    ----------

    h : int
      Passed on as it is.

    s : int
      Passed on as it is.

    l : int
      Passed on as it is.

    a : int
      Passed on as it is. May be left out, as in Qt: it is then 255.
    """
    #  void QColor::setHsl(int h, int s, int l, int a)
    self.uglySide.call('ritual_ZN6QColor6setHslEiiii', h, s, l, a)

  @overload(float, float, float)
  @overload(float, float, float, float)
  def setHslF(self, h: float, s: float, l: float, a: float = 1.0) -> None:
    """
    Calls Qt's 'void QColor::setHslF(float h, float s, float l, float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#setHslF

    Parameters
    ----------

    h : float
      Passed on as it is.

    s : float
      Passed on as it is.

    l : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  void QColor::setHslF(float h, float s, float l, float a)
    self.uglySide.call('ritual_ZN6QColor7setHslFEffff', h, s, l, a)

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
    Notes what was given, for Qt's 'QColor::QColor()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#QColor
    """
    #  QColor::QColor()
    self._noteCreation(QColor, lambda: Rituals.call('ritual_ZN6QColorC1Ev'))

  @overload(Qt.GlobalColor)
  def __init__(self, color: Qt.GlobalColor) -> None:
    """
    Notes what was given, for Qt's 'QColor::QColor(Qt::GlobalColor color)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#QColor

    Parameters
    ----------

    color : Qt.GlobalColor
      Passed on as its number.
    """
    #  QColor::QColor(Qt::GlobalColor color)
    self._noteCreation(QColor, lambda: Rituals.call(
        'ritual_ZN6QColorC1EN2Qt11GlobalColorE', color.value,
    ))

  @overload(int, int, int)
  @overload(int, int, int, int)
  def __init__(self, r: int, g: int, b: int, a: int = 255) -> None:
    """
    Notes what was given, for Qt's 'QColor::QColor(int r, int g, int b, int
    a)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#QColor

    Parameters
    ----------

    r : int
      Passed on as it is.

    g : int
      Passed on as it is.

    b : int
      Passed on as it is.

    a : int
      Passed on as it is. May be left out, as in Qt: it is then 255.
    """
    #  QColor::QColor(int r, int g, int b, int a)
    self._noteCreation(QColor, lambda: Rituals.call(
        'ritual_ZN6QColorC1Eiiii', r, g, b, a,
    ))

  @overload(int)
  def __init__(self, rgb: int) -> None:
    """
    Notes what was given, for Qt's 'QColor::QColor(QRgb rgb)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#QColor

    Parameters
    ----------

    rgb : int
      Passed on as it is.
    """
    #  QColor::QColor(QRgb rgb)
    self._noteCreation(QColor, lambda: Rituals.call(
        'ritual_ZN6QColorC1Ej', rgb,
    ))

  @overload(QRgba64)
  def __init__(self, rgba64: QRgba64) -> None:
    """
    Notes what was given, for Qt's 'QColor::QColor(QRgba64 rgba64)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#QColor

    Parameters
    ----------

    rgba64 : QRgba64
      Passed on as a value: Qt reads the C++ QRgba64, which stays Python's
      own.
    """
    #  QColor::QColor(QRgba64 rgba64)
    self._noteCreation(QColor, lambda: Rituals.call(
        'ritual_ZN6QColorC1E7QRgba64', self._valueOf(rgba64),
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QColor::QColor(const QString &name)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#QColor

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QColor::QColor(const QString &name)
    self._noteCreation(QColor, lambda: Rituals.call(
        'ritual_ZN6QColorC1ERK7QString', name,
    ))

  @overload(NoneType)
  def __init__(self, aname: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QColor::QColor(const char *aname)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#QColor

    Parameters
    ----------

    aname : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QColor::QColor(const char *aname)
    self._noteCreation(QColor, lambda: Rituals.call(
        'ritual_ZN6QColorC1EPKc', self._bytesOf(aname),
    ))

  @overload(Spec)
  def __init__(self, spec: Spec) -> None:
    """
    Notes what was given, for Qt's 'QColor::QColor(Spec spec)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#QColor

    Parameters
    ----------

    spec : Spec
      Passed on as its number.
    """
    #  QColor::QColor(Spec spec)
    self._noteCreation(QColor, lambda: Rituals.call(
        'ritual_ZN6QColorC1ENS_4SpecE', spec.value,
    ))

  @overload(Spec, int, int, int, int)
  @overload(Spec, int, int, int, int, int)
  def __init__(
      self,
      spec: Spec,
      a1: int,
      a2: int,
      a3: int,
      a4: int,
      a5: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColor::QColor(Spec spec, ushort a1,
    ushort a2, ushort a3, ushort a4, ushort a5)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolor.html#QColor

    Parameters
    ----------

    spec : Spec
      Passed on as its number.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : int
      Passed on as it is.

    a4 : int
      Passed on as it is.

    a5 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QColor::QColor(Spec spec, ushort a1, ushort a2, ushort a3, ushort a4,
    #      ushort a5)
    self._noteCreation(QColor, lambda: Rituals.call(
        'ritual_ZN6QColorC1ENS_4SpecEttttt', spec.value, a1, a2, a3, a4, a5,
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
