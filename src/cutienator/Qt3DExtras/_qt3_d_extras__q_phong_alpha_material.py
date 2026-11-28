"""
Qt3DExtras::QPhongAlphaMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qphongalphamaterial.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPhongAlphaMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QPhongAlphaMaterial: a plain Python
  object standing in front of one C++ Qt3DExtras::QPhongAlphaMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QPhongAlphaMaterial is built on Qt's Qt3DRender::QMaterial, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QPhongAlphaMaterial that has a ritual
  and that Python can call so far, 33 names in all: 'metaObject', 'tr',
  'ambient', 'diffuse', 'specular', 'shininess', 'alpha', 'sourceRgbArg',
  'destinationRgbArg', 'sourceAlphaArg', 'destinationAlphaArg',
  'blendFunctionArg', 'setAmbient', 'setDiffuse', 'setSpecular',
  'setShininess', 'setAlpha', 'setSourceRgbArg', 'setDestinationRgbArg',
  'setSourceAlphaArg', 'setDestinationAlphaArg', 'setBlendFunctionArg',
  'ambientChanged', 'diffuseChanged', 'specularChanged', 'shininessChanged',
  'alphaChanged', 'sourceRgbArgChanged', 'destinationRgbArgChanged',
  'sourceAlphaArgChanged', 'destinationAlphaArgChanged',
  'blendFunctionArgChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QPhongAlphaMaterial::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QPhongAlphaMaterial::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QPhongAlphaMaterial::~QPhongAlphaMaterial()': the
    destructor: Python never removes a C++ Qt3DExtras::QPhongAlphaMaterial.
  - Qt's 'const QPhongAlphaMaterialPrivate
    *Qt3DExtras::QPhongAlphaMaterial::d_func() const': takes in Python what
    'QPhongAlphaMaterialPrivate *Qt3DExtras::QPhongAlphaMaterial::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 40 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QPhongAlphaMaterial is created at the first use, not
    by 'Qt3DExtras::QPhongAlphaMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QPhongAlphaMaterial.
  - Qt tells when it has removed the C++ Qt3DExtras::QPhongAlphaMaterial.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QPhongAlphaMaterial::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QPhongAlphaMaterial::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QPhongAlphaMaterial'

  #  A C++ Qt3DExtras::QPhongAlphaMaterial Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QPhongAlphaMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DExtras::QPhongAlphaMaterial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QPhongAlphaMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ambient(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QPhongAlphaMaterial::ambient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#ambient

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QPhongAlphaMaterial::ambient() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial7ambientEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def diffuse(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QPhongAlphaMaterial::diffuse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#diffuse

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QPhongAlphaMaterial::diffuse() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial7diffuseEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def specular(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QPhongAlphaMaterial::specular() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#specular

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QPhongAlphaMaterial::specular() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial8specularEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def shininess(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QPhongAlphaMaterial::shininess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#shininess
    """
    #  float Qt3DExtras::QPhongAlphaMaterial::shininess() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial9shininessEv',
    )

  def alpha(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QPhongAlphaMaterial::alpha() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#alpha
    """
    #  float Qt3DExtras::QPhongAlphaMaterial::alpha() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial5alphaEv',
    )

  def sourceRgbArg(self) -> Qt3DRender.QBlendEquationArguments.Blending:
    """
    Calls Qt's 'Qt3DRender::QBlendEquationArguments::Blending
    Qt3DExtras::QPhongAlphaMaterial::sourceRgbArg() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#sourceRgbArg

    Returns
    -------

    Qt3DRender.QBlendEquationArguments.Blending
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QBlendEquationArguments.Blending(number)' gives.
    """
    #  Qt3DRender::QBlendEquationArguments::Blending
    #      Qt3DExtras::QPhongAlphaMaterial::sourceRgbArg() const
    return Qt3DRender.QBlendEquationArguments.Blending(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial12sourceRgbArgEv',
    ))

  def destinationRgbArg(self) -> Qt3DRender.QBlendEquationArguments.Blending:
    """
    Calls Qt's 'Qt3DRender::QBlendEquationArguments::Blending
    Qt3DExtras::QPhongAlphaMaterial::destinationRgbArg() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Returns
    -------

    Qt3DRender.QBlendEquationArguments.Blending
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QBlendEquationArguments.Blending(number)' gives.
    """
    #  Qt3DRender::QBlendEquationArguments::Blending
    #      Qt3DExtras::QPhongAlphaMaterial::destinationRgbArg() const
    return Qt3DRender.QBlendEquationArguments.Blending(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial17destinationRgbArgEv',
    ))

  def sourceAlphaArg(self) -> Qt3DRender.QBlendEquationArguments.Blending:
    """
    Calls Qt's 'Qt3DRender::QBlendEquationArguments::Blending
    Qt3DExtras::QPhongAlphaMaterial::sourceAlphaArg() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#sourceAlphaArg

    Returns
    -------

    Qt3DRender.QBlendEquationArguments.Blending
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QBlendEquationArguments.Blending(number)' gives.
    """
    #  Qt3DRender::QBlendEquationArguments::Blending
    #      Qt3DExtras::QPhongAlphaMaterial::sourceAlphaArg() const
    return Qt3DRender.QBlendEquationArguments.Blending(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial14sourceAlphaArgEv',
    ))

  def destinationAlphaArg(
      self,
  ) -> Qt3DRender.QBlendEquationArguments.Blending:
    """
    Calls Qt's 'Qt3DRender::QBlendEquationArguments::Blending
    Qt3DExtras::QPhongAlphaMaterial::destinationAlphaArg() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Returns
    -------

    Qt3DRender.QBlendEquationArguments.Blending
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QBlendEquationArguments.Blending(number)' gives.
    """
    #  Qt3DRender::QBlendEquationArguments::Blending
    #      Qt3DExtras::QPhongAlphaMaterial::destinationAlphaArg() const
    return Qt3DRender.QBlendEquationArguments.Blending(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial19destinationAlphaArgEv',
    ))

  def blendFunctionArg(self) -> Qt3DRender.QBlendEquation.BlendFunction:
    """
    Calls Qt's 'Qt3DRender::QBlendEquation::BlendFunction
    Qt3DExtras::QPhongAlphaMaterial::blendFunctionArg() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Returns
    -------

    Qt3DRender.QBlendEquation.BlendFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QBlendEquation.BlendFunction(number)' gives.
    """
    #  Qt3DRender::QBlendEquation::BlendFunction
    #      Qt3DExtras::QPhongAlphaMaterial::blendFunctionArg() const
    return Qt3DRender.QBlendEquation.BlendFunction(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial16blendFunctionArgEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setAmbient(self, ambient: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::setAmbient(const QColor
    &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#setAmbient

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setAmbient(const QColor
    #      &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial10setAmbientERK6QColor',
        self._valueOf(ambient),
    )

  @overload(QColor)
  def setDiffuse(self, diffuse: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::setDiffuse(const QColor
    &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#setDiffuse

    Parameters
    ----------

    diffuse : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setDiffuse(const QColor
    #      &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial10setDiffuseERK6QColor',
        self._valueOf(diffuse),
    )

  @overload(QColor)
  def setSpecular(self, specular: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::setSpecular(const
    QColor &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#setSpecular

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setSpecular(const QColor
    #      &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial11setSpecularERK6QColor',
        self._valueOf(specular),
    )

  @overload(float)
  def setShininess(self, shininess: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::setShininess(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#setShininess

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setShininess(float shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial12setShininessEf',
        shininess,
    )

  @overload(float)
  def setAlpha(self, alpha: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::setAlpha(float alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#setAlpha

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setAlpha(float alpha)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial8setAlphaEf', alpha,
    )

  @overload(Qt3DRender.QBlendEquationArguments.Blending)
  def setSourceRgbArg(
      self,
      sourceRgbArg: Qt3DRender.QBlendEquationArguments.Blending,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::setSourceRgbArg(Qt3DRender::
    QBlendEquationArguments::Blending sourceRgbArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    sourceRgbArg : Qt3DRender.QBlendEquationArguments.Blending
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setSourceRgbArg(Qt3DRender::
    #      QBlendEquationArguments::Blending sourceRgbArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial15setSourceRgbArgEN10Qt3'
        'DRender23QBlendEquationArguments8BlendingE',
        sourceRgbArg.value,
    )

  @overload(Qt3DRender.QBlendEquationArguments.Blending)
  def setDestinationRgbArg(
      self,
      destinationRgbArg: Qt3DRender.QBlendEquationArguments.Blending,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::setDestinationRgbArg(Qt3DRender::
    QBlendEquationArguments::Blending destinationRgbArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    destinationRgbArg : Qt3DRender.QBlendEquationArguments.Blending
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setDestinationRgbArg(
    #      Qt3DRender::QBlendEquationArguments::Blending destinationRgbArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial20setDestinationRgbArgEN'
        '10Qt3DRender23QBlendEquationArguments8BlendingE',
        destinationRgbArg.value,
    )

  @overload(Qt3DRender.QBlendEquationArguments.Blending)
  def setSourceAlphaArg(
      self,
      sourceAlphaArg: Qt3DRender.QBlendEquationArguments.Blending,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::setSourceAlphaArg(Qt3DRender::
    QBlendEquationArguments::Blending sourceAlphaArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    sourceAlphaArg : Qt3DRender.QBlendEquationArguments.Blending
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setSourceAlphaArg(Qt3DRender::
    #      QBlendEquationArguments::Blending sourceAlphaArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial17setSourceAlphaArgEN10Q'
        't3DRender23QBlendEquationArguments8BlendingE',
        sourceAlphaArg.value,
    )

  @overload(Qt3DRender.QBlendEquationArguments.Blending)
  def setDestinationAlphaArg(
      self,
      destinationAlphaArg: Qt3DRender.QBlendEquationArguments.Blending,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::setDestinationAlphaArg(Qt3DRender::
    QBlendEquationArguments::Blending destinationAlphaArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    destinationAlphaArg : Qt3DRender.QBlendEquationArguments.Blending
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setDestinationAlphaArg(
    #      Qt3DRender::QBlendEquationArguments::Blending destinationAlphaArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial22setDestinationAlphaArg'
        'EN10Qt3DRender23QBlendEquationArguments8BlendingE',
        destinationAlphaArg.value,
    )

  @overload(Qt3DRender.QBlendEquation.BlendFunction)
  def setBlendFunctionArg(
      self,
      blendFunctionArg: Qt3DRender.QBlendEquation.BlendFunction,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::setBlendFunctionArg(Qt3DRender::
    QBlendEquation::BlendFunction blendFunctionArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    blendFunctionArg : Qt3DRender.QBlendEquation.BlendFunction
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::setBlendFunctionArg(Qt3DRender::
    #      QBlendEquation::BlendFunction blendFunctionArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial19setBlendFunctionArgEN1'
        '0Qt3DRender14QBlendEquation13BlendFunctionE',
        blendFunctionArg.value,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QPhongAlphaMaterial::QPhongAlphaMaterial(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QPhongAlphaMaterial::QPhongAlphaMaterial(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QPhongAlphaMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterialC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(QColor)
  def ambientChanged(self, ambient: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::ambientChanged(const
    QColor &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#ambientChanged

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::ambientChanged(const QColor
    #      &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial14ambientChangedERK6QCol'
        'or',
        self._valueOf(ambient),
    )

  @overload(QColor)
  def diffuseChanged(self, diffuse: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::diffuseChanged(const
    QColor &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#diffuseChanged

    Parameters
    ----------

    diffuse : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::diffuseChanged(const QColor
    #      &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial14diffuseChangedERK6QCol'
        'or',
        self._valueOf(diffuse),
    )

  @overload(QColor)
  def specularChanged(self, specular: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::specularChanged(const
    QColor &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::specularChanged(const QColor
    #      &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial15specularChangedERK6QCo'
        'lor',
        self._valueOf(specular),
    )

  @overload(float)
  def shininessChanged(self, shininess: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::shininessChanged(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::shininessChanged(float
    #      shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial16shininessChangedEf',
        shininess,
    )

  @overload(float)
  def alphaChanged(self, alpha: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongAlphaMaterial::alphaChanged(float
    alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#alphaChanged

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::alphaChanged(float alpha)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial12alphaChangedEf', alpha,
    )

  @overload(Qt3DRender.QBlendEquationArguments.Blending)
  def sourceRgbArgChanged(
      self,
      sourceRgbArg: Qt3DRender.QBlendEquationArguments.Blending,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::sourceRgbArgChanged(Qt3DRender::
    QBlendEquationArguments::Blending sourceRgbArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    sourceRgbArg : Qt3DRender.QBlendEquationArguments.Blending
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::sourceRgbArgChanged(Qt3DRender::
    #      QBlendEquationArguments::Blending sourceRgbArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial19sourceRgbArgChangedEN1'
        '0Qt3DRender23QBlendEquationArguments8BlendingE',
        sourceRgbArg.value,
    )

  @overload(Qt3DRender.QBlendEquationArguments.Blending)
  def destinationRgbArgChanged(
      self,
      destinationRgbArg: Qt3DRender.QBlendEquationArguments.Blending,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::destinationRgbArgChanged(Qt3DRender::
    QBlendEquationArguments::Blending destinationRgbArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    destinationRgbArg : Qt3DRender.QBlendEquationArguments.Blending
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::destinationRgbArgChanged(
    #      Qt3DRender::QBlendEquationArguments::Blending destinationRgbArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial24destinationRgbArgChang'
        'edEN10Qt3DRender23QBlendEquationArguments8BlendingE',
        destinationRgbArg.value,
    )

  @overload(Qt3DRender.QBlendEquationArguments.Blending)
  def sourceAlphaArgChanged(
      self,
      sourceAlphaArg: Qt3DRender.QBlendEquationArguments.Blending,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::sourceAlphaArgChanged(Qt3DRender::
    QBlendEquationArguments::Blending sourceAlphaArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    sourceAlphaArg : Qt3DRender.QBlendEquationArguments.Blending
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::sourceAlphaArgChanged(
    #      Qt3DRender::QBlendEquationArguments::Blending sourceAlphaArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial21sourceAlphaArgChangedE'
        'N10Qt3DRender23QBlendEquationArguments8BlendingE',
        sourceAlphaArg.value,
    )

  @overload(Qt3DRender.QBlendEquationArguments.Blending)
  def destinationAlphaArgChanged(
      self,
      destinationAlphaArg: Qt3DRender.QBlendEquationArguments.Blending,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::destinationAlphaArgChanged(Qt3DRender::
    QBlendEquationArguments::Blending destinationAlphaArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    destinationAlphaArg : Qt3DRender.QBlendEquationArguments.Blending
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::destinationAlphaArgChanged(
    #      Qt3DRender::QBlendEquationArguments::Blending destinationAlphaArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial26destinationAlphaArgCha'
        'ngedEN10Qt3DRender23QBlendEquationArguments8BlendingE',
        destinationAlphaArg.value,
    )

  @overload(Qt3DRender.QBlendEquation.BlendFunction)
  def blendFunctionArgChanged(
      self,
      blendFunctionArg: Qt3DRender.QBlendEquation.BlendFunction,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QPhongAlphaMaterial::blendFunctionArgChanged(Qt3DRender::
    QBlendEquation::BlendFunction blendFunctionArg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html

    Parameters
    ----------

    blendFunctionArg : Qt3DRender.QBlendEquation.BlendFunction
      Passed on as its number.
    """
    #  void Qt3DExtras::QPhongAlphaMaterial::blendFunctionArgChanged(
    #      Qt3DRender::QBlendEquation::BlendFunction blendFunctionArg)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial23blendFunctionArgChange'
        'dEN10Qt3DRender14QBlendEquation13BlendFunctionE',
        blendFunctionArg.value,
    )

  def d_func(self) -> Optional[Qt3DExtras.QPhongAlphaMaterialPrivate]:
    """
    Calls Qt's 'QPhongAlphaMaterialPrivate
    *Qt3DExtras::QPhongAlphaMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongalphamaterial.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QPhongAlphaMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPhongAlphaMaterialPrivate *Qt3DExtras::QPhongAlphaMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QPhongAlphaMaterial6d_funcEv',
    )
    return Qt3DExtras.QPhongAlphaMaterialPrivate._cuteAt(address)
