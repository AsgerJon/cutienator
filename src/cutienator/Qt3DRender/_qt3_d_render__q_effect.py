"""
Qt3DRender::QEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qeffect.h, Qt 6.12.0. Changes made here are lost.
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


class QEffect(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QEffect: a plain Python object standing
  in front of one C++ Qt3DRender::QEffect.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DRender::QEffect is
  built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QEffect that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'addParameter',
  'removeParameter', 'addTechnique', 'removeTechnique', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QEffect::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QEffect::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QEffect::~QEffect()': the destructor: Python never
    removes a C++ Qt3DRender::QEffect.
  - Qt's 'QList<QParameter *> Qt3DRender::QEffect::parameters() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<QTechnique *> Qt3DRender::QEffect::techniques() const': gives
    a type Python has no way to take yet.
  - Qt's 'Qt3DRender::QEffect::QEffect(QEffectPrivate &dd, Qt3DCore::QNode
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QEffectPrivate *Qt3DRender::QEffect::d_func() const': takes
    in Python what 'QEffectPrivate *Qt3DRender::QEffect::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QEffect is created at the first use, not by
    'Qt3DRender::QEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QEffect.
  - Qt tells when it has removed the C++ Qt3DRender::QEffect. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QEffect that has no cute function yet,
    'parameters', 'techniques', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DRender::QEffect::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qeffect.html#tr

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
    #  QString Qt3DRender::QEffect::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender7QEffect2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QEffect'

  #  A C++ Qt3DRender::QEffect Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QEffect::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qeffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QEffect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QEffect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload()
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QEffect::QEffect(Qt3DCore::QNode *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qeffect.html#QEffect

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QEffect::QEffect(Qt3DCore::QNode *parent)
    self._noteCreation(QEffect, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender7QEffectC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DRender::QEffect::addParameter(QParameter
    *parameter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qeffect.html#addParameter

    Parameters
    ----------

    parameter : Optional[Qt3DRender.QParameter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QEffect::addParameter(QParameter *parameter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QEffect12addParameterEPNS_10QParameterE',
        self._addressOf(parameter),
    )

  @overload(WAIT['Qt3DRender.QParameter'])
  @overload(NoneType)
  def removeParameter(
      self,
      parameter: Optional[Qt3DRender.QParameter],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QEffect::removeParameter(QParameter
    *parameter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qeffect.html#removeParameter

    Parameters
    ----------

    parameter : Optional[Qt3DRender.QParameter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QEffect::removeParameter(QParameter *parameter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QEffect15removeParameterEPNS_10QParameterE',
        self._addressOf(parameter),
    )

  @overload(WAIT['Qt3DRender.QTechnique'])
  @overload(NoneType)
  def addTechnique(self, t: Optional[Qt3DRender.QTechnique]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QEffect::addTechnique(QTechnique *t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qeffect.html#addTechnique

    Parameters
    ----------

    t : Optional[Qt3DRender.QTechnique]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QEffect::addTechnique(QTechnique *t)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QEffect12addTechniqueEPNS_10QTechniqueE',
        self._addressOf(t),
    )

  @overload(WAIT['Qt3DRender.QTechnique'])
  @overload(NoneType)
  def removeTechnique(self, t: Optional[Qt3DRender.QTechnique]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QEffect::removeTechnique(QTechnique *t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qeffect.html#removeTechnique

    Parameters
    ----------

    t : Optional[Qt3DRender.QTechnique]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QEffect::removeTechnique(QTechnique *t)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QEffect15removeTechniqueEPNS_10QTechniqueE',
        self._addressOf(t),
    )

  def d_func(self) -> Optional[Qt3DRender.QEffectPrivate]:
    """
    Calls Qt's 'QEffectPrivate *Qt3DRender::QEffect::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qeffect.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QEffectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEffectPrivate *Qt3DRender::QEffect::d_func()
    address = self.uglySide.call('ritual_ZN10Qt3DRender7QEffect6d_funcEv')
    return Qt3DRender.QEffectPrivate._cuteAt(address)

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QList<QParameter *> Qt3DRender::QEffect::parameters() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QEffect.parameters' has no cute function yet. Qt's "
        "'QList<QParameter *> Qt3DRender::QEffect::parameters() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def techniques(*__, **_) -> Never:
    """
    Qt's 'QList<QTechnique *> Qt3DRender::QEffect::techniques() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QEffect.techniques' has no cute function yet. Qt's "
        "'QList<QTechnique *> Qt3DRender::QEffect::techniques() const': "
        "gives a type Python has no way to take yet.")
