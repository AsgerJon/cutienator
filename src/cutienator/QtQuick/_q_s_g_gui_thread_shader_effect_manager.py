"""
QSGGuiThreadShaderEffectManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGGuiThreadShaderEffectManager to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGGuiThreadShaderEffectManager(QObject):
  """
  The cute side of Qt's QSGGuiThreadShaderEffectManager: a plain Python
  object standing in front of one C++ QSGGuiThreadShaderEffectManager.

  It is built on the cute 'QObject', as Qt's QSGGuiThreadShaderEffectManager
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGGuiThreadShaderEffectManager that has a ritual
  and that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'hasSeparateSamplerAndTextureObjects', 'log', 'status',
  'logAndStatusChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGGuiThreadShaderEffectManager::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QSGGuiThreadShaderEffectManager::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QSGGuiThreadShaderEffectManager::~QSGGuiThreadShaderEffectManager()':
    the destructor: Python never removes a C++
    QSGGuiThreadShaderEffectManager.
  - Qt's 'void
    QSGGuiThreadShaderEffectManager::prepareShaderCode(ShaderInfo::Type
    typeHint, const QUrl &src, ShaderInfo *result)': names the enum
    'QSGGuiThreadShaderEffectManager::ShaderInfo::Type', whose class cannot
    be named here.
  - Qt's 'void QSGGuiThreadShaderEffectManager::shaderCodePrepared(bool ok,
    ShaderInfo::Type typeHint, const QUrl &src, ShaderInfo *result)': names
    the enum 'QSGGuiThreadShaderEffectManager::ShaderInfo::Type', whose class
    cannot be named here.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGGuiThreadShaderEffectManager is created at the first use, not
    by 'QSGGuiThreadShaderEffectManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGGuiThreadShaderEffectManager.
  - Qt tells when it has removed the C++ QSGGuiThreadShaderEffectManager.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGGuiThreadShaderEffectManager that has no cute
    function yet, 'prepareShaderCode', 'shaderCodePrepared', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSGGuiThreadShaderEffectManager, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Status(CuteNum):
    """
    The enum 'QSGGuiThreadShaderEffectManager::Status' of Qt, with the 3
    names Qt gives in it.
    """

    Compiled = Kee[int](0)
    Uncompiled = Kee[int](1)
    Error = Kee[int](2)

  #  The classes Qt writes inside QSGGuiThreadShaderEffectManager, each a
  #  class in here as in C++.

  class ShaderInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGGuiThreadShaderEffectManager::ShaderInfo: a
    plain Python object standing in front of one C++
    QSGGuiThreadShaderEffectManager::ShaderInfo.

    C++ hands a QSGGuiThreadShaderEffectManager::ShaderInfo around as a copy,
    so every C++ QSGGuiThreadShaderEffectManager::ShaderInfo behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSGGuiThreadShaderEffectManager::ShaderInfo yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGGuiThreadShaderEffectManager::ShaderInfo::~ShaderInfo()': the
      destructor: Python removes its C++
      QSGGuiThreadShaderEffectManager::ShaderInfo by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSGGuiThreadShaderEffectManager::ShaderInfo is created at the
      first use, not by 'QSGGuiThreadShaderEffectManager::ShaderInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGGuiThreadShaderEffectManager::ShaderInfo back
      gives a copy the ritual made for Python, in a new cute
      QSGGuiThreadShaderEffectManager::ShaderInfo.
    """

    #  The enums Qt writes inside
    #  QSGGuiThreadShaderEffectManager::ShaderInfo, each a class in here as
    #  in C++, and the names Qt has for the combinations of its flags enums.

    class Type(CuteNum):
      """
      The enum 'QSGGuiThreadShaderEffectManager::ShaderInfo::Type' of Qt,
      with the 3 names Qt gives in it.
      """

      TypeVertex = Kee[int](0)
      TypeFragment = Kee[int](1)
      TypeOther = Kee[int](2)

    class VariableType(CuteNum):
      """
      The enum 'QSGGuiThreadShaderEffectManager::ShaderInfo::VariableType' of
      Qt, with the 3 names Qt gives in it.
      """

      Constant = Kee[int](0)
      Sampler = Kee[int](1)
      Texture = Kee[int](2)

    #  The classes Qt writes inside
    #  QSGGuiThreadShaderEffectManager::ShaderInfo, each a class in here as
    #  in C++.

    class Variable(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QSGGuiThreadShaderEffectManager::ShaderInfo::Variable: a plain Python
      object standing in front of one C++
      QSGGuiThreadShaderEffectManager::ShaderInfo::Variable.

      C++ hands a QSGGuiThreadShaderEffectManager::ShaderInfo::Variable
      around as a copy, so every C++
      QSGGuiThreadShaderEffectManager::ShaderInfo::Variable behind a cute one
      is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's
      QSGGuiThreadShaderEffectManager::ShaderInfo::Variable yet. None can be
      made from Python: one comes out of a function of another class that
      gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's
        'QSGGuiThreadShaderEffectManager::ShaderInfo::Variable::~Variable()':
        the destructor: Python removes its C++
        QSGGuiThreadShaderEffectManager::ShaderInfo::Variable by it, and has
        no other use for it.

      What to expect
      --------------

      - The C++ QSGGuiThreadShaderEffectManager::ShaderInfo::Variable is
        created at the first use, not by
        'QSGGuiThreadShaderEffectManager::ShaderInfo::Variable(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a
        QSGGuiThreadShaderEffectManager::ShaderInfo::Variable back gives a
        copy the ritual made for Python, in a new cute
        QSGGuiThreadShaderEffectManager::ShaderInfo::Variable.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QSGGuiThreadShaderEffectManager::ShaderInfo::Variable'

      #  Qt's '~QSGGuiThreadShaderEffectManager::ShaderInfo::Variable()'.
      #  Naming it makes this a value class: Python owns every C++
      #  QSGGuiThreadShaderEffectManager::ShaderInfo::Variable behind a cute
      #  one, and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN31QSGGuiThreadShaderEffectManager10ShaderInfo8VariableD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGGuiThreadShaderEffectManager::ShaderInfo'

    #  Qt's '~QSGGuiThreadShaderEffectManager::ShaderInfo()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSGGuiThreadShaderEffectManager::ShaderInfo behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN31QSGGuiThreadShaderEffectManager10ShaderInfoD1Ev')

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
    Calls Qt's 'QString QSGGuiThreadShaderEffectManager::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgguithreadshadereffectmanager.html#tr

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
    #  QString QSGGuiThreadShaderEffectManager::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QSGGuiThreadShaderEffectManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGGuiThreadShaderEffectManager'

  #  A C++ QSGGuiThreadShaderEffectManager Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGGuiThreadShaderEffectManager'

  #  The functions Qt calls itself that QSGGuiThreadShaderEffectManager is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'hasSeparateSamplerAndTextureObjects': (
          ('_ZNK31QSGGuiThreadShaderEffectManager35hasSeparateSamplerAndTex'
           'tureObjectsEv',
           ('bool', 'number', ''),
           ()),
      ),
      'log': (
          ('_ZNK31QSGGuiThreadShaderEffectManager3logEv',
           ('address', 'text', ''),
           ()),
      ),
      'status': (
          ('_ZNK31QSGGuiThreadShaderEffectManager6statusEv',
           ('int', 'enum', 'QtQuick:QSGGuiThreadShaderEffectManager.Status'),
           ()),
      ),
      'prepareShaderCode': (
          ('_ZN31QSGGuiThreadShaderEffectManager17prepareShaderCodeENS_10Sh'
           'aderInfo4TypeERK4QUrlPS0_',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtQuick:QSGGuiThreadShaderEffectManager.ShaderInfo.Type'),
               ('address', 'value', 'QtCore:QUrl'),
               ('address', 'address',
                'QtQuick:QSGGuiThreadShaderEffectManager.ShaderInfo'),
           )),
      ),
  }

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
    *QSGGuiThreadShaderEffectManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgguithreadshadereffectmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGGuiThreadShaderEffectManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QSGGuiThreadShaderEffectManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasSeparateSamplerAndTextureObjects(self) -> bool:
    """
    Calls Qt's 'bool
    QSGGuiThreadShaderEffectManager::hasSeparateSamplerAndTextureObjects()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgguithreadshadereffectmanager.html
    """
    #  bool QSGGuiThreadShaderEffectManager::
    #      hasSeparateSamplerAndTextureObjects() const
    return self.uglySide.call(
        'ritual_ZNK31QSGGuiThreadShaderEffectManager35hasSeparateSamplerAnd'
        'TextureObjectsEv',
    )

  def log(self) -> str:
    """
    Calls Qt's 'QString QSGGuiThreadShaderEffectManager::log() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgguithreadshadereffectmanager.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSGGuiThreadShaderEffectManager::log() const
    return self.uglySide.call(
        'ritual_ZNK31QSGGuiThreadShaderEffectManager3logEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status QSGGuiThreadShaderEffectManager::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgguithreadshadereffectmanager.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QSGGuiThreadShaderEffectManager::status() const
    return QSGGuiThreadShaderEffectManager.Status(self.uglySide.call(
        'ritual_ZNK31QSGGuiThreadShaderEffectManager6statusEv',
    ))

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

  def logAndStatusChanged(self) -> None:
    """
    Calls Qt's 'void QSGGuiThreadShaderEffectManager::logAndStatusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgguithreadshadereffectmanager.html
    """
    #  void QSGGuiThreadShaderEffectManager::logAndStatusChanged()
    self.uglySide.call(
        'ritual_ZN31QSGGuiThreadShaderEffectManager19logAndStatusChangedEv',
    )

  @staticmethod
  def prepareShaderCode(*__, **_) -> Never:
    """
    Qt's 'void
    QSGGuiThreadShaderEffectManager::prepareShaderCode(ShaderInfo::Type
    typeHint, const QUrl &src, ShaderInfo *result)': names the enum
    'QSGGuiThreadShaderEffectManager::ShaderInfo::Type', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QSGGuiThreadShaderEffectManager.prepareShaderCode' has no cute "
        "function yet. Qt's 'void "
        "QSGGuiThreadShaderEffectManager::prepareShaderCode(ShaderInfo::Type"
        " typeHint, const QUrl &src, ShaderInfo *result)': names the enum "
        "'QSGGuiThreadShaderEffectManager::ShaderInfo::Type', whose class "
        "cannot be named here.")

  @staticmethod
  def shaderCodePrepared(*__, **_) -> Never:
    """
    Qt's 'void QSGGuiThreadShaderEffectManager::shaderCodePrepared(bool ok,
    ShaderInfo::Type typeHint, const QUrl &src, ShaderInfo *result)': names
    the enum 'QSGGuiThreadShaderEffectManager::ShaderInfo::Type', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSGGuiThreadShaderEffectManager.shaderCodePrepared' has no cute "
        "function yet. Qt's 'void "
        "QSGGuiThreadShaderEffectManager::shaderCodePrepared(bool ok, "
        "ShaderInfo::Type typeHint, const QUrl &src, ShaderInfo *result)': "
        "names the enum "
        "'QSGGuiThreadShaderEffectManager::ShaderInfo::Type', whose class "
        "cannot be named here.")
