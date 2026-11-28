"""
QQuick3DParticleDynamicBurst binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledynamicburst_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleDynamicBurst to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuick3DParticleEmitBurst

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleDynamicBurst(QQuick3DParticleEmitBurst):
  """
  The cute side of Qt's QQuick3DParticleDynamicBurst: a plain Python object
  standing in front of one C++ QQuick3DParticleDynamicBurst.

  It is built on the cute 'QQuick3DParticleEmitBurst', as Qt's
  QQuick3DParticleDynamicBurst is built on Qt's QQuick3DParticleEmitBurst,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleDynamicBurst that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'enabled', 'amountVariation', 'triggerMode', 'setEnabled',
  'setAmountVariation', 'setTriggerMode', 'enabledChanged',
  'amountVariationChanged', 'triggerModeChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleDynamicBurst::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleDynamicBurst::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleDynamicBurst is created at the first use, not by
    'QQuick3DParticleDynamicBurst(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleDynamicBurst.
  - Qt tells when it has removed the C++ QQuick3DParticleDynamicBurst. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DParticleDynamicBurst, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class TriggerMode(CuteNum):
    """
    The enum 'QQuick3DParticleDynamicBurst::TriggerMode' of Qt, with the 3
    names Qt gives in it.
    """

    TriggerTime = Kee[int](0)
    TriggerStart = Kee[int](1)
    TriggerEnd = Kee[int](2)

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
    Calls Qt's 'QString QQuick3DParticleDynamicBurst::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html#tr

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
    #  QString QQuick3DParticleDynamicBurst::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QQuick3DParticleDynamicBurst2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleDynamicBurst'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleDynamicBurst::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleDynamicBurst::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleDynamicBurst10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleDynamicBurst::enabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html#enabled
    """
    #  bool QQuick3DParticleDynamicBurst::enabled() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleDynamicBurst7enabledEv',
    )

  def amountVariation(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleDynamicBurst::amountVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html#amountVariation
    """
    #  int QQuick3DParticleDynamicBurst::amountVariation() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleDynamicBurst15amountVariationEv',
    )

  def triggerMode(self) -> TriggerMode:
    """
    Calls Qt's 'TriggerMode QQuick3DParticleDynamicBurst::triggerMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html#triggerMode

    Returns
    -------

    TriggerMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TriggerMode(number)'
      gives.
    """
    #  TriggerMode QQuick3DParticleDynamicBurst::triggerMode() const
    return QQuick3DParticleDynamicBurst.TriggerMode(self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleDynamicBurst11triggerModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleDynamicBurst::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleDynamicBurst::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleDynamicBurst10setEnabledEb', enabled,
    )

  @overload(int)
  def setAmountVariation(self, value: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleDynamicBurst::setAmountVariation(int
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QQuick3DParticleDynamicBurst::setAmountVariation(int value)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleDynamicBurst18setAmountVariationEi',
        value,
    )

  @overload(TriggerMode)
  def setTriggerMode(self, mode: TriggerMode) -> None:
    """
    Calls Qt's 'void QQuick3DParticleDynamicBurst::setTriggerMode(TriggerMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html#setTriggerMode

    Parameters
    ----------

    mode : TriggerMode
      Passed on as its number.
    """
    #  void QQuick3DParticleDynamicBurst::setTriggerMode(TriggerMode mode)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleDynamicBurst14setTriggerModeENS_11Trigg'
        'erModeE',
        mode.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleDynamicBurst::QQuick3DParticleDynamicBurst(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleDynamicBurst::QQuick3DParticleDynamicBurst(QObject
    #      *parent)
    self._noteCreation(QQuick3DParticleDynamicBurst, lambda: Rituals.call(
        'ritual_ZN28QQuick3DParticleDynamicBurstC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleDynamicBurst::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html#enabledChanged
    """
    #  void QQuick3DParticleDynamicBurst::enabledChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleDynamicBurst14enabledChangedEv',
    )

  def amountVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleDynamicBurst::amountVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html
    """
    #  void QQuick3DParticleDynamicBurst::amountVariationChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleDynamicBurst22amountVariationChangedEv',
    )

  def triggerModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleDynamicBurst::triggerModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticledynamicburst.html
    """
    #  void QQuick3DParticleDynamicBurst::triggerModeChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleDynamicBurst18triggerModeChangedEv',
    )
