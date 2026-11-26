//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtCore/QHash>
#include <QtCore/private/qnumeric_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4string.cpp, line 63, as _ZN3QV44Heap13ComplexString4initEPNS0_6StringES3_
namespace QV4 {
inline void Heap::ComplexString::init(String *l, String *r)
{
    StringOrSymbol::init();
    subtype = String::StringType_AddedString;

    left = l;
    right = r;
    len = left->length() + right->length();
    if (left->subtype >= StringType_Complex)
        largestSubLength = static_cast<ComplexString *>(left)->largestSubLength;
    else
        largestSubLength = left->length();
    if (right->subtype >= StringType_Complex)
        largestSubLength = qMax(largestSubLength, static_cast<ComplexString *>(right)->largestSubLength);
    else
        largestSubLength = qMax(largestSubLength, right->length());

    // make sure we don't get excessive depth in our strings
    if (len > 256 && len >= 2*largestSubLength)
        simplifyString();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4string.cpp, line 85, as _ZN3QV44Heap13ComplexString4initEPNS0_6StringEii
namespace QV4 {
inline void Heap::ComplexString::init(Heap::String *ref, int from, int len)
{
    Q_ASSERT(ref->length() >= from + len);
    StringOrSymbol::init();

    subtype = String::StringType_SubString;

    left = ref;
    this->from = from;
    this->len = len;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ComplexString::init(String *l, String *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13ComplexString4initEPNS0_6StringES3_(
    QV4::Heap::ComplexString *self,
    QV4::Heap::String *l,
    QV4::Heap::String *n) {
  self->init(l, n);
}

//  void QV4::Heap::ComplexString::init(String *ref, int from, int len)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13ComplexString4initEPNS0_6StringEii(
    QV4::Heap::ComplexString *self,
    QV4::Heap::String *ref,
    int from,
    int len) {
  self->init(ref, from, len);
}
