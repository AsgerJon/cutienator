"""ClassText is the text of the Python file of one cute class."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import collections
import os
import re
import textwrap
import threading
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable

from . import HeaderReader
from .class_tables import SECTION_NAMES, WATCHED_NAME

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Tuple

  Record = Dict[str, Any]


#  How many letters a line may have right now, kept for each thread: 77,
#  and two less for each class the one being written stands inside.
_LOCAL = threading.local()


def _width() -> int:
  """Gives how many letters a line may have right now."""
  return getattr(_LOCAL, 'width', 77)


class ClassText:
  """
  The text of the Python file of one cute class: the heading, the names
  the file brings in, the class with its docstring, the names it binds
  and its sections, and the lists of the class at its end, each line
  at most 77 letters. What goes into it, the functions of the class and
  what is left out and why, is decided by the 'ClassGenerator' of the
  class, the viewer. How it is written down is decided here.

    classText = ClassText()
    classText.setViewer(classGenerator)
    classText.getParts()        # the lines of each part of the file
    classText.getText()         # the whole text of the file
    classText.getNestedLines()  # a class Qt writes inside another

  A class Qt writes inside another has no file of its own, and
  'getParts' and 'getText' refuse it: the text of the class around it
  holds it, through 'getNestedLines', with lines two letters shorter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _wrapWords(words: str, indent: str, width: int = 0) -> List[str]:
    """Gives words as lines of at most 'width' letters, each indented:
    as many as a line may have right now when none is given."""
    return textwrap.wrap(
        ' '.join(words.split()), width or _width(), initial_indent=indent,
        subsequent_indent=indent, break_long_words=False,
        break_on_hyphens=False,
    ) or [indent.rstrip()]

  @staticmethod
  def _wrapCpp(shown: str, first: str, later: str) -> List[str]:
    """
    Gives a function as C++ writes it as lines of at most 77 letters.

    C++ writes a name with what it takes right behind it, as
    'QWidget::setParent(QWidget', which can be longer than a line. Such
    a word is broken behind a '(' or a '::'.

    Parameters
    ----------

    shown : str
      The function as C++ writes it.

    first : str
      What the first line starts with.

    later : str
      What every other line starts with.
    """
    lines, line = [], first
    for word in shown.split():
      pieces = [word]
      while len(later) + len(pieces[-1]) > _width():
        long = pieces.pop()
        room = _width() - len(later)
        cut = max(long.rfind('(', 0, room), long.rfind('::', 0, room - 1))
        if cut <= 0:
          pieces.append(long)
          break
        cut += 1 if long[cut] == '(' else 2
        pieces.extend((long[:cut], long[cut:]))
      for index, piece in enumerate(pieces):
        glue = '' if index or line in (first, later) else ' '
        if len(line) + len(glue) + len(piece) > _width():
          if line.strip() and line not in (first, later):
            lines.append(line)
            line, glue = later, ''
        line = '%s%s%s' % (line, glue, piece)
    lines.append(line)
    return lines

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  __class_generator__ = None  # type: Any

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getViewer(self) -> Any:
    """
    Gives the 'ClassGenerator' of the cute class the text is of.

    Provided by you, through 'setViewer'.

    Raises
    ------

    MissingVariable
      'setViewer' has not been called.
    """
    if self.__class_generator__ is None:
      raise MissingVariable(self, '__class_generator__', object)
    return self.__class_generator__

  def _getHeading(self) -> List[str]:
    """Says who wrote the file, from what, and that it is written
    anew."""
    viewer = self.getViewer()
    tree, className = viewer.getDependencyTree(), viewer.getClassName()
    headerPath = tree.getHeaderPath(className, viewer.getPartName())
    relative = os.path.relpath(headerPath, HeaderReader.getQtHeaderFolder())
    infoSpec = """Written by dev_tooling.ClassGenerator from the records
    of %s, Qt %s. Changes made here are lost."""
    info = infoSpec % (relative, HeaderReader.getQtVersion())
    lines = self._wrapWords(info, '#  ')
    headerReader = tree.getHeaderReader(className, viewer.getPartName())
    if headerReader.hasPrivate():
      if headerPath.startswith(headerReader.getPrivateFolder()):
        infoSpec = """Qt means %s to be private: it declares the
        class in a header it calls private. cutienator does not care.
        Qt hands objects of the class out all the same, and a class we
        are handed is a class we have."""
        lines.append('#')
        lines.extend(self._wrapWords(infoSpec % className, '#  '))
    return lines

  def _writeImports(self) -> List[str]:
    """Gives the lines at the top of the file that bring in names."""
    viewer = self.getViewer()
    needed = viewer._getNeeds()
    className = viewer.getClassName()
    lines = ['from __future__ import annotations', '']
    lines.extend(('from typing import TYPE_CHECKING', ''))
    top = needed['top']
    worktoy = []
    if 'THIS' in top:
      worktoy.append('from worktoy.core.sentinels import THIS')
    if 'overload' in top:
      worktoy.append('from worktoy.dispatch import overload')
    if 'Kee' in top:
      worktoy.append('from worktoy.keenum import Kee')
    if worktoy:
      lines.extend((*worktoy, ''))
    cute = [name for name in (
        'CuteMixin', 'CuteFlags', 'CuteNum', 'MetaCute', 'WAIT',
    ) if name in top]
    ours = []
    if cute:
      ours.append('from ..cute import %s' % ', '.join(cute))
    if 'Rituals' in top:
      ours.append('from ..occult import Rituals')
    classes = [n for n in needed['classes'] if n != className]
    #  The namespace 'Qt', the classes this one is built on, and each
    #  class that holds an enum or a class this file names, are asked of
    #  the package of their part, the cute way. The package brings in
    #  the one file each of them is in, and no other.
    #  Each by what its file is reached through: a class Qt writes inside
    #  a namespace by that namespace, one inside a class by that class.
    asking = {viewer.getImportName(n) for n in classes}
    asked = {partName for partName, _ in asking}
    asked.add('QtCore')
    #  The namespaces whose enums the file names, as 'QtCore:Qt' or
    #  'QtNetwork:QSsl': each is asked of the package of the part its
    #  enums lie in, before the classes of that part.
    spaces = {(*noted.split(':'),) for noted in needed['namespace']}
    asked.update(partName for partName, _ in spaces)
    for partName in viewer.getImportOrder(asked):
      names = sorted({n for p, n in asking if p == partName})
      if partName == 'QtCore':
        #  'QList' and 'QStringList' are classes of QtCore the tree
        #  knows nothing of: cutienator writes them by hand.
        names = sorted({*names, *needed['lists']})
      first = sorted({n for p, n in spaces if p == partName})
      names = [*first, *(n for n in names if n not in first)]
      ours.extend(self._writeAsking(partName, names, ''))
    lines.extend(ours)
    typing = sorted(needed['typing'])
    #  What this class waits for. A class written inside it binds its
    #  own 'WAIT' lines, in its body.
    late = sorted(viewer.__needed_names__['late'])
    #  What the annotations name and the file does not bring in.
    hinted = {*late, *needed['hinted']}
    hinted = sorted(hinted - {className, *classes})
    if typing or hinted:
      lines.append('')
      lines.append('if TYPE_CHECKING:  # pragma: no cover, no mutate')
    if typing:
      lines.append('  from typing import %s' % ', '.join(typing))
    if typing and hinted:
      lines.append('')
    #  A type checker is shown each class the cute way, from the
    #  package of its part. Python never runs these lines, so they
    #  bring nothing in.
    showing = {viewer.getImportName(n) for n in hinted} - asking
    shown = {partName for partName, _ in showing}
    for partName in viewer.getImportOrder(shown):
      names = sorted({n for p, n in showing if p == partName})
      lines.extend(self._writeAsking(partName, names, '  '))
    if late:
      lines.append('else:')
      infoSpec = """The cute classes this file names and is not built on.
      Each is brought in by the program that uses it, and a signature
      naming it waits until then; see 'WAIT'."""
      lines.extend(self._wrapWords(infoSpec, '  #  '))
      for lateName in late:
        lines.append("  %s = WAIT['%s']" % (
            lateName, viewer.getWaitKey(lateName)))
    if 'NoneType' in top:
      lines.append('')
      infoSpec = """The class of None, for a signature that takes None in
      the place of an object or of text."""
      lines.extend(self._wrapWords(infoSpec, '#  '))
      lines.append('NoneType = type(None)')
    return lines

  def _writeAsking(
      self,
      partName: str,
      names: List[str],
      indent: str,
  ) -> List[str]:
    """
    Gives the lines that ask the package of one part of Qt for names of
    it, the cute way: 'from ..QtGui import QFont, QIcon', or
    'from . import QEvent' in a file of that same part. As many names
    stand on a line as fit, and the import is written again for the
    rest. No name gives no line.

    Asking the package is as cheap as asking the file: the package
    brings in the one file a class is in, the first time the class is
    asked for.
    """
    viewer = self.getViewer()
    module = '.' if partName == viewer.getPartName() else '..%s' % partName
    opening, line = '%sfrom %s import ' % (indent, module), ''
    lines = []  # type: List[str]
    for name in names:
      longer = '%s, %s' % (line, name) if line else name
      if line and len(opening) + len(longer) > _width():
        lines.append('%s%s' % (opening, line))
        longer = name
      line = longer
    if line:
      lines.append('%s%s' % (opening, line))
    return lines

  def _writeBringing(self, otherName: str, indent: str) -> str:
    """
    Gives the line by which a function brings in the cute class of
    another class of Qt, the cute way: 'from ..QtGui import QFont'. A
    class Qt writes inside another is brought in with that class, as
    'from ..QtCore import QMetaObject' for 'QMetaObject::Connection'.
    """
    partName, asked = self.getViewer().getImportName(otherName)
    return self._writeAsking(partName, [asked], indent)[0]

  def _countNotWritten(self) -> List[Tuple[int, str]]:
    """Gives how many functions of the class have no ritual, for each
    reason, the most frequent first."""
    viewer = self.getViewer()
    reasons = collections.Counter()  # type: Any
    for _, reason in viewer.getRitualGenerator().getNotWritten():
      reasons[reason.partition(':')[0]] += 1
    return [
        (count, reason) for reason, count in reasons.most_common() if count
    ]

  def _writeClassDocstring(self) -> List[str]:
    """Gives the docstring of the cute class."""
    viewer = self.getViewer()
    className, baseName = viewer.getClassName(), viewer.getBaseName()
    functions, leftOut = viewer.getFunctions(), viewer.getLeftOut()
    written = viewer.getRitualGenerator().getWritten()
    notWritten = viewer.getRitualGenerator().getNotWritten()
    owned = viewer.getDeleteRitual() is not None
    paragraphs = []  # type: List[Any]
    infoSpec = """The cute side of Qt's %s: a plain Python object
    standing in front of one C++ %s."""
    paragraphs.append(infoSpec % (className, className))
    if baseName is not None:
      infoSpec = """It is built on the cute '%s', as Qt's %s is built on
      Qt's %s, and has everything that class has."""
      info = infoSpec % (baseName, className, baseName)
      for parent in viewer.getFurtherBaseNames():
        infoSpec = """ It is built on the cute '%s' as well, as Qt's %s
        is built on Qt's %s too, and has everything that class has."""
        info = '%s%s' % (info, ' '.join(
            (infoSpec % (parent, className, parent)).split()))
        info = info.replace('.It is', '. It is')
      for parent in viewer.getUnreflectedParents():
        infoSpec = """ Qt's %s is built on Qt's %s as well, which is not
        reflected."""
        info = '%s%s' % (info, infoSpec % (className, parent))
      paragraphs.append(info)
    if owned:
      infoSpec = """C++ hands a %s around as a copy, so every C++ %s
      behind a cute one is Python's own: it is removed, by the ritual
      named in '__delete_ritual__', when the cute object goes."""
      paragraphs.append(infoSpec % (className, className))
    names = [*dict.fromkeys(
        f['pythonName'] for f in functions if f['kind'] != 'constructor')]
    makers = [f for f in functions if f['kind'] == 'constructor']
    paragraphs.append(('What exists', None))
    if names:
      infoSpec = """Every function of Qt's %s that has a ritual and that
      Python can call so far, %d %s in all: %s."""
      shown = ', '.join("'%s'" % name for name in names)
      word = 'name' if len(names) == 1 else 'names'
      info = infoSpec % (className, len(names), word, shown)
    else:
      info = """No function of Qt's %s yet.""" % className
    if makers:
      infoSpec = """ It can be made from Python, in %d %s; see
      '__init__'."""
      word = 'way' if len(makers) == 1 else 'ways'
      info = '%s%s' % (info, infoSpec % (len(makers), word))
    else:
      infoSpec = """ None can be made from Python: one comes out of a
      function of another class that gives one back."""
      info = '%s%s' % (info, infoSpec)
    paragraphs.append(info)
    if leftOut:
      paragraphs.append(('What has a ritual and is left out, and why', None))
      for shown, reason in leftOut:
        paragraphs.append(('- ', "Qt's '%s': %s." % (shown, reason)))
    without = len(notWritten)
    if without:
      paragraphs.append(('What has no ritual', None))
      infoSpec = """%d of the %d functions Qt declares:"""
      #  A ritual of our own making stands for no function Qt declares,
      #  and one that runs just the class's own function for one that
      #  has a ritual already.
      ours = ('cast', 'take', 'own', 'list', 'map', 'drop')
      declared = [plan for plan in written if plan['kind'] not in ours]
      total = len(declared) + len(notWritten)
      counted = '; '.join(
          '%d %s' % pair for pair in self._countNotWritten())
      paragraphs.append(
          '%s %s.' % (infoSpec % (without, total), counted))
    paragraphs.append(('What to expect', None))
    infoSpec = """The C++ %s is created at the first use, not by
    '%s(...)'."""
    if viewer.isApplication():
      infoSpec = """The C++ %s is created by '%s(...)' at once, since
      nearly every other object of Qt can only be made after it."""
    expected = [infoSpec % (className, className)]
    infoSpec = """A wrong argument is refused in Python, with
    'DispatchException', and never reaches C++."""
    expected.append(infoSpec)
    infoSpec = """None is taken wherever Qt takes an object by its
    address, or text as C has it, and is passed on as nothing. Whether
    Qt can do with nothing there is as in C++."""
    expected.append(infoSpec)
    if owned:
      infoSpec = """A function giving a %s back gives a copy the ritual
      made for Python, in a new cute %s."""
      expected.append(infoSpec % (className, className))
    else:
      infoSpec = """Python never removes the C++ %s."""
      expected.append(infoSpec % className)
    tree = viewer.getDependencyTree()
    watched = WATCHED_NAME
    ancestors = tree.getAncestors(className, viewer.getPartName())
    if className == watched or watched in [n for _, n in ancestors]:
      infoSpec = """Qt tells when it has removed the C++ %s. Every call
      on the cute object, and every use of it as an argument, then
      raises 'RuntimeError', and nothing reaches C++."""
      expected.append(infoSpec % className)
    unsupported = [name for name, _ in viewer.getUnsupported()]
    if unsupported:
      infoSpec = """Each name of Qt's %s that has no cute function yet,
      %s, holds a function that raises 'NotImplementedError', and its
      docstring says why."""
      shown = ', '.join("'%s'" % name for name in unsupported)
      expected.append(infoSpec % (className, shown))
    for info in expected:
      paragraphs.append(('- ', info))
    lines = ['  """']
    previous = None  # type: Any
    for paragraph in paragraphs:
      if isinstance(paragraph, tuple) and paragraph[1] is None:
        lines.extend(('', '  %s' % paragraph[0]))
        lines.extend(('  %s' % ('-' * len(paragraph[0])), ''))
      elif isinstance(paragraph, tuple):
        lines.extend(self._wrapCpp(paragraph[1], '  - ', '    '))
      else:
        if previous is not None and not isinstance(previous, tuple):
          lines.append('')
        lines.extend(self._wrapWords(paragraph, '  '))
      previous = paragraph
    lines.append('  """')
    return lines

  @staticmethod
  def _writeBanner(sectionName: str) -> List[str]:
    """Gives the three lines that head one section of a class body."""
    full = '  %s#' % ('# ' * ((_width() - 3) // 2))
    head = '  #  %s  ' % sectionName
    if len(head) % 2:
      head = '%s ' % head
    while len(head) < len(full):
      head = '%s# ' % head
    return [full, head.rstrip(), full]

  def _writeNames(self) -> List[str]:
    """
    Gives the lines right under the docstring of the class, which bind
    what the signatures below them name: the classes and the enums Qt
    writes inside the class.

    They stand above every section, since a signature can only name
    what the body has bound on a line above it.
    """
    viewer = self.getViewer()
    className, lines = viewer.getClassName(), []  # type: str, List[str]
    late = sorted(viewer.__needed_names__['late'])
    if viewer.isNested() and late:
      infoSpec = """The cute classes this class names and is not built on.
      Each waits until it is made; see 'WAIT'. A type checker reads the
      imports at the top of the file instead."""
      lines.append('')
      lines.extend(self._wrapWords(infoSpec, '  #  '))
      lines.append('  if not TYPE_CHECKING:')
      for lateName in late:
        lines.append("    %s = WAIT['%s']" % (
            lateName, viewer.getWaitKey(lateName)))
    generators = viewer.getEnumGenerators()
    if generators:
      infoSpec = """The enums Qt writes inside %s, each a class in here
      as in C++, and the names Qt has for the combinations of its flags
      enums."""
      lines.append('')
      lines.extend(self._wrapWords(infoSpec % className, '  #  '))
      for generator in generators:
        ownName = generator.getOwnName()
        lines.append('')
        lines.extend(generator.getNestedLines(_width()))
        flagsName = generator.getFlagsName()
        if flagsName:
          shortName = flagsName.rpartition('::')[2]
          lines.append('')
          lines.extend(self._writeBinding(shortName, ownName))
    inner = viewer.getInnerGenerators()
    if inner:
      infoSpec = """The classes Qt writes inside %s, each a class in here
      as in C++."""
      lines.append('')
      lines.extend(self._wrapWords(infoSpec % className, '  #  '))
      for generator in inner:
        lines.append('')
        lines.extend(generator.getNestedLines())
    return lines

  @staticmethod
  def _writeBinding(name: str, joinedName: str) -> List[str]:
    """Gives the line of the class body that binds a name to what the
    package gave, on two lines when one would be too long."""
    line = '  %s = %s' % (name, joinedName)
    if len(line) <= _width():
      return [line]
    return ['  %s = (' % name, '      %s)' % joinedName]

  def _writeNamespace(self) -> List[str]:
    """Gives the lines of the section that holds the variables of the
    class: the class of Qt it stands for, and its delete ritual."""
    viewer = self.getViewer()
    className = viewer.getClassName()
    lines = ['  #  Class Variables']
    lines.append('  #  The class of Qt this class stands for.')
    lines.append("  __qt_class__ = '%s'" % className)
    if viewer.isShared():
      lines.append('  #  The part of Qt it is of, as another part has a '
                   'class of its name too.')
      lines.append("  __qt_part__ = '%s'" % viewer.getPartName())
    if className == WATCHED_NAME:
      infoSpec = """Qt can watch a %s and tell when it has removed it.
      Every class built on this one is a %s too, and inherits this."""
      lines.append('')
      lines.extend(self._wrapWords(
          infoSpec % (className, className), '  #  '))
      lines.append('  __watched_by_qt__ = True')
    casts = [
        plan for plan in viewer.getRitualGenerator().getWritten()
        if plan['kind'] == 'cast'
        and plan['baseName'] in viewer.getFurtherBaseNames()
    ]
    if casts:
      lines.append('')
      infoSpec = """Qt's %s is built on more than one class. The part of
      a C++ %s that belongs to a class after the first begins somewhere
      inside the object, and the ritual named for that class gives
      where; see 'CuteMixin._addressAs'."""
      lines.extend(self._wrapWords(
          infoSpec % (className, className), '  #  '))
      lines.append('  __cast_rituals__ = {')
      for plan in casts:
        line = "      '%s': '%s'," % (plan['baseName'], plan['ritualName'])
        if len(line) > _width():
          line = "      '%s':\n          '%s'," % (
              plan['baseName'], plan['ritualName'])
        lines.append(line)
      lines.append('  }')
    lines.extend(self._writeTakingOver())
    deleteRitual = viewer.getDeleteRitual()
    if deleteRitual is not None:
      lines.append('')
      infoSpec = """Qt's '~%s()'. Naming it makes this a value class:
      Python owns every C++ %s behind a cute one, and removes it by
      this ritual."""
      info = infoSpec % (className, className)
      lines.extend(self._wrapWords(info, '  #  '))
      line = "  __delete_ritual__ = '%s'" % deleteRitual
      if len(line) > _width():
        line = "  __delete_ritual__ = (\n      '%s')" % deleteRitual
      lines.append(line)
    lines.extend((
        '', '  #  Fallback Variables', '', '  #  Private Variables',
        '', '  #  Public Variables', '', '  #  Virtual Variables',
    ))
    return lines

  def _writeCall(
      self,
      opening: str,
      called: str,
      ritualName: str,
      passed: List[str],
      closing: str = ')',
      leading: str = '',
      named: str = '',
  ) -> List[str]:
    """
    Gives the lines of one call of a ritual, kept to 77 letters where
    the names allow it.

    Parameters
    ----------

    opening : str
      What stands before the call, indent included, as
      '    address = '.

    called : str
      What is called, as 'self.uglySide.call'.

    ritualName : str
      The ritual.

    passed : List[str]
      What the ritual is handed, in order.

    closing : str
      What ends the call, as ')' or '))'.

    leading : str
      What the call is handed before the ritual, as "'QPaintDevice'"
      for 'self._callAs', or nothing.

    named : str
      The name the lines above bound the ritual to, where the function
      picks between two, or nothing.
    """
    quoted = named or "'%s'" % ritualName
    head = [leading] if leading else []
    whole = '%s%s(%s%s' % (
        opening, called, ', '.join([*head, quoted, *passed]), closing)
    if len(whole) <= _width():
      return [whole]
    indent = ' ' * (len(opening) - len(opening.lstrip()))
    if opening.endswith('(') and len('%s%s(' % (opening, called)) > _width():
      #  What stands before the call fills the line, as the name of a
      #  class and of an enum of it. The call goes on lines of its own
      #  below it.
      lines = [opening]
      lines.extend(self._writeCall(
          '%s    ' % indent, called, ritualName, passed, closing[:1],
          leading))
      lines[-1] = '%s%s' % (lines[-1], closing[1:])
      return lines
    inner = '%s    ' % indent
    lines = ['%s%s(' % (opening, called)]
    rest = ', '.join(passed)
    whole = '%s%s,' % (inner, ', '.join([*head, quoted, *passed]))
    if len(whole) <= _width():
      lines.append(whole)
    else:
      first = '%s%s,' % (inner, ', '.join([*head, quoted]))
      if len(first) > _width():
        if head:
          lines.append('%s%s,' % (inner, leading))
        first = '%s%s,' % (inner, quoted)
      if len(first) > _width():
        #  A name longer than a line is written as two texts side by
        #  side, which Python reads as one.
        room = _width() - len(inner) - 3
        pieces = [
            ritualName[i:i + room] for i in range(0, len(ritualName), room)
        ]
        for piece in pieces[:-1]:
          lines.append("%s'%s'" % (inner, piece))
        first = "%s'%s'," % (inner, pieces[-1])
      lines.append(first)
      if rest:
        packed = textwrap.wrap(
            '%s,' % rest, _width(), initial_indent=inner,
            subsequent_indent=inner, break_long_words=False,
            break_on_hyphens=False,
        )
        lines.extend(packed)
    lines.append('%s%s' % (indent, closing))
    return lines

  def _writeDef(self, function: Record) -> List[str]:
    """Gives the decorators and the 'def' line of one function."""
    viewer = self.getViewer()
    lines = []  # type: List[str]
    static = function['kind'] == 'static method'
    if static:
      lines.append('  @staticmethod')
    if function['overloaded']:
      for signature in function['signatures']:
        line = '  @overload(%s)' % ', '.join(signature)
        if len(line) <= _width():
          lines.append(line)
          continue
        lines.append('  @overload(')
        lines.extend(textwrap.wrap(
            '%s,' % ', '.join(signature), _width(), initial_indent='      ',
            subsequent_indent='      ', break_long_words=False,
        ))
        lines.append('  )')
    shown = [] if static else ['self']
    stacked = len(function['signatures']) > 1
    for parameter in function['parameters']:
      annotation = parameter['annotation']
      default = parameter['default'] if stacked else None
      if parameter['nullable'] or (default and 'made' in default):
        annotation = 'Optional[%s]' % annotation
      text = '%s: %s' % (parameter['name'], annotation)
      if default is not None:
        text = '%s = %s' % (text, default['text'])
      shown.append(text)
    gives = function['gives']
    annotation = 'None' if gives is None else gives['annotation']
    if function.get('inPlace'):
      #  'a += b' gives 'a' itself back, in C++ and in Python.
      annotation = viewer.getLocalName()
    whole = '  def %s(%s) -> %s:' % (
        function['pythonName'], ', '.join(shown), annotation)
    if len(whole) <= _width():
      lines.append(whole)
    else:
      lines.append('  def %s(' % function['pythonName'])
      for text in shown:
        line = '      %s,' % text
        if len(line) > _width() and ' = ' in text:
          #  A default too long for the line goes on a line of its own.
          named, _, default = text.partition(' = ')
          lines.append('      %s = (' % named)
          line = '          %s),' % default
          if len(line) > _width() and ' | ' in default:
            #  Flags joined with '|' go one to a line.
            *first, last = default.split(' | ')
            lines.extend('          %s |' % one for one in first)
            line = '          %s),' % last
        lines.append(line)
      lines.append('  ) -> %s:' % annotation)
    return lines

  def _writeDocstring(self, function: Record) -> List[str]:
    """Gives the docstring of one function."""
    viewer = self.getViewer()
    plan, className = function['plan'], viewer.getClassName()
    stem = className.lower().replace('::', '-')
    if function['kind'] == 'constructor':
      infoSpec = """Notes what was given, for Qt's '%s', which is called
      at the first use."""
      if viewer.isApplication():
        infoSpec = """Calls Qt's '%s' at once: nearly every other
        object of Qt can only be made after the application."""
      anchor = viewer.getPythonName()
    else:
      infoSpec = """Calls Qt's '%s'."""
      anchor = plan['name']
    lines = ['    """']
    lines.extend(self._wrapCpp(
        infoSpec % plan['function'], '    ', '    '))
    link = 'https://doc.qt.io/qt-6/%s.html#%s' % (stem, anchor)
    whole = "    Qt's own words: %s" % link
    lines.append('')
    if len(whole) <= _width():
      lines.append(whole)
    else:
      if len(link) > _width() - 4:
        #  A link cannot be broken, so one too long for a line is given
        #  as the page alone, without the place on it.
        link = link.partition('#')[0]
      lines.extend(("    Qt's own words:", '    %s' % link))
    stacked = len(function['signatures']) > 1
    parameters = function['parameters']
    if parameters:
      lines.extend(('', '    Parameters', '    ----------'))
      for parameter in parameters:
        annotation = parameter['annotation']
        words = parameter['words']
        if parameter['nullable']:
          annotation = 'Optional[%s]' % annotation
          if parameter['kind'] == 'chars':
            words = '%s None is passed on as no text.' % words
          else:
            words = '%s None is passed on as no object.' % words
        default = parameter['default'] if stacked else None
        if default is not None:
          if 'left' in default:
            infoSpec = """%s May be left out, as in Qt: what '%s'
            gives is then passed on."""
            words = infoSpec % (words, default['made'])
          elif 'made' in default:
            annotation = 'Optional[%s]' % annotation
            infoSpec = """%s May be left out, as in Qt: a new '%s' is
            then passed on."""
            words = infoSpec % (words, default['made'])
          else:
            infoSpec = """%s May be left out, as in Qt: it is then %s."""
            words = infoSpec % (words, default['text'])
        lines.append('')
        lines.append('    %s : %s' % (parameter['name'], annotation))
        lines.extend(self._wrapWords(words, '      '))
    gives = function['gives']
    if gives is not None and gives['words']:
      lines.extend(('', '    Returns', '    -------', ''))
      lines.append('    %s' % gives['annotation'])
      lines.extend(self._wrapWords(gives['words'], '      '))
    lines.append('    """')
    if len(lines) == 3 and len(lines[1]) <= 70:
      return ['    """%s"""' % lines[1].strip()]
    return lines

  def _writeBody(self, function: Record) -> List[str]:
    """Gives the lines of one function below its docstring."""
    viewer = self.getViewer()
    plan, className = function['plan'], viewer.getLocalName()
    kind, gives = function['kind'], function['gives']
    lines = self._wrapCpp(plan['function'], '    #  ', '    #      ')
    stacked = len(function['signatures']) > 1
    passed = []
    for parameter in function['parameters']:
      default = parameter['default'] if stacked else None
      if default is not None and 'made' in default:
        name = parameter['name']
        left = default.get('left', 'None')
        lines.append('    if %s is %s:' % (name, left))
        brought = []  # type: List[str]
        if parameter['late'] and parameter['bring']:
          brought.append(parameter['bring'])
        for otherName in default.get('brings', ()):
          if otherName not in brought:
            brought.append(otherName)
        for otherName in brought:
          lines.append(self._writeBringing(otherName, '      '))
        lines.append('      %s = %s' % (name, default['made']))
      passed.append(parameter['passed'])
    ritualName = plan['ritualName']
    if kind == 'constructor':
      opening = '    self._noteCreation(%s, lambda: ' % className
      if len('%sRituals.call(' % opening) > _width():
        #  The name of the class fills the line, so it goes on a line of
        #  its own below.
        lines.append('    self._noteCreation(')
        opening = '        %s, lambda: ' % className
      lines.extend(self._writeCall(
          opening, 'Rituals.call', ritualName, passed, '))'))
      if viewer.isApplication():
        #  Reading the ugly side is the first use.
        lines.append('    self._getUglySide()')
      return lines
    called = 'Rituals.call' if kind in ('static method', 'friend') else (
        'self.uglySide.call')
    if kind == 'friend':
      #  The ritual takes the object where Qt's operator takes it.
      place = function['operator']['selfIndex']
      passed = [*passed[:place], function['selfPassed'], *passed[place:]]
    leading = ''
    ownKey = (viewer.getPartName(), viewer.getClassName())
    if kind == 'method' and ownKey in viewer._getPartNames():
      #  The object may be of a class built on this one beside another,
      #  whose part of this class begins inside the object. The ritual
      #  is handed the address of that part.
      called, leading = 'self._callAs', "'%s'" % viewer.getClassName()
    named = ''
    if function.get('ownRitual'):
      #  C++ looks this function up in the object. In an object of ours
      #  that leads to the Python function a class of the program wrote
      #  in its place, which may be the very one calling this. So for
      #  such an object just the class's own function is run.
      named = 'ritual'
      for indent, ritual in (('    ', ritualName), (
          '      ', function['ownRitual'])):
        line = "%sritual = '%s'" % (indent, ritual)
        if len(line) <= _width():
          lines.append(line)
        else:
          #  A name too long for the line is written in pieces, which
          #  Python reads as one text.
          room = _width() - len(indent) - 7
          pieces = [
              ritual[at:at + room] for at in range(0, len(ritual), room)]
          lines.append('%sritual = (' % indent)
          lines.extend("%s    '%s'" % (indent, piece) for piece in pieces)
          lines[-1] = '%s)' % lines[-1]
        if indent == '    ':
          lines.append('    if self.uglySide.isOurs():')
    givenKind = gives['kind']
    if givenKind == 'nothing':
      lines.extend(self._writeCall(
          '    ', called, ritualName, passed, ')', leading, named))
    elif givenKind in ('number', 'text'):
      lines.extend(self._writeCall(
          '    return ', called, ritualName, passed, ')', leading, named))
    elif givenKind == 'chars':
      lines.extend(self._writeCall(
          '    chars = ', called, ritualName, passed, ')', leading, named))
      lines.append('    return None if chars is None else chars.decode()')
    elif givenKind in ('enum', 'flags'):
      lines.extend(self._writeCall(
          '    return %s(' % gives['maker'], called, ritualName, passed,
          '))', leading, named,
      ))
    else:
      lines.extend(self._writeCall(
          '    address = ', called, ritualName, passed, ')', leading, named))
      holder = gives['holder']
      if gives['late'] and gives['bring']:
        #  The file of the class may not be brought in yet. It is
        #  brought in here, at the first call.
        lines.append(self._writeBringing(gives['bring'], '    '))
      maker = '_cuteAt' if givenKind == 'address' else '_cuteOwning'
      lines.append('    return %s.%s(address)' % (holder, maker))
    if function.get('inPlace'):
      lines.append('    return self')
    return lines

  @staticmethod
  def _writeFallback(pythonName: str) -> List[str]:
    """
    Gives the lines of the function that answers, at a name Python asks
    one side of an operator for, a call no signature takes.

    Python has a word for that answer: 'NotImplemented'. Python then
    asks the other side, and when that cannot either, 'a + b' raises
    'TypeError' and 'a == b' is False. It stands where the door stands
    at every other overloaded name.
    """
    return [
        '',
        '  @overload.fallback',
        '  def %s(self, *args: object) -> object:' % pythonName,
        '    """',
        '    Tells Python that no function of this name takes what it was',
        "    handed, with Python's own word for it. Python then asks the",
        '    other side of the operator.',
        '    """',
        '    return NotImplemented',
    ]

  @staticmethod
  def _writeShape(indent: str, shape: Any) -> List[str]:
    """Gives the lines of one thing a function gives or takes, as the
    table of functions to take over holds it, on two lines when one
    would be too long."""
    line = '%s%r,' % (indent, (*shape,))
    if len(line) <= _width():
      return [line]
    word, how, where = shape
    return [
        '%s(%r, %r,' % (indent, word, how),
        '%s %r),' % (indent, where),
    ]

  def _writeTakingOver(self) -> List[str]:
    """
    Gives the lines of the class body that say which ritual hands a
    Python function over to an object of the class, and which
    functions Qt calls itself that the class is the first to declare,
    so that a class of a program built on it can write them anew.
    """
    viewer = self.getViewer()
    generator = viewer.getRitualGenerator()
    className, lines = viewer.getClassName(), []  # type: str, List[str]
    for plan in generator.getWritten():
      if plan['kind'] != 'take':
        continue
      infoSpec = """A C++ %s Python makes is of a C++ class of ours, in
      which Python can take functions over. This ritual hands one over;
      see 'CuteMixin._takeOver'."""
      lines.append('')
      lines.extend(self._wrapWords(infoSpec % className, '  #  '))
      lines.append("  __take_ritual__ = '%s'" % plan['ritualName'])
    table = collections.OrderedDict()  # type: Dict[str, List[Any]]
    for function in generator.getOverridable():
      if function['rootOwner'] != className:
        continue
      shapes = [function['gives'], *function['takes']]
      wheres = [
          viewer.getCuteName(what).findWhere(how) for _, how, what in shapes]
      if any(where is None for where in wheres):
        continue
      turned = [(s[0], s[1], w) for s, w in zip(shapes, wheres)]
      table.setdefault(function['name'], []).append(
          (function['key'], turned[0], (*turned[1:],)))
    lines.extend(self._writeLeftOutVirtuals(table))
    if not table:
      return lines
    infoSpec = """The functions Qt calls itself that %s is the first to
    declare. A class of a program built on it can write one anew, and
    Qt then calls that. For each name: the key C++ knows the function
    by, what it gives, and what it takes."""
    lines.append('')
    lines.extend(self._wrapWords(infoSpec % className, '  #  '))
    lines.append('  __virtual_functions__ = {')
    for name, variants in table.items():
      lines.append("      '%s': (" % name)
      for key, gives, takes in variants:
        room = _width() - 14
        pieces = [key[at:at + room] for at in range(0, len(key), room)]
        #  A key too long for the line is written in pieces, which
        #  Python reads as one text.
        lines.append("          ('%s'" % pieces[0])
        lines.extend("           '%s'" % piece for piece in pieces[1:])
        lines[-1] = '%s,' % lines[-1]
        lines.extend(self._writeShape('           ', gives))
        if not takes:
          lines.append('           ()),')
          continue
        lines.append('           (')
        for take in takes:
          lines.extend(self._writeShape('               ', take))
        lines.append('           )),')
      lines.append('      ),')
    lines.append('  }')
    return lines

  def _writeLeftOutVirtuals(self, table: Any) -> List[str]:
    """
    Gives the lines of the class body that name the functions Qt calls
    itself which the class is the first to declare and of which none
    of that name can be handed to Python yet, each as Qt declares it.
    'CuteMixin._refuseLeftOut' refuses a class of a program that writes
    one of them anew: Qt would never call what it wrote.

    Parameters
    ----------

    table : Any
      The functions of the class that can be handed to Python, by
      name, as '_writeTakingOver' gathered them.
    """
    viewer = self.getViewer()
    generator = viewer.getRitualGenerator()
    leftOut = collections.OrderedDict()  # type: Dict[str, List[str]]
    for virtual in generator.getDeclaredVirtuals():
      if virtual['name'] not in table:
        leftOut.setdefault(virtual['name'], []).append(virtual['written'])
    if not leftOut:
      return []
    infoSpec = """The functions Qt calls itself that %s is the first to
    declare and that cannot be handed to Python yet, each as Qt
    declares it. A class of a program that writes one of them anew is
    refused, since Qt would never call what it wrote; see
    'CuteMixin._refuseLeftOut'."""
    lines = ['']
    lines.extend(self._wrapWords(infoSpec % viewer.getClassName(), '  #  '))
    lines.append('  __virtual_left_out__ = {')
    for name, declarations in leftOut.items():
      lines.append("      '%s': (" % name)
      for written in declarations:
        #  A declaration too long for the line is written in pieces,
        #  which Python reads as one text.
        pieces, room = [], _width() - 13  # type: List[str], int
        while len(written) > room:
          cut = written.rfind(' ', 0, room) + 1 or room
          pieces.append(written[:cut])
          written = written[cut:]
        pieces.append(written)
        lines.extend("          '%s'" % piece for piece in pieces)
        lines[-1] = '%s,' % lines[-1]
      lines.append('      ),')
    lines.append('  }')
    return lines

  @staticmethod
  def _findUnsupportedSection(name: str) -> str:
    """Gives the section of the class body the function standing at a
    name with no cute function yet is written in."""
    return 'CONSTRUCTORS' if name == '__init__' else 'PUBLIC METHODS'

  @staticmethod
  def _writeText(text: str, indent: str) -> List[str]:
    """
    Gives a text as Python writes it, as pieces in double quotes on
    lines of their own, each line at most as long as a line may be
    right now. Python reads pieces side by side as one text. A piece
    ends after a space where it can, and a word longer than a line is
    cut.
    """
    room = _width() - len(indent) - 2
    pieces, piece = [], ''  # type: List[str], str
    for word in re.findall(r'\S+\s*', text):
      #  Each word as it stands between the quotes, so that what is
      #  measured is what is written.
      word = word.replace('\\', '\\\\').replace('"', '\\"')
      while len(piece) + len(word) > room:
        if piece:
          pieces.append(piece)
          piece = ''
          continue
        cut = room
        #  A cut never parts a backslash from what it stands before.
        while (len(word[:cut]) - len(word[:cut].rstrip('\\'))) % 2:
          cut -= 1
        pieces.append(word[:cut])
        word = word[cut:]
      piece = '%s%s' % (piece, word)
    if piece or not pieces:
      pieces.append(piece)
    return ['%s"%s"' % (indent, piece) for piece in pieces]

  def _writeUnsupported(self, name: str, reasons: Any) -> List[str]:
    """
    Gives the lines of the function standing at a name of Qt that has
    no cute function yet, which raises 'NotImplementedError'. It is a
    staticmethod, so that it is the same through the class and through
    an object. Its docstring names each function of Qt at the name, as
    Qt declares it, and why it has none, and so does what it raises.

    Parameters
    ----------

    name : str
      The name, as Python has it, as 'nativeEvent'.

    reasons : Any
      For each function of Qt at the name: the function as C++ writes
      it, and the reason in words.
    """
    viewer = self.getViewer()
    lines = ['  @staticmethod', '  def %s(*__, **_) -> Never:' % name]
    docstring = ['    """']
    first, later = ('    ', '    ') if len(reasons) == 1 else (
        '    - ', '      ')
    said = []  # type: List[str]
    for shown, reason in reasons:
      info = "Qt's '%s': %s." % (shown, reason)
      said.append(info)
      docstring.extend(self._wrapCpp(info, first, later))
    docstring.append('    """')
    if len(docstring) == 3 and len(docstring[1]) <= 70:
      docstring = ['    """%s"""' % docstring[1].strip()]
    lines.extend(docstring)
    info = "'%s.%s' has no cute function yet. %s" % (
        viewer.getDottedName(), name, ' '.join(said))
    alone = self._writeText(info, '')
    whole = '    raise NotImplementedError(%s)' % alone[0]
    if len(alone) == 1 and len(whole) <= _width():
      lines.append(whole)
      return lines
    lines.append('    raise NotImplementedError(')
    lines.extend(self._writeText(info, '        '))
    if len(lines[-1]) < _width():
      lines[-1] = '%s)' % lines[-1]
    else:
      lines.append('    )')
    return lines

  def _writeFunction(self, function: Record) -> List[str]:
    """Gives every line of one function of the class body."""
    lines = [
        *self._writeDef(function), *self._writeDocstring(function),
        *self._writeBody(function),
    ]
    if function.get('fallbackAfter'):
      lines.extend(self._writeFallback(function['pythonName']))
    return lines

  def _writeListKinds(self) -> List[str]:
    """
    Gives the lines at the end of the file that make the class of each
    kind of list holding the class, and collect it in 'QList'. The
    list of a class is made in the file of that class, so that there
    is one as soon as there can be an object of the class.
    """
    viewer = self.getViewer()
    generator = viewer.getRitualGenerator()
    className, lines = viewer.getClassName(), []  # type: str, List[str]
    for listed in generator.getOwnListKinds():
      names = generator.getListNames(listed)
      rituals = {
          plan['listRole']: plan['ritualName']
          for plan in generator.getWritten()
          if plan['kind'] == 'list' and plan['listed'] is listed
      }
      infoSpec = """Qt's '%s': the list of %s, which 'QList[%s]' gives.
      It is made here, so that there is one as soon as there can be a
      %s.""" % (listed['listType'], className, className, className)
      if names:
        infoSpec = """%s Qt has a name of its own for it.""" % infoSpec
      lines.extend(('', ''))
      lines.extend(self._wrapWords(infoSpec, '#  '))
      lines.append('%sQList.createKind(' % ''.join(
          '%s = ' % name for name in names))
      lines.append("    %s, '%s'," % (className, listed['crossing']))
      if names:
        lines.append("    name='%s'," % names[0])
      for role in ('make', 'add', 'size', 'at', 'drop'):
        lines.append("    %s='%s'," % (role, rituals[role]))
      lines.append(')')
    for mapped in generator.getOwnMapKinds():
      names = generator.getMapNames(mapped)
      rituals = {
          plan['mapRole']: plan['ritualName']
          for plan in generator.getWritten()
          if plan['kind'] == 'map' and plan['mapped'] is mapped
      }
      key = 'str' if mapped['keyWord'] == 'text' else 'int'
      pattern = mapped['pattern']
      infoSpec = """Qt's '%s': the %s from %s to %s, which '%s[%s, %s]'
      gives. It is completed here, in the file of the class of its
      values.""" % (
          mapped['mapType'], pattern, 'text' if key == 'str' else 'a number',
          className, pattern, key, className)
      if names:
        infoSpec = """%s Qt has a name of its own for it.""" % infoSpec
      lines.extend(('', ''))
      lines.extend(self._wrapWords(infoSpec, '#  '))
      lines.append('%s%s.createKind(' % (
          ''.join('%s = ' % name for name in names), pattern))
      lines.append("    %s, %s, '%s'," % (
          key, className, mapped['crossing']))
      if names:
        lines.append("    name='%s'," % names[0])
      for role in ('make', 'put', 'size', 'key', 'value', 'has', 'get',
                   'drop'):
        lines.append("    %s='%s'," % (role, rituals[role]))
      lines.append(')')
    return lines

  def _getClassLines(self) -> List[str]:
    """Gives the class statement and everything below it."""
    viewer = self.getViewer()
    baseName, pythonName = viewer.getBaseName(), viewer.getPythonName()
    bases = [
        viewer.getDottedName(name) for name in (
            *filter(None, (baseName,)), *viewer.getFurtherBaseNames())]
    functions = viewer.getFunctions()
    lines = []  # type: List[str]
    if not bases:
      lines.append('class %s(CuteMixin, metaclass=MetaCute):' % pythonName)
    else:
      lines.append('class %s(%s):' % (pythonName, ', '.join(bases)))
    lines.extend(self._writeClassDocstring())
    lines.extend(self._writeNames())
    for sectionName in SECTION_NAMES:
      lines.append('')
      lines.extend(self._writeBanner(sectionName))
      if sectionName == 'NAMESPACE':
        lines.append('')
        lines.extend(self._writeNamespace())
      for function in functions:
        if function['section'] != sectionName:
          continue
        lines.append('')
        lines.extend(self._writeFunction(function))
      for name, reasons in viewer.getUnsupported():
        if self._findUnsupportedSection(name) != sectionName:
          continue
        lines.append('')
        lines.extend(self._writeUnsupported(name, reasons))
    return '\n'.join(lines).split('\n')

  def getParts(self) -> Record:
    """
    Gives what the file is made of, each part as its lines: 'opening',
    the docstring of the file and its license; 'heading', who wrote the
    file and from what; 'imports', the names the file brings in;
    'body', the class statement and everything below it; 'lists', the
    lists of the class made at the end of the file.

    Raises
    ------

    ValueError
      Qt writes the class inside another, so it has no file of its own.
    """
    viewer = self.getViewer()
    if viewer.isNested():
      infoSpec = """Qt writes '%s' inside another class, so it has no
      file of its own: the generator of '%s' writes it."""
      className = viewer.getClassName()
      info = infoSpec % (
          className, viewer.getCuteName().getTopClassName())
      raise ValueError(' '.join(info.split()))
    className = viewer.getClassName()
    opening = ['"""', '%s binding of the Qt C++' % className, '"""']
    opening.extend(('#  Apache-2.0 license',
                    '#  Copyright (c) 2026 Asger Jon Vistisen'))
    heading = self._getHeading()
    imports = self._writeImports()
    body = self._getClassLines()
    return dict(
        opening=opening, heading=heading, imports=imports, body=body,
        lists=self._writeListKinds())

  def getStandInText(self, reason: str) -> str:
    """
    Gives the whole text of the file of a class of Qt that has no cute
    class yet: a class 'UnsupportedMeta' makes, at the name and in the
    file the cute class would have, whose docstring names the class of
    Qt and says why. Making one, or reading an attribute it lacks,
    raises NotImplementedError saying that; and a 'WAIT' for the class
    holds it.

    Raises
    ------

    ValueError
      Qt writes the class inside another, so it has no file of its own.
    """
    viewer = self.getViewer()
    className, partName = viewer.getClassName(), viewer.getPartName()
    if viewer.isNested():
      infoSpec = """Qt writes '%s' inside another class, so it has no
      file of its own: the generator of '%s' writes it."""
      info = infoSpec % (
          className, viewer.getCuteName().getTopClassName())
      raise ValueError(' '.join(info.split()))
    pythonName = viewer.getPythonName()
    infoSpec = """%s stands in for the class '%s' of Qt, which has no
    cute class yet."""
    about = ' '.join((infoSpec % (pythonName, className)).split())
    infoSpec = """Qt's class '%s' of %s: %s"""
    said = ' '.join((infoSpec % (className, partName, reason)).split())
    lines = [
        '"""', *textwrap.wrap(about, _width()), '"""',
        '#  Apache-2.0 license',
        '#  Copyright (c) 2026 Asger Jon Vistisen',
        *self._getHeading(),
        'from __future__ import annotations',
        '',
        'from ..cute import UnsupportedMeta',
        '',
        '',
        'class %s(metaclass=UnsupportedMeta):' % pythonName,
        '  """',
        *('  %s' % line for line in textwrap.wrap(said, _width() - 2)),
        '  """',
        '',
        '  #  The class of Qt this class stands in for.',
        "  __qt_class__ = '%s'" % className,
    ]
    if viewer.isShared():
      lines.append('  #  The part of Qt it is of, as another part has a '
                   'class of its name too.')
      lines.append("  __qt_part__ = '%s'" % partName)
    return '%s\n' % '\n'.join(lines)

  def getText(self) -> str:
    """
    Gives the whole text of the file, without writing it: the parts
    'getParts' gives, in order, two empty lines before the class.

    Raises
    ------

    ValueError
      Qt writes the class inside another, so it has no file of its own.
    """
    parts = self.getParts()
    lines = [*parts['opening'], *parts['heading'], *parts['imports']]
    lines.extend(('', ''))
    lines.extend((*parts['body'], *parts['lists']))
    return '%s\n' % '\n'.join(lines)

  def getNestedLines(self) -> List[str]:
    """
    Gives the class as the lines that stand in the body of the class Qt
    writes it inside, where C++, PySide6 and PyQt have it:
    'QMetaObject.Connection'. Its lines are two letters shorter, and
    stand two letters further in.
    """
    held = _width()
    _LOCAL.width = held - 2
    try:
      lines = self._getClassLines()
    finally:
      _LOCAL.width = held
    return ['  %s' % line if line.strip() else '' for line in lines]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setViewer(self, viewer: Any) -> None:
    """Sets the 'ClassGenerator' of the cute class the text is of."""
    self.__class_generator__ = viewer
