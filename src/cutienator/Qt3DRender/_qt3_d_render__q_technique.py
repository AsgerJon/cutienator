"""
Qt3DRender::QTechnique binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qtechnique.h, Qt 6.12.0. Changes made here are lost.
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


class QTechnique(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QTechnique: a plain Python object
  standing in front of one C++ Qt3DRender::QTechnique.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DRender::QTechnique
  is built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QTechnique that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr',
  'addFilterKey', 'removeFilterKey', 'addParameter', 'removeParameter',
  'addRenderPass', 'removeRenderPass', 'graphicsApiFilter', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QTechnique::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QTechnique::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QTechnique::~QTechnique()': the destructor: Python
    never removes a C++ Qt3DRender::QTechnique.
  - Qt's 'QList<QFilterKey *> Qt3DRender::QTechnique::filterKeys() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<QParameter *> Qt3DRender::QTechnique::parameters() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<QRenderPass *> Qt3DRender::QTechnique::renderPasses() const':
    gives a type Python has no way to take yet.
  - Qt's 'const QGraphicsApiFilter
    *Qt3DRender::QTechnique::graphicsApiFilter() const': takes in Python what
    'QGraphicsApiFilter *Qt3DRender::QTechnique::graphicsApiFilter()' takes.
  - Qt's 'Qt3DRender::QTechnique::QTechnique(QTechniquePrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QTechniquePrivate *Qt3DRender::QTechnique::d_func() const':
    takes in Python what 'QTechniquePrivate
    *Qt3DRender::QTechnique::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QTechnique is created at the first use, not by
    'Qt3DRender::QTechnique(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QTechnique.
  - Qt tells when it has removed the C++ Qt3DRender::QTechnique. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QTechnique that has no cute function yet,
    'filterKeys', 'parameters', 'renderPasses', holds a function that raises
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
    Calls Qt's 'QString Qt3DRender::QTechnique::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qtechnique.html#tr

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
    #  QString Qt3DRender::QTechnique::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QTechnique2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QTechnique'

  #  A C++ Qt3DRender::QTechnique Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QTechnique'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QTechnique::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtechnique.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QTechnique::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QTechnique10metaObjectEv',
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
    'Qt3DRender::QTechnique::QTechnique(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtechnique.html#QTechnique

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QTechnique::QTechnique(Qt3DCore::QNode *parent)
    self._noteCreation(QTechnique, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QTechniqueC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DRender::QTechnique::addFilterKey(QFilterKey
    *filterKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtechnique.html#addFilterKey

    Parameters
    ----------

    filterKey : Optional[Qt3DRender.QFilterKey]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QTechnique::addFilterKey(QFilterKey *filterKey)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QTechnique12addFilterKeyEPNS_10QFilterKeyE',
        self._addressOf(filterKey),
    )

  @overload(WAIT['Qt3DRender.QFilterKey'])
  @overload(NoneType)
  def removeFilterKey(
      self,
      filterKey: Optional[Qt3DRender.QFilterKey],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTechnique::removeFilterKey(QFilterKey
    *filterKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtechnique.html#removeFilterKey

    Parameters
    ----------

    filterKey : Optional[Qt3DRender.QFilterKey]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QTechnique::removeFilterKey(QFilterKey *filterKey)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QTechnique15removeFilterKeyEPNS_10QFilterKe'
        'yE',
        self._addressOf(filterKey),
    )

  @overload(WAIT['Qt3DRender.QParameter'])
  @overload(NoneType)
  def addParameter(self, p: Optional[Qt3DRender.QParameter]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTechnique::addParameter(QParameter *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtechnique.html#addParameter

    Parameters
    ----------

    p : Optional[Qt3DRender.QParameter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QTechnique::addParameter(QParameter *p)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QTechnique12addParameterEPNS_10QParameterE',
        self._addressOf(p),
    )

  @overload(WAIT['Qt3DRender.QParameter'])
  @overload(NoneType)
  def removeParameter(self, p: Optional[Qt3DRender.QParameter]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTechnique::removeParameter(QParameter *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtechnique.html#removeParameter

    Parameters
    ----------

    p : Optional[Qt3DRender.QParameter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QTechnique::removeParameter(QParameter *p)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QTechnique15removeParameterEPNS_10QParamete'
        'rE',
        self._addressOf(p),
    )

  @overload(WAIT['Qt3DRender.QRenderPass'])
  @overload(NoneType)
  def addRenderPass(self, pass_: Optional[Qt3DRender.QRenderPass]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTechnique::addRenderPass(QRenderPass
    *pass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtechnique.html#addRenderPass

    Parameters
    ----------

    pass_ : Optional[Qt3DRender.QRenderPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QTechnique::addRenderPass(QRenderPass *pass)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QTechnique13addRenderPassEPNS_11QRenderPass'
        'E',
        self._addressOf(pass_),
    )

  @overload(WAIT['Qt3DRender.QRenderPass'])
  @overload(NoneType)
  def removeRenderPass(
      self,
      pass_: Optional[Qt3DRender.QRenderPass],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTechnique::removeRenderPass(QRenderPass
    *pass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtechnique.html#removeRenderPass

    Parameters
    ----------

    pass_ : Optional[Qt3DRender.QRenderPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QTechnique::removeRenderPass(QRenderPass *pass)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QTechnique16removeRenderPassEPNS_11QRenderP'
        'assE',
        self._addressOf(pass_),
    )

  def graphicsApiFilter(self) -> Optional[Qt3DRender.QGraphicsApiFilter]:
    """
    Calls Qt's 'QGraphicsApiFilter
    *Qt3DRender::QTechnique::graphicsApiFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtechnique.html#graphicsApiFilter

    Returns
    -------

    Optional[Qt3DRender.QGraphicsApiFilter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsApiFilter *Qt3DRender::QTechnique::graphicsApiFilter()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QTechnique17graphicsApiFilterEv',
    )
    return Qt3DRender.QGraphicsApiFilter._cuteAt(address)

  def d_func(self) -> Optional[Qt3DRender.QTechniquePrivate]:
    """
    Calls Qt's 'QTechniquePrivate *Qt3DRender::QTechnique::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qtechnique.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QTechniquePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTechniquePrivate *Qt3DRender::QTechnique::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QTechnique6d_funcEv',
    )
    return Qt3DRender.QTechniquePrivate._cuteAt(address)

  @staticmethod
  def filterKeys(*__, **_) -> Never:
    """
    Qt's 'QList<QFilterKey *> Qt3DRender::QTechnique::filterKeys() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTechnique.filterKeys' has no cute function yet. Qt's "
        "'QList<QFilterKey *> Qt3DRender::QTechnique::filterKeys() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QList<QParameter *> Qt3DRender::QTechnique::parameters() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTechnique.parameters' has no cute function yet. Qt's "
        "'QList<QParameter *> Qt3DRender::QTechnique::parameters() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def renderPasses(*__, **_) -> Never:
    """
    Qt's 'QList<QRenderPass *> Qt3DRender::QTechnique::renderPasses() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTechnique.renderPasses' has no cute function yet. "
        "Qt's 'QList<QRenderPass *> Qt3DRender::QTechnique::renderPasses() "
        "const': gives a type Python has no way to take yet.")
