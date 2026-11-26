//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes
//  made here are lost.
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
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

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
//  -----------------------------------------------------------------------

//  A QSortedModelEngine that Python can take functions over in. Every QSortedModelEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(completer)
typedef const QMatchData * (*CuteQSortedModelEngineCall0)(const void *, const QString *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(completer)
#if QT_CONFIG(completer)
typedef void (*CuteQSortedModelEngineCall1)(const void *, int, int *);
#endif  // QT_CONFIG(completer)
class CuteQSortedModelEngine : public QSortedModelEngine {
public:
  using QSortedModelEngine::QSortedModelEngine;
  CuteQSortedModelEngine(const QSortedModelEngine & other) : QSortedModelEngine(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZN17QCompletionEngine6filterERK7QStringRK11QModelIndexi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZN17QCompletionEngine14filterOnDemandEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
    return false;
  }

#if QT_CONFIG(completer)
  //  QMatchData QSortedModelEngine::filter(const QString &a0, const
  //      QModelIndex &a1, int a2)
  QMatchData filter(
      const QString &a0,
      const QModelIndex &a1,
      int a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSortedModelEngineCall0 call = reinterpret_cast<CuteQSortedModelEngineCall0>(taken[0]);
      const QMatchData * given = call(this, &a0, &a1, a2, &handled);
      if (handled && given) return *given;
    }
    return QSortedModelEngine::filter(a0, a1, a2);
  }
#endif  // QT_CONFIG(completer)

#if QT_CONFIG(completer)
  //  void QCompletionEngine::filterOnDemand(int a0)
  void filterOnDemand(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSortedModelEngineCall1 call = reinterpret_cast<CuteQSortedModelEngineCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QCompletionEngine::filterOnDemand(a0);
  }
#endif  // QT_CONFIG(completer)
};

//  QSortedModelEngine::QSortedModelEngine(QCompleterPrivate *c)
extern "C" Q_DECL_EXPORT
QSortedModelEngine *ritual_ZN18QSortedModelEngineC1EP17QCompleterPrivate(
    QCompleterPrivate *c) {
  return new CuteQSortedModelEngine(c);
}

//  QMatchData QSortedModelEngine::filter(const QString &a0, const
//      QModelIndex &a1, int a2)
extern "C" Q_DECL_EXPORT
QMatchData *ritual_ZN18QSortedModelEngine6filterERK7QStringRK11QModelIndexi(
    QSortedModelEngine *self,
    const QString *a0,
    const QModelIndex *a1,
    int a2) {
  return new QMatchData(self->filter(*a0, *a1, a2));
}

//  QIndexMapper QSortedModelEngine::indexHint(QString a0, const QModelIndex
//      &a1, Qt::SortOrder a2)
extern "C" Q_DECL_EXPORT
QIndexMapper *ritual_ZN18QSortedModelEngine9indexHintE7QStringRK11QModelIndexN2Qt9SortOrderE(
    QSortedModelEngine *self,
    const QString *a0,
    const QModelIndex *a1,
    Qt::SortOrder a2) {
  return new QIndexMapper(self->indexHint(*a0, *a1, a2));
}

//  Qt::SortOrder QSortedModelEngine::sortOrder(const QModelIndex &a0) const
extern "C" Q_DECL_EXPORT
Qt::SortOrder ritual_ZNK18QSortedModelEngine9sortOrderERK11QModelIndex(
    const QSortedModelEngine *self,
    const QModelIndex *a0) {
  return self->sortOrder(*a0);
}

//  QSortedModelEngine::~QSortedModelEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSortedModelEngineD1Ev(QSortedModelEngine *self) {
  delete self;
}

//  a Python function taken by a CuteQSortedModelEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSortedModelEngine(
    QSortedModelEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSortedModelEngine *>(self)->take(key, call);
}

//  QMatchData QSortedModelEngine::filter(const QString &a0, const
//      QModelIndex &a1, int a2)
extern "C" Q_DECL_EXPORT
QMatchData *ritual_own_ZN18QSortedModelEngine6filterERK7QStringRK11QModelIndexi(
    QSortedModelEngine *self,
    const QString *a0,
    const QModelIndex *a1,
    int a2) {
  return new QMatchData(self->QSortedModelEngine::filter(*a0, *a1, a2));
}

#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(completer)
