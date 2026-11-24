//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qsplitter_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qsplitter.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qsplitter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qframe.h>
#include <QtGui/qbitmap.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qframe_p.h>
#include <QtWidgets/qsplitter.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qcursor.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qlayout.h>
#include <QtCore/qlist.h>
#include <QtGui/qpainter.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/qrubberband.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qvarlengtharray.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#include <QtWidgets/private/qsplitter_p.h>
#include <QtCore/qdebug.h>
#include <ctype.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qframe.cpp, line 19, as _ZN13QFramePrivateC2Ev
inline QFramePrivate::QFramePrivate()
    : frect(0, 0, 0, 0),
      frameStyle(QFrame::NoFrame | QFrame::Plain),
      lineWidth(1),
      midLineWidth(0),
      frameWidth(0),
      leftFrameWidth(0), rightFrameWidth(0),
      topFrameWidth(0), bottomFrameWidth(0)
{
}

//  from src/widgets/widgets/qframe.cpp, line 30, as _ZN13QFramePrivateD2Ev
inline QFramePrivate::~QFramePrivate()
{
}

//  from src/widgets/widgets/qsplitter.cpp, line 346, as _ZN21QSplitterLayoutStruct13getHandleSizeEN2Qt11OrientationE
inline int QSplitterLayoutStruct::getHandleSize(Qt::Orientation orient)
{
    return pick(handle->sizeHint(), orient);
}

//  from src/widgets/widgets/qsplitter.cpp, line 327, as _ZN21QSplitterLayoutStruct13getWidgetSizeEN2Qt11OrientationE
inline int QSplitterLayoutStruct::getWidgetSize(Qt::Orientation orient)
{
    if (sizer == -1) {
        QSize s = widget->sizeHint();
        const int presizer = pick(s, orient);
        const int realsize = pick(widget->size(), orient);
        if (!s.isValid() || (widget->testAttribute(Qt::WA_Resized) && (realsize > presizer))) {
            sizer = pick(widget->size(), orient);
        } else {
            sizer = presizer;
        }
        QSizePolicy p = widget->sizePolicy();
        int sf = (orient == Qt::Horizontal) ? p.horizontalStretch() : p.verticalStretch();
        if (sf > 1)
            sizer *= sf;
    }
    return sizer;
}

//  from src/widgets/widgets/qsplitter.cpp, line 33, as _ZN16QSplitterPrivateD1Ev
inline QSplitterPrivate::~QSplitterPrivate()
{
}

//  from src/widgets/widgets/qsplitter.cpp, line 351, as _ZN16QSplitterPrivate4initEv
inline void QSplitterPrivate::init()
{
    Q_Q(QSplitter);
    QSizePolicy sp(QSizePolicy::Expanding, QSizePolicy::Preferred);
    if (orient == Qt::Vertical)
        sp.transpose();
    q->setSizePolicy(sp);
    q->setAttribute(Qt::WA_WState_OwnSizePolicy, false);
}

//  from src/widgets/widgets/qsplitter.cpp, line 361, as _ZN16QSplitterPrivate6recalcEb
inline void QSplitterPrivate::recalc(bool update)
{
    Q_Q(QSplitter);
    int n = list.size();
    /*
      Splitter handles before the first visible widget or right
      before a hidden widget must be hidden.
    */
    bool first = true;
    bool allInvisible = n != 0;
    for (int i = 0; i < n ; ++i) {
        QSplitterLayoutStruct *s = list.at(i);
        bool widgetHidden = s->widget->isHidden();
        if (allInvisible && !widgetHidden && !s->collapsed)
            allInvisible = false;
        s->handle->setHidden(first || widgetHidden);
        if (!widgetHidden)
            first = false;
    }

    if (allInvisible)
        for (int i = 0; i < n ; ++i) {
            QSplitterLayoutStruct *s = list.at(i);
            if (!s->widget->isHidden()) {
                s->collapsed = false;
                break;
            }
        }

    int fi = 2 * q->frameWidth();
    int maxl = fi;
    int minl = fi;
    int maxt = QWIDGETSIZE_MAX;
    int mint = fi;
    /*
      calculate min/max sizes for the whole splitter
    */
    bool empty = true;
    for (int j = 0; j < n; j++) {
        QSplitterLayoutStruct *s = list.at(j);

        if (!s->widget->isHidden()) {
            empty = false;
            if (!s->handle->isHidden()) {
                minl += s->getHandleSize(orient);
                maxl += s->getHandleSize(orient);
            }

            QSize minS = qSmartMinSize(s->widget);
            minl += pick(minS);
            maxl += pick(qSmartMaxSize(s->widget));
            mint = qMax(mint, trans(minS));
            int tm = trans(qSmartMaxSize(s->widget));
            if (tm > 0)
                maxt = qMin(maxt, tm);
        }
    }

    if (empty) {
        if (qobject_cast<QSplitter *>(parent)) {
            // nested splitters; be nice
            maxl = maxt = 0;
        } else {
            // QSplitter with no children yet
            maxl = QWIDGETSIZE_MAX;
        }
    } else {
        maxl = qMin<int>(maxl, QWIDGETSIZE_MAX);
    }
    if (maxt < mint)
        maxt = mint;

    if (update) {
        if (orient == Qt::Horizontal) {
            q->setMaximumSize(maxl, maxt);
            if (q->isWindow())
                q->setMinimumSize(minl,mint);
        } else {
            q->setMaximumSize(maxt, maxl);
            if (q->isWindow())
                q->setMinimumSize(mint,minl);
        }
        doResize();
        q->updateGeometry();
    } else {
        firstShow = true;
    }
}

//  from src/widgets/widgets/qsplitter.cpp, line 450, as _ZN16QSplitterPrivate8doResizeEv
inline void QSplitterPrivate::doResize()
{
    Q_Q(QSplitter);
    QRect r = q->contentsRect();
    int n = list.size();
    QList<QLayoutStruct> a(n * 2);
    int i;

    bool noStretchFactorsSet = true;
    for (i = 0; i < n; ++i) {
        QSizePolicy p = list.at(i)->widget->sizePolicy();
        int sf = orient == Qt::Horizontal ? p.horizontalStretch() : p.verticalStretch();
        if (sf != 0) {
            noStretchFactorsSet = false;
            break;
        }
    }

    int j=0;
    for (i = 0; i < n; ++i) {
        QSplitterLayoutStruct *s = list.at(i);
#ifdef QSPLITTER_DEBUG
        qDebug("widget %d hidden: %d collapsed: %d handle hidden: %d", i, s->widget->isHidden(),
               s->collapsed, s->handle->isHidden());
#endif

        a[j].init();
        if (s->handle->isHidden()) {
            a[j].maximumSize = 0;
        } else {
            a[j].sizeHint = a[j].minimumSize = a[j].maximumSize = s->getHandleSize(orient);
            a[j].empty = false;
        }
        ++j;

        a[j].init();
        if (s->widget->isHidden() || s->collapsed) {
            a[j].maximumSize = 0;
        } else {
            a[j].minimumSize = pick(qSmartMinSize(s->widget));
            a[j].maximumSize = pick(qSmartMaxSize(s->widget));
            a[j].empty = false;

            bool stretch = noStretchFactorsSet;
            if (!stretch) {
                QSizePolicy p = s->widget->sizePolicy();
                int sf = orient == Qt::Horizontal ? p.horizontalStretch() : p.verticalStretch();
                stretch = (sf != 0);
            }
            if (stretch) {
                a[j].stretch = s->getWidgetSize(orient);
                a[j].sizeHint = a[j].minimumSize;
                a[j].expansive = true;
            } else {
                a[j].sizeHint = qMax(s->getWidgetSize(orient), a[j].minimumSize);
            }
        }
        ++j;
    }

    qGeomCalc(a, 0, n*2, pick(r.topLeft()), pick(r.size()), 0);

#ifdef QSPLITTER_DEBUG
    for (i = 0; i < n*2; ++i) {
        qDebug("%*s%d: stretch %d, sh %d, minS %d, maxS %d, exp %d, emp %d -> %d, %d",
               i, "", i,
               a[i].stretch,
               a[i].sizeHint,
               a[i].minimumSize,
               a[i].maximumSize,
               a[i].expansive,
               a[i].empty,
               a[i].pos,
               a[i].size);
    }
#endif

    for (i = 0; i < n; ++i) {
        QSplitterLayoutStruct *s = list.at(i);
        setGeo(s, a[i*2+1].pos, a[i*2+1].size, false);
    }
}

//  from src/widgets/widgets/qsplitter.cpp, line 533, as _ZN16QSplitterPrivate10storeSizesEv
inline void QSplitterPrivate::storeSizes()
{
    for (int i = 0; i < list.size(); ++i) {
        QSplitterLayoutStruct *sls = list.at(i);
        sls->sizer = pick(sls->rect.size());
    }
}

//  from src/widgets/widgets/qsplitter.cpp, line 577, as _ZNK16QSplitterPrivate8getRangeEiPiS0_S0_S0_
inline void QSplitterPrivate::getRange(int index, int *farMin, int *min, int *max, int *farMax) const
{
    Q_Q(const QSplitter);
    int n = list.size();
    if (index <= 0 || index >= n)
        return;

    int collapsibleSizeBefore = 0;
    int idJustBefore = findWidgetJustBeforeOrJustAfter(index, -1, collapsibleSizeBefore);

    int collapsibleSizeAfter = 0;
    int idJustAfter = findWidgetJustBeforeOrJustAfter(index, +1, collapsibleSizeAfter);

    int minBefore = 0;
    int minAfter = 0;
    int maxBefore = 0;
    int maxAfter = 0;
    int i;

    for (i = 0; i < index; ++i)
        addContribution(i, &minBefore, &maxBefore, i == idJustBefore);
    for (i = index; i < n; ++i)
        addContribution(i, &minAfter, &maxAfter, i == idJustAfter);

    QRect r = q->contentsRect();
    int farMinVal;
    int minVal;
    int maxVal;
    int farMaxVal;

    int smartMinBefore = qMax(minBefore, pick(r.size()) - maxAfter);
    int smartMaxBefore = qMin(maxBefore, pick(r.size()) - minAfter);

    minVal = pick(r.topLeft()) + smartMinBefore;
    maxVal = pick(r.topLeft()) + smartMaxBefore;

    farMinVal = minVal;
    if (minBefore - collapsibleSizeBefore >= pick(r.size()) - maxAfter)
        farMinVal -= collapsibleSizeBefore;
    farMaxVal = maxVal;
    if (pick(r.size()) - (minAfter - collapsibleSizeAfter) <= maxBefore)
        farMaxVal += collapsibleSizeAfter;

    if (farMin)
        *farMin = farMinVal;
    if (min)
        *min = minVal;
    if (max)
        *max = maxVal;
    if (farMax)
        *farMax = farMaxVal;
}

//  from src/widgets/widgets/qsplitter.cpp, line 541, as _ZNK16QSplitterPrivate15addContributionEiPiS0_b
inline void QSplitterPrivate::addContribution(int index, int *min, int *max, bool mayCollapse) const
{
    QSplitterLayoutStruct *s = list.at(index);
    if (!s->widget->isHidden()) {
        if (!s->handle->isHidden()) {
            *min += s->getHandleSize(orient);
            *max += s->getHandleSize(orient);
        }
        if (mayCollapse || !s->collapsed)
            *min += pick(qSmartMinSize(s->widget));

        *max += pick(qSmartMaxSize(s->widget));
    }
}

//  from src/widgets/widgets/qsplitter.cpp, line 630, as _ZNK16QSplitterPrivate9adjustPosEiiPiS0_S0_S0_
inline int QSplitterPrivate::adjustPos(int pos, int index, int *farMin, int *min, int *max, int *farMax) const
{
    const int Threshold = 40;

    getRange(index, farMin, min, max, farMax);

    if (pos >= *min) {
        if (pos <= *max) {
            return pos;
        } else {
            int delta = pos - *max;
            int width = *farMax - *max;

            if (delta > width / 2 && delta >= qMin(Threshold, width)) {
                return *farMax;
            } else {
                return *max;
            }
        }
    } else {
        int delta = *min - pos;
        int width = *min - *farMin;

        if (delta > width / 2 && delta >= qMin(Threshold, width)) {
            return *farMin;
        } else {
            return *min;
        }
    }
}

//  from src/widgets/widgets/qsplitter.cpp, line 661, as _ZNK16QSplitterPrivate11collapsibleEP21QSplitterLayoutStruct
inline bool QSplitterPrivate::collapsible(QSplitterLayoutStruct *s) const
{
    if (s->collapsible != Default) {
        return (bool)s->collapsible;
    } else {
        return childrenCollapsible;
    }
}

//  from src/widgets/widgets/qsplitter.cpp, line 793, as _ZNK16QSplitterPrivate10findWidgetEP7QWidget
inline QSplitterLayoutStruct *QSplitterPrivate::findWidget(QWidget *w) const
{
    for (int i = 0; i < list.size(); ++i) {
        if (list.at(i)->widget == w)
            return list.at(i);
    }
    return nullptr;
}

//  from src/widgets/widgets/qsplitter.cpp, line 757, as _ZN16QSplitterPrivate6doMoveEbiiibPiS0_
inline void QSplitterPrivate::doMove(bool backwards, int hPos, int index, int delta, bool mayCollapse,
                              int *positions, int *widths)
{
    if (index < 0 || index >= list.size())
        return;

#ifdef QSPLITTER_DEBUG
    qDebug() << "QSplitterPrivate::doMove" << backwards << hPos << index << delta << mayCollapse;
#endif

    QSplitterLayoutStruct *s = list.at(index);
    QWidget *w = s->widget;

    int nextId = backwards ? index - delta : index + delta;

    if (w->isHidden()) {
        doMove(backwards, hPos, nextId, delta, collapsible(nextId), positions, widths);
    } else {
        int hs =s->handle->isHidden() ? 0 : s->getHandleSize(orient);

        int  ws = backwards ? hPos - pick(s->rect.topLeft())
                 : pick(s->rect.bottomRight()) - hPos -hs + 1;
        if (ws > 0 || (!s->collapsed && !mayCollapse)) {
            ws = qMin(ws, pick(qSmartMaxSize(w)));
            ws = qMax(ws, pick(qSmartMinSize(w)));
        } else {
            ws = 0;
        }
        positions[index] = backwards ? hPos - ws : hPos + hs;
        widths[index] = ws;
        doMove(backwards, backwards ? hPos - ws - hs : hPos + hs + ws, nextId, delta,
               collapsible(nextId), positions, widths);
    }

}

//  from src/widgets/widgets/qsplitter.cpp, line 715, as _ZN16QSplitterPrivate6setGeoEP21QSplitterLayoutStructiib
inline void QSplitterPrivate::setGeo(QSplitterLayoutStruct *sls, int p, int s, bool allowCollapse)
{
    Q_Q(QSplitter);
    QWidget *w = sls->widget;
    QRect r;
    QRect contents = q->contentsRect();
    if (orient == Qt::Horizontal) {
        r.setRect(p, contents.y(), s, contents.height());
    } else {
        r.setRect(contents.x(), p, contents.width(), s);
    }
    sls->rect = r;

    int minSize = pick(qSmartMinSize(w));

    if (orient == Qt::Horizontal && q->isRightToLeft())
        r.moveRight(contents.width() - r.left());

    if (allowCollapse)
        sls->collapsed = s <= 0 && minSize > 0 && !w->isHidden();

    //   Hide the child widget, but without calling hide() so that
    //   the splitter handle is still shown.
    if (sls->collapsed)
        r.moveTopLeft(QPoint(-r.width()-1, -r.height()-1));

    w->setGeometry(r);

    if (!sls->handle->isHidden()) {
        QSplitterHandle *h = sls->handle;
        QSize hs = h->sizeHint();
        const QMargins m = h->contentsMargins();
        if (orient==Qt::Horizontal) {
            if (q->isRightToLeft())
                p = contents.width() - p + hs.width();
            h->setGeometry(p-hs.width() - m.left(), contents.y(), hs.width() + m.left() + m.right(), contents.height());
        } else {
            h->setGeometry(contents.x(), p-hs.height() - m.top(), contents.width(), hs.height() + m.top() + m.bottom());
        }
    }
}

//  from src/widgets/widgets/qsplitter.cpp, line 556, as _ZNK16QSplitterPrivate31findWidgetJustBeforeOrJustAfterEiiRi
inline int QSplitterPrivate::findWidgetJustBeforeOrJustAfter(int index, int delta, int &collapsibleSize) const
{
    if (delta < 0)
        index += delta;
    do {
        QWidget *w = list.at(index)->widget;
        if (!w->isHidden()) {
            if (collapsible(list.at(index)))
                collapsibleSize = pick(qSmartMinSize(w));
            return index;
        }
        index += delta;
    } while (index >= 0 && index < list.size());

    return -1;
}

//  from src/widgets/widgets/qsplitter.cpp, line 670, as _ZN16QSplitterPrivate13updateHandlesEv
inline void QSplitterPrivate::updateHandles()
{
    Q_Q(QSplitter);
    recalc(q->isVisible());
}

//  from src/widgets/widgets/qsplitter.cpp, line 709, as _ZNK16QSplitterPrivate16shouldShowWidgetEPK7QWidget
inline bool QSplitterPrivate::shouldShowWidget(const QWidget *w) const
{
    Q_Q(const QSplitter);
    return q->isVisible() && !QWidgetPrivate::get(w)->isExplicitlyHidden();
}
//  -----------------------------------------------------------------------

//  A QSplitterPrivate that Python can take functions over in. Every QSplitterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSplitterPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQSplitterPrivateCall1)(const void *, int, int *);
typedef void (*CuteQSplitterPrivateCall2)(const void *, int *);
typedef void (*CuteQSplitterPrivateCall3)(const void *, int *);
typedef void * (*CuteQSplitterPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQSplitterPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQSplitterPrivateCall6)(const void *, int *);
typedef int (*CuteQSplitterPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQSplitterPrivateCall8)(const void *, int *);
typedef void (*CuteQSplitterPrivateCall9)(const void *, int *);
typedef void (*CuteQSplitterPrivateCall10)(const void *, int *);
typedef void (*CuteQSplitterPrivateCall11)(const void *, int *);
typedef void (*CuteQSplitterPrivateCall12)(const void *, int *);
typedef void (*CuteQSplitterPrivateCall13)(const void *, int *);
typedef void (*CuteQSplitterPrivateCall14)(const void *, int *);
typedef void (*CuteQSplitterPrivateCall15)(const void *, int *);
typedef bool (*CuteQSplitterPrivateCall16)(const void *, int *);
typedef bool (*CuteQSplitterPrivateCall17)(const void *, int *);
class CuteQSplitterPrivate : public QSplitterPrivate {
public:
  using QSplitterPrivate::QSplitterPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSplitterPrivateCall0 call = reinterpret_cast<CuteQSplitterPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSplitterPrivateCall1 call = reinterpret_cast<CuteQSplitterPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSplitterPrivateCall2 call = reinterpret_cast<CuteQSplitterPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSplitterPrivateCall3 call = reinterpret_cast<CuteQSplitterPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSplitterPrivateCall4 call = reinterpret_cast<CuteQSplitterPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSplitterPrivateCall5 call = reinterpret_cast<CuteQSplitterPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSplitterPrivateCall6 call = reinterpret_cast<CuteQSplitterPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSplitterPrivateCall7 call = reinterpret_cast<CuteQSplitterPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSplitterPrivateCall8 call = reinterpret_cast<CuteQSplitterPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSplitterPrivateCall9 call = reinterpret_cast<CuteQSplitterPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSplitterPrivateCall10 call = reinterpret_cast<CuteQSplitterPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSplitterPrivateCall11 call = reinterpret_cast<CuteQSplitterPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSplitterPrivateCall12 call = reinterpret_cast<CuteQSplitterPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSplitterPrivateCall13 call = reinterpret_cast<CuteQSplitterPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQSplitterPrivateCall14 call = reinterpret_cast<CuteQSplitterPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQSplitterPrivateCall15 call = reinterpret_cast<CuteQSplitterPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSplitterPrivateCall16 call = reinterpret_cast<CuteQSplitterPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQSplitterPrivateCall17 call = reinterpret_cast<CuteQSplitterPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QSplitter *QSplitterPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSplitter *ritual_ZN16QSplitterPrivate6q_funcEv(QSplitterPrivate *self) {
  return self->q_func();
}

//  const QSplitter *QSplitterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSplitter *ritual_ZNK16QSplitterPrivate6q_funcEv(
    const QSplitterPrivate *self) {
  return self->q_func();
}

//  QSplitterPrivate::~QSplitterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSplitterPrivateD1Ev(QSplitterPrivate *self) {
  delete self;
}

//  int QSplitterPrivate::pick(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSplitterPrivate4pickERK6QPoint(
    const QSplitterPrivate *self,
    const QPoint *pos) {
  return self->pick(*pos);
}

//  int QSplitterPrivate::pick(const QSize &s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSplitterPrivate4pickERK5QSize(
    const QSplitterPrivate *self,
    const QSize *s) {
  return self->pick(*s);
}

//  int QSplitterPrivate::trans(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSplitterPrivate5transERK6QPoint(
    const QSplitterPrivate *self,
    const QPoint *pos) {
  return self->trans(*pos);
}

//  int QSplitterPrivate::trans(const QSize &s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSplitterPrivate5transERK5QSize(
    const QSplitterPrivate *self,
    const QSize *s) {
  return self->trans(*s);
}

//  void QSplitterPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSplitterPrivate4initEv(QSplitterPrivate *self) {
  self->init();
}

//  void QSplitterPrivate::recalc(bool update)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSplitterPrivate6recalcEb(
    QSplitterPrivate *self,
    bool update) {
  self->recalc(update);
}

//  void QSplitterPrivate::doResize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSplitterPrivate8doResizeEv(QSplitterPrivate *self) {
  self->doResize();
}

//  void QSplitterPrivate::storeSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSplitterPrivate10storeSizesEv(QSplitterPrivate *self) {
  self->storeSizes();
}

//  void QSplitterPrivate::getRange(int index, int *a1, int *a2, int *a3, int
//      *a4) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QSplitterPrivate8getRangeEiPiS0_S0_S0_(
    const QSplitterPrivate *self,
    int index,
    int *a1,
    int *a2,
    int *a3,
    int *a4) {
  self->getRange(index, a1, a2, a3, a4);
}

//  void QSplitterPrivate::addContribution(int a0, int *a1, int *a2, bool a3)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QSplitterPrivate15addContributionEiPiS0_b(
    const QSplitterPrivate *self,
    int a0,
    int *a1,
    int *a2,
    bool a3) {
  self->addContribution(a0, a1, a2, a3);
}

//  int QSplitterPrivate::adjustPos(int a0, int a1, int *a2, int *a3, int
//      *a4, int *a5) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSplitterPrivate9adjustPosEiiPiS0_S0_S0_(
    const QSplitterPrivate *self,
    int a0,
    int a1,
    int *a2,
    int *a3,
    int *a4,
    int *a5) {
  return self->adjustPos(a0, a1, a2, a3, a4, a5);
}

//  bool QSplitterPrivate::collapsible(QSplitterLayoutStruct *a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSplitterPrivate11collapsibleEP21QSplitterLayoutStruct(
    const QSplitterPrivate *self,
    QSplitterLayoutStruct *a0) {
  return self->collapsible(a0);
}

//  bool QSplitterPrivate::collapsible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSplitterPrivate11collapsibleEi(
    const QSplitterPrivate *self,
    int index) {
  return self->collapsible(index);
}

//  QSplitterLayoutStruct *QSplitterPrivate::findWidget(QWidget *a0) const
extern "C" Q_DECL_EXPORT
QSplitterLayoutStruct *ritual_ZNK16QSplitterPrivate10findWidgetEP7QWidget(
    const QSplitterPrivate *self,
    QWidget *a0) {
  return self->findWidget(a0);
}

//  void QSplitterPrivate::doMove(bool backwards, int pos, int index, int
//      delta, bool mayCollapse, int *positions, int *widths)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSplitterPrivate6doMoveEbiiibPiS0_(
    QSplitterPrivate *self,
    bool backwards,
    int pos,
    int index,
    int delta,
    bool mayCollapse,
    int *positions,
    int *widths) {
  self->doMove(backwards, pos, index, delta, mayCollapse, positions, widths);
}

//  void QSplitterPrivate::setGeo(QSplitterLayoutStruct *s, int pos, int
//      size, bool allowCollapse)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSplitterPrivate6setGeoEP21QSplitterLayoutStructiib(
    QSplitterPrivate *self,
    QSplitterLayoutStruct *s,
    int pos,
    int size,
    bool allowCollapse) {
  self->setGeo(s, pos, size, allowCollapse);
}

//  int QSplitterPrivate::findWidgetJustBeforeOrJustAfter(int index, int
//      delta, int &collapsibleSize) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSplitterPrivate31findWidgetJustBeforeOrJustAfterEiiRi(
    const QSplitterPrivate *self,
    int index,
    int delta,
    int *collapsibleSize) {
  return self->findWidgetJustBeforeOrJustAfter(
      index,
      delta,
      *collapsibleSize);
}

//  void QSplitterPrivate::updateHandles()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSplitterPrivate13updateHandlesEv(QSplitterPrivate *self) {
  self->updateHandles();
}

//  bool QSplitterPrivate::shouldShowWidget(const QWidget *w) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSplitterPrivate16shouldShowWidgetEPK7QWidget(
    const QSplitterPrivate *self,
    const QWidget *w) {
  return self->shouldShowWidget(w);
}

//  a Python function taken by a CuteQSplitterPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSplitterPrivate(
    QSplitterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSplitterPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(splitter)
#endif  // QT_CONFIG(splitter)
