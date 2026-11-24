//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpageranges_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpageranges_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qpageranges.h"
#include "qpageranges_p.h"
#include <QtCore/qstack.h>
#include <QtCore/qdebug.h>
#include <QtCore/qdatastream.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpageranges.cpp, line 16, as _ZN18QPageRangesPrivate14mergeIntervalsEv
inline void QPageRangesPrivate::mergeIntervals()
{
    const int count = intervals.size();

    if (count <= 1)
        return;

    std::sort(intervals.begin(), intervals.end());

    QStack<QPageRanges::Range> stack;
    stack.push(intervals[0]);

    for (int i = 1; i < count; ++i) {
        QPageRanges::Range &top = stack.top();

        if (top.to < intervals[i].from - 1)
            stack.push(intervals[i]);
        else if (top.to < intervals[i].to)
            top.to = intervals[i].to;
    }

    intervals = stack;
}
//  -----------------------------------------------------------------------

//  void QPageRangesPrivate::mergeIntervals()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPageRangesPrivate14mergeIntervalsEv(
    QPageRangesPrivate *self) {
  self->mergeIntervals();
}

//  QPageRangesPrivate::~QPageRangesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPageRangesPrivateD1Ev(QPageRangesPrivate *self) {
  delete self;
}
