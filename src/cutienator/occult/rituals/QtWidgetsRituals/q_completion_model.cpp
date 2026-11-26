//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QCompletionModel' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(completer)
#if QT_CONFIG(completer)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWidgets/private/qcompleter_p.h>
#include "QtWidgets/qscrollbar.h"
#include "QtCore/qdir.h"
#if QT_CONFIG(stringlistmodel)
#include "QtCore/qstringlistmodel.h"
#endif
#if QT_CONFIG(filesystemmodel)
#include "QtGui/qfilesystemmodel.h"
#endif
#include "QtWidgets/qheaderview.h"
#if QT_CONFIG(listview)
#include "QtWidgets/qlistview.h"
#endif
#include "QtWidgets/qapplication.h"
#include "QtGui/qevent.h"
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtGui/qpa/qplatformwindow.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#if QT_CONFIG(lineedit)
#include "QtWidgets/qlineedit.h"
#endif
#include "QtCore/qdir.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from QtWidgets__QCompletionModel.cpp, line 1, as moc:QCompletionModel
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN16QCompletionModelE_t {};
} // unnamed namespace

template <> constexpr inline auto QCompletionModel::qt_create_metaobjectdata<qt_meta_tag_ZN16QCompletionModelE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QCompletionModel",
        "rowsAdded",
        "",
        "invalidate",
        "rowsInserted",
        "modelDestroyed"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'rowsAdded'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'invalidate'
        QtMocHelpers::SlotData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'rowsInserted'
        QtMocHelpers::SlotData<void()>(4, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'modelDestroyed'
        QtMocHelpers::SlotData<void()>(5, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QCompletionModel, qt_meta_tag_ZN16QCompletionModelE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QCompletionModel::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstractProxyModel::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QCompletionModelE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QCompletionModelE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN16QCompletionModelE_t>.metaTypes,
    nullptr
} };

void QCompletionModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QCompletionModel *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->rowsAdded(); break;
        case 1: _t->invalidate(); break;
        case 2: _t->rowsInserted(); break;
        case 3: _t->modelDestroyed(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QCompletionModel::*)()>(_a, &QCompletionModel::rowsAdded, 0))
            return;
    }
}

const QMetaObject *QCompletionModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QCompletionModel::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QCompletionModelE_t>.strings))
        return static_cast<void*>(this);
    return QAbstractProxyModel::qt_metacast(_clname);
}

int QCompletionModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractProxyModel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 4;
    }
    return _id;
}

// SIGNAL 0
void QCompletionModel::rowsAdded()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from src/widgets/util/qcompleter.cpp, line 381, as _ZN16QCompletionModel10invalidateEv
inline void QCompletionModel::invalidate()
{
    engine->cache.clear();
    filter(engine->curParts);
}

//  from src/widgets/util/qcompleter.cpp, line 375, as _ZN16QCompletionModel12rowsInsertedEv
inline void QCompletionModel::rowsInserted()
{
    invalidate();
    emit rowsAdded();
}

//  from src/widgets/util/qcompleter.cpp, line 369, as _ZN16QCompletionModel14modelDestroyedEv
inline void QCompletionModel::modelDestroyed()
{
    QAbstractProxyModel::setSourceModel(nullptr); // switch to static empty model
    invalidate();
}

//  from src/widgets/util/qcompleter.cpp, line 149, as _ZN16QCompletionModel14setSourceModelEP18QAbstractItemModel
inline void QCompletionModel::setSourceModel(QAbstractItemModel *source)
{
    bool hadModel = (sourceModel() != nullptr);

    if (hadModel)
        QObject::disconnect(sourceModel(), nullptr, this, nullptr);

    QAbstractProxyModel::setSourceModel(source);

    if (source) {
        // TODO: Optimize updates in the source model
        connect(source, SIGNAL(modelReset()), this, SLOT(invalidate()));
        connect(source, SIGNAL(destroyed()), this, SLOT(modelDestroyed()));
        connect(source, SIGNAL(layoutChanged()), this, SLOT(invalidate()));
        connect(source, SIGNAL(rowsInserted(QModelIndex,int,int)), this, SLOT(rowsInserted()));
        connect(source, SIGNAL(rowsRemoved(QModelIndex,int,int)), this, SLOT(invalidate()));
        connect(source, SIGNAL(columnsInserted(QModelIndex,int,int)), this, SLOT(invalidate()));
        connect(source, SIGNAL(columnsRemoved(QModelIndex,int,int)), this, SLOT(invalidate()));
        connect(source, SIGNAL(dataChanged(QModelIndex,QModelIndex)), this, SLOT(invalidate()));
    }

    invalidate();
}

//  from src/widgets/util/qcompleter.cpp, line 143, as _ZNK16QCompletionModel11columnCountERK11QModelIndex
inline int QCompletionModel::columnCount(const QModelIndex &) const
{
    Q_D(const QCompletionModel);
    return d->model->columnCount();
}

//  from src/widgets/util/qcompleter.cpp, line 348, as _ZNK16QCompletionModel11hasChildrenERK11QModelIndex
inline bool QCompletionModel::hasChildren(const QModelIndex &parent) const
{
    Q_D(const QCompletionModel);
    if (parent.isValid())
        return false;

    if (showAll)
        return d->model->hasChildren(mapToSource(parent));

    if (!engine->matchCount())
        return false;

    return true;
}

//  from src/widgets/util/qcompleter.cpp, line 196, as _ZNK16QCompletionModel11mapToSourceERK11QModelIndex
inline QModelIndex QCompletionModel::mapToSource(const QModelIndex& index) const
{
    Q_D(const QCompletionModel);
    if (!index.isValid())
        return engine->curParent;

    int row;
    QModelIndex parent = engine->curParent;
    if (!showAll) {
        if (!engine->matchCount())
            return QModelIndex();
        Q_ASSERT(index.row() < engine->matchCount());
        QIndexMapper& rootIndices = engine->historyMatch.indices;
        if (index.row() < rootIndices.count()) {
            row = rootIndices[index.row()];
            parent = QModelIndex();
        } else {
            row = engine->curMatch.indices[index.row() - rootIndices.count()];
        }
    } else {
        row = index.row();
    }

    return d->model->index(row, index.column(), parent);
}

//  from src/widgets/util/qcompleter.cpp, line 222, as _ZNK16QCompletionModel13mapFromSourceERK11QModelIndex
inline QModelIndex QCompletionModel::mapFromSource(const QModelIndex& idx) const
{
    if (!idx.isValid())
        return QModelIndex();

    int row = -1;
    if (!showAll) {
        if (!engine->matchCount())
            return QModelIndex();

        QIndexMapper& rootIndices = engine->historyMatch.indices;
        if (idx.parent().isValid()) {
            if (idx.parent() != engine->curParent)
                return QModelIndex();
        } else {
            row = rootIndices.indexOf(idx.row());
            if (row == -1 && engine->curParent.isValid())
                return QModelIndex(); // source parent and our parent don't match
        }

        if (row == -1) {
            QIndexMapper& indices = engine->curMatch.indices;
            engine->filterOnDemand(idx.row() - indices.last());
            row = indices.indexOf(idx.row()) + rootIndices.count();
        }

        if (row == -1)
            return QModelIndex();
    } else {
        if (idx.parent() != engine->curParent)
            return QModelIndex();
        row = idx.row();
    }

    return createIndex(row, idx.column());
}

//  from src/widgets/util/qcompleter.cpp, line 363, as _ZNK16QCompletionModel4dataERK11QModelIndexi
inline QVariant QCompletionModel::data(const QModelIndex& index, int role) const
{
    Q_D(const QCompletionModel);
    return d->model->data(mapToSource(index), role);
}

//  from src/widgets/util/qcompleter.cpp, line 289, as _ZNK16QCompletionModel5indexEiiRK11QModelIndex
inline QModelIndex QCompletionModel::index(int row, int column, const QModelIndex& parent) const
{
    Q_D(const QCompletionModel);
    if (row < 0 || column < 0 || column >= columnCount(parent) || parent.isValid())
        return QModelIndex();

    if (!showAll) {
        if (!engine->matchCount())
            return QModelIndex();
        if (row >= engine->historyMatch.indices.count()) {
            int want = row + 1 - engine->matchCount();
            if (want > 0)
                engine->filterOnDemand(want);
            if (row >= engine->matchCount())
                return QModelIndex();
        }
    } else {
        if (row >= d->model->rowCount(engine->curParent))
            return QModelIndex();
    }

    return createIndex(row, column);
}

//  from src/widgets/util/qcompleter.cpp, line 322, as _ZNK16QCompletionModel8rowCountERK11QModelIndex
inline int QCompletionModel::rowCount(const QModelIndex &parent) const
{
    Q_D(const QCompletionModel);
    if (parent.isValid())
        return 0;

    if (showAll) {
        // Show all items below current parent, even if we have no valid matches
        if (engine->curParts.size() != 1  && !engine->matchCount()
            && !engine->curParent.isValid())
            return 0;
        return d->model->rowCount(engine->curParent);
    }

    return completionCount();
}

//  from src/widgets/util/qcompleter.cpp, line 611, as _ZN18QSortedModelEngine6filterERK7QStringRK11QModelIndexi
inline QMatchData QSortedModelEngine::filter(const QString& part, const QModelIndex& parent, int)
{
    const QAbstractItemModel *model = c->proxy->sourceModel();

    QMatchData hint;
    if (lookupCache(part, parent, &hint))
        return hint;

    QIndexMapper indices;
    Qt::SortOrder order = sortOrder(parent);

    if (matchHint(part, parent, &hint)) {
        if (!hint.isValid())
            return QMatchData();
        indices = hint.indices;
    } else {
        indices = indexHint(part, parent, order);
    }

    // binary search the model within 'indices' for 'part' under 'parent'
    int high = indices.to() + 1;
    int low = indices.from() - 1;
    int probe;
    QModelIndex probeIndex;
    QString probeData;

    while (high - low > 1)
    {
        probe = (high + low) / 2;
        probeIndex = model->index(probe, c->column, parent);
        probeData = model->data(probeIndex, c->role).toString();
        const int cmp = QString::compare(probeData, part, c->cs);
        if ((order == Qt::AscendingOrder && cmp >= 0)
            || (order == Qt::DescendingOrder && cmp < 0)) {
            high = probe;
        } else {
            low = probe;
        }
    }

    if ((order == Qt::AscendingOrder && low == indices.to())
        || (order == Qt::DescendingOrder && high == indices.from())) { // not found
        saveInCache(part, parent, QMatchData());
        return QMatchData();
    }

    probeIndex = model->index(order == Qt::AscendingOrder ? low+1 : high-1, c->column, parent);
    probeData = model->data(probeIndex, c->role).toString();
    if (!probeData.startsWith(part, c->cs)) {
        saveInCache(part, parent, QMatchData());
        return QMatchData();
    }

    const bool exactMatch = QString::compare(probeData, part, c->cs) == 0;
    int emi =  exactMatch ? (order == Qt::AscendingOrder ? low+1 : high-1) : -1;

    int from = 0;
    int to = 0;
    if (order == Qt::AscendingOrder) {
        from = low + 1;
        high = indices.to() + 1;
        low = from;
    } else {
        to = high - 1;
        low = indices.from() - 1;
        high = to;
    }

    while (high - low > 1)
    {
        probe = (high + low) / 2;
        probeIndex = model->index(probe, c->column, parent);
        probeData = model->data(probeIndex, c->role).toString();
        const bool startsWith = probeData.startsWith(part, c->cs);
        if ((order == Qt::AscendingOrder && startsWith)
            || (order == Qt::DescendingOrder && !startsWith)) {
            low = probe;
        } else {
            high = probe;
        }
    }

    QMatchData m(order == Qt::AscendingOrder ? QIndexMapper(from, high - 1) : QIndexMapper(low+1, to), emi, false);
    saveInCache(part, parent, m);
    return m;
}

//  from src/widgets/util/qcompleter.cpp, line 749, as _ZN20QUnsortedModelEngine14filterOnDemandEi
inline void QUnsortedModelEngine::filterOnDemand(int n)
{
    Q_ASSERT(matchCount());
    if (!curMatch.partial)
        return;
    Q_ASSERT(n >= -1);
    const QAbstractItemModel *model = c->proxy->sourceModel();
    int lastRow = model->rowCount(curParent) - 1;
    QIndexMapper im(curMatch.indices.last() + 1, lastRow);
    int lastIndex = buildIndices(curParts.constLast(), curParent, n, im, &curMatch);
    curMatch.partial = (lastRow != lastIndex);
    saveInCache(curParts.constLast(), curParent, curMatch);
}

//  from src/widgets/util/qcompleter.cpp, line 763, as _ZN20QUnsortedModelEngine6filterERK7QStringRK11QModelIndexi
inline QMatchData QUnsortedModelEngine::filter(const QString& part, const QModelIndex& parent, int n)
{
    QMatchData hint;

    QList<int> v;
    QIndexMapper im(v);
    QMatchData m(im, -1, true);

    const QAbstractItemModel *model = c->proxy->sourceModel();
    bool foundInCache = lookupCache(part, parent, &m);

    if (!foundInCache) {
        if (matchHint(part, parent, &hint) && !hint.isValid())
            return QMatchData();
    }

    if (!foundInCache && !hint.isValid()) {
        const int lastRow = model->rowCount(parent) - 1;
        QIndexMapper all(0, lastRow);
        int lastIndex = buildIndices(part, parent, n, all, &m);
        m.partial = (lastIndex != lastRow);
    } else {
        if (!foundInCache) { // build from hint as much as we can
            buildIndices(part, parent, INT_MAX, hint.indices, &m);
            m.partial = hint.partial;
        }
        if (m.partial && ((n == -1 && m.exactMatchIndex == -1) || (m.indices.count() < n))) {
            // need more and have more
            const int lastRow = model->rowCount(parent) - 1;
            QIndexMapper rest(hint.indices.last() + 1, lastRow);
            int want = n == -1 ? -1 : n - m.indices.count();
            int lastIndex = buildIndices(part, parent, want, rest, &m);
            m.partial = (lastRow != lastIndex);
        }
    }

    saveInCache(part, parent, m);
    return m;
}

//  from src/widgets/util/qcompleter.cpp, line 412, as _ZN17QCompletionEngine6filterERK5QListI7QStringE
inline void QCompletionEngine::filter(const QStringList& parts)
{
    const QAbstractItemModel *model = c->proxy->sourceModel();
    curParts = parts;
    if (curParts.isEmpty())
        curParts.append(QString());

    curRow = -1;
    curParent = QModelIndex();
    curMatch = QMatchData();
    historyMatch = filterHistory();

    if (!model)
        return;

    QModelIndex parent;
    for (int i = 0; i < curParts.size() - 1; i++) {
        QString part = curParts.at(i);
        int emi = filter(part, parent, -1).exactMatchIndex;
        if (emi == -1)
            return;
        parent = model->index(emi, c->column, parent);
    }

    // Note that we set the curParent to a valid parent, even if we have no matches
    // When filtering is disabled, we show all the items under this parent
    curParent = parent;
    if (curParts.constLast().isEmpty())
        curMatch = QMatchData(QIndexMapper(0, model->rowCount(curParent) - 1), -1, false);
    else
        curMatch = filter(curParts.constLast(), curParent, 1); // build at least one
    curRow = curMatch.isValid() ? 0 : -1;
}

//  from src/widgets/util/qcompleter.cpp, line 446, as _ZN17QCompletionEngine13filterHistoryEv
#if defined(Q_OS_LINUX)
inline QMatchData QCompletionEngine::filterHistory()
{
    QAbstractItemModel *source = c->proxy->sourceModel();
    if (curParts.size() <= 1 || c->proxy->showAll || !source)
        return QMatchData();

#if QT_CONFIG(filesystemmodel)
    const bool isFsModel = (qobject_cast<QFileSystemModel *>(source) != nullptr);
#else
    const bool isFsModel = false;
#endif
    Q_UNUSED(isFsModel);
    QList<int> v;
    QIndexMapper im(v);
    QMatchData m(im, -1, true);

    for (int i = 0; i < source->rowCount(); i++) {
        QString str = source->index(i, c->column).data().toString();
        if (str.startsWith(c->prefix, c->cs)
#if !defined(Q_OS_WIN)
            && (!isFsModel || QDir::toNativeSeparators(str) != QDir::separator())
#endif
            )
            m.indices.append(i);
    }
    return m;
}
#endif  // defined(Q_OS_LINUX)

//  from src/widgets/util/qcompleter.cpp, line 523, as _ZN17QCompletionEngine11saveInCacheE7QStringRK11QModelIndexRK10QMatchData
inline void QCompletionEngine::saveInCache(QString part, const QModelIndex& parent, const QMatchData& m)
{
    if (c->filterMode == Qt::MatchEndsWith)
        return;
    QMatchData old = cache[parent].take(part);
    cost = cost + m.indices.cost() - old.indices.cost();
    if (cost * sizeof(int) > 1024 * 1024) {
        QMap<QModelIndex, CacheItem>::iterator it1 = cache.begin();
        while (it1 != cache.end()) {
            CacheItem& ci = it1.value();
            int sz = ci.size()/2;
            QMap<QString, QMatchData>::iterator it2 = ci.begin();
            int i = 0;
            while (it2 != ci.end() && i < sz) {
                cost -= it2.value().indices.cost();
                it2 = ci.erase(it2);
                i++;
            }
            if (ci.size() == 0) {
              it1 = cache.erase(it1);
            } else {
              ++it1;
            }
        }
    }

    if (c->cs == Qt::CaseInsensitive)
        part = std::move(part).toLower();
    cache[parent][part] = m;
}

//  from src/widgets/util/qcompleter.cpp, line 555, as _ZN18QSortedModelEngine9indexHintE7QStringRK11QModelIndexN2Qt9SortOrderE
inline QIndexMapper QSortedModelEngine::indexHint(QString part, const QModelIndex& parent, Qt::SortOrder order)
{
    const QAbstractItemModel *model = c->proxy->sourceModel();

    if (c->cs == Qt::CaseInsensitive)
        part = std::move(part).toLower();

    const CacheItem& map = cache[parent];

    // Try to find a lower and upper bound for the search from previous results
    int to = model->rowCount(parent) - 1;
    int from = 0;
    const CacheItem::const_iterator it = map.lowerBound(part);

    // look backward for first valid hint
    for (CacheItem::const_iterator it1 = it; it1 != map.constBegin();) {
        --it1;
        const QMatchData& value = it1.value();
        if (value.isValid()) {
            if (order == Qt::AscendingOrder) {
                from = value.indices.last() + 1;
            } else {
                to = value.indices.first() - 1;
            }
            break;
        }
    }

    // look forward for first valid hint
    for(CacheItem::const_iterator it2 = it; it2 != map.constEnd(); ++it2) {
        const QMatchData& value = it2.value();
        if (value.isValid() && !it2.key().startsWith(part)) {
            if (order == Qt::AscendingOrder) {
                to = value.indices.first() - 1;
            } else {
                from = value.indices.first() + 1;
            }
            break;
        }
    }

    return QIndexMapper(from, to);
}

//  from src/widgets/util/qcompleter.cpp, line 699, as _ZN20QUnsortedModelEngine12buildIndicesERK7QStringRK11QModelIndexiRK12QIndexMapperP10QMatchData
inline int QUnsortedModelEngine::buildIndices(const QString& str, const QModelIndex& parent, int n,
                                      const QIndexMapper& indices, QMatchData* m)
{
    Q_ASSERT(m->partial);
    Q_ASSERT(n != -1 || m->exactMatchIndex == -1);
    const QAbstractItemModel *model = c->proxy->sourceModel();
    int i, count = 0;

    for (i = 0; i < indices.count() && count != n; ++i) {
        QModelIndex idx = model->index(indices[i], c->column, parent);

        if (!(model->flags(idx) & Qt::ItemIsSelectable))
            continue;

        QString data = model->data(idx, c->role).toString();

        switch (c->filterMode) {
        case Qt::MatchStartsWith:
            if (!data.startsWith(str, c->cs))
                continue;
            break;
        case Qt::MatchContains:
            if (!data.contains(str, c->cs))
                continue;
            break;
        case Qt::MatchEndsWith:
            if (!data.endsWith(str, c->cs))
                continue;
            break;
        case Qt::MatchExactly:
        case Qt::MatchFixedString:
        case Qt::MatchCaseSensitive:
        case Qt::MatchRegularExpression:
        case Qt::MatchWildcard:
        case Qt::MatchWrap:
        case Qt::MatchRecursive:
            Q_UNREACHABLE();
            break;
        }
        m->indices.append(indices[i]);
        ++count;
        if (m->exactMatchIndex == -1 && QString::compare(data, str, c->cs) == 0) {
            m->exactMatchIndex = indices[i];
            if (n == -1)
                return indices[i];
        }
    }
    return indices[i-1];
}

//  from src/widgets/util/qcompleter.cpp, line 501, as _ZNK17QCompletionEngine11lookupCacheERK7QStringRK11QModelIndexP10QMatchData
inline bool QCompletionEngine::lookupCache(const QString &part, const QModelIndex &parent, QMatchData *m) const
{
    if (part.isEmpty())
        return false; // early out to avoid cache[parent] lookup costs

    const auto cit = cache.find(parent);
    if (cit == cache.end())
        return false;

    const CacheItem& map = *cit;

    const QString key = c->cs == Qt::CaseInsensitive ? part.toLower() : part;

    const auto it = map.find(key);
    if (it == map.end())
        return false;

    *m = it.value();
    return true;
}

//  from src/widgets/util/qcompleter.cpp, line 475, as _ZNK17QCompletionEngine9matchHintERK7QStringRK11QModelIndexP10QMatchData
inline bool QCompletionEngine::matchHint(const QString &part, const QModelIndex &parent, QMatchData *hint) const
{
    if (part.isEmpty())
        return false; // early out to avoid cache[parent] lookup costs

    const auto cit = cache.find(parent);
    if (cit == cache.end())
        return false;

    const CacheItem& map = *cit;
    const auto mapEnd = map.end();

    QString key = c->cs == Qt::CaseInsensitive ? part.toLower() : part;

    while (!key.isEmpty()) {
        key.chop(1);
        const auto it = map.find(key);
        if (it != mapEnd) {
            *hint = *it;
            return true;
        }
    }

    return false;
}

//  from src/widgets/util/qcompleter.cpp, line 599, as _ZNK18QSortedModelEngine9sortOrderERK11QModelIndex
inline Qt::SortOrder QSortedModelEngine::sortOrder(const QModelIndex &parent) const
{
    const QAbstractItemModel *model = c->proxy->sourceModel();

    int rowCount = model->rowCount(parent);
    if (rowCount < 2)
        return Qt::AscendingOrder;
    QString first = model->data(model->index(0, c->column, parent), c->role).toString();
    QString last = model->data(model->index(rowCount - 1, c->column, parent), c->role).toString();
    return QString::compare(first, last, c->cs) <= 0 ? Qt::AscendingOrder : Qt::DescendingOrder;
}

//  from src/widgets/util/qcompleter.cpp, line 136, as _ZN16QCompletionModelC1EP17QCompleterPrivateP7QObject
inline QCompletionModel::QCompletionModel(QCompleterPrivate *c, QObject *parent)
    : QAbstractProxyModel(*new QCompletionModelPrivate, parent),
      c(c), showAll(false)
{
    createEngine();
}

//  from src/widgets/util/qcompleter.cpp, line 173, as _ZN16QCompletionModel12createEngineEv
inline void QCompletionModel::createEngine()
{
    bool sortedEngine = false;
    if (c->filterMode == Qt::MatchStartsWith) {
        switch (c->sorting) {
        case QCompleter::UnsortedModel:
            sortedEngine = false;
            break;
        case QCompleter::CaseSensitivelySortedModel:
            sortedEngine = c->cs == Qt::CaseSensitive;
            break;
        case QCompleter::CaseInsensitivelySortedModel:
            sortedEngine = c->cs == Qt::CaseInsensitive;
            break;
        }
    }

    if (sortedEngine)
        engine.reset(new QSortedModelEngine(c));
    else
        engine.reset(new QUnsortedModelEngine(c));
}

//  from src/widgets/util/qcompleter.cpp, line 339, as _ZN16QCompletionModel11setFilteredEb
inline void QCompletionModel::setFiltered(bool filtered)
{
    if (showAll == !filtered)
        return;
    beginResetModel();
    showAll = !filtered;
    endResetModel();
}

//  from src/widgets/util/qcompleter.cpp, line 387, as _ZN16QCompletionModel6filterERK5QListI7QStringE
inline void QCompletionModel::filter(const QStringList& parts)
{
    Q_D(QCompletionModel);
    beginResetModel();
    engine->filter(parts);
    endResetModel();

    if (d->model->canFetchMore(engine->curParent))
        d->model->fetchMore(engine->curParent);

#if QT_CONFIG(filesystemmodel)
    // No match can mean the directory being completed within was never listed by
    // the QFileSystemModel (e.g. a path set via setText() and then edited). Start
    // its listing so directoryLoaded() re-runs the completion. (QTBUG-148220)
    if (engine->matchCount() == 0 && parts.size() > 1) {
        if (auto *fsModel = qobject_cast<QFileSystemModel *>(d->model)) {
            const QModelIndex dirIndex = fsModel->index(QFileInfo(c->prefix).path());
            if (dirIndex.isValid() && fsModel->canFetchMore(dirIndex))
                fsModel->fetchMore(dirIndex);
        }
    }
#endif
}

//  from src/widgets/util/qcompleter.cpp, line 313, as _ZNK16QCompletionModel15completionCountEv
inline int QCompletionModel::completionCount() const
{
    if (!engine->matchCount())
        return 0;

    engine->filterOnDemand(INT_MAX);
    return engine->matchCount();
}

//  from src/widgets/util/qcompleter.cpp, line 259, as _ZN16QCompletionModel13setCurrentRowEi
inline bool QCompletionModel::setCurrentRow(int row)
{
    if (row < 0 || !engine->matchCount())
        return false;

    if (row >= engine->matchCount())
        engine->filterOnDemand(row + 1 - engine->matchCount());

    if (row >= engine->matchCount()) // invalid row
        return false;

    engine->curRow = row;
    return true;
}

//  from src/widgets/util/qcompleter.cpp, line 274, as _ZNK16QCompletionModel12currentIndexEb
inline QModelIndex QCompletionModel::currentIndex(bool sourceIndex) const
{
    if (!engine->matchCount())
        return QModelIndex();

    int row = engine->curRow;
    if (showAll)
        row = engine->curMatch.indices[engine->curRow];

    QModelIndex idx = createIndex(row, c->column);
    if (!sourceIndex)
        return idx;
    return mapToSource(idx);
}
//  -----------------------------------------------------------------------

//  A QCompletionModel that Python can take functions over in. Every QCompletionModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
typedef const QModelIndex * (*CuteQCompletionModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
typedef int (*CuteQCompletionModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
typedef int (*CuteQCompletionModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
typedef bool (*CuteQCompletionModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
typedef const QModelIndex * (*CuteQCompletionModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
typedef const QVariant * (*CuteQCompletionModelCall5)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(completer)
typedef void (*CuteQCompletionModelCall6)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(completer)
typedef const QModelIndex * (*CuteQCompletionModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(completer)
typedef const QModelIndex * (*CuteQCompletionModelCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
typedef const QItemSelection * (*CuteQCompletionModelCall9)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
typedef const QItemSelection * (*CuteQCompletionModelCall10)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQCompletionModelCall11)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef void (*CuteQCompletionModelCall12)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef const QVariant * (*CuteQCompletionModelCall13)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef int (*CuteQCompletionModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQCompletionModelCall15)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQCompletionModelCall16)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQCompletionModelCall17)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef const QModelIndex * (*CuteQCompletionModelCall18)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQCompletionModelCall19)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef void (*CuteQCompletionModelCall20)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef void (*CuteQCompletionModelCall21)(const void *, int, int, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef const QSize * (*CuteQCompletionModelCall22)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef const QModelIndex * (*CuteQCompletionModelCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQCompletionModelCall24)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQCompletionModelCall25)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef int (*CuteQCompletionModelCall26)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef int (*CuteQCompletionModelCall27)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQCompletionModelCall28)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQCompletionModelCall29)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQCompletionModelCall30)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQCompletionModelCall31)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQCompletionModelCall32)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQCompletionModelCall33)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQCompletionModelCall34)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQCompletionModelCall35)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCompletionModelCall36)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCompletionModelCall37)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompletionModelCall38)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompletionModelCall39)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompletionModelCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompletionModelCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompletionModelCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCompletionModel : public QCompletionModel {
public:
  using QCompletionModel::QCompletionModel;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemModel")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel11mapToSourceERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel13mapFromSourceERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSelection")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemSelection")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
  //  QModelIndex QCompletionModel::index(int row, int column, const
  //      QModelIndex &a2) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &a2) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCompletionModelCall0 call = reinterpret_cast<CuteQCompletionModelCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &a2, &handled);
      if (handled && given) return *given;
    }
    return QCompletionModel::index(row, column, a2);
  }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
  //  int QCompletionModel::rowCount(const QModelIndex &index) const
  int rowCount(const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCompletionModelCall1 call = reinterpret_cast<CuteQCompletionModelCall1>(taken[1]);
      int given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QCompletionModel::rowCount(index);
  }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
  //  int QCompletionModel::columnCount(const QModelIndex &index) const
  int columnCount(const QModelIndex &index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQCompletionModelCall2 call = reinterpret_cast<CuteQCompletionModelCall2>(taken[2]);
      int given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QCompletionModel::columnCount(index);
  }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
  //  bool QCompletionModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQCompletionModelCall3 call = reinterpret_cast<CuteQCompletionModelCall3>(taken[3]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QCompletionModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
  //  QModelIndex QCompletionModel::parent(const QModelIndex &a0) const
  QModelIndex parent(const QModelIndex &a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQCompletionModelCall4 call = reinterpret_cast<CuteQCompletionModelCall4>(taken[4]);
      const QModelIndex * given = call(this, &a0, &handled);
      if (handled && given) return *given;
    }
    return QCompletionModel::parent(a0);
  }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(completer)
  //  QVariant QCompletionModel::data(const QModelIndex &index, int role)
  //      const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQCompletionModelCall5 call = reinterpret_cast<CuteQCompletionModelCall5>(taken[5]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QCompletionModel::data(index, role);
  }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(completer)
  //  void QCompletionModel::setSourceModel(QAbstractItemModel
  //      *sourceModel)
  void setSourceModel(QAbstractItemModel *sourceModel) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCompletionModelCall6 call = reinterpret_cast<CuteQCompletionModelCall6>(taken[6]);
      call(this, sourceModel, &handled);
      if (handled) return;
    }
    QCompletionModel::setSourceModel(sourceModel);
  }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(completer)
  //  QModelIndex QCompletionModel::mapToSource(const QModelIndex
  //      &proxyIndex) const
  QModelIndex mapToSource(const QModelIndex &proxyIndex) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQCompletionModelCall7 call = reinterpret_cast<CuteQCompletionModelCall7>(taken[7]);
      const QModelIndex * given = call(this, &proxyIndex, &handled);
      if (handled && given) return *given;
    }
    return QCompletionModel::mapToSource(proxyIndex);
  }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(completer)
  //  QModelIndex QCompletionModel::mapFromSource(const QModelIndex
  //      &sourceIndex) const
  QModelIndex mapFromSource(const QModelIndex &sourceIndex) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQCompletionModelCall8 call = reinterpret_cast<CuteQCompletionModelCall8>(taken[8]);
      const QModelIndex * given = call(this, &sourceIndex, &handled);
      if (handled && given) return *given;
    }
    return QCompletionModel::mapFromSource(sourceIndex);
  }
#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
  //  QItemSelection QAbstractProxyModel::mapSelectionToSource(const
  //      QItemSelection &selection) const
  QItemSelection mapSelectionToSource(
      const QItemSelection &selection) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQCompletionModelCall9 call = reinterpret_cast<CuteQCompletionModelCall9>(taken[9]);
      const QItemSelection * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::mapSelectionToSource(selection);
  }
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
  //  QItemSelection QAbstractProxyModel::mapSelectionFromSource(const
  //      QItemSelection &selection) const
  QItemSelection mapSelectionFromSource(
      const QItemSelection &selection) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQCompletionModelCall10 call = reinterpret_cast<CuteQCompletionModelCall10>(taken[10]);
      const QItemSelection * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::mapSelectionFromSource(selection);
  }
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::submit()
  bool submit() override {
    if (taken[11]) {
      int handled = 0;
      CuteQCompletionModelCall11 call = reinterpret_cast<CuteQCompletionModelCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::submit();
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  void QAbstractProxyModel::revert()
  void revert() override {
    if (taken[12]) {
      int handled = 0;
      CuteQCompletionModelCall12 call = reinterpret_cast<CuteQCompletionModelCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::revert();
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  QVariant QAbstractProxyModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQCompletionModelCall13 call = reinterpret_cast<CuteQCompletionModelCall13>(taken[13]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  Qt::ItemFlags QAbstractProxyModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQCompletionModelCall14 call = reinterpret_cast<CuteQCompletionModelCall14>(taken[14]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QAbstractProxyModel::flags(index);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[15]) {
      int handled = 0;
      CuteQCompletionModelCall15 call = reinterpret_cast<CuteQCompletionModelCall15>(taken[15]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[16]) {
      int handled = 0;
      CuteQCompletionModelCall16 call = reinterpret_cast<CuteQCompletionModelCall16>(taken[16]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[17]) {
      int handled = 0;
      CuteQCompletionModelCall17 call = reinterpret_cast<CuteQCompletionModelCall17>(taken[17]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::clearItemData(index);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  QModelIndex QAbstractProxyModel::buddy(const QModelIndex &index)
  //      const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQCompletionModelCall18 call = reinterpret_cast<CuteQCompletionModelCall18>(taken[18]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::buddy(index);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQCompletionModelCall19 call = reinterpret_cast<CuteQCompletionModelCall19>(taken[19]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  void QAbstractProxyModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[20]) {
      int handled = 0;
      CuteQCompletionModelCall20 call = reinterpret_cast<CuteQCompletionModelCall20>(taken[20]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::fetchMore(parent);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  void QAbstractProxyModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[21]) {
      int handled = 0;
      CuteQCompletionModelCall21 call = reinterpret_cast<CuteQCompletionModelCall21>(taken[21]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractProxyModel::sort(column, order);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  QSize QAbstractProxyModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQCompletionModelCall22 call = reinterpret_cast<CuteQCompletionModelCall22>(taken[22]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::span(index);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  QModelIndex QAbstractProxyModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQCompletionModelCall23 call = reinterpret_cast<CuteQCompletionModelCall23>(taken[23]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::canDropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQCompletionModelCall24 call = reinterpret_cast<CuteQCompletionModelCall24>(taken[24]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[25]) {
      int handled = 0;
      CuteQCompletionModelCall25 call = reinterpret_cast<CuteQCompletionModelCall25>(taken[25]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  Qt::DropActions QAbstractProxyModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQCompletionModelCall26 call = reinterpret_cast<CuteQCompletionModelCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractProxyModel::supportedDragActions();
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  Qt::DropActions QAbstractProxyModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQCompletionModelCall27 call = reinterpret_cast<CuteQCompletionModelCall27>(taken[27]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractProxyModel::supportedDropActions();
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[28]) {
      int handled = 0;
      CuteQCompletionModelCall28 call = reinterpret_cast<CuteQCompletionModelCall28>(taken[28]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[29]) {
      int handled = 0;
      CuteQCompletionModelCall29 call = reinterpret_cast<CuteQCompletionModelCall29>(taken[29]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[30]) {
      int handled = 0;
      CuteQCompletionModelCall30 call = reinterpret_cast<CuteQCompletionModelCall30>(taken[30]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[31]) {
      int handled = 0;
      CuteQCompletionModelCall31 call = reinterpret_cast<CuteQCompletionModelCall31>(taken[31]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent,
  //      int sourceRow, int count, const QModelIndex &destinationParent,
  //      int destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[32]) {
      int handled = 0;
      CuteQCompletionModelCall32 call = reinterpret_cast<CuteQCompletionModelCall32>(taken[32]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent,
  //      int sourceColumn, int count, const QModelIndex
  //      &destinationParent, int destinationChild)
  bool moveColumns(
      const QModelIndex &sourceParent,
      int sourceColumn,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[33]) {
      int handled = 0;
      CuteQCompletionModelCall33 call = reinterpret_cast<CuteQCompletionModelCall33>(taken[33]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQCompletionModelCall34 call = reinterpret_cast<CuteQCompletionModelCall34>(taken[34]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[35]) {
      int handled = 0;
      CuteQCompletionModelCall35 call = reinterpret_cast<CuteQCompletionModelCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQCompletionModelCall36 call = reinterpret_cast<CuteQCompletionModelCall36>(taken[36]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQCompletionModelCall37 call = reinterpret_cast<CuteQCompletionModelCall37>(taken[37]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQCompletionModelCall38 call = reinterpret_cast<CuteQCompletionModelCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQCompletionModelCall39 call = reinterpret_cast<CuteQCompletionModelCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQCompletionModelCall40 call = reinterpret_cast<CuteQCompletionModelCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQCompletionModelCall41 call = reinterpret_cast<CuteQCompletionModelCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQCompletionModelCall42 call = reinterpret_cast<CuteQCompletionModelCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCompletionModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QCompletionModel10metaObjectEv(
    const QCompletionModel *self) {
  return self->metaObject();
}

//  void *QCompletionModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QCompletionModel11qt_metacastEPKc(
    QCompletionModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCompletionModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QCompletionModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QCompletionModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if defined(Q_OS_LINUX)
//  QString QCompletionModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QCompletionModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCompletionModel::tr(s, c, n));
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QCompletionModel::QCompletionModel(QCompleterPrivate *c, QObject *parent)
extern "C" Q_DECL_EXPORT
QCompletionModel *ritual_ZN16QCompletionModelC1EP17QCompleterPrivateP7QObject(
    QCompleterPrivate *c,
    QObject *parent) {
  return new CuteQCompletionModel(c, parent);
}
#endif  // defined(Q_OS_LINUX)

//  void QCompletionModel::createEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCompletionModel12createEngineEv(QCompletionModel *self) {
  self->createEngine();
}

//  void QCompletionModel::setFiltered(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCompletionModel11setFilteredEb(
    QCompletionModel *self,
    bool a0) {
  self->setFiltered(a0);
}

#if defined(Q_OS_LINUX)
//  void QCompletionModel::filter(const QStringList &parts)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCompletionModel6filterERK5QListI7QStringE(
    QCompletionModel *self,
    const QList<QString> *parts) {
  self->filter(*parts);
}
#endif  // defined(Q_OS_LINUX)

//  int QCompletionModel::completionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCompletionModel15completionCountEv(
    const QCompletionModel *self) {
  return self->completionCount();
}

//  int QCompletionModel::currentRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCompletionModel10currentRowEv(
    const QCompletionModel *self) {
  return self->currentRow();
}

//  bool QCompletionModel::setCurrentRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCompletionModel13setCurrentRowEi(
    QCompletionModel *self,
    int row) {
  return self->setCurrentRow(row);
}

//  QModelIndex QCompletionModel::currentIndex(bool a0) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QCompletionModel12currentIndexEb(
    const QCompletionModel *self,
    bool a0) {
  return new QModelIndex(self->currentIndex(a0));
}

//  QModelIndex QCompletionModel::index(int row, int column, const
//      QModelIndex &a2) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QCompletionModel5indexEiiRK11QModelIndex(
    const QCompletionModel *self,
    int row,
    int column,
    const QModelIndex *a2) {
  return new QModelIndex(self->index(row, column, *a2));
}

//  int QCompletionModel::rowCount(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCompletionModel8rowCountERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *index) {
  return self->rowCount(*index);
}

//  int QCompletionModel::columnCount(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QCompletionModel11columnCountERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *index) {
  return self->columnCount(*index);
}

//  bool QCompletionModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QCompletionModel11hasChildrenERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QModelIndex QCompletionModel::parent(const QModelIndex &a0) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QCompletionModel6parentERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *a0) {
  return new QModelIndex(self->parent(*a0));
}

//  QVariant QCompletionModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QCompletionModel4dataERK11QModelIndexi(
    const QCompletionModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  void QCompletionModel::setSourceModel(QAbstractItemModel *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCompletionModel14setSourceModelEP18QAbstractItemModel(
    QCompletionModel *self,
    QAbstractItemModel *sourceModel) {
  self->setSourceModel(sourceModel);
}

//  QModelIndex QCompletionModel::mapToSource(const QModelIndex &proxyIndex)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QCompletionModel11mapToSourceERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QCompletionModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QCompletionModel13mapFromSourceERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QCompletionModelPrivate *QCompletionModel::d_func()
extern "C" Q_DECL_EXPORT
QCompletionModelPrivate *ritual_ZN16QCompletionModel6d_funcEv(
    QCompletionModel *self) {
  return self->d_func();
}

//  const QCompletionModelPrivate *QCompletionModel::d_func() const
extern "C" Q_DECL_EXPORT
const QCompletionModelPrivate *ritual_ZNK16QCompletionModel6d_funcEv(
    const QCompletionModel *self) {
  return self->d_func();
}

//  void QCompletionModel::rowsAdded()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCompletionModel9rowsAddedEv(QCompletionModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCompletionModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rowsAdded()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rowsAdded()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCompletionModel::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCompletionModel10invalidateEv(QCompletionModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCompletionModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "invalidate()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "invalidate()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCompletionModel::rowsInserted()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCompletionModel12rowsInsertedEv(QCompletionModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCompletionModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rowsInserted()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rowsInserted()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCompletionModel::modelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCompletionModel14modelDestroyedEv(QCompletionModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCompletionModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "modelDestroyed()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "modelDestroyed()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQCompletionModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCompletionModel(
    QCompletionModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCompletionModel *>(self)->take(key, call);
}

//  QModelIndex QCompletionModel::index(int row, int column, const
//      QModelIndex &a2) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK16QCompletionModel5indexEiiRK11QModelIndex(
    const QCompletionModel *self,
    int row,
    int column,
    const QModelIndex *a2) {
  return new QModelIndex(self->QCompletionModel::index(row, column, *a2));
}

//  int QCompletionModel::rowCount(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QCompletionModel8rowCountERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *index) {
  return self->QCompletionModel::rowCount(*index);
}

//  int QCompletionModel::columnCount(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QCompletionModel11columnCountERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *index) {
  return self->QCompletionModel::columnCount(*index);
}

//  bool QCompletionModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QCompletionModel11hasChildrenERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *parent) {
  return self->QCompletionModel::hasChildren(*parent);
}

//  QModelIndex QCompletionModel::parent(const QModelIndex &a0) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK16QCompletionModel6parentERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *a0) {
  return new QModelIndex(self->QCompletionModel::parent(*a0));
}

//  QVariant QCompletionModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK16QCompletionModel4dataERK11QModelIndexi(
    const QCompletionModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QCompletionModel::data(*index, role));
}

#if defined(Q_OS_LINUX)
//  void QCompletionModel::setSourceModel(QAbstractItemModel *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QCompletionModel14setSourceModelEP18QAbstractItemModel(
    QCompletionModel *self,
    QAbstractItemModel *sourceModel) {
  self->QCompletionModel::setSourceModel(sourceModel);
}
#endif  // defined(Q_OS_LINUX)

//  QModelIndex QCompletionModel::mapToSource(const QModelIndex &proxyIndex)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK16QCompletionModel11mapToSourceERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->QCompletionModel::mapToSource(*proxyIndex));
}

//  QModelIndex QCompletionModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK16QCompletionModel13mapFromSourceERK11QModelIndex(
    const QCompletionModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(
      self->QCompletionModel::mapFromSource(
          *sourceIndex));
}

#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(completer)
