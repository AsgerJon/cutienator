//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgraphicsview.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qregion.h>
#include <QtGui/qcursor.h>
#include <QtGui/qtransform.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractscrollarea.h"
#if QT_CONFIG(scrollarea)
#include "qscrollbar.h"
#include "qapplication.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qevent.h"
#include "qdebug.h"
#include "qboxlayout.h"
#include "qpainter.h"
#include "qmargins.h"
#if QT_CONFIG(itemviews)
#include "qheaderview.h"
#endif
#include <QDebug>
#include "qabstractscrollarea_p.h"
#include "qscrollbar_p.h"
#include <qwidget.h>
#include <private/qguiapplication_p.h>
#include <qpa/qplatformtheme.h>
#include <private/qapplication_p.h>
#ifdef Q_OS_WIN
#  include <qt_windows.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1368, as _ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv
#if QT_CONFIG(scrollarea)
inline QPoint QAbstractScrollAreaPrivate::contentsOffset() const
{
    Q_Q(const QAbstractScrollArea);
    QPoint offset;
    if (vbar->isVisible())
        offset.setY(vbar->value());
    if (hbar->isVisible()) {
        if (q->isRightToLeft())
            offset.setX(hbar->maximum() - hbar->value());
        else
            offset.setX(hbar->value());
    }
    return offset;
}
#endif  // QT_CONFIG(scrollarea)
//  -----------------------------------------------------------------------

//  A QGraphicsViewPrivate that Python can take functions over in. Every QGraphicsViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsViewPrivateCall0)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQGraphicsViewPrivateCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QPoint * (*CuteQGraphicsViewPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQGraphicsViewPrivateCall3)(const void *, bool, int *);
typedef void (*CuteQGraphicsViewPrivateCall4)(const void *, int, int *);
typedef void (*CuteQGraphicsViewPrivateCall5)(const void *, int *);
typedef void (*CuteQGraphicsViewPrivateCall6)(const void *, int *);
typedef void * (*CuteQGraphicsViewPrivateCall7)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQGraphicsViewPrivateCall8)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQGraphicsViewPrivateCall9)(const void *, int *);
typedef int (*CuteQGraphicsViewPrivateCall10)(const void *, int *);
typedef const QImage * (*CuteQGraphicsViewPrivateCall11)(const void *, int *);
typedef void (*CuteQGraphicsViewPrivateCall12)(const void *, int *);
typedef void (*CuteQGraphicsViewPrivateCall13)(const void *, int *);
typedef void (*CuteQGraphicsViewPrivateCall14)(const void *, int *);
typedef void (*CuteQGraphicsViewPrivateCall15)(const void *, int *);
typedef void (*CuteQGraphicsViewPrivateCall16)(const void *, int *);
typedef void (*CuteQGraphicsViewPrivateCall17)(const void *, int *);
typedef void (*CuteQGraphicsViewPrivateCall18)(const void *, int *);
typedef bool (*CuteQGraphicsViewPrivateCall19)(const void *, int *);
typedef bool (*CuteQGraphicsViewPrivateCall20)(const void *, int *);
class CuteQGraphicsViewPrivate : public QGraphicsViewPrivate {
public:
  using QGraphicsViewPrivate::QGraphicsViewPrivate;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsViewPrivate::canStartScrollingAt(const QPoint
  //      &startPos) const
  bool canStartScrollingAt(const QPoint &startPos) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall0 call = reinterpret_cast<CuteQGraphicsViewPrivateCall0>(taken[0]);
      bool given = call(this, &startPos, &handled);
      if (handled) return given;
    }
    return QGraphicsViewPrivate::canStartScrollingAt(startPos);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void
  //      QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientatio
  //      n a0, Qt::ScrollBarPolicy a1)
  void scrollBarPolicyChanged(
      Qt::Orientation a0,
      Qt::ScrollBarPolicy a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall1 call = reinterpret_cast<CuteQGraphicsViewPrivateCall1>(taken[1]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QAbstractScrollAreaPrivate::scrollBarPolicyChanged(a0, a1);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QPoint QAbstractScrollAreaPrivate::contentsOffset() const
  QPoint contentsOffset() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall2 call = reinterpret_cast<CuteQGraphicsViewPrivateCall2>(taken[2]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollAreaPrivate::contentsOffset();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall3 call = reinterpret_cast<CuteQGraphicsViewPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall4 call = reinterpret_cast<CuteQGraphicsViewPrivateCall4>(taken[4]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall5 call = reinterpret_cast<CuteQGraphicsViewPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall6 call = reinterpret_cast<CuteQGraphicsViewPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall7 call = reinterpret_cast<CuteQGraphicsViewPrivateCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall8 call = reinterpret_cast<CuteQGraphicsViewPrivateCall8>(taken[8]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall9 call = reinterpret_cast<CuteQGraphicsViewPrivateCall9>(taken[9]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall10 call = reinterpret_cast<CuteQGraphicsViewPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall11 call = reinterpret_cast<CuteQGraphicsViewPrivateCall11>(taken[11]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall12 call = reinterpret_cast<CuteQGraphicsViewPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall13 call = reinterpret_cast<CuteQGraphicsViewPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall14 call = reinterpret_cast<CuteQGraphicsViewPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall15 call = reinterpret_cast<CuteQGraphicsViewPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall16 call = reinterpret_cast<CuteQGraphicsViewPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall17 call = reinterpret_cast<CuteQGraphicsViewPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall18 call = reinterpret_cast<CuteQGraphicsViewPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall19 call = reinterpret_cast<CuteQGraphicsViewPrivateCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsViewPrivateCall20 call = reinterpret_cast<CuteQGraphicsViewPrivateCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QGraphicsView *QGraphicsViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsView *ritual_ZN20QGraphicsViewPrivate6q_funcEv(
    QGraphicsViewPrivate *self) {
  return self->q_func();
}

//  const QGraphicsView *QGraphicsViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsView *ritual_ZNK20QGraphicsViewPrivate6q_funcEv(
    const QGraphicsViewPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(scrollarea)
//  QGraphicsViewPrivate::QGraphicsViewPrivate()
extern "C" Q_DECL_EXPORT
QGraphicsViewPrivate *ritual_ZN20QGraphicsViewPrivateC1Ev() {
  return new CuteQGraphicsViewPrivate();
}
#endif  // QT_CONFIG(scrollarea)

//  QGraphicsViewPrivate::~QGraphicsViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivateD1Ev(QGraphicsViewPrivate *self) {
  delete self;
}

//  void QGraphicsViewPrivate::recalculateContentSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate22recalculateContentSizeEv(
    QGraphicsViewPrivate *self) {
  self->recalculateContentSize();
}

//  void QGraphicsViewPrivate::centerView(QGraphicsView::ViewportAnchor
//      anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate10centerViewEN13QGraphicsView14ViewportAnchorE(
    QGraphicsViewPrivate *self,
    QGraphicsView::ViewportAnchor anchor) {
  self->centerView(anchor);
}

//  void QGraphicsViewPrivate::updateLastCenterPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate21updateLastCenterPointEv(
    QGraphicsViewPrivate *self) {
  self->updateLastCenterPoint();
}

//  qint64 QGraphicsViewPrivate::horizontalScroll() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QGraphicsViewPrivate16horizontalScrollEv(
    const QGraphicsViewPrivate *self) {
  return self->horizontalScroll();
}

//  qint64 QGraphicsViewPrivate::verticalScroll() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QGraphicsViewPrivate14verticalScrollEv(
    const QGraphicsViewPrivate *self) {
  return self->verticalScroll();
}

//  QRectF QGraphicsViewPrivate::mapRectToScene(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsViewPrivate14mapRectToSceneERK5QRect(
    const QGraphicsViewPrivate *self,
    const QRect *rect) {
  return new QRectF(self->mapRectToScene(*rect));
}

//  QRectF QGraphicsViewPrivate::mapRectFromScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsViewPrivate16mapRectFromSceneERK6QRectF(
    const QGraphicsViewPrivate *self,
    const QRectF *rect) {
  return new QRectF(self->mapRectFromScene(*rect));
}

//  void QGraphicsViewPrivate::updateScroll()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate12updateScrollEv(
    QGraphicsViewPrivate *self) {
  self->updateScroll();
}

//  bool QGraphicsViewPrivate::canStartScrollingAt(const QPoint &startPos)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsViewPrivate19canStartScrollingAtERK6QPoint(
    const QGraphicsViewPrivate *self,
    const QPoint *startPos) {
  return self->canStartScrollingAt(*startPos);
}

//  void QGraphicsViewPrivate::replayLastMouseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate20replayLastMouseEventEv(
    QGraphicsViewPrivate *self) {
  self->replayLastMouseEvent();
}

//  void QGraphicsViewPrivate::storeMouseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate15storeMouseEventEP11QMouseEvent(
    QGraphicsViewPrivate *self,
    QMouseEvent *event) {
  self->storeMouseEvent(event);
}

//  void QGraphicsViewPrivate::mouseMoveEventHandler(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate21mouseMoveEventHandlerEP11QMouseEvent(
    QGraphicsViewPrivate *self,
    QMouseEvent *event) {
  self->mouseMoveEventHandler(event);
}

#if QT_CONFIG(rubberband)
//  QRegion QGraphicsViewPrivate::rubberBandRegion(const QWidget *widget,
//      const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK20QGraphicsViewPrivate16rubberBandRegionEPK7QWidgetRK5QRect(
    const QGraphicsViewPrivate *self,
    const QWidget *widget,
    const QRect *rect) {
  return new QRegion(self->rubberBandRegion(widget, *rect));
}
#endif  // QT_CONFIG(rubberband)

#if QT_CONFIG(rubberband)
//  void QGraphicsViewPrivate::updateRubberBand(const QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate16updateRubberBandEPK11QMouseEvent(
    QGraphicsViewPrivate *self,
    const QMouseEvent *event) {
  self->updateRubberBand(event);
}
#endif  // QT_CONFIG(rubberband)

#if QT_CONFIG(rubberband)
//  void QGraphicsViewPrivate::clearRubberBand()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate15clearRubberBandEv(
    QGraphicsViewPrivate *self) {
  self->clearRubberBand();
}
#endif  // QT_CONFIG(rubberband)

//  QStyleOptionGraphicsItem
//      *QGraphicsViewPrivate::allocStyleOptionsArray(int numItems)
extern "C" Q_DECL_EXPORT
QStyleOptionGraphicsItem *ritual_ZN20QGraphicsViewPrivate22allocStyleOptionsArrayEi(
    QGraphicsViewPrivate *self,
    int numItems) {
  return self->allocStyleOptionsArray(numItems);
}

//  void QGraphicsViewPrivate::freeStyleOptionsArray(QStyleOptionGraphicsItem
//      *array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate21freeStyleOptionsArrayEP24QStyleOptionGraphicsItem(
    QGraphicsViewPrivate *self,
    QStyleOptionGraphicsItem *array) {
  self->freeStyleOptionsArray(array);
}

#if !defined(QT_NO_CURSOR)
//  void QGraphicsViewPrivate::_q_setViewportCursor(const QCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate20_q_setViewportCursorERK7QCursor(
    QGraphicsViewPrivate *self,
    const QCursor *cursor) {
  self->_q_setViewportCursor(*cursor);
}
#endif  // !defined(QT_NO_CURSOR)

#if !defined(QT_NO_CURSOR)
//  void QGraphicsViewPrivate::_q_unsetViewportCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate22_q_unsetViewportCursorEv(
    QGraphicsViewPrivate *self) {
  self->_q_unsetViewportCursor();
}
#endif  // !defined(QT_NO_CURSOR)

//  void QGraphicsViewPrivate::storeDragDropEvent(const
//      QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate18storeDragDropEventEPK27QGraphicsSceneDragDropEvent(
    QGraphicsViewPrivate *self,
    const QGraphicsSceneDragDropEvent *event) {
  self->storeDragDropEvent(event);
}

//  void QGraphicsViewPrivate::populateSceneDragDropEvent(QGraphicsSceneDragD
//      ropEvent *dest, QDropEvent *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate26populateSceneDragDropEventEP27QGraphicsSceneDragDropEventP10QDropEvent(
    QGraphicsViewPrivate *self,
    QGraphicsSceneDragDropEvent *dest,
    QDropEvent *source) {
  self->populateSceneDragDropEvent(dest, source);
}

//  QTransform QGraphicsViewPrivate::mapToViewTransform(const QGraphicsItem
//      *item) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK20QGraphicsViewPrivate18mapToViewTransformEPK13QGraphicsItem(
    const QGraphicsViewPrivate *self,
    const QGraphicsItem *item) {
  return new QTransform(self->mapToViewTransform(item));
}

//  QRect QGraphicsViewPrivate::mapToViewRect(const QGraphicsItem *item,
//      const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK20QGraphicsViewPrivate13mapToViewRectEPK13QGraphicsItemRK6QRectF(
    const QGraphicsViewPrivate *self,
    const QGraphicsItem *item,
    const QRectF *rect) {
  return new QRect(self->mapToViewRect(item, *rect));
}

//  QRegion QGraphicsViewPrivate::mapToViewRegion(const QGraphicsItem *item,
//      const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK20QGraphicsViewPrivate15mapToViewRegionEPK13QGraphicsItemRK6QRectF(
    const QGraphicsViewPrivate *self,
    const QGraphicsItem *item,
    const QRectF *rect) {
  return new QRegion(self->mapToViewRegion(item, *rect));
}

//  void QGraphicsViewPrivate::processPendingUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate21processPendingUpdatesEv(
    QGraphicsViewPrivate *self) {
  self->processPendingUpdates();
}

//  void QGraphicsViewPrivate::updateAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate9updateAllEv(
    QGraphicsViewPrivate *self) {
  self->updateAll();
}

//  void QGraphicsViewPrivate::dispatchPendingUpdateRequests()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate29dispatchPendingUpdateRequestsEv(
    QGraphicsViewPrivate *self) {
  self->dispatchPendingUpdateRequests();
}

//  void QGraphicsViewPrivate::setUpdateClip(QGraphicsItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate13setUpdateClipEP13QGraphicsItem(
    QGraphicsViewPrivate *self,
    QGraphicsItem *a0) {
  self->setUpdateClip(a0);
}

//  bool QGraphicsViewPrivate::updateRectF(const QRectF &rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsViewPrivate11updateRectFERK6QRectF(
    QGraphicsViewPrivate *self,
    const QRectF *rect) {
  return self->updateRectF(*rect);
}

//  bool QGraphicsViewPrivate::updateRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsViewPrivate10updateRectERK5QRect(
    QGraphicsViewPrivate *self,
    const QRect *rect) {
  return self->updateRect(*rect);
}

//  bool QGraphicsViewPrivate::updateRegion(const QRectF &rect, const
//      QTransform &xform)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsViewPrivate12updateRegionERK6QRectFRK10QTransform(
    QGraphicsViewPrivate *self,
    const QRectF *rect,
    const QTransform *xform) {
  return self->updateRegion(*rect, *xform);
}

//  QList<QGraphicsItem *> QGraphicsViewPrivate::findItems(const QRegion
//      &exposedRegion, bool *allItems, const QTransform &viewTransform)
//      const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK20QGraphicsViewPrivate9findItemsERK7QRegionPbRK10QTransform(
    const QGraphicsViewPrivate *self,
    const QRegion *exposedRegion,
    bool *allItems,
    const QTransform *viewTransform) {
  return new QList<QGraphicsItem *>(
      self->findItems(
          *exposedRegion,
          allItems,
          *viewTransform));
}

//  QPointF QGraphicsViewPrivate::mapToScene(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK20QGraphicsViewPrivate10mapToSceneERK7QPointF(
    const QGraphicsViewPrivate *self,
    const QPointF *point) {
  return new QPointF(self->mapToScene(*point));
}

//  QRectF QGraphicsViewPrivate::mapToScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsViewPrivate10mapToSceneERK6QRectF(
    const QGraphicsViewPrivate *self,
    const QRectF *rect) {
  return new QRectF(self->mapToScene(*rect));
}

//  void QGraphicsViewPrivate::translateTouchEvent(QGraphicsViewPrivate *d,
//      QTouchEvent *touchEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate19translateTouchEventEPS_P11QTouchEvent(
    QGraphicsViewPrivate *d,
    QTouchEvent *touchEvent) {
  QGraphicsViewPrivate::translateTouchEvent(d, touchEvent);
}

//  void QGraphicsViewPrivate::updateInputMethodSensitivity()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsViewPrivate28updateInputMethodSensitivityEv(
    QGraphicsViewPrivate *self) {
  self->updateInputMethodSensitivity();
}

//  a Python function taken by a CuteQGraphicsViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsViewPrivate(
    QGraphicsViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsViewPrivate *>(self)->take(key, call);
}

//  bool QGraphicsViewPrivate::canStartScrollingAt(const QPoint &startPos)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QGraphicsViewPrivate19canStartScrollingAtERK6QPoint(
    const QGraphicsViewPrivate *self,
    const QPoint *startPos) {
  return self->QGraphicsViewPrivate::canStartScrollingAt(*startPos);
}

#endif  // QT_CONFIG(graphicsview)
