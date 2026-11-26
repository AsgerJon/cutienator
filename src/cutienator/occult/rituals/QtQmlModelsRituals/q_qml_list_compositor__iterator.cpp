//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 2. Kept as it is when the generator runs again. Also added by
//  hand on 2026-11-25, rituals for functions the generator leaves out: 1.
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
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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
//  -----------------------------------------------------------------------

//  QQmlListCompositor::iterator::iterator()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::iterator *ritual_ZN18QQmlListCompositor8iteratorC1Ev() {
  return new QQmlListCompositor::iterator();
}

//  QQmlListCompositor::iterator::iterator(Range *range, int offset, Group
//      group, int groupCount)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::iterator *ritual_ZN18QQmlListCompositor8iteratorC1EPNS_5RangeEiNS_5GroupEi(
    QQmlListCompositor::Range *range,
    int offset,
    QQmlListCompositor::Group group,
    int groupCount) {
  return new QQmlListCompositor::iterator(range, offset, group, groupCount);
}

//  bool QQmlListCompositor::iterator::operator==(const iterator &it) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor8iteratoreqERKS0_(
    const QQmlListCompositor::iterator *self,
    const QQmlListCompositor::iterator *it) {
  return self->operator==(*it);
}

//  bool QQmlListCompositor::iterator::operator!=(const iterator &it) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor8iteratorneERKS0_(
    const QQmlListCompositor::iterator *self,
    const QQmlListCompositor::iterator *it) {
  return self->operator!=(*it);
}

//  bool QQmlListCompositor::iterator::operator==(Group group) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor8iteratoreqENS_5GroupE(
    const QQmlListCompositor::iterator *self,
    QQmlListCompositor::Group group) {
  return self->operator==(group);
}

//  bool QQmlListCompositor::iterator::operator!=(Group group) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor8iteratorneENS_5GroupE(
    const QQmlListCompositor::iterator *self,
    QQmlListCompositor::Group group) {
  return self->operator!=(group);
}

//  Range *const &QQmlListCompositor::iterator::operator*() const
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Range *const *ritual_ZNK18QQmlListCompositor8iteratordeEv(
    const QQmlListCompositor::iterator *self) {
  return &(self->operator*());
}

//  Range *QQmlListCompositor::iterator::operator->()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Range *ritual_ZN18QQmlListCompositor8iteratorptEv(
    QQmlListCompositor::iterator *self) {
  return self->operator->();
}

//  const Range *QQmlListCompositor::iterator::operator->() const
extern "C" Q_DECL_EXPORT
const QQmlListCompositor::Range *ritual_ZNK18QQmlListCompositor8iteratorptEv(
    const QQmlListCompositor::iterator *self) {
  return self->operator->();
}

//  iterator &QQmlListCompositor::iterator::operator+=(int difference)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iteratorpLEi(
    QQmlListCompositor::iterator *self,
    int difference) {
  self->operator+=(difference);
}

//  int QQmlListCompositor::iterator::modelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor8iterator10modelIndexEv(
    const QQmlListCompositor::iterator *self) {
  return self->modelIndex();
}

//  void QQmlListCompositor::iterator::incrementIndexes(int difference)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator16incrementIndexesEi(
    QQmlListCompositor::iterator *self,
    int difference) {
  self->incrementIndexes(difference);
}

//  void QQmlListCompositor::iterator::decrementIndexes(int difference)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator16decrementIndexesEi(
    QQmlListCompositor::iterator *self,
    int difference) {
  self->decrementIndexes(difference);
}

//  void QQmlListCompositor::iterator::incrementIndexes(int difference, uint
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator16incrementIndexesEij(
    QQmlListCompositor::iterator *self,
    int difference,
    uint flags) {
  self->incrementIndexes(difference, flags);
}

//  void QQmlListCompositor::iterator::decrementIndexes(int difference, uint
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator16decrementIndexesEij(
    QQmlListCompositor::iterator *self,
    int difference,
    uint flags) {
  self->decrementIndexes(difference, flags);
}

//  void QQmlListCompositor::iterator::setGroup(Group g)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator8setGroupENS_5GroupE(
    QQmlListCompositor::iterator *self,
    QQmlListCompositor::Group g) {
  self->setGroup(g);
}

//  int QQmlListCompositor::iterator::cacheIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor8iterator10cacheIndexEv(
    const QQmlListCompositor::iterator *self) {
  return self->cacheIndex();
}

//  void QQmlListCompositor::iterator::setCacheIndex(int cacheIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator13setCacheIndexEi(
    QQmlListCompositor::iterator *self,
    int cacheIndex) {
  self->setCacheIndex(cacheIndex);
}

//  QQmlListCompositor::iterator::~iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iteratorD1Ev(
    QQmlListCompositor::iterator *self) {
  delete self;
}

//  QQmlAdaptorModel *QQmlListCompositor::iterator::list<QQmlAdaptorModel>()
//      const
extern "C" Q_DECL_EXPORT
QQmlAdaptorModel *ritual_ZNK18QQmlListCompositor8iterator4listI16QQmlAdaptorModelEEPT_v(
    const QQmlListCompositor::iterator *self) {
  return self->list<QQmlAdaptorModel>();
}

//  QObject *QQmlListCompositor::iterator::list<QObject>() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QQmlListCompositor8iterator4listI7QObjectEEPT_v(
    const QQmlListCompositor::iterator *self) {
  return self->list<QObject>();
}

//  Range *&QQmlListCompositor::iterator::operator*()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Range **ritual_ZN18QQmlListCompositor8iteratordeEv(
    QQmlListCompositor::iterator *self) {
  return &(**self);
}

#endif  // QT_CONFIG(qml_delegate_model)
