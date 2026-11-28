"""
qfloat16 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qfloat16.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Qt


class qfloat16(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qfloat16: a plain Python object standing in front of
  one C++ qfloat16.

  C++ hands a qfloat16 around as a copy, so every C++ qfloat16 behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's qfloat16 that has a ritual and that Python can call
  so far, 30 names in all: 'isInf', 'isNaN', 'isFinite', 'fpClassify',
  'copySign', '_limit_epsilon', '_limit_min', '_limit_denorm_min',
  '_limit_max', '_limit_lowest', '_limit_infinity', '_limit_quiet_NaN',
  '_limit_signaling_NaN', 'isNormal', '__pos__', '__neg__', '__add__',
  '__sub__', '__mul__', '__truediv__', '__radd__', '__rsub__', '__rmul__',
  '__rtruediv__', '__eq__', '__ne__', '__lt__', '__gt__', '__le__', '__ge__'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'float qfloat16::operator float() const': an operator Python has no
    name for.
  - Qt's 'qfloat16 qfloat16::operator++(int a0)': an operator Python has no
    name for.
  - Qt's 'qfloat16 &qfloat16::operator++()': an operator Python has no name
    for.
  - Qt's 'qfloat16 qfloat16::operator--(int a0)': an operator Python has no
    name for.
  - Qt's 'qfloat16 &qfloat16::operator--()': an operator Python has no name
    for.
  - Qt's 'qfloat16::qfloat16(Wrap nibble)': takes a type Python has no way to
    hand over yet.
  - Qt's 'long double operator+(qfloat16 lhs, long double rhs)': takes a type
    Python has no way to hand over yet.
  - Qt's 'long double operator+(long double lhs, qfloat16 rhs)': takes a type
    Python has no way to hand over yet.
  - Qt's 'long double operator-(qfloat16 lhs, long double rhs)': takes a type
    Python has no way to hand over yet.
  - Qt's 'long double operator-(long double lhs, qfloat16 rhs)': takes a type
    Python has no way to hand over yet.
  - Qt's 'long double operator*(qfloat16 lhs, long double rhs)': takes a type
    Python has no way to hand over yet.
  - Qt's 'long double operator*(long double lhs, qfloat16 rhs)': takes a type
    Python has no way to hand over yet.
  - Qt's 'long double operator/(qfloat16 lhs, long double rhs)': takes a type
    Python has no way to hand over yet.
  - Qt's 'long double operator/(long double lhs, qfloat16 rhs)': takes a type
    Python has no way to hand over yet.
  - Qt's 'qfloat16 &operator+=(qfloat16 &lhs, long double rhs)': an operator
    Python has no name for.
  - Qt's 'qfloat16 &operator-=(qfloat16 &lhs, long double rhs)': an operator
    Python has no name for.
  - Qt's 'qfloat16 &operator*=(qfloat16 &lhs, long double rhs)': an operator
    Python has no name for.
  - Qt's 'qfloat16 &operator/=(qfloat16 &lhs, long double rhs)': an operator
    Python has no name for.
  - Qt's 'qfloat16 &operator+=(qfloat16 &lhs, double rhs)': an operator
    Python has no name for.
  - Qt's 'qfloat16 &operator-=(qfloat16 &lhs, double rhs)': an operator
    Python has no name for.
  - Qt's 'qfloat16 &operator*=(qfloat16 &lhs, double rhs)': an operator
    Python has no name for.
  - Qt's 'qfloat16 &operator/=(qfloat16 &lhs, double rhs)': an operator
    Python has no name for.
  - Qt's 'float operator+(qfloat16 lhs, float rhs)': takes in Python what
    'double operator+(qfloat16 lhs, double rhs)' takes.
  - Qt's 'float operator+(float lhs, qfloat16 rhs)': takes in Python what
    'double operator+(double lhs, qfloat16 rhs)' takes.
  - Qt's 'float operator-(qfloat16 lhs, float rhs)': takes in Python what
    'double operator-(qfloat16 lhs, double rhs)' takes.
  - Qt's 'float operator-(float lhs, qfloat16 rhs)': takes in Python what
    'double operator-(double lhs, qfloat16 rhs)' takes.
  - Qt's 'float operator*(qfloat16 lhs, float rhs)': takes in Python what
    'double operator*(qfloat16 lhs, double rhs)' takes.
  - Qt's 'float operator*(float lhs, qfloat16 rhs)': takes in Python what
    'double operator*(double lhs, qfloat16 rhs)' takes.
  - Qt's 'float operator/(qfloat16 lhs, float rhs)': takes in Python what
    'double operator/(qfloat16 lhs, double rhs)' takes.
  - Qt's 'float operator/(float lhs, qfloat16 rhs)': takes in Python what
    'double operator/(double lhs, qfloat16 rhs)' takes.
  - Qt's 'qfloat16 &operator+=(qfloat16 &lhs, float rhs)': an operator Python
    has no name for.
  - Qt's 'qfloat16 &operator-=(qfloat16 &lhs, float rhs)': an operator Python
    has no name for.
  - Qt's 'qfloat16 &operator*=(qfloat16 &lhs, float rhs)': an operator Python
    has no name for.
  - Qt's 'qfloat16 &operator/=(qfloat16 &lhs, float rhs)': an operator Python
    has no name for.
  - Qt's 'bool operator==(const qfloat16 &lhs, const long double &rhs)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const long double &rhs)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool operator<(const qfloat16 &lhs, const long double &rhs)': takes
    a type Python has no way to hand over yet.
  - Qt's 'bool operator>(const qfloat16 &lhs, const long double &rhs)': takes
    a type Python has no way to hand over yet.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const long double &rhs)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const long double &rhs)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool operator==(const long double &lhs, const qfloat16 &rhs)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool operator!=(const long double &lhs, const qfloat16 &rhs)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool operator<(const long double &lhs, const qfloat16 &rhs)': takes
    a type Python has no way to hand over yet.
  - Qt's 'bool operator>(const long double &lhs, const qfloat16 &rhs)': takes
    a type Python has no way to hand over yet.
  - Qt's 'bool operator<=(const long double &lhs, const qfloat16 &rhs)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool operator>=(const long double &lhs, const qfloat16 &rhs)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool operator==(const double &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator!=(const double &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator<(const double &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator>(const double &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator<=(const double &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator>=(const double &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const float &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const float &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const float &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const float &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const float &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const float &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator==(const float &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator!=(const float &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator<(const float &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator>(const float &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator<=(const float &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator>=(const float &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const double &rhs)'
    takes.
  - Qt's 'bool operator==(const qint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const quint8 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const quint8 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const quint8 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const quint8 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const quint8 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const quint8 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const quint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const quint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const quint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const quint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const quint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const quint8 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const qint16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const qint16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const qint16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const qint16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const qint16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const qint16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const quint16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const quint16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const quint16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const quint16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const quint16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const quint16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const quint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const quint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const quint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const quint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const quint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const quint16 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const qint32 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const qint32 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const qint32 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const qint32 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const qint32 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const qint32 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const quint32 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const quint32 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const quint32 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const quint32 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const quint32 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const quint32 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const quint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const quint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const quint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const quint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const quint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const quint32 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const long &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const long &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const long &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const long &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const long &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const long &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const long &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const long &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const long &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const long &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const long &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const long &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const unsigned long &rhs)':
    takes in Python what 'bool operator==(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const unsigned long &rhs)':
    takes in Python what 'bool operator!=(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const unsigned long &rhs)':
    takes in Python what 'bool operator<(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const unsigned long &rhs)':
    takes in Python what 'bool operator>(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const unsigned long &rhs)':
    takes in Python what 'bool operator<=(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const unsigned long &rhs)':
    takes in Python what 'bool operator>=(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator==(const unsigned long &lhs, const qfloat16 &rhs)':
    takes in Python what 'bool operator==(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator!=(const unsigned long &lhs, const qfloat16 &rhs)':
    takes in Python what 'bool operator!=(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator<(const unsigned long &lhs, const qfloat16 &rhs)':
    takes in Python what 'bool operator>(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator>(const unsigned long &lhs, const qfloat16 &rhs)':
    takes in Python what 'bool operator<(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator<=(const unsigned long &lhs, const qfloat16 &rhs)':
    takes in Python what 'bool operator>=(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator>=(const unsigned long &lhs, const qfloat16 &rhs)':
    takes in Python what 'bool operator<=(const qfloat16 &lhs, const qint8
    &rhs)' takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const qint64 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const qint64 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const qint64 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const qint64 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const qint64 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const qint64 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const qfloat16 &lhs, const quint64 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const qfloat16 &lhs, const quint64 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const qfloat16 &lhs, const quint64 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const qfloat16 &lhs, const quint64 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const qfloat16 &lhs, const quint64 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const qfloat16 &lhs, const quint64 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator==(const quint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator!=(const quint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<(const quint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>(const quint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator<=(const quint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'bool operator>=(const quint64 &lhs, const qfloat16 &rhs)': takes in
    Python what 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'
    takes.
  - Qt's 'QDataStream &operator<<(QDataStream &ds, qfloat16 f)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &ds, qfloat16 &f)': an operator
    between other classes, written inside this one.
  - Qt's 'QTextStream &operator<<(QTextStream &ts, qfloat16 f)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QTextStream &operator>>(QTextStream &ts, qfloat16 &f)': an operator
    between other classes, written inside this one.
  - Qt's 'qfloat16::~qfloat16()': the destructor: Python removes its C++
    qfloat16 by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 241 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ qfloat16 is created at the first use, not by 'qfloat16(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qfloat16 back gives a copy the ritual made for
    Python, in a new cute qfloat16.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _limit_epsilon() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_epsilon()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_epsilon

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_epsilon()
    address = Rituals.call('ritual_ZN8qfloat1614_limit_epsilonEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_min() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_min()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_min

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_min()
    address = Rituals.call('ritual_ZN8qfloat1610_limit_minEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_denorm_min() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_denorm_min()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_denorm_min

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_denorm_min()
    address = Rituals.call('ritual_ZN8qfloat1617_limit_denorm_minEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_max() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_max()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_max

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_max()
    address = Rituals.call('ritual_ZN8qfloat1610_limit_maxEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_lowest() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_lowest()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_lowest

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_lowest()
    address = Rituals.call('ritual_ZN8qfloat1613_limit_lowestEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_infinity() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_infinity()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_infinity

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_infinity()
    address = Rituals.call('ritual_ZN8qfloat1615_limit_infinityEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_quiet_NaN() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_quiet_NaN()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_quiet_NaN

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_quiet_NaN()
    address = Rituals.call('ritual_ZN8qfloat1616_limit_quiet_NaNEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_signaling_NaN() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_signaling_NaN()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_signaling_NaN

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_signaling_NaN()
    address = Rituals.call('ritual_ZN8qfloat1620_limit_signaling_NaNEv')
    return qfloat16._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qfloat16'

  #  Qt's '~qfloat16()'. Naming it makes this a value class: Python owns
  #  every C++ qfloat16 behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8qfloat16D1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isInf(self) -> bool:
    """
    Calls Qt's 'bool qfloat16::isInf() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#isInf
    """
    #  bool qfloat16::isInf() const
    return self.uglySide.call('ritual_ZNK8qfloat165isInfEv')

  def isNaN(self) -> bool:
    """
    Calls Qt's 'bool qfloat16::isNaN() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#isNaN
    """
    #  bool qfloat16::isNaN() const
    return self.uglySide.call('ritual_ZNK8qfloat165isNaNEv')

  def isFinite(self) -> bool:
    """
    Calls Qt's 'bool qfloat16::isFinite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#isFinite
    """
    #  bool qfloat16::isFinite() const
    return self.uglySide.call('ritual_ZNK8qfloat168isFiniteEv')

  def fpClassify(self) -> int:
    """
    Calls Qt's 'int qfloat16::fpClassify() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#fpClassify
    """
    #  int qfloat16::fpClassify() const
    return self.uglySide.call('ritual_ZNK8qfloat1610fpClassifyEv')

  @overload(THIS)
  def copySign(self, sign: qfloat16) -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::copySign(qfloat16 sign) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#copySign

    Parameters
    ----------

    sign : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::copySign(qfloat16 sign) const
    address = self.uglySide.call(
        'ritual_ZNK8qfloat168copySignES_', self._valueOf(sign),
    )
    return qfloat16._cuteOwning(address)

  def isNormal(self) -> bool:
    """
    Calls Qt's 'bool qfloat16::isNormal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#isNormal
    """
    #  bool qfloat16::isNormal() const
    return self.uglySide.call('ritual_ZNK8qfloat168isNormalEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __pos__(self) -> qfloat16:
    """
    Calls Qt's 'qfloat16 operator+(qfloat16 a)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator+

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 operator+(qfloat16 a)
    address = Rituals.call('ritual_Zps8qfloat16', CuteMixin._valueOf(self))
    return qfloat16._cuteOwning(address)

  def __neg__(self) -> qfloat16:
    """
    Calls Qt's 'qfloat16 operator-(qfloat16 a)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator-

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 operator-(qfloat16 a)
    address = Rituals.call('ritual_Zng8qfloat16', CuteMixin._valueOf(self))
    return qfloat16._cuteOwning(address)

  @overload(THIS)
  def __add__(self, b: qfloat16) -> qfloat16:
    """
    Calls Qt's 'qfloat16 operator+(qfloat16 a, qfloat16 b)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator+

    Parameters
    ----------

    b : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 operator+(qfloat16 a, qfloat16 b)
    address = Rituals.call(
        'ritual_Zpl8qfloat16S_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )
    return qfloat16._cuteOwning(address)

  @overload(float)
  def __add__(self, rhs: float) -> float:
    """
    Calls Qt's 'double operator+(qfloat16 lhs, double rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator+

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  double operator+(qfloat16 lhs, double rhs)
    return Rituals.call(
        'ritual_Zpl8qfloat16d', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __add__(self, rhs: int) -> float:
    """
    Calls Qt's 'double operator+(qfloat16 lhs, int rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator+

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  double operator+(qfloat16 lhs, int rhs)
    return Rituals.call(
        'ritual_Zpl8qfloat16i', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, b: qfloat16) -> qfloat16:
    """
    Calls Qt's 'qfloat16 operator-(qfloat16 a, qfloat16 b)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator-

    Parameters
    ----------

    b : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 operator-(qfloat16 a, qfloat16 b)
    address = Rituals.call(
        'ritual_Zmi8qfloat16S_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )
    return qfloat16._cuteOwning(address)

  @overload(float)
  def __sub__(self, rhs: float) -> float:
    """
    Calls Qt's 'double operator-(qfloat16 lhs, double rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator-

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  double operator-(qfloat16 lhs, double rhs)
    return Rituals.call(
        'ritual_Zmi8qfloat16d', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __sub__(self, rhs: int) -> float:
    """
    Calls Qt's 'double operator-(qfloat16 lhs, int rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator-

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  double operator-(qfloat16 lhs, int rhs)
    return Rituals.call(
        'ritual_Zmi8qfloat16i', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __mul__(self, b: qfloat16) -> qfloat16:
    """
    Calls Qt's 'qfloat16 operator*(qfloat16 a, qfloat16 b)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator*

    Parameters
    ----------

    b : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 operator*(qfloat16 a, qfloat16 b)
    address = Rituals.call(
        'ritual_Zml8qfloat16S_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )
    return qfloat16._cuteOwning(address)

  @overload(float)
  def __mul__(self, rhs: float) -> float:
    """
    Calls Qt's 'double operator*(qfloat16 lhs, double rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator*

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  double operator*(qfloat16 lhs, double rhs)
    return Rituals.call(
        'ritual_Zml8qfloat16d', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __mul__(self, rhs: int) -> float:
    """
    Calls Qt's 'double operator*(qfloat16 lhs, int rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator*

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  double operator*(qfloat16 lhs, int rhs)
    return Rituals.call(
        'ritual_Zml8qfloat16i', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __truediv__(self, b: qfloat16) -> qfloat16:
    """
    Calls Qt's 'qfloat16 operator/(qfloat16 a, qfloat16 b)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator/

    Parameters
    ----------

    b : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 operator/(qfloat16 a, qfloat16 b)
    address = Rituals.call(
        'ritual_Zdv8qfloat16S_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )
    return qfloat16._cuteOwning(address)

  @overload(float)
  def __truediv__(self, rhs: float) -> float:
    """
    Calls Qt's 'double operator/(qfloat16 lhs, double rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator/

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  double operator/(qfloat16 lhs, double rhs)
    return Rituals.call(
        'ritual_Zdv8qfloat16d', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __truediv__(self, rhs: int) -> float:
    """
    Calls Qt's 'double operator/(qfloat16 lhs, int rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator/

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  double operator/(qfloat16 lhs, int rhs)
    return Rituals.call(
        'ritual_Zdv8qfloat16i', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __truediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __radd__(self, lhs: float) -> float:
    """
    Calls Qt's 'double operator+(double lhs, qfloat16 rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator+

    Parameters
    ----------

    lhs : float
      Passed on as it is.
    """
    #  double operator+(double lhs, qfloat16 rhs)
    return Rituals.call(
        'ritual_Zpld8qfloat16', lhs, CuteMixin._valueOf(self),
    )

  @overload(int)
  def __radd__(self, lhs: int) -> float:
    """
    Calls Qt's 'double operator+(int lhs, qfloat16 rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator+

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  double operator+(int lhs, qfloat16 rhs)
    return Rituals.call(
        'ritual_Zpli8qfloat16', lhs, CuteMixin._valueOf(self),
    )

  @overload.fallback
  def __radd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __rsub__(self, lhs: float) -> float:
    """
    Calls Qt's 'double operator-(double lhs, qfloat16 rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator-

    Parameters
    ----------

    lhs : float
      Passed on as it is.
    """
    #  double operator-(double lhs, qfloat16 rhs)
    return Rituals.call(
        'ritual_Zmid8qfloat16', lhs, CuteMixin._valueOf(self),
    )

  @overload(int)
  def __rsub__(self, lhs: int) -> float:
    """
    Calls Qt's 'double operator-(int lhs, qfloat16 rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator-

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  double operator-(int lhs, qfloat16 rhs)
    return Rituals.call(
        'ritual_Zmii8qfloat16', lhs, CuteMixin._valueOf(self),
    )

  @overload.fallback
  def __rsub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __rmul__(self, lhs: float) -> float:
    """
    Calls Qt's 'double operator*(double lhs, qfloat16 rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator*

    Parameters
    ----------

    lhs : float
      Passed on as it is.
    """
    #  double operator*(double lhs, qfloat16 rhs)
    return Rituals.call(
        'ritual_Zmld8qfloat16', lhs, CuteMixin._valueOf(self),
    )

  @overload(int)
  def __rmul__(self, lhs: int) -> float:
    """
    Calls Qt's 'double operator*(int lhs, qfloat16 rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator*

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  double operator*(int lhs, qfloat16 rhs)
    return Rituals.call(
        'ritual_Zmli8qfloat16', lhs, CuteMixin._valueOf(self),
    )

  @overload.fallback
  def __rmul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __rtruediv__(self, lhs: float) -> float:
    """
    Calls Qt's 'double operator/(double lhs, qfloat16 rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator/

    Parameters
    ----------

    lhs : float
      Passed on as it is.
    """
    #  double operator/(double lhs, qfloat16 rhs)
    return Rituals.call(
        'ritual_Zdvd8qfloat16', lhs, CuteMixin._valueOf(self),
    )

  @overload(int)
  def __rtruediv__(self, lhs: int) -> float:
    """
    Calls Qt's 'double operator/(int lhs, qfloat16 rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator/

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  double operator/(int lhs, qfloat16 rhs)
    return Rituals.call(
        'ritual_Zdvi8qfloat16', lhs, CuteMixin._valueOf(self),
    )

  @overload.fallback
  def __rtruediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: qfloat16) -> bool:
    """
    Calls Qt's 'bool operator==(const qfloat16 &lhs, const qfloat16 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator==

    Parameters
    ----------

    rhs : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.
    """
    #  bool operator==(const qfloat16 &lhs, const qfloat16 &rhs)
    return Rituals.call(
        'ritual_ZeqRK8qfloat16S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(float)
  def __eq__(self, rhs: float) -> bool:
    """
    Calls Qt's 'bool operator==(const qfloat16 &lhs, const double &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator==

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  bool operator==(const qfloat16 &lhs, const double &rhs)
    return Rituals.call(
        'ritual_ZeqRK8qfloat16RKd', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __eq__(self, rhs: int) -> bool:
    """
    Calls Qt's 'bool operator==(const qfloat16 &lhs, const qint8 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator==

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  bool operator==(const qfloat16 &lhs, const qint8 &rhs)
    return Rituals.call(
        'ritual_ZeqRK8qfloat16RKa', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: qfloat16) -> bool:
    """
    Calls Qt's 'bool operator!=(const qfloat16 &lhs, const qfloat16 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator!=

    Parameters
    ----------

    rhs : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.
    """
    #  bool operator!=(const qfloat16 &lhs, const qfloat16 &rhs)
    return Rituals.call(
        'ritual_ZneRK8qfloat16S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(float)
  def __ne__(self, rhs: float) -> bool:
    """
    Calls Qt's 'bool operator!=(const qfloat16 &lhs, const double &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator!=

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  bool operator!=(const qfloat16 &lhs, const double &rhs)
    return Rituals.call(
        'ritual_ZneRK8qfloat16RKd', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __ne__(self, rhs: int) -> bool:
    """
    Calls Qt's 'bool operator!=(const qfloat16 &lhs, const qint8 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator!=

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  bool operator!=(const qfloat16 &lhs, const qint8 &rhs)
    return Rituals.call(
        'ritual_ZneRK8qfloat16RKa', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: qfloat16) -> bool:
    """
    Calls Qt's 'bool operator<(const qfloat16 &lhs, const qfloat16 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator<

    Parameters
    ----------

    rhs : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.
    """
    #  bool operator<(const qfloat16 &lhs, const qfloat16 &rhs)
    return Rituals.call(
        'ritual_ZltRK8qfloat16S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(float)
  def __lt__(self, rhs: float) -> bool:
    """
    Calls Qt's 'bool operator<(const qfloat16 &lhs, const double &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator<

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  bool operator<(const qfloat16 &lhs, const double &rhs)
    return Rituals.call(
        'ritual_ZltRK8qfloat16RKd', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __lt__(self, rhs: int) -> bool:
    """
    Calls Qt's 'bool operator<(const qfloat16 &lhs, const qint8 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator<

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  bool operator<(const qfloat16 &lhs, const qint8 &rhs)
    return Rituals.call(
        'ritual_ZltRK8qfloat16RKa', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: qfloat16) -> bool:
    """
    Calls Qt's 'bool operator>(const qfloat16 &lhs, const qfloat16 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator>

    Parameters
    ----------

    rhs : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.
    """
    #  bool operator>(const qfloat16 &lhs, const qfloat16 &rhs)
    return Rituals.call(
        'ritual_ZgtRK8qfloat16S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(float)
  def __gt__(self, rhs: float) -> bool:
    """
    Calls Qt's 'bool operator>(const qfloat16 &lhs, const double &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator>

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  bool operator>(const qfloat16 &lhs, const double &rhs)
    return Rituals.call(
        'ritual_ZgtRK8qfloat16RKd', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __gt__(self, rhs: int) -> bool:
    """
    Calls Qt's 'bool operator>(const qfloat16 &lhs, const qint8 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator>

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  bool operator>(const qfloat16 &lhs, const qint8 &rhs)
    return Rituals.call(
        'ritual_ZgtRK8qfloat16RKa', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: qfloat16) -> bool:
    """
    Calls Qt's 'bool operator<=(const qfloat16 &lhs, const qfloat16 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator<=

    Parameters
    ----------

    rhs : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.
    """
    #  bool operator<=(const qfloat16 &lhs, const qfloat16 &rhs)
    return Rituals.call(
        'ritual_ZleRK8qfloat16S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(float)
  def __le__(self, rhs: float) -> bool:
    """
    Calls Qt's 'bool operator<=(const qfloat16 &lhs, const double &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator<=

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  bool operator<=(const qfloat16 &lhs, const double &rhs)
    return Rituals.call(
        'ritual_ZleRK8qfloat16RKd', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __le__(self, rhs: int) -> bool:
    """
    Calls Qt's 'bool operator<=(const qfloat16 &lhs, const qint8 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator<=

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  bool operator<=(const qfloat16 &lhs, const qint8 &rhs)
    return Rituals.call(
        'ritual_ZleRK8qfloat16RKa', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: qfloat16) -> bool:
    """
    Calls Qt's 'bool operator>=(const qfloat16 &lhs, const qfloat16 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator>=

    Parameters
    ----------

    rhs : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.
    """
    #  bool operator>=(const qfloat16 &lhs, const qfloat16 &rhs)
    return Rituals.call(
        'ritual_ZgeRK8qfloat16S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(float)
  def __ge__(self, rhs: float) -> bool:
    """
    Calls Qt's 'bool operator>=(const qfloat16 &lhs, const double &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator>=

    Parameters
    ----------

    rhs : float
      Passed on as it is.
    """
    #  bool operator>=(const qfloat16 &lhs, const double &rhs)
    return Rituals.call(
        'ritual_ZgeRK8qfloat16RKd', CuteMixin._valueOf(self), rhs,
    )

  @overload(int)
  def __ge__(self, rhs: int) -> bool:
    """
    Calls Qt's 'bool operator>=(const qfloat16 &lhs, const qint8 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#operator>=

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  bool operator>=(const qfloat16 &lhs, const qint8 &rhs)
    return Rituals.call(
        'ritual_ZgeRK8qfloat16RKa', CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's 'qfloat16::qfloat16(Qt::Initialization
    a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#qfloat16

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  qfloat16::qfloat16(Qt::Initialization a0)
    self._noteCreation(qfloat16, lambda: Rituals.call(
        'ritual_ZN8qfloat16C1EN2Qt14InitializationE', a0.value,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'qfloat16::qfloat16()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#qfloat16
    """
    #  qfloat16::qfloat16()
    self._noteCreation(qfloat16, lambda: Rituals.call(
        'ritual_ZN8qfloat16C1Ev',
    ))

  @overload(float)
  def __init__(self, f: float) -> None:
    """
    Notes what was given, for Qt's 'qfloat16::qfloat16(float f)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#qfloat16

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  qfloat16::qfloat16(float f)
    self._noteCreation(qfloat16, lambda: Rituals.call(
        'ritual_ZN8qfloat16C1Ef', f,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
