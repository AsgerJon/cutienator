//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qitemselectionmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qitemselectionmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/private/qitemselectionmodel_p.h>
#include <QtCore/private/qitemselectionmodel_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 289, as local:qitemselectionmodel.cpp:rowLengthsFromRange
static void rowLengthsFromRange(const QItemSelectionRange &range, QList<std::pair<QPersistentModelIndex, uint>> &result)
{
    if (range.isValid() && range.model()) {
        const QModelIndex topLeft = range.topLeft();
        const int bottom = range.bottom();
        const uint width = range.width();
        const int column = topLeft.column();
        for (int row = topLeft.row(); row <= bottom; ++row) {
            // We don't need to keep track of ItemIsSelectable and ItemIsEnabled here. That is
            // required in indexesFromRange() because that method is called from public API
            // which requires the limitation.
            result.emplace_back(topLeft.sibling(row, column), width);
        }
    }
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 328, as local:qitemselectionmodel.cpp:qSelectionIndexes
template<typename ModelIndexContainer>
static ModelIndexContainer qSelectionIndexes(const QItemSelection &selection)
{
    ModelIndexContainer result;
    for (const auto &range : selection)
        indexesFromRange(range, result);
    return result;
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 479, as local:qitemselectionmodel.cpp:qSelectionPersistentRowLengths
static QList<std::pair<QPersistentModelIndex, uint>> qSelectionPersistentRowLengths(const QItemSelection &sel)
{
    QList<std::pair<QPersistentModelIndex, uint>> result;
    for (const QItemSelectionRange &range : sel)
        rowLengthsFromRange(range, result);
    return result;
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 964, as local:qitemselectionmodel.cpp:mergeIndexes
static QItemSelection mergeIndexes(const QList<QPersistentModelIndex> &indexes)
{
    QItemSelection colSpans;
    // merge columns
    int i = 0;
    while (i < indexes.size()) {
        const QPersistentModelIndex &tl = indexes.at(i);
        if (!tl.isValid()) {
            ++i;
            continue;
        }
        QPersistentModelIndex br = tl;
        QModelIndex brParent = br.parent();
        int brRow = br.row();
        int brColumn = br.column();
        while (++i < indexes.size()) {
            const QPersistentModelIndex &next = indexes.at(i);
            if (!next.isValid())
                continue;
            const QModelIndex nextParent = next.parent();
            const int nextRow = next.row();
            const int nextColumn = next.column();
            if ((nextParent == brParent)
                 && (nextRow == brRow)
                 && (nextColumn == brColumn + 1)) {
                br = next;
                brParent = nextParent;
                brRow = nextRow;
                brColumn = nextColumn;
            } else {
                break;
            }
        }
        colSpans.append(QItemSelectionRange(tl, br));
    }
    // merge rows
    QItemSelection rowSpans;
    i = 0;
    while (i < colSpans.size()) {
        QModelIndex tl = colSpans.at(i).topLeft();
        QModelIndex br = colSpans.at(i).bottomRight();
        QModelIndex prevTl = tl;
        while (++i < colSpans.size()) {
            QModelIndex nextTl = colSpans.at(i).topLeft();
            QModelIndex nextBr = colSpans.at(i).bottomRight();

            if (nextTl.parent() != tl.parent())
                break; // we can't merge selection ranges from different parents

            if ((nextTl.column() == prevTl.column()) && (nextBr.column() == br.column())
                && (nextTl.row() == prevTl.row() + 1) && (nextBr.row() == br.row() + 1)) {
                br = nextBr;
                prevTl = nextTl;
            } else {
                break;
            }
        }
        rowSpans.append(QItemSelectionRange(tl, br));
    }
    return rowSpans;
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 1035, as local:qitemselectionmodel.cpp:qt_PersistentModelIndexLessThan
static bool qt_PersistentModelIndexLessThan(const QPersistentModelIndex &i1, const QPersistentModelIndex &i2)
{
    const QModelIndex parent1 = i1.parent();
    const QModelIndex parent2 = i2.parent();
    return parent1 == parent2 ? i1 < i2 : parent1 < parent2;
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 594, as _ZN26QItemSelectionModelPrivateD1Ev
inline QItemSelectionModelPrivate::~QItemSelectionModelPrivate()
    = default;

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 656, as _ZNK26QItemSelectionModelPrivate15expandSelectionERK14QItemSelection6QFlagsIN19QItemSelectionModel13SelectionFlagEE
inline QItemSelection QItemSelectionModelPrivate::expandSelection(const QItemSelection &selection,
                                                           QItemSelectionModel::SelectionFlags command) const
{
    if (selection.isEmpty() && !((command & QItemSelectionModel::Rows) ||
                                 (command & QItemSelectionModel::Columns)))
        return selection;

    QItemSelection expanded;
    if (command & QItemSelectionModel::Rows) {
        for (int i = 0; i < selection.size(); ++i) {
            QModelIndex parent = selection.at(i).parent();
            int colCount = model->columnCount(parent);
            QModelIndex tl = model->index(selection.at(i).top(), 0, parent);
            QModelIndex br = model->index(selection.at(i).bottom(), colCount - 1, parent);
            //we need to merge because the same row could have already been inserted
            expanded.merge(QItemSelection(tl, br), QItemSelectionModel::Select);
        }
    }
    if (command & QItemSelectionModel::Columns) {
        for (int i = 0; i < selection.size(); ++i) {
            QModelIndex parent = selection.at(i).parent();
            int rowCount = model->rowCount(parent);
            QModelIndex tl = model->index(0, selection.at(i).left(), parent);
            QModelIndex br = model->index(rowCount - 1, selection.at(i).right(), parent);
            //we need to merge because the same column could have already been inserted
            expanded.merge(QItemSelection(tl, br), QItemSelectionModel::Select);
        }
    }
    return expanded;
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 690, as _ZN26QItemSelectionModelPrivate20rowsAboutToBeRemovedERK11QModelIndexii
inline void QItemSelectionModelPrivate::rowsAboutToBeRemoved(const QModelIndex &parent,
                                                         int start, int end)
{
    Q_Q(QItemSelectionModel);
    Q_ASSERT(start <= end);
    finalize();

    // update current index
    if (currentIndex.isValid() && parent == currentIndex.parent()
        && currentIndex.row() >= start && currentIndex.row() <= end) {
        QModelIndex old = currentIndex;
        if (start > 0) {
            // there are rows left above the change
            currentIndex = model->index(start - 1, old.column(), parent);
        } else if (model.value() && end < model->rowCount(parent) - 1) {
            // there are rows left below the change
            currentIndex = model->index(end + 1, old.column(), parent);
        } else {
            // there are no rows left in the table
            currentIndex = QModelIndex();
        }
        emit q->currentChanged(currentIndex, old);
        emit q->currentRowChanged(currentIndex, old);
        if (currentIndex.column() != old.column())
            emit q->currentColumnChanged(currentIndex, old);
    }

    QItemSelection deselected;
    QItemSelection newParts;
    bool indexesOfSelectionChanged = false;
    QItemSelection::iterator it = ranges.begin();
    while (it != ranges.end()) {
        if (it->topLeft().parent() != parent) {  // Check parents until reaching root or contained in range
            QModelIndex itParent = it->topLeft().parent();
            while (itParent.isValid() && itParent.parent() != parent)
                itParent = itParent.parent();

            if (itParent.isValid() && start <= itParent.row() && itParent.row() <= end) {
                deselected.append(*it);
                it = ranges.erase(it);
            } else {
                if (itParent.isValid() && end < itParent.row())
                    indexesOfSelectionChanged = true;
                ++it;
            }
        } else if (start <= it->bottom() && it->bottom() <= end    // Full inclusion
                   && start <= it->top() && it->top() <= end) {
            deselected.append(*it);
            it = ranges.erase(it);
        } else if (start <= it->top() && it->top() <= end) {      // Top intersection
            deselected.append(QItemSelectionRange(it->topLeft(), model->index(end, it->right(), it->parent())));
            *it = QItemSelectionRange(model->index(end + 1, it->left(), it->parent()), it->bottomRight());
            ++it;
        } else if (start <= it->bottom() && it->bottom() <= end) {    // Bottom intersection
            deselected.append(QItemSelectionRange(model->index(start, it->left(), it->parent()), it->bottomRight()));
            *it = QItemSelectionRange(it->topLeft(), model->index(start - 1, it->right(), it->parent()));
            ++it;
        } else if (it->top() < start && end < it->bottom()) { // Middle intersection
            // If the parent contains (1, 2, 3, 4, 5, 6, 7, 8) and [3, 4, 5, 6] is selected,
            // and [4, 5] is removed, we need to split [3, 4, 5, 6] into [3], [4, 5] and [6].
            // [4, 5] is appended to deselected, and [3] and [6] remain part of the selection
            // in ranges.
            const QItemSelectionRange removedRange(model->index(start, it->left(), it->parent()),
                                                    model->index(end, it->right(), it->parent()));
            deselected.append(removedRange);
            QItemSelection::split(*it, removedRange, &newParts);
            it = ranges.erase(it);
        } else if (end < it->top()) { // deleted row before selection
            indexesOfSelectionChanged = true;
            ++it;
        } else {
            ++it;
        }
    }
    ranges.append(newParts);

    if (!deselected.isEmpty() || indexesOfSelectionChanged)
        emit q->selectionChanged(QItemSelection(), deselected);
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 773, as _ZN26QItemSelectionModelPrivate23columnsAboutToBeRemovedERK11QModelIndexii
inline void QItemSelectionModelPrivate::columnsAboutToBeRemoved(const QModelIndex &parent,
                                                            int start, int end)
{
    Q_Q(QItemSelectionModel);

    // update current index
    if (currentIndex.isValid() && parent == currentIndex.parent()
        && currentIndex.column() >= start && currentIndex.column() <= end) {
        QModelIndex old = currentIndex;
        if (start > 0) {
            // there are columns to the left of the change
            currentIndex = model->index(old.row(), start - 1, parent);
        } else if (model.value() && end < model->columnCount() - 1) {
            // there are columns to the right of the change
            currentIndex = model->index(old.row(), end + 1, parent);
        } else {
            // there are no columns left in the table
            currentIndex = QModelIndex();
        }
        emit q->currentChanged(currentIndex, old);
        if (currentIndex.row() != old.row())
            emit q->currentRowChanged(currentIndex, old);
        emit q->currentColumnChanged(currentIndex, old);
    }

    // update selections
    QModelIndex tl = model->index(0, start, parent);
    QModelIndex br = model->index(model->rowCount(parent) - 1, end, parent);
    q->select(QItemSelection(tl, br), QItemSelectionModel::Deselect);
    finalize();
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 840, as _ZN26QItemSelectionModelPrivate21rowsAboutToBeInsertedERK11QModelIndexii
inline void QItemSelectionModelPrivate::rowsAboutToBeInserted(const QModelIndex &parent,
                                                          int start, int end)
{
    Q_Q(QItemSelectionModel);
    Q_UNUSED(end);
    finalize();
    QList<QItemSelectionRange> split;
    QList<QItemSelectionRange>::iterator it = ranges.begin();
    bool indexesOfSelectionChanged = false;
    for (; it != ranges.end(); ) {
        const QModelIndex &itParent = it->parent();
        if ((*it).isValid() && itParent == parent
            && (*it).top() < start && (*it).bottom() >= start) {
            QModelIndex middleRight = model->index(start - 1, (*it).right(), itParent);
            QItemSelectionRange top((*it).topLeft(), middleRight);
            QModelIndex middleLeft = model->index(start, (*it).left(), itParent);
            QItemSelectionRange bottom(middleLeft, (*it).bottomRight());
            it = ranges.erase(it);
            split.append(top);
            split.append(bottom);
        } else if ((*it).isValid() && itParent == parent      // insertion before selection
            && (*it).top() >= start) {
            indexesOfSelectionChanged = true;
            ++it;
        } else {
            ++it;
        }
    }
    ranges += split;

    if (indexesOfSelectionChanged)
        emit q->selectionChanged(QItemSelection(), QItemSelection());
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 810, as _ZN26QItemSelectionModelPrivate24columnsAboutToBeInsertedERK11QModelIndexii
inline void QItemSelectionModelPrivate::columnsAboutToBeInserted(const QModelIndex &parent,
                                                             int start, int end)
{
    Q_UNUSED(end);
    finalize();
    QList<QItemSelectionRange> split;
    QList<QItemSelectionRange>::iterator it = ranges.begin();
    for (; it != ranges.end(); ) {
        const QModelIndex &itParent = it->parent();
        if ((*it).isValid() && itParent == parent
            && (*it).left() < start && (*it).right() >= start) {
            QModelIndex bottomMiddle = model->index((*it).bottom(), start - 1, itParent);
            QItemSelectionRange left((*it).topLeft(), bottomMiddle);
            QModelIndex topMiddle = model->index((*it).top(), start, itParent);
            QItemSelectionRange right(topMiddle, (*it).bottomRight());
            it = ranges.erase(it);
            split.append(left);
            split.append(right);
        } else {
            ++it;
        }
    }
    ranges += split;
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 1131, as _ZN26QItemSelectionModelPrivate14modelDestroyedEv
inline void QItemSelectionModelPrivate::modelDestroyed()
{
    model.setValueBypassingBindings(nullptr);
    disconnectModel();
    model.notify();
}

//  from src/corelib/itemmodels/qitemselectionmodel.cpp, line 642, as _ZN26QItemSelectionModelPrivate15disconnectModelEv
inline void QItemSelectionModelPrivate::disconnectModel()
{
    for (auto &connection : connections)
        QObject::disconnect(connection);
}
//  -----------------------------------------------------------------------

//  QItemSelectionModel *QItemSelectionModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZN26QItemSelectionModelPrivate6q_funcEv(
    QItemSelectionModelPrivate *self) {
  return self->q_func();
}

//  const QItemSelectionModel *QItemSelectionModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QItemSelectionModel *ritual_ZNK26QItemSelectionModelPrivate6q_funcEv(
    const QItemSelectionModelPrivate *self) {
  return self->q_func();
}

//  QItemSelectionModelPrivate::QItemSelectionModelPrivate()
extern "C" Q_DECL_EXPORT
QItemSelectionModelPrivate *ritual_ZN26QItemSelectionModelPrivateC1Ev() {
  return new QItemSelectionModelPrivate();
}

//  QItemSelectionModelPrivate::~QItemSelectionModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivateD1Ev(
    QItemSelectionModelPrivate *self) {
  delete self;
}

//  QItemSelection QItemSelectionModelPrivate::expandSelection(const
//      QItemSelection &selection, QItemSelectionModel::SelectionFlags
//      command) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK26QItemSelectionModelPrivate15expandSelectionERK14QItemSelection6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    const QItemSelectionModelPrivate *self,
    const QItemSelection *selection,
    int command) {
  return new QItemSelection(
      self->expandSelection(
          *selection,
          QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command)));
}

//  void QItemSelectionModelPrivate::rowsAboutToBeRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate20rowsAboutToBeRemovedERK11QModelIndexii(
    QItemSelectionModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsAboutToBeRemoved(*parent, start, end);
}

//  void QItemSelectionModelPrivate::columnsAboutToBeRemoved(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate23columnsAboutToBeRemovedERK11QModelIndexii(
    QItemSelectionModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->columnsAboutToBeRemoved(*parent, start, end);
}

//  void QItemSelectionModelPrivate::rowsAboutToBeInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate21rowsAboutToBeInsertedERK11QModelIndexii(
    QItemSelectionModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsAboutToBeInserted(*parent, start, end);
}

//  void QItemSelectionModelPrivate::columnsAboutToBeInserted(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate24columnsAboutToBeInsertedERK11QModelIndexii(
    QItemSelectionModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->columnsAboutToBeInserted(*parent, start, end);
}

//  void QItemSelectionModelPrivate::modelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate14modelDestroyedEv(
    QItemSelectionModelPrivate *self) {
  self->modelDestroyed();
}

//  void QItemSelectionModelPrivate::remove(QList<QItemSelectionRange> &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate6removeER5QListI19QItemSelectionRangeE(
    QItemSelectionModelPrivate *self,
    QList<QItemSelectionRange> *r) {
  self->remove(*r);
}

//  void QItemSelectionModelPrivate::finalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate8finalizeEv(
    QItemSelectionModelPrivate *self) {
  self->finalize();
}

//  void QItemSelectionModelPrivate::setModel(QAbstractItemModel *mod)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate8setModelEP18QAbstractItemModel(
    QItemSelectionModelPrivate *self,
    QAbstractItemModel *mod) {
  self->setModel(mod);
}

//  void QItemSelectionModelPrivate::disconnectModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate15disconnectModelEv(
    QItemSelectionModelPrivate *self) {
  self->disconnectModel();
}

//  void QItemSelectionModelPrivate::modelChanged(QAbstractItemModel *mod)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QItemSelectionModelPrivate12modelChangedEP18QAbstractItemModel(
    QItemSelectionModelPrivate *self,
    QAbstractItemModel *mod) {
  self->modelChanged(mod);
}

//  size_t QItemSelectionModelPrivate::_qt_property_model_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN26QItemSelectionModelPrivate25_qt_property_model_offsetEv() {
  return QItemSelectionModelPrivate::_qt_property_model_offset();
}

#endif  // QT_CONFIG(itemmodel)
#endif  // QT_CONFIG(itemmodel)
