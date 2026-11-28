"""
QSSGShaderKeyPropertyBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderKeyPropertyBase to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGShaderKeyPropertyBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderKeyPropertyBase: a plain Python object
  standing in front of one C++ QSSGShaderKeyPropertyBase.

  C++ hands a QSSGShaderKeyPropertyBase around as a copy, so every C++
  QSSGShaderKeyPropertyBase behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGShaderKeyPropertyBase that has a ritual and that
  Python can call so far, 4 names in all: 'getOffset', 'setOffset', 'getIdx',
  'getBoolValue'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGShaderKeyPropertyBase::internalToString(QByteArray &ioStr,
    const QByteArrayView &inBuffer) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGShaderKeyPropertyBase::internalToString(QByteArray &ioStr,
    const QByteArrayView &name, bool inValue)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSSGShaderKeyPropertyBase::~QSSGShaderKeyPropertyBase()': the
    destructor: Python removes its C++ QSSGShaderKeyPropertyBase by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QSSGShaderKeyPropertyBase is created at the first use, not by
    'QSSGShaderKeyPropertyBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderKeyPropertyBase back gives a copy the
    ritual made for Python, in a new cute QSSGShaderKeyPropertyBase.
  - Each name of Qt's QSSGShaderKeyPropertyBase that has no cute function
    yet, 'getMaskTemplate', 'internalToString', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray, QByteArrayView)
  def getBoolValue(str: QByteArray, name: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QSSGShaderKeyPropertyBase::getBoolValue(const QByteArray
    &str, const QByteArrayView &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeypropertybase.html#getBoolValue

    Parameters
    ----------

    str : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QSSGShaderKeyPropertyBase::getBoolValue(const QByteArray &str,
    #      const QByteArrayView &name)
    return Rituals.call(
        'ritual_ZN25QSSGShaderKeyPropertyBase12getBoolValueERK10QByteArrayR'
        'K14QByteArrayView',
        CuteMixin._valueOf(str), CuteMixin._valueOf(name),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderKeyPropertyBase'

  #  Qt's '~QSSGShaderKeyPropertyBase()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGShaderKeyPropertyBase behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QSSGShaderKeyPropertyBaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getOffset(self) -> int:
    """
    Calls Qt's 'quint32 QSSGShaderKeyPropertyBase::getOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeypropertybase.html#getOffset
    """
    #  quint32 QSSGShaderKeyPropertyBase::getOffset() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGShaderKeyPropertyBase9getOffsetEv',
    )

  def getIdx(self) -> int:
    """
    Calls Qt's 'quint32 QSSGShaderKeyPropertyBase::getIdx() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeypropertybase.html#getIdx
    """
    #  quint32 QSSGShaderKeyPropertyBase::getIdx() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGShaderKeyPropertyBase6getIdxEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setOffset(self, of: int) -> None:
    """
    Calls Qt's 'void QSSGShaderKeyPropertyBase::setOffset(quint32 of)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeypropertybase.html#setOffset

    Parameters
    ----------

    of : int
      Passed on as it is.
    """
    #  void QSSGShaderKeyPropertyBase::setOffset(quint32 of)
    self.uglySide.call(
        'ritual_ZN25QSSGShaderKeyPropertyBase9setOffsetEj', of,
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

  @overload(str)
  @overload(NoneType)
  def __init__(self, inName: Optional[str]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGShaderKeyPropertyBase::QSSGShaderKeyPropertyBase(const char
    *inName)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeypropertybase.html

    Parameters
    ----------

    inName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QSSGShaderKeyPropertyBase::QSSGShaderKeyPropertyBase(const char
    #      *inName)
    self._noteCreation(QSSGShaderKeyPropertyBase, lambda: Rituals.call(
        'ritual_ZN25QSSGShaderKeyPropertyBaseC1EPKc', self._bytesOf(inName),
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
  def getMaskTemplate(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderKeyPropertyBase::getMaskTemplate': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyPropertyBase.getMaskTemplate' has no cute function "
        "yet. Qt's 'QSSGShaderKeyPropertyBase::getMaskTemplate': a "
        "template: a pattern and no single function.")

  @staticmethod
  def internalToString(*__, **_) -> Never:
    """
    - Qt's 'void QSSGShaderKeyPropertyBase::internalToString(QByteArray
      &ioStr, const QByteArrayView &inBuffer) const': takes a type Python has
      no way to hand over yet.
    - Qt's 'void QSSGShaderKeyPropertyBase::internalToString(QByteArray
      &ioStr, const QByteArrayView &name, bool inValue)': takes a type Python
      has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyPropertyBase.internalToString' has no cute function "
        "yet. Qt's 'void "
        "QSSGShaderKeyPropertyBase::internalToString(QByteArray &ioStr, "
        "const QByteArrayView &inBuffer) const': takes a type Python has no "
        "way to hand over yet. Qt's 'void "
        "QSSGShaderKeyPropertyBase::internalToString(QByteArray &ioStr, "
        "const QByteArrayView &name, bool inValue)': takes a type Python "
        "has no way to hand over yet.")
