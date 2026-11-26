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
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
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
//  -----------------------------------------------------------------------

//  QUnsortedModelEngine::QUnsortedModelEngine(QCompleterPrivate *c)
extern "C" Q_DECL_EXPORT
QUnsortedModelEngine *ritual_ZN20QUnsortedModelEngineC1EP17QCompleterPrivate(
    QCompleterPrivate *c) {
  return new QUnsortedModelEngine(c);
}

//  void QUnsortedModelEngine::filterOnDemand(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QUnsortedModelEngine14filterOnDemandEi(
    QUnsortedModelEngine *self,
    int a0) {
  self->filterOnDemand(a0);
}

//  QMatchData QUnsortedModelEngine::filter(const QString &a0, const
//      QModelIndex &a1, int a2)
extern "C" Q_DECL_EXPORT
QMatchData *ritual_ZN20QUnsortedModelEngine6filterERK7QStringRK11QModelIndexi(
    QUnsortedModelEngine *self,
    const QString *a0,
    const QModelIndex *a1,
    int a2) {
  return new QMatchData(self->filter(*a0, *a1, a2));
}

//  int QUnsortedModelEngine::buildIndices(const QString &str, const
//      QModelIndex &parent, int n, const QIndexMapper &iv, QMatchData *m)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QUnsortedModelEngine12buildIndicesERK7QStringRK11QModelIndexiRK12QIndexMapperP10QMatchData(
    QUnsortedModelEngine *self,
    const QString *str,
    const QModelIndex *parent,
    int n,
    const QIndexMapper *iv,
    QMatchData *m) {
  return self->buildIndices(*str, *parent, n, *iv, m);
}

//  QUnsortedModelEngine::~QUnsortedModelEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QUnsortedModelEngineD1Ev(QUnsortedModelEngine *self) {
  delete self;
}

//  void QUnsortedModelEngine::filterOnDemand(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QUnsortedModelEngine14filterOnDemandEi(
    QUnsortedModelEngine *self,
    int a0) {
  self->QUnsortedModelEngine::filterOnDemand(a0);
}

//  QMatchData QUnsortedModelEngine::filter(const QString &a0, const
//      QModelIndex &a1, int a2)
extern "C" Q_DECL_EXPORT
QMatchData *ritual_own_ZN20QUnsortedModelEngine6filterERK7QStringRK11QModelIndexi(
    QUnsortedModelEngine *self,
    const QString *a0,
    const QModelIndex *a1,
    int a2) {
  return new QMatchData(self->QUnsortedModelEngine::filter(*a0, *a1, a2));
}

#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(completer)
