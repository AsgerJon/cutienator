//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/effects/qgraphicseffect.cpp, line 345, as _ZN28QGraphicsEffectSourcePrivateD2Ev
inline QGraphicsEffectSourcePrivate::~QGraphicsEffectSourcePrivate()
{
    invalidateCache();
}

//  from src/widgets/effects/qgraphicseffect.cpp, line 350, as _ZN28QGraphicsEffectSourcePrivate15setCachedOffsetERK6QPoint
inline void QGraphicsEffectSourcePrivate::setCachedOffset(const QPoint &offset)
{
    m_cachedOffset = offset;
}

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
//  -----------------------------------------------------------------------

//  A QGraphicsEffectSourcePrivate that Python can take functions over in. Every QGraphicsEffectSourcePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQGraphicsEffectSourcePrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef const QRectF * (*CuteQGraphicsEffectSourcePrivateCall1)(const void *, int, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef const QRect * (*CuteQGraphicsEffectSourcePrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void * (*CuteQGraphicsEffectSourcePrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void * (*CuteQGraphicsEffectSourcePrivateCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void * (*CuteQGraphicsEffectSourcePrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQGraphicsEffectSourcePrivateCall6)(const void *, QPainter *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQGraphicsEffectSourcePrivateCall7)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef bool (*CuteQGraphicsEffectSourcePrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef const QPixmap * (*CuteQGraphicsEffectSourcePrivateCall9)(const void *, int, QPoint *, int, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQGraphicsEffectSourcePrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(graphicseffect)
class CuteQGraphicsEffectSourcePrivate : public QGraphicsEffectSourcePrivate {
public:
  using QGraphicsEffectSourcePrivate::QGraphicsEffectSourcePrivate;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate6detachEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate10deviceRectEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate12graphicsItemEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate6widgetEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate11styleOptionEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate4drawEP8QPainter")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate6updateEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate8isPixmapEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK28QGraphicsEffectSourcePrivate6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN28QGraphicsEffectSourcePrivate25effectBoundingRectChangedEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
    return false;
  }

#if QT_CONFIG(graphicseffect)
  //  void QGraphicsEffectSourcePrivate::detach()
  void detach() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall0 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  QRectF
  //      QGraphicsEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
  //      system) const
  QRectF boundingRect(Qt::CoordinateSystem system) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall1 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall1>(taken[1]);
      const QRectF * given = call(this, static_cast<int>(system), &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  QRect QGraphicsEffectSourcePrivate::deviceRect() const
  QRect deviceRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall2 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall2>(taken[2]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  const QGraphicsItem *QGraphicsEffectSourcePrivate::graphicsItem()
  //      const
  const QGraphicsItem *graphicsItem() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall3 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QGraphicsItem *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  const QWidget *QGraphicsEffectSourcePrivate::widget() const
  const QWidget *widget() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall4 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QWidget *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  const QStyleOption *QGraphicsEffectSourcePrivate::styleOption() const
  const QStyleOption *styleOption() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall5 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QStyleOption *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QGraphicsEffectSourcePrivate::draw(QPainter *p)
  void draw(QPainter *p) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall6 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall6>(taken[6]);
      call(this, p, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QGraphicsEffectSourcePrivate::update()
  void update() override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall7 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  bool QGraphicsEffectSourcePrivate::isPixmap() const
  bool isPixmap() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall8 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  QPixmap QGraphicsEffectSourcePrivate::pixmap(Qt::CoordinateSystem
  //      system, QPoint *offset, QGraphicsEffect::PixmapPadMode mode)
  //      const
  QPixmap pixmap(
      Qt::CoordinateSystem system,
      QPoint *offset,
      QGraphicsEffect::PixmapPadMode mode) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall9 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall9>(taken[9]);
      const QPixmap * given = call(this, static_cast<int>(system), offset, static_cast<int>(mode), &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QGraphicsEffectSourcePrivate::effectBoundingRectChanged()
  void effectBoundingRectChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsEffectSourcePrivateCall10 call = reinterpret_cast<CuteQGraphicsEffectSourcePrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(graphicseffect)
};

//  QGraphicsEffectSource *QGraphicsEffectSourcePrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsEffectSource *ritual_ZN28QGraphicsEffectSourcePrivate6q_funcEv(
    QGraphicsEffectSourcePrivate *self) {
  return self->q_func();
}

//  const QGraphicsEffectSource *QGraphicsEffectSourcePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsEffectSource *ritual_ZNK28QGraphicsEffectSourcePrivate6q_funcEv(
    const QGraphicsEffectSourcePrivate *self) {
  return self->q_func();
}

//  QGraphicsEffectSourcePrivate::QGraphicsEffectSourcePrivate()
extern "C" Q_DECL_EXPORT
QGraphicsEffectSourcePrivate *ritual_ZN28QGraphicsEffectSourcePrivateC1Ev() {
  return new CuteQGraphicsEffectSourcePrivate();
}

//  QGraphicsEffectSourcePrivate::~QGraphicsEffectSourcePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsEffectSourcePrivateD1Ev(
    QGraphicsEffectSourcePrivate *self) {
  delete self;
}

//  void QGraphicsEffectSourcePrivate::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsEffectSourcePrivate6detachEv(
    QGraphicsEffectSourcePrivate *self) {
  self->detach();
}

//  QRectF QGraphicsEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
//      system) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK28QGraphicsEffectSourcePrivate12boundingRectEN2Qt16CoordinateSystemE(
    const QGraphicsEffectSourcePrivate *self,
    Qt::CoordinateSystem system) {
  return new QRectF(self->boundingRect(system));
}

//  QRect QGraphicsEffectSourcePrivate::deviceRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK28QGraphicsEffectSourcePrivate10deviceRectEv(
    const QGraphicsEffectSourcePrivate *self) {
  return new QRect(self->deviceRect());
}

//  const QGraphicsItem *QGraphicsEffectSourcePrivate::graphicsItem() const
extern "C" Q_DECL_EXPORT
const QGraphicsItem *ritual_ZNK28QGraphicsEffectSourcePrivate12graphicsItemEv(
    const QGraphicsEffectSourcePrivate *self) {
  return self->graphicsItem();
}

//  const QWidget *QGraphicsEffectSourcePrivate::widget() const
extern "C" Q_DECL_EXPORT
const QWidget *ritual_ZNK28QGraphicsEffectSourcePrivate6widgetEv(
    const QGraphicsEffectSourcePrivate *self) {
  return self->widget();
}

//  const QStyleOption *QGraphicsEffectSourcePrivate::styleOption() const
extern "C" Q_DECL_EXPORT
const QStyleOption *ritual_ZNK28QGraphicsEffectSourcePrivate11styleOptionEv(
    const QGraphicsEffectSourcePrivate *self) {
  return self->styleOption();
}

//  void QGraphicsEffectSourcePrivate::draw(QPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsEffectSourcePrivate4drawEP8QPainter(
    QGraphicsEffectSourcePrivate *self,
    QPainter *p) {
  self->draw(p);
}

//  void QGraphicsEffectSourcePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsEffectSourcePrivate6updateEv(
    QGraphicsEffectSourcePrivate *self) {
  self->update();
}

//  bool QGraphicsEffectSourcePrivate::isPixmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QGraphicsEffectSourcePrivate8isPixmapEv(
    const QGraphicsEffectSourcePrivate *self) {
  return self->isPixmap();
}

//  QPixmap QGraphicsEffectSourcePrivate::pixmap(Qt::CoordinateSystem system,
//      QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK28QGraphicsEffectSourcePrivate6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE(
    const QGraphicsEffectSourcePrivate *self,
    Qt::CoordinateSystem system,
    QPoint *offset,
    QGraphicsEffect::PixmapPadMode mode) {
  return new QPixmap(self->pixmap(system, offset, mode));
}

//  void QGraphicsEffectSourcePrivate::effectBoundingRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsEffectSourcePrivate25effectBoundingRectChangedEv(
    QGraphicsEffectSourcePrivate *self) {
  self->effectBoundingRectChanged();
}

//  void QGraphicsEffectSourcePrivate::setCachedOffset(const QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsEffectSourcePrivate15setCachedOffsetERK6QPoint(
    QGraphicsEffectSourcePrivate *self,
    const QPoint *offset) {
  self->setCachedOffset(*offset);
}

//  void QGraphicsEffectSourcePrivate::invalidateCache(InvalidateReason
//      reason) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QGraphicsEffectSourcePrivate15invalidateCacheENS_16InvalidateReasonE(
    const QGraphicsEffectSourcePrivate *self,
    QGraphicsEffectSourcePrivate::InvalidateReason reason) {
  self->invalidateCache(reason);
}

//  Qt::CoordinateSystem QGraphicsEffectSourcePrivate::currentCachedSystem()
//      const
extern "C" Q_DECL_EXPORT
Qt::CoordinateSystem ritual_ZNK28QGraphicsEffectSourcePrivate19currentCachedSystemEv(
    const QGraphicsEffectSourcePrivate *self) {
  return self->currentCachedSystem();
}

//  QGraphicsEffect::PixmapPadMode
//      QGraphicsEffectSourcePrivate::currentCachedMode() const
extern "C" Q_DECL_EXPORT
QGraphicsEffect::PixmapPadMode ritual_ZNK28QGraphicsEffectSourcePrivate17currentCachedModeEv(
    const QGraphicsEffectSourcePrivate *self) {
  return self->currentCachedMode();
}

//  a Python function taken by a CuteQGraphicsEffectSourcePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsEffectSourcePrivate(
    QGraphicsEffectSourcePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsEffectSourcePrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicseffect)
#endif  // QT_CONFIG(graphicseffect)
