"""MetaExpert reaches a signal, a slot or an invokable function of a
class of Qt through the class's meta-object."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from .. import HeaderReader
from . import ConditionExpert, CppText, ReachExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, FrozenSet, List, Set

  Record = Dict[str, Any]


class MetaExpert(ReachExpert):
  """
  Reaches a function of a class of Qt that Qt's library offers under no
  name, where the class's meta-object knows it: a signal, a slot, or a
  function Qt marks 'Q_INVOKABLE', of a class built on 'QObject'. The
  ritual finds the function in the meta-object by its signature, and
  has the object run it through 'qt_metacall', which C++ looks up in
  the object, so Qt's library need offer nothing by name. Qt's own code
  runs; nothing is copied. Calling a signal so emits it.

  The meta-object knows a function by its signature as Qt's 'moc' wrote
  it, from the header as written: the name, and each type it takes as
  the header spells it, as 'clicked(bool)'. The ritual asks for it
  under 'QMetaObject::normalizedSignature' of that, in the meta-object
  of the class itself, found among those of the object by the name of
  the class. Where it is not there, the ritual stops the program with
  what it looked for: the signature here would be wrong, and calling
  nothing would hide that.

  Only functions giving back nothing are reached this way so far, as
  every signal does; a function giving back a value is refused, with
  that as the reason.

  The sections of a class are read from the text of its header, as Qt
  writes them: the lines under 'signals:' and 'Q_SIGNALS:' are
  signals, as 'HeaderReader.getSignalLines' has them, and those under
  'slots:' and 'Q_SLOTS:', or marked 'Q_SLOT' or 'Q_INVOKABLE' on the
  line or the line before, are slots and invokable functions.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The lines of each header file that declare slots and invokable
  #  functions, read once; see '_getInvokableLines'.
  __invokable_lines__ = dict()  # type: Dict[str, FrozenSet[int]]
  __slots_opening__ = re.compile(
      r'^\s*(?:(?:public|protected|private)\s+)?(?:Q_SLOTS|slots)\s*:')
  __section_closing__ = re.compile(
      r'^\s*(?:(?:public|protected|private)\s*:'
      r'|(?:public\s+|protected\s+|private\s+)?(?:Q_SIGNALS|signals)\s*:'
      r'|\};)')
  __marked__ = re.compile(r'\b(?:Q_INVOKABLE|Q_SLOT)\b')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _getInvokableLines(cls, headerPath: str) -> FrozenSet[int]:
    """Gives the lines of a header file that declare slots and invokable
    functions, read from the text of the file alone, and kept."""
    if headerPath in cls.__invokable_lines__:
      return cls.__invokable_lines__[headerPath]
    with open(headerPath, errors='replace') as file:
      text = file.read().replace('\r', '')
    #  Comments go, and the lines keep their numbers.
    text = re.sub(
        r'/\*.*?\*/', lambda found: '\n' * found.group(0).count('\n'),
        text, flags=re.S)
    found, inside = set(), False  # type: Set[int], bool
    lines = [re.sub(r'//.*$', '', line) for line in text.split('\n')]
    for number, line in enumerate(lines, 1):
      if cls.__slots_opening__.match(line):
        inside = True
      elif cls.__section_closing__.match(line):
        inside = False
      elif inside or cls.__marked__.search(line):
        found.add(number)
      elif number > 1 and cls.__marked__.search(lines[number - 2]):
        #  The mark alone on the line before the function.
        found.add(number)
    cls.__invokable_lines__[headerPath] = frozenset(found)
    return cls.__invokable_lines__[headerPath]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _isObject(self) -> bool:
    """Says whether the class is built on 'QObject', whose meta-object
    runs a function by 'qt_metacall'."""
    generator = self.getGenerator()
    className = generator.getClassName()
    if className == 'QObject':
      return True
    tree = generator.getDependencyTree()
    ancestors = tree.getAncestors(className, generator.getPartName())
    return any(name == 'QObject' for _, name in ancestors)

  def _isKnownToMeta(self, member: Record) -> bool:
    """Says whether the header declares the function as a signal, a
    slot or an invokable function."""
    place = member.get('loc', dict())
    place = place.get('expansionLoc', place)
    headerPath, line = place.get('file'), place.get('line')
    if not headerPath or not line:
      return False
    if line in HeaderReader.getSignalLines(headerPath):
      return True
    return line in self._getInvokableLines(headerPath)

  def canReach(self, member: Record) -> bool:
    """Says whether the class's meta-object knows the function, and the
    function gives back nothing."""
    if member.get('kind') != 'CXXMethodDecl':
      return False
    if member.get('storageClass') == 'static':
      return False
    functionType = member.get('type', dict()).get('qualType', '')
    if CppText.splitFunctionType(functionType)[0] != 'void':
      return False
    if 'nullptr_t' in functionType:
      #  Python hands nothing for it, and the meta-object wants a value
      #  for every argument.
      return False
    if not self._isObject():
      return False
    return self._isKnownToMeta(member)

  def getWay(self) -> str:
    """Says what this way does: the meta-object runs the function."""
    return 'be called through the meta-object'

  def getRefusal(self) -> str:
    """Says why the meta-object does not run the function."""
    infoSpec = """it is no signal, slot or invokable function giving
    back nothing, of a class built on QObject"""
    return ' '.join(infoSpec.split())

  def _findSignature(self, member: Record) -> str:
    """Gives the signature of the function as the header writes it, as
    moc read it: the name and each type it takes, as
    'setValue(const QString &)'. Qt's mark that only the class itself
    emits a signal, 'QPrivateSignal', is no part of it."""
    taken = []  # type: List[str]
    for entry in member.get('inner', ()):
      if not isinstance(entry, dict) or entry.get('kind') != 'ParmVarDecl':
        continue
      written = entry['type']['qualType']
      if written.split('::')[-1] == 'QPrivateSignal':
        continue
      taken.append(written)
    return '%s(%s)' % (member['name'], ','.join(taken))

  def adopt(self, plan: Record, member: Record) -> None:
    """
    Writes the ritual of a function this way reached anew, keeping what
    it takes: it finds the function in the meta-object and has the
    object run it. Each argument goes to the meta-object as the address
    of a value of the type the function takes: the object the ritual
    was handed the address of, the ritual's own argument where it is of
    that type, or else a value of that type made for the call.
    """
    from . import RitualFileExpert
    generator = self.getGenerator()
    className = generator.getClassName()
    handedTo = []  # type: List[str]
    made = []  # type: List[str]
    for index, argument in enumerate(plan['arguments']):
      name, written = argument['name'], argument['written']
      passing = argument['passing']
      expert = generator.getTypeExpertOf(passing['kind'])
      handed = expert.writeTaken(name, written, passing)[1]
      if handed in ('*%s' % name, 'std::move(*%s)' % name):
        where = name
      elif handed == name and not passing.get('widened'):
        where = '&%s' % name
      else:
        local = 'value%d' % index
        made.append('  %s %s = %s;' % (
            CppText.stripReadOnly(written), local, handed))
        where = '&%s' % local
      handedTo.append(
          'const_cast<void *>(static_cast<const void *>(%s))' % where)
    signature = self._findSignature(member)
    body = [
        '  const QObject *object = self;',
        '  const QMetaObject *meta = object->metaObject();',
        '  for (const QMetaObject *up = meta; up; up = up->superClass()) {',
        '    if (!qstrcmp(up->className(), "%s")) {' % className,
        '      meta = up;',
        '      break;',
        '    }',
        '  }',
        '  const int index = meta->indexOfMethod(',
        '      QMetaObject::normalizedSignature(',
        '          "%s").constData());' % signature,
        '  if (index < 0)',
        '    qFatal("cutienator: the meta-object of %s has no %s",',
        '           meta->className(), "%s");' % signature,
        *made,
        '  void *arguments[] = {',
        '      nullptr,',
        *('      %s,' % one for one in handedTo),
        '  };',
        '  static_cast<QObject *>(self)->qt_metacall(',
        '      QMetaObject::InvokeMetaMethod, index, arguments);',
    ]
    fileExpert = generator.getExpert(RitualFileExpert)
    plan['bare'] = fileExpert.writeRitual(plan, body)
    plan['text'] = ConditionExpert.wrapInConditions(
        plan['bare'], plan['conditions'])
