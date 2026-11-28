"""
QQuick3DShaderUtilsRenderPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DShaderUtilsRenderPass to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DShaderUtilsRenderPass(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DShaderUtilsRenderPass: a plain Python object
  standing in front of one C++ QQuick3DShaderUtilsRenderPass.

  It is built on the cute 'QQuick3DObject', as Qt's
  QQuick3DShaderUtilsRenderPass is built on Qt's QQuick3DObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DShaderUtilsRenderPass that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject', 'tr', 'changed'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DShaderUtilsRenderPass::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DShaderUtilsRenderPass::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DShaderUtilsRenderPass::~QQuick3DShaderUtilsRenderPass()':
    the destructor: Python never removes a C++ QQuick3DShaderUtilsRenderPass.
  - Qt's 'void QQuick3DShaderUtilsRenderPass::qmlAppendCommand(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list,
    QQuick3DShaderUtilsRenderCommand *command)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
  - Qt's 'QQuick3DShaderUtilsRenderCommand
    *QQuick3DShaderUtilsRenderPass::qmlCommandAt(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list, qsizetype
    index)': names 'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>',
    which has no cute class yet.
  - Qt's 'qsizetype QQuick3DShaderUtilsRenderPass::qmlCommandCount(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
  - Qt's 'void QQuick3DShaderUtilsRenderPass::qmlCommandClear(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
  - Qt's 'void QQuick3DShaderUtilsRenderPass::qmlAppendShader(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list,
    QQuick3DShaderUtilsShader *shader)': names
    'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute class
    yet.
  - Qt's 'QQuick3DShaderUtilsShader
    *QQuick3DShaderUtilsRenderPass::qmlShaderAt(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list, qsizetype index)':
    names 'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute
    class yet.
  - Qt's 'qsizetype QQuick3DShaderUtilsRenderPass::qmlShaderCount(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute class
    yet.
  - Qt's 'void QQuick3DShaderUtilsRenderPass::qmlShaderClear(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute class
    yet.
  - Qt's 'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>
    QQuick3DShaderUtilsRenderPass::commands()': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlListProperty<QQuick3DShaderUtilsShader>
    QQuick3DShaderUtilsRenderPass::shaders()': gives a type Python has no way
    to take yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DShaderUtilsRenderPass is created at the first use, not by
    'QQuick3DShaderUtilsRenderPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DShaderUtilsRenderPass.
  - Qt tells when it has removed the C++ QQuick3DShaderUtilsRenderPass. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DShaderUtilsRenderPass that has no cute function
    yet, 'commands', 'qmlAppendCommand', 'qmlAppendShader', 'qmlCommandAt',
    'qmlCommandClear', 'qmlCommandCount', 'qmlShaderAt', 'qmlShaderClear',
    'qmlShaderCount', 'shaders', holds a function that raises
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
    Calls Qt's 'QString QQuick3DShaderUtilsRenderPass::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpass.html#tr

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
    #  QString QQuick3DShaderUtilsRenderPass::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQuick3DShaderUtilsRenderPass2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DShaderUtilsRenderPass'

  #  A C++ QQuick3DShaderUtilsRenderPass Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DShaderUtilsRenderPass'

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
    *QQuick3DShaderUtilsRenderPass::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpass.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DShaderUtilsRenderPass::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DShaderUtilsRenderPass10metaObjectEv',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DShaderUtilsRenderPass::QQuick3DShaderUtilsRenderPass()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpass.html
    """
    #  QQuick3DShaderUtilsRenderPass::QQuick3DShaderUtilsRenderPass()
    self._noteCreation(QQuick3DShaderUtilsRenderPass, lambda: Rituals.call(
        'ritual_ZN29QQuick3DShaderUtilsRenderPassC1Ev',
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

  def changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsRenderPass::changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpass.html#changed
    """
    #  void QQuick3DShaderUtilsRenderPass::changed()
    self.uglySide.call('ritual_ZN29QQuick3DShaderUtilsRenderPass7changedEv')

  @staticmethod
  def commands(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>
    QQuick3DShaderUtilsRenderPass::commands()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.commands' has no cute function yet. "
        "Qt's 'QQmlListProperty<QQuick3DShaderUtilsRenderCommand> "
        "QQuick3DShaderUtilsRenderPass::commands()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def qmlAppendCommand(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DShaderUtilsRenderPass::qmlAppendCommand(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list,
    QQuick3DShaderUtilsRenderCommand *command)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.qmlAppendCommand' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DShaderUtilsRenderPass::qmlAppendCommand(QQmlListProperty<QQ"
        "uick3DShaderUtilsRenderCommand> *list, "
        "QQuick3DShaderUtilsRenderCommand *command)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlAppendShader(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DShaderUtilsRenderPass::qmlAppendShader(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list,
    QQuick3DShaderUtilsShader *shader)': names
    'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.qmlAppendShader' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DShaderUtilsRenderPass::qmlAppendShader(QQmlListProperty<QQu"
        "ick3DShaderUtilsShader> *list, QQuick3DShaderUtilsShader "
        "*shader)': names 'QQmlListProperty<QQuick3DShaderUtilsShader>', "
        "which has no cute class yet.")

  @staticmethod
  def qmlCommandAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DShaderUtilsRenderCommand
    *QQuick3DShaderUtilsRenderPass::qmlCommandAt(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list, qsizetype
    index)': names 'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.qmlCommandAt' has no cute function "
        "yet. Qt's 'QQuick3DShaderUtilsRenderCommand "
        "*QQuick3DShaderUtilsRenderPass::qmlCommandAt(QQmlListProperty<QQuic"
        "k3DShaderUtilsRenderCommand> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlCommandClear(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DShaderUtilsRenderPass::qmlCommandClear(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.qmlCommandClear' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DShaderUtilsRenderPass::qmlCommandClear(QQmlListProperty<QQu"
        "ick3DShaderUtilsRenderCommand> *list)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlCommandCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DShaderUtilsRenderPass::qmlCommandCount(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.qmlCommandCount' has no cute "
        "function yet. Qt's 'qsizetype "
        "QQuick3DShaderUtilsRenderPass::qmlCommandCount(QQmlListProperty<QQu"
        "ick3DShaderUtilsRenderCommand> *list)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlShaderAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DShaderUtilsShader
    *QQuick3DShaderUtilsRenderPass::qmlShaderAt(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list, qsizetype index)':
    names 'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.qmlShaderAt' has no cute function "
        "yet. Qt's 'QQuick3DShaderUtilsShader "
        "*QQuick3DShaderUtilsRenderPass::qmlShaderAt(QQmlListProperty<QQuick"
        "3DShaderUtilsShader> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute "
        "class yet.")

  @staticmethod
  def qmlShaderClear(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DShaderUtilsRenderPass::qmlShaderClear(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.qmlShaderClear' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DShaderUtilsRenderPass::qmlShaderClear(QQmlListProperty<QQui"
        "ck3DShaderUtilsShader> *list)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute "
        "class yet.")

  @staticmethod
  def qmlShaderCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DShaderUtilsRenderPass::qmlShaderCount(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.qmlShaderCount' has no cute "
        "function yet. Qt's 'qsizetype "
        "QQuick3DShaderUtilsRenderPass::qmlShaderCount(QQmlListProperty<QQui"
        "ck3DShaderUtilsShader> *list)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsShader>', which has no cute "
        "class yet.")

  @staticmethod
  def shaders(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DShaderUtilsShader>
    QQuick3DShaderUtilsRenderPass::shaders()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DShaderUtilsRenderPass.shaders' has no cute function yet. "
        "Qt's 'QQmlListProperty<QQuick3DShaderUtilsShader> "
        "QQuick3DShaderUtilsRenderPass::shaders()': gives a type Python has "
        "no way to take yet.")
