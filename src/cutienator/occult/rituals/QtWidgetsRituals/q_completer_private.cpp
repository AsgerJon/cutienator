//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(completer)
#if QT_CONFIG(completer)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qcompleter.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qitemselectionmodel.h>
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

//  from src/widgets/util/qcompleter.cpp, line 804, as _ZN17QCompleterPrivateC1Ev
inline QCompleterPrivate::QCompleterPrivate()
    : widget(nullptr),
      proxy(nullptr),
      popup(nullptr),
      filterMode(Qt::MatchStartsWith),
      cs(Qt::CaseSensitive),
      role(Qt::EditRole),
      column(0),
      maxVisibleItems(7),
      sorting(QCompleter::UnsortedModel),
      wrap(true),
      eatFocusOut(true),
      hiddenBecauseNoMatch(false)
{
}

//  from src/widgets/util/qcompleter.cpp, line 820, as _ZN17QCompleterPrivate4initEP18QAbstractItemModel
inline void QCompleterPrivate::init(QAbstractItemModel *m)
{
    Q_Q(QCompleter);
    proxy = new QCompletionModel(this, q);
    QObject::connect(proxy, SIGNAL(rowsAdded()), q, SLOT(_q_autoResizePopup()));
    q->setModel(m);
#if !QT_CONFIG(listview)
    q->setCompletionMode(QCompleter::InlineCompletion);
#else
    q->setCompletionMode(QCompleter::PopupCompletion);
#endif // QT_CONFIG(listview)
}

//  from src/widgets/util/qcompleter.cpp, line 902, as _ZN17QCompleterPrivate9showPopupERK5QRect
inline void QCompleterPrivate::showPopup(const QRect& rect)
{
    const QRect screen = widget->screen()->availableGeometry();
    QPoint pos;
    int rh, w;
    int h = (popup->sizeHintForRow(0) * qMin(maxVisibleItems, popup->model()->rowCount()) + 3) + 3;
    QScrollBar *hsb = popup->horizontalScrollBar();
    if (hsb && hsb->isVisible())
        h += popup->horizontalScrollBar()->sizeHint().height();

    if (rect.isValid()) {
        rh = rect.height();
        w = rect.width();
        pos = widget->mapToGlobal(rect.bottomLeft());
    } else {
        rh = widget->height();
        pos = widget->mapToGlobal(QPoint(0, widget->height() - 2));
        w = widget->width();
    }

    if (w > screen.width())
        w = screen.width();
    if ((pos.x() + w) > (screen.x() + screen.width()))
        pos.setX(screen.x() + screen.width() - w);
    if (pos.x() < screen.x())
        pos.setX(screen.x());

    int top = pos.y() - rh - screen.top() + 2;
    int bottom = screen.bottom() - pos.y();
    h = qMax(h, popup->minimumHeight());
    if (h > bottom) {
        h = qMin(qMax(top, bottom), h);

        if (top > bottom)
            pos.setY(pos.y() - h - rh + 2);
    }

    popup->setGeometry(pos.x(), pos.y(), w, h);

    if (!popup->isVisible()) {
#if QT_CONFIG(wayland)
        popup->createWinId();
        if (auto waylandWindow = dynamic_cast<QNativeInterface::Private::QWaylandWindow*>(popup->windowHandle()->handle())) {
            popup->windowHandle()->setTransientParent(widget->window()->windowHandle());
            if (!rect.isValid()) { // Automatically positioned popup
                const QRect controlGeometry = QRect(
                        widget->mapTo(widget->topLevelWidget(), QPoint(0, 0)), widget->size());
                waylandWindow->setParentControlGeometry(controlGeometry);
                waylandWindow->setExtendedWindowType(
                        QNativeInterface::Private::QWaylandWindow::ComboBox);
            }
        }
#endif
        popup->show();
    }
}

//  from src/widgets/util/qcompleter.cpp, line 863, as _ZN17QCompleterPrivate11_q_completeE11QModelIndexb
inline void QCompleterPrivate::_q_complete(QModelIndex index, bool highlighted)
{
    Q_Q(QCompleter);
    QString completion;

    if (!index.isValid() || (!proxy->showAll && (index.row() >= proxy->engine->matchCount()))) {
        completion = prefix;
        index = QModelIndex();
    } else {
        if (!(index.flags() & Qt::ItemIsEnabled))
            return;
        QModelIndex si = proxy->mapToSource(index);
        si = si.sibling(si.row(), column); // for clicked()
        completion = q->pathFromIndex(si);
#if QT_CONFIG(filesystemmodel)
        // add a trailing separator in inline
        if (mode == QCompleter::InlineCompletion) {
            if (qobject_cast<QFileSystemModel *>(proxy->sourceModel()) && QFileInfo(completion).isDir())
                completion += QDir::separator();
        }
#endif
    }

    if (highlighted) {
        emit q->highlighted(index);
        emit q->highlighted(completion);
    } else {
        emit q->activated(index);
        emit q->activated(completion);
    }
}

//  from src/widgets/util/qcompleter.cpp, line 854, as _ZN17QCompleterPrivate21_q_completionSelectedERK14QItemSelection
inline void QCompleterPrivate::_q_completionSelected(const QItemSelection& selection)
{
    QModelIndex index;
    if (const auto indexes = selection.indexes(); !indexes.isEmpty())
        index = indexes.first();

    _q_complete(index, true);
}

//  from src/widgets/util/qcompleter.cpp, line 895, as _ZN17QCompleterPrivate18_q_autoResizePopupEv
inline void QCompleterPrivate::_q_autoResizePopup()
{
    if (!popup || !popup->isVisible())
        return;
    showPopup(popupRect);
}

//  from src/widgets/util/qcompleter.cpp, line 833, as _ZN17QCompleterPrivate15setCurrentIndexE11QModelIndexb
inline void QCompleterPrivate::setCurrentIndex(QModelIndex index, bool select)
{
    Q_Q(QCompleter);
    if (!q->popup())
        return;
    if (!select) {
        popup->selectionModel()->setCurrentIndex(index, QItemSelectionModel::NoUpdate);
    } else {
        if (!index.isValid())
            popup->selectionModel()->clear();
        else
            popup->selectionModel()->setCurrentIndex(index, QItemSelectionModel::Select
                                                            | QItemSelectionModel::Rows);
    }
    index = popup->selectionModel()->currentIndex();
    if (!index.isValid())
        popup->scrollToTop();
    else
        popup->scrollTo(index, QAbstractItemView::PositionAtTop);
}
//  -----------------------------------------------------------------------

//  QCompleter *QCompleterPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZN17QCompleterPrivate6q_funcEv(QCompleterPrivate *self) {
  return self->q_func();
}

//  const QCompleter *QCompleterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCompleter *ritual_ZNK17QCompleterPrivate6q_funcEv(
    const QCompleterPrivate *self) {
  return self->q_func();
}

//  QCompleterPrivate::QCompleterPrivate()
extern "C" Q_DECL_EXPORT
QCompleterPrivate *ritual_ZN17QCompleterPrivateC1Ev() {
  return new QCompleterPrivate();
}

//  QCompleterPrivate::~QCompleterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivateD1Ev(QCompleterPrivate *self) {
  delete self;
}

//  void QCompleterPrivate::init(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate4initEP18QAbstractItemModel(
    QCompleterPrivate *self,
    QAbstractItemModel *model) {
  self->init(model);
}

//  void QCompleterPrivate::showPopup(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate9showPopupERK5QRect(
    QCompleterPrivate *self,
    const QRect *a0) {
  self->showPopup(*a0);
}

//  void QCompleterPrivate::_q_complete(QModelIndex a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate11_q_completeE11QModelIndexb(
    QCompleterPrivate *self,
    const QModelIndex *a0,
    bool a1) {
  self->_q_complete(*a0, a1);
}

//  void QCompleterPrivate::_q_completionSelected(const QItemSelection &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate21_q_completionSelectedERK14QItemSelection(
    QCompleterPrivate *self,
    const QItemSelection *a0) {
  self->_q_completionSelected(*a0);
}

//  void QCompleterPrivate::_q_autoResizePopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate18_q_autoResizePopupEv(
    QCompleterPrivate *self) {
  self->_q_autoResizePopup();
}

//  void QCompleterPrivate::setCurrentIndex(QModelIndex a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate15setCurrentIndexE11QModelIndexb(
    QCompleterPrivate *self,
    const QModelIndex *a0,
    bool a1) {
  self->setCurrentIndex(*a0, a1);
}

//  QCompleterPrivate *QCompleterPrivate::get(QCompleter *o)
extern "C" Q_DECL_EXPORT
QCompleterPrivate *ritual_ZN17QCompleterPrivate3getEP10QCompleter(
    QCompleter *o) {
  return QCompleterPrivate::get(o);
}

//  const QCompleterPrivate *QCompleterPrivate::get(const QCompleter *o)
extern "C" Q_DECL_EXPORT
const QCompleterPrivate *ritual_ZN17QCompleterPrivate3getEPK10QCompleter(
    const QCompleter *o) {
  return QCompleterPrivate::get(o);
}

#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(completer)
