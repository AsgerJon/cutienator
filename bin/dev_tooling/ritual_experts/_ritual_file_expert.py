"""RitualFileExpert writes the text of the ritual file and of the sigil
file of a class."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
import re
import textwrap
from typing import TYPE_CHECKING

from .. import HeaderFolder, HeaderReader
from . import CppText, RitualExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Tuple

  Record = Dict[str, Any]


class RitualFileExpert(RitualExpert):
  """
  Writes the text of the ritual file of a class and of the sigil file
  that goes with it, from what the generator decided: a heading, the
  lines pulling in the header files the rituals need, the code taken
  from Qt's source, the classes of ours, and each ritual under the Qt
  function it calls; see 'getRitualText' and 'getSigilText'. Nothing is
  written to a file here; 'RitualGenerator.write' does that.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def writeBody(
      opening: str,
      called: str,
      passed: List[str],
      closing: str,
  ) -> List[str]:
    """
    Gives the lines between the curly brackets of one ritual: the call
    of the Qt function. They are kept to 77 letters where the names
    allow it.

    Parameters
    ----------

    opening : str
      What stands before the call, as 'return ' or 'return new QSize('.

    called : str
      What is called, as 'self->expandedTo' or 'new QSize'.

    passed : List[str]
      What is passed on, in order, as '*otherSize'.

    closing : str
      What stands after the last thing passed on, as '));'.
    """
    whole = '  %s%s(%s%s' % (opening, called, ', '.join(passed), closing)
    if len(whole) <= 77:
      return [whole]
    lines, indent = [], '  '
    if opening.endswith('('):
      lines.append('%s%s' % (indent, opening))
      indent, opening = '      ', ''
    lines.append('%s%s%s(' % (indent, opening, called))
    if not passed:
      lines[-1] = '%s%s' % (lines[-1], closing)
      return lines
    for index, entry in enumerate(passed):
      end = closing if index == len(passed) - 1 else ','
      lines.append('%s    %s%s' % (indent, entry, end))
    return lines

  @classmethod
  def findRitualAt(cls, lines: List[str], lineNumber: int) -> str:
    """
    Gives the name of the ritual a line of the text of a ritual file
    belongs to, the first line being 1: the last ritual whose own line,
    as 'writeRitual' writes it, stands at or before it. '' for a line
    before every ritual: a line pulling a file in, code taken from Qt's
    source, or a class of ours.
    """
    found = ''
    for line in lines[:max(lineNumber, 0)]:
      match = cls.__ritual_line__.match(line)
      if match is not None:
        found = match.group(1)
    return found

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The lines around lines pulling files in that stay with the ritual
  #  file: 'Summon' puts only the lines under no '#if' into its common
  #  header, and nothing defines this name.
  __not_common_start__ = '#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER'
  __not_common_end__ = '#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER'
  #  The line of a ritual's own name, as 'writeRitual' writes it: at
  #  the edge, the type it gives, its name and the bracket.
  __ritual_line__ = re.compile(r'^[A-Za-z_][^/#]*?\b(ritual_\w+)\(')


  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getHeading(self) -> str:
    """Says who wrote a file, from what, and that it is written anew."""
    generator = self.getGenerator()
    headerReader = generator.getHeaderReader()
    headerPath = generator.getDependencyTree().getHeaderPath(
        generator.getClassName(), generator.getPartName())
    relative = os.path.relpath(headerPath, headerReader.getQtHeaderFolder())
    infoSpec = """Written by dev_tooling.RitualGenerator from the records
    of %s, Qt %s. Changes made here are lost."""
    info = infoSpec % (relative, headerReader.getQtVersion())
    return ' '.join(info.split())

  def getRitualText(self) -> str:
    """
    Gives the whole text of the ritual file, without writing it.

    Written for you from 'RitualGenerator.getWritten': a heading, the
    lines pulling in the header file of the class, as
    'HeaderReader.getIncludeLines' gives them, the same for each value
    class a ritual copies, and then each ritual under the Qt function it
    calls.
    """
    from . import (ConditionExpert, CopyExpert, CuteClassExpert,
                   HeldValueExpert, ListExpert, MapExpert)
    generator = self.getGenerator()
    #  The plan first: settling it finds what has to be pulled in first.
    generator.getWritten()
    copyExpert = generator.getExpert(CopyExpert)
    cuteExpert = generator.getExpert(CuteClassExpert)
    conditionExpert = generator.getExpert(ConditionExpert)
    tree = generator.getDependencyTree()
    className = generator.getClassName()
    heading = textwrap.wrap(self.getHeading(), 73)
    blocks = ['\n'.join('//  %s' % line for line in heading)]
    #  The class Qt keeps the data of another class in, as
    #  'QWidgetTextControlPrivate', names that class in its 'q_func'
    #  ('Q_DECLARE_PUBLIC'), and its header file may not pull in the
    #  one declaring it: Qt's own '.cpp' files pull that one in first.
    needed = [
        *self._findPublicClasses(), *copyExpert.getPulledFirst(),
        className]
    for ritual in generator.getWritten():
      needed.extend(n for n in ritual['needs'] if n not in needed)
    if cuteExpert.hasCuteClass():
      #  The C++ class of ours holds the functions of the classes this
      #  one is built on as well, and a value one of them takes or
      #  gives has to be known in full here.
      for function in cuteExpert.getOverridable():
        needed.extend(n for n in function['needs'] if n not in needed)
    includeLines = []  # type: List[str]
    privateLine = self._getPrivateGlobalLine()
    if privateLine:
      #  The file may ask of a part Qt keeps to itself: the class is
      #  declared in a header file Qt calls private, or code taken from
      #  Qt's source stands in it. The private list of the part answers
      #  that, and is read before any '#if'.
      includeLines.append(privateLine)
    partName = generator.getPartName()
    folder = HeaderReader.getHeaderFolder()
    for name in needed:
      headerReader = tree.getHeaderReader(name, partName)
      headerPath = tree.getHeaderPath(name, partName)
      lines = headerReader.getIncludeLines(headerPath)
      installed = folder.getInstallCondition(headerPath)
      #  Only a condition asking for a system: one asking for a feature,
      #  'QT_CONFIG(action)', reads the part's list of features, which
      #  may not be pulled in yet where the line stands.
      if installed and 'QT_CONFIG' in installed:
        installed = ''
      if name != className and installed:
        #  A class another needs, declared in a header file Qt installs
        #  for some systems only, as 'qquick3dxrinputmanager_visionos_p.h'
        #  for visionOS: pulled in where Qt installs it. A ritual that
        #  needs it elsewhere does not compile there, and goes.
        pulled = [one for one in lines.split('\n') if one.strip()]
        if not all(one in includeLines for one in pulled):
          includeLines.extend(('#if %s' % installed, *pulled, '#endif'))
        continue
      for line in lines.split('\n'):
        if line.strip() and line not in includeLines:
          includeLines.append(line)
    #  A function whose code lies in another header file than the one
    #  its class is declared in: that header file is pulled in as well.
    ownPath = tree.getHeaderPath(className, partName)
    for ritual in generator.getWritten():
      ritualName = ritual['ritualName']
      for start in ('ritual_own', 'ritual'):
        if ritualName.startswith(start):
          break
      codePath = tree.getDefinedPath(ritualName[len(start):], partName)
      if codePath is None or codePath == ownPath:
        continue
      for headerReader in tree.getHeaderReaders():
        if not codePath.startswith('%s/' % headerReader.getPartFolder()):
          continue
        for line in headerReader.getIncludeLines(codePath).split('\n'):
          if line.strip() and line not in includeLines:
            includeLines.append(line)
    owned = [r for r in generator.getWritten() if r['kind'] == 'own']
    if any(ListExpert.isUsedBy(ritual) for ritual in generator.getWritten()):
      includeLines.append('#include <QtCore/qlist.h>')
    if any(MapExpert.isUsedBy(ritual) for ritual in generator.getWritten()):
      includeLines.append('#include <QtCore/qmap.h>')
      includeLines.append('#include <QtCore/qhash.h>')
      includeLines.append('#include <iterator>')
    if cuteExpert.hasCuteClass():
      includeLines.append('#include <cstring>')
    #  What the held values of the rituals name, defined in full.
    heldExpert = generator.getExpert(HeldValueExpert)
    for line in heldExpert.getIncludeLines():
      if line not in includeLines:
        includeLines.append(line)
    #  A header file Qt keeps apart, as 'qabstractspinbox_p.h', stays
    #  with this file as well, out of the common header 'Summon' makes:
    #  Qt writes those for its own files one at a time, and all of them
    #  together do not mean what each means alone. That one declares an
    #  'operator+' of two QVariant for everybody, which makes the '+' of
    #  two QLatin1StringView in 'qdbusabstractinterface.cpp' ambiguous.
    #  Qt's header files for everybody are meant to be read together.
    apart = re.compile(r'^#include <Qt\w+/\d+\.\d+\.\d+/Qt\w+/')
    grouped = []  # type: List[str]
    for line in includeLines:
      if line == privateLine or not apart.match(line):
        grouped.append(line)
        continue
      if grouped and grouped[-1] == self.__not_common_end__:
        grouped.insert(len(grouped) - 1, line)
        continue
      grouped.extend((self.__not_common_start__, line,
                      self.__not_common_end__))
    includeLines = grouped
    #  What the code taken from Qt's source needs comes as Qt's files
    #  have it, with the '#if' lines around it, so no line of it is
    #  left out for standing above already. It stays with this file,
    #  out of the common header 'Summon' makes of the lines under no
    #  '#if': a header file of Qt's source may be one to be read once
    #  only, as 'qmetaobject_moc_p.h', which has no guard.
    if copyExpert.getSourceIncludes():
      includeLines.extend((
          self.__not_common_start__, *copyExpert.getSourceIncludes(),
          self.__not_common_end__))
    conditions = conditionExpert.getFileConditions()
    #  A switch another part has, asked by an '#if' of the file, as
    #  'QT_CONFIG(http)' of QtNetwork in a file of QtHttpServer, is
    #  answered by the list of that part, pulled in first.
    asking = [*conditions]
    for ritual in generator.getWritten():
      asking.extend(ritual.get('conditions', ()))
    if cuteExpert.hasCuteClass():
      for function in cuteExpert.getOverridable():
        asking.extend(function.get('conditions', ()))
    switchLines = conditionExpert.findSwitchLines(asking, privateLine)
    if conditions:
      #  Qt declares the class under an '#if', so the whole file stands
      #  under it: where a Qt has no such class, nothing of the file is
      #  compiled. What an '#if' of Qt's asks can only be answered once
      #  the header file of the part has been read, so that comes first.
      asked = ['#include <%s/%s>' % (
          partName, HeaderFolder.getGlobalHeader(partName))]
      if privateLine:
        asked.append(privateLine)
      opening = [
          *switchLines, *asked, *('#if %s' % one for one in conditions)]
      blocks[0] = '\n'.join((blocks[0], *opening, *includeLines))
    else:
      blocks[0] = '\n'.join((blocks[0], *switchLines, *includeLines))
    if copyExpert.getSourceText():
      blocks.append(copyExpert.getSourceText())
    ownClass = cuteExpert.writeOwnClass(owned)
    if ownClass:
      blocks.append(ownClass)
    if cuteExpert.hasCuteClass():
      blocks.append(cuteExpert.writeCuteClass())
    blocks.extend(ritual['text'] for ritual in generator.getWritten())
    if conditions:
      blocks.append('\n'.join(
          '#endif  // %s' % one for one in reversed(conditions)))
    return '%s\n' % '\n\n'.join(blocks)

  def getSigilText(self) -> str:
    """
    Gives the whole text of the sigil file, without writing it.

    Written for you from 'RitualGenerator.getSigils', as JSON: under
    'about' the heading of the ritual file; for a part of
    'HeaderReader.getOwnOrderParts' only, under 'parts first' the part
    and the parts it needs, the nearest first, whose folders the
    compiler looked in first, so that 'Rituals.summon' does the same;
    and under 'sigils' each ritual with its sigil.
    """
    generator = self.getGenerator()
    about = textwrap.wrap(self.getHeading(), 66)
    lines = ['{', '  "about": [']
    lines.extend(
        '    %s%s' % (json.dumps(line), ',' if line is not about[-1] else '')
        for line in about
    )
    lines.append('  ],')
    partName = generator.getPartName()
    if partName in HeaderReader.getOwnOrderParts():
      first = HeaderReader.getNeededParts(partName)
      lines.append('  "parts first": [')
      packed = '   '
      for position, name in enumerate(first):
        piece = json.dumps(name)
        if position < len(first) - 1:
          piece = '%s,' % piece
        if len(packed) + 1 + len(piece) > 77 and packed.strip():
          lines.append(packed)
          packed = '   '
        packed = '%s %s' % (packed, piece)
      lines.append(packed)
      lines.append('  ],')
    lines.append('  "sigils": {')
    sigils = [*generator.getSigils().items()]
    for index, (ritualName, sigil) in enumerate(sigils):
      end = '' if index == len(sigils) - 1 else ','
      words = ', '.join(json.dumps(word) for word in sigil)
      whole = '    %s: [%s]%s' % (json.dumps(ritualName), words, end)
      if len(whole) <= 77:
        lines.append(whole)
        continue
      lines.append('    %s: [' % json.dumps(ritualName))
      #  The words are put on lines one by one. A word may hold a space,
      #  as 'unsigned int', and must not be broken there.
      packed = '     '
      for position, word in enumerate(sigil):
        piece = json.dumps(word)
        if position < len(sigil) - 1:
          piece = '%s,' % piece
        if len(packed) + 1 + len(piece) > 77 and packed.strip():
          lines.append(packed)
          packed = '     '
        packed = '%s %s' % (packed, piece)
      lines.append(packed)
      lines.append('    ]%s' % end)
    lines.extend(('  }', '}'))
    return '%s\n' % '\n'.join(lines)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _findPublicClasses(self) -> Tuple[str, ...]:
    """
    Gives the class whose data the class of the generator keeps, as
    'QWidgetTextControl' for 'QWidgetTextControlPrivate': the class its
    function 'q_func' gives, which Qt's 'Q_DECLARE_PUBLIC' writes.
    Nothing for a class with no such function, or one giving a class
    the tree does not know.
    """
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    className = generator.getClassName()
    found = []  # type: List[str]
    for member in generator._readRecord(className).get('inner', ()):
      if not isinstance(member, dict) or member.get('name') != 'q_func':
        continue
      qualType = member.get('type', dict()).get('qualType', '')
      match = re.match(r'\s*(?:const\s+)?([\w:]+)\s*\*', qualType)
      if match is None:
        continue
      name = match.group(1)
      if name != className and tree.hasClass(name, generator.getPartName()):
        if name not in found:
          found.append(name)
    return (*found,)

  def _getPrivateGlobalLine(self) -> str:
    """
    Gives the line pulling in the private global header file of the
    part of the class, as '#include <QtWidgets/6.12.0/QtWidgets/private/
    qtwidgetsglobal_p.h>', where the ritual file needs it: the class is
    declared in a header file Qt keeps apart, or code taken from Qt's
    source stands in the file. Else ''.
    """
    from . import CopyExpert
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    className, partName = generator.getClassName(), generator.getPartName()
    headerReader = tree.getHeaderReader(className, partName)
    headerPath = tree.getHeaderPath(className, partName)
    apart = any(
        headerPath.startswith(folder)
        for folder in headerReader.getApartFolders())
    sourceText = generator.getExpert(CopyExpert).getSourceText()
    if not apart and not sourceText:
      return ''
    if not HeaderFolder.getPrivateGlobalHeader(partName):
      #  A part with no such file of its own, as QtXml, has no private
      #  switches: its files ask those of QtCore.
      partName = 'QtCore'
    return '#include <%s/%s/%s/private/%s>' % (
        partName, HeaderReader.getQtVersion(), partName,
        HeaderFolder.getPrivateGlobalHeader(partName))

  def writeRitual(self, plan: Record, body: List[str]) -> str:
    """
    Gives the C++ text of one ritual, under the function it calls.

    Every ritual starts with the line 'extern "C" Q_DECL_EXPORT'. The
    first part gives it the plain name Python finds it by. The second is
    Qt's own mark for a function a shared object is to offer: Windows
    offers only what carries it, and on Linux and macOS it changes
    nothing.
    """
    lines = textwrap.wrap(
        plan['function'], 77, initial_indent='//  ',
        subsequent_indent='//      ',
    ) or ['//  ']
    takes = [CppText.joinType(t, n) for n, t in plan['takes']]
    named = CppText.joinType(plan['gives'], plan['ritualName'])
    lines.append('extern "C" Q_DECL_EXPORT')
    head = '%s(' % named
    whole = '%s%s) {' % (head, ', '.join(takes))
    if len(whole) <= 77:
      lines.append(whole)
    else:
      lines.append(head)
      for index, take in enumerate(takes):
        end = ') {' if index == len(takes) - 1 else ','
        lines.append('    %s%s' % (take, end))
      if not takes:
        lines[-1] = '%s) {' % head
    lines.extend(body)
    lines.append('}')
    return '\n'.join(lines)
