"""
Qt3DRender::QMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qmaterial.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMaterial(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QMaterial: a plain Python object standing
  in front of one C++ Qt3DRender::QMaterial.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QMaterial is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QMaterial that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'effect',
  'addParameter', 'removeParameter', 'setEffect', 'effectChanged', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QMaterial::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QMaterial::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QMaterial::~QMaterial()': the destructor: Python never
    removes a C++ Qt3DRender::QMaterial.
  - Qt's 'QList<QParameter *> Qt3DRender::QMaterial::parameters() const':
    gives a type Python has no way to take yet.
  - Qt's 'Qt3DRender::QMaterial::QMaterial(QMaterialPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QMaterialPrivate *Qt3DRender::QMaterial::d_func() const':
    takes in Python what 'QMaterialPrivate *Qt3DRender::QMaterial::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QMaterial is created at the first use, not by
    'Qt3DRender::QMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QMaterial.
  - Qt tells when it has removed the C++ Qt3DRender::QMaterial. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QMaterial that has no cute function yet,
    'parameters', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString Qt3DRender::QMaterial::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qmaterial.html#tr

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
    #  QString Qt3DRender::QMaterial::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender9QMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QMaterial'

  #  A C++ Qt3DRender::QMaterial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QMaterial::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender9QMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def effect(self) -> Optional[Qt3DRender.QEffect]:
    """
    Calls Qt's 'QEffect *Qt3DRender::QMaterial::effect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qmaterial.html#effect

    Returns
    -------

    Optional[Qt3DRender.QEffect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEffect *Qt3DRender::QMaterial::effect() const
    address = self.uglySide.call('ritual_ZNK10Qt3DRender9QMaterial6effectEv')
    return Qt3DRender.QEffect._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QEffect'])
  @overload(NoneType)
  def setEffect(self, effect: Optional[Qt3DRender.QEffect]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QMaterial::setEffect(QEffect *effect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmaterial.html#setEffect

    Parameters
    ----------

    effect : Optional[Qt3DRender.QEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QMaterial::setEffect(QEffect *effect)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QMaterial9setEffectEPNS_7QEffectE',
        self._addressOf(effect),
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
    'Qt3DRender::QMaterial::QMaterial(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmaterial.html#QMaterial

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QMaterial::QMaterial(Qt3DCore::QNode *parent)
    self._noteCreation(QMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender9QMaterialC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DRender.QParameter'])
  @overload(NoneType)
  def addParameter(self, parameter: Optional[Qt3DRender.QParameter]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QMaterial::addParameter(QParameter
    *parameter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmaterial.html#addParameter

    Parameters
    ----------

    parameter : Optional[Qt3DRender.QParameter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QMaterial::addParameter(QParameter *parameter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QMaterial12addParameterEPNS_10QParameterE',
        self._addressOf(parameter),
    )

  @overload(WAIT['Qt3DRender.QParameter'])
  @overload(NoneType)
  def removeParameter(
      self,
      parameter: Optional[Qt3DRender.QParameter],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QMaterial::removeParameter(QParameter
    *parameter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmaterial.html#removeParameter

    Parameters
    ----------

    parameter : Optional[Qt3DRender.QParameter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QMaterial::removeParameter(QParameter *parameter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QMaterial15removeParameterEPNS_10QParameterE',
        self._addressOf(parameter),
    )

  @overload(WAIT['Qt3DRender.QEffect'])
  @overload(NoneType)
  def effectChanged(self, effect: Optional[Qt3DRender.QEffect]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QMaterial::effectChanged(QEffect *effect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmaterial.html#effectChanged

    Parameters
    ----------

    effect : Optional[Qt3DRender.QEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QMaterial::effectChanged(QEffect *effect)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QMaterial13effectChangedEPNS_7QEffectE',
        self._addressOf(effect),
    )

  def d_func(self) -> Optional[Qt3DRender.QMaterialPrivate]:
    """
    Calls Qt's 'QMaterialPrivate *Qt3DRender::QMaterial::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qmaterial.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMaterialPrivate *Qt3DRender::QMaterial::d_func()
    address = self.uglySide.call('ritual_ZN10Qt3DRender9QMaterial6d_funcEv')
    return Qt3DRender.QMaterialPrivate._cuteAt(address)

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QList<QParameter *> Qt3DRender::QMaterial::parameters() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QMaterial.parameters' has no cute function yet. Qt's "
        "'QList<QParameter *> Qt3DRender::QMaterial::parameters() const': "
        "gives a type Python has no way to take yet.")
