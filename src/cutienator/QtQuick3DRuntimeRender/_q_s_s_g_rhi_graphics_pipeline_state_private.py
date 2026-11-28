"""
QSSGRhiGraphicsPipelineStatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiGraphicsPipelineStatePrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSSGRhiGraphicsPipelineState, QSSGRhiShaderPipeline
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRhiGraphicsPipelineState = WAIT['QSSGRhiGraphicsPipelineState']


class QSSGRhiGraphicsPipelineStatePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiGraphicsPipelineStatePrivate: a plain Python
  object standing in front of one C++ QSSGRhiGraphicsPipelineStatePrivate.

  C++ hands a QSSGRhiGraphicsPipelineStatePrivate around as a copy, so every
  C++ QSSGRhiGraphicsPipelineStatePrivate behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QSSGRhiGraphicsPipelineStatePrivate that has a
  ritual and that Python can call so far, 1 name in all: 'getShaderPipeline'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGRhiGraphicsPipelineStatePrivate::setShaderPipeline(
    QSSGRhiGraphicsPipelineState &ps, const QSSGRhiShaderPipeline
    *pipeline)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiGraphicsPipelineStatePrivate::
    ~QSSGRhiGraphicsPipelineStatePrivate()': the destructor: Python removes
    its C++ QSSGRhiGraphicsPipelineStatePrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGRhiGraphicsPipelineStatePrivate is created at the first use,
    not by 'QSSGRhiGraphicsPipelineStatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRhiGraphicsPipelineStatePrivate back gives a copy
    the ritual made for Python, in a new cute
    QSSGRhiGraphicsPipelineStatePrivate.
  - Each name of Qt's QSSGRhiGraphicsPipelineStatePrivate that has no cute
    function yet, 'setShaderPipeline', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSSGRhiGraphicsPipelineState)
  def getShaderPipeline(
      ps: QSSGRhiGraphicsPipelineState,
  ) -> Optional[QSSGRhiShaderPipeline]:
    """
    Calls Qt's 'const QSSGRhiShaderPipeline
    *QSSGRhiGraphicsPipelineStatePrivate::getShaderPipeline(const
    QSSGRhiGraphicsPipelineState &ps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhigraphicspipelinestateprivate.html

    Parameters
    ----------

    ps : QSSGRhiGraphicsPipelineState
      Passed on as a value: Qt reads the C++ QSSGRhiGraphicsPipelineState,
      which stays Python's own.

    Returns
    -------

    Optional[QSSGRhiShaderPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSSGRhiShaderPipeline
    #      *QSSGRhiGraphicsPipelineStatePrivate::getShaderPipeline(const
    #      QSSGRhiGraphicsPipelineState &ps)
    address = Rituals.call(
        'ritual_ZN35QSSGRhiGraphicsPipelineStatePrivate17getShaderPipelineE'
        'RK28QSSGRhiGraphicsPipelineState',
        CuteMixin._valueOf(ps),
    )
    from . import QSSGRhiShaderPipeline
    return QSSGRhiShaderPipeline._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiGraphicsPipelineStatePrivate'

  #  Qt's '~QSSGRhiGraphicsPipelineStatePrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QSSGRhiGraphicsPipelineStatePrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN35QSSGRhiGraphicsPipelineStatePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def setShaderPipeline(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiGraphicsPipelineStatePrivate::setShaderPipeline(
    QSSGRhiGraphicsPipelineState &ps, const QSSGRhiShaderPipeline
    *pipeline)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiGraphicsPipelineStatePrivate.setShaderPipeline' has no "
        "cute function yet. Qt's 'void "
        "QSSGRhiGraphicsPipelineStatePrivate::setShaderPipeline(QSSGRhiGraph"
        "icsPipelineState &ps, const QSSGRhiShaderPipeline *pipeline)': "
        "takes a type Python has no way to hand over yet.")
