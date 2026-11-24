//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgraphicseffect_p.h"
#include "private/qgraphicsitem_p.h"
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtCore/qdebug.h>
#include <private/qdrawhelper_p.h>
#include "qapplication.h"
#include "qapplication_p.h"
#include "qbrush.h"
#include "qcursor.h"
#include "private/qduplicatetracker_p.h"
#include "qevent.h"
#include "qlayout.h"
#if QT_CONFIG(menu)
#include "qmenu.h"
#endif
#include "qmetaobject.h"
#include "qpixmap.h"
#include "qpointer.h"
#include "qstack.h"
#include "qstyle.h"
#include "qstylefactory.h"
#include "qvariant.h"
#include "qwidget.h"
#include "qstyleoption.h"
#include "qstylehints.h"
#if QT_CONFIG(accessibility)
# include "qaccessible.h"
# include <private/qaccessiblecache_p.h>
#endif
#include <qpa/qplatformwindow.h>
#include <qpa/qplatformwindow_p.h>
#include "private/qwidgetwindow_p.h"
#include "qpainter.h"
#if QT_CONFIG(tooltip)
#include "private/qtooltip_p.h"
#endif
#if QT_CONFIG(whatsthis)
#include "qwhatsthis.h"
#endif
#include "qdebug.h"
#if QT_CONFIG(style_stylesheet)
#include "private/qstylesheetstyle_p.h"
#endif
#include "private/qstyle_p.h"
#include "qfileinfo.h"
#include "qscopeguard.h"
#include <QtGui/qinputmethod.h>
#if QT_CONFIG(graphicseffect)
#include <private/qgraphicseffect_p.h>
#endif
#include <qbackingstore.h>
#include <private/qwidgetrepaintmanager_p.h>
#include <private/qpaintengine_raster_p.h>
#include "qwidget_p.h"
#include <QtGui/private/qwindow_p.h>
#if QT_CONFIG(action)
#  include "QtGui/private/qaction_p.h"
#endif
#include "qlayout_p.h"
#if QT_CONFIG(graphicsview)
#include "QtWidgets/qgraphicsproxywidget.h"
#include "QtWidgets/qgraphicsscene.h"
#include "private/qgraphicsproxywidget_p.h"
#include "private/qgraphicsview_p.h"
#endif
#include "QtWidgets/qabstractscrollarea.h"
#include "private/qabstractscrollarea_p.h"
#include "private/qevent_p.h"
#include "private/qgesturemanager_p.h"
#include "qwindowcontainer_p.h"
#include <sstream>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/effects/qgraphicseffect.cpp, line 345, as _ZN28QGraphicsEffectSourcePrivateD2Ev
inline QGraphicsEffectSourcePrivate::~QGraphicsEffectSourcePrivate()
{
    invalidateCache();
}

//  from src/widgets/kernel/qwidget.cpp, line 5797, as _ZNK26QWidgetEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE
#if QT_CONFIG(graphicseffect)
inline QRectF QWidgetEffectSourcePrivate::boundingRect(Qt::CoordinateSystem system) const
{
    if (system != Qt::DeviceCoordinates)
        return m_widget->rect();

    if (Q_UNLIKELY(!context)) {
        // Device coordinates without context not yet supported.
        qWarning("QGraphicsEffectSource::boundingRect: Not yet implemented, lacking device context");
        return QRectF();
    }

    return context->painter->worldTransform().mapRect(m_widget->rect());
}
#endif  // QT_CONFIG(graphicseffect)

//  from src/widgets/kernel/qwidget.cpp, line 5811, as _ZN26QWidgetEffectSourcePrivate4drawEP8QPainter
#if QT_CONFIG(graphicseffect)
inline void QWidgetEffectSourcePrivate::draw(QPainter *painter)
{
    if (!context || context->painter != painter) {
        m_widget->render(painter);
        return;
    }

    // The region saved in the context is neither clipped to the rect
    // nor the mask, so we have to clip it here before calling drawWidget.
    QRegion toBePainted = context->rgn;
    toBePainted &= m_widget->rect();
    QWidgetPrivate *wd = qt_widget_private(m_widget);
    if (wd->extra && wd->extra->hasMask)
        toBePainted &= wd->extra->mask;

    wd->drawWidget(context->pdev, toBePainted, context->offset, context->flags,
                   context->sharedPainter, context->repaintManager);
}
#endif  // QT_CONFIG(graphicseffect)

//  from src/widgets/kernel/qwidget.cpp, line 5830, as _ZNK26QWidgetEffectSourcePrivate6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE
#if QT_CONFIG(graphicseffect)
inline QPixmap QWidgetEffectSourcePrivate::pixmap(Qt::CoordinateSystem system, QPoint *offset,
                                           QGraphicsEffect::PixmapPadMode mode) const
{
    const bool deviceCoordinates = (system == Qt::DeviceCoordinates);
    if (Q_UNLIKELY(!context && deviceCoordinates)) {
        // Device coordinates without context not yet supported.
        qWarning("QGraphicsEffectSource::pixmap: Not yet implemented, lacking device context");
        return QPixmap();
    }

    QPoint pixmapOffset;
    QRectF sourceRect = m_widget->rect();

    if (deviceCoordinates) {
        const QTransform &painterTransform = context->painter->worldTransform();
        sourceRect = painterTransform.mapRect(sourceRect);
        pixmapOffset = painterTransform.map(pixmapOffset);
    }

    QRect effectRect;

    if (mode == QGraphicsEffect::PadToEffectiveBoundingRect)
        effectRect = m_widget->graphicsEffect()->boundingRectFor(sourceRect).toAlignedRect();
    else if (mode == QGraphicsEffect::PadToTransparentBorder)
        effectRect = sourceRect.adjusted(-1, -1, 1, 1).toAlignedRect();
    else
        effectRect = sourceRect.toAlignedRect();

    if (offset)
        *offset = effectRect.topLeft();

    pixmapOffset -= effectRect.topLeft();

    qreal dpr(1.0);
    if (const auto *paintDevice = context->painter->device())
        dpr = paintDevice->devicePixelRatio();
    else
        qWarning("QWidgetEffectSourcePrivate::pixmap: Painter not active");
    QPixmap pixmap(effectRect.size() * dpr);
    pixmap.setDevicePixelRatio(dpr);

    pixmap.fill(Qt::transparent);
    m_widget->render(&pixmap, pixmapOffset, QRegion(), QWidget::DrawChildren);
    return pixmap;
}
#endif  // QT_CONFIG(graphicseffect)
//  -----------------------------------------------------------------------

//  A QWidgetEffectSourcePrivate that Python can take functions over in. Every QWidgetEffectSourcePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQWidgetEffectSourcePrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void * (*CuteQWidgetEffectSourcePrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void * (*CuteQWidgetEffectSourcePrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQWidgetEffectSourcePrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef bool (*CuteQWidgetEffectSourcePrivateCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQWidgetEffectSourcePrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void * (*CuteQWidgetEffectSourcePrivateCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef const QRect * (*CuteQWidgetEffectSourcePrivateCall7)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef const QRectF * (*CuteQWidgetEffectSourcePrivateCall8)(const void *, int, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQWidgetEffectSourcePrivateCall9)(const void *, QPainter *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef const QPixmap * (*CuteQWidgetEffectSourcePrivateCall10)(const void *, int, QPoint *, int, int *);
#endif  // QT_CONFIG(graphicseffect)
class CuteQWidgetEffectSourcePrivate : public QWidgetEffectSourcePrivate {
public:
  using QWidgetEffectSourcePrivate::QWidgetEffectSourcePrivate;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate6detachEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate12graphicsItemEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate6widgetEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate6updateEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate8isPixmapEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate25effectBoundingRectChangedEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate11styleOptionEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate10deviceRectEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate4drawEP8QPainter")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
    return false;
  }

#if QT_CONFIG(graphicseffect)
  //  void QWidgetEffectSourcePrivate::detach()
  void detach() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall0 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetEffectSourcePrivate::detach();
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  const QGraphicsItem *QWidgetEffectSourcePrivate::graphicsItem() const
  const QGraphicsItem *graphicsItem() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall1 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QGraphicsItem *>(given);
    }
    return QWidgetEffectSourcePrivate::graphicsItem();
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  const QWidget *QWidgetEffectSourcePrivate::widget() const
  const QWidget *widget() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall2 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QWidget *>(given);
    }
    return QWidgetEffectSourcePrivate::widget();
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QWidgetEffectSourcePrivate::update()
  void update() override {
    if (taken[3]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall3 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetEffectSourcePrivate::update();
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  bool QWidgetEffectSourcePrivate::isPixmap() const
  bool isPixmap() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall4 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetEffectSourcePrivate::isPixmap();
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QWidgetEffectSourcePrivate::effectBoundingRectChanged()
  void effectBoundingRectChanged() override {
    if (taken[5]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall5 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetEffectSourcePrivate::effectBoundingRectChanged();
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  const QStyleOption *QWidgetEffectSourcePrivate::styleOption() const
  const QStyleOption *styleOption() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall6 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QStyleOption *>(given);
    }
    return QWidgetEffectSourcePrivate::styleOption();
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  QRect QWidgetEffectSourcePrivate::deviceRect() const
  QRect deviceRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall7 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall7>(taken[7]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetEffectSourcePrivate::deviceRect();
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  QRectF QWidgetEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
  //      system) const
  QRectF boundingRect(Qt::CoordinateSystem system) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall8 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall8>(taken[8]);
      const QRectF * given = call(this, static_cast<int>(system), &handled);
      if (handled && given) return *given;
    }
    return QWidgetEffectSourcePrivate::boundingRect(system);
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QWidgetEffectSourcePrivate::draw(QPainter *p)
  void draw(QPainter *p) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall9 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall9>(taken[9]);
      call(this, p, &handled);
      if (handled) return;
    }
    QWidgetEffectSourcePrivate::draw(p);
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  QPixmap QWidgetEffectSourcePrivate::pixmap(Qt::CoordinateSystem
  //      system, QPoint *offset, QGraphicsEffect::PixmapPadMode mode)
  //      const
  QPixmap pixmap(
      Qt::CoordinateSystem system,
      QPoint *offset,
      QGraphicsEffect::PixmapPadMode mode) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWidgetEffectSourcePrivateCall10 call = reinterpret_cast<CuteQWidgetEffectSourcePrivateCall10>(taken[10]);
      const QPixmap * given = call(this, static_cast<int>(system), offset, static_cast<int>(mode), &handled);
      if (handled && given) return *given;
    }
    return QWidgetEffectSourcePrivate::pixmap(system, offset, mode);
  }
#endif  // QT_CONFIG(graphicseffect)
};

//  void QWidgetEffectSourcePrivate::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWidgetEffectSourcePrivate6detachEv(
    QWidgetEffectSourcePrivate *self) {
  self->detach();
}

//  const QGraphicsItem *QWidgetEffectSourcePrivate::graphicsItem() const
extern "C" Q_DECL_EXPORT
const QGraphicsItem *ritual_ZNK26QWidgetEffectSourcePrivate12graphicsItemEv(
    const QWidgetEffectSourcePrivate *self) {
  return self->graphicsItem();
}

//  const QWidget *QWidgetEffectSourcePrivate::widget() const
extern "C" Q_DECL_EXPORT
const QWidget *ritual_ZNK26QWidgetEffectSourcePrivate6widgetEv(
    const QWidgetEffectSourcePrivate *self) {
  return self->widget();
}

//  void QWidgetEffectSourcePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWidgetEffectSourcePrivate6updateEv(
    QWidgetEffectSourcePrivate *self) {
  self->update();
}

//  bool QWidgetEffectSourcePrivate::isPixmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWidgetEffectSourcePrivate8isPixmapEv(
    const QWidgetEffectSourcePrivate *self) {
  return self->isPixmap();
}

//  void QWidgetEffectSourcePrivate::effectBoundingRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWidgetEffectSourcePrivate25effectBoundingRectChangedEv(
    QWidgetEffectSourcePrivate *self) {
  self->effectBoundingRectChanged();
}

//  const QStyleOption *QWidgetEffectSourcePrivate::styleOption() const
extern "C" Q_DECL_EXPORT
const QStyleOption *ritual_ZNK26QWidgetEffectSourcePrivate11styleOptionEv(
    const QWidgetEffectSourcePrivate *self) {
  return self->styleOption();
}

//  QRect QWidgetEffectSourcePrivate::deviceRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK26QWidgetEffectSourcePrivate10deviceRectEv(
    const QWidgetEffectSourcePrivate *self) {
  return new QRect(self->deviceRect());
}

//  QRectF QWidgetEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
//      system) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK26QWidgetEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE(
    const QWidgetEffectSourcePrivate *self,
    Qt::CoordinateSystem system) {
  return new QRectF(self->boundingRect(system));
}

//  void QWidgetEffectSourcePrivate::draw(QPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWidgetEffectSourcePrivate4drawEP8QPainter(
    QWidgetEffectSourcePrivate *self,
    QPainter *p) {
  self->draw(p);
}

//  QPixmap QWidgetEffectSourcePrivate::pixmap(Qt::CoordinateSystem system,
//      QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK26QWidgetEffectSourcePrivate6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE(
    const QWidgetEffectSourcePrivate *self,
    Qt::CoordinateSystem system,
    QPoint *offset,
    QGraphicsEffect::PixmapPadMode mode) {
  return new QPixmap(self->pixmap(system, offset, mode));
}

//  a Python function taken by a CuteQWidgetEffectSourcePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidgetEffectSourcePrivate(
    QWidgetEffectSourcePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWidgetEffectSourcePrivate *>(self)->take(key, call);
}

//  void QWidgetEffectSourcePrivate::detach()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QWidgetEffectSourcePrivate6detachEv(
    QWidgetEffectSourcePrivate *self) {
  self->QWidgetEffectSourcePrivate::detach();
}

//  const QGraphicsItem *QWidgetEffectSourcePrivate::graphicsItem() const
extern "C" Q_DECL_EXPORT
const QGraphicsItem *ritual_own_ZNK26QWidgetEffectSourcePrivate12graphicsItemEv(
    const QWidgetEffectSourcePrivate *self) {
  return self->QWidgetEffectSourcePrivate::graphicsItem();
}

//  const QWidget *QWidgetEffectSourcePrivate::widget() const
extern "C" Q_DECL_EXPORT
const QWidget *ritual_own_ZNK26QWidgetEffectSourcePrivate6widgetEv(
    const QWidgetEffectSourcePrivate *self) {
  return self->QWidgetEffectSourcePrivate::widget();
}

//  void QWidgetEffectSourcePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QWidgetEffectSourcePrivate6updateEv(
    QWidgetEffectSourcePrivate *self) {
  self->QWidgetEffectSourcePrivate::update();
}

//  bool QWidgetEffectSourcePrivate::isPixmap() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QWidgetEffectSourcePrivate8isPixmapEv(
    const QWidgetEffectSourcePrivate *self) {
  return self->QWidgetEffectSourcePrivate::isPixmap();
}

//  void QWidgetEffectSourcePrivate::effectBoundingRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QWidgetEffectSourcePrivate25effectBoundingRectChangedEv(
    QWidgetEffectSourcePrivate *self) {
  self->QWidgetEffectSourcePrivate::effectBoundingRectChanged();
}

//  const QStyleOption *QWidgetEffectSourcePrivate::styleOption() const
extern "C" Q_DECL_EXPORT
const QStyleOption *ritual_own_ZNK26QWidgetEffectSourcePrivate11styleOptionEv(
    const QWidgetEffectSourcePrivate *self) {
  return self->QWidgetEffectSourcePrivate::styleOption();
}

//  QRect QWidgetEffectSourcePrivate::deviceRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK26QWidgetEffectSourcePrivate10deviceRectEv(
    const QWidgetEffectSourcePrivate *self) {
  return new QRect(self->QWidgetEffectSourcePrivate::deviceRect());
}

#if QT_CONFIG(graphicseffect)
//  QRectF QWidgetEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
//      system) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK26QWidgetEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE(
    const QWidgetEffectSourcePrivate *self,
    Qt::CoordinateSystem system) {
  return new QRectF(self->QWidgetEffectSourcePrivate::boundingRect(system));
}
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
//  void QWidgetEffectSourcePrivate::draw(QPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QWidgetEffectSourcePrivate4drawEP8QPainter(
    QWidgetEffectSourcePrivate *self,
    QPainter *p) {
  self->QWidgetEffectSourcePrivate::draw(p);
}
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
//  QPixmap QWidgetEffectSourcePrivate::pixmap(Qt::CoordinateSystem system,
//      QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK26QWidgetEffectSourcePrivate6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE(
    const QWidgetEffectSourcePrivate *self,
    Qt::CoordinateSystem system,
    QPoint *offset,
    QGraphicsEffect::PixmapPadMode mode) {
  return new QPixmap(
      self->QWidgetEffectSourcePrivate::pixmap(
          system,
          offset,
          mode));
}
#endif  // QT_CONFIG(graphicseffect)

#endif  // QT_CONFIG(graphicseffect)
