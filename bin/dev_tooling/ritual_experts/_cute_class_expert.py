"""CuteClassExpert writes the C++ class of ours through which Python can
take functions of a class of Qt over."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import collections
import textwrap
from typing import TYPE_CHECKING

from . import ConditionExpert, CppText, RitualExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Set, Tuple

  Record = Dict[str, Any]
  Records = Tuple[Record, ...]


class CuteClassExpert(RitualExpert):
  """
  Writes the C++ class of ours built on the class of Qt, as
  'CuteQWidget', through which Python can take functions over: those C++
  looks up in the object, the class's own and inherited, that a class
  built on this one may replace and whose arguments can be handed to
  Python; see 'getOverridable'. Every object Python makes of the class
  is of that C++ class, and each such function asks Python first, when
  Python has handed a function over for it.

  With it come the rituals of the class of ours: the one handing a
  Python function over ('planTake'), and, for each function of its
  own, the one that runs just Qt's function ('planOwn').
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The classes that get a C++ class of ours, through which Python can
  #  take a function over, or None for every class that has such a
  #  function. It is set while the way is tried on a few classes.
  __cute_class_limit__ = None  # type: Optional[Tuple[str, ...]]
  #  The functions C++ looks up in the object that are Qt's own
  #  workings, and are never taken over.
  __qt_own_virtuals__ = ('metaObject', 'qt_metacast', 'qt_metacall')

  #  Private Variables
  __has_cute_class__ = None  # type: Optional[bool]
  __overridable_functions__ = None  # type: Optional[Records]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isWithinLimit(self, className: str) -> bool:
    """Says whether the class is one that gets the rituals of its own
    functions, while the way is tried on a few classes only; see
    '__cute_class_limit__'."""
    limit = self.__cute_class_limit__
    return limit is None or className in limit

  def hasCuteClass(self) -> bool:
    """
    Says whether the class gets a C++ class of ours built on it. Every
    object Python makes of the class is then of that C++ class, in
    which each function of 'getOverridable' asks Python first, when
    Python has handed a function over for it.
    """
    if self.__has_cute_class__ is None:
      self.__has_cute_class__ = self._findCuteClass()
    return self.__has_cute_class__

  def getOverridable(self) -> Records:
    """
    Gives the functions of the class that Python can take over: those
    C++ looks up in the object, the class's own and inherited, that a
    class built on this one may replace and whose arguments can be
    handed to Python.

    Decided for you. Each is the plan of the function as the nearest
    class declares it, with 'key': the compiler's name of the function
    where it was first declared, by which Python names it to C++;
    'owner': the class whose function Qt runs when Python takes nothing
    over; 'rootOwner': the class that first declared it; 'access';
    'pure': whether Qt has no function of its own for it; and what
    '_planCallback' gives.
    """
    if self.__overridable_functions__ is not None:
      return self.__overridable_functions__
    generator = self.getGenerator()
    found = []  # type: List[Record]
    for virtual in self._findVirtuals():
      nearest, root = virtual['nearest'], virtual['root']
      name = virtual['name']
      if name in self.__qt_own_virtuals__ or name.startswith('operator'):
        continue
      if nearest['final']:
        continue
      if 'mangledName' not in root['member']:
        continue
      if nearest['member'].get('explicitlyDeleted'):
        #  Qt forbids the function in the nearest class.
        continue
      other = generator._getOther(nearest['owner'])
      plan = other._planFunction(nearest['member'])
      if plan['unknownTypes'] or plan['unsureNumbers'] or plan['variadic']:
        continue
      if '&&' in plan['words'] or '&' in plan['words']:
        continue
      shape = self._planCallback(plan)
      if shape is None:
        continue
      named = [a['written'] for a in plan['arguments']]
      named.append(plan['giving']['written'])
      if any(self._isHiddenType(typeName) for typeName in named):
        #  A type Qt keeps for classes built on its class cannot be
        #  named by a ritual, which stands outside every class.
        continue
      #  Where Qt declares the function under an '#if', what is written
      #  for it here stands under the same: every '#if' around it in
      #  the class that declares it first and in the nearest one.
      conditions = ConditionExpert.findConditions(root['member'])
      for condition in ConditionExpert.findConditions(nearest['member']):
        if condition not in conditions:
          conditions = (*conditions, condition)
      found.append(dict(
          plan, key=root['member']['mangledName'], owner=nearest['owner'],
          rootOwner=root['owner'], access=nearest['access'],
          pure=nearest['pure'], conditions=conditions, **shape))
    self.__overridable_functions__ = (*found,)
    return self.__overridable_functions__

  def getDeclaredVirtuals(self) -> Records:
    """
    Gives every function Qt calls itself that the class is the first
    to declare and that a class built on it may put its own in the
    place of, whether or not Python can take it over.

    Decided for you. The class generator needs it to name, in the
    class file, the functions that cannot be handed to Python yet: a
    class of a program that writes one of those anew is refused, where
    Qt would otherwise never call what it wrote.

    Returns
    -------

    Records
      For each function its 'name', and 'written': the function as Qt
      declares it, as 'void QWidget::paintEvent(QPaintEvent *)'.
    """
    found = []  # type: List[Record]
    className = self.getGenerator().getClassName()
    for virtual in self._findVirtuals():
      nearest, root = virtual['nearest'], virtual['root']
      name = virtual['name']
      if root['owner'] != className:
        continue
      if name in self.__qt_own_virtuals__ or name.startswith('operator'):
        continue
      if nearest['final']:
        continue
      functionType = root['member']['type']['qualType']
      gives, taken, words = CppText.splitFunctionType(functionType)
      space = '' if gives.endswith(('*', '&')) else ' '
      written = '%s%s%s::%s(%s)' % (gives, space, className, name, taken)
      found.append(dict(name=name, written=' '.join([written, *words])))
    return (*found,)

  def fillsEveryOpenFunction(self) -> bool:
    """
    Says whether the C++ class of ours has a function for every one the
    class of Qt leaves open, its own and those of the classes it is
    built on: every function Qt declares '= 0' and no class between
    gives. C++ can then make an object of ours where it cannot make one
    of an abstract class of Qt. Without an answer from Python, such a
    function of ours gives what its type is made of from nothing, as
    '_writeOverride' writes it.
    """
    if not self.hasCuteClass():
      return False
    filled = {
        function['key'] for function in self.getOverridable()
        if function['pure']}
    for virtual in self._findVirtuals():
      if not virtual['nearest']['pure']:
        continue
      if virtual['root']['member'].get('mangledName') not in filled:
        return False
    return True

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _findCuteClass(self) -> bool:
    """Does the looking for 'hasCuteClass', which keeps the answer."""
    generator = self.getGenerator()
    className = generator.getClassName()
    limit = self.__cute_class_limit__
    if limit is not None and className not in limit:
      return False
    record = generator._readRecord(className)
    access = 'private' if record.get('tagUsed') == 'class' else 'public'
    for child in record.get('inner', ()):
      if not isinstance(child, dict):
        continue
      kind = child.get('kind')
      if kind == 'AccessSpecDecl':
        access = child['access']
      elif kind == 'FinalAttr':
        #  Qt forbids building a class on this one.
        return False
      elif kind == 'CXXDestructorDecl' and access == 'private':
        #  Only Qt may remove one, so no class can be built on it.
        return False
    return True if self.getOverridable() else False

  def _findVirtuals(self) -> List[Record]:
    """
    Gives every function of the class that C++ looks up in the object
    when it is called, its own and those of the classes it is built
    on. Qt calls such a function itself, and a class built on this one
    can put a function of its own in its place.

    Returns
    -------

    List[Record]
      For each 'name'; 'nearest': where the function Qt runs for an
      object of this class is declared, as 'owner', 'member', 'access',
      'final' and 'pure'; and 'root': the same for the class that first
      declared it.
    """
    generator = self.getGenerator()
    tree, className = generator.getDependencyTree(), generator.getClassName()
    ancestors = tree.getAncestors(className, generator.getPartName())
    chain = (className, *(name for _, name in reversed(ancestors)))
    groups = dict()  # type: Dict[Tuple[str, str], List[Record]]
    for owner in chain:
      record = generator._readRecord(owner)
      access = 'private' if record.get('tagUsed') == 'class' else 'public'
      for member in record.get('inner', ()):
        kind = member.get('kind')
        if kind == 'AccessSpecDecl':
          access = member['access']
          continue
        if kind != 'CXXMethodDecl' or member.get('isImplicit'):
          continue
        if member.get('storageClass') == 'static':
          continue
        marks = [
            child.get('kind') for child in member.get('inner', ())
            if isinstance(child, dict)
        ]
        looked = True if member.get('virtual') else False
        if 'OverrideAttr' in marks or 'FinalAttr' in marks:
          looked = True
        #  One function is known by its name, what it takes and whether
        #  it leaves the object as it is. What it gives is left out: a
        #  class may declare it anew giving a class built on what the
        #  first one gave.
        functionType = member['type']['qualType']
        _, taken, words = CppText.splitFunctionType(functionType)
        shape = '%s|%s' % (taken, 'const' if 'const' in words else '')
        groups.setdefault((member['name'], shape), []).append(dict(
            owner=owner, member=member, access=access, virtual=looked,
            final='FinalAttr' in marks,
            pure=True if member.get('pure') else False,
        ))
    virtuals = []  # type: List[Record]
    for name, declared in self._joinSpelledApart(chain, groups):
      if any(entry['virtual'] for entry in declared):
        virtuals.append(
            dict(name=name, nearest=declared[0], root=declared[-1]))
    return virtuals

  def _joinSpelledApart(self, chain: Any, groups: Any) -> List[Any]:
    """
    Joins the declarations of one function that two classes spell
    apart. A class may shorten the name of a type a class it is built
    on declares: 'QIODevice::open(QIODeviceBase::OpenMode)' is
    'QBuffer::open(OpenMode)' in QBuffer, and both are one function.

    Parameters
    ----------

    chain : Any
      The class and the classes it is built on, the nearest first.

    groups : Any
      The declarations gathered by name and by what the function takes
      as its class spells it, each list the nearest first.

    Returns
    -------

    List[Any]
      For each function its name and its declarations, the nearest
      first. Only a name with more than one group is spelled out in
      full, which is where two spellings of one function can be.
    """
    generator = self.getGenerator()
    counts = collections.Counter(name for name, _ in groups)
    joined = collections.OrderedDict()  # type: Dict[Any, List[Record]]
    for (name, shape), declared in groups.items():
      if counts[name] < 2:
        joined[name, shape] = declared
        continue
      for entry in declared:
        other = generator._getOther(entry['owner'])
        spelled = [
            other._spellOutside(child['type']['qualType'])
            for child in entry['member'].get('inner', ())
            if isinstance(child, dict) and child.get('kind') == 'ParmVarDecl'
        ]
        full = '%s|%s' % (', '.join(spelled), shape.rpartition('|')[2])
        joined.setdefault((name, full), []).append(entry)
    out = []  # type: List[Any]
    for (name, _), declared in joined.items():
      declared.sort(key=lambda entry: chain.index(entry['owner']))
      out.append((name, declared))
    return out

  def _planCallback(self, plan: Record) -> Optional[Record]:
    """
    Says how a function Qt calls is handed on to Python: what C++ hands
    the Python function and what it takes back. Each type expert says
    it for its kind; see 'TypeExpert.handOver' and
    'TypeExpert.handBack'.

    Returns
    -------

    Optional[Record]
      None when something of it cannot be handed over yet. Else
      'cTakes': the C++ types handed over after the object; 'cPassed':
      what is handed over; 'takes': for Python, the word of each
      ('address', 'int', ...) with what it is ('address' of a class,
      'value' of a class, 'number', 'enum' of an enum, 'flags' of an
      enum, 'text'); 'cGives', 'gives' and 'given': the same for what
      comes back.
    """
    generator = self.getGenerator()
    cTakes, cPassed, takes = [], [], []
    for argument in plan['arguments']:
      passing = argument['passing']
      expert = generator.getTypeExpertOf(passing['kind'])
      if expert is None:
        return None
      handed = expert.handOver(
          argument['name'], argument['written'], passing)
      if handed is None:
        return None
      cTake, cPass, take = handed
      cTakes.append(cTake)
      cPassed.append(cPass)
      takes.append(take)
    giving = plan['giving']
    expert = generator.getTypeExpertOf(giving['kind'])
    if expert is None:
      return None
    back = expert.handBack(giving['written'], giving)
    if back is None:
      return None
    cGives, gives, given = back
    return dict(
        cTakes=(*cTakes,), cPassed=(*cPassed,), takes=(*takes,),
        cGives=cGives, gives=gives, given=given,
    )

  def _isHiddenType(self, typeName: str) -> bool:
    """Says whether a type is one Qt writes inside a class and keeps
    for that class and the classes built on it, as the enum
    'QAbstractSlider::SliderChange'."""
    generator = self.getGenerator()
    plain = typeName.replace('const ', '').replace('&', '')
    plain = plain.replace('*', '').strip()
    owner, _, own = plain.rpartition('::')
    if not owner:
      return False
    try:
      ownerKey = generator._keyOf(owner)
    except LookupError:
      #  Written in a namespace, as 'Qt::FocusPolicy', or in no class
      #  the tree knows: nothing keeps it from being named.
      return False
    kept = generator.getDependencyTree().getKept('hidden types')
    try:
      return kept[(ownerKey, own)]
    except KeyError:
      hidden = self._findHiddenType(owner, own)
      kept[(ownerKey, own)] = hidden
      return hidden

  def _findHiddenType(self, owner: str, own: str) -> bool:
    """Does the looking for '_isHiddenType', which keeps the answer."""
    try:
      record = self.getGenerator()._readRecord(owner)
    except (ValueError, LookupError):
      #  Written in a namespace, as 'Qt::FocusPolicy', or in no class
      #  the tree knows: nothing keeps it from being named.
      return False
    access = 'private' if record.get('tagUsed') == 'class' else 'public'
    for member in record.get('inner', ()):
      if member.get('kind') == 'AccessSpecDecl':
        access = member['access']
      elif member.get('name') == own and 'Decl' in member.get('kind', ''):
        return access != 'public'
    return False

  def writeCuteClass(self) -> str:
    """
    Gives the C++ text of the class of ours built on the class of Qt.

    It holds, for each function of 'getOverridable', a place for the
    Python function handed over and the function Qt calls: that one
    asks the Python function when there is one, and runs Qt's own when
    there is none or when Python says it did not take the call.
    """
    generator = self.getGenerator()
    className = generator.getClassName()
    cuteName = generator.getCuteClassName()
    wrap = ConditionExpert.wrapInConditions
    functions = self.getOverridable()
    lines = [
        '//  A %s that Python can take functions over in. Every %s' % (
            className, className),
        '//  Python makes is one. Each function below asks the Python',
        '//  function handed over for it, and runs Qt\'s own without one.',
    ]
    for index, function in enumerate(functions):
      handed = ['const void *', *function['cTakes'], 'int *']
      named = 'typedef %s (*%sCall%d)(%s);' % (
          function['cGives'], cuteName, index, ', '.join(handed))
      lines.append(wrap(named, function['conditions']))
    lines.append('class %s : public %s {' % (cuteName, className))
    lines.append('public:')
    lines.append('  using %s::%s;' % (className, className.split('::')[-1]))
    forwarded = []  # type: List[str]
    if className in generator._getTypeTables()['copyable']:
      #  A copy of an object of Qt is an object of ours as well.
      forwarded.append('const %s &' % className)
    #  C++ does not hand a class its base's constructors that copy or
    #  move a base, as 'QEvent(const QEvent &)': where a ritual makes an
    #  object so, ours takes the object and hands it on.
    for plan in generator.getWritten():
      #  What a class made in place has its 'operator new' take comes
      #  first, and is no argument of the constructor.
      arguments = plan.get('arguments', ())[plan.get('placed', 0):]
      if plan['kind'] != 'constructor' or len(arguments) != 1:
        continue
      argument = arguments[0]
      if argument['passing']['kind'] not in ('reference', 'moved'):
        continue
      written = argument['written']
      own = written.replace('const ', '').replace('&', '').strip()
      if own == className and written not in forwarded:
        forwarded.append(written)
    for written in forwarded:
      handed = 'std::move(other)' if written.endswith('&&') else 'other'
      lines.append('  %s(%s other) : %s(%s) {}' % (
          cuteName, written, className, handed))
    lines.append('  void *taken[%d] = {};' % len(functions))
    lines.append('')
    lines.append('  bool take(const char *key, void *call) {')
    for index, function in enumerate(functions):
      #  Where a Qt has no such function, its key is not known here
      #  and 'take' says no for it: Qt would never call what Python
      #  hands over.
      asked = '\n'.join((
          '    if (!std::strcmp(key, "%s")) {' % function['key'],
          '      taken[%d] = call;' % index,
          '      return true;',
          '    }'))
      lines.append(wrap(asked, function['conditions']))
    lines.append('    return false;')
    lines.append('  }')
    for index, function in enumerate(functions):
      lines.append('')
      written = '\n'.join(self._writeOverride(index, function))
      lines.append(wrap(written, function['conditions']))
    lines.append('};')
    return '\n'.join(lines)

  def _writeOverride(self, index: int, function: Record) -> List[str]:
    """Gives the lines of one function of the C++ class of ours."""
    cuteName = self.getGenerator().getCuteClassName()
    name = function['name']
    giving, words = function['giving'], function['words']
    arguments = function['arguments']
    shown = ', '.join(
        CppText.joinType(a['written'], a['name']) for a in arguments)
    tail = ''.join(' %s' % w for w in ('const', 'noexcept') if w in words)
    head = CppText.joinType(giving['written'], '%s(%s)' % (name, shown))
    lines = textwrap.wrap(
        function['function'], 75, initial_indent='  //  ',
        subsequent_indent='  //      ')
    whole = '  %s%s override {' % (head, tail)
    if len(whole) <= 77 or not arguments:
      #  A function that takes nothing has no place to break its line
      #  at, as 'QPlatformScreen::subpixelAntialiasingTypeHint()'.
      lines.append(whole)
    else:
      opening = CppText.joinType(giving['written'], '%s(' % name)
      lines.append('  %s' % opening)
      for place, argument in enumerate(arguments):
        end = ')%s override {' % tail if place == len(arguments) - 1 else ','
        lines.append('      %s%s' % (
            CppText.joinType(argument['written'], argument['name']), end))
    callName = '%sCall%d' % (cuteName, index)
    passed = ', '.join(['this', *function['cPassed'], '&handled'])
    nothing = function['cGives'] == 'void'
    lines.append('    if (taken[%d]) {' % index)
    lines.append('      int handled = 0;')
    lines.append('      %s call = reinterpret_cast<%s>(taken[%d]);' % (
        callName, callName, index))
    if nothing:
      lines.append('      call(%s);' % passed)
      lines.append('      if (handled) return;')
    else:
      lines.append(
          '      %s given = call(%s);' % (function['cGives'], passed))
      test = 'handled'
      if function['given'] == '*given':
        test = 'handled && given'
      if function['gives'][1] == 'text':
        #  The text was made for this call alone, so it is removed here.
        lines.append('      if (%s) {' % test)
        lines.append('        %s back(*given);' % giving['className'])
        lines.append('        delete given;')
        lines.append('        return back;')
        lines.append('      }')
      else:
        lines.append('      if (%s) return %s;' % (test, function['given']))
    lines.append('    }')
    names = ', '.join(a['name'] for a in arguments)
    if not function['pure']:
      own = '%s::%s(%s);' % (function['owner'], name, names)
      lines.append('    %s%s' % ('' if nothing else 'return ', own))
    elif not nothing:
      #  Qt has no function of its own here. Without an answer from
      #  Python, what the type is made of from nothing goes back.
      lines.append('    return {};')
    lines.append('  }')
    return lines

  def planTake(self) -> Record:
    """Works out the ritual that hands a Python function over to an
    object of the C++ class of ours, for one of its functions."""
    from . import RitualFileExpert
    generator = self.getGenerator()
    className = generator.getClassName()
    cuteName = generator.getCuteClassName()
    plan = dict(
        ritualName='ritual_take_%s' % className.replace('::', '_'),
        function='a Python function taken by a %s, for the function '
                 'named by the key' % cuteName,
        kind='take', gives='bool',
        takes=(('self', '%s *' % className), ('key', 'const char *'),
               ('call', 'void *')),
        sigil=('bool', 'address', 'chars', 'address'), needs=(),
        unknownTypes=(), unsureNumbers=(), words=(), variadic=False,
        name='', arguments=(), giving=None, inPlace=False,
    )
    body = ['  return static_cast<%s *>(self)->take(key, call);' % cuteName]
    fileExpert = generator.getExpert(RitualFileExpert)
    plan['text'] = fileExpert.writeRitual(plan, body)
    return plan

  def planOwn(self) -> List[Record]:
    """
    Works out, for each function of 'getOverridable' the class declares
    itself, the ritual that runs just that function of Qt and no other:
    'self->QWidget::sizeHint()'. The cute function calls it for an
    object of ours, where the ordinary call would come back to Python.
    """
    generator = self.getGenerator()
    className = generator.getClassName()
    plans = []  # type: List[Record]
    record = generator._readRecord(className)
    for child in record.get('inner', ()):
      if isinstance(child, dict) and child.get('kind') == 'FinalAttr':
        #  Qt forbids building a class on this one, so no object of it
        #  is of a class of ours, and the ordinary call never comes
        #  back to Python.
        return plans
    #  The names the class also has a function of that only Qt itself
    #  may call. A function of such a name that a class built on this
    #  one may call cannot be reached apart from the other one.
    access = 'private' if record.get('tagUsed') == 'class' else 'public'
    closed = set()  # type: Set[str]
    for member in record.get('inner', ()):
      if member.get('kind') == 'AccessSpecDecl':
        access = member['access']
      elif member.get('kind') == 'CXXMethodDecl' and access == 'private':
        closed.add(member.get('name'))
    for function in self.getOverridable():
      if function['owner'] != className or function['pure']:
        continue
      if function['access'] == 'protected' and function['name'] in closed:
        continue
      for member in self._findOwnMembers(function['name']):
        if member.get('mangledName') != function['ritualName'][6:]:
          continue
        hidden = function['access'] == 'protected'
        plan = generator._planFunction(member, own=True, hidden=hidden)
        plan['kind'], plan['key'] = 'own', function['key']
        plan['access'] = function['access']
        plans.append(plan)
    return plans

  def _findOwnMembers(self, name: str) -> List[Record]:
    """Gives the functions of a name the class declares itself."""
    generator = self.getGenerator()
    record = generator._readRecord(generator.getClassName())
    return [
        member for member in record.get('inner', ())
        if member.get('kind') == 'CXXMethodDecl'
        and member.get('name') == name
    ]

  def writeOwnClass(self, plans: List[Record]) -> str:
    """Gives the C++ text of the class through which a ritual reaches
    the functions of Qt that only a class built on it may call."""
    className = self.getGenerator().getClassName()
    ownName = 'Own%s' % className.replace('::', '_')
    names = []  # type: List[str]
    for plan in plans:
      if plan['access'] == 'protected' and plan['name'] not in names:
        names.append(plan['name'])
    if not names:
      return ''
    lines = [
        '//  Only a class built on %s may call these functions of it.' % (
            className,),
        '//  This one is, and makes them free for the rituals to call.',
        'struct %s : %s {' % (ownName, className),
    ]
    lines.extend('  using %s::%s;' % (className, name) for name in names)
    lines.append('};')
    return '\n'.join(lines)
