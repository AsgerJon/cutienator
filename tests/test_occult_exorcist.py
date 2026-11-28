"""
TestOccultExorcist tests 'Exorcist', which drives the rituals the
compiler or the linker refused out of a ritual file, and nothing else.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import shutil
import tempfile
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator.occult import Exorcist

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import List, Tuple

  Item = Tuple[str, str, int, int]

#  A ritual file made up for the tests, one line for each entry, so
#  that line 'n' of the file is '_LINES[n - 1]'. It holds an item of
#  every kind 'Exorcist' knows, and the pieces it must pass by: a block
#  after 'extern "C"' naming no ritual (58 to 61), one never closed (63
#  on), and a Cute class never closed (66).
_LINES = (
  '//  Written by hand for the test of Exorcist.',  # 1
  '#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>',  # 2
  '#include <QtCore/QtCore>',  # 3
  '#if QT_CONFIG(cutie)',  # 4
  '#include <QtCore/qcutie.h>',  # 5
  '#include <QtCore/qtcore-config.h>',  # 6
  '',  # 7
  "//  Qt's own code, from here to the line of dashes.",  # 8
  '',  # 9
  '//  from src/corelib/cutie.cpp, line 10, as _ZN11CutieHelper4helpEv',
  'QT_BEGIN_NAMESPACE',  # 11
  'class CutieHelper {',  # 12
  'public:',  # 13
  '  int help();',  # 14
  '};',  # 15
  'inline int CutieHelper::help()',  # 16
  '{',  # 17
  '    return 1;',  # 18
  '}',  # 19
  'QT_END_NAMESPACE',  # 20
  '',  # 21
  '//  from src/corelib/cutie.cpp, line 30, as _Z10cutieOtheri',  # 22
  'struct CutieOther { int x; };',  # 23
  'int cutieOther(int value)',  # 24
  '{',  # 25
  '    return value;',  # 26
  '}',  # 27
  '//  ' + '-' * 71,  # 28
  '',  # 29
  'typedef void (*CuteQCutieCall0)(const void *, int *);',  # 30
  'class CuteQCutie : public QCutie {',  # 31
  'public:',  # 32
  '  void *taken[1] = {};',  # 33
  '',  # 34
  '  //  int QCutie::size() const',  # 35
  '  int size() const override {',  # 36
  '    return 0;',  # 37
  '  }',  # 38
  '',  # 39
  '  //  bool QCutie::operator==(const QCutie &other) const',  # 40
  '  bool operator==(const QCutie &other) const {',  # 41
  '    return true;',  # 42
  '  }',  # 43
  '};',  # 44
  '',  # 45
  '//  int QCutie::size() const',  # 46
  'extern "C" Q_DECL_EXPORT',  # 47
  'int ritual_ZNK6QCutie4sizeEv(',  # 48
  '    const QCutie *self) {',  # 49
  '  return self->size();',  # 50
  '}',  # 51
  '',  # 52
  'extern "C" Q_DECL_EXPORT',  # 53
  'void ritual_ZN6QCutie5clearEv(QCutie *self) {',  # 54
  '  self->clear();',  # 55
  '}',  # 56
  '',  # 57
  'extern "C" Q_DECL_EXPORT',  # 58
  'int not_one(int x) {',  # 59
  '  return x;',  # 60
  '}',  # 61
  '#endif  // QT_CONFIG(cutie)',  # 62
  'extern "C" Q_DECL_EXPORT',  # 63
  'int ritual_never_closed(int x) {',  # 64
  '  return x;',  # 65
  'class CuteBroken : public QCutie {',  # 66
)

#  The items of '_LINES', each as 'Exorcist' gives it.
_HELPER = ('copied', 'src/corelib/cutie.cpp, line 10, as '
           '_ZN11CutieHelper4helpEv', 10, 21)
_OTHER = ('copied', 'src/corelib/cutie.cpp, line 30, as _Z10cutieOtheri',
          22, 27)
_TYPEDEF = ('typedef', 'CuteQCutieCall0', 30, 30)
_CUTE = ('cute class', 'CuteQCutie', 31, 44)
_SIZE = ('cute function', 'size', 35, 38)
_EQUAL = ('cute function', 'operator==', 40, 43)
_RITUAL_SIZE = ('ritual', 'ritual_ZNK6QCutie4sizeEv', 46, 51)
_RITUAL_CLEAR = ('ritual', 'ritual_ZN6QCutie5clearEv', 53, 56)
_GLOBAL = ('include', '<QtCore/6.12.0/QtCore/private/qglobal_p.h>', 2, 2)
_ALL = ('include', '<QtCore/QtCore>', 3, 3)
_CUTIE = ('include', '<QtCore/qcutie.h>', 5, 5)
_CONFIG = ('include', '<QtCore/qtcore-config.h>', 6, 6)

#  A Cute class holding two comments that come before no function: one
#  before a block with no name, one before a line and no end.
_ODD = (
  'class CuteQOdd : public QOdd {',  # 1
  'public:',  # 2
  '  //  a block with no name',  # 3
  '  {',  # 4
  '  }',  # 5
  '',  # 6
  '  //  a note, and no function after it',  # 7
  '  int field = 0;',  # 8
  '};',  # 9
)

#  A ritual file with no Cute class.
_PLAIN = (
  '#include <QtCore/QtCore>',
  '',
  'extern "C" Q_DECL_EXPORT',
  'void ritual_ZN6QCutie5clearEv(QCutie *self) {',
  '  self->clear();',
  '}',
)


class TestOccultExorcist(BaseTest):
  """
  Tests 'Exorcist': reading what 'clang++' and each of the linkers say,
  reading a ritual file into its items, finding the item an error is
  blamed on, dropping it, and the copy and the record without it.

  What to know before adding a test
  ---------------------------------

  - The ritual file is made up ('_LINES'), written to a temporary
    folder for each test, so every line number is known; the items it
    holds are the names starting with an underscore above the class.
  - What the compiler and the linkers say is quoted in the shape each
    of them says it, on Linux, macOS and Windows alike.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _write(self, lines: Tuple[str, ...], name: str = 'q_cutie.cpp') -> str:
    """Writes the lines as a ritual file and gives its path."""
    folder = tempfile.mkdtemp()
    self.addCleanup(shutil.rmtree, folder)
    path = os.path.join(folder, name)
    with open(path, 'w', encoding='utf-8') as file:
      file.write('\n'.join(lines))
    return path

  def _exorcist(self, lines: Tuple[str, ...] = _LINES) -> Exorcist:
    """An 'Exorcist' reading the lines, as a ritual file."""
    exorcist = Exorcist()
    exorcist.setRitualFile(self._write(lines))
    return exorcist

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMES AND KEPT LINES   # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_base_name_of_a_path(self) -> None:
    """The last part of a path, at '/' and '\\' alike, spaces gone."""
    for path in ('/a/b/q_cutie.o', 'D:\\a\\b\\q_cutie.o',
                 ' D:\\\\a\\\\q_cutie.o ', 'q_cutie.o', 'a/b\\q_cutie.o'):
      with self.subTest(path=path):
        self.assertEqual(Exorcist._getBaseName(path), 'q_cutie.o')

  def test_lines_kept_when_their_item_goes(self) -> None:
    """Each line of an '#if' kept, and the lines of Qt's namespace."""
    for line in ('#if QT_CONFIG(cutie)', '#ifdef Q_OS_WIN', '#ifndef X',
                 '#elif defined(Y)', '#else', '#endif  // X',
                 '  #  if Z', 'QT_BEGIN_NAMESPACE', ' QT_END_NAMESPACE '):
      with self.subTest(line=line):
        self.assertIs(Exorcist._isKept(line), True)
    for line in ('#include <QtCore/QtCore>', '#define X 1', 'int x;', '',
                 '// #if not a line of the compiler', '#iff'):
      with self.subTest(line=line):
        self.assertIs(Exorcist._isKept(line), False)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT THE COMPILER SAID   # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_error_and_where_it_lies(self) -> None:
    """An error gives its path, its line and its text with the base
    name of the path; what is no message of clang is passed by."""
    said = '\n'.join((
        'clang++ -c q_cutie.cpp',
        '/work/q_cutie.cpp:50:10: error: no member named size',
        '   50 |   return self->size();',
        '1 error generated.',
    ))
    errors = Exorcist.readCompilerErrors(said)
    self.assertEqual(errors, [dict(
        path='/work/q_cutie.cpp', line=50,
        text='q_cutie.cpp:50:10: error: no member named size',
        included=[], notes=[], instantiated=False)])

  def test_a_fatal_error_is_an_error(self) -> None:
    """A fatal error is read as an error, its kind in its text."""
    errors = Exorcist.readCompilerErrors(
        'q_cutie.cpp:5:10: fatal error: qcutie.h file not found')
    self.assertEqual(
        errors[0]['text'],
        'q_cutie.cpp:5:10: fatal error: qcutie.h file not found')

  def test_the_files_an_error_is_included_from(self) -> None:
    """The 'In file included from' lines before an error are its, in
    order, ending in ':' or ','; they are not the next error's."""
    said = '\n'.join((
        'In file included from q_cutie.cpp:5,',
        'In file included from /qt/qcutie.h:3:',
        '/qt/qcutie_p.h:9:1: error: unknown type name Cutie',
        '/qt/qcutie_p.h:12:1: error: unknown type name Cuter',
    ))
    first, second = Exorcist.readCompilerErrors(said)
    self.assertEqual(first['included'],
                     [('q_cutie.cpp', 5), ('/qt/qcutie.h', 3)])
    self.assertEqual(second['included'], [])

  def test_the_notes_of_an_error(self) -> None:
    """The notes after an error are its; one of an instantiation marks
    the error as one of a template."""
    said = '\n'.join((
        '/qt/qlist.h:9:1: error: no matching function',
        'q_cutie.cpp:41:3: note: candidate here',
        '/qt/qlist.h:20:1: note: in instantiation of QList<Cutie>',
    ))
    error, = Exorcist.readCompilerErrors(said)
    self.assertEqual(error['notes'],
                     [('q_cutie.cpp', 41), ('/qt/qlist.h', 20)])
    self.assertIs(error['instantiated'], True)

  def test_each_word_of_an_instantiation(self) -> None:
    """'requested here', a substitution or a deduction mark it too."""
    for text in ('requested here', 'during template argument deduction',
                 'while substituting'):
      with self.subTest(text=text):
        said = 'a.h:1:1: error: e\nq_cutie.cpp:2:3: note: %s' % text
        self.assertIs(
            Exorcist.readCompilerErrors(said)[0]['instantiated'], True)

  def test_a_note_of_no_error_is_passed_by(self) -> None:
    """A note before any error, or after a warning, is no error's."""
    said = '\n'.join((
        'q_cutie.cpp:1:1: note: before anything',
        'q_cutie.cpp:2:1: warning: unused',
        'q_cutie.cpp:3:1: note: of the warning',
        'q_cutie.cpp:4:1: remark: said',
        'q_cutie.cpp:5:1: note: of the remark',
        'q_cutie.cpp:6:1: error: the one',
    ))
    error, = Exorcist.readCompilerErrors(said)
    self.assertEqual(error['line'], 6)
    self.assertEqual(error['notes'], [])

  def test_nothing_said_is_no_error(self) -> None:
    """Nothing said, or only other lines: no errors."""
    self.assertEqual(Exorcist.readCompilerErrors(''), [])
    self.assertEqual(Exorcist.readCompilerErrors('all fine\n'), [])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT A LINKER SAID   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_gnu_ld(self) -> None:
    """GNU ld: a function needing a symbol, data needing one, and one
    defined twice, each with its object file."""
    said = '\n'.join((
        "/usr/bin/ld: q_cutie.o: in function `ritual_ZN6QCutie5clearEv':",
        "q_cutie.cpp:(.text+0x1a): undefined reference to `QCutie::clear()'",
        '/usr/bin/ld: q_cutie.o:(.data.rel.ro+0x10): undefined reference '
        "to `vtable for QCutie'",
        "/usr/bin/ld: q_other.o: in function `CutieHelper::help()':",
        "q_other.cpp:(.text+0x5): multiple definition of "
        "`CutieHelper::help()'; q_cutie.o:q_cutie.cpp:(.text+0x0): first "
        'defined here',
    ))
    self.assertEqual(Exorcist.readLinkerRefusal(said), [
        ('q_cutie.o', ('ritual_ZN6QCutie5clearEv', 'QCutie::clear()',
                       'undefined')),
        ('q_cutie.o', ('.data.rel.ro+0x10', 'vtable for QCutie',
                       'undefined')),
        ('q_other.o', ('CutieHelper::help()', 'CutieHelper::help()',
                       'duplicate')),
    ])

  def test_gnu_ld_with_no_function_named(self) -> None:
    """A symbol missed, or one defined twice, with no function named
    before it, is passed by."""
    said = '\n'.join((
        "q_cutie.cpp:(.text+0x1a): undefined reference to `QCutie::clear()'",
        "q_other.cpp:(.text+0x5): multiple definition of `X::y()'; here",
    ))
    self.assertEqual(Exorcist.readLinkerRefusal(said), [])

  def test_ld_lld(self) -> None:
    """ld.lld: a symbol missed, and where; the line of the source is
    passed by."""
    said = '\n'.join((
        'ld.lld: error: undefined symbol: QCutie::clear()',
        '>>> referenced by q_cutie.cpp:54',
        '>>>               q_cutie.o:(ritual_ZN6QCutie5clearEv)',
    ))
    self.assertEqual(Exorcist.readLinkerRefusal(said), [(
        'q_cutie.o', ('ritual_ZN6QCutie5clearEv', 'QCutie::clear()',
                      'undefined'))])

  def test_ld_lld_duplicate(self) -> None:
    """ld.lld: a symbol defined twice gives the first object file only."""
    said = '\n'.join((
        'ld64.lld: error: duplicate symbol: CutieHelper::help()',
        '>>> defined at q_cutie.cpp:16',
        '>>>            q_cutie.o:(CutieHelper::help())',
        '>>> defined at q_other.cpp:3',
        '>>>            q_other.o:(.text+0x0)',
    ))
    self.assertEqual(Exorcist.readLinkerRefusal(said), [(
        'q_cutie.o', ('CutieHelper::help()', 'CutieHelper::help()',
                      'duplicate'))])

  def test_lld_link(self) -> None:
    """lld-link names the object file alone, its backslashes doubled."""
    said = '\n'.join((
        'lld-link.exe: error: undefined symbol: public: void __cdecl '
        'QCutie::clear(void)',
        '>>> referenced by D:\\\\a\\\\cutie\\\\q_cutie.o',
        '>>> referenced by D:\\a\\cutie\\q_other.obj',
    ))
    self.assertEqual(Exorcist.readLinkerRefusal(said), [
        ('q_cutie.o', (None, 'public: void __cdecl QCutie::clear(void)',
                       'undefined')),
        ('q_other.obj', (None, 'public: void __cdecl QCutie::clear(void)',
                         'undefined')),
    ])

  def test_a_place_of_lld_before_any_symbol(self) -> None:
    """A '>>>' line before any symbol is passed by."""
    self.assertEqual(
        Exorcist.readLinkerRefusal('>>> referenced by q_cutie.o'), [])

  def test_apple_ld(self) -> None:
    """Apple's ld, in its old and its new words: each symbol, quoted or
    not, and what it is referenced from."""
    for head in ('Undefined symbols for architecture arm64:',
                 'ld: Undefined symbols:'):
      with self.subTest(head=head):
        said = '\n'.join((
            head,
            '  "QCutie::clear()", referenced from:',
            '      _ritual_ZN6QCutie5clearEv in q_cutie.o',
            '  QCutie::size() const, referenced from:',
            '      ritual_ZNK6QCutie4sizeEv in q_other.o',
            'ld: symbol(s) not found for architecture arm64',
        ))
        self.assertEqual(Exorcist.readLinkerRefusal(said), [
            ('q_cutie.o', ('_ritual_ZN6QCutie5clearEv', 'QCutie::clear()',
                           'undefined')),
            ('q_other.o', ('ritual_ZNK6QCutie4sizeEv',
                           'QCutie::size() const', 'undefined')),
        ])

  def test_apple_ld_duplicate(self) -> None:
    """Apple's ld: a symbol defined twice gives the first object file;
    a line of a referrer, or a second object file, is passed by."""
    said = '\n'.join((
        "duplicate symbol 'CutieHelper::help()' in:",
        '    ritual_a in q_cutie.o',
        '    q_cutie.o',
        '    q_other.o',
        'ld: 1 duplicate symbols',
    ))
    self.assertEqual(Exorcist.readLinkerRefusal(said), [(
        'q_cutie.o', (None, 'CutieHelper::help()', 'duplicate'))])

  def test_microsoft_link(self) -> None:
    """Microsoft's link.exe: a symbol missed in a function, one missed
    with none named, and one defined twice."""
    said = '\n'.join((
        'q_cutie.obj : error LNK2019: unresolved external symbol "public: '
        'void __cdecl QCutie::clear(void)" (?clear@QCutie@@QEAAXXZ) '
        'referenced in function ritual_ZN6QCutie5clearEv',
        'q_cutie.obj : error LNK2001: unresolved external symbol "const '
        "QCutie::`vftable'\" (??_7QCutie@@6B@)",
        'q_other.obj : error LNK2005: "public: int __cdecl '
        'CutieHelper::help(void)" (?help@CutieHelper@@QEAAHXZ) already '
        'defined in q_cutie.obj',
    ))
    self.assertEqual(Exorcist.readLinkerRefusal(said), [
        ('q_cutie.obj', (
            'ritual_ZN6QCutie5clearEv',
            '"public: void __cdecl QCutie::clear(void)" '
            '(?clear@QCutie@@QEAAXXZ)', 'undefined')),
        ('q_cutie.obj', (
            None, "\"const QCutie::`vftable'\" (??_7QCutie@@6B@)",
            'undefined')),
        ('q_other.obj', (
            None, '"public: int __cdecl CutieHelper::help(void)" '
            '(?help@CutieHelper@@QEAAHXZ)', 'duplicate')),
    ])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  QUALIFIED NAMES  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_qualified_name_of_what_a_linker_says(self) -> None:
    """The qualified name of a function or a class, from its stored
    spelling or its readable one, quoted or not, a thunk or not."""
    for said, name in (
        ('_ZN6QCutie5clearEv', 'QCutie::clear'),
        ('__ZNK6QCutie4sizeEv', 'QCutie::size'),
        ('_Z10cutieOtheri', 'cutieOther'),
        ('"QCutie::clear()"', 'QCutie::clear'),
        ('QCutie::clear()', 'QCutie::clear'),
        ('non-virtual thunk to QCutie::event(QEvent*)', 'QCutie::event'),
        ('virtual thunk to QCutie::grow()', 'QCutie::grow'),
        ('covariant return thunk to QCutie::copy()', 'QCutie::copy'),
        ('QList<int>::append(int const&)', 'QList<int>::append'),
        ('public: void __cdecl QCutie::clear(void)', 'QCutie::clear'),
        ('QWidget* QCutie::make()', 'QCutie::make'),
        ('vtable for QCutie', 'QCutie'),
    ):
      with self.subTest(said=said):
        self.assertEqual(Exorcist._readQualifiedName(said), name)

  def test_no_qualified_name(self) -> None:
    """Nothing, or a call with no name before it, gives none."""
    for said in ('', '   ', '(int)'):
      with self.subTest(said=said):
        self.assertIsNone(Exorcist._readQualifiedName(said))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE RITUAL FILE  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_nothing_is_read_before_a_file_is_named(self) -> None:
    """Before 'setRitualFile', asking for the file or its items raises."""
    exorcist = Exorcist()
    for ask in (exorcist.getRitualFile, exorcist.getItems,
                lambda: exorcist.getItemAt(1)):
      with self.subTest(ask=ask):
        with self.assertRaises(MissingVariable):
          ask()
    self.assertEqual(exorcist.getDropped(), {})
    self.assertIsNone(exorcist.getWholeReason())

  def test_a_ritual_file_must_be_a_path_to_a_file(self) -> None:
    """A path that is no 'str' is refused, as is one where no file is."""
    exorcist = Exorcist()
    with self.assertRaises(TypeException):
      exorcist.setRitualFile(b'/no/such.cpp')
    with self.assertRaises(FileNotFoundError) as caught:
      exorcist.setRitualFile('/no/such/q_cutie.cpp')
    self.assertIn("'/no/such/q_cutie.cpp'", str(caught.exception))

  def test_the_items_of_the_file(self) -> None:
    """Every item of the file, in the order they begin; the pieces that
    are no item are passed by."""
    exorcist = self._exorcist()
    self.assertEqual(exorcist.getItems(), (
        _GLOBAL, _ALL, _CUTIE, _CONFIG, _HELPER, _OTHER, _TYPEDEF, _CUTE,
        _SIZE, _EQUAL, _RITUAL_SIZE, _RITUAL_CLEAR,
    ))

  def test_comments_before_no_function_are_passed_by(self) -> None:
    """A comment in a Cute class before no function makes no item."""
    exorcist = self._exorcist(_ODD)
    self.assertEqual(
        exorcist.getItems(), (('cute class', 'CuteQOdd', 1, 9),))

  def test_the_item_of_a_line(self) -> None:
    """The innermost item a line is in, or None where it is in none."""
    exorcist = self._exorcist()
    for line, item in (
        (2, _GLOBAL), (14, _HELPER), (20, _HELPER), (24, _OTHER),
        (30, _TYPEDEF), (33, _CUTE), (36, _SIZE), (41, _EQUAL),
        (46, _RITUAL_SIZE), (50, _RITUAL_SIZE), (55, _RITUAL_CLEAR),
        (1, None), (7, None), (59, None), (0, None), (-3, None),
        (len(_LINES) + 1, None), (10000, None),
    ):
      with self.subTest(line=line):
        self.assertEqual(exorcist.getItemAt(line), item)

  def test_a_file_read_again_starts_over(self) -> None:
    """Naming a file again forgets what was dropped of the one before."""
    exorcist = self._exorcist()
    exorcist.drop(_RITUAL_SIZE, 'refused')
    exorcist.dropWhole('all of it')
    exorcist.setRitualFile(self._write(_PLAIN))
    self.assertEqual(exorcist.getDropped(), {})
    self.assertIsNone(exorcist.getWholeReason())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DROPPING   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_item_dropped_once(self) -> None:
    """An item is dropped once: 'drop' says so the first time only."""
    exorcist = self._exorcist()
    self.assertIs(exorcist.drop(_RITUAL_SIZE, 'refused'), True)
    self.assertIs(exorcist.drop(_RITUAL_SIZE, 'again'), False)
    self.assertEqual(exorcist.getDropped(), {_RITUAL_SIZE: 'refused'})

  def test_an_item_in_a_dropped_one_is_dropped(self) -> None:
    """An item inside one dropped is dropped with it."""
    exorcist = self._exorcist()
    exorcist.drop(_CUTE, 'refused')
    self.assertIs(exorcist.drop(_SIZE, 'too'), False)
    self.assertEqual(exorcist.getDropped(), {_CUTE: 'refused'})

  def test_what_is_no_item_is_refused(self) -> None:
    """Dropping what is no item of the file raises, naming it."""
    exorcist = self._exorcist()
    with self.assertRaises(ValueError) as caught:
      exorcist.drop(('ritual', 'ritual_gone', 1, 2), 'refused')
    self.assertIn("'ritual_gone'", str(caught.exception))

  def test_the_rituals_left_out(self) -> None:
    """Each ritual dropped, with the function its comment names, or its
    own name without one; other items dropped are no ritual."""
    exorcist = self._exorcist()
    exorcist.drop(_RITUAL_SIZE, 'one')
    exorcist.drop(_RITUAL_CLEAR, 'two')
    exorcist.drop(_HELPER, 'three')
    self.assertEqual(exorcist.getLeftOut(), {
        'ritual_ZNK6QCutie4sizeEv': ('int QCutie::size() const', 'one'),
        'ritual_ZN6QCutie5clearEv': ('ritual_ZN6QCutie5clearEv', 'two'),
    })

  def test_the_whole_file_dropped(self) -> None:
    """A file dropped whole leaves out every ritual for that reason, and
    every item counts as dropped."""
    exorcist = self._exorcist()
    exorcist.dropWhole('the linker refused it all')
    self.assertEqual(exorcist.getWholeReason(), 'the linker refused it all')
    self.assertEqual(exorcist.getLeftOut(), {
        'ritual_ZNK6QCutie4sizeEv': (
            'int QCutie::size() const', 'the linker refused it all'),
        'ritual_ZN6QCutie5clearEv': (
            'ritual_ZN6QCutie5clearEv', 'the linker refused it all'),
    })
    self.assertIs(exorcist.drop(_TYPEDEF, 'too'), False)
    self.assertEqual(exorcist.getCandidates(wide=True), ())

  def test_dropping_whole_needs_a_file(self) -> None:
    """Dropping the whole of no file raises."""
    with self.assertRaises(MissingVariable):
      Exorcist().dropWhole('nothing')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE COPY   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_copy_of_a_file_with_nothing_dropped(self) -> None:
    """With nothing dropped the copy is the file."""
    self.assertEqual(self._exorcist().getCopyText(), '\n'.join(_LINES))

  def test_the_copy_without_what_is_dropped(self) -> None:
    """The lines of each item dropped, and of each one tried, are empty;
    the lines of an '#if' and of Qt's namespace stay; every other line
    stays where it was."""
    exorcist = self._exorcist()
    exorcist.drop(_HELPER, 'refused')
    lines = exorcist.getCopyText(_RITUAL_CLEAR).split('\n')
    self.assertEqual(len(lines), len(_LINES))
    for number in range(1, len(_LINES) + 1):
      with self.subTest(line=number):
        if number in (11, 20) or not (
            10 <= number <= 21 or 53 <= number <= 56):
          self.assertEqual(lines[number - 1], _LINES[number - 1])
        else:
          self.assertEqual(lines[number - 1], '')

  def test_the_copy_keeps_an_if_inside_an_item(self) -> None:
    """A line of an '#if' inside an item dropped stays."""
    lines = (*_PLAIN[:3], '#if QT_CONFIG(cutie)', *_PLAIN[3:5], '#endif',
             _PLAIN[5])
    exorcist = self._exorcist(lines)
    ritual, = (i for i in exorcist.getItems() if i[0] == 'ritual')
    exorcist.drop(ritual, 'refused')
    copy = exorcist.getCopyText().split('\n')
    self.assertEqual(copy[3], '#if QT_CONFIG(cutie)')
    self.assertEqual(copy[6], '#endif')
    self.assertEqual(copy[4], '')

  def test_the_copy_of_a_file_dropped_whole(self) -> None:
    """A file dropped whole gives empty lines, as many as it has."""
    exorcist = self._exorcist()
    exorcist.dropWhole('all of it')
    self.assertEqual(exorcist.getCopyText(), '\n' * (len(_LINES) - 1))

  def test_the_candidates_of_a_trial(self) -> None:
    """A trial tries the rituals and the Cute functions first; widened,
    the Cute class, the copied code and the includes too, but never an
    include that is fixed, nor what is dropped."""
    exorcist = self._exorcist()
    exorcist.drop(_RITUAL_CLEAR, 'refused')
    self.assertEqual(exorcist.getCandidates(), (_RITUAL_SIZE, _SIZE, _EQUAL))
    self.assertEqual(exorcist.getCandidates(wide=True), (
        _RITUAL_SIZE, _SIZE, _EQUAL, _CUTE, _HELPER, _OTHER, _CUTIE))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE RECORD   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_record_and_back(self) -> None:
    """The record says what was dropped in plain lists, and another
    'Exorcist' of the same file takes it back as it was."""
    exorcist = self._exorcist()
    exorcist.drop(_RITUAL_SIZE, 'one')
    exorcist.drop(_HELPER, 'two')
    record = exorcist.getRecord()
    self.assertEqual(record, dict(
        dropped=[[*_RITUAL_SIZE, 'one'], [*_HELPER, 'two']],
        whole=None,
        leftOut={'ritual_ZNK6QCutie4sizeEv': [
            'int QCutie::size() const', 'one']},
    ))
    again = Exorcist()
    again.setRitualFile(exorcist.getRitualFile())
    again.setRecord(record)
    self.assertEqual(again.getDropped(), exorcist.getDropped())
    self.assertEqual(again.getRecord(), record)

  def test_the_record_of_a_file_dropped_whole(self) -> None:
    """The record of a file dropped whole says why, and is taken back."""
    exorcist = self._exorcist()
    exorcist.dropWhole('all of it')
    again = self._exorcist()
    again.setRecord(exorcist.getRecord())
    self.assertEqual(again.getWholeReason(), 'all of it')

  def test_an_empty_record(self) -> None:
    """A record that says nothing drops nothing."""
    exorcist = self._exorcist()
    exorcist.setRecord(dict())
    self.assertEqual(exorcist.getDropped(), {})
    self.assertIsNone(exorcist.getWholeReason())

  def test_a_record_of_another_file_is_refused(self) -> None:
    """A record dropping what the file does not hold raises, naming it."""
    exorcist = self._exorcist()
    with self.assertRaises(ValueError) as caught:
      exorcist.setRecord(
          dict(dropped=[['ritual', 'ritual_gone', 3, 4, 'x']]))
    self.assertIn("'ritual_gone' of lines 3 to 4", str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  BLAMING THE COMPILER   # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_line_of_the_compiled_file(self) -> None:
    """An error lies where it says when that is the compiled file, else
    at its note in it, else, unless of a template, at its include; else
    nowhere."""
    exorcist = self._exorcist()
    compiled = 'q_cutie.exorcised.cpp'
    for error, line in (
        (dict(path='/w/q_cutie.exorcised.cpp', line=50, notes=[],
              included=[]), 50),
        (dict(path='/qt/a.h', line=9, notes=[('/w/x.cpp', 1),
              ('/w/q_cutie.exorcised.cpp', 41)], included=[]), 41),
        (dict(path='/qt/a.h', line=9, notes=[], instantiated=True,
              included=[('q_cutie.exorcised.cpp', 5)]), 0),
        (dict(path='/qt/a.h', line=9, notes=[], instantiated=False,
              included=[('/qt/b.h', 2), ('q_cutie.exorcised.cpp', 5)]), 5),
        (dict(path='/qt/a.h', line=9, notes=[], included=[]), 0),
    ):
      with self.subTest(error=error):
        self.assertEqual(exorcist._findLine(error, compiled), line)

  def test_the_items_errors_are_blamed_on(self) -> None:
    """Each item an error points at, once, with the error's words and
    the ritual file's name; an error at no item, or at a fixed include,
    is unblamed; one at an item dropped or tried is passed by."""
    exorcist = self._exorcist()
    exorcist.drop(_RITUAL_CLEAR, 'refused')
    compiled = '/w/q_cutie.exorcised.cpp'
    said = '\n'.join((
        '/w/q_cutie.exorcised.cpp:50:3: error: no size',
        '/w/q_cutie.exorcised.cpp:49:3: error: no size again',
        '/w/q_cutie.exorcised.cpp:1:1: error: at no item',
        'In file included from /w/q_cutie.exorcised.cpp:2:',
        '/qt/qglobal_p.h:3:1: error: in a fixed include',
        'In file included from /w/q_cutie.exorcised.cpp:5:',
        '/qt/qcutie.h:3:1: error: in an include',
        '/w/q_cutie.exorcised.cpp:55:3: error: in a dropped ritual',
        '/w/q_cutie.exorcised.cpp:41:3: error: in a tried one',
    ))
    blamed, unblamed = exorcist.readBlame(said, compiled, _EQUAL)
    self.assertEqual(blamed, [
        (_RITUAL_SIZE, 'the compiler refused it on this machine: '
                       'q_cutie.cpp:50:3: error: no size'),
        (_CUTIE, 'the compiler refused it on this machine: '
                 'qcutie.h:3:1: error: in an include'),
    ])
    self.assertEqual(unblamed, [
        'q_cutie.cpp:1:1: error: at no item',
        'qglobal_p.h:3:1: error: in a fixed include',
    ])

  def test_blaming_the_compiler_drops_the_items(self) -> None:
    """Each item blamed is dropped; it says whether one was."""
    exorcist = self._exorcist()
    said = '/w/q_cutie.cpp:50:3: error: no size'
    self.assertIs(exorcist.blameCompiler(said, '/w/q_cutie.cpp'), True)
    self.assertEqual(exorcist.getDropped(), {
        _RITUAL_SIZE: 'the compiler refused it on this machine: '
                      'q_cutie.cpp:50:3: error: no size'})
    self.assertIs(exorcist.blameCompiler(said, '/w/q_cutie.cpp'), False)
    self.assertIs(exorcist.blameCompiler('', '/w/q_cutie.cpp'), False)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  FINDING WHAT DEFINES A NAME  # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_item_of_a_class(self) -> None:
    """The Cute class by its name; a class or struct of copied code; or
    none."""
    exorcist = self._exorcist()
    for name, item in (
        ('CuteQCutie', _CUTE), ('ns::CuteQCutie', _CUTE),
        ('CutieHelper', _HELPER), ('CutieOther', _OTHER),
        ('QCutie', None), ('Cutie', None),
    ):
      with self.subTest(name=name):
        self.assertEqual(exorcist._findClass(name), item)

  def test_the_item_of_a_function(self) -> None:
    """A function of the Cute class, or the class; a function of copied
    code; the class of a function not found; or none."""
    exorcist = self._exorcist()
    for name, item in (
        ('CuteQCutie::size', _SIZE),
        ('CuteQCutie::operator==', _EQUAL),
        ('CuteQCutie::gone', _CUTE),
        ('CutieHelper::help', _HELPER),
        ('cutieOther', _OTHER),
        ('CutieHelper::unknown', _HELPER),
        ('Nobody::gone', None),
        ('gone', None),
        ('elper::help', None),
    ):
      with self.subTest(name=name):
        self.assertEqual(exorcist._findDefinition(name), item)

  def test_the_item_a_linker_names(self) -> None:
    """A ritual by its name, a class by its table, copied code by its
    stored name, or a function by its qualified name."""
    exorcist = self._exorcist()
    for referrer, item in (
        ('ritual_ZNK6QCutie4sizeEv', _RITUAL_SIZE),
        ('_ritual_ZNK6QCutie4sizeEv', _RITUAL_SIZE),
        ('"ritual_ZN6QCutie5clearEv"', _RITUAL_CLEAR),
        ('ritual_gone', None),
        ('vtable for CuteQCutie', _CUTE),
        ('typeinfo for CutieHelper', _HELPER),
        ('typeinfo name for CutieOther', _OTHER),
        ('VTT for CuteQCutie', _CUTE),
        ("CutieHelper::`vftable'", _HELPER),
        ('_ZTV10CuteQCutie', _CUTE),
        ('.text._ZTI11CutieHelper', _HELPER),
        ('__ZTS10CutieOther', _OTHER),
        ('_ZN11CutieHelper4helpEv', _HELPER),
        ('_ZN6QCutie4sizeEv', None),
        ('CutieHelper::help()', _HELPER),
        ('(void)', None),
    ):
      with self.subTest(referrer=referrer):
        self.assertEqual(exorcist._findReferrer(referrer), item)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  BLAMING THE LINKER   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_blaming_the_linker(self) -> None:
    """A symbol defined twice drops what defines it; one missed drops
    what needs it, or the Cute class when nothing is named; what is
    found nowhere is passed by."""
    exorcist = self._exorcist()
    found = exorcist.blameLinker([
        (None, 'CutieHelper::help()', 'duplicate'),
        ('ritual_ZN6QCutie5clearEv', 'QCutie::clear()', 'undefined'),
        (None, 'vtable for QCutie', 'undefined'),
        ('ritual_gone', 'QCutie::gone()', 'undefined'),
    ])
    self.assertIs(found, True)
    self.assertEqual(exorcist.getDropped(), {
        _HELPER: "the linker refused it on this machine: "
                 "'CutieHelper::help()' is defined by another ritual "
                 "file too",
        _RITUAL_CLEAR: "the linker refused it on this machine: it needs "
                       "'QCutie::clear()', which no library of Qt here "
                       "offers",
        _CUTE: "the linker refused it on this machine: it needs 'vtable "
               "for QCutie', which no library of Qt here offers",
    })

  def test_blaming_the_linker_again_drops_nothing(self) -> None:
    """What is dropped already, or found nowhere, drops nothing."""
    exorcist = self._exorcist()
    blames = [('ritual_ZN6QCutie5clearEv', 'QCutie::clear()', 'undefined')]
    self.assertIs(exorcist.blameLinker(blames), True)
    self.assertIs(exorcist.blameLinker(blames), False)
    self.assertIs(exorcist.blameLinker([
        ('ritual_gone', 'x', 'undefined')]), False)
    self.assertIs(exorcist.blameLinker([]), False)

  def test_a_symbol_of_no_one_in_a_file_with_no_cute_class(self) -> None:
    """With nothing named and no Cute class, nothing is dropped."""
    exorcist = self._exorcist(_PLAIN)
    self.assertIs(exorcist.blameLinker([
        (None, 'vtable for QCutie', 'undefined')]), False)
    self.assertEqual(exorcist.getDropped(), {})
