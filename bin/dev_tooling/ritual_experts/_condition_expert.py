"""ConditionExpert finds the '#if' lines a ritual file and each ritual
stand under."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
import textwrap
from typing import TYPE_CHECKING

from .. import HeaderFolder, HeaderReader
from . import RitualExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Tuple

  Record = Dict[str, Any]


class ConditionExpert(RitualExpert):
  """
  Finds the '#if' lines a ritual file and each ritual in it stand
  under, as Qt's header files have them, and writes them.

  A ritual stands between the same '#if' lines as the function it
  calls stands between in Qt's header file. The compiler of each
  machine then compiles the ritual exactly where that machine's Qt has
  the function, and leaves it out where it has not. Nothing is decided
  here: the text is the same for every system.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def wrapInConditions(text: str, conditions: Tuple[str, ...]) -> str:
    """
    Gives a piece of C++ text with one '#if' line for each condition
    above it, outermost first, and the '#endif' lines below it.

    A ritual stands between the same '#if' lines as the function it
    calls stands between in Qt's header file. The compiler of each
    machine then compiles the ritual exactly where that machine's Qt
    has the function, and leaves it out where it has not. Nothing is
    decided here: the text is the same for every system.
    """
    if not conditions:
      return text
    opening, closing = [], []  # type: List[str], List[str]
    for condition in conditions:
      line = '#if %s' % condition
      if len(line) > 77:
        #  A long question goes on in the next line after a backslash.
        pieces = textwrap.wrap(
            line, 73, break_long_words=False, break_on_hyphens=False)
        line = ' \\\n    '.join(pieces)
      opening.append(line)
      note = '#endif  // %s' % condition
      closing.insert(0, note if len(note) <= 77 else '#endif')
    return '\n'.join((*opening, text, *closing))

  @staticmethod
  def findConditions(record: Record) -> Tuple[str, ...]:
    """
    Gives the conditions under which Qt declares a function, a class
    or an enum: what each '#if' line around its declaration asks,
    outermost first, as 'HeaderReader.getConditions' reads them from
    the text of the header file. Empty for a thing under no '#if', and
    for one the compiler made itself, which stands at no line.

    Parameters
    ----------

    record : Record
      What the compiler wrote down about the thing, with the place it
      is declared at under 'loc'.
    """
    place = record.get('loc', dict())
    place = place.get('expansionLoc', place)
    headerPath, line = place.get('file'), place.get('line')
    if not headerPath or not line:
      return ()
    return HeaderReader.getConditions(headerPath, line)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getFileConditions(self) -> Tuple[str, ...]:
    """
    Gives the conditions the whole ritual file stands under, outermost
    first: the one under which Qt installs the header file of the
    class, as 'QT_CONFIG(metal)' for 'qrhimetal_p.h', when there is
    one, or, where that one asks what no compiler knows, whether the
    header file is there, as '__has_include(<QtOpcUa/qopcuakeypair.h>)';
    then what each '#if' line around the class asks. Where one does
    not hold, nothing of the file is compiled.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    className = generator.getClassName()
    conditions = self.findConditions(generator._readRecord(className))
    headerPath = tree.getHeaderPath(className, generator.getPartName())
    installed = HeaderReader.getHeaderFolder().getInstallCondition(
        headerPath)
    if installed is None:
      #  Qt installs the header file under a condition no compiler can
      #  be asked, as 'OPENSSL_FOUND' or 'ANDROID_EMBEDDED': whether it
      #  is installed is asked in its place, as the compiler can.
      relative = os.path.relpath(
          headerPath, generator.getHeaderReader().getQtHeaderFolder())
      installed = '__has_include(<%s>)' % relative
    if installed:
      return (installed, *conditions)
    return conditions

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def findOwnConditions(self, member: Record) -> Tuple[str, ...]:
    """Gives the conditions of a function of the class that go beyond
    those of the class itself. The ones of the class stand around the
    whole ritual file; see 'getFileConditions'."""
    generator = self.getGenerator()
    record = generator._readRecord(generator.getClassName())
    whole = self.findConditions(record)
    own = self.findConditions(member)
    if own[:len(whole)] == whole:
      return own[len(whole):]
    return own

  def findSwitchLines(
      self,
      conditions: List[str],
      privateLine: str,
  ) -> List[str]:
    """
    Gives the lines that pull in the list of switches of each other
    part whose switch the conditions ask, as 'QT_CONFIG(http)' of
    QtNetwork: its header file that brings the list in, or, for a
    switch Qt keeps to itself, the one in its folder 'private'. A part
    with no such file of its own has the list pulled in itself. The
    public list of the part of the class comes with the class.
    """
    folder = HeaderReader.getHeaderFolder()
    version = HeaderReader.getQtVersion()
    partName = self.getGenerator().getPartName()
    lines = []  # type: List[str]
    for name in re.findall(r'QT_CONFIG\((\w+)\)', ' '.join(conditions)):
      owner = folder.getSwitchOwner(name)
      if owner is None:
        continue
      ownerName, private = owner
      if not private:
        if ownerName == partName:
          continue
        line = '#include <%s/%s>' % (
            ownerName, HeaderFolder.getGlobalHeader(ownerName))
      else:
        header = HeaderFolder.getPrivateGlobalHeader(ownerName)
        if not header:
          header = '%s-config_p.h' % ownerName.lower()
        line = '#include <%s/%s/%s/private/%s>' % (
            ownerName, version, ownerName, header)
        if line == privateLine:
          continue
      if line not in lines:
        lines.append(line)
    return lines
