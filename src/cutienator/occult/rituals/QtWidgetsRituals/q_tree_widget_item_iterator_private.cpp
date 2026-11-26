//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtreewidgetitemiterator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treewidget)
#if QT_CONFIG(treewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treewidget)
#include <QtWidgets/qtreewidgetitemiterator.h>
#endif
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtreewidgetitemiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qtreewidgetitemiterator_p.h>
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/private/qtreewidget_p.h>
#include <QtWidgets/private/qwidgetitemdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qtreewidgetitemiterator.cpp, line 231, as _ZNK30QTreeWidgetItemIteratorPrivate11nextSiblingEPK15QTreeWidgetItem
inline QTreeWidgetItem* QTreeWidgetItemIteratorPrivate::nextSibling(const QTreeWidgetItem* item) const
{
    Q_ASSERT(item);
    QTreeWidgetItem *next = nullptr;
    if (QTreeWidgetItem *par = item->parent()) {
        int i = par->indexOfChild(const_cast<QTreeWidgetItem*>(item));
        next = par->child(i + 1);
    } else {
        QTreeWidget *tw = item->treeWidget();
        int i = tw->indexOfTopLevelItem(const_cast<QTreeWidgetItem*>(item));
        next = tw->topLevelItem(i + 1);
    }
    return next;
}

//  from src/widgets/itemviews/qtreewidgetitemiterator.cpp, line 297, as _ZN30QTreeWidgetItemIteratorPrivate19ensureValidIteratorEPK15QTreeWidgetItem
inline void QTreeWidgetItemIteratorPrivate::ensureValidIterator(const QTreeWidgetItem *itemToBeRemoved)
{
    Q_Q(QTreeWidgetItemIterator);
    Q_ASSERT(itemToBeRemoved);

    if (!q->current) return;
    QTreeWidgetItem *nextItem = q->current;

    // Do not walk to the ancestor to find the other item if they have the same parent.
    if (nextItem->parent() != itemToBeRemoved->parent()) {
        while (nextItem->parent() && nextItem != itemToBeRemoved) {
            nextItem = nextItem->parent();
        }
    }
    // If the item to be removed is an ancestor of the current iterator item,
    // we need to adjust the iterator.
    if (nextItem == itemToBeRemoved) {
        QTreeWidgetItem *parent = nextItem;
        nextItem = nullptr;
        while (parent && !nextItem) {
            nextItem = nextSibling(parent);
            parent = parent->parent();
        }
        if (nextItem) {
            // Ooooh... Set the iterator to the next valid item
            *q = QTreeWidgetItemIterator(nextItem, q->flags);
            if (!(q->matchesFlags(nextItem))) ++(*q);
        } else {
            // set it to null.
            q->current = nullptr;
            m_parentIndex.clear();
            return;
        }
    }
    if (nextItem->parent() == itemToBeRemoved->parent()) {
        // They have the same parent, i.e. we have to adjust the m_currentIndex member of the iterator
        // if the deleted item is to the left of the nextItem.

        QTreeWidgetItem *par = itemToBeRemoved->parent();   // We know they both have the same parent.
        QTreeWidget *tw = itemToBeRemoved->treeWidget();    // ..and widget
        int indexOfItemToBeRemoved = par ? par->indexOfChild(const_cast<QTreeWidgetItem *>(itemToBeRemoved))
            : tw->indexOfTopLevelItem(const_cast<QTreeWidgetItem *>(itemToBeRemoved));
        int indexOfNextItem = par ? par->indexOfChild(nextItem) : tw->indexOfTopLevelItem(nextItem);

        if (indexOfItemToBeRemoved <= indexOfNextItem) {
            // A sibling to the left of us was deleted, adjust the m_currentIndex member of the iterator.
            // Note that the m_currentIndex will be wrong until the item is actually removed!
            m_currentIndex--;
        }
    }
}

//  from src/widgets/itemviews/qtreewidgetitemiterator.cpp, line 246, as _ZN30QTreeWidgetItemIteratorPrivate4nextEPK15QTreeWidgetItem
inline QTreeWidgetItem *QTreeWidgetItemIteratorPrivate::next(const QTreeWidgetItem *current)
{
    if (!current) return nullptr;

    QTreeWidgetItem *next = nullptr;
    if (current->childCount()) {
        // walk the child
        m_parentIndex.push(m_currentIndex);
        m_currentIndex = 0;
        next = current->child(0);
    } else {
        // walk the sibling
        QTreeWidgetItem *parent = current->parent();
        next = parent ? parent->child(m_currentIndex + 1)
                      : m_model->rootItem->child(m_currentIndex + 1);
        while (!next && parent) {
            // if we had no sibling walk up the parent and try the sibling of that
            parent = parent->parent();
            m_currentIndex = m_parentIndex.pop();
            next = parent ? parent->child(m_currentIndex + 1)
                          : m_model->rootItem->child(m_currentIndex + 1);
        }
        if (next) ++(m_currentIndex);
    }
    return next;
}

//  from src/widgets/itemviews/qtreewidgetitemiterator.cpp, line 273, as _ZN30QTreeWidgetItemIteratorPrivate8previousEPK15QTreeWidgetItem
inline QTreeWidgetItem *QTreeWidgetItemIteratorPrivate::previous(const QTreeWidgetItem *current)
{
    if (!current) return nullptr;

    QTreeWidgetItem *prev = nullptr;
    // walk the previous sibling
    QTreeWidgetItem *parent = current->parent();
    prev = parent ? parent->child(m_currentIndex - 1)
                  : m_model->rootItem->child(m_currentIndex - 1);
    if (prev) {
        // Yes, we had a previous sibling but we need go down to the last leafnode.
        --m_currentIndex;
        while (prev && prev->childCount()) {
            m_parentIndex.push(m_currentIndex);
            m_currentIndex = prev->childCount() - 1;
            prev = prev->child(m_currentIndex);
        }
    } else if (parent) {
        m_currentIndex = m_parentIndex.pop();
        prev = parent;
    }
    return prev;
}
//  -----------------------------------------------------------------------

//  QTreeWidgetItemIterator *QTreeWidgetItemIteratorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN30QTreeWidgetItemIteratorPrivate6q_funcEv(
    QTreeWidgetItemIteratorPrivate *self) {
  return self->q_func();
}

//  const QTreeWidgetItemIterator *QTreeWidgetItemIteratorPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QTreeWidgetItemIterator *ritual_ZNK30QTreeWidgetItemIteratorPrivate6q_funcEv(
    const QTreeWidgetItemIteratorPrivate *self) {
  return self->q_func();
}

//  QTreeWidgetItemIteratorPrivate::QTreeWidgetItemIteratorPrivate(QTreeWidge
//      tItemIterator *q, QTreeModel *model)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIteratorPrivate *ritual_ZN30QTreeWidgetItemIteratorPrivateC1EP23QTreeWidgetItemIteratorP10QTreeModel(
    QTreeWidgetItemIterator *q,
    QTreeModel *model) {
  return new QTreeWidgetItemIteratorPrivate(q, model);
}

//  QTreeWidgetItemIteratorPrivate::QTreeWidgetItemIteratorPrivate(const
//      QTreeWidgetItemIteratorPrivate &other)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIteratorPrivate *ritual_ZN30QTreeWidgetItemIteratorPrivateC1ERKS_(
    const QTreeWidgetItemIteratorPrivate *other) {
  return new QTreeWidgetItemIteratorPrivate(*other);
}

//  QTreeWidgetItemIteratorPrivate
//      &QTreeWidgetItemIteratorPrivate::operator=(const
//      QTreeWidgetItemIteratorPrivate &other)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIteratorPrivate *ritual_ZN30QTreeWidgetItemIteratorPrivateaSERKS_(
    QTreeWidgetItemIteratorPrivate *self,
    const QTreeWidgetItemIteratorPrivate *other) {
  return &(self->operator=(*other));
}

//  QTreeWidgetItemIteratorPrivate::~QTreeWidgetItemIteratorPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QTreeWidgetItemIteratorPrivateD1Ev(
    QTreeWidgetItemIteratorPrivate *self) {
  delete self;
}

//  QTreeWidgetItem *QTreeWidgetItemIteratorPrivate::nextSibling(const
//      QTreeWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK30QTreeWidgetItemIteratorPrivate11nextSiblingEPK15QTreeWidgetItem(
    const QTreeWidgetItemIteratorPrivate *self,
    const QTreeWidgetItem *item) {
  return self->nextSibling(item);
}

//  void QTreeWidgetItemIteratorPrivate::ensureValidIterator(const
//      QTreeWidgetItem *itemToBeRemoved)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QTreeWidgetItemIteratorPrivate19ensureValidIteratorEPK15QTreeWidgetItem(
    QTreeWidgetItemIteratorPrivate *self,
    const QTreeWidgetItem *itemToBeRemoved) {
  self->ensureValidIterator(itemToBeRemoved);
}

//  QTreeWidgetItem *QTreeWidgetItemIteratorPrivate::next(const
//      QTreeWidgetItem *current)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN30QTreeWidgetItemIteratorPrivate4nextEPK15QTreeWidgetItem(
    QTreeWidgetItemIteratorPrivate *self,
    const QTreeWidgetItem *current) {
  return self->next(current);
}

//  QTreeWidgetItem *QTreeWidgetItemIteratorPrivate::previous(const
//      QTreeWidgetItem *current)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN30QTreeWidgetItemIteratorPrivate8previousEPK15QTreeWidgetItem(
    QTreeWidgetItemIteratorPrivate *self,
    const QTreeWidgetItem *current) {
  return self->previous(current);
}

#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(treewidget)
