//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortfilterproxymodel_p_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortfilterproxymodel_p.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortfilterproxymodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#include <utility>
#include <QtCore/QModelIndex>
#include <QtCore/QHash>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmlsortercompositor_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p.h>
#include <QtQmlModels/private/qqmlfiltercompositor_p.h>
#include <QtQmlModels/private/qqmlsortercompositor_p.h>
#include <QtQmlModels/private/qqmlrolefilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 11, as _ZN20QQmlSorterCompositorC1EP7QObject
inline QQmlSorterCompositor::QQmlSorterCompositor(QObject *parent)
    : QQmlSorterBase(new QQmlSorterCompositorPrivate, parent)
{
    Q_D(QQmlSorterCompositor);
    d->init();
    // Connect the model reset with the update in the filter
    // The cache need to be updated once the model is reset with the
    // source model data.
    connect(d->m_sfpmModel, &QQmlSortFilterProxyModel::modelReset,
            this, &QQmlSorterCompositor::updateSorters);
    connect(d->m_sfpmModel, &QQmlSortFilterProxyModel::primarySorterChanged,
            this, &QQmlSorterCompositor::updateEffectiveSorters);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1594, as _ZN31QQmlSortFilterProxyModelPrivate15beginInsertRowsERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::beginInsertRows(const QModelIndex &parent, int first, int last) {
    Q_Q(QQmlSortFilterProxyModel);
    q->beginInsertRows(parent, first, last);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1602, as _ZN31QQmlSortFilterProxyModelPrivate18beginInsertColumnsERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::beginInsertColumns(const QModelIndex &parent, int first, int last) {
    Q_Q(QQmlSortFilterProxyModel);
    q->beginInsertColumns(parent, first, last);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1610, as _ZN31QQmlSortFilterProxyModelPrivate13endInsertRowsEv
inline void QQmlSortFilterProxyModelPrivate::endInsertRows() {
    Q_Q(QQmlSortFilterProxyModel);
    q->endInsertRows();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1618, as _ZN31QQmlSortFilterProxyModelPrivate16endInsertColumnsEv
inline void QQmlSortFilterProxyModelPrivate::endInsertColumns() {
    Q_Q(QQmlSortFilterProxyModel);
    q->endInsertColumns();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1626, as _ZN31QQmlSortFilterProxyModelPrivate15beginRemoveRowsERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::beginRemoveRows(const QModelIndex &parent, int first, int last) {
    Q_Q(QQmlSortFilterProxyModel);
    q->beginRemoveRows(parent, first, last);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1634, as _ZN31QQmlSortFilterProxyModelPrivate18beginRemoveColumnsERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::beginRemoveColumns(const QModelIndex &parent, int first, int last) {
    Q_Q(QQmlSortFilterProxyModel);
    q->beginRemoveColumns(parent, first, last);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1642, as _ZN31QQmlSortFilterProxyModelPrivate13endRemoveRowsEv
inline void QQmlSortFilterProxyModelPrivate::endRemoveRows() {
    Q_Q(QQmlSortFilterProxyModel);
    q->endRemoveRows();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1650, as _ZN31QQmlSortFilterProxyModelPrivate16endRemoveColumnsEv
inline void QQmlSortFilterProxyModelPrivate::endRemoveColumns() {
    Q_Q(QQmlSortFilterProxyModel);
    q->endRemoveColumns();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1658, as _ZN31QQmlSortFilterProxyModelPrivate15beginResetModelEv
inline void QQmlSortFilterProxyModelPrivate::beginResetModel() {
    Q_Q(QQmlSortFilterProxyModel);
    q->beginResetModel();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1666, as _ZN31QQmlSortFilterProxyModelPrivate13endResetModelEv
inline void QQmlSortFilterProxyModelPrivate::endResetModel() {
    Q_Q(QQmlSortFilterProxyModel);
    q->endResetModel();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1557, as _ZNK31QQmlSortFilterProxyModelPrivate24filterAcceptsRowInternalEiRK11QModelIndex
inline bool QQmlSortFilterProxyModelPrivate::filterAcceptsRowInternal(int row, const QModelIndex &sourceIndex) const
{
    Q_Q(const QQmlSortFilterProxyModel);
    const bool retVal = (q->filterAcceptsRow(row, sourceIndex) ||
                         (m_autoAcceptChildRows && recursiveParentAcceptsRow(sourceIndex)) ||
                         (m_recursiveFiltering && recursiveChildAcceptsRow(row, sourceIndex)));
    return retVal;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1674, as _ZNK31QQmlSortFilterProxyModelPrivate16filterAcceptsRowEiRK11QModelIndex
inline bool QQmlSortFilterProxyModelPrivate::filterAcceptsRow(int source_row, const QModelIndex &source_parent) const {
    return q_func()->filterAcceptsRow(source_row, source_parent);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1569, as _ZNK31QQmlSortFilterProxyModelPrivate27filterAcceptsColumnInternalEiRK11QModelIndex
inline bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumnInternal(int row, const QModelIndex &sourceIndex) const
{
    Q_Q(const QQmlSortFilterProxyModel);
    return q->filterAcceptsColumn(row, sourceIndex);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1681, as _ZNK31QQmlSortFilterProxyModelPrivate19filterAcceptsColumnEiRK11QModelIndex
inline bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumn(int source_column, const QModelIndex &source_parent) const {
    return q_func()->filterAcceptsColumn(source_column, source_parent);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1688, as _ZNK31QQmlSortFilterProxyModelPrivate8lessThanERK11QModelIndexS2_
inline bool QQmlSortFilterProxyModelPrivate::lessThan(const QModelIndex &source_left, const QModelIndex &source_right) const {
    return q_func()->lessThan(source_left, source_right);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 145, as _ZN20QQmlSorterCompositor13updateSortersEv
inline void QQmlSorterCompositor::updateSorters()
{
    Q_D(QQmlSorterCompositor);
    // Update sorters that has dependency with the model data to determine
    // whether it needs to be included or not
    for (auto &sorter: d->m_sorters)
        sorter->update(d->m_sfpmModel);
    updateCache();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 125, as _ZN20QQmlSorterCompositor22updateEffectiveSortersEv
inline void QQmlSorterCompositor::updateEffectiveSorters()
{
    Q_D(QQmlSorterCompositor);

    if (!d->m_primarySorter || !d->m_primarySorter->enabled()) {
        updateCache();
        return;
    }

    QList<QQmlSorterBase *> sorters;
    sorters.append(d->m_primarySorter);
    std::copy_if(d->m_effectiveSorters.constBegin(), d->m_effectiveSorters.constEnd(),
                 std::back_inserter(sorters), [d](QQmlSorterBase *sorter){
                     // Consider only the filters that are enabled and exclude the primary
                     // sorter as its already added to the list
                     return (sorter != d->m_primarySorter);
                 });
    d->m_effectiveSorters = sorters;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 30, as _ZN27QQmlSorterCompositorPrivate4initEv
inline void QQmlSorterCompositorPrivate::init()
{
    Q_Q(QQmlSorterCompositor);
    m_sfpmModel = qobject_cast<QQmlSortFilterProxyModel *>(q->parent());
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 155, as _ZN20QQmlSorterCompositor11updateCacheEv
inline void QQmlSorterCompositor::updateCache()
{
    Q_D(QQmlSorterCompositor);
    // Clear the existing cache
    d->m_effectiveSorters.clear();
    if (d->m_sfpmModel && d->m_sfpmModel->sourceModel()) {
        // Sort the filter according to their priority
        QList<QQmlSorterBase *> sorters = d->m_sorters;
        std::stable_sort(sorters.begin(), sorters.end(),
                [](QQmlSorterBase *sorterLeft, QQmlSorterBase *sorterRight) {
                        return sorterLeft->priority() < sorterRight->priority();
                });
        // Cache only the filters that are need to be evaluated (in order)
        std::copy_if(sorters.begin(), sorters.end(), std::back_inserter(d->m_effectiveSorters),
                [](QQmlSorterBase *sorter) { return sorter->enabled(); });
        // If there is no primary sorter set by the user explicitly, reset the
        // primary sorter according to the sorters in the lists
        d->resetPrimarySorter();
    }
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 210, as _ZN27QQmlSorterCompositorPrivate18resetPrimarySorterEv
inline void QQmlSorterCompositorPrivate::resetPrimarySorter()
{
    if (!m_primarySorter) {
        if (!m_effectiveSorters.isEmpty()) {
            // Set the primary sort column and its order to the proxy model
            const auto *sorter = m_effectiveSorters.at(0);
            m_sfpmModel->setPrimarySortOrder(sorter->sortOrder());
            m_sfpmModel->setPrimarySortColumn(sorter->column());
        } else {
            // By default reset the  sort order to ascending order and the
            // column to 0
            m_sfpmModel->setPrimarySortOrder(Qt::AscendingOrder);
            m_sfpmModel->setPrimarySortColumn(0);
        }
    }
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 839, as _ZN31QQmlSortFilterProxyModelPrivate4initEv
inline void QQmlSortFilterProxyModelPrivate::init()
{
    Q_Q(QQmlSortFilterProxyModel);
    m_filters = new QQmlFilterCompositor(q);
    QObject::connect(q, &QQmlSortFilterProxyModel::filtersChanged,
                     q, &QQmlSortFilterProxyModel::invalidateFilter);
    m_sorters = new QQmlSorterCompositor(q);
    QObject::connect(q, &QQmlSortFilterProxyModel::sortersChanged,
                     q, &QQmlSortFilterProxyModel::invalidateSorter);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1529, as _ZNK31QQmlSortFilterProxyModelPrivate29containRoleForRecursiveFilterERK5QListIiE
inline bool QQmlSortFilterProxyModelPrivate::containRoleForRecursiveFilter(const QList<int> &roles) const
{
    if (!model || roles.isEmpty())
        return false;
    // Get role names for the provided roles (roles arg.)
    const QHash<int, QByteArray> &roleNames = model->roleNames();
    QList<QString> filterRoles;
    std::for_each(roles.constBegin(), roles.constEnd(), [&roleNames, &filterRoles](const int role){
        if (roleNames.contains(role))
            filterRoles.append(QString::fromUtf8(roleNames[role]));
    });

    // Check if the configured role filter matches with the provided roles
    bool filterRoleConfigured = false;
    if (!filterRoles.isEmpty() && (m_filters && m_filters->filters().isEmpty())) {
        const QList<QQmlFilterBase *> proxyFilters = m_filters->filters();
        filterRoleConfigured = std::any_of(proxyFilters.constBegin(), proxyFilters.constEnd(), [&filterRoles](QQmlFilterBase* filterComp) {
            if (const auto *roleFilter = qobject_cast<QQmlRoleFilter *>(filterComp))
                return filterRoles.contains(roleFilter->roleName());
            return true;
        });
    }
    return m_recursiveFiltering && filterRoleConfigured;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 863, as _ZNK31QQmlSortFilterProxyModelPrivate25recursiveParentAcceptsRowERK11QModelIndex
inline bool QQmlSortFilterProxyModelPrivate::recursiveParentAcceptsRow(const QModelIndex &source_parent) const
{
    Q_Q(const QQmlSortFilterProxyModel);
    if (source_parent.isValid()) {
        const QModelIndex index = source_parent.parent();
        if (q->filterAcceptsRow(source_parent.row(), index))
            return true;
        return recursiveParentAcceptsRow(index);
    }
    return false;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 875, as _ZNK31QQmlSortFilterProxyModelPrivate24recursiveChildAcceptsRowEiRK11QModelIndex
inline bool QQmlSortFilterProxyModelPrivate::recursiveChildAcceptsRow(int source_row, const QModelIndex &source_parent) const
{
    Q_Q(const QQmlSortFilterProxyModel);
    const QModelIndex index = model->index(source_row, 0, source_parent);
    const int count = model->rowCount(index);
    for (int i = 0; i < count; ++i) {
        if (q->filterAcceptsRow(i, index))
            return true;
        if (recursiveChildAcceptsRow(i, index))
            return true;
    }
    return false;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1040, as _ZNK31QQmlSortFilterProxyModelPrivate12needsReorderERK5QListIiERK11QModelIndex
inline bool QQmlSortFilterProxyModelPrivate::needsReorder(const QList<int> &source_rows, const QModelIndex &source_parent) const
{
    Q_Q(const QQmlSortFilterProxyModel);
    Q_ASSERT(m_primarySortColumn != -1);
    const int proxyRowCount = q->rowCount(source_to_proxy(source_parent));
    // If any modified proxy row no longer passes lessThan(previous, current)
    // or lessThan(current, next) then we need to reorder.
    return std::any_of(source_rows.begin(), source_rows.end(),
                       [this, q, proxyRowCount, source_parent](int sourceRow) -> bool {
                           const QModelIndex sourceIndex = model->index(sourceRow, m_primarySortColumn, source_parent);
                           const QModelIndex proxyIndex = source_to_proxy(sourceIndex);
                           Q_ASSERT(proxyIndex.isValid()); // caller ensured source_rows were not filtered out
                           if (proxyIndex.row() > 0) {
                               const QModelIndex prevProxyIndex = q->sibling(proxyIndex.row() - 1, m_proxySortColumn, proxyIndex);
                               const QModelIndex prevSourceIndex = proxy_to_source(prevProxyIndex);
                               if (m_sortOrder == Qt::AscendingOrder ? q->lessThan(sourceIndex, prevSourceIndex) : q->lessThan(prevSourceIndex, sourceIndex))
                                   return true;
                           }
                           if (proxyIndex.row() < proxyRowCount - 1) {
                               const QModelIndex nextProxyIndex = q->sibling(proxyIndex.row() + 1, m_proxySortColumn, proxyIndex);
                               const QModelIndex nextSourceIndex = proxy_to_source(nextProxyIndex);
                               if (m_sortOrder == Qt::AscendingOrder ? q->lessThan(nextSourceIndex, sourceIndex) : q->lessThan(sourceIndex, nextSourceIndex))
                                   return true;
                           }
                           return false;
                       });
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 895, as _ZN31QQmlSortFilterProxyModelPrivate19updatePrimaryColumnEv
inline bool QQmlSortFilterProxyModelPrivate::updatePrimaryColumn()
{
    int old_primayColumn = m_primarySortColumn;

    if (m_proxySortColumn == -1) {
        m_primarySortColumn = -1;
    } else {
        // We cannot use index mapping here because in case of a still-empty
        // proxy model there's no valid proxy index we could map to source.
        // So always use the root mapping directly instead.
        QSortFilterProxyModelHelper::Mapping *m = create_mapping(QModelIndex()).value();
        if (m_proxySortColumn < m->source_columns.size())
            m_primarySortColumn = m->source_columns.at(m_proxySortColumn);
        else
            m_primarySortColumn = -1;
    }

    return old_primayColumn != m_primarySortColumn;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 921, as _ZNK31QQmlSortFilterProxyModelPrivate21findPrimarySortColumnEv
inline int QQmlSortFilterProxyModelPrivate::findPrimarySortColumn() const
{
    if (m_proxySortColumn == -1)
        return -1;

    const QModelIndex rootIndex;
    const int source_cols = model->columnCount();
    int accepted_columns = -1;

    Q_Q(const QQmlSortFilterProxyModel);
    for (int i = 0; i < source_cols; ++i) {
        if (q->filterAcceptsColumn(i, rootIndex)) {
            if (++accepted_columns == m_proxySortColumn)
                return i;
        }
    }

    return -1;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1068, as _ZN31QQmlSortFilterProxyModelPrivate20_q_sourceDataChangedERK11QModelIndexS2_RK5QListIiE
inline void QQmlSortFilterProxyModelPrivate::_q_sourceDataChanged(const QModelIndex &source_top_left,
                                                            const QModelIndex &source_bottom_right,
                                                            const QList<int> &roles)
{
    Q_Q(QQmlSortFilterProxyModel);
    if (!source_top_left.isValid() || !source_bottom_right.isValid())
        return;

    std::vector<QSortFilterProxyModelDataChanged> data_changed_list;
    data_changed_list.emplace_back(source_top_left, source_bottom_right);

    // Do check parents if the filter role have changed and we are recursive
    if (containRoleForRecursiveFilter(roles)) {
        QModelIndex source_parent = source_top_left.parent();
        while (source_parent.isValid()) {
            data_changed_list.emplace_back(source_parent, source_parent);
            source_parent = source_parent.parent();
        }
    }

    for (const QSortFilterProxyModelDataChanged &data_changed : data_changed_list) {
        const QModelIndex &source_top_left = data_changed.topLeft;
        const QModelIndex &source_bottom_right = data_changed.bottomRight;
        const QModelIndex source_parent = source_top_left.parent();

        bool change_in_unmapped_parent = false;
        QSortFilterProxyModelHelper::IndexMap::const_iterator it = source_index_mapping.constFind(source_parent);
        if (it == source_index_mapping.constEnd()) {
            // We don't have mapping for this index, so we cannot know how
            // things changed (in case the change affects filtering) in order
            // to forward the change correctly.
            // But we can at least forward the signal "as is", if the row isn't
            // filtered out, this is better than nothing.
            it = create_mapping_recursive(source_parent);
            if (it == source_index_mapping.constEnd())
                continue;
            change_in_unmapped_parent = true;
        }

        QSortFilterProxyModelHelper::Mapping *m = it.value();

        // Figure out how the source changes affect us
        QList<int> source_rows_remove;
        QList<int> source_rows_insert;
        QList<int> source_rows_change;
        QList<int> source_rows_resort;
        int end = qMin(source_bottom_right.row(), m->proxy_rows.size() - 1);
        for (int source_row = source_top_left.row(); source_row <= end; ++source_row) {
            if (m_dynamicSortFilter && !change_in_unmapped_parent) {
                if (m->proxy_rows.at(source_row) != -1) {
                    if (!filterAcceptsRowInternal(source_row, source_parent)) {
                        // This source row no longer satisfies the filter, so
                        // it must be removed
                        source_rows_remove.append(source_row);
                    } else if (m_primarySortColumn >= source_top_left.column() && m_primarySortColumn <= source_bottom_right.column()) {
                        // This source row has changed in a way that may affect
                        // sorted order
                        source_rows_resort.append(source_row);
                    } else {
                        // This row has simply changed, without affecting
                        // filtering nor sorting
                        source_rows_change.append(source_row);
                    }
                } else {
                    if (!m_itemsBeingRemoved.contains(source_parent, source_row) && filterAcceptsRowInternal(source_row, source_parent)) {
                        // This source row now satisfies the filter, so it must
                        // be added
                        source_rows_insert.append(source_row);
                    }
                }
            } else {
                if (m->proxy_rows.at(source_row) != -1)
                    source_rows_change.append(source_row);
            }
        }

        if (!source_rows_remove.isEmpty()) {
            remove_source_items(m->proxy_rows, m->source_rows,
                                source_rows_remove, source_parent, QSortFilterProxyModelHelper::Direction::Rows);
            QSet<int> source_rows_remove_set = qListToSet(source_rows_remove);
            QList<QModelIndex>::iterator childIt = m->mapped_children.end();
            while (childIt != m->mapped_children.begin()) {
                --childIt;
                const QModelIndex source_child_index = *childIt;
                if (source_rows_remove_set.contains(source_child_index.row())) {
                    childIt = m->mapped_children.erase(childIt);
                    remove_from_mapping(source_child_index);
                }
            }
        }

        if (!source_rows_resort.isEmpty()) {
            if (needsReorder(source_rows_resort, source_parent)) {
                // Re-sort the rows of this level
                QList<QPersistentModelIndex> parents;
                parents << q->mapFromSource(source_parent);
                emit q->layoutAboutToBeChanged(parents, QAbstractItemModel::VerticalSortHint);
                QModelIndexPairList source_indexes = store_persistent_indexes();
                remove_source_items(m->proxy_rows, m->source_rows, source_rows_resort,
                                    source_parent, QSortFilterProxyModelHelper::Direction::Rows, false);
                sort_source_rows(source_rows_resort, source_parent);
                insert_source_items(m->proxy_rows, m->source_rows, source_rows_resort,
                                    source_parent, QSortFilterProxyModelHelper::Direction::Rows, false);
                update_persistent_indexes(source_indexes);
                emit q->layoutChanged(parents, QAbstractItemModel::VerticalSortHint);
            }
            // Make sure we also emit dataChanged for the rows
            source_rows_change += source_rows_resort;
        }

        if (!source_rows_change.isEmpty()) {
            // Find the proxy row range
            int proxy_start_row;
            int proxy_end_row;
            proxy_item_range(m->proxy_rows, source_rows_change,
                             proxy_start_row, proxy_end_row);
            // ### Find the proxy column range also
            if (proxy_end_row >= 0) {
                // the row was accepted, but some columns might still be
                // filtered out
                int source_left_column = source_top_left.column();
                while (source_left_column < source_bottom_right.column()
                       && m->proxy_columns.at(source_left_column) == -1)
                    ++source_left_column;
                if (m->proxy_columns.at(source_left_column) != -1) {
                    const QModelIndex proxy_top_left = createIndex(
                            proxy_start_row, m->proxy_columns.at(source_left_column), it);
                    int source_right_column = source_bottom_right.column();
                    while (source_right_column > source_top_left.column()
                           && m->proxy_columns.at(source_right_column) == -1)
                        --source_right_column;
                    if (m->proxy_columns.at(source_right_column) != -1) {
                        const QModelIndex proxy_bottom_right = createIndex(
                                proxy_end_row, m->proxy_columns.at(source_right_column), it);
                        emit q->dataChanged(proxy_top_left, proxy_bottom_right, roles);
                    }
                }
            }
        }

        if (!source_rows_insert.isEmpty()) {
            sort_source_rows(source_rows_insert, source_parent);
            insert_source_items(m->proxy_rows, m->source_rows,
                                source_rows_insert, source_parent, QSortFilterProxyModelHelper::Direction::Rows);
        }
    }
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1216, as _ZN31QQmlSortFilterProxyModelPrivate26_q_sourceHeaderDataChangedEN2Qt11OrientationEii
inline void QQmlSortFilterProxyModelPrivate::_q_sourceHeaderDataChanged(Qt::Orientation orientation,
                                                                  int start, int end)
{
    Q_ASSERT(start <= end);

    Q_Q(QQmlSortFilterProxyModel);
    QSortFilterProxyModelHelper::Mapping *m = create_mapping(QModelIndex()).value();

    const QList<int> &source_to_proxy = (orientation == Qt::Vertical) ? m->proxy_rows : m->proxy_columns;

    QList<int> proxy_positions;
    proxy_positions.reserve(end - start + 1);
    {
        Q_ASSERT(source_to_proxy.size() > end);
        QList<int>::const_iterator it = source_to_proxy.constBegin() + start;
        const QList<int>::const_iterator endIt = source_to_proxy.constBegin() + end + 1;
        for ( ; it != endIt; ++it) {
            if (*it != -1)
                proxy_positions.push_back(*it);
        }
    }

    std::sort(proxy_positions.begin(), proxy_positions.end());

    int last_index = 0;
    const int numItems = proxy_positions.size();
    while (last_index < numItems) {
        const int proxyStart = proxy_positions.at(last_index);
        int proxyEnd = proxyStart;
        ++last_index;
        for (int i = last_index; i < numItems; ++i) {
            if (proxy_positions.at(i) == proxyEnd + 1) {
                ++last_index;
                ++proxyEnd;
            } else {
                break;
            }
        }
        emit q->headerDataChanged(orientation, proxyStart, proxyEnd);
    }
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1258, as _ZN31QQmlSortFilterProxyModelPrivate23_q_sourceAboutToBeResetEv
inline void QQmlSortFilterProxyModelPrivate::_q_sourceAboutToBeReset()
{
    Q_Q(QQmlSortFilterProxyModel);
    q->beginResetModel();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1264, as _ZN31QQmlSortFilterProxyModelPrivate14_q_sourceResetEv
inline void QQmlSortFilterProxyModelPrivate::_q_sourceReset()
{
    Q_Q(QQmlSortFilterProxyModel);
    invalidatePersistentIndexes();
    _q_clearMapping();
    // All internal structures are deleted in clear()
    q->endResetModel();
    if (updatePrimaryColumn() && m_dynamicSortFilter)
        sort();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 850, as _ZN31QQmlSortFilterProxyModelPrivate15_q_clearMappingEv
inline void QQmlSortFilterProxyModelPrivate::_q_clearMapping()
{
    // store the persistent indexes
    QModelIndexPairList source_indexes = store_persistent_indexes();

    clearSourceIndexMapping();
    if (m_dynamicSortFilter)
        m_primarySortColumn = findPrimarySortColumn();

    // update the persistent indexes
    update_persistent_indexes(source_indexes);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1275, as _ZN31QQmlSortFilterProxyModelPrivate31_q_sourceLayoutAboutToBeChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE
inline void QQmlSortFilterProxyModelPrivate::_q_sourceLayoutAboutToBeChanged(const QList<QPersistentModelIndex> &sourceParents, QAbstractItemModel::LayoutChangeHint hint)
{
    Q_Q(QQmlSortFilterProxyModel);
    Q_UNUSED(hint); // We can't forward Hint because we might filter additional rows or columns
    m_savedPersistentIndexes.clear();

    m_savedLayoutChangeParents.clear();
    for (const QPersistentModelIndex &parent : sourceParents) {
        if (!parent.isValid()) {
            m_savedLayoutChangeParents << QPersistentModelIndex();
            continue;
        }
        const QModelIndex mappedParent = q->mapFromSource(parent);
        // Might be filtered out.
        if (mappedParent.isValid())
            m_savedLayoutChangeParents << mappedParent;
    }

    // All parents filtered out.
    if (!sourceParents.isEmpty() && m_savedLayoutChangeParents.isEmpty())
        return;

    emit q->layoutAboutToBeChanged(m_savedLayoutChangeParents);
    if (persistent.indexes.isEmpty())
        return;

    m_savedPersistentIndexes = store_persistent_indexes();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1304, as _ZN31QQmlSortFilterProxyModelPrivate22_q_sourceLayoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE
inline void QQmlSortFilterProxyModelPrivate::_q_sourceLayoutChanged(const QList<QPersistentModelIndex> &sourceParents, QAbstractItemModel::LayoutChangeHint hint)
{
    Q_Q(QQmlSortFilterProxyModel);
    Q_UNUSED(hint); // We can't forward Hint because we might filter additional rows or columns

    if (!sourceParents.isEmpty() && m_savedLayoutChangeParents.isEmpty())
        return;

    // Optimize: We only actually have to clear the mapping related to the
    // contents of sourceParents, not everything.
    clearSourceIndexMapping();

    update_persistent_indexes(m_savedPersistentIndexes);
    m_savedPersistentIndexes.clear();

    if (m_dynamicSortFilter)
        m_primarySortColumn = findPrimarySortColumn();

    emit q->layoutChanged(m_savedLayoutChangeParents);
    m_savedLayoutChangeParents.clear();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1326, as _ZN31QQmlSortFilterProxyModelPrivate30_q_sourceRowsAboutToBeInsertedERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeInserted(
        const QModelIndex &source_parent, int start, int end)
{
    Q_UNUSED(start);
    Q_UNUSED(end);

    const bool toplevel = !source_parent.isValid();
    const bool recursive_accepted = m_recursiveFiltering && !toplevel && filterAcceptsRowInternal(source_parent.row(), source_parent.parent());
    // Force the creation of a mapping now, even if it's empty.
    // We need it because the proxy can be accessed at the moment it emits
    // rowsAboutToBeInserted in insert_source_items
    if (!m_recursiveFiltering || toplevel || recursive_accepted) {
        if (can_create_mapping(source_parent))
            create_mapping(source_parent);
        if (m_recursiveFiltering)
            m_completeInsert = true;
    } else {
        // The row could have been rejected or the parent might be not yet
        // known... let's try to discover it
        QModelIndex top_source_parent = source_parent;
        QModelIndex parent = source_parent.parent();
        QModelIndex grandParent = parent.parent();

        while (parent.isValid() && !filterAcceptsRowInternal(parent.row(), grandParent)) {
            top_source_parent = parent;
            parent = grandParent;
            grandParent = parent.parent();
        }

        m_lastTopSource = top_source_parent;
    }
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1359, as _ZN31QQmlSortFilterProxyModelPrivate21_q_sourceRowsInsertedERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::_q_sourceRowsInserted(
        const QModelIndex &source_parent, int start, int end)
{
    if (!m_recursiveFiltering || m_completeInsert) {
        if (m_recursiveFiltering)
            m_completeInsert = false;
        source_items_inserted(source_parent, start, end, QSortFilterProxyModelHelper::Direction::Rows);
        if (updatePrimaryColumn() && m_dynamicSortFilter) //previous call to updatePrimaryColumn may fail if the model has no column.
            sort(); // now it should succeed so we need to make sure to sort again
        return;
    }
    if (m_recursiveFiltering) {
        bool accept = false;
        for (int row = start; row <= end; ++row) {
            if (filterAcceptsRowInternal(row, source_parent)) {
                accept = true;
                break;
            }
        }
        if (!accept) // the new rows have no descendants that match the filter, filter them out.
            return;
        // m_lastTopSource should now become visible
        _q_sourceDataChanged(m_lastTopSource, m_lastTopSource, QList<int>());
    }
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1385, as _ZN31QQmlSortFilterProxyModelPrivate29_q_sourceRowsAboutToBeRemovedERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeRemoved(
        const QModelIndex &source_parent, int start, int end)
{
    m_itemsBeingRemoved = QRowsRemoval(source_parent, start, end);
    source_items_about_to_be_removed(source_parent, start, end,
                                     QSortFilterProxyModelHelper::Direction::Rows);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1393, as _ZN31QQmlSortFilterProxyModelPrivate20_q_sourceRowsRemovedERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::_q_sourceRowsRemoved(
        const QModelIndex &source_parent, int start, int end)
{
    m_itemsBeingRemoved = QRowsRemoval();
    source_items_removed(source_parent, start, end, QSortFilterProxyModelHelper::Direction::Rows);

    if (m_recursiveFiltering) {
        // Find out if removing this visible row means that some ascendant
        // row can now be hidden.
        // We go up until we find a row that should still be visible
        // and then make QSFPM re-evaluate the last one we saw before that,
        // to hide it.
        QModelIndex to_hide;
        QModelIndex source_ascendant = source_parent;

        while (source_ascendant.isValid()) {
            if (filterAcceptsRowInternal(source_ascendant.row(), source_ascendant.parent()))
                break;

            to_hide = source_ascendant;
            source_ascendant = source_ascendant.parent();
        }

        if (to_hide.isValid())
            _q_sourceDataChanged(to_hide, to_hide, QList<int>());
    }
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1421, as _ZN31QQmlSortFilterProxyModelPrivate27_q_sourceRowsAboutToBeMovedERK11QModelIndexiiS2_i
inline void QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeMoved(
        const QModelIndex &sourceParent, int /* sourceStart */, int /* sourceEnd */, const QModelIndex &destParent, int /* dest */)
{
    // Because rows which are contiguous in the source model might not be
    // contiguous in the proxy due to sorting, the best thing we can do here is
    // be specific about what parents are having their children changed.
    // Optimize: Emit move signals if the proxy is not sorted. Will need to
    // account for rows being filtered out though.
    QList<QPersistentModelIndex> parents;
    parents << sourceParent;
    if (sourceParent != destParent)
        parents << destParent;
    _q_sourceLayoutAboutToBeChanged(parents, QAbstractItemModel::NoLayoutChangeHint);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1436, as _ZN31QQmlSortFilterProxyModelPrivate18_q_sourceRowsMovedERK11QModelIndexiiS2_i
inline void QQmlSortFilterProxyModelPrivate::_q_sourceRowsMoved(
        const QModelIndex &sourceParent, int /* sourceStart */, int /* sourceEnd */, const QModelIndex &destParent, int /* dest */)
{
    QList<QPersistentModelIndex> parents;
    parents << sourceParent;
    if (sourceParent != destParent)
        parents << destParent;
    _q_sourceLayoutChanged(parents, QAbstractItemModel::NoLayoutChangeHint);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1446, as _ZN31QQmlSortFilterProxyModelPrivate33_q_sourceColumnsAboutToBeInsertedERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeInserted(
        const QModelIndex &source_parent, int start, int end)
{
    Q_UNUSED(start);
    Q_UNUSED(end);
    // Force the creation of a mapping now, even if it's empty.
    // We need it because the proxy can be accessed at the moment it emits
    // columnsAboutToBeInserted in insert_source_items
    if (can_create_mapping(source_parent))
        create_mapping(source_parent);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1458, as _ZN31QQmlSortFilterProxyModelPrivate24_q_sourceColumnsInsertedERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsInserted(
        const QModelIndex &source_parent, int start, int end)
{
    Q_Q(const QQmlSortFilterProxyModel);
    source_items_inserted(source_parent, start, end, QSortFilterProxyModelHelper::Direction::Columns);

    if (source_parent.isValid())
        return; //we sort according to the root column only
    if (m_primarySortColumn == -1) {
        //we update the primayColumn depending on the m_proxySortColumn
        if (updatePrimaryColumn() && m_dynamicSortFilter)
            sort();
    } else {
        if (start <= m_primarySortColumn)
            m_primarySortColumn += end - start + 1;

        m_proxySortColumn = q->mapFromSource(model->index(0,m_primarySortColumn, source_parent)).column();
    }
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1478, as _ZN31QQmlSortFilterProxyModelPrivate32_q_sourceColumnsAboutToBeRemovedERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeRemoved(
        const QModelIndex &source_parent, int start, int end)
{
    source_items_about_to_be_removed(source_parent, start, end,
                                     QSortFilterProxyModelHelper::Direction::Columns);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1485, as _ZN31QQmlSortFilterProxyModelPrivate23_q_sourceColumnsRemovedERK11QModelIndexii
inline void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsRemoved(
        const QModelIndex &source_parent, int start, int end)
{
    Q_Q(const QQmlSortFilterProxyModel);
    source_items_removed(source_parent, start, end, QSortFilterProxyModelHelper::Direction::Columns);

    if (source_parent.isValid())
        return; //we sort according to the root column only
    if (start <= m_primarySortColumn) {
        if (end < m_primarySortColumn)
            m_primarySortColumn -= end - start + 1;
        else
            m_primarySortColumn = -1;
    }

    if (m_primarySortColumn >= 0)
        m_proxySortColumn = q->mapFromSource(model->index(0,m_primarySortColumn, source_parent)).column();
    else
        m_proxySortColumn = -1;
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1506, as _ZN31QQmlSortFilterProxyModelPrivate30_q_sourceColumnsAboutToBeMovedERK11QModelIndexiiS2_i
inline void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeMoved(
        const QModelIndex &sourceParent, int /* sourceStart */, int /* sourceEnd */, const QModelIndex &destParent, int /* dest */)
{
    QList<QPersistentModelIndex> parents;
    parents << sourceParent;
    if (sourceParent != destParent)
        parents << destParent;
    _q_sourceLayoutAboutToBeChanged(parents, QAbstractItemModel::NoLayoutChangeHint);
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/qqmlsortfilterproxymodel.cpp, line 1516, as _ZN31QQmlSortFilterProxyModelPrivate21_q_sourceColumnsMovedERK11QModelIndexiiS2_i
inline void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsMoved(
        const QModelIndex &sourceParent, int /* sourceStart */, int /* sourceEnd */, const QModelIndex &destParent, int /* dest */)
{
    QList<QPersistentModelIndex> parents;
    parents << sourceParent;
    if (sourceParent != destParent)
        parents << destParent;
    _q_sourceLayoutChanged(parents, QAbstractItemModel::NoLayoutChangeHint);
}
//  -----------------------------------------------------------------------

//  A QQmlSortFilterProxyModelPrivate that Python can take functions over in. Every QQmlSortFilterProxyModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall0)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall1)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall2)(const void *, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall3)(const void *, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall4)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall5)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall6)(const void *, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall7)(const void *, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall8)(const void *, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall9)(const void *, int *);
typedef void * (*CuteQQmlSortFilterProxyModelPrivateCall10)(const void *, int *);
typedef bool (*CuteQQmlSortFilterProxyModelPrivateCall11)(const void *, int, const QModelIndex *, int *);
typedef bool (*CuteQQmlSortFilterProxyModelPrivateCall12)(const void *, int, const QModelIndex *, int *);
typedef bool (*CuteQQmlSortFilterProxyModelPrivateCall13)(const void *, int, const QModelIndex *, int *);
typedef bool (*CuteQQmlSortFilterProxyModelPrivateCall14)(const void *, int, const QModelIndex *, int *);
typedef bool (*CuteQQmlSortFilterProxyModelPrivateCall15)(const void *, const QModelIndex *, const QModelIndex *, int *);
#if QT_CONFIG(proxymodel)
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall16)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall17)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall18)(const void *, int, const QModelIndex *, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall19)(const void *, const QModelIndex *, int, int, int, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall20)(const void *, const QModelIndex *, int, int, int, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall21)(const void *, const QModelIndex *, int, int, int, int *);
typedef void (*CuteQQmlSortFilterProxyModelPrivateCall22)(const void *, int *);
class CuteQQmlSortFilterProxyModelPrivate : public QQmlSortFilterProxyModelPrivate {
public:
  using QQmlSortFilterProxyModelPrivate::QQmlSortFilterProxyModelPrivate;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper15beginInsertRowsERK11QModelIndexii")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper18beginInsertColumnsERK11QModelIndexii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper13endInsertRowsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper16endInsertColumnsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper15beginRemoveRowsERK11QModelIndexii")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper18beginRemoveColumnsERK11QModelIndexii")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper13endRemoveRowsEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper16endRemoveColumnsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper15beginResetModelEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper13endResetModelEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper10proxyModelEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper24filterAcceptsRowInternalEiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper16filterAcceptsRowEiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper27filterAcceptsColumnInternalEiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper19filterAcceptsColumnEiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper8lessThanERK11QModelIndexS2_")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN26QAbstractProxyModelPrivate23_q_sourceModelDestroyedEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper14filter_changedENS_9DirectionERK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper21source_items_insertedERK11QModelIndexiiNS_9DirectionE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper32source_items_about_to_be_removedERK11QModelIndexiiNS_9DirectionE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper20source_items_removedERK11QModelIndexiiNS_9DirectionE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper4sortEv")) {
      taken[22] = call;
      return true;
    }
    return false;
  }

  //  void QQmlSortFilterProxyModelPrivate::beginInsertRows(const
  //      QModelIndex &parent, int first, int last)
  void beginInsertRows(
      const QModelIndex &parent,
      int first,
      int last) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall0 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall0>(taken[0]);
      call(this, &parent, first, last, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::beginInsertRows(parent, first, last);
  }

  //  void QQmlSortFilterProxyModelPrivate::beginInsertColumns(const
  //      QModelIndex &parent, int first, int last)
  void beginInsertColumns(
      const QModelIndex &parent,
      int first,
      int last) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall1 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall1>(taken[1]);
      call(this, &parent, first, last, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::beginInsertColumns(parent, first, last);
  }

  //  void QQmlSortFilterProxyModelPrivate::endInsertRows()
  void endInsertRows() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall2 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::endInsertRows();
  }

  //  void QQmlSortFilterProxyModelPrivate::endInsertColumns()
  void endInsertColumns() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall3 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::endInsertColumns();
  }

  //  void QQmlSortFilterProxyModelPrivate::beginRemoveRows(const
  //      QModelIndex &parent, int first, int last)
  void beginRemoveRows(
      const QModelIndex &parent,
      int first,
      int last) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall4 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall4>(taken[4]);
      call(this, &parent, first, last, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::beginRemoveRows(parent, first, last);
  }

  //  void QQmlSortFilterProxyModelPrivate::beginRemoveColumns(const
  //      QModelIndex &parent, int first, int last)
  void beginRemoveColumns(
      const QModelIndex &parent,
      int first,
      int last) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall5 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall5>(taken[5]);
      call(this, &parent, first, last, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::beginRemoveColumns(parent, first, last);
  }

  //  void QQmlSortFilterProxyModelPrivate::endRemoveRows()
  void endRemoveRows() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall6 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::endRemoveRows();
  }

  //  void QQmlSortFilterProxyModelPrivate::endRemoveColumns()
  void endRemoveColumns() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall7 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::endRemoveColumns();
  }

  //  void QQmlSortFilterProxyModelPrivate::beginResetModel()
  void beginResetModel() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall8 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::beginResetModel();
  }

  //  void QQmlSortFilterProxyModelPrivate::endResetModel()
  void endResetModel() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall9 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModelPrivate::endResetModel();
  }

  //  const QAbstractProxyModel
  //      *QQmlSortFilterProxyModelPrivate::proxyModel() const
  const QAbstractProxyModel *proxyModel() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall10 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QAbstractProxyModel *>(given);
    }
    return QQmlSortFilterProxyModelPrivate::proxyModel();
  }

  //  bool QQmlSortFilterProxyModelPrivate::filterAcceptsRowInternal(int
  //      sourceRow, const QModelIndex &sourceIndex) const
  bool filterAcceptsRowInternal(
      int sourceRow,
      const QModelIndex &sourceIndex) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall11 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall11>(taken[11]);
      bool given = call(this, sourceRow, &sourceIndex, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModelPrivate::filterAcceptsRowInternal(sourceRow, sourceIndex);
  }

  //  bool QQmlSortFilterProxyModelPrivate::filterAcceptsRow(int
  //      source_row, const QModelIndex &source_parent) const
  bool filterAcceptsRow(
      int source_row,
      const QModelIndex &source_parent) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall12 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall12>(taken[12]);
      bool given = call(this, source_row, &source_parent, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModelPrivate::filterAcceptsRow(source_row, source_parent);
  }

  //  bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumnInternal(int
  //      sourceColumn, const QModelIndex &sourceIndex) const
  bool filterAcceptsColumnInternal(
      int sourceColumn,
      const QModelIndex &sourceIndex) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall13 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall13>(taken[13]);
      bool given = call(this, sourceColumn, &sourceIndex, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModelPrivate::filterAcceptsColumnInternal(sourceColumn, sourceIndex);
  }

  //  bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumn(int
  //      source_column, const QModelIndex &source_parent) const
  bool filterAcceptsColumn(
      int source_column,
      const QModelIndex &source_parent) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall14 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall14>(taken[14]);
      bool given = call(this, source_column, &source_parent, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModelPrivate::filterAcceptsColumn(source_column, source_parent);
  }

  //  bool QQmlSortFilterProxyModelPrivate::lessThan(const QModelIndex
  //      &source_left, const QModelIndex &source_right) const
  bool lessThan(
      const QModelIndex &source_left,
      const QModelIndex &source_right) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall15 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall15>(taken[15]);
      bool given = call(this, &source_left, &source_right, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModelPrivate::lessThan(source_left, source_right);
  }

#if QT_CONFIG(proxymodel)
  //  void QAbstractProxyModelPrivate::_q_sourceModelDestroyed()
  void _q_sourceModelDestroyed() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall16 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractProxyModelPrivate::_q_sourceModelDestroyed();
  }
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModelPrivate::executePendingOperations() const
  void executePendingOperations() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall17 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModelPrivate::executePendingOperations();
  }
#endif  // QT_CONFIG(itemmodel)

  //  void QSortFilterProxyModelHelper::filter_changed(Direction dir, const
  //      QModelIndex &source_parent)
  void filter_changed(
      QSortFilterProxyModelHelper::Direction dir,
      const QModelIndex &source_parent) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall18 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall18>(taken[18]);
      call(this, static_cast<int>(dir), &source_parent, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::filter_changed(dir, source_parent);
  }

  //  void QSortFilterProxyModelHelper::source_items_inserted(const
  //      QModelIndex &source_parent, int start, int end, Direction
  //      direction)
  void source_items_inserted(
      const QModelIndex &source_parent,
      int start,
      int end,
      QSortFilterProxyModelHelper::Direction direction) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall19 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall19>(taken[19]);
      call(this, &source_parent, start, end, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::source_items_inserted(source_parent, start, end, direction);
  }

  //  void
  //      QSortFilterProxyModelHelper::source_items_about_to_be_removed(con
  //      st QModelIndex &source_parent, int start, int end, Direction
  //      direction)
  void source_items_about_to_be_removed(
      const QModelIndex &source_parent,
      int start,
      int end,
      QSortFilterProxyModelHelper::Direction direction) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall20 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall20>(taken[20]);
      call(this, &source_parent, start, end, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::source_items_about_to_be_removed(source_parent, start, end, direction);
  }

  //  void QSortFilterProxyModelHelper::source_items_removed(const
  //      QModelIndex &source_parent, int start, int end, Direction
  //      direction)
  void source_items_removed(
      const QModelIndex &source_parent,
      int start,
      int end,
      QSortFilterProxyModelHelper::Direction direction) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall21 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall21>(taken[21]);
      call(this, &source_parent, start, end, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::source_items_removed(source_parent, start, end, direction);
  }

  //  void QSortFilterProxyModelHelper::sort()
  void sort() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelPrivateCall22 call = reinterpret_cast<CuteQQmlSortFilterProxyModelPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::sort();
  }
};

//  QQmlSortFilterProxyModel *QQmlSortFilterProxyModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSortFilterProxyModel *ritual_ZN31QQmlSortFilterProxyModelPrivate6q_funcEv(
    QQmlSortFilterProxyModelPrivate *self) {
  return self->q_func();
}

//  const QQmlSortFilterProxyModel *QQmlSortFilterProxyModelPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQmlSortFilterProxyModel *ritual_ZNK31QQmlSortFilterProxyModelPrivate6q_funcEv(
    const QQmlSortFilterProxyModelPrivate *self) {
  return self->q_func();
}

//  void QQmlSortFilterProxyModelPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate4initEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->init();
}

//  bool QQmlSortFilterProxyModelPrivate::containRoleForRecursiveFilter(const
//      QList<int> &roles) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlSortFilterProxyModelPrivate29containRoleForRecursiveFilterERK5QListIiE(
    const QQmlSortFilterProxyModelPrivate *self,
    const QList<int> *roles) {
  return self->containRoleForRecursiveFilter(*roles);
}

//  bool QQmlSortFilterProxyModelPrivate::recursiveParentAcceptsRow(const
//      QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlSortFilterProxyModelPrivate25recursiveParentAcceptsRowERK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_parent) {
  return self->recursiveParentAcceptsRow(*source_parent);
}

//  bool QQmlSortFilterProxyModelPrivate::recursiveChildAcceptsRow(int
//      source_row, const QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlSortFilterProxyModelPrivate24recursiveChildAcceptsRowEiRK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    int source_row,
    const QModelIndex *source_parent) {
  return self->recursiveChildAcceptsRow(source_row, *source_parent);
}

//  QList<std::pair<int, QList<int>>> QQmlSortFilterProxyModelPrivate::proxy_
//      intervals_for_source_items_to_add(const QList<int> &proxy_to_source,
//      const QList<int> &source_items, const QModelIndex &source_parent,
//      QSortFilterProxyModelHelper::Direction direction) const
extern "C" Q_DECL_EXPORT
QList<std::pair<int, QList<int>>> *ritual_ZNK31QQmlSortFilterProxyModelPrivate39proxy_intervals_for_source_items_to_addERK5QListIiES3_RK11QModelIndexN27QSortFilterProxyModelHelper9DirectionE(
    const QQmlSortFilterProxyModelPrivate *self,
    const QList<int> *proxy_to_source,
    const QList<int> *source_items,
    const QModelIndex *source_parent,
    QSortFilterProxyModelHelper::Direction direction) {
  return new QList<std::pair<int, QList<int>>>(
      self->proxy_intervals_for_source_items_to_add(
          *proxy_to_source,
          *source_items,
          *source_parent,
          direction));
}

//  bool QQmlSortFilterProxyModelPrivate::needsReorder(const QList<int>
//      &source_rows, const QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlSortFilterProxyModelPrivate12needsReorderERK5QListIiERK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    const QList<int> *source_rows,
    const QModelIndex *source_parent) {
  return self->needsReorder(*source_rows, *source_parent);
}

//  bool QQmlSortFilterProxyModelPrivate::updatePrimaryColumn()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QQmlSortFilterProxyModelPrivate19updatePrimaryColumnEv(
    QQmlSortFilterProxyModelPrivate *self) {
  return self->updatePrimaryColumn();
}

//  int QQmlSortFilterProxyModelPrivate::findPrimarySortColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQmlSortFilterProxyModelPrivate21findPrimarySortColumnEv(
    const QQmlSortFilterProxyModelPrivate *self) {
  return self->findPrimarySortColumn();
}

//  void QQmlSortFilterProxyModelPrivate::changePersistentIndexList(const
//      QModelIndexList &from, const QModelIndexList &to)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate25changePersistentIndexListERK5QListI11QModelIndexES4_(
    QQmlSortFilterProxyModelPrivate *self,
    const QList<QModelIndex> *from,
    const QList<QModelIndex> *to) {
  self->changePersistentIndexList(*from, *to);
}

//  void QQmlSortFilterProxyModelPrivate::beginInsertRows(const QModelIndex
//      &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate15beginInsertRowsERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginInsertRows(*parent, first, last);
}

//  void QQmlSortFilterProxyModelPrivate::beginInsertColumns(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate18beginInsertColumnsERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginInsertColumns(*parent, first, last);
}

//  void QQmlSortFilterProxyModelPrivate::endInsertRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate13endInsertRowsEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->endInsertRows();
}

//  void QQmlSortFilterProxyModelPrivate::endInsertColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate16endInsertColumnsEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->endInsertColumns();
}

//  void QQmlSortFilterProxyModelPrivate::beginRemoveRows(const QModelIndex
//      &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate15beginRemoveRowsERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginRemoveRows(*parent, first, last);
}

//  void QQmlSortFilterProxyModelPrivate::beginRemoveColumns(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate18beginRemoveColumnsERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginRemoveColumns(*parent, first, last);
}

//  void QQmlSortFilterProxyModelPrivate::endRemoveRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate13endRemoveRowsEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->endRemoveRows();
}

//  void QQmlSortFilterProxyModelPrivate::endRemoveColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate16endRemoveColumnsEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->endRemoveColumns();
}

//  void QQmlSortFilterProxyModelPrivate::beginResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate15beginResetModelEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->beginResetModel();
}

//  void QQmlSortFilterProxyModelPrivate::endResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate13endResetModelEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->endResetModel();
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceDataChanged(const
//      QModelIndex &source_top_left, const QModelIndex &source_bottom_right,
//      const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate20_q_sourceDataChangedERK11QModelIndexS2_RK5QListIiE(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_top_left,
    const QModelIndex *source_bottom_right,
    const QList<int> *roles) {
  self->_q_sourceDataChanged(*source_top_left, *source_bottom_right, *roles);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceHeaderDataChanged(Qt::Orie
//      ntation orientation, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate26_q_sourceHeaderDataChangedEN2Qt11OrientationEii(
    QQmlSortFilterProxyModelPrivate *self,
    Qt::Orientation orientation,
    int start,
    int end) {
  self->_q_sourceHeaderDataChanged(orientation, start, end);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceAboutToBeReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate23_q_sourceAboutToBeResetEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->_q_sourceAboutToBeReset();
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate14_q_sourceResetEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->_q_sourceReset();
}

//  void QQmlSortFilterProxyModelPrivate::_q_clearMapping()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate15_q_clearMappingEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->_q_clearMapping();
}

//  void
//      QQmlSortFilterProxyModelPrivate::_q_sourceLayoutAboutToBeChanged(cons
//      t QList<QPersistentModelIndex> &sourceParents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate31_q_sourceLayoutAboutToBeChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QQmlSortFilterProxyModelPrivate *self,
    const QList<QPersistentModelIndex> *sourceParents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->_q_sourceLayoutAboutToBeChanged(*sourceParents, hint);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceLayoutChanged(const
//      QList<QPersistentModelIndex> &sourceParents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate22_q_sourceLayoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QQmlSortFilterProxyModelPrivate *self,
    const QList<QPersistentModelIndex> *sourceParents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->_q_sourceLayoutChanged(*sourceParents, hint);
}

//  void
//      QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeInserted(const
//      QModelIndex &source_parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate30_q_sourceRowsAboutToBeInsertedERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_parent,
    int start,
    int end) {
  self->_q_sourceRowsAboutToBeInserted(*source_parent, start, end);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsInserted(const
//      QModelIndex &source_parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate21_q_sourceRowsInsertedERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_parent,
    int start,
    int end) {
  self->_q_sourceRowsInserted(*source_parent, start, end);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeRemoved(const
//      QModelIndex &source_parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate29_q_sourceRowsAboutToBeRemovedERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_parent,
    int start,
    int end) {
  self->_q_sourceRowsAboutToBeRemoved(*source_parent, start, end);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsRemoved(const
//      QModelIndex &source_parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate20_q_sourceRowsRemovedERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_parent,
    int start,
    int end) {
  self->_q_sourceRowsRemoved(*source_parent, start, end);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeMoved(const
//      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
//      QModelIndex &destParent, int dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate27_q_sourceRowsAboutToBeMovedERK11QModelIndexiiS2_i(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destParent,
    int dest) {
  self->_q_sourceRowsAboutToBeMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destParent,
      dest);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsMoved(const
//      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
//      QModelIndex &destParent, int dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate18_q_sourceRowsMovedERK11QModelIndexiiS2_i(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destParent,
    int dest) {
  self->_q_sourceRowsMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destParent,
      dest);
}

//  void
//      QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeInserted(co
//      nst QModelIndex &source_parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate33_q_sourceColumnsAboutToBeInsertedERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_parent,
    int start,
    int end) {
  self->_q_sourceColumnsAboutToBeInserted(*source_parent, start, end);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsInserted(const
//      QModelIndex &source_parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate24_q_sourceColumnsInsertedERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_parent,
    int start,
    int end) {
  self->_q_sourceColumnsInserted(*source_parent, start, end);
}

//  void
//      QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeRemoved(con
//      st QModelIndex &source_parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate32_q_sourceColumnsAboutToBeRemovedERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_parent,
    int start,
    int end) {
  self->_q_sourceColumnsAboutToBeRemoved(*source_parent, start, end);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsRemoved(const
//      QModelIndex &source_parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate23_q_sourceColumnsRemovedERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_parent,
    int start,
    int end) {
  self->_q_sourceColumnsRemoved(*source_parent, start, end);
}

//  void
//      QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeMoved(const
//      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
//      QModelIndex &destParent, int dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate30_q_sourceColumnsAboutToBeMovedERK11QModelIndexiiS2_i(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destParent,
    int dest) {
  self->_q_sourceColumnsAboutToBeMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destParent,
      dest);
}

//  void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsMoved(const
//      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
//      QModelIndex &destParent, int dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSortFilterProxyModelPrivate21_q_sourceColumnsMovedERK11QModelIndexiiS2_i(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destParent,
    int dest) {
  self->_q_sourceColumnsMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destParent,
      dest);
}

//  const QAbstractProxyModel *QQmlSortFilterProxyModelPrivate::proxyModel()
//      const
extern "C" Q_DECL_EXPORT
const QAbstractProxyModel *ritual_ZNK31QQmlSortFilterProxyModelPrivate10proxyModelEv(
    const QQmlSortFilterProxyModelPrivate *self) {
  return self->proxyModel();
}

//  QModelIndex QQmlSortFilterProxyModelPrivate::createIndex(int row, int
//      column, QHash<QtPrivate::QModelIndexWrapper,
//      QSortFilterProxyModelHelper::Mapping *>::const_iterator it) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK31QQmlSortFilterProxyModelPrivate11createIndexEiiN5QHashIN9QtPrivate18QModelIndexWrapperEPN27QSortFilterProxyModelHelper7MappingEE14const_iteratorE(
    const QQmlSortFilterProxyModelPrivate *self,
    int row,
    int column,
    const QHash<QtPrivate::QModelIndexWrapper, QSortFilterProxyModelHelper::Mapping *>::const_iterator *it) {
  return new QModelIndex(self->createIndex(row, column, *it));
}

//  bool QQmlSortFilterProxyModelPrivate::filterAcceptsRowInternal(int
//      sourceRow, const QModelIndex &sourceIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlSortFilterProxyModelPrivate24filterAcceptsRowInternalEiRK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    int sourceRow,
    const QModelIndex *sourceIndex) {
  return self->filterAcceptsRowInternal(sourceRow, *sourceIndex);
}

//  bool QQmlSortFilterProxyModelPrivate::filterAcceptsRow(int source_row,
//      const QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlSortFilterProxyModelPrivate16filterAcceptsRowEiRK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    int source_row,
    const QModelIndex *source_parent) {
  return self->filterAcceptsRow(source_row, *source_parent);
}

//  bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumnInternal(int
//      sourceColumn, const QModelIndex &sourceIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlSortFilterProxyModelPrivate27filterAcceptsColumnInternalEiRK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    int sourceColumn,
    const QModelIndex *sourceIndex) {
  return self->filterAcceptsColumnInternal(sourceColumn, *sourceIndex);
}

//  bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumn(int
//      source_column, const QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlSortFilterProxyModelPrivate19filterAcceptsColumnEiRK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    int source_column,
    const QModelIndex *source_parent) {
  return self->filterAcceptsColumn(source_column, *source_parent);
}

//  void QQmlSortFilterProxyModelPrivate::sort_source_rows(QList<int>
//      &source_rows, const QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK31QQmlSortFilterProxyModelPrivate16sort_source_rowsER5QListIiERK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    QList<int> *source_rows,
    const QModelIndex *source_parent) {
  self->sort_source_rows(*source_rows, *source_parent);
}

//  bool QQmlSortFilterProxyModelPrivate::lessThan(const QModelIndex
//      &source_left, const QModelIndex &source_right) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlSortFilterProxyModelPrivate8lessThanERK11QModelIndexS2_(
    const QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_left,
    const QModelIndex *source_right) {
  return self->lessThan(*source_left, *source_right);
}

//  QQmlSortFilterProxyModelPrivate as the QSortFilterProxyModelHelper it is
//      built on
extern "C" Q_DECL_EXPORT
QSortFilterProxyModelHelper *ritual_cast_QQmlSortFilterProxyModelPrivate_QSortFilterProxyModelHelper(
    QQmlSortFilterProxyModelPrivate *self) {
  return static_cast<QSortFilterProxyModelHelper *>(self);
}

//  a Python function taken by a CuteQQmlSortFilterProxyModelPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSortFilterProxyModelPrivate(
    QQmlSortFilterProxyModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSortFilterProxyModelPrivate *>(self)->take(key, call);
}

//  void QQmlSortFilterProxyModelPrivate::beginInsertRows(const QModelIndex
//      &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate15beginInsertRowsERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->QQmlSortFilterProxyModelPrivate::beginInsertRows(
      *parent,
      first,
      last);
}

//  void QQmlSortFilterProxyModelPrivate::beginInsertColumns(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate18beginInsertColumnsERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->QQmlSortFilterProxyModelPrivate::beginInsertColumns(
      *parent,
      first,
      last);
}

//  void QQmlSortFilterProxyModelPrivate::endInsertRows()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate13endInsertRowsEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->QQmlSortFilterProxyModelPrivate::endInsertRows();
}

//  void QQmlSortFilterProxyModelPrivate::endInsertColumns()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate16endInsertColumnsEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->QQmlSortFilterProxyModelPrivate::endInsertColumns();
}

//  void QQmlSortFilterProxyModelPrivate::beginRemoveRows(const QModelIndex
//      &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate15beginRemoveRowsERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->QQmlSortFilterProxyModelPrivate::beginRemoveRows(
      *parent,
      first,
      last);
}

//  void QQmlSortFilterProxyModelPrivate::beginRemoveColumns(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate18beginRemoveColumnsERK11QModelIndexii(
    QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->QQmlSortFilterProxyModelPrivate::beginRemoveColumns(
      *parent,
      first,
      last);
}

//  void QQmlSortFilterProxyModelPrivate::endRemoveRows()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate13endRemoveRowsEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->QQmlSortFilterProxyModelPrivate::endRemoveRows();
}

//  void QQmlSortFilterProxyModelPrivate::endRemoveColumns()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate16endRemoveColumnsEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->QQmlSortFilterProxyModelPrivate::endRemoveColumns();
}

//  void QQmlSortFilterProxyModelPrivate::beginResetModel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate15beginResetModelEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->QQmlSortFilterProxyModelPrivate::beginResetModel();
}

//  void QQmlSortFilterProxyModelPrivate::endResetModel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQmlSortFilterProxyModelPrivate13endResetModelEv(
    QQmlSortFilterProxyModelPrivate *self) {
  self->QQmlSortFilterProxyModelPrivate::endResetModel();
}

//  const QAbstractProxyModel *QQmlSortFilterProxyModelPrivate::proxyModel()
//      const
extern "C" Q_DECL_EXPORT
const QAbstractProxyModel *ritual_own_ZNK31QQmlSortFilterProxyModelPrivate10proxyModelEv(
    const QQmlSortFilterProxyModelPrivate *self) {
  return self->QQmlSortFilterProxyModelPrivate::proxyModel();
}

//  bool QQmlSortFilterProxyModelPrivate::filterAcceptsRowInternal(int
//      sourceRow, const QModelIndex &sourceIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK31QQmlSortFilterProxyModelPrivate24filterAcceptsRowInternalEiRK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    int sourceRow,
    const QModelIndex *sourceIndex) {
  return self->QQmlSortFilterProxyModelPrivate::filterAcceptsRowInternal(
      sourceRow,
      *sourceIndex);
}

//  bool QQmlSortFilterProxyModelPrivate::filterAcceptsRow(int source_row,
//      const QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK31QQmlSortFilterProxyModelPrivate16filterAcceptsRowEiRK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    int source_row,
    const QModelIndex *source_parent) {
  return self->QQmlSortFilterProxyModelPrivate::filterAcceptsRow(
      source_row,
      *source_parent);
}

//  bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumnInternal(int
//      sourceColumn, const QModelIndex &sourceIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK31QQmlSortFilterProxyModelPrivate27filterAcceptsColumnInternalEiRK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    int sourceColumn,
    const QModelIndex *sourceIndex) {
  return self->QQmlSortFilterProxyModelPrivate::filterAcceptsColumnInternal(
      sourceColumn,
      *sourceIndex);
}

//  bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumn(int
//      source_column, const QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK31QQmlSortFilterProxyModelPrivate19filterAcceptsColumnEiRK11QModelIndex(
    const QQmlSortFilterProxyModelPrivate *self,
    int source_column,
    const QModelIndex *source_parent) {
  return self->QQmlSortFilterProxyModelPrivate::filterAcceptsColumn(
      source_column,
      *source_parent);
}

//  bool QQmlSortFilterProxyModelPrivate::lessThan(const QModelIndex
//      &source_left, const QModelIndex &source_right) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK31QQmlSortFilterProxyModelPrivate8lessThanERK11QModelIndexS2_(
    const QQmlSortFilterProxyModelPrivate *self,
    const QModelIndex *source_left,
    const QModelIndex *source_right) {
  return self->QQmlSortFilterProxyModelPrivate::lessThan(
      *source_left,
      *source_right);
}

//  a QList<std::pair<int, QList<int>>> a ritual of
//      QQmlSortFilterProxyModelPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSortFilterProxyModelPrivate__QList_std_pair_int_QList_int(
    QList<std::pair<int, QList<int>>> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
