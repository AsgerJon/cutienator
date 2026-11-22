"""Rituals opens cutienator's own shared object and runs its rituals."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
import glob
import json
import os
import sys
from typing import TYPE_CHECKING

from worktoy.waitaminute import TypeException

from . import Build, System

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  Paths = Tuple[str, ...]
  Row = Tuple[str, ...]


class Rituals:
  """
  Runs the rituals of cutienator's own shared object. Everything is
  called on the class, since a program has one such shared object.

    Rituals.build()        # after a ritual file changed
    Rituals.call('ritual_ZNK7QObject6parentEv', address)  # run one
    Rituals.call('ritual_ZNK7QObject10objectNameEv', address)  # a str

  Terms
  -----

  - A ritual is one function of ours that Python can call, and that
    calls one Qt function. It is named 'ritual' followed by the
    compiler's own name for that Qt function, which has the types it
    takes packed into it: 'ritual_ZNK7QObject6parentEv' calls
    'QObject::parent()'. Its ritual file and its rows file name it.
  - A ritual file is a C++ file holding rituals, in the ritual folder.
  - The rows file of a ritual file lies beside it, under the same name
    with the ending '.json'. It holds one row for each ritual: one word
    for what comes back from it, then one word for each thing that goes
    into it. 'q_object.json' goes with 'q_object.cpp'.
  - The target file is the shared object built from the ritual files.

  You provide
  -----------

  Nothing at run time. To add rituals, put a ritual file and its rows
  file into the ritual folder, then call 'build'. The program
  'dev_tooling.RitualGenerator' writes the two together, from one plan,
  so they agree.

  Found for you
  -------------

  - 'getRitualFolder': the folder 'rituals' beside this module.
  - 'getRitualFiles': every C++ file in that folder.
  - 'getRowsFiles': the rows file of each of them.
  - 'getRows': every row of those files, under the name of its ritual.
  - 'getTargetFile': 'libcutienator.so' in that folder.
  - 'getQtSharedObjects': the Qt shared objects the rituals call into.

  The words of a row
  ------------------

  - 'nothing': nothing comes back.
  - 'address': where a C++ object is. It crosses as an 'int', or as
    'None' for no object.
  - 'text': Qt's QString. It crosses as a plain 'str', both ways. For
    the call a C++ QString is made from the 'str', and removed again
    when the ritual has run. A QString coming back is read into a 'str'
    and removed.
  - 'chars': text as C has it. It crosses as 'bytes', or 'None'.
  - A number goes by the name C++ has for it, as 'int', 'bool' and
    'long long', and 'size_t' for the number of that name.

  What to expect
  --------------

  - Nothing is compiled unless 'build' is called. 'call' refuses to run
    when the target file is missing, or older than a ritual file.
  - The target file is opened at the first 'call', once.
  - A ritual that no rows file lists, or that the target file does not
    offer, raises 'LookupError' naming it.
  - Anything but a 'str' in the place of text is refused here, with
    'TypeException'. No other wrong argument is caught here. C++ takes
    what it is given, and a wrong address ends the whole program.

  This class stands in for the metaclass that is planned to collect the
  shared objects.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  What each word of a row is to 'ctypes', which does the calling.
  #  'ctypes.c_void_p' means a number as wide as an address, and nothing
  #  more: it checks nothing and knows nothing of what the number is for.
  #  Text crosses as the address of a QString.
  __row_words__ = {
      'nothing': None,
      'address': ctypes.c_void_p,
      'text': ctypes.c_void_p,
      'chars': ctypes.c_char_p,
      'bool': ctypes.c_bool,
      'char': ctypes.c_char,
      'signed char': ctypes.c_byte,
      'unsigned char': ctypes.c_ubyte,
      'short': ctypes.c_short,
      'unsigned short': ctypes.c_ushort,
      'int': ctypes.c_int,
      'unsigned int': ctypes.c_uint,
      'long': ctypes.c_long,
      'unsigned long': ctypes.c_ulong,
      'long long': ctypes.c_longlong,
      'unsigned long long': ctypes.c_ulonglong,
      'size_t': ctypes.c_size_t,
      'float': ctypes.c_float,
      'double': ctypes.c_double,
  }  # type: Dict[str, Any]

  #  The four rituals of Qt's QString that a 'str' crosses by: the one
  #  making a QString from letters, the two reading one, and the one
  #  removing it.
  __text_make_ritual__ = 'ritual_ZN7QStringC1EPK5QCharx'
  __text_size_ritual__ = 'ritual_ZNK7QString4sizeEv'
  __text_data_ritual__ = 'ritual_ZNK7QString9constDataEv'
  __text_drop_ritual__ = 'ritual_ZN7QStringD1Ev'

  #  How a QString keeps its letters: two bytes for each, in the order
  #  the machine keeps the bytes of a number.
  __text_encoding__ = dict(
      little='utf-16-le', big='utf-16-be',
  )[sys.byteorder]

  #  The parts of Qt the rituals call into. 'System' knows the file of
  #  each part on the system Python runs on.
  __qt_parts__ = ('QtCore', 'QtGui', 'QtWidgets')

  #  Every row of the rows files, or None until they are read.
  __ritual_rows__ = None  # type: Optional[Dict[str, Row]]

  #  The opened target file, or None until the first call.
  __opened_target__ = None  # type: Optional[ctypes.CDLL]

  #  The texts a program was started with, each time they were handed to
  #  Qt, kept so that Python never removes them.
  __start_texts__ = []  # type: List[Any]

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def getRitualFolder(cls) -> str:
    """
    Gives the folder holding the ritual files.

    Found for you: it is the folder 'rituals' beside this module. The
    ritual files of each part of Qt lie in a folder of their own in it,
    named after the part: 'QtCoreRituals', 'QtGuiRituals' and
    'QtWidgetsRituals'. See 'getPartFolder'.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, 'rituals')

  @classmethod
  def getPartFolder(cls, partName: str) -> str:
    """
    Gives the folder holding the ritual files of one part of Qt.

    Parameters
    ----------

    partName : str
      The part of Qt, as 'QtCore'.

    Returns
    -------

    str
      The full path, ending in 'rituals/QtCoreRituals' for 'QtCore'.
      Having the path does not mean the folder is there.
    """
    return os.path.join(cls.getRitualFolder(), '%sRituals' % partName)

  @classmethod
  def getRitualFiles(cls) -> Paths:
    """
    Gives the ritual files that 'build' compiles.

    Found for you: every file ending in '.cpp' in the folder of a part
    of Qt in the ritual folder, part by part and in alphabetical order.
    Putting a file there is all it takes.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths.
    """
    pattern = os.path.join(cls.getRitualFolder(), '*Rituals', '*.cpp')
    return (*sorted(glob.glob(pattern)),)

  @classmethod
  def getTargetFile(cls) -> str:
    """
    Gives the path of cutienator's own shared object.

    Found for you: 'libcutienator.so' beside the ritual folder, so
    that nothing built lies among the ritual files. Having the path
    does not mean the file is there; 'build' makes it.
    """
    here = os.path.dirname(cls.getRitualFolder())
    return os.path.join(here, 'libcutienator.so')

  @classmethod
  def getQtSharedObjects(cls) -> Paths:
    """
    Gives the Qt shared objects the rituals call into.

    Found for you: one file for each part of Qt in '__qt_parts__', in
    the folder where Qt keeps its shared objects. 'System' gives the
    name the file has on the system Python runs on, which on Linux is
    'libQt6Core.so.6' for 'QtCore'.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths.
    """
    folder = Build.getQtSharedObjectFolder()
    system = System.getHere()
    names = (*(system.getQtFileName(part) for part in cls.__qt_parts__),)
    return (*(os.path.join(folder, name) for name in names),)

  @classmethod
  def getRowsFiles(cls) -> Paths:
    """
    Gives the rows file of each ritual file, in the order of
    'getRitualFiles'.

    Found for you: the path of the ritual file with '.json' in the place
    of '.cpp'. Having the path does not mean the file is there.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths.
    """
    stems = (os.path.splitext(path)[0] for path in cls.getRitualFiles())
    return (*('%s.json' % stem for stem in stems),)

  @classmethod
  def _createRows(cls) -> None:
    """
    Reads every rows file and keeps the rows.

    Raises
    ------

    FileNotFoundError
      A ritual file has no rows file beside it.

    ValueError
      A row holds a word that is none of the words of a row, or two rows
      files list one ritual.
    """
    rows = dict()  # type: Dict[str, Row]
    ritualFiles = cls.getRitualFiles()
    for ritualFile, rowsFile in zip(ritualFiles, cls.getRowsFiles()):
      if not os.path.isfile(rowsFile):
        infoSpec = """The ritual file '%s' has no rows file '%s' beside
        it. 'dev_tooling.RitualGenerator' writes the two together."""
        info = infoSpec % (ritualFile, os.path.basename(rowsFile))
        raise FileNotFoundError(' '.join(info.split()))
      with open(rowsFile) as file:
        written = json.load(file)['rows']
      for name, row in written.items():
        for word in row:
          if word not in cls.__row_words__:
            infoSpec = """The row of '%s' in '%s' holds '%s', which is no
            word of a row. The words are: %s."""
            words = ', '.join(cls.__row_words__)
            info = infoSpec % (name, rowsFile, word, words)
            raise ValueError(' '.join(info.split()))
        if name in rows:
          infoSpec = """The ritual '%s' is listed a second time, in
          '%s'."""
          raise ValueError(' '.join((infoSpec % (name, rowsFile)).split()))
        rows[name] = (*row,)
    cls.__ritual_rows__ = rows

  @classmethod
  def getRows(cls, **kwargs) -> Dict[str, Row]:
    """
    Gives the row of every ritual, under the name of the ritual.

    Found for you: the rows files are read at the first call, and the
    rows are kept. You pass nothing; the keyword is for the method's own
    use.

    Returns
    -------

    Dict[str, Row]
      A 'Dict[str, Tuple[str, ...]]'. Under
      'ritual_ZN7QObject12blockSignalsEb' it holds
      ('bool', 'address', 'bool'): a 'bool' comes back, and the address
      of the object and a 'bool' go in.

    Raises
    ------

    FileNotFoundError
      A ritual file has no rows file beside it.

    ValueError
      A rows file holds a word that is no word of a row, or lists a
      ritual another rows file lists.
    """
    if cls.__ritual_rows__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createRows()
      return cls.getRows(_recursion=True)
    return cls.__ritual_rows__

  @classmethod
  def getRitualNames(cls) -> Tuple[str, ...]:
    """Gives the name of every ritual the rows files list."""
    return (*cls.getRows(),)

  @classmethod
  def isStale(cls) -> bool:
    """
    Says whether 'build' has to be called before any ritual can run.

    Returns
    -------

    bool
      True when the target file is missing, or when a ritual file was
      changed after the target file was made.
    """
    target = cls.getTargetFile()
    if not os.path.isfile(target):
      return True
    made = os.path.getmtime(target)
    for ritualFile in cls.getRitualFiles():
      if os.path.getmtime(ritualFile) > made:
        return True
    return False

  @classmethod
  def _createOpened(cls) -> None:
    """Opens the target file and readies every listed ritual."""
    target = cls.getTargetFile()
    if cls.isStale():
      infoSpec = """The shared object '%s' is missing, or older than a
      ritual file. Call 'Rituals.build()' first."""
      raise FileNotFoundError(' '.join((infoSpec % target).split()))
    rows = cls.getRows()
    if any('text' in row for row in rows.values()):
      #  Text crosses by four rituals of QString. Without their rows a
      #  'str' could be handed to C++ and never be made into a QString.
      for name in cls._getTextRituals():
        if name not in rows:
          infoSpec = """A ritual takes or gives text, and the ritual '%s'
          that text crosses by is listed in no rows file. The ritual
          file of Qt's QString is missing from '%s'."""
          info = infoSpec % (name, cls.getRitualFolder())
          raise LookupError(' '.join(info.split()))
    System.getHere().prepareOpening()
    opened = ctypes.CDLL(target)
    words = cls.__row_words__
    for name, (gives, *takes) in rows.items():
      try:
        ritual = getattr(opened, name)
      except AttributeError as attributeError:
        infoSpec = """The ritual '%s' is listed in a rows file, but '%s'
        does not offer it. No ritual file defines it."""
        info = ' '.join((infoSpec % (name, target)).split())
        raise LookupError(info) from attributeError
      ritual.restype = words[gives]
      ritual.argtypes = [words[take] for take in takes]
    cls.__opened_target__ = opened

  @classmethod
  def _getTextRituals(cls) -> Tuple[str, ...]:
    """Gives the names of the four rituals that text crosses by."""
    return (
        cls.__text_make_ritual__, cls.__text_size_ritual__,
        cls.__text_data_ritual__, cls.__text_drop_ritual__,
    )

  @classmethod
  def getOpened(cls, **kwargs) -> ctypes.CDLL:
    """
    Gives the opened target file.

    Found for you: it is opened at the first call and kept. You pass
    nothing; the keyword is for the method's own use. 'call' is the
    usual way in, and this is here for what 'call' does not cover.

    Raises
    ------

    FileNotFoundError
      The target file is missing, or older than a ritual file.

    LookupError
      A listed ritual is not offered by the target file, or text is
      taken or given and the rituals of Qt's QString are not listed.
    """
    if cls.__opened_target__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createOpened()
      return cls.getOpened(_recursion=True)
    return cls.__opened_target__

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

  @classmethod
  def keepStartTexts(cls, texts: Any) -> Tuple[int, int]:
    """
    Gives what Qt takes for the texts a program was started with, as
    'sys.argv': the address of their count, and the address of the
    first of them as C has text.

    Qt's application reads both for as long as it lives, and may change
    them. So they are kept here for as long as Python runs.

    Parameters
    ----------

    texts : Any
      A list or tuple of 'str'.

    Returns
    -------

    Tuple[int, int]
      The two addresses, in the order Qt takes them.

    Raises
    ------

    TypeException
      'texts' is no list or tuple, or one of them is not a 'str'.
    """
    if not isinstance(texts, (list, tuple)):
      raise TypeException('texts', texts, list, tuple)
    encoded = []
    for text in texts:
      if not isinstance(text, str):
        raise TypeException('text', text, str)
      encoded.append(text.encode())
    count = ctypes.c_int(len(encoded))
    #  C ends such a row of texts with one that is nowhere.
    row = (ctypes.c_char_p * (len(encoded) + 1))(*encoded, None)
    cls.__start_texts__.append((count, row))
    return ctypes.addressof(count), ctypes.addressof(row)

  @classmethod
  def _makeText(cls, text: Any) -> int:
    """
    Makes a C++ QString holding the letters of a 'str', and gives its
    address. Whoever calls this removes the QString with '_dropText'.

    Every 'str' can be made into one, also one holding half of a pair
    of surrogates, which a QString may hold as well.

    Raises
    ------

    TypeException
      'text' is not a 'str'.
    """
    if not isinstance(text, str):
      raise TypeException('text', text, str)
    letters = text.encode(cls.__text_encoding__, 'surrogatepass')
    make = getattr(cls.getOpened(), cls.__text_make_ritual__)
    return make(letters, len(letters) // 2)

  @classmethod
  def _readText(cls, address: int) -> str:
    """Gives the letters of the C++ QString at an address as a 'str'."""
    opened = cls.getOpened()
    size = getattr(opened, cls.__text_size_ritual__)(address)
    data = getattr(opened, cls.__text_data_ritual__)(address)
    letters = ctypes.string_at(data, 2 * size)
    return letters.decode(cls.__text_encoding__, 'surrogatepass')

  @classmethod
  def _dropText(cls, address: int) -> None:
    """Removes the C++ QString at an address, which '_makeText' or a
    ritual giving text made for this one call."""
    getattr(cls.getOpened(), cls.__text_drop_ritual__)(address)

  @classmethod
  def _callWithText(cls, ritual: Any, row: Row, args: Tuple) -> Any:
    """
    Runs a ritual that takes or gives text.

    A QString is made from each 'str' standing where the row says
    'text'. The ritual then runs. A QString it gives back is read into
    a 'str'. Every QString made for the call, the one given back
    included, is removed before this returns, also when something
    raises on the way.

    Parameters
    ----------

    ritual : Any
      The ritual, as the opened target file gives it.

    row : Row
      Its row.

    args : Tuple
      What goes into it, a 'str' in each place of text.
    """
    gives, takes = row[0], row[1:]
    made = []  # type: List[int]
    try:
      passed = []
      for index, arg in enumerate(args):
        if index < len(takes) and takes[index] == 'text':
          arg = cls._makeText(arg)
          made.append(arg)
        passed.append(arg)
      back = ritual(*passed)
      if gives != 'text':
        return back
      made.append(back)
      return cls._readText(back)
    finally:
      for address in made:
        cls._dropText(address)

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

  @classmethod
  def build(cls) -> str:
    """
    Compiles every ritual file into the target file.

    Call it after adding or changing a ritual file, in a Python that has
    not run a ritual yet: a shared object that is already open cannot be
    swapped for a new one. Each ritual file is compiled by itself,
    several at the same time, and only when it changed since the last
    build; see 'Build'.

    Returns
    -------

    str
      The full path of the target file, which now exists.

    Raises
    ------

    RuntimeError
      The target file is already open in this Python, or 'clang++' refused
      a ritual file; its own message is then included.

    FileNotFoundError
      There is no ritual file, or 'clang++' or 'qmake6' is not installed.
    """
    if cls.__opened_target__ is not None:
      infoSpec = """The shared object is already open in this Python and
      cannot be swapped. Build in a Python that has run no ritual."""
      raise RuntimeError(' '.join(infoSpec.split()))
    ritualFiles = cls.getRitualFiles()
    if not ritualFiles:
      infoSpec = """There is no ritual file in '%s'."""
      raise FileNotFoundError(infoSpec % cls.getRitualFolder())
    build = Build()
    build.setRitualFiles(*ritualFiles)
    build.setTargetFile(cls.getTargetFile())
    build.setQtSharedObjects(*cls.getQtSharedObjects())
    return build.run()

  @classmethod
  def call(cls, name: str, *args: Any) -> Any:
    """
    Runs one ritual and gives what comes back.

    Parameters
    ----------

    name : str
      The name of the ritual, as its ritual file has it:
      'ritual_ZNK7QObject6parentEv'. A rows file must list it.

    *args : Any
      What goes into the ritual, in the order the ritual file declares.
      For a ritual on an object, the address of the object comes first.
      An address is an 'int', or 'None' for nowhere. Text is a 'str'.

    Returns
    -------

    Any
      What the ritual returns. An address comes back as an 'int', or as
      'None' when C++ answered nowhere. Text comes back as a 'str'.

    Raises
    ------

    LookupError
      No rows file lists a ritual of that name.

    FileNotFoundError
      The target file is missing, or older than a ritual file.

    TypeException
      Something that is no 'str' stands where the ritual takes text.
    """
    rows = cls.getRows()
    if name not in rows:
      infoSpec = """No rows file in '%s' lists a ritual named '%s'."""
      info = infoSpec % (cls.getRitualFolder(), name)
      raise LookupError(' '.join(info.split()))
    ritual = getattr(cls.getOpened(), name)
    if 'text' in rows[name]:
      return cls._callWithText(ritual, rows[name], args)
    return ritual(*args)
