"""
QPinchGesture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGesture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPinchGesture(QGesture):
  """
  The cute side of Qt's QPinchGesture: a plain Python object standing in
  front of one C++ QPinchGesture.

  It is built on the cute 'QGesture', as Qt's QPinchGesture is built on Qt's
  QGesture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPinchGesture that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'totalChangeFlags',
  'setTotalChangeFlags', 'changeFlags', 'setChangeFlags', 'startCenterPoint',
  'lastCenterPoint', 'centerPoint', 'setStartCenterPoint',
  'setLastCenterPoint', 'setCenterPoint', 'totalScaleFactor',
  'lastScaleFactor', 'scaleFactor', 'setTotalScaleFactor',
  'setLastScaleFactor', 'setScaleFactor', 'totalRotationAngle',
  'lastRotationAngle', 'rotationAngle', 'setTotalRotationAngle',
  'setLastRotationAngle', 'setRotationAngle'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPinchGesture::~QPinchGesture()': the destructor: Python never
    removes a C++ QPinchGesture.

  What has no ritual
  ------------------

  6 of the 32 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QPinchGesture is created at the first use, not by
    'QPinchGesture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPinchGesture.
  - Qt tells when it has removed the C++ QPinchGesture. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPinchGesture, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ChangeFlag(CuteFlags):
    """
    The flags enum 'QPinchGesture::ChangeFlag' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QPinchGesture::ChangeFlags'.
    """

    ScaleFactorChanged = 0x1
    RotationAngleChanged = 0x2
    CenterPointChanged = 0x4

  ChangeFlags = ChangeFlag

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
    Calls Qt's 'QString QPinchGesture::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#tr

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
    #  QString QPinchGesture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QPinchGesture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPinchGesture'

  #  A C++ QPinchGesture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPinchGesture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPinchGesture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPinchGesture::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QPinchGesture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def totalChangeFlags(self) -> ChangeFlags:
    """
    Calls Qt's 'ChangeFlags QPinchGesture::totalChangeFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#totalChangeFlags

    Returns
    -------

    ChangeFlags
      The value standing for the combination Qt gave back.
    """
    #  ChangeFlags QPinchGesture::totalChangeFlags() const
    return QPinchGesture.ChangeFlags(self.uglySide.call(
        'ritual_ZNK13QPinchGesture16totalChangeFlagsEv',
    ))

  def changeFlags(self) -> ChangeFlags:
    """
    Calls Qt's 'ChangeFlags QPinchGesture::changeFlags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#changeFlags

    Returns
    -------

    ChangeFlags
      The value standing for the combination Qt gave back.
    """
    #  ChangeFlags QPinchGesture::changeFlags() const
    return QPinchGesture.ChangeFlags(self.uglySide.call(
        'ritual_ZNK13QPinchGesture11changeFlagsEv',
    ))

  def startCenterPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPinchGesture::startCenterPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#startCenterPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPinchGesture::startCenterPoint() const
    address = self.uglySide.call(
        'ritual_ZNK13QPinchGesture16startCenterPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastCenterPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPinchGesture::lastCenterPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#lastCenterPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPinchGesture::lastCenterPoint() const
    address = self.uglySide.call(
        'ritual_ZNK13QPinchGesture15lastCenterPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def centerPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPinchGesture::centerPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#centerPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPinchGesture::centerPoint() const
    address = self.uglySide.call('ritual_ZNK13QPinchGesture11centerPointEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def totalScaleFactor(self) -> float:
    """
    Calls Qt's 'qreal QPinchGesture::totalScaleFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#totalScaleFactor
    """
    #  qreal QPinchGesture::totalScaleFactor() const
    return self.uglySide.call(
        'ritual_ZNK13QPinchGesture16totalScaleFactorEv',
    )

  def lastScaleFactor(self) -> float:
    """
    Calls Qt's 'qreal QPinchGesture::lastScaleFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#lastScaleFactor
    """
    #  qreal QPinchGesture::lastScaleFactor() const
    return self.uglySide.call('ritual_ZNK13QPinchGesture15lastScaleFactorEv')

  def scaleFactor(self) -> float:
    """
    Calls Qt's 'qreal QPinchGesture::scaleFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#scaleFactor
    """
    #  qreal QPinchGesture::scaleFactor() const
    return self.uglySide.call('ritual_ZNK13QPinchGesture11scaleFactorEv')

  def totalRotationAngle(self) -> float:
    """
    Calls Qt's 'qreal QPinchGesture::totalRotationAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#totalRotationAngle
    """
    #  qreal QPinchGesture::totalRotationAngle() const
    return self.uglySide.call(
        'ritual_ZNK13QPinchGesture18totalRotationAngleEv',
    )

  def lastRotationAngle(self) -> float:
    """
    Calls Qt's 'qreal QPinchGesture::lastRotationAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#lastRotationAngle
    """
    #  qreal QPinchGesture::lastRotationAngle() const
    return self.uglySide.call(
        'ritual_ZNK13QPinchGesture17lastRotationAngleEv',
    )

  def rotationAngle(self) -> float:
    """
    Calls Qt's 'qreal QPinchGesture::rotationAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#rotationAngle
    """
    #  qreal QPinchGesture::rotationAngle() const
    return self.uglySide.call('ritual_ZNK13QPinchGesture13rotationAngleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ChangeFlags)
  def setTotalChangeFlags(self, value: ChangeFlags) -> None:
    """
    Calls Qt's 'void QPinchGesture::setTotalChangeFlags(ChangeFlags value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#setTotalChangeFlags

    Parameters
    ----------

    value : ChangeFlags
      Passed on as its number.
    """
    #  void QPinchGesture::setTotalChangeFlags(ChangeFlags value)
    self.uglySide.call(
        'ritual_ZN13QPinchGesture19setTotalChangeFlagsE6QFlagsINS_10ChangeF'
        'lagEE',
        value.value,
    )

  @overload(ChangeFlags)
  def setChangeFlags(self, value: ChangeFlags) -> None:
    """
    Calls Qt's 'void QPinchGesture::setChangeFlags(ChangeFlags value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#setChangeFlags

    Parameters
    ----------

    value : ChangeFlags
      Passed on as its number.
    """
    #  void QPinchGesture::setChangeFlags(ChangeFlags value)
    self.uglySide.call(
        'ritual_ZN13QPinchGesture14setChangeFlagsE6QFlagsINS_10ChangeFlagEE',
        value.value,
    )

  @overload(QPointF)
  def setStartCenterPoint(self, value: QPointF) -> None:
    """
    Calls Qt's 'void QPinchGesture::setStartCenterPoint(const QPointF
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#setStartCenterPoint

    Parameters
    ----------

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPinchGesture::setStartCenterPoint(const QPointF &value)
    self.uglySide.call(
        'ritual_ZN13QPinchGesture19setStartCenterPointERK7QPointF',
        self._valueOf(value),
    )

  @overload(QPointF)
  def setLastCenterPoint(self, value: QPointF) -> None:
    """
    Calls Qt's 'void QPinchGesture::setLastCenterPoint(const QPointF
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#setLastCenterPoint

    Parameters
    ----------

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPinchGesture::setLastCenterPoint(const QPointF &value)
    self.uglySide.call(
        'ritual_ZN13QPinchGesture18setLastCenterPointERK7QPointF',
        self._valueOf(value),
    )

  @overload(QPointF)
  def setCenterPoint(self, value: QPointF) -> None:
    """
    Calls Qt's 'void QPinchGesture::setCenterPoint(const QPointF &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#setCenterPoint

    Parameters
    ----------

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPinchGesture::setCenterPoint(const QPointF &value)
    self.uglySide.call(
        'ritual_ZN13QPinchGesture14setCenterPointERK7QPointF',
        self._valueOf(value),
    )

  @overload(float)
  def setTotalScaleFactor(self, value: float) -> None:
    """
    Calls Qt's 'void QPinchGesture::setTotalScaleFactor(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#setTotalScaleFactor

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPinchGesture::setTotalScaleFactor(qreal value)
    self.uglySide.call(
        'ritual_ZN13QPinchGesture19setTotalScaleFactorEd', value,
    )

  @overload(float)
  def setLastScaleFactor(self, value: float) -> None:
    """
    Calls Qt's 'void QPinchGesture::setLastScaleFactor(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#setLastScaleFactor

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPinchGesture::setLastScaleFactor(qreal value)
    self.uglySide.call(
        'ritual_ZN13QPinchGesture18setLastScaleFactorEd', value,
    )

  @overload(float)
  def setScaleFactor(self, value: float) -> None:
    """
    Calls Qt's 'void QPinchGesture::setScaleFactor(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#setScaleFactor

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPinchGesture::setScaleFactor(qreal value)
    self.uglySide.call('ritual_ZN13QPinchGesture14setScaleFactorEd', value)

  @overload(float)
  def setTotalRotationAngle(self, value: float) -> None:
    """
    Calls Qt's 'void QPinchGesture::setTotalRotationAngle(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#setTotalRotationAngle

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPinchGesture::setTotalRotationAngle(qreal value)
    self.uglySide.call(
        'ritual_ZN13QPinchGesture21setTotalRotationAngleEd', value,
    )

  @overload(float)
  def setLastRotationAngle(self, value: float) -> None:
    """
    Calls Qt's 'void QPinchGesture::setLastRotationAngle(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#setLastRotationAngle

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPinchGesture::setLastRotationAngle(qreal value)
    self.uglySide.call(
        'ritual_ZN13QPinchGesture20setLastRotationAngleEd', value,
    )

  @overload(float)
  def setRotationAngle(self, value: float) -> None:
    """
    Calls Qt's 'void QPinchGesture::setRotationAngle(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpinchgesture.html#setRotationAngle

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPinchGesture::setRotationAngle(qreal value)
    self.uglySide.call('ritual_ZN13QPinchGesture16setRotationAngleEd', value)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QPinchGesture::QPinchGesture(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpinchgesture.html#QPinchGesture

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPinchGesture::QPinchGesture(QObject *parent)
    self._noteCreation(QPinchGesture, lambda: Rituals.call(
        'ritual_ZN13QPinchGestureC1EP7QObject', self._addressOf(parent),
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
