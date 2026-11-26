//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasboxshadow.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/qcanvasboxshadow.h>
#include <QtCore/qrect.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtCore/qdebug.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasboxshadow.h>
#include <QtCanvasPainter/private/qcanvasboxshadow_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#include <QtCore/QVariant>
#include <QtGui/QVector4D>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 14, as local:qcanvasboxshadow.cpp:QCPAINTER_BOX_SHADOW_MULTIPLIER
static constexpr qreal QCPAINTER_BOX_SHADOW_MULTIPLIER = 1.0;

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 570, as _ZN23QCanvasBoxShadowPrivate5cloneEv
inline QCanvasBrushPrivate *QCanvasBoxShadowPrivate::clone()
{
    return new QCanvasBoxShadowPrivate(*this);
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasboxshadow.cpp, line 137, as _ZNK23QCanvasBoxShadowPrivate6equalsERK19QCanvasBrushPrivate
inline bool QCanvasBoxShadowPrivate::equals(const QCanvasBrushPrivate &other) const noexcept
{
    Q_ASSERT(other.type == type);
    const auto &pd = static_cast<const QCanvasBoxShadowPrivate &>(other);

    if (x != pd.x
        || y != pd.y
        || width != pd.width
        || height != pd.height
        || radius != pd.radius
        || blur != pd.blur
        || spread != pd.spread
        || color != pd.color
        || topLeftRadius != pd.topLeftRadius
        || topRightRadius != pd.topRightRadius
        || bottomLeftRadius != pd.bottomLeftRadius
        || bottomRightRadius != pd.bottomRightRadius)
        return false;

    return true;
}
//  -----------------------------------------------------------------------

//  QCanvasBoxShadow::QCanvasBoxShadow()
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN16QCanvasBoxShadowC1Ev() {
  return new QCanvasBoxShadow();
}

//  QCanvasBoxShadow::QCanvasBoxShadow(qreal x, qreal y, qreal width, qreal
//      height)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN16QCanvasBoxShadowC1Edddd(
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  return new QCanvasBoxShadow(x, y, width, height);
}

//  QCanvasBoxShadow::QCanvasBoxShadow(const QRectF &rect)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN16QCanvasBoxShadowC1ERK6QRectF(
    const QRectF *rect) {
  return new QCanvasBoxShadow(*rect);
}

//  QCanvasBoxShadow::QCanvasBoxShadow(const QCanvasBoxShadow &a0)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN16QCanvasBoxShadowC1ERKS_(
    const QCanvasBoxShadow *a0) {
  return new QCanvasBoxShadow(*a0);
}

//  QCanvasBoxShadow &QCanvasBoxShadow::operator=(const QCanvasBoxShadow &a0)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN16QCanvasBoxShadowaSERKS_(
    QCanvasBoxShadow *self,
    const QCanvasBoxShadow *a0) {
  return &(self->operator=(*a0));
}

//  QCanvasBoxShadow::QCanvasBoxShadow(QCanvasBoxShadow &&a0)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN16QCanvasBoxShadowC1EOS_(QCanvasBoxShadow *a0) {
  return new QCanvasBoxShadow(std::move(*a0));
}

//  QCanvasBoxShadow &QCanvasBoxShadow::operator=(QCanvasBoxShadow &&other)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN16QCanvasBoxShadowaSEOS_(
    QCanvasBoxShadow *self,
    QCanvasBoxShadow *other) {
  return &(self->operator=(std::move(*other)));
}

//  QCanvasBoxShadow::~QCanvasBoxShadow()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadowD1Ev(QCanvasBoxShadow *self) {
  delete self;
}

//  QCanvasBrush QCanvasBoxShadow::operator QCanvasBrush() const
extern "C" Q_DECL_EXPORT
QCanvasBrush *ritual_ZNK16QCanvasBoxShadowcv12QCanvasBrushEv(
    const QCanvasBoxShadow *self) {
  return new QCanvasBrush(self->operator QCanvasBrush());
}

//  QVariant QCanvasBoxShadow::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QCanvasBoxShadowcv8QVariantEv(
    const QCanvasBoxShadow *self) {
  return new QVariant(self->operator QVariant());
}

//  QRectF QCanvasBoxShadow::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16QCanvasBoxShadow4rectEv(const QCanvasBoxShadow *self) {
  return new QRectF(self->rect());
}

//  void QCanvasBoxShadow::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow7setRectERK6QRectF(
    QCanvasBoxShadow *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QCanvasBoxShadow::setRect(qreal x, qreal y, qreal width, qreal
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow7setRectEdddd(
    QCanvasBoxShadow *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->setRect(x, y, width, height);
}

//  QRectF QCanvasBoxShadow::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16QCanvasBoxShadow12boundingRectEv(
    const QCanvasBoxShadow *self) {
  return new QRectF(self->boundingRect());
}

//  qreal QCanvasBoxShadow::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QCanvasBoxShadow6radiusEv(const QCanvasBoxShadow *self) {
  return self->radius();
}

//  void QCanvasBoxShadow::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow9setRadiusEd(
    QCanvasBoxShadow *self,
    qreal radius) {
  self->setRadius(radius);
}

//  qreal QCanvasBoxShadow::blur() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QCanvasBoxShadow4blurEv(const QCanvasBoxShadow *self) {
  return self->blur();
}

//  void QCanvasBoxShadow::setBlur(qreal blur)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow7setBlurEd(
    QCanvasBoxShadow *self,
    qreal blur) {
  self->setBlur(blur);
}

//  qreal QCanvasBoxShadow::spread() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QCanvasBoxShadow6spreadEv(const QCanvasBoxShadow *self) {
  return self->spread();
}

//  void QCanvasBoxShadow::setSpread(qreal spread)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow9setSpreadEd(
    QCanvasBoxShadow *self,
    qreal spread) {
  self->setSpread(spread);
}

//  QColor QCanvasBoxShadow::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QCanvasBoxShadow5colorEv(const QCanvasBoxShadow *self) {
  return new QColor(self->color());
}

//  void QCanvasBoxShadow::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow8setColorE6QColor(
    QCanvasBoxShadow *self,
    const QColor *color) {
  self->setColor(*color);
}

//  qreal QCanvasBoxShadow::topLeftRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QCanvasBoxShadow13topLeftRadiusEv(
    const QCanvasBoxShadow *self) {
  return self->topLeftRadius();
}

//  void QCanvasBoxShadow::setTopLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow16setTopLeftRadiusEd(
    QCanvasBoxShadow *self,
    qreal radius) {
  self->setTopLeftRadius(radius);
}

//  qreal QCanvasBoxShadow::topRightRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QCanvasBoxShadow14topRightRadiusEv(
    const QCanvasBoxShadow *self) {
  return self->topRightRadius();
}

//  void QCanvasBoxShadow::setTopRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow17setTopRightRadiusEd(
    QCanvasBoxShadow *self,
    qreal radius) {
  self->setTopRightRadius(radius);
}

//  qreal QCanvasBoxShadow::bottomLeftRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QCanvasBoxShadow16bottomLeftRadiusEv(
    const QCanvasBoxShadow *self) {
  return self->bottomLeftRadius();
}

//  void QCanvasBoxShadow::setBottomLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow19setBottomLeftRadiusEd(
    QCanvasBoxShadow *self,
    qreal radius) {
  self->setBottomLeftRadius(radius);
}

//  qreal QCanvasBoxShadow::bottomRightRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QCanvasBoxShadow17bottomRightRadiusEv(
    const QCanvasBoxShadow *self) {
  return self->bottomRightRadius();
}

//  void QCanvasBoxShadow::setBottomRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow20setBottomRightRadiusEd(
    QCanvasBoxShadow *self,
    qreal radius) {
  self->setBottomRightRadius(radius);
}

//  void QCanvasBoxShadow::swap(QCanvasBoxShadow &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCanvasBoxShadow4swapERS_(
    QCanvasBoxShadow *self,
    QCanvasBoxShadow *other) {
  self->swap(*other);
}

//  bool operator==(const QCanvasBoxShadow &lhs, const QCanvasBoxShadow &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QCanvasBoxShadowS1_(
    const QCanvasBoxShadow *lhs,
    const QCanvasBoxShadow *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCanvasBoxShadow &lhs, const QCanvasBoxShadow &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QCanvasBoxShadowS1_(
    const QCanvasBoxShadow *lhs,
    const QCanvasBoxShadow *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QCanvasBoxShadow::QCanvasBoxShadow(QCanvasBoxShadowPrivate *p)
extern "C" Q_DECL_EXPORT
QCanvasBoxShadow *ritual_ZN16QCanvasBoxShadowC1EP23QCanvasBoxShadowPrivate(
    QCanvasBoxShadowPrivate *p) {
  return new QCanvasBoxShadow(p);
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &a0, const QCanvasBoxShadow &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK16QCanvasBoxShadow(
    QDataStream *a0,
    const QCanvasBoxShadow *a1) {
  return &(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &a0, QCanvasBoxShadow &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR16QCanvasBoxShadow(
    QDataStream *a0,
    QCanvasBoxShadow *a1) {
  return &(operator>>(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QCanvasBoxShadow &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK16QCanvasBoxShadow(
    const QDebug *a0,
    const QCanvasBoxShadow *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
