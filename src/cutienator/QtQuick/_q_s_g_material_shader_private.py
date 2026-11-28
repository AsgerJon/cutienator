"""
QSGMaterialShaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgmaterialshader_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGMaterialShaderPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QShader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGMaterialShader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGMaterialShader = WAIT['QSGMaterialShader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGMaterialShaderPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGMaterialShaderPrivate: a plain Python object
  standing in front of one C++ QSGMaterialShaderPrivate.

  C++ hands a QSGMaterialShaderPrivate around as a copy, so every C++
  QSGMaterialShaderPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGMaterialShaderPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'get',
  'clearCachedRendererData', 'prepare', 'shader', 'loadShader'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSGMaterialShader *QSGMaterialShaderPrivate::q_func() const':
    takes in Python what 'QSGMaterialShader
    *QSGMaterialShaderPrivate::q_func()' takes.
  - Qt's 'const QSGMaterialShaderPrivate *QSGMaterialShaderPrivate::get(const
    QSGMaterialShader *s)': takes in Python what 'QSGMaterialShaderPrivate
    *QSGMaterialShaderPrivate::get(QSGMaterialShader *s)' takes.
  - Qt's 'QSGMaterialShaderPrivate::~QSGMaterialShaderPrivate()': the
    destructor: Python removes its C++ QSGMaterialShaderPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSGMaterialShaderPrivate is created at the first use, not by
    'QSGMaterialShaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGMaterialShaderPrivate back gives a copy the ritual
    made for Python, in a new cute QSGMaterialShaderPrivate.
  """

  #  The classes Qt writes inside QSGMaterialShaderPrivate, each a class in
  #  here as in C++.

  class ShaderStageData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGMaterialShaderPrivate::ShaderStageData: a plain
    Python object standing in front of one C++
    QSGMaterialShaderPrivate::ShaderStageData.

    C++ hands a QSGMaterialShaderPrivate::ShaderStageData around as a copy,
    so every C++ QSGMaterialShaderPrivate::ShaderStageData behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSGMaterialShaderPrivate::ShaderStageData yet. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGMaterialShaderPrivate::ShaderStageData::~ShaderStageData()':
      the destructor: Python removes its C++
      QSGMaterialShaderPrivate::ShaderStageData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSGMaterialShaderPrivate::ShaderStageData is created at the
      first use, not by 'QSGMaterialShaderPrivate::ShaderStageData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGMaterialShaderPrivate::ShaderStageData back
      gives a copy the ritual made for Python, in a new cute
      QSGMaterialShaderPrivate::ShaderStageData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QShader = WAIT['QShader']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGMaterialShaderPrivate::ShaderStageData'

    #  Qt's '~QSGMaterialShaderPrivate::ShaderStageData()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSGMaterialShaderPrivate::ShaderStageData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN24QSGMaterialShaderPrivate15ShaderStageDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSGMaterialShaderPrivate::ShaderStageData::ShaderStageData()', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshaderprivate-shaderstagedata.html
      """
      #  QSGMaterialShaderPrivate::ShaderStageData::ShaderStageData()
      self._noteCreation(
          QSGMaterialShaderPrivate.ShaderStageData, lambda: Rituals.call(
              'ritual_ZN24QSGMaterialShaderPrivate15ShaderStageDataC1Ev',
          ))

    @overload(QShader)
    def __init__(self, shader: QShader) -> None:
      """
      Notes what was given, for Qt's
      'QSGMaterialShaderPrivate::ShaderStageData::ShaderStageData(const
      QShader &shader)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshaderprivate-shaderstagedata.html

      Parameters
      ----------

      shader : QShader
        Passed on as a value: Qt reads the C++ QShader, which stays Python's
        own.
      """
      #  QSGMaterialShaderPrivate::ShaderStageData::ShaderStageData(const
      #      QShader &shader)
      self._noteCreation(
          QSGMaterialShaderPrivate.ShaderStageData, lambda: Rituals.call(
              'ritual_ZN24QSGMaterialShaderPrivate15ShaderStageDataC1ERK7QS'
              'hader',
              self._valueOf(shader),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSGMaterialShader)
  @overload(NoneType)
  def get(
      s: Optional[QSGMaterialShader],
  ) -> Optional[QSGMaterialShaderPrivate]:
    """
    Calls Qt's 'QSGMaterialShaderPrivate
    *QSGMaterialShaderPrivate::get(QSGMaterialShader *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterialshaderprivate.html#get

    Parameters
    ----------

    s : Optional[QSGMaterialShader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGMaterialShaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialShaderPrivate
    #      *QSGMaterialShaderPrivate::get(QSGMaterialShader *s)
    address = Rituals.call(
        'ritual_ZN24QSGMaterialShaderPrivate3getEP17QSGMaterialShader',
        CuteMixin._addressOf(s),
    )
    return QSGMaterialShaderPrivate._cuteAt(address)

  @staticmethod
  @overload(str)
  def loadShader(filename: str) -> QShader:
    """
    Calls Qt's 'QShader QSGMaterialShaderPrivate::loadShader(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshaderprivate.html#loadShader

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QShader
      A new cute QShader around the copy Qt gave back. Python owns it.
    """
    #  QShader QSGMaterialShaderPrivate::loadShader(const QString &filename)
    address = Rituals.call(
        'ritual_ZN24QSGMaterialShaderPrivate10loadShaderERK7QString',
        filename,
    )
    return QShader._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGMaterialShaderPrivate'

  #  Qt's '~QSGMaterialShaderPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QSGMaterialShaderPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QSGMaterialShaderPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QShader.Stage)
  def shader(self, stage: QShader.Stage) -> QShader:
    """
    Calls Qt's 'QShader QSGMaterialShaderPrivate::shader(QShader::Stage
    stage) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshaderprivate.html#shader

    Parameters
    ----------

    stage : QShader.Stage
      Passed on as its number.

    Returns
    -------

    QShader
      A new cute QShader around the copy Qt gave back. Python owns it.
    """
    #  QShader QSGMaterialShaderPrivate::shader(QShader::Stage stage) const
    address = self.uglySide.call(
        'ritual_ZNK24QSGMaterialShaderPrivate6shaderEN7QShader5StageE',
        stage.value,
    )
    return QShader._cuteOwning(address)

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

  @overload(QSGMaterialShader)
  @overload(NoneType)
  def __init__(self, q: Optional[QSGMaterialShader]) -> None:
    """
    Notes what was given, for Qt's
    'QSGMaterialShaderPrivate::QSGMaterialShaderPrivate(QSGMaterialShader
    *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshaderprivate.html

    Parameters
    ----------

    q : Optional[QSGMaterialShader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGMaterialShaderPrivate::QSGMaterialShaderPrivate(QSGMaterialShader
    #      *q)
    self._noteCreation(QSGMaterialShaderPrivate, lambda: Rituals.call(
        'ritual_ZN24QSGMaterialShaderPrivateC1EP17QSGMaterialShader',
        self._addressOf(q),
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

  def q_func(self) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader *QSGMaterialShaderPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshaderprivate.html#q_func

    Returns
    -------

    Optional[QSGMaterialShader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialShader *QSGMaterialShaderPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QSGMaterialShaderPrivate6q_funcEv',
    )
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  def clearCachedRendererData(self) -> None:
    """
    Calls Qt's 'void QSGMaterialShaderPrivate::clearCachedRendererData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshaderprivate.html
    """
    #  void QSGMaterialShaderPrivate::clearCachedRendererData()
    self.uglySide.call(
        'ritual_ZN24QSGMaterialShaderPrivate23clearCachedRendererDataEv',
    )

  @overload(QShader.Variant)
  def prepare(self, vertexShaderVariant: QShader.Variant) -> None:
    """
    Calls Qt's 'void QSGMaterialShaderPrivate::prepare(QShader::Variant
    vertexShaderVariant)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshaderprivate.html#prepare

    Parameters
    ----------

    vertexShaderVariant : QShader.Variant
      Passed on as its number.
    """
    #  void QSGMaterialShaderPrivate::prepare(QShader::Variant
    #      vertexShaderVariant)
    self.uglySide.call(
        'ritual_ZN24QSGMaterialShaderPrivate7prepareEN7QShader7VariantE',
        vertexShaderVariant.value,
    )
