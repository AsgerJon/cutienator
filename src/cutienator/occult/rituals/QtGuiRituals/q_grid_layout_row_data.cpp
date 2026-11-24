//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#include <QtGui/private/qgridlayoutengine_p.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/QtDebug>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/util/qgridlayoutengine.cpp, line 120, as _ZN18QGridLayoutRowData5resetEi
inline void QGridLayoutRowData::reset(int count)
{
    ignore.fill(false, count);
    boxes.fill(QGridLayoutBox(), count);
    multiCellMap.clear();
    stretches.fill(0, count);
    spacings.fill(0.0, count);
    hasIgnoreFlag = false;
}

//  from src/gui/util/qgridlayoutengine.cpp, line 420, as _ZNK18QGridLayoutRowData8totalBoxEii
inline QGridLayoutBox QGridLayoutRowData::totalBox(int start, int end) const
{
    QGridLayoutBox result;
    if (start < end) {
        result.q_maximumSize = 0.0;
        qreal nextSpacing = 0.0;
        for (int i = start; i < end; ++i) {
            if (ignore.testBit(i))
                continue;
            result.add(boxes.at(i), stretches.at(i), nextSpacing);
            nextSpacing = spacings.at(i);
        }
    }
    return result;
}

//  from src/gui/util/qgridlayoutengine.cpp, line 436, as _ZN18QGridLayoutRowData8stealBoxEiiiPdS0_
inline void QGridLayoutRowData::stealBox(int start, int end, int which, qreal *positions, qreal *sizes)
{
    qreal offset = 0.0;
    qreal nextSpacing = 0.0;

    for (int i = start; i < end; ++i) {
        qreal avail = 0.0;

        if (!ignore.testBit(i)) {
            const QGridLayoutBox &box = boxes.at(i);
            avail = box.q_sizes(which);
            offset += nextSpacing;
            nextSpacing = spacings.at(i);
        }

        *positions++ = offset;
        *sizes++ = avail;
        offset += avail;
    }
}
//  -----------------------------------------------------------------------

//  void QGridLayoutRowData::reset(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGridLayoutRowData5resetEi(
    QGridLayoutRowData *self,
    int count) {
  self->reset(count);
}

//  QGridLayoutBox QGridLayoutRowData::totalBox(int start, int end) const
extern "C" Q_DECL_EXPORT
QGridLayoutBox *ritual_ZNK18QGridLayoutRowData8totalBoxEii(
    const QGridLayoutRowData *self,
    int start,
    int end) {
  return new QGridLayoutBox(self->totalBox(start, end));
}

//  void QGridLayoutRowData::stealBox(int start, int end, int which, qreal
//      *positions, qreal *sizes)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGridLayoutRowData8stealBoxEiiiPdS0_(
    QGridLayoutRowData *self,
    int start,
    int end,
    int which,
    qreal *positions,
    qreal *sizes) {
  self->stealBox(start, end, which, positions, sizes);
}

//  QGridLayoutRowData::~QGridLayoutRowData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGridLayoutRowDataD1Ev(QGridLayoutRowData *self) {
  delete self;
}
