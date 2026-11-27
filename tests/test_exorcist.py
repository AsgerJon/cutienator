"""
TestExorcist tests that 'Exorcist' reads a ritual file into its items,
blames on them what a compiler or a linker said, and gives the copy
without what it dropped. Nothing is compiled here: what the compiler and
the linkers say is written out as each of them writes it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import shutil
import tempfile

from worktoy.work_test import BaseTest

from cutienator.occult import Exorcist

RITUAL_TEXT = """//  Written by dev_tooling.RitualGenerator from the records
//  of
//  QtCore/qmadeup.h, Qt 6.12.0.
#include <QtCore/qglobal.h>
#if QT_CONFIG(madeup)
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmadeup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  'inline' put before it where Qt did not write it.

//  from src/corelib/qmadeup.cpp, line 12, as _ZN7QMadeUp6helperEv
inline int QMadeUp::helper()
{
    return 1;
}

//  from src/corelib/qmadeup.cpp, line 30, as local:qmadeup.cpp:QMadeUpData
QT_BEGIN_NAMESPACE
class QMadeUpData
{
public:
    int value = 0;
};
//  -----------------------------------------------------------------------

//  A QMadeUp that Python can take functions over in.
#if QT_CONFIG(madeup)
typedef int (*CuteQMadeUpCall0)(const void *, int *);
#endif  // QT_CONFIG(madeup)
class CuteQMadeUp : public QMadeUp {
public:
  using QMadeUp::QMadeUp;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    return false;
  }

#if QT_CONFIG(madeup)
  //  int QMadeUp::size() const
  int size() const override {
    return QMadeUp::size();
  }
#endif  // QT_CONFIG(madeup)
};

//  int QMadeUp::helper()
extern "C" Q_DECL_EXPORT
int ritual_ZN7QMadeUp6helperEv(QMadeUp *self) {
  return self->helper();
}

#if QT_CONFIG(madeup)
//  QMadeUp::QMadeUp()
extern "C" Q_DECL_EXPORT
QMadeUp *ritual_ZN7QMadeUpC1Ev() {
  return new CuteQMadeUp();
}
#endif  // QT_CONFIG(madeup)

#endif  // QT_CONFIG(madeup)
"""

HELPER = 'ritual_ZN7QMadeUp6helperEv'
CONSTRUCTOR = 'ritual_ZN7QMadeUpC1Ev'


class TestExorcist(BaseTest):
  """
  Tests 'Exorcist' on a ritual file made up for the tests, of the shape
  the generator writes: global includes, a condition, Qt's code, the
  Cute class and two rituals.
  """

  def setUp(self) -> None:
    """Writes the made-up ritual file into a folder of its own."""
    BaseTest.setUp(self)
    folder = tempfile.mkdtemp(prefix='cutienator-test-exorcist-')
    self.addCleanup(shutil.rmtree, folder, True)
    self.ritualFile = os.path.join(folder, 'q_made_up.cpp')
    with open(self.ritualFile, 'w') as file:
      file.write(RITUAL_TEXT)
    self.exorcist = Exorcist()
    self.exorcist.setRitualFile(self.ritualFile)

  @staticmethod
  def lineOf(text: str, nth: int = 1) -> int:
    """Gives the line of the made-up file that holds the text, counted
    from 1; the nth such line."""
    found = [at for at, line in enumerate(RITUAL_TEXT.split('\n'), 1)
             if text in line]
    return found[nth - 1]

  def item(self, kind: str, name: str) -> tuple:
    """Gives the one item of that kind whose name holds the name."""
    found = [i for i in self.exorcist.getItems()
             if i[0] == kind and name in i[1]]
    self.assertEqual(len(found), 1, (kind, name, found))
    return found[0]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ITEMS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_items_of_a_ritual_file(self) -> None:
    """Each kind of item is read where it is, with its name."""
    kinds = [item[0] for item in self.exorcist.getItems()]
    self.assertEqual(kinds.count('include'), 3)
    self.assertEqual(kinds.count('copied'), 2)
    self.assertEqual(kinds.count('ritual'), 2)
    self.assertEqual(kinds.count('typedef'), 1)
    self.assertEqual(kinds.count('cute class'), 1)
    self.assertEqual(kinds.count('cute function'), 1)
    ritual = self.item('ritual', HELPER)
    self.assertEqual(ritual[2], self.lineOf('//  int QMadeUp::helper()'))
    self.assertEqual(ritual[3], self.lineOf('  return self->helper();') + 1)
    cute = self.item('cute class', 'CuteQMadeUp')
    closing = [at for at, line in enumerate(RITUAL_TEXT.split('\n'), 1)
               if line == '};']
    self.assertEqual(cute[3], closing[1])
    self.assertEqual(self.item('cute function', 'size')[2],
                     self.lineOf('  //  int QMadeUp::size() const'))

  def test_a_line_is_in_its_innermost_item(self) -> None:
    """The body of a ritual is in the ritual, the body of Qt's code in
    that code, an override in its function of the Cute class."""
    at = self.exorcist.getItemAt
    self.assertEqual(at(self.lineOf('return self->helper();'))[1], HELPER)
    self.assertEqual(at(self.lineOf('    return 1;'))[0], 'copied')
    self.assertEqual(at(self.lineOf('return QMadeUp::size();'))[0],
                     'cute function')
    self.assertEqual(at(self.lineOf('using QMadeUp::QMadeUp;'))[0],
                     'cute class')
    self.assertIsNone(at(self.lineOf("//  Qt's own code")))
    self.assertIsNone(at(10000))

  def test_the_functions_the_rituals_call(self) -> None:
    """Each ritual left out is named by the function of its comment."""
    self.exorcist.dropWhole('made up')
    leftOut = self.exorcist.getLeftOut()
    self.assertEqual(leftOut[HELPER], ('int QMadeUp::helper()', 'made up'))
    self.assertEqual(leftOut[CONSTRUCTOR][0], 'QMadeUp::QMadeUp()')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE COPY   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_copy_keeps_lines_and_conditions(self) -> None:
    """A dropped item leaves empty lines, as many, and its conditions
    and Qt's namespace stay."""
    self.exorcist.drop(self.item('ritual', CONSTRUCTOR), 'made up')
    self.exorcist.drop(self.item('copied', 'QMadeUpData'), 'made up')
    copy = self.exorcist.getCopyText().split('\n')
    original = RITUAL_TEXT.split('\n')
    self.assertEqual(len(copy), len(original))
    self.assertNotIn('return new CuteQMadeUp();', copy)
    self.assertNotIn('class QMadeUpData', copy)
    self.assertIn('QT_BEGIN_NAMESPACE', copy)
    self.assertEqual(copy.count('#if QT_CONFIG(madeup)'),
                     original.count('#if QT_CONFIG(madeup)'))
    self.assertIn('  return self->helper();', copy)
    self.assertEqual(self.exorcist.getLeftOut(), {
        CONSTRUCTOR: ('QMadeUp::QMadeUp()', 'made up')})

  def test_the_whole_file_dropped_is_an_empty_copy(self) -> None:
    """Every line is empty, and every ritual is left out."""
    self.exorcist.dropWhole('made up')
    copy = self.exorcist.getCopyText()
    self.assertEqual(copy.strip(), '')
    self.assertEqual(copy.count('\n'), RITUAL_TEXT.count('\n'))
    self.assertEqual(set(self.exorcist.getLeftOut()), {HELPER, CONSTRUCTOR})

  def test_a_trial_drops_nothing(self) -> None:
    """The items of a trial are out of that copy only."""
    ritual = self.item('ritual', HELPER)
    self.assertNotIn('  return self->helper();',
                     self.exorcist.getCopyText(ritual).split('\n'))
    self.assertEqual(self.exorcist.getDropped(), {})

  def test_the_candidates_of_a_trial(self) -> None:
    """Rituals and functions of the Cute class first; with 'wide' also
    the Cute class, Qt's code and the includes that may go."""
    narrow = self.exorcist.getCandidates()
    self.assertEqual({i[0] for i in narrow}, {'ritual', 'cute function'})
    wide = self.exorcist.getCandidates(True)
    self.assertEqual(wide[:len(narrow)], narrow)
    names = [i[1] for i in wide if i[0] == 'include']
    self.assertNotIn('<QtCore/qglobal.h>', names)
    self.assertIn('<QtCore/QtCore>', names)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE COMPILER   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_error_in_a_ritual_drops_the_ritual(self) -> None:
    """Only that ritual is left out, with what the compiler said."""
    said = "%s:%d:9: error: no member named 'helper' in 'QMadeUp'" % (
        self.ritualFile, self.lineOf('return self->helper();'))
    self.assertTrue(self.exorcist.blameCompiler(said, self.ritualFile))
    function, reason = self.exorcist.getLeftOut()[HELPER]
    self.assertIn("q_made_up.cpp:%d:9: error: no member named" % (
        self.lineOf('return self->helper();')), reason)
    self.assertEqual(list(self.exorcist.getLeftOut()), [HELPER])
    self.assertFalse(self.exorcist.blameCompiler(said, self.ritualFile))

  def test_an_error_in_the_copy_is_told_of_the_ritual_file(self) -> None:
    """The copy has the lines of the ritual file."""
    copyFile = '/elsewhere/q_made_up.exorcised.cpp'
    said = '%s:%d:9: error: oops' % (
        copyFile, self.lineOf('return self->helper();'))
    self.assertTrue(self.exorcist.blameCompiler(said, copyFile))
    reason = self.exorcist.getLeftOut()[HELPER][1]
    self.assertIn('q_made_up.cpp:', reason)
    self.assertNotIn('exorcised', reason)

  def test_an_error_on_windows_is_read(self) -> None:
    """A path with a drive and backslashes, as clang on Windows says."""
    said = r'D:\a\x\q_made_up.cpp:%d:3: error: oops' % (
        self.lineOf('return new CuteQMadeUp();'))
    self.assertTrue(self.exorcist.blameCompiler(said, self.ritualFile))
    self.assertEqual(list(self.exorcist.getLeftOut()), [CONSTRUCTOR])

  def test_an_error_in_a_header_drops_its_include(self) -> None:
    """Blamed on the '#include' line it came in by."""
    said = '\n'.join((
        'In file included from %s:%d:' % (
            self.ritualFile, self.lineOf('qmadeup_p.h')),
        '/kit/QtCore/private/qmadeup_p.h:3:1: error: unknown type name X',
    ))
    self.assertTrue(self.exorcist.blameCompiler(said, self.ritualFile))
    dropped = list(self.exorcist.getDropped())
    self.assertEqual(dropped, [self.item('include', 'qmadeup_p.h')])
    self.assertEqual(self.exorcist.getLeftOut(), {})

  def test_a_global_include_is_never_dropped(self) -> None:
    """An include before the first condition says what the conditions
    ask; an error blamed on it is blamed on no item."""
    said = '\n'.join((
        'In file included from %s:3:' % self.ritualFile,
        '/kit/QtCore/qglobal.h:9:1: error: broken',
    ))
    self.assertFalse(self.exorcist.blameCompiler(said, self.ritualFile))
    blamed, unblamed = self.exorcist.readBlame(said, self.ritualFile)
    self.assertEqual(blamed, [])
    self.assertEqual(len(unblamed), 1)

  def test_a_template_is_blamed_where_the_file_asked_for_it(self) -> None:
    """A note naming a line of the ritual file blames that line."""
    said = '\n'.join((
        'In file included from %s:5:' % self.ritualFile,
        '/kit/QtCore/qlist.h:80:7: error: incomplete type X',
        '/kit/QtCore/qlist.h:20:3: note: in instantiation of member '
        "function 'QList<X>::~QList' requested here",
        "%s:%d:10: note: in instantiation of member function 'f' "
        'requested here' % (
            self.ritualFile, self.lineOf('return new CuteQMadeUp();')),
    ))
    self.assertTrue(self.exorcist.blameCompiler(said, self.ritualFile))
    self.assertEqual(list(self.exorcist.getLeftOut()), [CONSTRUCTOR])

  def test_a_template_asked_for_unsaid_is_blamed_on_nothing(self) -> None:
    """A template worked out where clang names no line of the ritual
    file: its include is not to blame."""
    said = '\n'.join((
        'In file included from %s:5:' % self.ritualFile,
        '/kit/QtCore/qlist.h:80:7: error: incomplete type X',
        '/kit/QtCore/qlist.h:20:3: note: in instantiation of member '
        "function 'QList<X>::~QList' requested here",
    ))
    self.assertFalse(self.exorcist.blameCompiler(said, self.ritualFile))
    self.assertEqual(len(self.exorcist.readBlame(
        said, self.ritualFile)[1]), 1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE LINKERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_gnu_ld(self) -> None:
    """GNU's 'ld': the function, or the section of the data, and what
    it needs."""
    said = '\n'.join((
        '/usr/bin/ld: /tmp/demons/QtCoreDemons/q_made_up.o: in function '
        '`%s\':' % HELPER,
        "q_made_up.cpp:(.text+0x9): undefined reference to "
        "`QMadeUp::helper()'",
        '/usr/bin/ld: /tmp/demons/QtCoreDemons/q_made_up.o:(.data.rel.ro.'
        '_ZTV11CuteQMadeUp[_ZTV11CuteQMadeUp]+0x10): undefined reference '
        "to `QMadeUp::size() const'",
        'clang++: error: linker command failed with exit code 1',
    ))
    found = Exorcist.readLinkerRefusal(said)
    self.assertEqual([name for name, blame in found], ['q_made_up.o'] * 2)
    self.assertEqual(found[0][1], (HELPER, 'QMadeUp::helper()', 'undefined'))
    self.assertTrue(self.exorcist.blameLinker([b for n, b in found]))
    self.assertEqual(set(self.exorcist.getDropped()), {
        self.item('ritual', HELPER), self.item('cute class', 'CuteQMadeUp')})
    reason = self.exorcist.getLeftOut()[HELPER][1]
    self.assertIn('linker', reason)
    self.assertIn('QMadeUp::helper()', reason)

  def test_gnu_ld_names_a_function_of_qts_code(self) -> None:
    """A function of Qt's code, by its name or by its mangled name,
    is the piece of Qt's code that defines it."""
    for referrer in ('QMadeUp::helper()', '_ZN7QMadeUp6helperEv'):
      with self.subTest(referrer=referrer):
        exorcist = Exorcist()
        exorcist.setRitualFile(self.ritualFile)
        said = '\n'.join((
            '/usr/bin/ld: /x/q_made_up.o: in function `%s\':' % referrer,
            "q_made_up.cpp:(.text+0x9): undefined reference to `qGone()'",
        ))
        blames = [b for n, b in Exorcist.readLinkerRefusal(said)]
        self.assertTrue(exorcist.blameLinker(blames))
        self.assertEqual(list(exorcist.getDropped()), [
            [i for i in exorcist.getItems() if i[0] == 'copied'][0]])
        self.assertEqual(exorcist.getLeftOut(), {})

  def test_gnu_ld_twice(self) -> None:
    """A symbol two object files define: the item of this one."""
    said = ('/usr/bin/ld: /x/q_made_up.o: in function `QMadeUp::helper()\':'
            "\nq_made_up.cpp:(.text+0x0): multiple definition of "
            "`QMadeUp::helper()'; /x/q_other.o:q_other.cpp:(.text+0x0): "
            'first defined here')
    found = Exorcist.readLinkerRefusal(said)
    self.assertEqual(found, [('q_made_up.o', (
        'QMadeUp::helper()', 'QMadeUp::helper()', 'duplicate'))])
    self.assertTrue(self.exorcist.blameLinker([found[0][1]]))
    self.assertEqual(self.exorcist.getDropped().popitem()[0][0], 'copied')

  def test_lld(self) -> None:
    """LLVM's 'ld.lld' and 'lld-link'."""
    said = '\n'.join((
        'ld.lld: error: undefined symbol: QMadeUp::helper()',
        '>>> referenced by q_made_up.cpp',
        '>>>               /x/QtCoreDemons/q_made_up.o:(%s)' % HELPER,
        'lld-link: error: undefined symbol: int __cdecl qGone(void)',
        r'>>> referenced by D:\a\x\q_made_up.o:(%s)' % CONSTRUCTOR,
    ))
    found = Exorcist.readLinkerRefusal(said)
    self.assertEqual(found, [
        ('q_made_up.o', (HELPER, 'QMadeUp::helper()', 'undefined')),
        ('q_made_up.o', (CONSTRUCTOR, 'int __cdecl qGone(void)',
                         'undefined')),
    ])
    self.assertTrue(self.exorcist.blameLinker([b for n, b in found]))
    self.assertEqual(set(self.exorcist.getLeftOut()), {HELPER, CONSTRUCTOR})

  def test_lld_link_names_the_object_file_alone(self) -> None:
    """'lld-link' names an object file without debugging records alone,
    its path with each backslash doubled, as GitHub's Windows machine
    wrote it on 2026-11-27: what needs the symbol is then not said."""
    said = '\n'.join((
        'lld-link: error: undefined symbol: public: virtual __cdecl '
        'QMadeUp::~QMadeUp(void)',
        r'>>> referenced by D:\\a\\x\\QtCoreDemons\\q_made_up.o',
        'clang++: error: linker command failed with exit code 1',
    ))
    found = Exorcist.readLinkerRefusal(said)
    self.assertEqual(found, [
        ('q_made_up.o', (
            None, 'public: virtual __cdecl QMadeUp::~QMadeUp(void)',
            'undefined')),
    ])

  def test_apple_ld(self) -> None:
    """Apple's 'ld', with the names between quotes and without, the
    function a C name with its underscore."""
    for quote in ('"', ''):
      with self.subTest(quote=quote):
        said = '\n'.join((
            'Undefined symbols for architecture arm64:',
            '  %sQMadeUp::helper()%s, referenced from:' % (quote, quote),
            '      _%s in q_made_up.o' % HELPER,
            '      vtable for CuteQMadeUp in q_made_up.o',
            'ld: symbol(s) not found for architecture arm64',
        ))
        found = Exorcist.readLinkerRefusal(said)
        self.assertEqual(found, [
            ('q_made_up.o', ('_%s' % HELPER, 'QMadeUp::helper()',
                             'undefined')),
            ('q_made_up.o', ('vtable for CuteQMadeUp', 'QMadeUp::helper()',
                             'undefined')),
        ])
        exorcist = Exorcist()
        exorcist.setRitualFile(self.ritualFile)
        self.assertTrue(exorcist.blameLinker([b for n, b in found]))
        self.assertEqual({i[0] for i in exorcist.getDropped()},
                         {'ritual', 'cute class'})

  def test_msvc_link(self) -> None:
    """Microsoft's 'link.exe': the function where it names one, the
    Cute class where it does not."""
    said = '\n'.join((
        r'D:\a\x\q_made_up.o : error LNK2019: unresolved external symbol '
        '"public: int __cdecl QMadeUp::helper(void)" '
        '(?helper@QMadeUp@@QEAAHXZ) referenced in function %s' % HELPER,
        r'D:\a\x\q_made_up.o : error LNK2001: unresolved external symbol '
        '"public: virtual int __cdecl QMadeUp::size(void)const " '
        '(?size@QMadeUp@@UEBAHXZ)',
        'cutienator_QtCore.dll : fatal error LNK1120: 2 unresolved '
        'externals',
    ))
    found = Exorcist.readLinkerRefusal(said)
    self.assertEqual([n for n, b in found], ['q_made_up.o'] * 2)
    self.assertEqual(found[0][1][0], HELPER)
    self.assertIsNone(found[1][1][0])
    self.assertTrue(self.exorcist.blameLinker([b for n, b in found]))
    self.assertEqual({i[0] for i in self.exorcist.getDropped()},
                     {'ritual', 'cute class'})

  def test_msvc_names_a_function_of_the_cute_class(self) -> None:
    """The function of the Cute class a referrer of MSVC names."""
    referrer = ('"public: virtual int __cdecl CuteQMadeUp::size(void)'
                'const " (?size@CuteQMadeUp@@UEBAHXZ)')
    blames = [(referrer, 'x', 'undefined')]
    self.assertTrue(self.exorcist.blameLinker(blames))
    self.assertEqual(list(self.exorcist.getDropped()), [
        self.item('cute function', 'size')])

  def test_a_linker_naming_nothing_of_the_file(self) -> None:
    """Nothing is dropped for what no item holds."""
    self.assertFalse(self.exorcist.blameLinker([
        ('somethingElse()', 'qGone()', 'undefined')]))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE RECORD   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_record_is_taken_back(self) -> None:
    """What was dropped is dropped again from the record, as JSON."""
    self.exorcist.drop(self.item('ritual', HELPER), 'made up')
    record = self.exorcist.getRecord()
    other = Exorcist()
    other.setRitualFile(self.ritualFile)
    other.setRecord(record)
    self.assertEqual(other.getDropped(), self.exorcist.getDropped())
    self.assertEqual(other.getCopyText(), self.exorcist.getCopyText())
    self.assertEqual(record['leftOut'], {
        HELPER: ['int QMadeUp::helper()', 'made up']})

  def test_a_record_of_another_file_is_refused(self) -> None:
    """An item the file does not hold as it is now."""
    record = dict(dropped=[['ritual', 'ritual_gone', 3, 4, 'x']], whole=None)
    with self.assertRaises(ValueError):
      self.exorcist.setRecord(record)

  def test_a_ritual_file_must_be_there(self) -> None:
    """No file, no Exorcist."""
    with self.assertRaises(FileNotFoundError):
      Exorcist().setRitualFile(self.ritualFile + '.gone')
