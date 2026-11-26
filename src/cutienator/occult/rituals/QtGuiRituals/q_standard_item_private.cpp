//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstandarditemmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(standarditemmodel)
#if QT_CONFIG(standarditemmodel)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstandarditemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <utility>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qstandarditemmodel.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qmimedata.h>
#include <QtCore/qiodevice.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtGui/private/qstandarditemmodel_p.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 27, as local:qstandarditemmodel.cpp:QStandardItemModelLessThan
class QStandardItemModelLessThan
{
public:
    inline QStandardItemModelLessThan()
        { }

    inline bool operator()(const std::pair<QStandardItem*, int> &l,
                           const std::pair<QStandardItem*, int> &r) const
    {
        return *(l.first) < *(r.first);
    }
};

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 40, as local:qstandarditemmodel.cpp:QStandardItemModelGreaterThan
class QStandardItemModelGreaterThan
{
public:
    inline QStandardItemModelGreaterThan()
        { }

    inline bool operator()(const std::pair<QStandardItem*, int> &l,
                           const std::pair<QStandardItem*, int> &r) const
    {
        return *(r.first) < *(l.first);
    }
};

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 163, as local:qstandarditemmodel.cpp:ByNormalizedRole
namespace {
struct ByNormalizedRole
    {
        static int normalizedRole(int role)
        {
            return role == Qt::EditRole ? Qt::DisplayRole : role;
        }

       bool operator()(const QStandardItemData& standardItemData, const std::pair<const int &, const QVariant&>& roleMapIt) const
       {
           return standardItemData.role < normalizedRole(roleMapIt.first);
       }
       bool operator()(const std::pair<const int&, const QVariant &>& roleMapIt, const QStandardItemData& standardItemData) const
       {
           return normalizedRole(roleMapIt.first) < standardItemData.role;
       }

    };
}  // namespace

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 186, as local:qstandarditemmodel.cpp:roleMapStandardItemDataTransform
namespace {
inline template<class Input, class OutputIt>
    OutputIt roleMapStandardItemDataTransform(Input first1, Input last1, OutputIt d_first)
    {
        while (first1 != last1) {
            if ((*first1).second.isValid())
                *d_first++ = QStandardItemData(*first1);
            ++first1;
        }
        return d_first;
    }
}  // namespace

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 203, as local:qstandarditemmodel.cpp:roleMapStandardItemDataUnion
namespace {
inline template<class Input1, class Input2,
             class OutputIt, class Compare>
    OutputIt roleMapStandardItemDataUnion(Input1 first1, Input1 last1,
                                          Input2 first2, Input2 last2,
                                          OutputIt d_first, Compare comp)
    {
        for (; first1 != last1; ++d_first) {
            if (first2 == last2) {
                return roleMapStandardItemDataTransform(first1, last1, d_first);
            }
            if (comp(*first2, *first1)) {
                *d_first = *first2++;
            } else {
                if ((*first1).second.isValid())
                    *d_first = QStandardItemData(*first1);
                if (!comp(*first1, *first2))
                    ++first2;
                ++first1;
            }
        }
        return std::copy(first2, last2, d_first);
    }
}  // namespace

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 551, as _ZN25QStandardItemModelPrivate11itemChangedEP13QStandardItemRK5QListIiE
inline void QStandardItemModelPrivate::itemChanged(QStandardItem *item, const QList<int> &roles)
{
    Q_Q(QStandardItemModel);
    Q_ASSERT(item);
    if (item->d_func()->parent == nullptr) {
        // Header item
        int idx = columnHeaderItems.indexOf(item);
        if (idx != -1) {
            emit q->headerDataChanged(Qt::Horizontal, idx, idx);
        } else {
            idx = rowHeaderItems.indexOf(item);
            if (idx != -1)
                emit q->headerDataChanged(Qt::Vertical, idx, idx);
        }
    } else {
        // Normal item
        const QModelIndex index = q->indexFromItem(item);
        emit q->dataChanged(index, index, roles);
    }
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 619, as _ZN25QStandardItemModelPrivate12rowsInsertedEP13QStandardItemii
inline void QStandardItemModelPrivate::rowsInserted(QStandardItem *parent,
                                             int row, int count)
{
    Q_Q(QStandardItemModel);
    if (parent == root.data())
        rowHeaderItems.insert(row, count, nullptr);
    q->endInsertRows();
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 575, as _ZN25QStandardItemModelPrivate21rowsAboutToBeInsertedEP13QStandardItemii
inline void QStandardItemModelPrivate::rowsAboutToBeInserted(QStandardItem *parent,
                                                      int start, int end)
{
    Q_Q(QStandardItemModel);
    QModelIndex index = q->indexFromItem(parent);
    q->beginInsertRows(index, start, end);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 631, as _ZN25QStandardItemModelPrivate15columnsInsertedEP13QStandardItemii
inline void QStandardItemModelPrivate::columnsInserted(QStandardItem *parent,
                                                int column, int count)
{
    Q_Q(QStandardItemModel);
    if (parent == root.data())
        columnHeaderItems.insert(column, count, nullptr);
    q->endInsertColumns();
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 586, as _ZN25QStandardItemModelPrivate24columnsAboutToBeInsertedEP13QStandardItemii
inline void QStandardItemModelPrivate::columnsAboutToBeInserted(QStandardItem *parent,
                                                         int start, int end)
{
    Q_Q(QStandardItemModel);
    QModelIndex index = q->indexFromItem(parent);
    q->beginInsertColumns(index, start, end);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 56, as _ZNK20QStandardItemPrivate8positionEv
inline std::pair<int, int> QStandardItemPrivate::position() const
{
    if (QStandardItem *par = parent) {
        int idx = par->d_func()->childIndex(q_func());
        if (idx == -1)
            return std::pair<int, int>(-1, -1);
        return std::pair<int, int>(idx / par->columnCount(), idx % par->columnCount());
    }
    // ### support header items?
    return std::pair<int, int>(-1, -1);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 71, as _ZN20QStandardItemPrivate8setChildEiiP13QStandardItemb
inline void QStandardItemPrivate::setChild(int row, int column, QStandardItem *item,
                                    bool emitChanged)
{
    Q_Q(QStandardItem);
    if (item == q) {
        qWarning("QStandardItem::setChild: Can't make an item a child of itself %p",
                 item);
        return;
    }
    if ((row < 0) || (column < 0))
        return;
    if (rows <= row)
        q->setRowCount(row + 1);
    if (columns <= column)
        q->setColumnCount(column + 1);
    int index = childIndex(row, column);
    Q_ASSERT(index != -1);
    QStandardItem *oldItem = children.at(index);
    if (item == oldItem)
        return;

    if (model && emitChanged) {
        emit model->layoutAboutToBeChanged();
    }

    if (item) {
        if (item->d_func()->parent == nullptr) {
            item->d_func()->setParentAndModel(q, model);
        } else {
            qWarning("QStandardItem::setChild: Ignoring duplicate insertion of item %p",
                     item);
            return;
        }
    }

    // setting the model to nullptr invalidates the persistent index which we want to avoid
    if (!item && oldItem)
        oldItem->d_func()->setModel(nullptr);

    children.replace(index, item);

    // since now indexFromItem() does no longer return a valid index, the persistent index
    // will not be invalidated anymore
    if (oldItem)
        oldItem->d_func()->setModel(nullptr);
    delete oldItem;

    if (item)
        item->d_func()->lastKnownIndex = index;

    if (model && emitChanged)
        emit model->layoutChanged();

    if (emitChanged && model) {
        if (item) {
            model->d_func()->itemChanged(item);
        } else {
            const QModelIndex idx = model->index(row, column, q->index());
            emit model->dataChanged(idx, idx);
        }
    }
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 152, as _ZN20QStandardItemPrivate12childDeletedEP13QStandardItem
inline void QStandardItemPrivate::childDeleted(QStandardItem *child)
{
    int index = childIndex(child);
    Q_ASSERT(index != -1);
    const auto modelIndex = child->index();
    children.replace(index, nullptr);
    emit model->dataChanged(modelIndex, modelIndex);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 356, as _ZN20QStandardItemPrivate8setModelEP18QStandardItemModel
inline void QStandardItemPrivate::setModel(QStandardItemModel *mod)
{
    if (children.isEmpty()) {
        if (model)
            model->d_func()->invalidatePersistentIndex(model->indexFromItem(q_ptr));
        model = mod;
    } else {
        QStack<QStandardItem*> stack;
        stack.push(q_ptr);
        while (!stack.isEmpty()) {
            QStandardItem *itm = stack.pop();
            if (itm->d_func()->model) {
                itm->d_func()->model->d_func()->invalidatePersistentIndex(itm->d_func()->model->indexFromItem(itm));
            }
            itm->d_func()->model = mod;
            const QList<QStandardItem*> &childList = itm->d_func()->children;
            for (int i = 0; i < childList.size(); ++i) {
                QStandardItem *chi = childList.at(i);
                if (chi)
                    stack.push(chi);
            }
        }
    }
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 138, as _ZN20QStandardItemPrivate11changeFlagsEb6QFlagsIN2Qt8ItemFlagEE
inline void QStandardItemPrivate::changeFlags(bool enable, Qt::ItemFlags f)
{
    Q_Q(QStandardItem);
    Qt::ItemFlags flags = q->flags();
    if (enable)
        flags |= f;
    else
        flags &= ~f;
    q->setFlags(flags);
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 230, as _ZN20QStandardItemPrivate11setItemDataERK4QMapIi8QVariantE
inline void QStandardItemPrivate::setItemData(const QMap<int, QVariant> &roles)
{
    Q_Q(QStandardItem);

    auto byRole = [](const QStandardItemData& item1, const QStandardItemData& item2) {
        return item1.role < item2.role;
    };

    std::sort(values.begin(), values.end(), byRole);

    /*
        Create a list of QStandardItemData that will contain the original values
        if the matching role is not contained in roles, the new value if it is and
        if the new value is an invalid QVariant, it will be removed.
    */
    QList<QStandardItemData> newValues;
    newValues.reserve(values.size());
    roleMapStandardItemDataUnion(roles.keyValueBegin(),
                                 roles.keyValueEnd(),
                                 values.cbegin(), values.cend(),
                                 std::back_inserter(newValues), ByNormalizedRole());

    if (newValues != values) {
        values.swap(newValues);
        if (model) {
            QList<int> roleKeys;
            roleKeys.reserve(roles.size() + 1);
            bool hasEditRole = false;
            bool hasDisplayRole = false;
            for (auto it = roles.keyBegin(); it != roles.keyEnd(); ++it) {
                roleKeys.push_back(*it);
                if (*it == Qt::EditRole)
                    hasEditRole = true;
                else if (*it == Qt::DisplayRole)
                    hasDisplayRole = true;
            }
            if (hasEditRole && !hasDisplayRole)
                roleKeys.push_back(Qt::DisplayRole);
            else if (!hasEditRole && hasDisplayRole)
                roleKeys.push_back(Qt::EditRole);
            model->d_func()->itemChanged(q, roleKeys);
        }
    }
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 278, as _ZNK20QStandardItemPrivate8itemDataEv
inline QMap<int, QVariant> QStandardItemPrivate::itemData() const
{
    QMap<int, QVariant> result;
    for (const auto &data : values) {
        if (data.role != Qt::StandardItemFlagsRole)
            result.insert(data.role, data.value);
    }
    return result;
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 460, as _ZN20QStandardItemPrivate10insertRowsEiiRK5QListIP13QStandardItemE
inline bool QStandardItemPrivate::insertRows(int row, int count, const QList<QStandardItem*> &items)
{
    Q_Q(QStandardItem);
    if ((count < 1) || (row < 0) || (row > rowCount()) || count == 0)
        return false;
    if (model)
        model->d_func()->rowsAboutToBeInserted(q, row, row + count - 1);
    if (rowCount() == 0) {
        children.resize(columnCount() * count);
        rows = count;
    } else {
        rows += count;
        int index = childIndex(row, 0);
        if (index != -1)
            children.insert(index, columnCount() * count, nullptr);
    }
    if (!items.isEmpty()) {
        int index = childIndex(row, 0);
        int limit = qMin(items.size(), columnCount() * count);
        for (int i = 0; i < limit; ++i) {
            QStandardItem *item = items.at(i);
            if (item) {
                if (item->d_func()->parent == nullptr) {
                    item->d_func()->setParentAndModel(q, model);
                } else {
                    qWarning("QStandardItem::insertRows: Ignoring duplicate insertion of item %p",
                             item);
                    item = nullptr;
                }
            }
            children.replace(index, item);
            if (item)
                item->d_func()->lastKnownIndex = index;
            ++index;
        }
    }
    if (model)
        model->d_func()->rowsInserted(q, row, count);
    return true;
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 428, as _ZN20QStandardItemPrivate10insertRowsEiRK5QListIP13QStandardItemE
inline bool QStandardItemPrivate::insertRows(int row, const QList<QStandardItem*> &items)
{
    Q_Q(QStandardItem);
    if ((row < 0) || (row > rowCount()) || items.isEmpty())
        return false;
    int count = items.size();
    if (model)
        model->d_func()->rowsAboutToBeInserted(q, row, row + count - 1);
    if (rowCount() == 0) {
        if (columnCount() == 0)
            q->setColumnCount(1);
        children.resize(columnCount() * count);
        rows = count;
    } else {
        rows += count;
        int index = childIndex(row, 0);
        if (index != -1)
            children.insert(index, columnCount() * count, nullptr);
    }
    for (int i = 0; i < items.size(); ++i) {
        QStandardItem *item = items.at(i);
        item->d_func()->setParentAndModel(q, model);
        int index = childIndex(i + row, 0);
        children.replace(index, item);
        if (item)
            item->d_func()->lastKnownIndex = index;
    }
    if (model)
        model->d_func()->rowsInserted(q, row, count);
    return true;
}

//  from src/gui/itemmodels/qstandarditemmodel.cpp, line 504, as _ZN20QStandardItemPrivate13insertColumnsEiiRK5QListIP13QStandardItemE
inline bool QStandardItemPrivate::insertColumns(int column, int count, const QList<QStandardItem*> &items)
{
    Q_Q(QStandardItem);
    if ((count < 1) || (column < 0) || (column > columnCount()) || count == 0)
        return false;
    if (model)
        model->d_func()->columnsAboutToBeInserted(q, column, column + count - 1);
    if (columnCount() == 0) {
        children.resize(rowCount() * count);
        columns = count;
    } else {
        columns += count;
        int index = childIndex(0, column);
        for (int row = 0; row < rowCount(); ++row) {
            children.insert(index, count, nullptr);
            index += columnCount();
        }
    }
    if (!items.isEmpty()) {
        int limit = qMin(items.size(), rowCount() * count);
        for (int i = 0; i < limit; ++i) {
            QStandardItem *item = items.at(i);
            if (item) {
                if (item->d_func()->parent == nullptr) {
                    item->d_func()->setParentAndModel(q, model);
                } else {
                    qWarning("QStandardItem::insertColumns: Ignoring duplicate insertion of item %p",
                             item);
                    item = nullptr;
                }
            }
            int r = i / count;
            int c = column + (i % count);
            int index = childIndex(r, c);
            children.replace(index, item);
            if (item)
                item->d_func()->lastKnownIndex = index;
        }
    }
    if (model)
        model->d_func()->columnsInserted(q, column, count);
    return true;
}
//  -----------------------------------------------------------------------

//  QStandardItem *QStandardItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN20QStandardItemPrivate6q_funcEv(
    QStandardItemPrivate *self) {
  return self->q_func();
}

//  const QStandardItem *QStandardItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QStandardItem *ritual_ZNK20QStandardItemPrivate6q_funcEv(
    const QStandardItemPrivate *self) {
  return self->q_func();
}

//  QStandardItemPrivate::QStandardItemPrivate()
extern "C" Q_DECL_EXPORT
QStandardItemPrivate *ritual_ZN20QStandardItemPrivateC1Ev() {
  return new QStandardItemPrivate();
}

//  int QStandardItemPrivate::childIndex(int row, int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QStandardItemPrivate10childIndexEii(
    const QStandardItemPrivate *self,
    int row,
    int column) {
  return self->childIndex(row, column);
}

//  int QStandardItemPrivate::childIndex(const QStandardItem *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QStandardItemPrivate10childIndexEPK13QStandardItem(
    const QStandardItemPrivate *self,
    const QStandardItem *child) {
  return self->childIndex(child);
}

//  std::pair<int, int> QStandardItemPrivate::position() const
extern "C" Q_DECL_EXPORT
std::pair<int, int> *ritual_ZNK20QStandardItemPrivate8positionEv(
    const QStandardItemPrivate *self) {
  return new std::pair<int, int>(self->position());
}

//  void QStandardItemPrivate::setChild(int row, int column, QStandardItem
//      *item, bool emitChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStandardItemPrivate8setChildEiiP13QStandardItemb(
    QStandardItemPrivate *self,
    int row,
    int column,
    QStandardItem *item,
    bool emitChanged) {
  self->setChild(row, column, item, emitChanged);
}

//  int QStandardItemPrivate::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QStandardItemPrivate8rowCountEv(
    const QStandardItemPrivate *self) {
  return self->rowCount();
}

//  int QStandardItemPrivate::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QStandardItemPrivate11columnCountEv(
    const QStandardItemPrivate *self) {
  return self->columnCount();
}

//  void QStandardItemPrivate::childDeleted(QStandardItem *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStandardItemPrivate12childDeletedEP13QStandardItem(
    QStandardItemPrivate *self,
    QStandardItem *child) {
  self->childDeleted(child);
}

//  void QStandardItemPrivate::setModel(QStandardItemModel *mod)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStandardItemPrivate8setModelEP18QStandardItemModel(
    QStandardItemPrivate *self,
    QStandardItemModel *mod) {
  self->setModel(mod);
}

//  void QStandardItemPrivate::setParentAndModel(QStandardItem *par,
//      QStandardItemModel *mod)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStandardItemPrivate17setParentAndModelEP13QStandardItemP18QStandardItemModel(
    QStandardItemPrivate *self,
    QStandardItem *par,
    QStandardItemModel *mod) {
  self->setParentAndModel(par, mod);
}

//  void QStandardItemPrivate::changeFlags(bool enable, Qt::ItemFlags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStandardItemPrivate11changeFlagsEb6QFlagsIN2Qt8ItemFlagEE(
    QStandardItemPrivate *self,
    bool enable,
    int f) {
  self->changeFlags(enable, QFlags<Qt::ItemFlag>::fromInt(f));
}

//  void QStandardItemPrivate::setItemData(const QMap<int, QVariant> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStandardItemPrivate11setItemDataERK4QMapIi8QVariantE(
    QStandardItemPrivate *self,
    const QMap<int, QVariant> *roles) {
  self->setItemData(*roles);
}

//  QMap<int, QVariant> QStandardItemPrivate::itemData() const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK20QStandardItemPrivate8itemDataEv(
    const QStandardItemPrivate *self) {
  return new QMap<int, QVariant>(self->itemData());
}

//  bool QStandardItemPrivate::insertRows(int row, int count, const
//      QList<QStandardItem *> &items)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStandardItemPrivate10insertRowsEiiRK5QListIP13QStandardItemE(
    QStandardItemPrivate *self,
    int row,
    int count,
    const QList<QStandardItem *> *items) {
  return self->insertRows(row, count, *items);
}

//  bool QStandardItemPrivate::insertRows(int row, const QList<QStandardItem
//      *> &items)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStandardItemPrivate10insertRowsEiRK5QListIP13QStandardItemE(
    QStandardItemPrivate *self,
    int row,
    const QList<QStandardItem *> *items) {
  return self->insertRows(row, *items);
}

//  bool QStandardItemPrivate::insertColumns(int column, int count, const
//      QList<QStandardItem *> &items)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStandardItemPrivate13insertColumnsEiiRK5QListIP13QStandardItemE(
    QStandardItemPrivate *self,
    int column,
    int count,
    const QList<QStandardItem *> *items) {
  return self->insertColumns(column, count, *items);
}

//  QStandardItemPrivate::~QStandardItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStandardItemPrivateD1Ev(QStandardItemPrivate *self) {
  delete self;
}

//  a std::pair<int, int> a ritual of QStandardItemPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStandardItemPrivate__std_pair_int_int(
    std::pair<int, int> *self) {
  delete self;
}

#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(standarditemmodel)
