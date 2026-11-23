"""HeaderFile is one header file of Qt and what it holds."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Contents = Tuple[Record, ...]


class HeaderFile:
  """
  One header file of Qt, and what it holds as the compiler read it.

    for headerFile in headerReader.getHeaderFiles():
      headerFile.getHeaderPath()  # '/usr/include/qt6/QtCore/qobject.h'
      headerFile.getContents()    # a tuple of 40 records

  Terms
  -----

  - A top-level thing is something a header file declares outside of
    everything else: a class, a function, a namespace, another name for
    a type. What a class or a namespace holds is inside it.
  - A record is what the compiler wrote down about one top-level thing,
    as JSON turned into Python: dicts, lists, text and numbers. Its
    entry 'kind' says what the thing is, and 'name' what it is called.
  - The record file is the file the records of this header file are
    kept in, one record per line.

  You provide
  -----------

  Nothing. A 'HeaderReader' fills each header file in, through the setters,
  from the reading of its part of Qt. You read it.

  What to expect
  --------------

  - 'getContents' loads the records from the record file at the first
    call, and keeps them. A big header file takes a second and a good
    deal of memory.
  - A header file holding only macros and '#include' lines gives an
    empty tuple: the compiler writes neither down.
  - A header file the compiler never read has no contents to give.
    'getContents' then raises, and 'getComplaint' says why.
  - Reading a value its setter was never given raises
    'MissingVariable', naming it.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables

  #  Private Variables
  __header_path__ = None  # type: Optional[str]
  __record_path__ = None  # type: Optional[str]
  __was_read__ = None  # type: Optional[bool]
  __compiler_complaint__ = None  # type: Optional[str]
  __record_count__ = None  # type: Optional[int]
  __loaded_contents__ = None  # type: Optional[Contents]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getHeaderPath(self) -> str:
    """
    Gives the full path of the header file, as
    '/usr/include/qt6/QtCore/qobject.h'.

    Filled in by the 'HeaderReader'.
    """
    if self.__header_path__ is None:
      raise MissingVariable(self, '__header_path__', str)
    return self.__header_path__

  def getRecordPath(self) -> str:
    """
    Gives the full path of the record file: where the records of this
    header file are kept, one per line.

    Filled in by the 'HeaderReader'. Having the path does not mean the
    file is there: none is written for a header file with no records.
    """
    if self.__record_path__ is None:
      raise MissingVariable(self, '__record_path__', str)
    return self.__record_path__

  def wasRead(self) -> bool:
    """
    Says whether the compiler read this header file when the part was
    read.

    Filled in by the 'HeaderReader'. It is False for a header file that is in
    no other header and that the compiler refused when handed it
    directly; 'getComplaint' then gives what the compiler said.
    """
    if self.__was_read__ is None:
      raise MissingVariable(self, '__was_read__', bool)
    return self.__was_read__

  def getComplaint(self) -> str:
    """
    Gives what the compiler said when it refused this header file.

    Filled in by the 'HeaderReader'. It is '' for a header file that was
    read.
    """
    if self.__compiler_complaint__ is None:
      raise MissingVariable(self, '__compiler_complaint__', str)
    return self.__compiler_complaint__

  def getRecordCount(self) -> int:
    """
    Gives how many top-level things the header file holds, without
    loading them.

    Filled in by the 'HeaderReader'. It is 0 for a header file holding only
    macros and '#include' lines, and for one that was not read.
    """
    if self.__record_count__ is None:
      raise MissingVariable(self, '__record_count__', int)
    return self.__record_count__

  def _createContents(self, ) -> None:
    """Loads the records of this header file from its record file."""
    headerPath = self.getHeaderPath()
    if not self.wasRead():
      infoSpec = """The compiler did not read '%s', so it has no
      contents to give. The compiler said: %s"""
      info = infoSpec % (headerPath, self.getComplaint() or 'nothing')
      raise RuntimeError(' '.join(info.split()))
    recordCount = self.getRecordCount()
    if not recordCount:
      self.__loaded_contents__ = ()
      return
    recordPath = self.getRecordPath()
    if not os.path.isfile(recordPath):
      infoSpec = """The records of '%s' were expected in '%s', and there
      is no such file. Read the part of Qt again."""
      info = infoSpec % (headerPath, recordPath)
      raise FileNotFoundError(' '.join(info.split()))
    with open(recordPath) as file:
      contents = (*(json.loads(line) for line in file),)
    if len(contents) != recordCount:
      infoSpec = """'%s' was expected to hold %d records, and holds %d.
      Read the part of Qt again."""
      info = infoSpec % (recordPath, recordCount, len(contents))
      raise RuntimeError(' '.join(info.split()))
    self.__loaded_contents__ = contents

  def getContents(self, **kwargs) -> Contents:
    """
    Gives all the contents of the header file: one record per top-level
    thing, in the order the compiler read them.

    Loaded for you from the record file, at the first call, and kept.
    You pass nothing; the keyword is for the method's own use.

    Returns
    -------

    Contents
      A 'Tuple[Dict[str, Any], ...]'. It is empty for a header file
      holding only macros and '#include' lines.

    Raises
    ------

    RuntimeError
      The compiler did not read this header file, or the record file
      does not hold the number of records it should.

    FileNotFoundError
      The record file is gone.
    """
    if self.__loaded_contents__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createContents()
      return self.getContents(_recursion=True)
    return self.__loaded_contents__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setHeaderPath(self, headerPath: str) -> None:
    """Called by the 'HeaderReader' with the full path of the header file."""
    if not isinstance(headerPath, str):
      raise TypeException('headerPath', headerPath, str)
    self.__header_path__ = headerPath

  def setRecordPath(self, recordPath: str) -> None:
    """Called by the 'HeaderReader' with the full path of the record file."""
    if not isinstance(recordPath, str):
      raise TypeException('recordPath', recordPath, str)
    self.__record_path__ = recordPath
    self.__loaded_contents__ = None

  def setRead(self, wasRead: bool) -> None:
    """Called by the 'HeaderReader': did the compiler read the header
    file?"""
    if not isinstance(wasRead, bool):
      raise TypeException('wasRead', wasRead, bool)
    self.__was_read__ = wasRead

  def setComplaint(self, complaint: str) -> None:
    """
    Called by the 'HeaderReader' with what the compiler said when it refused
    the header file, or with '' when it was read.
    """
    if not isinstance(complaint, str):
      raise TypeException('complaint', complaint, str)
    self.__compiler_complaint__ = complaint

  def setRecordCount(self, recordCount: int) -> None:
    """Called by the 'HeaderReader' with the number of top-level things."""
    if isinstance(recordCount, bool) or not isinstance(recordCount, int):
      raise TypeException('recordCount', recordCount, int)
    self.__record_count__ = recordCount
    self.__loaded_contents__ = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Names the header file and says how many records it holds."""
    clsName = type(self).__name__
    if self.__header_path__ is None:
      return '<%s not filled in yet>' % clsName
    if self.__was_read__ is False:
      return "<%s '%s', not read>" % (clsName, self.__header_path__)
    if self.__record_count__ is None:
      return "<%s '%s'>" % (clsName, self.__header_path__)
    infoSpec = """<%s '%s' of %d records>"""
    return infoSpec % (clsName, self.__header_path__, self.__record_count__)

  __repr__ = __str__

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

  def forgetContents(self) -> None:
    """
    Lets go of the records 'getContents' loaded, to free the memory they
    take. The next 'getContents' loads them again.
    """
    self.__loaded_contents__ = None
