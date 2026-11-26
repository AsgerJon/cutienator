//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpainterpath_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainterpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qbezier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/private/qpainterpath_p.h>
#include <QtGui/qbitmap.h>
#include <QtCore/qdebug.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qlist.h>
#include <QtGui/qpen.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qtextlayout.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qmath.h>
#include <QtGui/private/qbezier_p.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qobject_p.h>
#include <QtGui/private/qpathclipper_p.h>
#include <QtGui/private/qstroker_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <cmath>
#include <limits.h>
#if 0
#include <performance.h>
#else
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpainterpath.cpp, line 3064, as local:qpainterpath.cpp:uncached_bezierAtT
static inline QBezier uncached_bezierAtT(const QPainterPath &path, qreal t, qreal *startingLength,
                                         qreal *bezierLength)
{
    *startingLength = 0;
    if (t > 1)
        return QBezier();

    qreal curLen = 0;
    qreal totalLength = path.length();

    const int lastElement = path.elementCount() - 1;
    for (int i=0; i <= lastElement; ++i) {
        const QPainterPath::Element &e = path.elementAt(i);

        switch (e.type) {
        case QPainterPath::MoveToElement:
            break;
        case QPainterPath::LineToElement:
        {
            QLineF line(path.elementAt(i-1), e);
            qreal llen = line.length();
            curLen += llen;
            if (i == lastElement || curLen/totalLength >= t) {
                *bezierLength = llen;
                QPointF a = path.elementAt(i-1);
                QPointF delta = e - a;
                return QBezier::fromPoints(a, a + delta / 3, a + 2 * delta / 3, e);
            }
            break;
        }
        case QPainterPath::CurveToElement:
        {
            QBezier b = QBezier::fromPoints(path.elementAt(i-1),
                                            e,
                                            path.elementAt(i+1),
                                            path.elementAt(i+2));
            qreal blen = b.length();
            curLen += blen;

            if (i + 2 == lastElement || curLen/totalLength >= t) {
                *bezierLength = blen;
                return b;
            }

            i += 2;
            break;
        }
        default:
            break;
        }
        *startingLength = curLen;
    }
    return QBezier();
}

//  from src/gui/painting/qpainterpath.cpp, line 3706, as _ZN19QPainterPathPrivate17computeRunLengthsEv
inline void QPainterPathPrivate::computeRunLengths()
{
    Q_ASSERT(!elements.isEmpty());

    m_runLengths.clear();
    const int numElems = elements.size();
    m_runLengths.reserve(numElems);

    QPointF runPt = elements[0];
    qreal runLen = 0.0;
    for (int i = 0; i < numElems; i++) {
        QPainterPath::Element e = elements[i];
        switch (e.type) {
        case QPainterPath::LineToElement:
            runLen += QLineF(runPt, e).length();
            runPt = e;
            break;
        case QPainterPath::CurveToElement: {
            Q_ASSERT(i < numElems - 2);
            QPainterPath::Element ee = elements[i + 2];
            runLen += QBezier::fromPoints(runPt, e, elements[i + 1], ee).length();
            runPt = ee;
            break;
        }
        case QPainterPath::MoveToElement:
            runPt = e;
            break;
        case QPainterPath::CurveToDataElement:
            break;
        }
        m_runLengths.append(runLen);
    }
    Q_ASSERT(m_runLengths.size() == elements.size());

    dirtyRunLengths = false;
}

//  from src/gui/painting/qpainterpath.cpp, line 3119, as _ZNK19QPainterPathPrivate9bezierAtTERK12QPainterPathdPdS3_
inline QBezier QPainterPathPrivate::bezierAtT(const QPainterPath &path, qreal t, qreal *startingLength,
                                       qreal *bezierLength) const
{
    Q_ASSERT(t >= 0 && t <= 1);
    QPainterPathPrivate *d = path.d_func();
    if (!path.isEmpty() && d->cacheEnabled) {
        const int ei = qMax(d->elementAtT(t), 1); // Avoid the initial MoveTo element
        const qreal prevRunLength = d->m_runLengths[ei - 1];
        *startingLength = prevRunLength;
        *bezierLength = d->m_runLengths[ei] - prevRunLength;
        const QPointF prev = d->elements[ei - 1];
        const QPainterPath::Element &e = d->elements[ei];
        switch (e.type) {
        case QPainterPath::LineToElement:
        {
            QPointF delta = (e - prev) / 3;
            return QBezier::fromPoints(prev, prev + delta, prev + 2 * delta, e);
        }
        case QPainterPath::CurveToElement:
            return QBezier::fromPoints(prev, e, elements[ei + 1], elements[ei + 2]);
            break;
        default:
            Q_UNREACHABLE();
        }
    }

    return uncached_bezierAtT(path, t, startingLength, bezierLength);
}

//  from src/gui/painting/qpainterpath.cpp, line 3369, as _ZN19QPainterPathPrivate20appendTrimmedElementEP12QPainterPathiidd
inline void QPainterPathPrivate::appendTrimmedElement(QPainterPath *to, int elemIdx, int trimFlags,
                                               qreal startLen, qreal endLen)
{
    Q_ASSERT(cacheEnabled);
    Q_ASSERT(!dirtyRunLengths);

    if (elemIdx <= 0 || elemIdx >= elements.size())
        return;

    const qreal prevLen = m_runLengths.at(elemIdx - 1);
    const qreal elemLen = m_runLengths.at(elemIdx) - prevLen;
    const qreal len1 = startLen - prevLen;
    const qreal len2 = endLen - prevLen;
    if (qFuzzyIsNull(elemLen))
        return;

    const QPointF pp = elements.at(elemIdx - 1);
    const QPainterPath::Element e = elements.at(elemIdx);
    if (e.isLineTo()) {
        QLineF l(pp, e);
        QPointF p1 = (trimFlags & TrimStart) ? l.pointAt(len1 / elemLen) : pp;
        QPointF p2 = (trimFlags & TrimEnd) ? l.pointAt(len2 / elemLen) : e;
        if (to->isEmpty())
            to->moveTo(p1);
        to->lineTo(p2);
    } else if (e.isCurveTo()) {
        Q_ASSERT(elemIdx < elements.size() - 2);
        QBezier b = QBezier::fromPoints(pp, e, elements.at(elemIdx + 1), elements.at(elemIdx + 2));
        qreal t1 = (trimFlags & TrimStart) ? b.tAtLength(len1) : 0.0;  // or simply len1/elemLen to trim by t instead of len
        qreal t2 = (trimFlags & TrimEnd) ? b.tAtLength(len2) : 1.0;
        QBezier c = b.getSubRange(t1, t2);
        if (to->isEmpty())
            to->moveTo(c.pt1());
        to->cubicTo(c.pt2(), c.pt3(), c.pt4());
    } else {
        Q_UNREACHABLE();
    }
}

//  from src/gui/painting/qpainterpath.cpp, line 3408, as _ZN19QPainterPathPrivate18appendElementRangeEP12QPainterPathii
inline void QPainterPathPrivate::appendElementRange(QPainterPath *to, int first, int last)
{
    if (first < 0 || first >= elements.size() || last < 0 || last >= elements.size())
        return;

    // (Could optimize by direct copy of elements, but must ensure correct state flags)
    for (int i = first; i <= last; i++) {
        const QPainterPath::Element &e = elements.at(i);
        switch (e.type) {
        case QPainterPath::MoveToElement:
            to->moveTo(e);
            break;
        case QPainterPath::LineToElement:
            to->lineTo(e);
            break;
        case QPainterPath::CurveToElement:
            Q_ASSERT(i < elements.size() - 2);
            to->cubicTo(e, elements.at(i + 1), elements.at(i + 2));
            i += 2;
            break;
        default:
            // 'first' may point to CurveToData element, just skip it
            break;
        }
    }
}
//  -----------------------------------------------------------------------

//  QPainterPathPrivate::QPainterPathPrivate()
extern "C" Q_DECL_EXPORT
QPainterPathPrivate *ritual_ZN19QPainterPathPrivateC1Ev() {
  return new QPainterPathPrivate();
}

//  QPainterPathPrivate::QPainterPathPrivate(QPointF startPoint)
extern "C" Q_DECL_EXPORT
QPainterPathPrivate *ritual_ZN19QPainterPathPrivateC1E7QPointF(
    const QPointF *startPoint) {
  return new QPainterPathPrivate(*startPoint);
}

//  QPainterPathPrivate::QPainterPathPrivate(const QPainterPathPrivate
//      &other)
extern "C" Q_DECL_EXPORT
QPainterPathPrivate *ritual_ZN19QPainterPathPrivateC1ERKS_(
    const QPainterPathPrivate *other) {
  return new QPainterPathPrivate(*other);
}

//  QPainterPathPrivate::~QPainterPathPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivateD1Ev(QPainterPathPrivate *self) {
  delete self;
}

//  bool QPainterPathPrivate::isClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QPainterPathPrivate8isClosedEv(
    const QPainterPathPrivate *self) {
  return self->isClosed();
}

//  void QPainterPathPrivate::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivate5closeEv(QPainterPathPrivate *self) {
  self->close();
}

//  void QPainterPathPrivate::maybeMoveTo()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivate11maybeMoveToEv(
    QPainterPathPrivate *self) {
  self->maybeMoveTo();
}

//  void QPainterPathPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivate5clearEv(QPainterPathPrivate *self) {
  self->clear();
}

//  QPointF QPainterPathPrivate::endPointOfElement(int elemIdx) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QPainterPathPrivate17endPointOfElementEi(
    const QPainterPathPrivate *self,
    int elemIdx) {
  return new QPointF(self->endPointOfElement(elemIdx));
}

//  void QPainterPathPrivate::computeRunLengths()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivate17computeRunLengthsEv(
    QPainterPathPrivate *self) {
  self->computeRunLengths();
}

//  int QPainterPathPrivate::elementAtLength(qreal len)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QPainterPathPrivate15elementAtLengthEd(
    QPainterPathPrivate *self,
    qreal len) {
  return self->elementAtLength(len);
}

//  int QPainterPathPrivate::elementAtT(qreal t)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QPainterPathPrivate10elementAtTEd(
    QPainterPathPrivate *self,
    qreal t) {
  return self->elementAtT(t);
}

//  QBezier QPainterPathPrivate::bezierAtT(const QPainterPath &path, qreal t,
//      qreal *startingLength, qreal *bezierLength) const
extern "C" Q_DECL_EXPORT
QBezier *ritual_ZNK19QPainterPathPrivate9bezierAtTERK12QPainterPathdPdS3_(
    const QPainterPathPrivate *self,
    const QPainterPath *path,
    qreal t,
    qreal *startingLength,
    qreal *bezierLength) {
  return new QBezier(
      self->bezierAtT(
          *path,
          t,
          startingLength,
          bezierLength));
}

//  void QPainterPathPrivate::appendTrimmedElement(QPainterPath *to, int
//      elemIdx, int trimFlags, qreal startLen, qreal endLen)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivate20appendTrimmedElementEP12QPainterPathiidd(
    QPainterPathPrivate *self,
    QPainterPath *to,
    int elemIdx,
    int trimFlags,
    qreal startLen,
    qreal endLen) {
  self->appendTrimmedElement(to, elemIdx, trimFlags, startLen, endLen);
}

//  void QPainterPathPrivate::appendStartOfElement(QPainterPath *to, int
//      elemIdx, qreal len)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivate20appendStartOfElementEP12QPainterPathid(
    QPainterPathPrivate *self,
    QPainterPath *to,
    int elemIdx,
    qreal len) {
  self->appendStartOfElement(to, elemIdx, len);
}

//  void QPainterPathPrivate::appendEndOfElement(QPainterPath *to, int
//      elemIdx, qreal len)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivate18appendEndOfElementEP12QPainterPathid(
    QPainterPathPrivate *self,
    QPainterPath *to,
    int elemIdx,
    qreal len) {
  self->appendEndOfElement(to, elemIdx, len);
}

//  void QPainterPathPrivate::appendSliceOfElement(QPainterPath *to, int
//      elemIdx, qreal fromLen, qreal toLen)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivate20appendSliceOfElementEP12QPainterPathidd(
    QPainterPathPrivate *self,
    QPainterPath *to,
    int elemIdx,
    qreal fromLen,
    qreal toLen) {
  self->appendSliceOfElement(to, elemIdx, fromLen, toLen);
}

//  void QPainterPathPrivate::appendElementRange(QPainterPath *to, int first,
//      int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPainterPathPrivate18appendElementRangeEP12QPainterPathii(
    QPainterPathPrivate *self,
    QPainterPath *to,
    int first,
    int last) {
  self->appendElementRange(to, first, last);
}

//  const QVectorPath &QPainterPathPrivate::vectorPath()
extern "C" Q_DECL_EXPORT
const QVectorPath *ritual_ZN19QPainterPathPrivate10vectorPathEv(
    QPainterPathPrivate *self) {
  return &(self->vectorPath());
}
