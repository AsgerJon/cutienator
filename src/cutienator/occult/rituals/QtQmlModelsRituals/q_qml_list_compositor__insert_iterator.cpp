//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmllistcompositor_p.h>
#include <QtCore/qvarlengtharray.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 199, as _ZN18QQmlListCompositor8iteratorpLEi
inline QQmlListCompositor::iterator &QQmlListCompositor::iterator::operator +=(int difference)
{
    // Update all indexes to the start of the range.
    decrementIndexes(offset);

    // If the iterator group isn't a member of the current range ignore the current offset.
    if (!(range->flags & groupFlag))
        offset = 0;

    offset += difference;

    // Iterate backwards looking for a range with a positive offset.
    while (offset <= 0 && range->previous->flags) {
        range = range->previous;
        if (range->flags & groupFlag)
            offset += range->count;
        decrementIndexes(range->count);
    }

    // Iterate forwards looking for the first range which contains both the offset and the
    // iterator group.
    while (range->flags && (offset >= range->count || !(range->flags & groupFlag))) {
        if (range->flags & groupFlag)
            offset -= range->count;
        incrementIndexes(range->count);
        range = range->next;
    }

    // Update all the indexes to inclue the remaining offset.
    incrementIndexes(offset);

    return *this;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 233, as _ZN18QQmlListCompositor15insert_iteratorpLEi
inline QQmlListCompositor::insert_iterator &QQmlListCompositor::insert_iterator::operator +=(int difference)
{
    iterator::operator +=(difference);

    // If the previous range contains the append flag move the iterator to the tail of the previous
    // range so that appended appear after the insert position.
    if (offset == 0 && range->previous->append()) {
        range = range->previous;
        offset = range->inGroup() ? range->count : 0;
    }

    return *this;
}
//  -----------------------------------------------------------------------

//  QQmlListCompositor::insert_iterator::insert_iterator()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::insert_iterator *ritual_ZN18QQmlListCompositor15insert_iteratorC1Ev() {
  return new QQmlListCompositor::insert_iterator();
}

//  QQmlListCompositor::insert_iterator::insert_iterator(const iterator &it)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::insert_iterator *ritual_ZN18QQmlListCompositor15insert_iteratorC1ERKNS_8iteratorE(
    const QQmlListCompositor::iterator *it) {
  return new QQmlListCompositor::insert_iterator(*it);
}

//  QQmlListCompositor::insert_iterator::insert_iterator(Range *a0, int a1,
//      Group a2, int a3)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::insert_iterator *ritual_ZN18QQmlListCompositor15insert_iteratorC1EPNS_5RangeEiNS_5GroupEi(
    QQmlListCompositor::Range *a0,
    int a1,
    QQmlListCompositor::Group a2,
    int a3) {
  return new QQmlListCompositor::insert_iterator(a0, a1, a2, a3);
}

//  insert_iterator &QQmlListCompositor::insert_iterator::operator+=(int
//      difference)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor15insert_iteratorpLEi(
    QQmlListCompositor::insert_iterator *self,
    int difference) {
  self->operator+=(difference);
}

//  QQmlListCompositor::insert_iterator::~insert_iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor15insert_iteratorD1Ev(
    QQmlListCompositor::insert_iterator *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
