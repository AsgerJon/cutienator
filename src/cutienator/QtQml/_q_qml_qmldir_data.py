"""
QQmlQmldirData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldirdata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlQmldirData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QQmlDataBlob, QQmlPrivate, QQmlTypeLoader, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlQmldirData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlQmldirData: a plain Python object standing in
  front of one C++ QQmlQmldirData.

  What exists
  -----------

  Every function of Qt's QQmlQmldirData that has a ritual and that Python can
  call so far, 4 names in all: 'content', 'importLocation', 'dataReceived',
  'initializeFromCachedUnit'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 2 leans on 'QQmlThread; 1 a template.

  What to expect
  --------------

  - The C++ QQmlQmldirData is created at the first use, not by
    'QQmlQmldirData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlQmldirData.
  - Each name of Qt's QQmlQmldirData that has no cute function yet,
    '__init__', 'processImports', 'setPriority', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlQmldirData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def content(self) -> str:
    """
    Calls Qt's 'const QString &QQmlQmldirData::content() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlqmldirdata.html#content

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QQmlQmldirData::content() const
    return self.uglySide.call('ritual_ZNK14QQmlQmldirData7contentEv')

  @overload(QQmlTypeLoader.Blob)
  @overload(NoneType)
  def importLocation(
      self,
      blob: Optional[QQmlTypeLoader.Blob],
  ) -> QV4.CompiledData.Location:
    """
    Calls Qt's 'QV4::CompiledData::Location
    QQmlQmldirData::importLocation(Blob *blob) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlqmldirdata.html#importLocation

    Parameters
    ----------

    blob : Optional[QQmlTypeLoader.Blob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.CompiledData.Location
      A new cute QV4::CompiledData::Location around the copy Qt gave back.
      Python owns it.
    """
    #  QV4::CompiledData::Location QQmlQmldirData::importLocation(Blob *blob)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlQmldirData14importLocationEPN14QQmlTypeLoader4Blob'
        'E',
        self._addressOf(blob),
    )
    return QV4.CompiledData.Location._cuteOwning(address)

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
    Qt's 'QQmlQmldirData::QQmlQmldirData(const QUrl &a0, QQmlTypeLoader
    *a1)': leans on 'QQmlThread::isThisThread() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlQmldirData.__init__' has no cute function yet. Qt's "
        "'QQmlQmldirData::QQmlQmldirData(const QUrl &a0, QQmlTypeLoader "
        "*a1)': leans on 'QQmlThread::isThisThread() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
    Calls Qt's 'void QQmlQmldirData::dataReceived(const SourceCodeData &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlqmldirdata.html#dataReceived

    Parameters
    ----------

    a0 : QQmlDataBlob.SourceCodeData
      Passed on as a value: Qt reads the C++ QQmlDataBlob::SourceCodeData,
      which stays Python's own.
    """
    #  void QQmlQmldirData::dataReceived(const SourceCodeData &a0)
    self.uglySide.call(
        'ritual_ZN14QQmlQmldirData12dataReceivedERKN12QQmlDataBlob14SourceC'
        'odeDataE',
        self._valueOf(a0),
    )

  @overload(WAIT['QQmlPrivate.CachedQmlUnit'])
  @overload(NoneType)
  def initializeFromCachedUnit(
      self,
      a0: Optional[QQmlPrivate.CachedQmlUnit],
  ) -> None:
    """
    Calls Qt's 'void QQmlQmldirData::initializeFromCachedUnit(const
    QQmlPrivate::CachedQmlUnit *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlqmldirdata.html#initializeFromCachedUnit

    Parameters
    ----------

    a0 : Optional[QQmlPrivate.CachedQmlUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlQmldirData::initializeFromCachedUnit(const
    #      QQmlPrivate::CachedQmlUnit *a0)
    self.uglySide.call(
        'ritual_ZN14QQmlQmldirData24initializeFromCachedUnitEPKN11QQmlPriva'
        'te13CachedQmlUnitE',
        self._addressOf(a0),
    )

  @staticmethod
  def processImports(*__, **_) -> Never:
    """
    Qt's 'QQmlQmldirData::processImports': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlQmldirData.processImports' has no cute function yet. Qt's "
        "'QQmlQmldirData::processImports': a template: a pattern and no "
        "single function.")

  @staticmethod
  def setPriority(*__, **_) -> Never:
    """
    Qt's 'void QQmlQmldirData::setPriority(Blob *a0, const PendingImportPtr
    &a1, int a2)': leans on 'QQmlThread::isThisThread() const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlQmldirData.setPriority' has no cute function yet. Qt's 'void "
        "QQmlQmldirData::setPriority(Blob *a0, const PendingImportPtr &a1, "
        "int a2)': leans on 'QQmlThread::isThisThread() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
