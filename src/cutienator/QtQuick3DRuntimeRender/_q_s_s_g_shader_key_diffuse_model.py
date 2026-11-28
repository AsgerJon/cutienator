"""
QSSGShaderKeyDiffuseModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderKeyDiffuseModel to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGShaderKeyDiffuseModel(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderKeyDiffuseModel: a plain Python object
  standing in front of one C++ QSSGShaderKeyDiffuseModel.

  C++ hands a QSSGShaderKeyDiffuseModel around as a copy, so every C++
  QSSGShaderKeyDiffuseModel behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGShaderKeyDiffuseModel yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QSSGShaderKeyDiffuseModel::setDiffuseModel(QSSGDataRef<quint32> inKeySet,
    QSSGRenderDefaultMaterial::MaterialDiffuseModel inModel)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSSGRenderDefaultMaterial::MaterialDiffuseModel
    QSSGShaderKeyDiffuseModel::getDiffuseModel(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyDiffuseModel::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGShaderKeyDiffuseModel::fromString(const QByteArray &ioStr,
    QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QSSGShaderKeyDiffuseModel::~QSSGShaderKeyDiffuseModel()': the
    destructor: Python removes its C++ QSSGShaderKeyDiffuseModel by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGShaderKeyDiffuseModel is created at the first use, not by
    'QSSGShaderKeyDiffuseModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderKeyDiffuseModel back gives a copy the
    ritual made for Python, in a new cute QSSGShaderKeyDiffuseModel.
  - Each name of Qt's QSSGShaderKeyDiffuseModel that has no cute function
    yet, 'fromString', 'getDiffuseModel', 'setDiffuseModel', 'toString',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderKeyDiffuseModel'

  #  Qt's '~QSSGShaderKeyDiffuseModel()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGShaderKeyDiffuseModel behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QSSGShaderKeyDiffuseModelD1Ev'

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

  @overload(str)
  @overload(NoneType)
  def __init__(self, inName: Optional[str]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGShaderKeyDiffuseModel::QSSGShaderKeyDiffuseModel(const char
    *inName)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeydiffusemodel.html

    Parameters
    ----------

    inName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QSSGShaderKeyDiffuseModel::QSSGShaderKeyDiffuseModel(const char
    #      *inName)
    self._noteCreation(QSSGShaderKeyDiffuseModel, lambda: Rituals.call(
        'ritual_ZN25QSSGShaderKeyDiffuseModelC1EPKc', self._bytesOf(inName),
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

  @staticmethod
  def fromString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyDiffuseModel::fromString(const QByteArray &ioStr,
    QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyDiffuseModel.fromString' has no cute function yet. "
        "Qt's 'void QSSGShaderKeyDiffuseModel::fromString(const QByteArray "
        "&ioStr, QSSGDataRef<quint32> inKeySet)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def getDiffuseModel(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderDefaultMaterial::MaterialDiffuseModel
    QSSGShaderKeyDiffuseModel::getDiffuseModel(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyDiffuseModel.getDiffuseModel' has no cute function "
        "yet. Qt's 'QSSGRenderDefaultMaterial::MaterialDiffuseModel "
        "QSSGShaderKeyDiffuseModel::getDiffuseModel(QSSGDataView<quint32> "
        "inKeySet) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setDiffuseModel(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGShaderKeyDiffuseModel::setDiffuseModel(QSSGDataRef<quint32> inKeySet,
    QSSGRenderDefaultMaterial::MaterialDiffuseModel inModel)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyDiffuseModel.setDiffuseModel' has no cute function "
        "yet. Qt's 'void "
        "QSSGShaderKeyDiffuseModel::setDiffuseModel(QSSGDataRef<quint32> "
        "inKeySet, QSSGRenderDefaultMaterial::MaterialDiffuseModel "
        "inModel)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyDiffuseModel::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyDiffuseModel.toString' has no cute function yet. "
        "Qt's 'void QSSGShaderKeyDiffuseModel::toString(QByteArray &ioStr, "
        "QSSGDataView<quint32> inKeySet) const': takes a type Python has no "
        "way to hand over yet.")
