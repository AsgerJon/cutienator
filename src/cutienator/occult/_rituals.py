"""Rituals opens cutienator's own shared objects and runs their
rituals."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
import glob
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

from worktoy.waitaminute import TypeException

from . import Summon, System

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

  Paths = Tuple[str, ...]
  Row = Tuple[str, ...]


class Rituals:
  """
  Runs the rituals of cutienator's own shared objects, one for each
  part of Qt. Everything is called on the class, since a program has
  one such shared object for each part.

    Rituals.summon()        # after a ritual file changed
    Rituals.call('ritual_ZNK7QObject6parentEv', address)  # run one
    Rituals.call('ritual_ZNK7QObject10objectNameEv', address)  # a str
    Rituals.callFrom('QtGraphs', 'ritual_ZNK10QBarSeries5countEv', address)

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
  - The target file of a part is the shared object built from the
    ritual files of that part, as 'libcutienator_QtCore.so' from those
    of 'QtCoreRituals'.
  - Two parts may each have a class by one name, as QtCharts and
    QtGraphs each a 'QBarSeries', and so rituals by one name: each
    lies in the target file of its own part, which is joined to the
    shared object of that part of Qt first and opened by itself, so
    the one never sees the other. 'call' runs a ritual only one part
    has. 'callFrom' runs a ritual as a part sees it: its own, else
    that of the first part in its order; see 'getPartOrder'.
  - The rows files of a part whose own header files would find
    another part's file by a bare name, as QtGraphs those of QtCharts,
    say under 'parts first' the parts that part sees first: itself,
    then the parts it needs, the nearest first. Its ritual files were
    made and checked that way, so its target file is built that way.

  You provide
  -----------

  Nothing at run time. To add rituals, put a ritual file and its rows
  file into the ritual folder, then call 'summon'. The program
  'dev_tooling.RitualGenerator' writes the two together, from one plan,
  so they agree.

  Found for you
  -------------

  - 'getRitualFolder': the folder 'rituals' beside this module.
  - 'getRitualFiles': every C++ file in that folder.
  - 'getRowsFiles': the rows file of each of them.
  - 'getRows': every row of the rows files of a part, under the name
    of its ritual.
  - 'getPartsOf': the parts whose rows files list a ritual.
  - 'getPartOrder': the order a part sees the parts in.
  - 'getTargetFile': 'libcutienator_QtCore.so' beside that folder for
    'QtCore', and the same for each part.
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

  - Nothing is compiled unless 'summon' is called. 'call' refuses to run
    when the target file of the part is missing.
  - The target file of a part is opened at the first ritual of that
    part that is called, once.
  - A ritual that no rows file lists raises 'LookupError' naming it,
    and so does one that several parts list, given to 'call'.
  - A ritual a rows file lists and the target file of its part does
    not offer is one the Qt of this machine has no function for: its
    ritual file has it between Qt's own '#if' lines, and they do not
    hold here. The target file opens all the same, and 'call' raises
    'LookupError' for that ritual alone, when it is called. See
    'getMissing'.
  - Anything but a 'str' in the place of text is refused here, with
    'TypeException'. No other wrong argument is caught here. C++ takes
    what it is given, and a wrong address ends the whole program.
  - Qt calls some functions itself while a ritual runs, as 'paintEvent'
    while 'app.exec()' runs, and such a function may be one a class of
    a program wrote in Python. An exception raised in it cannot travel
    up through C++. It is kept and raised by 'call' as soon as the
    ritual Python was in returns. See 'keepException'.

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

  #  The parts of Qt that have cute classes, each a package of
  #  cutienator. The rituals call into more parts: see 'getRitualParts'.
  __components__ = ('QtCore', 'QtGui', 'QtWidgets')

  #  The ritual of Qt's 'QCoreApplication::exit(int)', which tells the
  #  loop of events to stop. See 'keepException'.
  __loop_stop_ritual__ = 'ritual_ZN16QCoreApplication4exitEi'

  #  The exception a Python function raised while Qt was calling it,
  #  until it is raised where Python was. Kept on 'Rituals' itself and
  #  read off it by name, since a program has one. See 'keepException'.
  __kept_exception__ = None  # type: Optional[BaseException]

  #  What a Python function called by Qt gave back last. See 'keepGiven'.
  __kept_given__ = None  # type: Any

  #  The rows of the rows files of each part, under the name of each
  #  ritual, or None until they are read; the parts whose rows files
  #  list each ritual; and what the rows files of each part say under
  #  'parts first'. See '_createRows'.
  __ritual_rows__ = None  # type: Optional[Dict[str, Dict[str, Row]]]
  __ritual_parts__ = None  # type: Optional[Dict[str, Paths]]
  __parts_first__ = None  # type: Optional[Dict[str, Paths]]

  #  The key of the rows files that names the parts a part sees first.
  __parts_first_key__ = 'parts first'

  #  The part of Qt whose target file has the rituals text crosses by,
  #  and the one that stops the loop of events.
  __text_part__ = 'QtCore'

  #  The opened target file of each part, once opened.
  __opened_targets__ = dict()  # type: Dict[str, ctypes.CDLL]
  #  For each opened part, the rituals its rows files list and its
  #  target file does not offer; see 'getMissing'.
  __missing_rituals__ = dict()  # type: Dict[str, FrozenSet[str]]
  #  The part 'callFrom' found for a ritual several parts list, under
  #  the part it was seen from and the name of the ritual.
  __seen_parts__ = dict()  # type: Dict[Tuple[str, str], str]
  #  Whether the system was readied for opening a target file.
  __opening_ready__ = False

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
    named after the part, as 'QtCoreRituals' and 'QtNetworkRituals'.
    See 'getPartFolder' and 'getRitualParts'.
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
    Gives every ritual file of the package. 'summon' compiles those of
    the parts the Qt of this machine has; see 'getBuiltRitualFiles'.

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
  def getBuiltRitualFiles(cls) -> Paths:
    """
    Gives the ritual files that 'summon' compiles: those of
    'getRitualFiles' of the parts the Qt of this machine has, as
    'getInstalledParts' finds them. Those of a part it lacks, as Qt3D
    where it is not installed, are left out, and their rituals raise
    when called; see 'call'.
    """
    installed = {*cls.getInstalledParts()}
    return (*(
        path for path in cls.getRitualFiles()
        if cls._getPartOf(path) in installed),)

  @classmethod
  def getPartRitualFiles(cls, partName: str) -> Paths:
    """Gives the ritual files of one part of Qt, as those of
    'getRitualFiles' in the folder 'QtCoreRituals' for 'QtCore', in
    alphabetical order. A part with no such folder has none."""
    pattern = os.path.join(cls.getPartFolder(partName), '*.cpp')
    return (*sorted(glob.glob(pattern)),)

  @staticmethod
  def _getPartOf(ritualFile: str) -> str:
    """Gives the part of Qt a ritual file is of, as 'QtCore' for
    '.../QtCoreRituals/q_object.cpp'."""
    return os.path.basename(os.path.dirname(ritualFile))[:-len('Rituals')]

  @classmethod
  def getTargetFile(cls, partName: str) -> str:
    """
    Gives the path of cutienator's own shared object of one part of
    Qt, built from the ritual files of that part.

    Found for you: 'libcutienator_QtCore.so' beside the ritual folder
    for 'QtCore', so that nothing built lies among the ritual files.
    Having the path does not mean the file is there; 'summon' makes it.

    Raises
    ------

    TypeException
      'partName' is not a 'str'.
    """
    if not isinstance(partName, str):
      raise TypeException('partName', partName, str)
    here = os.path.dirname(cls.getRitualFolder())
    return os.path.join(here, 'libcutienator_%s.so' % partName)

  @classmethod
  def getTargetFiles(cls) -> Paths:
    """Gives the target file of each part 'summon' builds one for: each
    part of 'getInstalledParts' that has ritual files, in that
    order."""
    return (*(cls.getTargetFile(part) for part in cls.getBuiltParts()),)

  @classmethod
  def getBuiltParts(cls) -> Paths:
    """Gives the parts of 'getInstalledParts' that have ritual files,
    in that order: those 'summon' builds a target file for."""
    built = {cls._getPartOf(path) for path in cls.getBuiltRitualFiles()}
    return (*(part for part in cls.getInstalledParts() if part in built),)

  @classmethod
  def getComponents(cls) -> Paths:
    """Gives the parts of Qt that have cute classes, as 'QtCore'. Each
    is a package of cutienator, holding the cute classes of that part.
    The rituals may call into more parts; see 'getRitualParts'."""
    return cls.__components__

  @classmethod
  def getRitualParts(cls) -> Paths:
    """
    Gives the parts of Qt the rituals call into, as 'QtCore', in
    alphabetical order.

    Found for you: one for each folder of the ritual folder named
    after a part, as 'QtNetworkRituals' for 'QtNetwork'. The shared
    object of each is linked to cutienator's own; see
    'getQtSharedObjects'.
    """
    pattern = os.path.join(cls.getRitualFolder(), 'Qt*Rituals')
    found = []  # type: List[str]
    for folder in glob.glob(pattern):
      if os.path.isdir(folder):
        found.append(os.path.basename(folder)[:-len('Rituals')])
    #  By the names of the parts, as the dev tooling orders them:
    #  'QtCharts' before 'QtChartsQml', whose folders are the other way.
    return (*sorted(found),)

  @classmethod
  def getInstalledParts(cls) -> Paths:
    """
    Gives the parts of 'getRitualParts' the Qt of this machine has, in
    the same order: its shared object is in the folder where Qt keeps
    them, or, for a part of header files alone as QtUiPlugin, its
    folder of header files is in Qt's header folder. The ritual files
    of the others are not built here.
    """
    folder = Summon.getQtSharedObjectFolder()
    headers = Summon.getQtHeaderFolder()
    system = System.getHere()
    found = []  # type: List[str]
    for part in cls.getRitualParts():
      shared = os.path.join(folder, system.getQtFileName(part))
      if os.path.exists(shared) or os.path.isdir(
          os.path.join(headers, part)):
        found.append(part)
    return (*found,)

  @classmethod
  def getQtSharedObjects(cls) -> Paths:
    """
    Gives the Qt shared objects the rituals call into.

    Found for you: the file of each part of 'getInstalledParts' that
    has one, in the folder where Qt keeps its shared objects. 'System'
    gives the name the file has on the system Python runs on, which on
    Linux is 'libQt6Core.so.6' for 'QtCore'. A part of header files
    alone, as QtUiPlugin, has none.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths.
    """
    return cls._findSharedObjects(cls.getInstalledParts())

  @classmethod
  def _findSharedObjects(cls, partNames: Paths) -> Paths:
    """Gives the Qt shared object of each part named that has one
    here, in the order named."""
    folder = Summon.getQtSharedObjectFolder()
    system = System.getHere()
    paths = (
        os.path.join(folder, system.getQtFileName(part))
        for part in partNames)
    return (*(path for path in paths if os.path.exists(path)),)

  @classmethod
  def getPartsFirst(cls, partName: str) -> Paths:
    """
    Gives the parts a part of Qt sees first, as the rows files of its
    ritual files name them under 'parts first': itself, then the parts
    it needs, the nearest first. Only a part whose own header files
    would find another part's file by a bare name has them, as
    QtGraphs, which would find QtCharts' 'qabstractseries_p.h'. For
    any other part it is empty.

    Raises
    ------

    LookupError
      The ritual folder has no folder of that part.
    """
    cls.getRows(partName)
    return cls.__parts_first__[partName]

  @classmethod
  def getPartOrder(cls, partName: str) -> Paths:
    """
    Gives the order a part of Qt sees the parts in: the part itself,
    then those of 'getPartsFirst', then the other parts of
    'getInstalledParts', in alphabetical order. The target file of the
    part is joined to their shared objects in that order, so a
    function two of them offer by one name is taken from the first;
    and 'callFrom' finds a ritual several parts list by it.

    Raises
    ------

    LookupError
      The ritual folder has no folder of that part.
    """
    order = [partName]
    for part in (*cls.getPartsFirst(partName), *cls.getInstalledParts()):
      if part not in order:
        order.append(part)
    return (*order,)

  @classmethod
  def getPartSharedObjects(cls, partName: str) -> Paths:
    """Gives the Qt shared objects the target file of a part is joined
    to: those of 'getQtSharedObjects', in the order of
    'getPartOrder'."""
    return cls._findSharedObjects(cls.getPartOrder(partName))

  @classmethod
  def getPartComponents(cls, partName: str) -> Paths:
    """
    Gives the parts the build of the target file of a part looks in
    the folders of the private headers of, in the order the ritual
    files of the part were made and checked with: those of
    'getPartsFirst', then every folder of Qt's header folder, in
    alphabetical order, as 'QtCharts' and 'QtScxmlGlobal'. The build
    leaves out a folder that is not there; see
    'Summon.getPrivateIncludeFolders'. So a part with ritual files
    coming or going changes nothing for the others.
    """
    names = sorted(os.listdir(Summon.getQtHeaderFolder()))
    order = [*cls.getPartsFirst(partName)]
    order.extend(name for name in names if name not in order)
    return (*order,)

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
    Reads every rows file and keeps the rows, part by part.

    Raises
    ------

    FileNotFoundError
      A ritual file has no rows file beside it.

    ValueError
      A row holds a word that is none of the words of a row, two rows
      files of one part list one ritual, or the rows files of one part
      do not all say the same under 'parts first'.
    """
    rows = dict()  # type: Dict[str, Dict[str, Row]]
    named = dict()  # type: Dict[str, List[str]]
    partsFirst = dict()  # type: Dict[str, Paths]
    saidBy = dict()  # type: Dict[str, str]
    key = cls.__parts_first_key__
    for partName in cls.getRitualParts():
      rows[partName] = dict()
      for ritualFile in cls.getPartRitualFiles(partName):
        rowsFile = '%s.json' % os.path.splitext(ritualFile)[0]
        if not os.path.isfile(rowsFile):
          infoSpec = """The ritual file '%s' has no rows file '%s'
          beside it. 'dev_tooling.RitualGenerator' writes the two
          together."""
          info = infoSpec % (ritualFile, os.path.basename(rowsFile))
          raise FileNotFoundError(' '.join(info.split()))
        with open(rowsFile) as file:
          written = json.load(file)
        said = (*written.get(key, ()),)
        if partName not in partsFirst:
          partsFirst[partName], saidBy[partName] = said, rowsFile
        elif said != partsFirst[partName]:
          infoSpec = """The rows files '%s' and '%s' of %s say different
          things under '%s': the ritual files of a part are made with
          one order of the parts, and are written again together."""
          info = infoSpec % (saidBy[partName], rowsFile, partName, key)
          raise ValueError(' '.join(info.split()))
        for name, row in written['rows'].items():
          for word in row:
            if word not in cls.__row_words__:
              infoSpec = """The row of '%s' in '%s' holds '%s', which is
              no word of a row. The words are: %s."""
              words = ', '.join(cls.__row_words__)
              info = infoSpec % (name, rowsFile, word, words)
              raise ValueError(' '.join(info.split()))
          if name in rows[partName]:
            infoSpec = """The ritual '%s' is listed a second time in %s,
            in '%s'."""
            info = infoSpec % (name, partName, rowsFile)
            raise ValueError(' '.join(info.split()))
          rows[partName][name] = (*row,)
          named.setdefault(name, []).append(partName)
      partsFirst.setdefault(partName, ())
    cls.__parts_first__ = partsFirst
    cls.__ritual_parts__ = {
        name: (*parts,) for name, parts in named.items()}
    cls.__ritual_rows__ = rows

  @classmethod
  def getRows(cls, partName: str, **kwargs) -> Dict[str, Row]:
    """
    Gives the row of every ritual the rows files of one part of Qt
    list, under the name of the ritual.

    Found for you: the rows files are read at the first call, and the
    rows are kept. The keyword is for the method's own use.

    Parameters
    ----------

    partName : str
      The part of Qt, as 'QtCore'.

    Returns
    -------

    Dict[str, Row]
      A 'Dict[str, Tuple[str, ...]]'. Under
      'ritual_ZN7QObject12blockSignalsEb' the rows of QtCore hold
      ('bool', 'address', 'bool'): a 'bool' comes back, and the address
      of the object and a 'bool' go in.

    Raises
    ------

    LookupError
      The ritual folder has no folder of that part.

    FileNotFoundError
      A ritual file has no rows file beside it.

    ValueError
      A rows file holds a word that is no word of a row, or lists a
      ritual another rows file of its part lists; see '_createRows'.
    """
    if cls.__ritual_rows__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createRows()
      return cls.getRows(partName, _recursion=True)
    if partName not in cls.__ritual_rows__:
      infoSpec = """The ritual folder '%s' has no folder of ritual files
      of a part named '%s'."""
      info = infoSpec % (cls.getRitualFolder(), partName)
      raise LookupError(' '.join(info.split()))
    return cls.__ritual_rows__[partName]

  @classmethod
  def getPartsOf(cls, ritualName: str) -> Paths:
    """
    Gives the parts of Qt whose rows files list a ritual, in
    alphabetical order: one for most, as 'QtCore' for
    'ritual_ZNK7QObject6parentEv', two for a ritual of a class two
    parts each have, and none for a name no rows file lists.
    """
    if cls.__ritual_parts__ is None:
      cls._createRows()
    return cls.__ritual_parts__.get(ritualName, ())

  @classmethod
  def getRitualNames(cls) -> Tuple[str, ...]:
    """Gives the name of every ritual the rows files list, once each,
    part by part in alphabetical order."""
    if cls.__ritual_parts__ is None:
      cls._createRows()
    return (*cls.__ritual_parts__,)

  @classmethod
  def isStale(cls) -> bool:
    """
    Says whether 'summon' has to be called before every ritual can run.

    Returns
    -------

    bool
      True when the target file of a part of 'getBuiltParts' is
      missing, or when a ritual file of that part was changed after
      its target file was made.
    """
    for partName in cls.getBuiltParts():
      target = cls.getTargetFile(partName)
      if not os.path.isfile(target):
        return True
      made = os.path.getmtime(target)
      for ritualFile in cls.getPartRitualFiles(partName):
        if os.path.getmtime(ritualFile) > made:
          return True
    return False

  @classmethod
  def _checkTextRituals(cls, partName: str) -> None:
    """
    Makes sure text can cross for the rituals of a part: when one of
    them takes or gives text, the four rituals of Qt's QString that
    text crosses by must be listed in the rows files of QtCore, whose
    target file runs them. Without them a 'str' could be handed to
    C++ and never be made into a QString.

    Raises
    ------

    LookupError
      A ritual of the part takes or gives text, and one of the four is
      not listed for QtCore.
    """
    rows = cls.getRows(partName)
    if not any('text' in row for row in rows.values()):
      return
    textPart = cls.__text_part__
    for name in cls._getTextRituals():
      if textPart not in cls.getPartsOf(name):
        infoSpec = """A ritual of %s takes or gives text, and the ritual
        '%s' that text crosses by is listed in no rows file of %s. The
        ritual file of Qt's QString is missing from '%s'."""
        info = infoSpec % (
            partName, name, textPart, cls.getPartFolder(textPart))
        raise LookupError(' '.join(info.split()))

  @classmethod
  def _createOpened(cls, partName: str) -> None:
    """Opens the target file of a part and readies every ritual its
    rows files list."""
    rows = cls.getRows(partName)
    cls._checkTextRituals(partName)
    if partName not in cls.getInstalledParts():
      infoSpec = """%s is not installed here, so there is no target file
      of it to open, and its rituals cannot run."""
      raise LookupError(' '.join((infoSpec % partName).split()))
    target = cls.getTargetFile(partName)
    if not os.path.isfile(target):
      infoSpec = """The shared object '%s' is missing. Call
      'Rituals.summon()' first."""
      raise FileNotFoundError(' '.join((infoSpec % target).split()))
    if not cls.__opening_ready__:
      System.getHere().prepareOpening()
      cls.__opening_ready__ = True
    opened = ctypes.CDLL(target)
    words = cls.__row_words__
    missing = set()  # type: Set[str]
    for name, (gives, *takes) in rows.items():
      try:
        ritual = getattr(opened, name)
      except AttributeError:
        #  Its ritual file has it between Qt's own '#if' lines, which
        #  do not hold for the Qt of this machine. It raises when
        #  called.
        missing.add(name)
        continue
      ritual.restype = words[gives]
      ritual.argtypes = [words[take] for take in takes]
    if partName == cls.__text_part__:
      for name in cls._getTextRituals():
        if name in missing:
          infoSpec = """The ritual '%s', by which text crosses, is listed
          in a rows file, and '%s' does not offer it."""
          info = infoSpec % (name, target)
          raise LookupError(' '.join(info.split()))
    cls.__missing_rituals__[partName] = frozenset(missing)
    cls.__opened_targets__[partName] = opened

  @classmethod
  def _getTextRituals(cls) -> Tuple[str, ...]:
    """Gives the names of the four rituals that text crosses by."""
    return (
        cls.__text_make_ritual__, cls.__text_size_ritual__,
        cls.__text_data_ritual__, cls.__text_drop_ritual__,
    )

  @classmethod
  def getOpened(cls, partName: str, **kwargs) -> ctypes.CDLL:
    """
    Gives the opened target file of one part of Qt.

    Found for you: it is opened at the first call for that part and
    kept. The keyword is for the method's own use. 'call' is the usual
    way in, and this is here for what 'call' does not cover.

    Parameters
    ----------

    partName : str
      The part of Qt, as 'QtCore'.

    Raises
    ------

    FileNotFoundError
      The target file is missing.

    LookupError
      The ritual folder has no folder of that part, or the part is not
      installed here; or text is taken or given and the rituals of Qt's
      QString are not listed for QtCore, or not offered by its target
      file.
    """
    opened = cls.__opened_targets__.get(partName, None)
    if opened is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createOpened(partName)
      return cls.getOpened(partName, _recursion=True)
    return opened

  @classmethod
  def getMissing(cls, partName: str) -> FrozenSet[str]:
    """
    Gives the name of every ritual the rows files of one part of Qt
    list and the Qt of this machine has no function for. For a part
    not installed here, which 'summon' leaves out, that is every one of
    them. For one installed, those its target file does not offer:
    their ritual files have them between Qt's own '#if' lines, which
    do not hold here, so 'summon' compiled them out.

    Found for you: for an installed part, when its target file is
    opened, as 'getOpened' does.

    Raises
    ------

    LookupError
      The ritual folder has no folder of that part.
    """
    rows = cls.getRows(partName)
    if partName not in cls.getInstalledParts():
      return frozenset(rows)
    cls.getOpened(partName)
    return cls.__missing_rituals__[partName]

  @classmethod
  def hasKeptException(cls) -> bool:
    """
    Says whether an exception is kept that is still to be raised.

    Found for you: 'keepException' keeps one, and 'call' raises it and
    keeps it no more. While one is kept, no further Python function is
    asked by Qt.
    """
    return False if Rituals.__kept_exception__ is None else True

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
    make = getattr(
        cls.getOpened(cls.__text_part__), cls.__text_make_ritual__)
    return make(letters, len(letters) // 2)

  @classmethod
  def _readText(cls, address: int) -> str:
    """Gives the letters of the C++ QString at an address as a 'str'."""
    opened = cls.getOpened(cls.__text_part__)
    size = getattr(opened, cls.__text_size_ritual__)(address)
    data = getattr(opened, cls.__text_data_ritual__)(address)
    letters = ctypes.string_at(data, 2 * size)
    return letters.decode(cls.__text_encoding__, 'surrogatepass')

  @classmethod
  def _dropText(cls, address: int) -> None:
    """Removes the C++ QString at an address, which '_makeText' or a
    ritual giving text made for this one call."""
    drop = cls.__text_drop_ritual__
    getattr(cls.getOpened(cls.__text_part__), drop)(address)

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

  @classmethod
  def createCall(
      cls,
      gives: str,
      takes: Tuple[str, ...],
      function: Any,
  ) -> Any:
    """
    Makes of a Python function something C++ can call: a function of C
    that 'ctypes' builds around it. 'CuteMixin' hands one to C++ for
    each function of Qt that a class of a program wrote anew.

    Parameters
    ----------

    gives : str
      The word of what the function gives back, as a row has it:
      'nothing', 'address', 'int', 'bool' and so on.

    takes : Tuple[str, ...]
      The word of each thing C++ hands it after the address of the
      object.

    function : Any
      The Python function. C++ calls it with the address of the object,
      then what 'takes' says, and last a place holding the number 0,
      into which the function writes 1 when it took the call. When it
      leaves the 0, C++ runs Qt's own function.

    Returns
    -------

    Any
      The function of C. Whoever asked keeps it for as long as C++ may
      call it: C++ holds only its address.

    Raises
    ------

    ValueError
      'gives' or one of 'takes' is no word of a row, or is 'text',
      which no Python function called by Qt takes or gives yet.

    LookupError
      No rows file lists the ritual 'keepException' stops Qt's loop of
      events by. Without it an exception raised in the function could
      not be raised where Python was.
    """
    words = cls.__row_words__
    for word in (gives, *takes):
      if word not in words or word == 'text':
        infoSpec = """A Python function called by Qt cannot take or give
        '%s'. The words are: %s."""
        known = ', '.join(word for word in words if word != 'text')
        raise ValueError(' '.join((infoSpec % (word, known)).split()))
    textPart = cls.__text_part__
    if textPart not in cls.getPartsOf(cls.__loop_stop_ritual__):
      infoSpec = """No rows file in '%s' lists the ritual '%s', by which
      Qt's loop of events is stopped when a Python function called by Qt
      raises. The ritual file of Qt's QCoreApplication is missing."""
      info = infoSpec % (
          cls.getPartFolder(textPart), cls.__loop_stop_ritual__)
      raise LookupError(' '.join(info.split()))
    shape = ctypes.CFUNCTYPE(
        words[gives], ctypes.c_void_p, *(words[take] for take in takes),
        ctypes.POINTER(ctypes.c_int),
    )
    return shape(function)

  @classmethod
  def takeText(cls, address: int) -> str:
    """
    Gives the letters of a text of Qt that C++ hands a Python function
    it calls, as the 'QString' Qt hands 'highlightBlock'.

    The text stays Qt's own: it is read, and neither kept nor removed.

    Parameters
    ----------

    address : int
      Where the C++ QString is.
    """
    return cls._readText(address)

  @classmethod
  def giveText(cls, text: str) -> int:
    """
    Makes a text of Qt from what a Python function called by Qt gave
    back, as the 'str' a program gives from 'textFromValue', and gives
    its address.

    The C++ class of ours that asked copies the QString and removes
    it, so nothing of Python removes it.

    Parameters
    ----------

    text : str
      What the Python function gave back.

    Raises
    ------

    TypeException
      'text' is not a 'str'.
    """
    return cls._makeText(text)

  @classmethod
  def keepException(cls, exception: BaseException) -> None:
    """
    Keeps an exception that a Python function raised while Qt was
    calling it, and has it raised where Python was.

    Qt calls such a function from C++, as 'paintEvent', and an
    exception cannot travel up through C++. So it is neither dropped
    nor only printed:

    1. It is kept here.
    2. While it is kept, no further Python function is asked by Qt: Qt
       runs its own in the place of each.
    3. Qt's loop of events is told to stop, by 'QCoreApplication::exit'
       with the number 1. Without an application that does nothing.
    4. 'call' raises it as soon as the ritual Python was in returns, as
       'app.exec()' or 'widget.grab()', and keeps it no more.

    Parameters
    ----------

    exception : BaseException
      What the Python function raised. When one is kept already, that
      one stays and this one is let go: the first is the one raised.
    """
    if Rituals.__kept_exception__ is not None:
      return
    Rituals.__kept_exception__ = exception
    stop = cls.__loop_stop_ritual__
    getattr(cls.getOpened(cls.__text_part__), stop)(1)

  @classmethod
  def _raiseKept(cls) -> None:
    """Raises the exception 'keepException' kept, when there is one,
    and keeps it no more."""
    exception = Rituals.__kept_exception__
    if exception is not None:
      Rituals.__kept_exception__ = None
      raise exception

  @classmethod
  def keepGiven(cls, given: Any) -> None:
    """
    Keeps what a Python function called by Qt gave back, until the next
    one gives something.

    Such a function may give a value back, as a 'QSize' from
    'sizeHint'. C++ is handed the address of the C++ object behind it
    and copies it right as the function returns. The cute object would
    be gone by then, and its C++ object with it, were it not kept here.

    Parameters
    ----------

    given : Any
      The cute object the function gave back.
    """
    Rituals.__kept_given__ = given

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
  def summon(cls) -> Paths:
    """
    Compiles the ritual files of each part of 'getBuiltParts' into the
    target file of that part.

    Call it after adding or changing a ritual file, in a Python that has
    not run a ritual yet: a shared object that is already open cannot be
    swapped for a new one. Each part has a 'Summon' of its own; see
    'createPartSummon'. Each
    ritual file is compiled by itself, and only when it changed since
    the last build; see 'Summon'. The builds of the parts run at the
    same time, and no more programs at once than the machine has
    processors.

    Returns
    -------

    Paths
      The full path of each target file, which now exists, in the
      order of 'getBuiltParts'.

    Raises
    ------

    RuntimeError
      A target file is already open in this Python, or 'clang++'
      refused a ritual file; its own message is then included, after
      the part. The other parts are built all the same.

    FileNotFoundError
      There is no ritual file of a part of Qt this machine has, or
      'clang++' or 'qmake6' is not installed.
    """
    if cls.__opened_targets__:
      infoSpec = """The shared objects of %s are already open in this
      Python and cannot be swapped. Build in a Python that has run no
      ritual."""
      info = infoSpec % ', '.join(sorted(cls.__opened_targets__))
      raise RuntimeError(' '.join(info.split()))
    partNames = cls.getBuiltParts()
    if not partNames:
      infoSpec = """There is no ritual file in '%s' of a part of Qt this
      machine has."""
      info = infoSpec % cls.getRitualFolder()
      raise FileNotFoundError(' '.join(info.split()))
    jobCount = os.cpu_count() or 1
    with ThreadPoolExecutor(max_workers=jobCount) as pool:
      return (*pool.map(cls._summonPart, partNames),)

  @classmethod
  def createPartSummon(cls, partName: str) -> Summon:
    """
    Gives the 'Summon' of the target file of one part, told what
    'summon' tells it, without running it: the ritual files of the part,
    its target file, the Qt shared objects of 'getPartSharedObjects'
    and the parts of 'getPartComponents'.

    Raises
    ------

    ValueError
      The part has no ritual files.
    """
    build = Summon()
    build.setRitualFiles(*cls.getPartRitualFiles(partName))
    build.setTargetFile(cls.getTargetFile(partName))
    build.setQtSharedObjects(*cls.getPartSharedObjects(partName))
    build.setComponents(*cls.getPartComponents(partName))
    return build

  @classmethod
  def _summonPart(cls, partName: str) -> str:
    """Builds the target file of one part, as 'summon' tells, and gives
    its path."""
    build = cls.createPartSummon(partName)
    try:
      return build.run()
    except RuntimeError as runtimeError:
      info = 'The target file of %s was not built.' % partName
      raise RuntimeError('%s %s' % (info, runtimeError)) from runtimeError

  @classmethod
  def _findPart(cls, ritualName: str, partName: Optional[str]) -> str:
    """
    Gives the part whose target file runs a ritual, seen from a part:
    the one part whose rows files list it; or, when several do, the
    first of them in the order of 'getPartOrder' of the part it is
    seen from. Seen from no part, only a ritual one part lists is
    found.

    Raises
    ------

    LookupError
      No rows file lists the ritual; or several parts list it, and it
      is seen from no part, or from one that sees none of them.
    """
    parts = cls.getPartsOf(ritualName)
    if len(parts) == 1:
      return parts[0]
    if not parts:
      infoSpec = """No rows file in '%s' lists a ritual named '%s'."""
      info = infoSpec % (cls.getRitualFolder(), ritualName)
      raise LookupError(' '.join(info.split()))
    if partName is not None:
      key = (partName, ritualName)
      found = cls.__seen_parts__.get(key, None)
      if found is not None:
        return found
      for part in cls.getPartOrder(partName):
        if part in parts:
          cls.__seen_parts__[key] = part
          return part
      infoSpec = """The ritual '%s' is listed by %s, and %s sees none of
      them: none is installed here."""
      info = infoSpec % (ritualName, ' and '.join(parts), partName)
      raise LookupError(' '.join(info.split()))
    infoSpec = """The ritual '%s' is listed by %s, one for each: say
    which part it is seen from, with 'callFrom'."""
    info = infoSpec % (ritualName, ' and '.join(parts))
    raise LookupError(' '.join(info.split()))

  @classmethod
  def _runIn(cls, partName: str, ritualName: str, args: Tuple) -> Any:
    """
    Runs a ritual in the target file of a part, as 'call' and
    'callFrom' do once they found the part.
    """
    opened = cls.__opened_targets__.get(partName, None)
    if opened is None:
      if partName not in cls.getInstalledParts():
        infoSpec = """The ritual '%s' calls a function the Qt of this
        machine does not have: its ritual file is of %s, which is not
        installed here."""
        info = infoSpec % (ritualName, partName)
        raise LookupError(' '.join(info.split()))
      opened = cls.getOpened(partName)
    if ritualName in cls.__missing_rituals__[partName]:
      infoSpec = """The ritual '%s' calls a function the Qt of this
      machine does not have: its ritual file has it between Qt's own
      '#if' lines, which do not hold here, so '%s' does not offer it."""
      info = infoSpec % (ritualName, cls.getTargetFile(partName))
      raise LookupError(' '.join(info.split()))
    row = cls.__ritual_rows__[partName][ritualName]
    ritual = getattr(opened, ritualName)
    try:
      if 'text' in row:
        return cls._callWithText(ritual, row, args)
      return ritual(*args)
    finally:
      #  Qt may have called a Python function meanwhile, and that one
      #  may have raised. Python is back here now, so here it is raised.
      cls._raiseKept()

  @classmethod
  def call(cls, name: str, *args: Any) -> Any:
    """
    Runs one ritual and gives what comes back. It is run in the target
    file of the one part whose rows files list it. A ritual several
    parts list, as one of 'QBarSeries' of QtCharts and of QtGraphs, is
    run with 'callFrom'.

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
      No rows file lists a ritual of that name, several parts list it,
      or the Qt of this machine has no function for it; see
      'getMissing'.

    FileNotFoundError
      The target file of the part is missing.

    TypeException
      Something that is no 'str' stands where the ritual takes text.

    BaseException
      Whatever a Python function raised that Qt called while the ritual
      ran, as a 'paintEvent' a class of a program wrote. See
      'keepException'.
    """
    return cls._runIn(cls._findPart(name, None), name, args)

  @classmethod
  def callFrom(cls, partName: str, name: str, *args: Any) -> Any:
    """
    Runs one ritual as a part of Qt sees it, and gives what comes back:
    in the target file of the one part whose rows files list it, or,
    when several do, of the first of them in the order of
    'getPartOrder' of that part, which is the part itself when it
    lists the ritual. A cute class of a part runs its rituals this way,
    through its 'Ugly'.

    Parameters
    ----------

    partName : str
      The part the ritual is seen from, as 'QtGraphs'.

    name : str
      The name of the ritual, as for 'call'.

    *args : Any
      What goes into the ritual, as for 'call'.

    Returns
    -------

    Any
      What the ritual returns, as for 'call'.

    Raises
    ------

    LookupError
      No rows file lists a ritual of that name, several parts list it
      and none of them is installed here, or the Qt of this machine has
      no function for it; see 'getMissing'. Also when the ritual
      folder has no folder of the part it is seen from, and several
      parts list the ritual.

    FileNotFoundError, TypeException, BaseException
      As for 'call'.
    """
    return cls._runIn(cls._findPart(name, partName), name, args)
