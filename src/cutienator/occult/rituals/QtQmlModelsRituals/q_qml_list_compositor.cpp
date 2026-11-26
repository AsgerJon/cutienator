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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 252, as _ZN18QQmlListCompositorC1Ev
inline QQmlListCompositor::QQmlListCompositor()
    : m_end(m_ranges.next, 0, Default, 2)
    , m_cacheIt(m_end)
    , m_groupCount(2)
    , m_defaultFlags(PrependFlag | DefaultFlag)
    , m_removeFlags(AppendFlag | PrependFlag | GroupMask)
    , m_moveId(0)
{
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 266, as _ZN18QQmlListCompositorD1Ev
inline QQmlListCompositor::~QQmlListCompositor()
{
    for (Range *next, *range = m_ranges.next; range != &m_ranges; range = next) {
        next = range->next;
        delete range;
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 305, as _ZN18QQmlListCompositor13setGroupCountEi
inline void QQmlListCompositor::setGroupCount(int count)
{
    m_groupCount = count;
    m_end = iterator(&m_ranges, 0, Default, m_groupCount);
    m_cacheIt = m_end;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 316, as _ZNK18QQmlListCompositor5countENS_5GroupE
inline int QQmlListCompositor::count(Group group) const
{
    return m_end.index[group];
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 1305, as _ZN18QQmlListCompositor10transitionENS_5GroupES0_P5QListIN13QQmlChangeSet6ChangeEES5_
inline void QQmlListCompositor::transition(
        Group from,
        Group to,
        QList<QQmlChangeSet::Change> *removes,
        QList<QQmlChangeSet::Change> *inserts)
{
    int removeCount = 0;
    for (iterator it(m_ranges.next, 0, Default, m_groupCount); *it != &m_ranges; *it = it->next) {
        if (it == from && it != to) {
            removes->append(QQmlChangeSet::Change(it.index[from]- removeCount, it->count));
            removeCount += it->count;
        } else if (it != from && it == to) {
            inserts->append(QQmlChangeSet::Change(it.index[to], it->count));
        }
        it.incrementIndexes(it->count);
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 279, as _ZN18QQmlListCompositor6insertEPNS_5RangeEPviij
inline QQmlListCompositor::Range *QQmlListCompositor::insert(
        Range *before, void *list, int index, int count, uint flags)
{
    return new Range(before, list, index, count, flags);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 291, as _ZN18QQmlListCompositor5eraseEPNS_5RangeE
inline QQmlListCompositor::Range *QQmlListCompositor::erase(
        Range *range)
{
    Range *next = range->next;
    next->previous = range->previous;
    next->previous->next = range->next;
    delete range;
    return next;
}
//  -----------------------------------------------------------------------

//  QQmlListCompositor::QQmlListCompositor()
extern "C" Q_DECL_EXPORT
QQmlListCompositor *ritual_ZN18QQmlListCompositorC1Ev() {
  return new QQmlListCompositor();
}

//  QQmlListCompositor::~QQmlListCompositor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositorD1Ev(QQmlListCompositor *self) {
  delete self;
}

//  int QQmlListCompositor::defaultGroups() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor13defaultGroupsEv(
    const QQmlListCompositor *self) {
  return self->defaultGroups();
}

//  void QQmlListCompositor::setDefaultGroups(int groups)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor16setDefaultGroupsEi(
    QQmlListCompositor *self,
    int groups) {
  self->setDefaultGroups(groups);
}

//  void QQmlListCompositor::setDefaultGroup(Group group)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor15setDefaultGroupENS_5GroupE(
    QQmlListCompositor *self,
    QQmlListCompositor::Group group) {
  self->setDefaultGroup(group);
}

//  void QQmlListCompositor::clearDefaultGroup(Group group)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor17clearDefaultGroupENS_5GroupE(
    QQmlListCompositor *self,
    QQmlListCompositor::Group group) {
  self->clearDefaultGroup(group);
}

//  void QQmlListCompositor::setRemoveGroups(int groups)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor15setRemoveGroupsEi(
    QQmlListCompositor *self,
    int groups) {
  self->setRemoveGroups(groups);
}

//  void QQmlListCompositor::setGroupCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor13setGroupCountEi(
    QQmlListCompositor *self,
    int count) {
  self->setGroupCount(count);
}

//  int QQmlListCompositor::count(Group group) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor5countENS_5GroupE(
    const QQmlListCompositor *self,
    QQmlListCompositor::Group group) {
  return self->count(group);
}

//  const iterator &QQmlListCompositor::end()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::iterator *ritual_ZN18QQmlListCompositor3endEv(
    QQmlListCompositor *self) {
  return new QQmlListCompositor::iterator(self->end());
}

//  void QQmlListCompositor::transition(Group from, Group to,
//      QList<QQmlChangeSet::Change> *removes, QList<QQmlChangeSet::Change>
//      *inserts)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor10transitionENS_5GroupES0_P5QListIN13QQmlChangeSet6ChangeEES5_(
    QQmlListCompositor *self,
    QQmlListCompositor::Group from,
    QQmlListCompositor::Group to,
    QList<QQmlChangeSet::Change> *removes,
    QList<QQmlChangeSet::Change> *inserts) {
  self->transition(from, to, removes, inserts);
}

//  Range *QQmlListCompositor::insert(Range *before, void *list, int index,
//      int count, uint flags)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Range *ritual_ZN18QQmlListCompositor6insertEPNS_5RangeEPviij(
    QQmlListCompositor *self,
    QQmlListCompositor::Range *before,
    void *list,
    int index,
    int count,
    uint flags) {
  return self->insert(before, list, index, count, flags);
}

//  Range *QQmlListCompositor::erase(Range *range)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Range *ritual_ZN18QQmlListCompositor5eraseEPNS_5RangeE(
    QQmlListCompositor *self,
    QQmlListCompositor::Range *range) {
  return self->erase(range);
}

#endif  // QT_CONFIG(qml_delegate_model)
