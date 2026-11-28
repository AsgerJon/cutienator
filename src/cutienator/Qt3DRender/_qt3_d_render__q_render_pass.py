"""
Qt3DRender::QRenderPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qrenderpass.h, Qt 6.12.0. Changes made here are lost.
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


class QRenderPass(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QRenderPass: a plain Python object
  standing in front of one C++ Qt3DRender::QRenderPass.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DRender::QRenderPass
  is built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderPass that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr',
  'shaderProgram', 'addFilterKey', 'removeFilterKey', 'addRenderState',
  'removeRenderState', 'addParameter', 'removeParameter', 'setShaderProgram',
  'shaderProgramChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QRenderPass::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QRenderPass::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QRenderPass::~QRenderPass()': the destructor: Python
    never removes a C++ Qt3DRender::QRenderPass.
  - Qt's 'QList<QFilterKey *> Qt3DRender::QRenderPass::filterKeys() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<QRenderState *> Qt3DRender::QRenderPass::renderStates()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<QParameter *> Qt3DRender::QRenderPass::parameters() const':
    gives a type Python has no way to take yet.
  - Qt's 'Qt3DRender::QRenderPass::QRenderPass(QRenderPassPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QRenderPassPrivate *Qt3DRender::QRenderPass::d_func() const':
    takes in Python what 'QRenderPassPrivate
    *Qt3DRender::QRenderPass::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderPass is created at the first use, not by
    'Qt3DRender::QRenderPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderPass.
  - Qt tells when it has removed the C++ Qt3DRender::QRenderPass. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QRenderPass that has no cute function yet,
    'filterKeys', 'parameters', 'renderStates', holds a function that raises
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
    Calls Qt's 'QString Qt3DRender::QRenderPass::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#tr

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
    #  QString Qt3DRender::QRenderPass::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender11QRenderPass2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderPass'

  #  A C++ Qt3DRender::QRenderPass Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderPass'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QRenderPass::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QRenderPass::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QRenderPass10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shaderProgram(self) -> Optional[Qt3DRender.QShaderProgram]:
    """
    Calls Qt's 'QShaderProgram *Qt3DRender::QRenderPass::shaderProgram()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#shaderProgram

    Returns
    -------

    Optional[Qt3DRender.QShaderProgram]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShaderProgram *Qt3DRender::QRenderPass::shaderProgram() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QRenderPass13shaderProgramEv',
    )
    return Qt3DRender.QShaderProgram._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QShaderProgram'])
  @overload(NoneType)
  def setShaderProgram(
      self,
      shaderProgram: Optional[Qt3DRender.QShaderProgram],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderPass::setShaderProgram(QShaderProgram
    *shaderProgram)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#setShaderProgram

    Parameters
    ----------

    shaderProgram : Optional[Qt3DRender.QShaderProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderPass::setShaderProgram(QShaderProgram
    #      *shaderProgram)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QRenderPass16setShaderProgramEPNS_14QShader'
        'ProgramE',
        self._addressOf(shaderProgram),
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
    'Qt3DRender::QRenderPass::QRenderPass(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#QRenderPass

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRenderPass::QRenderPass(Qt3DCore::QNode *parent)
    self._noteCreation(QRenderPass, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender11QRenderPassC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DRender.QFilterKey'])
  @overload(NoneType)
  def addFilterKey(self, filterKey: Optional[Qt3DRender.QFilterKey]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderPass::addFilterKey(QFilterKey
    *filterKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#addFilterKey

    Parameters
    ----------

    filterKey : Optional[Qt3DRender.QFilterKey]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderPass::addFilterKey(QFilterKey *filterKey)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QRenderPass12addFilterKeyEPNS_10QFilterKeyE',
        self._addressOf(filterKey),
    )

  @overload(WAIT['Qt3DRender.QFilterKey'])
  @overload(NoneType)
  def removeFilterKey(
      self,
      filterKey: Optional[Qt3DRender.QFilterKey],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderPass::removeFilterKey(QFilterKey
    *filterKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#removeFilterKey

    Parameters
    ----------

    filterKey : Optional[Qt3DRender.QFilterKey]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderPass::removeFilterKey(QFilterKey *filterKey)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QRenderPass15removeFilterKeyEPNS_10QFilterK'
        'eyE',
        self._addressOf(filterKey),
    )

  @overload(WAIT['Qt3DRender.QRenderState'])
  @overload(NoneType)
  def addRenderState(self, state: Optional[Qt3DRender.QRenderState]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderPass::addRenderState(QRenderState
    *state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#addRenderState

    Parameters
    ----------

    state : Optional[Qt3DRender.QRenderState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderPass::addRenderState(QRenderState *state)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QRenderPass14addRenderStateEPNS_12QRenderSt'
        'ateE',
        self._addressOf(state),
    )

  @overload(WAIT['Qt3DRender.QRenderState'])
  @overload(NoneType)
  def removeRenderState(
      self,
      state: Optional[Qt3DRender.QRenderState],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderPass::removeRenderState(QRenderState
    *state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#removeRenderState

    Parameters
    ----------

    state : Optional[Qt3DRender.QRenderState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderPass::removeRenderState(QRenderState *state)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QRenderPass17removeRenderStateEPNS_12QRende'
        'rStateE',
        self._addressOf(state),
    )

  @overload(WAIT['Qt3DRender.QParameter'])
  @overload(NoneType)
  def addParameter(self, p: Optional[Qt3DRender.QParameter]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderPass::addParameter(QParameter *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#addParameter

    Parameters
    ----------

    p : Optional[Qt3DRender.QParameter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderPass::addParameter(QParameter *p)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QRenderPass12addParameterEPNS_10QParameterE',
        self._addressOf(p),
    )

  @overload(WAIT['Qt3DRender.QParameter'])
  @overload(NoneType)
  def removeParameter(self, p: Optional[Qt3DRender.QParameter]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderPass::removeParameter(QParameter
    *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#removeParameter

    Parameters
    ----------

    p : Optional[Qt3DRender.QParameter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderPass::removeParameter(QParameter *p)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QRenderPass15removeParameterEPNS_10QParamet'
        'erE',
        self._addressOf(p),
    )

  @overload(WAIT['Qt3DRender.QShaderProgram'])
  @overload(NoneType)
  def shaderProgramChanged(
      self,
      shaderProgram: Optional[Qt3DRender.QShaderProgram],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderPass::shaderProgramChanged(QShaderProgram
    *shaderProgram)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#shaderProgramChanged

    Parameters
    ----------

    shaderProgram : Optional[Qt3DRender.QShaderProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderPass::shaderProgramChanged(QShaderProgram
    #      *shaderProgram)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QRenderPass20shaderProgramChangedEPNS_14QSh'
        'aderProgramE',
        self._addressOf(shaderProgram),
    )

  def d_func(self) -> Optional[Qt3DRender.QRenderPassPrivate]:
    """
    Calls Qt's 'QRenderPassPrivate *Qt3DRender::QRenderPass::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qrenderpass.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QRenderPassPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderPassPrivate *Qt3DRender::QRenderPass::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender11QRenderPass6d_funcEv',
    )
    return Qt3DRender.QRenderPassPrivate._cuteAt(address)

  @staticmethod
  def filterKeys(*__, **_) -> Never:
    """
    Qt's 'QList<QFilterKey *> Qt3DRender::QRenderPass::filterKeys() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QRenderPass.filterKeys' has no cute function yet. Qt's "
        "'QList<QFilterKey *> Qt3DRender::QRenderPass::filterKeys() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QList<QParameter *> Qt3DRender::QRenderPass::parameters() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QRenderPass.parameters' has no cute function yet. Qt's "
        "'QList<QParameter *> Qt3DRender::QRenderPass::parameters() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def renderStates(*__, **_) -> Never:
    """
    Qt's 'QList<QRenderState *> Qt3DRender::QRenderPass::renderStates()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QRenderPass.renderStates' has no cute function yet. "
        "Qt's 'QList<QRenderState *> "
        "Qt3DRender::QRenderPass::renderStates() const': gives a type "
        "Python has no way to take yet.")
