"""
QQuick3DShaderUtilsRenderPassAddDefine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DShaderUtilsRenderPassAddDefine to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DShaderUtilsRenderCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGCommand
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DShaderUtilsRenderPassAddDefine(QQuick3DShaderUtilsRenderCommand):
  """
  The cute side of Qt's QQuick3DShaderUtilsRenderPassAddDefine: a plain
  Python object standing in front of one C++
  QQuick3DShaderUtilsRenderPassAddDefine.

  It is built on the cute 'QQuick3DShaderUtilsRenderCommand', as Qt's
  QQuick3DShaderUtilsRenderPassAddDefine is built on Qt's
  QQuick3DShaderUtilsRenderCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DShaderUtilsRenderPassAddDefine that has a
  ritual and that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'cloneCommand', 'name', 'setName', 'value', 'setValue', 'nameChanged',
  'valueChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DShaderUtilsRenderPassAddDefine::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuick3DShaderUtilsRenderPassAddDefine::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DShaderUtilsRenderPassAddDefine::
    ~QQuick3DShaderUtilsRenderPassAddDefine()': the destructor: Python never
    removes a C++ QQuick3DShaderUtilsRenderPassAddDefine.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DShaderUtilsRenderPassAddDefine is created at the first
    use, not by 'QQuick3DShaderUtilsRenderPassAddDefine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DShaderUtilsRenderPassAddDefine.
  - Qt tells when it has removed the C++
    QQuick3DShaderUtilsRenderPassAddDefine. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString QQuick3DShaderUtilsRenderPassAddDefine::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html#tr

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
    #  QString QQuick3DShaderUtilsRenderPassAddDefine::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DShaderUtilsRenderPassAddDefine'

  #  A C++ QQuick3DShaderUtilsRenderPassAddDefine Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DShaderUtilsRenderPassAddDefine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuick3DShaderUtilsRenderPassAddDefine::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuick3DShaderUtilsRenderPassAddDefine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK38QQuick3DShaderUtilsRenderPassAddDefine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQuick3DShaderUtilsRenderPassAddDefine::name()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQuick3DShaderUtilsRenderPassAddDefine::name() const
    address = self.uglySide.call(
        'ritual_ZNK38QQuick3DShaderUtilsRenderPassAddDefine4nameEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def value(self) -> int:
    """
    Calls Qt's 'int QQuick3DShaderUtilsRenderPassAddDefine::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html#value
    """
    #  int QQuick3DShaderUtilsRenderPassAddDefine::value() const
    return self.uglySide.call(
        'ritual_ZNK38QQuick3DShaderUtilsRenderPassAddDefine5valueEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setName(self, newName: QByteArray) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsRenderPassAddDefine::setName(const
    QByteArray &newName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html

    Parameters
    ----------

    newName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuick3DShaderUtilsRenderPassAddDefine::setName(const QByteArray
    #      &newName)
    self.uglySide.call(
        'ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine7setNameERK10QByt'
        'eArray',
        self._valueOf(newName),
    )

  @overload(int)
  def setValue(self, newValue: int) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsRenderPassAddDefine::setValue(int
    newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html

    Parameters
    ----------

    newValue : int
      Passed on as it is.
    """
    #  void QQuick3DShaderUtilsRenderPassAddDefine::setValue(int newValue)
    self.uglySide.call(
        'ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine8setValueEi',
        newValue,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQuick3DShaderUtilsRenderPassAddDefine::
    QQuick3DShaderUtilsRenderPassAddDefine()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html
    """
    #  QQuick3DShaderUtilsRenderPassAddDefine::
    #      QQuick3DShaderUtilsRenderPassAddDefine()
    self._noteCreation(
        QQuick3DShaderUtilsRenderPassAddDefine, lambda: Rituals.call(
            'ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefineC1Ev',
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

  def cloneCommand(self) -> Optional[QSSGCommand]:
    """
    Calls Qt's 'QSSGCommand
    *QQuick3DShaderUtilsRenderPassAddDefine::cloneCommand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html

    Returns
    -------

    Optional[QSSGCommand]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGCommand *QQuick3DShaderUtilsRenderPassAddDefine::cloneCommand()
    ritual = (
        'ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine12cloneCommandEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN38QQuick3DShaderUtilsRenderPassAddDefine12cloneComm'
          'andEv')
    address = self.uglySide.call(ritual)
    from ..QtQuick3DRuntimeRender import QSSGCommand
    return QSSGCommand._cuteAt(address)

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsRenderPassAddDefine::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html
    """
    #  void QQuick3DShaderUtilsRenderPassAddDefine::nameChanged()
    self.uglySide.call(
        'ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine11nameChangedEv',
    )

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsRenderPassAddDefine::valueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpassadddefine.html
    """
    #  void QQuick3DShaderUtilsRenderPassAddDefine::valueChanged()
    self.uglySide.call(
        'ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine12valueChangedEv',
    )
