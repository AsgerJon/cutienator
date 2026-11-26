//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpathclipper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgraphicseffect_p.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtCore/qdebug.h>
#include <QtGui/private/qdrawhelper_p.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtWidgets/qgraphicsview.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/qgraphicsproxywidget.h>
#include <QtWidgets/private/qgraphicsscenebsptreeindex_p.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qpoint.h>
#include <QtCore/qstack.h>
#include <QtCore/qvariant.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qnumeric.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpixmapcache.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qevent.h>
#include <QtGui/qinputmethod.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/qgraphicseffect.h>
#endif
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/private/qgraphicswidget_p.h>
#include <QtWidgets/private/qwidgettextcontrol_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qgesturemanager_p.h>
#include <QtCore/private/qdebug_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4772, as local:qgraphicsscene.cpp:setClip
static inline void setClip(QPainter *painter, QGraphicsItem *item)
{
    painter->save();
    QRectF clipRect;
    const QPainterPath clipPath(item->shape());
    if (QPathClipper::pathToRect(clipPath, &clipRect))
        painter->setClipRect(clipRect.normalized(), Qt::IntersectClip);
    else
        painter->setClipPath(clipPath, Qt::IntersectClip);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4783, as local:qgraphicsscene.cpp:setWorldTransform
static inline void setWorldTransform(QPainter *painter, const QTransform *const transformPtr,
                                     const QTransform *effectTransform)
{
    Q_ASSERT(transformPtr);
    if (effectTransform)
        painter->setWorldTransform(*transformPtr * *effectTransform);
    else
        painter->setWorldTransform(*transformPtr);
}

//  from src/widgets/effects/qgraphicseffect.cpp, line 345, as _ZN28QGraphicsEffectSourcePrivateD2Ev
inline QGraphicsEffectSourcePrivate::~QGraphicsEffectSourcePrivate()
{
    invalidateCache();
}

//  from src/widgets/graphicsview/qgraphicsitem.cpp, line 11039, as _ZN32QGraphicsItemEffectSourcePrivate4drawEP8QPainter
#if QT_CONFIG(graphicseffect)
inline void QGraphicsItemEffectSourcePrivate::draw(QPainter *painter)
{
    if (!info) {
        qWarning("QGraphicsEffectSource::draw: Can only begin as a result of QGraphicsEffect::draw");
        return;
    }

    Q_ASSERT(item->d_ptr->scene);
    QGraphicsScenePrivate *scened = item->d_ptr->scene->d_func();
    if (painter == info->painter) {
        scened->draw(item, painter, info->viewTransform, info->transformPtr, info->exposedRegion,
                     info->widget, info->opacity, info->effectTransform, info->wasDirtySceneTransform,
                     info->drawItem);
    } else {
        QTransform effectTransform = info->painter->worldTransform().inverted();
        effectTransform *= painter->worldTransform();
        scened->draw(item, painter, info->viewTransform, info->transformPtr, info->exposedRegion,
                     info->widget, info->opacity, &effectTransform, info->wasDirtySceneTransform,
                     info->drawItem);
    }
}
#endif  // QT_CONFIG(graphicseffect)

//  from src/widgets/graphicsview/qgraphicsitem.cpp, line 11018, as _ZNK32QGraphicsItemEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE
#if QT_CONFIG(graphicseffect)
inline QRectF QGraphicsItemEffectSourcePrivate::boundingRect(Qt::CoordinateSystem system) const
{
    const bool deviceCoordinates = (system == Qt::DeviceCoordinates);
    if (!info && deviceCoordinates) {
        // Device coordinates without info not yet supported.
        qWarning("QGraphicsEffectSource::boundingRect: Not yet implemented, lacking device context");
        return QRectF();
    }

    QRectF rect = item->boundingRect();
    if (!item->d_ptr->children.isEmpty())
        rect |= item->childrenBoundingRect();

    if (deviceCoordinates) {
        Q_ASSERT(info->painter);
        rect = info->painter->worldTransform().mapRect(rect);
    }

    return rect;
}
#endif  // QT_CONFIG(graphicseffect)

//  from src/widgets/graphicsview/qgraphicsitem.cpp, line 11093, as _ZNK32QGraphicsItemEffectSourcePrivate6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE
#if QT_CONFIG(graphicseffect)
inline QPixmap QGraphicsItemEffectSourcePrivate::pixmap(Qt::CoordinateSystem system, QPoint *offset,
                                                 QGraphicsEffect::PixmapPadMode mode) const
{
    const bool deviceCoordinates = (system == Qt::DeviceCoordinates);
    if (!info && deviceCoordinates) {
        // Device coordinates without info not yet supported.
        qWarning("QGraphicsEffectSource::pixmap: Not yet implemented, lacking device context");
        return QPixmap();
    }
    if (!item->d_ptr->scene)
        return QPixmap();
    QGraphicsScenePrivate *scened = item->d_ptr->scene->d_func();

    bool unpadded;
    const QRectF sourceRect = boundingRect(system);
    QRectF effectRectF = paddedEffectRect(system, mode, sourceRect, &unpadded);
    QRect effectRect = effectRectF.toAlignedRect();

    if (offset)
        *offset = effectRect.topLeft();

    bool untransformed = !deviceCoordinates
            || info->painter->worldTransform().type() <= QTransform::TxTranslate;
    if (untransformed && unpadded && isPixmap()) {
        if (offset)
            *offset = boundingRect(system).topLeft().toPoint();
        return static_cast<QGraphicsPixmapItem *>(item)->pixmap();
    }

    if (effectRect.isEmpty())
        return QPixmap();

    const auto dpr = info ? info->painter->device()->devicePixelRatio() : 1.0;
    QPixmap pixmap(QRectF(effectRectF.topLeft(), effectRectF.size() * dpr).toAlignedRect().size());
    pixmap.setDevicePixelRatio(dpr);
    pixmap.fill(Qt::transparent);
    QPainter pixmapPainter(&pixmap);
    pixmapPainter.setRenderHints(info ? info->painter->renderHints() : QPainter::TextAntialiasing);

    QTransform effectTransform = QTransform::fromTranslate(-effectRect.x(), -effectRect.y());
    if (deviceCoordinates && info->effectTransform)
        effectTransform *= *info->effectTransform;

    if (!info) {
        // Logical coordinates without info.
        QTransform sceneTransform = item->sceneTransform();
        QTransform newEffectTransform = sceneTransform.inverted();
        newEffectTransform *= effectTransform;
        scened->draw(item, &pixmapPainter, nullptr, &sceneTransform, nullptr, nullptr, qreal(1.0),
                     &newEffectTransform, false, true);
    } else if (deviceCoordinates) {
        // Device coordinates with info.
        scened->draw(item, &pixmapPainter, info->viewTransform, info->transformPtr, nullptr,
                     info->widget, info->opacity, &effectTransform, info->wasDirtySceneTransform,
                     info->drawItem);
    } else {
        // Item coordinates with info.
        QTransform newEffectTransform = info->transformPtr->inverted();
        newEffectTransform *= effectTransform;
        scened->draw(item, &pixmapPainter, info->viewTransform, info->transformPtr, nullptr,
                     info->widget, info->opacity, &newEffectTransform, info->wasDirtySceneTransform,
                     info->drawItem);
    }

    pixmapPainter.end();

    return pixmap;
}
#endif  // QT_CONFIG(graphicseffect)

//  from src/widgets/effects/qgraphicseffect.cpp, line 355, as _ZNK28QGraphicsEffectSourcePrivate15invalidateCacheENS_16InvalidateReasonE
inline void QGraphicsEffectSourcePrivate::invalidateCache(InvalidateReason reason) const
{
    if (m_cachedMode != QGraphicsEffect::PadToEffectiveBoundingRect
        && (reason == EffectRectChanged
            || (reason == TransformChanged && m_cachedSystem == Qt::LogicalCoordinates))) {
        return;
    }

    QPixmapCache::remove(m_cacheKey);
}

//  from src/widgets/graphicsview/qgraphicsitem.cpp, line 11062, as _ZNK32QGraphicsItemEffectSourcePrivate16paddedEffectRectEN2Qt16CoordinateSystemEN15QGraphicsEffect13PixmapPadModeERK6QRectFPb
#if QT_CONFIG(graphicseffect)
inline QRectF QGraphicsItemEffectSourcePrivate::paddedEffectRect(Qt::CoordinateSystem system, QGraphicsEffect::PixmapPadMode mode, const QRectF &sourceRect, bool *unpadded) const
{
    QRectF effectRectF;

    if (unpadded)
        *unpadded = false;

    if (mode == QGraphicsEffect::PadToEffectiveBoundingRect) {
        if (info) {
            QRectF deviceRect = system == Qt::DeviceCoordinates ? sourceRect : info->painter->worldTransform().mapRect(sourceRect);
            effectRectF = item->graphicsEffect()->boundingRectFor(deviceRect);
            if (unpadded)
                *unpadded = (effectRectF.size() == sourceRect.size());
            if (info && system == Qt::LogicalCoordinates)
                effectRectF = info->painter->worldTransform().inverted().mapRect(effectRectF);
        } else {
            // no choice but to send a logical coordinate bounding rect to boundingRectFor
            effectRectF = item->graphicsEffect()->boundingRectFor(sourceRect);
        }
    } else if (mode == QGraphicsEffect::PadToTransparentBorder) {
        // adjust by 1.5 to account for cosmetic pens
        effectRectF = sourceRect.adjusted(-1.5, -1.5, 1.5, 1.5);
    } else {
        effectRectF = sourceRect;
        if (unpadded)
            *unpadded = true;
    }

    return effectRectF;
}
#endif  // QT_CONFIG(graphicseffect)
//  -----------------------------------------------------------------------

//  A QGraphicsItemEffectSourcePrivate that Python can take functions over in. Every QGraphicsItemEffectSourcePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemEffectSourcePrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef void * (*CuteQGraphicsItemEffectSourcePrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef void * (*CuteQGraphicsItemEffectSourcePrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemEffectSourcePrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemEffectSourcePrivateCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsItemEffectSourcePrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef void * (*CuteQGraphicsItemEffectSourcePrivateCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef const QRect * (*CuteQGraphicsItemEffectSourcePrivateCall7)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteQGraphicsItemEffectSourcePrivateCall8)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemEffectSourcePrivateCall9)(const void *, QPainter *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
typedef const QPixmap * (*CuteQGraphicsItemEffectSourcePrivateCall10)(const void *, int, QPoint *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
class CuteQGraphicsItemEffectSourcePrivate : public QGraphicsItemEffectSourcePrivate {
public:
  using QGraphicsItemEffectSourcePrivate::QGraphicsItemEffectSourcePrivate;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate6detachEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate12graphicsItemEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate6widgetEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate6updateEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate25effectBoundingRectChangedEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate8isPixmapEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate11styleOptionEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate10deviceRectEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate4drawEP8QPainter")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
    return false;
  }

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemEffectSourcePrivate::detach()
  void detach() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall0 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemEffectSourcePrivate::detach();
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  const QGraphicsItem *QGraphicsItemEffectSourcePrivate::graphicsItem()
  //      const
  const QGraphicsItem *graphicsItem() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall1 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QGraphicsItem *>(given);
    }
    return QGraphicsItemEffectSourcePrivate::graphicsItem();
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  const QWidget *QGraphicsItemEffectSourcePrivate::widget() const
  const QWidget *widget() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall2 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QWidget *>(given);
    }
    return QGraphicsItemEffectSourcePrivate::widget();
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemEffectSourcePrivate::update()
  void update() override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall3 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemEffectSourcePrivate::update();
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemEffectSourcePrivate::effectBoundingRectChanged()
  void effectBoundingRectChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall4 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemEffectSourcePrivate::effectBoundingRectChanged();
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItemEffectSourcePrivate::isPixmap() const
  bool isPixmap() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall5 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsItemEffectSourcePrivate::isPixmap();
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  const QStyleOption *QGraphicsItemEffectSourcePrivate::styleOption()
  //      const
  const QStyleOption *styleOption() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall6 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QStyleOption *>(given);
    }
    return QGraphicsItemEffectSourcePrivate::styleOption();
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  QRect QGraphicsItemEffectSourcePrivate::deviceRect() const
  QRect deviceRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall7 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall7>(taken[7]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItemEffectSourcePrivate::deviceRect();
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  QRectF
  //      QGraphicsItemEffectSourcePrivate::boundingRect(Qt::CoordinateSyst
  //      em system) const
  QRectF boundingRect(Qt::CoordinateSystem system) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall8 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall8>(taken[8]);
      const QRectF * given = call(this, static_cast<int>(system), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItemEffectSourcePrivate::boundingRect(system);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemEffectSourcePrivate::draw(QPainter *a0)
  void draw(QPainter *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall9 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QGraphicsItemEffectSourcePrivate::draw(a0);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicsview)
  //  QPixmap QGraphicsItemEffectSourcePrivate::pixmap(Qt::CoordinateSystem
  //      system, QPoint *offset, QGraphicsEffect::PixmapPadMode mode)
  //      const
  QPixmap pixmap(
      Qt::CoordinateSystem system,
      QPoint *offset,
      QGraphicsEffect::PixmapPadMode mode) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsItemEffectSourcePrivateCall10 call = reinterpret_cast<CuteQGraphicsItemEffectSourcePrivateCall10>(taken[10]);
      const QPixmap * given = call(this, static_cast<int>(system), offset, static_cast<int>(mode), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItemEffectSourcePrivate::pixmap(system, offset, mode);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicseffect)
};

//  void QGraphicsItemEffectSourcePrivate::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QGraphicsItemEffectSourcePrivate6detachEv(
    QGraphicsItemEffectSourcePrivate *self) {
  self->detach();
}

//  const QGraphicsItem *QGraphicsItemEffectSourcePrivate::graphicsItem()
//      const
extern "C" Q_DECL_EXPORT
const QGraphicsItem *ritual_ZNK32QGraphicsItemEffectSourcePrivate12graphicsItemEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return self->graphicsItem();
}

//  const QWidget *QGraphicsItemEffectSourcePrivate::widget() const
extern "C" Q_DECL_EXPORT
const QWidget *ritual_ZNK32QGraphicsItemEffectSourcePrivate6widgetEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return self->widget();
}

//  void QGraphicsItemEffectSourcePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QGraphicsItemEffectSourcePrivate6updateEv(
    QGraphicsItemEffectSourcePrivate *self) {
  self->update();
}

//  void QGraphicsItemEffectSourcePrivate::effectBoundingRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QGraphicsItemEffectSourcePrivate25effectBoundingRectChangedEv(
    QGraphicsItemEffectSourcePrivate *self) {
  self->effectBoundingRectChanged();
}

//  bool QGraphicsItemEffectSourcePrivate::isPixmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QGraphicsItemEffectSourcePrivate8isPixmapEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return self->isPixmap();
}

//  const QStyleOption *QGraphicsItemEffectSourcePrivate::styleOption() const
extern "C" Q_DECL_EXPORT
const QStyleOption *ritual_ZNK32QGraphicsItemEffectSourcePrivate11styleOptionEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return self->styleOption();
}

//  QRect QGraphicsItemEffectSourcePrivate::deviceRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK32QGraphicsItemEffectSourcePrivate10deviceRectEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return new QRect(self->deviceRect());
}

//  QRectF
//      QGraphicsItemEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
//      system) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK32QGraphicsItemEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE(
    const QGraphicsItemEffectSourcePrivate *self,
    Qt::CoordinateSystem system) {
  return new QRectF(self->boundingRect(system));
}

//  void QGraphicsItemEffectSourcePrivate::draw(QPainter *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QGraphicsItemEffectSourcePrivate4drawEP8QPainter(
    QGraphicsItemEffectSourcePrivate *self,
    QPainter *a0) {
  self->draw(a0);
}

//  QPixmap QGraphicsItemEffectSourcePrivate::pixmap(Qt::CoordinateSystem
//      system, QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK32QGraphicsItemEffectSourcePrivate6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE(
    const QGraphicsItemEffectSourcePrivate *self,
    Qt::CoordinateSystem system,
    QPoint *offset,
    QGraphicsEffect::PixmapPadMode mode) {
  return new QPixmap(self->pixmap(system, offset, mode));
}

#if QT_CONFIG(graphicseffect)
//  QRectF
//      QGraphicsItemEffectSourcePrivate::paddedEffectRect(Qt::CoordinateSyst
//      em system, QGraphicsEffect::PixmapPadMode mode, const QRectF
//      &sourceRect, bool *unpadded) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK32QGraphicsItemEffectSourcePrivate16paddedEffectRectEN2Qt16CoordinateSystemEN15QGraphicsEffect13PixmapPadModeERK6QRectFPb(
    const QGraphicsItemEffectSourcePrivate *self,
    Qt::CoordinateSystem system,
    QGraphicsEffect::PixmapPadMode mode,
    const QRectF *sourceRect,
    bool *unpadded) {
  return new QRectF(
      self->paddedEffectRect(
          system,
          mode,
          *sourceRect,
          unpadded));
}
#endif  // QT_CONFIG(graphicseffect)

//  a Python function taken by a CuteQGraphicsItemEffectSourcePrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsItemEffectSourcePrivate(
    QGraphicsItemEffectSourcePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsItemEffectSourcePrivate *>(self)->take(key, call);
}

//  void QGraphicsItemEffectSourcePrivate::detach()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QGraphicsItemEffectSourcePrivate6detachEv(
    QGraphicsItemEffectSourcePrivate *self) {
  self->QGraphicsItemEffectSourcePrivate::detach();
}

//  const QGraphicsItem *QGraphicsItemEffectSourcePrivate::graphicsItem()
//      const
extern "C" Q_DECL_EXPORT
const QGraphicsItem *ritual_own_ZNK32QGraphicsItemEffectSourcePrivate12graphicsItemEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return self->QGraphicsItemEffectSourcePrivate::graphicsItem();
}

//  const QWidget *QGraphicsItemEffectSourcePrivate::widget() const
extern "C" Q_DECL_EXPORT
const QWidget *ritual_own_ZNK32QGraphicsItemEffectSourcePrivate6widgetEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return self->QGraphicsItemEffectSourcePrivate::widget();
}

//  void QGraphicsItemEffectSourcePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QGraphicsItemEffectSourcePrivate6updateEv(
    QGraphicsItemEffectSourcePrivate *self) {
  self->QGraphicsItemEffectSourcePrivate::update();
}

//  void QGraphicsItemEffectSourcePrivate::effectBoundingRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QGraphicsItemEffectSourcePrivate25effectBoundingRectChangedEv(
    QGraphicsItemEffectSourcePrivate *self) {
  self->QGraphicsItemEffectSourcePrivate::effectBoundingRectChanged();
}

//  bool QGraphicsItemEffectSourcePrivate::isPixmap() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK32QGraphicsItemEffectSourcePrivate8isPixmapEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return self->QGraphicsItemEffectSourcePrivate::isPixmap();
}

//  const QStyleOption *QGraphicsItemEffectSourcePrivate::styleOption() const
extern "C" Q_DECL_EXPORT
const QStyleOption *ritual_own_ZNK32QGraphicsItemEffectSourcePrivate11styleOptionEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return self->QGraphicsItemEffectSourcePrivate::styleOption();
}

//  QRect QGraphicsItemEffectSourcePrivate::deviceRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK32QGraphicsItemEffectSourcePrivate10deviceRectEv(
    const QGraphicsItemEffectSourcePrivate *self) {
  return new QRect(self->QGraphicsItemEffectSourcePrivate::deviceRect());
}

#if QT_CONFIG(graphicseffect)
//  QRectF
//      QGraphicsItemEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
//      system) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK32QGraphicsItemEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE(
    const QGraphicsItemEffectSourcePrivate *self,
    Qt::CoordinateSystem system) {
  return new QRectF(
      self->QGraphicsItemEffectSourcePrivate::boundingRect(
          system));
}
#endif  // QT_CONFIG(graphicseffect)

#endif  // QT_CONFIG(graphicseffect)
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
