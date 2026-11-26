//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtableview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tableview)
#if QT_CONFIG(tableview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtableview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QSet>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qtableview.h>
#include <QtWidgets/qheaderview.h>
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtCore/qsize.h>
#include <QtGui/qevent.h>
#include <QtCore/qbitarray.h>
#include <QtWidgets/qscrollbar.h>
#if QT_CONFIG(abstractbutton)
#include <QtWidgets/qabstractbutton.h>
#endif
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qtableview_p.h>
#include <QtWidgets/private/qheaderview_p.h>
#include <QtWidgets/private/qscrollbar_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
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

//  from src/widgets/itemviews/qtableview.cpp, line 36, as _ZN15QSpanCollection7addSpanEPNS_4SpanE
inline void QSpanCollection::addSpan(QSpanCollection::Span *span)
{
    spans.push_back(span);
    Index::iterator it_y = index.lowerBound(-span->top());
    if (it_y == index.end() || it_y.key() != -span->top()) {
        //there is no spans that starts with the row in the index, so create a sublist for it.
        SubIndex sub_index;
        if (it_y != index.end()) {
            //the previouslist is the list of spans that sarts _before_ the row of the span.
            // and which may intersect this row.
            const SubIndex previousList = it_y.value();
            for (Span *s : previousList) {
                //If a subspans intersect the row, we need to split it into subspans
                if (s->bottom() >= span->top())
                    sub_index.insert(-s->left(), s);
            }
        }
        it_y = index.insert(-span->top(), sub_index);
        //we will insert span to *it_y in the later loop
    }

    //insert the span as supspan in all the lists that intesects the span
    while(-it_y.key() <= span->bottom()) {
        (*it_y).insert(-span->left(), span);
        if (it_y == index.begin())
            break;
        --it_y;
    }
}

//  from src/widgets/itemviews/qtableview.cpp, line 74, as _ZN15QSpanCollection10updateSpanEPNS_4SpanEi
inline void QSpanCollection::updateSpan(QSpanCollection::Span *span, int old_height)
{
    if (old_height < span->height()) {
        //add the span as subspan in all the lists that intersect the new covered columns
        Index::iterator it_y = index.lowerBound(-(span->top() + old_height - 1));
        Q_ASSERT(it_y != index.end()); //it_y must exist since the span is in the list
        while (-it_y.key() <= span->bottom()) {
            (*it_y).insert(-span->left(), span);
            if (it_y == index.begin())
                break;
            --it_y;
        }
    } else if (old_height > span->height()) {
        //remove the span from all the subspans lists that intersect the columns not covered anymore
        Index::iterator it_y = index.lowerBound(-qMax(span->bottom(), span->top())); //qMax useful if height is 0
        Q_ASSERT(it_y != index.end()); //it_y must exist since the span is in the list
        while (-it_y.key() <= span->top() + old_height -1) {
            if (-it_y.key() > span->bottom()) {
                int removed = (*it_y).remove(-span->left());
                Q_ASSERT(removed == 1);
                Q_UNUSED(removed);
                if (it_y->isEmpty()) {
                    it_y = index.erase(it_y);
                }
            }
            if (it_y == index.begin())
                break;
            --it_y;
        }
    }

    if (span->width() == 0 && span->height() == 0) {
        spans.remove(span);
        delete span;
    }
}

//  from src/widgets/itemviews/qtableview.cpp, line 115, as _ZNK15QSpanCollection6spanAtEii
inline QSpanCollection::Span *QSpanCollection::spanAt(int x, int y) const
{
    Index::const_iterator it_y = index.lowerBound(-y);
    if (it_y == index.end())
        return nullptr;
    SubIndex::const_iterator it_x = (*it_y).lowerBound(-x);
    if (it_x == (*it_y).end())
        return nullptr;
    Span *span = *it_x;
    if (span->right() >= x && span->bottom() >= y)
        return span;
    return nullptr;
}

//  from src/widgets/itemviews/qtableview.cpp, line 133, as _ZN15QSpanCollection5clearEv
inline void QSpanCollection::clear()
{
    qDeleteAll(spans);
    index.clear();
    spans.clear();
}

//  from src/widgets/itemviews/qtableview.cpp, line 143, as _ZNK15QSpanCollection11spansInRectEiiii
inline QSet<QSpanCollection::Span *> QSpanCollection::spansInRect(int x, int y, int w, int h) const
{
    QSet<Span *> list;
    Index::const_iterator it_y = index.lowerBound(-y);
    if (it_y == index.end())
        --it_y;
    while(-it_y.key() <= y + h) {
        SubIndex::const_iterator it_x = (*it_y).lowerBound(-x);
        if (it_x == (*it_y).end())
            --it_x;
        while(-it_x.key() <= x + w) {
            Span *s = *it_x;
            if (s->bottom() >= y && s->right() >= x)
                list << s;
            if (it_x == (*it_y).begin())
                break;
            --it_x;
        }
        if (it_y == index.begin())
            break;
        --it_y;
    }
    return list;
}

//  from src/widgets/itemviews/qtableview.cpp, line 188, as _ZN15QSpanCollection18updateInsertedRowsEii
inline void QSpanCollection::updateInsertedRows(int start, int end)
{
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << start << end << Qt::endl << index;
#endif
    if (spans.empty())
        return;

    int delta = end - start + 1;
#ifdef DEBUG_SPAN_UPDATE
    qDebug("Before");
#endif
    for (Span *span : spans) {
#ifdef DEBUG_SPAN_UPDATE
        qDebug() << span << *span;
#endif
        if (span->m_bottom < start)
            continue;
        if (span->m_top >= start)
            span->m_top += delta;
        span->m_bottom += delta;
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug("After");
    qDebug() << spans;
#endif

    for (Index::iterator it_y = index.begin(); it_y != index.end(); ) {
        int y = -it_y.key();
        if (y < start) {
            ++it_y;
            continue;
        }

        index.insert(-y - delta, it_y.value());
        it_y = index.erase(it_y);
    }
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << index;
#endif
}

//  from src/widgets/itemviews/qtableview.cpp, line 234, as _ZN15QSpanCollection21updateInsertedColumnsEii
inline void QSpanCollection::updateInsertedColumns(int start, int end)
{
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << start << end << Qt::endl << index;
#endif
    if (spans.empty())
        return;

    int delta = end - start + 1;
#ifdef DEBUG_SPAN_UPDATE
    qDebug("Before");
#endif
    for (Span *span : spans) {
#ifdef DEBUG_SPAN_UPDATE
        qDebug() << span << *span;
#endif
        if (span->m_right < start)
            continue;
        if (span->m_left >= start)
            span->m_left += delta;
        span->m_right += delta;
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug("After");
    qDebug() << spans;
#endif

    for (Index::iterator it_y = index.begin(); it_y != index.end(); ++it_y) {
        SubIndex &subindex = it_y.value();
        for (SubIndex::iterator it = subindex.begin(); it != subindex.end(); ) {
            int x = -it.key();
            if (x < start) {
                ++it;
                continue;
            }
            subindex.insert(-x - delta, it.value());
            it = subindex.erase(it);
        }
    }
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << index;
#endif
}

//  from src/widgets/itemviews/qtableview.cpp, line 313, as _ZN15QSpanCollection17updateRemovedRowsEii
inline void QSpanCollection::updateRemovedRows(int start, int end)
{
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << start << end << Qt::endl << index;
#endif
    if (spans.empty())
        return;

    SpanList spansToBeDeleted;
    int delta = end - start + 1;
#ifdef DEBUG_SPAN_UPDATE
    qDebug("Before");
#endif
    for (SpanList::iterator it = spans.begin(); it != spans.end(); ) {
        Span *span = *it;
#ifdef DEBUG_SPAN_UPDATE
        qDebug() << span << *span;
#endif
        if (span->m_bottom < start) {
            ++it;
            continue;
        }
        if (span->m_top < start) {
            if (span->m_bottom <= end)
                span->m_bottom = start - 1;
            else
                span->m_bottom -= delta;
        } else {
            if (span->m_bottom > end) {
                if (span->m_top <= end)
                    span->m_top = start;
                else
                    span->m_top -= delta;
                span->m_bottom -= delta;
            } else {
                span->will_be_deleted = true;
            }
        }
        if (span->m_top == span->m_bottom && span->m_left == span->m_right)
            span->will_be_deleted = true;
        if (span->will_be_deleted) {
            spansToBeDeleted.push_back(span);
            it = spans.erase(it);
        } else {
            ++it;
        }
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug("After");
    qDebug() << spans;
#endif
    if (spans.empty()) {
        qDeleteAll(spansToBeDeleted);
        index.clear();
        return;
    }

    Index::iterator it_y = index.end();
    do {
        --it_y;
        int y = -it_y.key();
        SubIndex &subindex = it_y.value();
        if (y < start) {
            if (cleanSpanSubIndex(subindex, y))
                it_y = index.erase(it_y);
        } else if (y >= start && y <= end) {
            bool span_at_start = false;
            SubIndex spansToBeMoved;
            for (SubIndex::iterator it = subindex.begin(); it != subindex.end(); ++it) {
                Span *span = it.value();
                if (span->will_be_deleted)
                    continue;
                if (!span_at_start && span->m_top == start)
                    span_at_start = true;
                spansToBeMoved.insert(it.key(), span);
            }

            if (y == start && span_at_start)
                subindex.clear();
            else
                it_y = index.erase(it_y);

            if (span_at_start) {
                Index::iterator it_start;
                if (y == start)
                    it_start = it_y;
                else {
                    it_start = index.find(-start);
                    if (it_start == index.end())
                        it_start = index.insert(-start, SubIndex());
                }
                SubIndex &start_subindex = it_start.value();
                for (SubIndex::iterator it = spansToBeMoved.begin(); it != spansToBeMoved.end(); ++it)
                    start_subindex.insert(it.key(), it.value());
            }
        } else {
            if (y == end + 1) {
                Index::iterator it_top = index.find(-y + delta);
                if (it_top == index.end())
                    it_top = index.insert(-y + delta, SubIndex());
                for (SubIndex::iterator it = subindex.begin(); it != subindex.end(); ) {
                    Span *span = it.value();
                    if (!span->will_be_deleted)
                        it_top.value().insert(it.key(), span);
                    ++it;
                }
            } else {
                index.insert(-y + delta, subindex);
            }
            it_y = index.erase(it_y);
        }
    } while (it_y != index.begin());

#ifdef DEBUG_SPAN_UPDATE
    qDebug() << index;
    qDebug("Deleted");
    qDebug() << spansToBeDeleted;
#endif
    qDeleteAll(spansToBeDeleted);
}

//  from src/widgets/itemviews/qtableview.cpp, line 438, as _ZN15QSpanCollection20updateRemovedColumnsEii
inline void QSpanCollection::updateRemovedColumns(int start, int end)
{
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << start << end << Qt::endl << index;
#endif
    if (spans.empty())
        return;

    SpanList toBeDeleted;
    int delta = end - start + 1;
#ifdef DEBUG_SPAN_UPDATE
    qDebug("Before");
#endif
    for (SpanList::iterator it = spans.begin(); it != spans.end(); ) {
        Span *span = *it;
#ifdef DEBUG_SPAN_UPDATE
        qDebug() << span << *span;
#endif
        if (span->m_right < start) {
            ++it;
            continue;
        }
        if (span->m_left < start) {
            if (span->m_right <= end)
                span->m_right = start - 1;
            else
                span->m_right -= delta;
        } else {
            if (span->m_right > end) {
                if (span->m_left <= end)
                    span->m_left = start;
                else
                    span->m_left -= delta;
                span->m_right -= delta;
            } else {
                span->will_be_deleted = true;
            }
        }
        if (span->m_top == span->m_bottom && span->m_left == span->m_right)
            span->will_be_deleted = true;
        if (span->will_be_deleted) {
            toBeDeleted.push_back(span);
            it = spans.erase(it);
        } else {
            ++it;
        }
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug("After");
    qDebug() << spans;
#endif
    if (spans.empty()) {
        qDeleteAll(toBeDeleted);
        index.clear();
        return;
    }

    for (Index::iterator it_y = index.begin(); it_y != index.end(); ) {
        int y = -it_y.key();
        if (cleanSpanSubIndex(it_y.value(), y, true))
            it_y = index.erase(it_y);
        else
            ++it_y;
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug() << index;
    qDebug("Deleted");
    qDebug() << toBeDeleted;
#endif
    qDeleteAll(toBeDeleted);
}

//  from src/widgets/itemviews/qtableview.cpp, line 284, as _ZN15QSpanCollection17cleanSpanSubIndexER4QMapIiPNS_4SpanEEib
inline bool QSpanCollection::cleanSpanSubIndex(QSpanCollection::SubIndex &subindex, int y, bool update)
{
    if (subindex.isEmpty())
        return true;

    bool should_be_deleted = true;
    SubIndex::iterator it = subindex.end();
    do {
        --it;
        int x = -it.key();
        Span *span = it.value();
        if (span->will_be_deleted) {
            it = subindex.erase(it);
            continue;
        }
        if (update && span->m_left != x) {
            subindex.insert(-span->m_left, span);
            it = subindex.erase(it);
        }
        if (should_be_deleted && span->m_top == y)
            should_be_deleted = false;
    } while (it != subindex.begin());

    return should_be_deleted;
}
//  -----------------------------------------------------------------------

//  QSpanCollection::~QSpanCollection()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpanCollectionD1Ev(QSpanCollection *self) {
  delete self;
}

//  void QSpanCollection::addSpan(Span *span)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpanCollection7addSpanEPNS_4SpanE(
    QSpanCollection *self,
    QSpanCollection::Span *span) {
  self->addSpan(span);
}

//  void QSpanCollection::updateSpan(Span *span, int old_height)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpanCollection10updateSpanEPNS_4SpanEi(
    QSpanCollection *self,
    QSpanCollection::Span *span,
    int old_height) {
  self->updateSpan(span, old_height);
}

//  Span *QSpanCollection::spanAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QSpanCollection::Span *ritual_ZNK15QSpanCollection6spanAtEii(
    const QSpanCollection *self,
    int x,
    int y) {
  return self->spanAt(x, y);
}

//  void QSpanCollection::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpanCollection5clearEv(QSpanCollection *self) {
  self->clear();
}

//  QSet<Span *> QSpanCollection::spansInRect(int x, int y, int w, int h)
//      const
extern "C" Q_DECL_EXPORT
QSet<QSpanCollection::Span *> *ritual_ZNK15QSpanCollection11spansInRectEiiii(
    const QSpanCollection *self,
    int x,
    int y,
    int w,
    int h) {
  return new QSet<QSpanCollection::Span *>(self->spansInRect(x, y, w, h));
}

//  void QSpanCollection::updateInsertedRows(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpanCollection18updateInsertedRowsEii(
    QSpanCollection *self,
    int start,
    int end) {
  self->updateInsertedRows(start, end);
}

//  void QSpanCollection::updateInsertedColumns(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpanCollection21updateInsertedColumnsEii(
    QSpanCollection *self,
    int start,
    int end) {
  self->updateInsertedColumns(start, end);
}

//  void QSpanCollection::updateRemovedRows(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpanCollection17updateRemovedRowsEii(
    QSpanCollection *self,
    int start,
    int end) {
  self->updateRemovedRows(start, end);
}

//  void QSpanCollection::updateRemovedColumns(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpanCollection20updateRemovedColumnsEii(
    QSpanCollection *self,
    int start,
    int end) {
  self->updateRemovedColumns(start, end);
}

//  bool QSpanCollection::cleanSpanSubIndex(SubIndex &subindex, int end, bool
//      update)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSpanCollection17cleanSpanSubIndexER4QMapIiPNS_4SpanEEib(
    QSpanCollection *self,
    QSpanCollection::SubIndex *subindex,
    int end,
    bool update) {
  return self->cleanSpanSubIndex(*subindex, end, update);
}

//  a QSet<QSpanCollection::Span *> a ritual of QSpanCollection gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSpanCollection__QSet_QSpanCollection_Span(
    QSet<QSpanCollection::Span *> *self) {
  delete self;
}

#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(tableview)
