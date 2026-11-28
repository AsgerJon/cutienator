"""
QQmlScriptBlob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlscriptblob_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlScriptBlob to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QQmlDataBlob, QQmlNotifyingBlob, QQmlPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlScriptBlob(QQmlNotifyingBlob):
  """
  The cute side of Qt's QQmlScriptBlob: a plain Python object standing in
  front of one C++ QQmlScriptBlob.

  It is built on the cute 'QQmlNotifyingBlob', as Qt's QQmlScriptBlob is
  built on Qt's QQmlNotifyingBlob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlScriptBlob that has a ritual and that Python can
  call so far, 4 names in all: 'dataReceived', 'initializeFromCachedUnit',
  'done', 'stringAt'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlScriptBlob::~QQmlScriptBlob()': the destructor: Python never
    removes a C++ QQmlScriptBlob.
  - Qt's 'QQmlRefPointer<QQmlScriptData> QQmlScriptBlob::scriptData() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QQmlScriptBlob::scriptImported(const
    QQmlRefPointer<QQmlScriptBlob> &blob, const QV4::CompiledData::Location
    &location, const QString &qualifier, const QString &nameSpace)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 leans on 'QQmlThread.

  What to expect
  --------------

  - The C++ QQmlScriptBlob is created at the first use, not by
    'QQmlScriptBlob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlScriptBlob.
  - Each name of Qt's QQmlScriptBlob that has no cute function yet,
    '__init__', 'initializeFromCompilationUnit', 'scriptData', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlScriptBlob, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class IsESModule(CuteNum, scoped=True):
    """
    The enum 'QQmlScriptBlob::IsESModule' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  #  The classes Qt writes inside QQmlScriptBlob, each a class in here as in
  #  C++.

  class ScriptReference(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlScriptBlob::ScriptReference: a plain Python
    object standing in front of one C++ QQmlScriptBlob::ScriptReference.

    C++ hands a QQmlScriptBlob::ScriptReference around as a copy, so every
    C++ QQmlScriptBlob::ScriptReference behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQmlScriptBlob::ScriptReference yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlScriptBlob::ScriptReference::~ScriptReference()': the
      destructor: Python removes its C++ QQmlScriptBlob::ScriptReference by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlScriptBlob::ScriptReference is created at the first use,
      not by 'QQmlScriptBlob::ScriptReference(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlScriptBlob::ScriptReference back gives a copy
      the ritual made for Python, in a new cute
      QQmlScriptBlob::ScriptReference.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlScriptBlob::ScriptReference'

    #  Qt's '~QQmlScriptBlob::ScriptReference()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlScriptBlob::ScriptReference
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QQmlScriptBlob15ScriptReferenceD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlScriptBlob'

  #  A C++ QQmlScriptBlob Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlScriptBlob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def stringAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QQmlScriptBlob::stringAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlscriptblob.html#stringAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlScriptBlob::stringAt(int index) const
    ritual = 'ritual_ZNK14QQmlScriptBlob8stringAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlScriptBlob8stringAtEi'
    return self.uglySide.call(ritual, index)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlScriptBlob::QQmlScriptBlob(const QUrl &url, QQmlTypeLoader
    *typeLoader, IsESModule isESModule)': leans on
    'QQmlThread::isThisThread() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlScriptBlob.__init__' has no cute function yet. Qt's "
        "'QQmlScriptBlob::QQmlScriptBlob(const QUrl &url, QQmlTypeLoader "
        "*typeLoader, IsESModule isESModule)': leans on "
        "'QQmlThread::isThisThread() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QQmlDataBlob.SourceCodeData)
  def dataReceived(self, a0: QQmlDataBlob.SourceCodeData) -> None:
    """
    Calls Qt's 'void QQmlScriptBlob::dataReceived(const SourceCodeData &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlscriptblob.html#dataReceived

    Parameters
    ----------

    a0 : QQmlDataBlob.SourceCodeData
      Passed on as a value: Qt reads the C++ QQmlDataBlob::SourceCodeData,
      which stays Python's own.
    """
    #  void QQmlScriptBlob::dataReceived(const SourceCodeData &a0)
    self.uglySide.call(
        'ritual_ZN14QQmlScriptBlob12dataReceivedERKN12QQmlDataBlob14SourceC'
        'odeDataE',
        self._valueOf(a0),
    )

  @overload(WAIT['QQmlPrivate.CachedQmlUnit'])
  @overload(NoneType)
  def initializeFromCachedUnit(
      self,
      unit: Optional[QQmlPrivate.CachedQmlUnit],
  ) -> None:
    """
    Calls Qt's 'void QQmlScriptBlob::initializeFromCachedUnit(const
    QQmlPrivate::CachedQmlUnit *unit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlscriptblob.html#initializeFromCachedUnit

    Parameters
    ----------

    unit : Optional[QQmlPrivate.CachedQmlUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlScriptBlob::initializeFromCachedUnit(const
    #      QQmlPrivate::CachedQmlUnit *unit)
    self.uglySide.call(
        'ritual_ZN14QQmlScriptBlob24initializeFromCachedUnitEPKN11QQmlPriva'
        'te13CachedQmlUnitE',
        self._addressOf(unit),
    )

  def done(self) -> None:
    """
    Calls Qt's 'void QQmlScriptBlob::done()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlscriptblob.html#done
    """
    #  void QQmlScriptBlob::done()
    self.uglySide.call('ritual_ZN14QQmlScriptBlob4doneEv')

  @staticmethod
  def initializeFromCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlScriptBlob::initializeFromCompilationUnit(QQmlRefPointer<QV4::
    CompiledData::CompilationUnit> &&cu)': leans on
    'QQmlThread::isThisThread() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlScriptBlob.initializeFromCompilationUnit' has no cute "
        "function yet. Qt's 'void "
        "QQmlScriptBlob::initializeFromCompilationUnit(QQmlRefPointer<QV4::C"
        "ompiledData::CompilationUnit> &&cu)': leans on "
        "'QQmlThread::isThisThread() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def scriptData(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlScriptData> QQmlScriptBlob::scriptData() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlScriptBlob.scriptData' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlScriptData> QQmlScriptBlob::scriptData() "
        "const': gives a type Python has no way to take yet.")
