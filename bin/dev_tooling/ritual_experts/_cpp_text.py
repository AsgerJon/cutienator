"""CppText takes apart and puts together types as C++ writes them."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import List, Tuple


class CppText:
  """
  Takes apart and puts together types as C++ writes them. It holds no
  state: every function of it is static, and the generator and each of
  its experts use them alike.

    CppText.splitFunctionType('QObject *() const')
    # ('QObject *', '', ['const'])
    CppText.joinType('QObject *', 'parent')    # 'QObject *parent'
    CppText.stripReadOnly('const int &')       # 'int'
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def splitFunctionType(functionType: str) -> Tuple[str, str, List[str]]:
    """
    Takes apart the type the compiler writes for a function.

    Parameters
    ----------

    functionType : str
      As 'QObject *() const': what it gives, what it takes between
      brackets, and then words such as 'const'.

    Returns
    -------

    Tuple[str, str, List[str]]
      What the function gives, as 'QObject *'; what stands between the
      brackets; and the words after them.

    Raises
    ------

    ValueError
      The text has no pair of brackets holding what the function takes.
    """
    #  The compiler may write 'noexcept(true)' where the header says
    #  'noexcept' with a condition. It is the word 'noexcept' here.
    marker = functionType.rfind(' noexcept(')
    if marker >= 0 and functionType.endswith(')'):
      inside = functionType[marker + len(' noexcept('):-1]
      if inside.count('(') == inside.count(')'):
        functionType = '%s noexcept' % functionType[:marker]
    close = functionType.rfind(')')
    depth, start = 0, -1
    for index in range(close, -1, -1):
      if functionType[index] == ')':
        depth += 1
      elif functionType[index] == '(':
        depth -= 1
        if depth == 0:
          start = index
          break
    if close < 0 or start < 0:
      infoSpec = """Expected the type of a function, as 'int (int)', but
      received '%s'."""
      raise ValueError(' '.join((infoSpec % functionType).split()))
    given = functionType[:start].strip()
    taken = functionType[start + 1:close]
    return given, taken, functionType[close + 1:].split()

  @staticmethod
  def joinType(cppType: str, name: str) -> str:
    """Writes a type and a name the way C++ does, as 'QObject *parent'."""
    if not name:
      return cppType
    if cppType.endswith(('*', '&')):
      return '%s%s' % (cppType, name)
    return '%s %s' % (cppType, name)

  @staticmethod
  def stripReadOnly(cppType: str) -> str:
    """Gives 'int' for 'int', 'const int' and 'const int &'."""
    if cppType.startswith('const '):
      cppType = cppType[6:]
      if cppType.endswith(' &'):
        cppType = cppType[:-2]
    return cppType
