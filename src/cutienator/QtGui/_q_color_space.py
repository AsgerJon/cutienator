"""
QColorSpace binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qcolorspace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QColorSpaceColorModel, QColorSpaceNamedColorSpace
from . import QColorSpacePrimaries, QColorSpacePrimaryPoints
from . import QColorSpaceTransferFunction, QColorSpaceTransformModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray, QPointF
  from . import QColorTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QPointF = WAIT['QPointF']


class QColorSpace(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorSpace: a plain Python object standing in front
  of one C++ QColorSpace.

  C++ hands a QColorSpace around as a copy, so every C++ QColorSpace behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorSpace that has a ritual and that Python can
  call so far, 20 names in all: 'primaries', 'transferFunction', 'gamma',
  'description', 'setDescription', 'setTransferFunction',
  'withTransferFunction', 'setPrimaries', 'setWhitePoint', 'whitePoint',
  'setPrimaryPoints', 'primaryPoints', 'transformModel', 'colorModel',
  'detach', 'isValid', 'isValidTarget', 'fromIccProfile', 'iccProfile',
  'transformationToColorSpace'. It can be made from Python, in 8 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorSpace::~QColorSpace()': the destructor: Python removes its
    C++ QColorSpace by it, and has no other use for it.
  - Qt's 'QVariant QColorSpace::operator QVariant() const': an operator,
    which is not reflected yet.

  What has no ritual
  ------------------

  16 of the 47 functions Qt declares: 12 takes or gives a type that cannot be
  passed yet; 2 private; 1 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QColorSpace is created at the first use, not by
    'QColorSpace(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorSpace back gives a copy the ritual made for
    Python, in a new cute QColorSpace.
  """

  #  The classes Qt writes inside QColorSpace.
  PrimaryPoints = QColorSpacePrimaryPoints

  #  The enums Qt writes inside QColorSpace, and the names Qt has for the
  #  combinations of its flags enums.
  ColorModel = QColorSpaceColorModel
  NamedColorSpace = QColorSpaceNamedColorSpace
  Primaries = QColorSpacePrimaries
  TransferFunction = QColorSpaceTransferFunction
  TransformModel = QColorSpaceTransformModel

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray)
  def fromIccProfile(iccProfile: QByteArray) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace QColorSpace::fromIccProfile(const QByteArray
    &iccProfile)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#fromIccProfile

    Parameters
    ----------

    iccProfile : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QColorSpace::fromIccProfile(const QByteArray &iccProfile)
    address = Rituals.call(
        'ritual_ZN11QColorSpace14fromIccProfileERK10QByteArray',
        CuteMixin._valueOf(iccProfile),
    )
    return QColorSpace._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorSpace'

  #  Qt's '~QColorSpace()'. Naming it makes this a value class: Python owns
  #  every C++ QColorSpace behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QColorSpaceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def primaries(self) -> Primaries:
    """
    Calls Qt's 'Primaries QColorSpace::primaries() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#primaries

    Returns
    -------

    Primaries
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Primaries(number)' gives.
    """
    #  Primaries QColorSpace::primaries() const
    return QColorSpace.Primaries(self.uglySide.call(
        'ritual_ZNK11QColorSpace9primariesEv',
    ))

  def transferFunction(self) -> TransferFunction:
    """
    Calls Qt's 'TransferFunction QColorSpace::transferFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#transferFunction

    Returns
    -------

    TransferFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransferFunction(number)'
      gives.
    """
    #  TransferFunction QColorSpace::transferFunction() const
    return QColorSpace.TransferFunction(self.uglySide.call(
        'ritual_ZNK11QColorSpace16transferFunctionEv',
    ))

  def gamma(self) -> float:
    """
    Calls Qt's 'float QColorSpace::gamma() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#gamma
    """
    #  float QColorSpace::gamma() const
    return self.uglySide.call('ritual_ZNK11QColorSpace5gammaEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QColorSpace::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QColorSpace::description() const
    return self.uglySide.call('ritual_ZNK11QColorSpace11descriptionEv')

  @overload(TransferFunction)
  @overload(TransferFunction, float)
  def withTransferFunction(
      self,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace
    QColorSpace::withTransferFunction(TransferFunction transferFunction,
    float gamma) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspace.html#withTransferFunction

    Parameters
    ----------

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QColorSpace::withTransferFunction(TransferFunction
    #      transferFunction, float gamma) const
    address = self.uglySide.call(
        'ritual_ZNK11QColorSpace20withTransferFunctionENS_16TransferFunctio'
        'nEf',
        transferFunction.value, gamma,
    )
    return QColorSpace._cuteOwning(address)

  def whitePoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QColorSpace::whitePoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#whitePoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QColorSpace::whitePoint() const
    address = self.uglySide.call('ritual_ZNK11QColorSpace10whitePointEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def primaryPoints(self) -> PrimaryPoints:
    """
    Calls Qt's 'PrimaryPoints QColorSpace::primaryPoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#primaryPoints

    Returns
    -------

    PrimaryPoints
      A new cute QColorSpace::PrimaryPoints around the copy Qt gave back.
      Python owns it.
    """
    #  PrimaryPoints QColorSpace::primaryPoints() const
    address = self.uglySide.call('ritual_ZNK11QColorSpace13primaryPointsEv')
    return QColorSpacePrimaryPoints._cuteOwning(address)

  def transformModel(self) -> TransformModel:
    """
    Calls Qt's 'TransformModel QColorSpace::transformModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#transformModel

    Returns
    -------

    TransformModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransformModel(number)'
      gives.
    """
    #  TransformModel QColorSpace::transformModel() const
    return QColorSpace.TransformModel(self.uglySide.call(
        'ritual_ZNK11QColorSpace14transformModelEv',
    ))

  def colorModel(self) -> ColorModel:
    """
    Calls Qt's 'ColorModel QColorSpace::colorModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#colorModel

    Returns
    -------

    ColorModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorModel(number)'
      gives.
    """
    #  ColorModel QColorSpace::colorModel() const
    return QColorSpace.ColorModel(self.uglySide.call(
        'ritual_ZNK11QColorSpace10colorModelEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QColorSpace::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#isValid
    """
    #  bool QColorSpace::isValid() const
    return self.uglySide.call('ritual_ZNK11QColorSpace7isValidEv')

  def isValidTarget(self) -> bool:
    """
    Calls Qt's 'bool QColorSpace::isValidTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#isValidTarget
    """
    #  bool QColorSpace::isValidTarget() const
    return self.uglySide.call('ritual_ZNK11QColorSpace13isValidTargetEv')

  def iccProfile(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QColorSpace::iccProfile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#iccProfile

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QColorSpace::iccProfile() const
    address = self.uglySide.call('ritual_ZNK11QColorSpace10iccProfileEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(THIS)
  def transformationToColorSpace(
      self,
      colorspace: QColorSpace,
  ) -> QColorTransform:
    """
    Calls Qt's 'QColorTransform QColorSpace::transformationToColorSpace(const
    QColorSpace &colorspace) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspace.html#transformationToColorSpace

    Parameters
    ----------

    colorspace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.

    Returns
    -------

    QColorTransform
      A new cute QColorTransform around the copy Qt gave back. Python owns
      it.
    """
    #  QColorTransform QColorSpace::transformationToColorSpace(const
    #      QColorSpace &colorspace) const
    address = self.uglySide.call(
        'ritual_ZNK11QColorSpace26transformationToColorSpaceERKS_',
        self._valueOf(colorspace),
    )
    from . import QColorTransform
    return QColorTransform._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QColorSpace::setDescription(const QString
    &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QColorSpace::setDescription(const QString &description)
    self.uglySide.call(
        'ritual_ZN11QColorSpace14setDescriptionERK7QString', description,
    )

  @overload(TransferFunction)
  @overload(TransferFunction, float)
  def setTransferFunction(
      self,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Calls Qt's 'void QColorSpace::setTransferFunction(TransferFunction
    transferFunction, float gamma)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspace.html#setTransferFunction

    Parameters
    ----------

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QColorSpace::setTransferFunction(TransferFunction
    #      transferFunction, float gamma)
    self.uglySide.call(
        'ritual_ZN11QColorSpace19setTransferFunctionENS_16TransferFunctionE'
        'f',
        transferFunction.value, gamma,
    )

  @overload(Primaries)
  def setPrimaries(self, primariesId: Primaries) -> None:
    """
    Calls Qt's 'void QColorSpace::setPrimaries(Primaries primariesId)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setPrimaries

    Parameters
    ----------

    primariesId : Primaries
      Passed on as its number.
    """
    #  void QColorSpace::setPrimaries(Primaries primariesId)
    self.uglySide.call(
        'ritual_ZN11QColorSpace12setPrimariesENS_9PrimariesE',
        primariesId.value,
    )

  @overload(QPointF, QPointF, QPointF, QPointF)
  def setPrimaries(
      self,
      whitePoint: QPointF,
      redPoint: QPointF,
      greenPoint: QPointF,
      bluePoint: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QColorSpace::setPrimaries(const QPointF &whitePoint,
    const QPointF &redPoint, const QPointF &greenPoint, const QPointF
    &bluePoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setPrimaries

    Parameters
    ----------

    whitePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    redPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    greenPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    bluePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QColorSpace::setPrimaries(const QPointF &whitePoint, const
    #      QPointF &redPoint, const QPointF &greenPoint, const QPointF
    #      &bluePoint)
    self.uglySide.call(
        'ritual_ZN11QColorSpace12setPrimariesERK7QPointFS2_S2_S2_',
        self._valueOf(whitePoint), self._valueOf(redPoint),
        self._valueOf(greenPoint), self._valueOf(bluePoint),
    )

  @overload(QPointF)
  def setWhitePoint(self, whitePoint: QPointF) -> None:
    """
    Calls Qt's 'void QColorSpace::setWhitePoint(QPointF whitePoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setWhitePoint

    Parameters
    ----------

    whitePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QColorSpace::setWhitePoint(QPointF whitePoint)
    self.uglySide.call(
        'ritual_ZN11QColorSpace13setWhitePointE7QPointF',
        self._valueOf(whitePoint),
    )

  @overload(PrimaryPoints)
  def setPrimaryPoints(self, primaryPoints: PrimaryPoints) -> None:
    """
    Calls Qt's 'void QColorSpace::setPrimaryPoints(const PrimaryPoints
    &primaryPoints)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setPrimaryPoints

    Parameters
    ----------

    primaryPoints : PrimaryPoints
      Passed on as a value: Qt reads the C++ QColorSpace::PrimaryPoints,
      which stays Python's own.
    """
    #  void QColorSpace::setPrimaryPoints(const PrimaryPoints &primaryPoints)
    self.uglySide.call(
        'ritual_ZN11QColorSpace16setPrimaryPointsERKNS_13PrimaryPointsE',
        self._valueOf(primaryPoints),
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
    Notes what was given, for Qt's 'QColorSpace::QColorSpace()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace
    """
    #  QColorSpace::QColorSpace()
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1Ev',
    ))

  @overload(NamedColorSpace)
  def __init__(self, namedColorSpace: NamedColorSpace) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(NamedColorSpace
    namedColorSpace)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    namedColorSpace : NamedColorSpace
      Passed on as its number.
    """
    #  QColorSpace::QColorSpace(NamedColorSpace namedColorSpace)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ENS_15NamedColorSpaceE',
        namedColorSpace.value,
    ))

  @overload(QPointF, TransferFunction)
  @overload(QPointF, TransferFunction, float)
  def __init__(
      self,
      whitePoint: QPointF,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(QPointF
    whitePoint, TransferFunction transferFunction, float gamma)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    whitePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QColorSpace::QColorSpace(QPointF whitePoint, TransferFunction
    #      transferFunction, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1E7QPointFNS_16TransferFunctionEf',
        self._valueOf(whitePoint), transferFunction.value, gamma,
    ))

  @overload(Primaries, TransferFunction)
  @overload(Primaries, TransferFunction, float)
  def __init__(
      self,
      primaries: Primaries,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(Primaries
    primaries, TransferFunction transferFunction, float gamma)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    primaries : Primaries
      Passed on as its number.

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QColorSpace::QColorSpace(Primaries primaries, TransferFunction
    #      transferFunction, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ENS_9PrimariesENS_16TransferFunctionEf',
        primaries.value, transferFunction.value, gamma,
    ))

  @overload(Primaries, float)
  def __init__(self, primaries: Primaries, gamma: float) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(Primaries
    primaries, float gamma)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    primaries : Primaries
      Passed on as its number.

    gamma : float
      Passed on as it is.
    """
    #  QColorSpace::QColorSpace(Primaries primaries, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ENS_9PrimariesEf', primaries.value, gamma,
    ))

  @overload(QPointF, QPointF, QPointF, QPointF, TransferFunction)
  @overload(QPointF, QPointF, QPointF, QPointF, TransferFunction, float)
  def __init__(
      self,
      whitePoint: QPointF,
      redPoint: QPointF,
      greenPoint: QPointF,
      bluePoint: QPointF,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(const QPointF
    &whitePoint, const QPointF &redPoint, const QPointF &greenPoint, const
    QPointF &bluePoint, TransferFunction transferFunction, float gamma)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    whitePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    redPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    greenPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    bluePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QColorSpace::QColorSpace(const QPointF &whitePoint, const QPointF
    #      &redPoint, const QPointF &greenPoint, const QPointF &bluePoint,
    #      TransferFunction transferFunction, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ERK7QPointFS2_S2_S2_NS_16TransferFunctionE'
        'f',
        self._valueOf(whitePoint), self._valueOf(redPoint),
        self._valueOf(greenPoint), self._valueOf(bluePoint),
        transferFunction.value, gamma,
    ))

  @overload(PrimaryPoints, TransferFunction)
  @overload(PrimaryPoints, TransferFunction, float)
  def __init__(
      self,
      primaryPoints: PrimaryPoints,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(const
    PrimaryPoints &primaryPoints, TransferFunction transferFunction, float
    gamma)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    primaryPoints : PrimaryPoints
      Passed on as a value: Qt reads the C++ QColorSpace::PrimaryPoints,
      which stays Python's own.

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QColorSpace::QColorSpace(const PrimaryPoints &primaryPoints,
    #      TransferFunction transferFunction, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ERKNS_13PrimaryPointsENS_16TransferFunctio'
        'nEf',
        self._valueOf(primaryPoints), transferFunction.value, gamma,
    ))

  @overload(THIS)
  def __init__(self, colorSpace: QColorSpace) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(const
    QColorSpace &colorSpace)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  QColorSpace::QColorSpace(const QColorSpace &colorSpace)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ERKS_', self._valueOf(colorSpace),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QColorSpace::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#detach
    """
    #  void QColorSpace::detach()
    self.uglySide.call('ritual_ZN11QColorSpace6detachEv')
