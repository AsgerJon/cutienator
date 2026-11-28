"""
QOpenGLProgramBinaryCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopenglprogrambinarycache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLProgramBinaryCache to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QShader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QOpenGLProgramBinaryCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLProgramBinaryCache: a plain Python object
  standing in front of one C++ QOpenGLProgramBinaryCache.

  What exists
  -----------

  Every function of Qt's QOpenGLProgramBinaryCache that has a ritual and that
  Python can call so far, 4 names in all: 'load', 'save', 'cacheFileName',
  'verifyHeader'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QOpenGLProgramBinaryCache::setProgramBinary(uint programId,
    uint blobFormat, const void *p, uint blobSize)': names 'void', which has
    no cute class yet.

  What to expect
  --------------

  - The C++ QOpenGLProgramBinaryCache is created at the first use, not by
    'QOpenGLProgramBinaryCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLProgramBinaryCache.
  - Each name of Qt's QOpenGLProgramBinaryCache that has no cute function
    yet, 'setProgramBinary', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QOpenGLProgramBinaryCache, each a class in
  #  here as in C++.

  class ProgramDesc(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpenGLProgramBinaryCache::ProgramDesc: a plain
    Python object standing in front of one C++
    QOpenGLProgramBinaryCache::ProgramDesc.

    C++ hands a QOpenGLProgramBinaryCache::ProgramDesc around as a copy, so
    every C++ QOpenGLProgramBinaryCache::ProgramDesc behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QOpenGLProgramBinaryCache::ProgramDesc that has a
    ritual and that Python can call so far, 1 name in all: 'cacheKey'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QOpenGLProgramBinaryCache::ProgramDesc::~ProgramDesc()': the
      destructor: Python removes its C++
      QOpenGLProgramBinaryCache::ProgramDesc by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QOpenGLProgramBinaryCache::ProgramDesc is created at the first
      use, not by 'QOpenGLProgramBinaryCache::ProgramDesc(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOpenGLProgramBinaryCache::ProgramDesc back gives a
      copy the ritual made for Python, in a new cute
      QOpenGLProgramBinaryCache::ProgramDesc.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpenGLProgramBinaryCache::ProgramDesc'

    #  Qt's '~QOpenGLProgramBinaryCache::ProgramDesc()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QOpenGLProgramBinaryCache::ProgramDesc behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QOpenGLProgramBinaryCache11ProgramDescD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def cacheKey(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray
      QOpenGLProgramBinaryCache::ProgramDesc::cacheKey() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglprogrambinarycache-programdesc.html

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QOpenGLProgramBinaryCache::ProgramDesc::cacheKey() const
      address = self.uglySide.call(
          'ritual_ZNK25QOpenGLProgramBinaryCache11ProgramDesc8cacheKeyEv',
      )
      from ..QtCore import QByteArray
      return QByteArray._cuteOwning(address)

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

  class ShaderDesc(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpenGLProgramBinaryCache::ShaderDesc: a plain
    Python object standing in front of one C++
    QOpenGLProgramBinaryCache::ShaderDesc.

    C++ hands a QOpenGLProgramBinaryCache::ShaderDesc around as a copy, so
    every C++ QOpenGLProgramBinaryCache::ShaderDesc behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QOpenGLProgramBinaryCache::ShaderDesc yet. It can be
    made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QOpenGLProgramBinaryCache::ShaderDesc::~ShaderDesc()': the
      destructor: Python removes its C++
      QOpenGLProgramBinaryCache::ShaderDesc by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QOpenGLProgramBinaryCache::ShaderDesc is created at the first
      use, not by 'QOpenGLProgramBinaryCache::ShaderDesc(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOpenGLProgramBinaryCache::ShaderDesc back gives a
      copy the ritual made for Python, in a new cute
      QOpenGLProgramBinaryCache::ShaderDesc.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArray = WAIT['QByteArray']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpenGLProgramBinaryCache::ShaderDesc'

    #  Qt's '~QOpenGLProgramBinaryCache::ShaderDesc()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QOpenGLProgramBinaryCache::ShaderDesc behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QOpenGLProgramBinaryCache10ShaderDescD1Ev')

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
      'QOpenGLProgramBinaryCache::ShaderDesc::ShaderDesc()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglprogrambinarycache-shaderdesc.html
      """
      #  QOpenGLProgramBinaryCache::ShaderDesc::ShaderDesc()
      self._noteCreation(
          QOpenGLProgramBinaryCache.ShaderDesc, lambda: Rituals.call(
              'ritual_ZN25QOpenGLProgramBinaryCache10ShaderDescC1Ev',
          ))

    @overload(QShader.Stage)
    @overload(QShader.Stage, QByteArray)
    def __init__(
        self,
        stage: QShader.Stage,
        source: Optional[QByteArray] = None,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QOpenGLProgramBinaryCache::ShaderDesc::ShaderDesc(QShader::Stage
      stage, const QByteArray &source)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglprogrambinarycache-shaderdesc.html

      Parameters
      ----------

      stage : QShader.Stage
        Passed on as its number.

      source : Optional[QByteArray]
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own. May be left out, as in Qt: a new 'QByteArray()' is then
        passed on.
      """
      #  QOpenGLProgramBinaryCache::ShaderDesc::ShaderDesc(QShader::Stage
      #      stage, const QByteArray &source)
      if source is None:
        from ..QtCore import QByteArray
        source = QByteArray()
      self._noteCreation(
          QOpenGLProgramBinaryCache.ShaderDesc, lambda: Rituals.call(
              'ritual_ZN25QOpenGLProgramBinaryCache10ShaderDescC1EN7QShader'
              '5StageERK10QByteArray',
              stage.value, self._valueOf(source),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLProgramBinaryCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def cacheFileName(self, cacheKey: QByteArray) -> str:
    """
    Calls Qt's 'QString QOpenGLProgramBinaryCache::cacheFileName(const
    QByteArray &cacheKey) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglprogrambinarycache.html#cacheFileName

    Parameters
    ----------

    cacheKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpenGLProgramBinaryCache::cacheFileName(const QByteArray
    #      &cacheKey) const
    return self.uglySide.call(
        'ritual_ZNK25QOpenGLProgramBinaryCache13cacheFileNameERK10QByteArra'
        'y',
        self._valueOf(cacheKey),
    )

  @overload(QByteArray)
  def verifyHeader(self, buf: QByteArray) -> bool:
    """
    Calls Qt's 'bool QOpenGLProgramBinaryCache::verifyHeader(const QByteArray
    &buf) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglprogrambinarycache.html#verifyHeader

    Parameters
    ----------

    buf : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QOpenGLProgramBinaryCache::verifyHeader(const QByteArray &buf)
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QOpenGLProgramBinaryCache12verifyHeaderERK10QByteArray',
        self._valueOf(buf),
    )

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
    'QOpenGLProgramBinaryCache::QOpenGLProgramBinaryCache()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglprogrambinarycache.html
    """
    #  QOpenGLProgramBinaryCache::QOpenGLProgramBinaryCache()
    self._noteCreation(QOpenGLProgramBinaryCache, lambda: Rituals.call(
        'ritual_ZN25QOpenGLProgramBinaryCacheC1Ev',
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

  @overload(QByteArray, int)
  def load(self, cacheKey: QByteArray, programId: int) -> bool:
    """
    Calls Qt's 'bool QOpenGLProgramBinaryCache::load(const QByteArray
    &cacheKey, uint programId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglprogrambinarycache.html#load

    Parameters
    ----------

    cacheKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    programId : int
      Passed on as it is.
    """
    #  bool QOpenGLProgramBinaryCache::load(const QByteArray &cacheKey, uint
    #      programId)
    return self.uglySide.call(
        'ritual_ZN25QOpenGLProgramBinaryCache4loadERK10QByteArrayj',
        self._valueOf(cacheKey), programId,
    )

  @overload(QByteArray, int)
  def save(self, cacheKey: QByteArray, programId: int) -> None:
    """
    Calls Qt's 'void QOpenGLProgramBinaryCache::save(const QByteArray
    &cacheKey, uint programId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglprogrambinarycache.html#save

    Parameters
    ----------

    cacheKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    programId : int
      Passed on as it is.
    """
    #  void QOpenGLProgramBinaryCache::save(const QByteArray &cacheKey, uint
    #      programId)
    self.uglySide.call(
        'ritual_ZN25QOpenGLProgramBinaryCache4saveERK10QByteArrayj',
        self._valueOf(cacheKey), programId,
    )

  @staticmethod
  def setProgramBinary(*__, **_) -> Never:
    """
    Qt's 'bool QOpenGLProgramBinaryCache::setProgramBinary(uint programId,
    uint blobFormat, const void *p, uint blobSize)': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLProgramBinaryCache.setProgramBinary' has no cute function "
        "yet. Qt's 'bool QOpenGLProgramBinaryCache::setProgramBinary(uint "
        "programId, uint blobFormat, const void *p, uint blobSize)': names "
        "'void', which has no cute class yet.")
