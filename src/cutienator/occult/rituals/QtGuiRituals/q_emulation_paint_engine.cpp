//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qemulationpaintengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qemulationpaintengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qemulationpaintengine_p.h>
#include <QtGui/private/qpainter_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qemulationpaintengine.cpp, line 112, as _ZN21QEmulationPaintEngine4clipERK11QVectorPathN2Qt13ClipOperationE
inline void QEmulationPaintEngine::clip(const QVectorPath &path, Qt::ClipOperation op)
{
    real_engine->clip(path, op);
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 24, as _ZN21QEmulationPaintEngine5beginEP12QPaintDevice
inline bool QEmulationPaintEngine::begin(QPaintDevice *)
{
    return true;
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 29, as _ZN21QEmulationPaintEngine3endEv
inline bool QEmulationPaintEngine::end()
{
    return true;
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 19, as _ZNK21QEmulationPaintEngine4typeEv
inline QPaintEngine::Type QEmulationPaintEngine::type() const
{
    return real_engine->type();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 35, as _ZNK21QEmulationPaintEngine11createStateEP13QPainterState
inline QPainterState *QEmulationPaintEngine::createState(QPainterState *orig) const
{
    return real_engine->createState(orig);
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 117, as _ZN21QEmulationPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_
inline void QEmulationPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm, const QRectF &sr)
{
    if (state()->bgMode == Qt::OpaqueMode && pm.isQBitmap())
        fillBGRect(r);
    real_engine->drawPixmap(r, pm, sr);
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 162, as _ZN21QEmulationPaintEngine18drawStaticTextItemEP15QStaticTextItem
inline void QEmulationPaintEngine::drawStaticTextItem(QStaticTextItem *item)
{
    real_engine->drawStaticTextItem(item);
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 167, as _ZN21QEmulationPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF
inline void QEmulationPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap &pixmap, const QPointF &s)
{
    if (state()->bgMode == Qt::OpaqueMode && pixmap.isQBitmap())
        fillBGRect(r);
    real_engine->drawTiledPixmap(r, pixmap, s);
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 174, as _ZN21QEmulationPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE
inline void QEmulationPaintEngine::drawImage(const QRectF &r, const QImage &pm, const QRectF &sr, Qt::ImageConversionFlags flags)
{
    real_engine->drawImage(r, pm, sr, flags);
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 179, as _ZN21QEmulationPaintEngine18clipEnabledChangedEv
inline void QEmulationPaintEngine::clipEnabledChanged()
{
    real_engine->clipEnabledChanged();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 184, as _ZN21QEmulationPaintEngine10penChangedEv
inline void QEmulationPaintEngine::penChanged()
{
    real_engine->penChanged();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 189, as _ZN21QEmulationPaintEngine12brushChangedEv
inline void QEmulationPaintEngine::brushChanged()
{
    real_engine->brushChanged();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 194, as _ZN21QEmulationPaintEngine18brushOriginChangedEv
inline void QEmulationPaintEngine::brushOriginChanged()
{
    real_engine->brushOriginChanged();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 199, as _ZN21QEmulationPaintEngine14opacityChangedEv
inline void QEmulationPaintEngine::opacityChanged()
{
    real_engine->opacityChanged();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 204, as _ZN21QEmulationPaintEngine22compositionModeChangedEv
inline void QEmulationPaintEngine::compositionModeChanged()
{
    real_engine->compositionModeChanged();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 209, as _ZN21QEmulationPaintEngine18renderHintsChangedEv
inline void QEmulationPaintEngine::renderHintsChanged()
{
    real_engine->renderHintsChanged();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 214, as _ZN21QEmulationPaintEngine16transformChangedEv
inline void QEmulationPaintEngine::transformChanged()
{
    real_engine->transformChanged();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 219, as _ZN21QEmulationPaintEngine8setStateEP13QPainterState
inline void QEmulationPaintEngine::setState(QPainterState *s)
{
    QPaintEngine::state = s;
    real_engine->setState(s);
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 225, as _ZN21QEmulationPaintEngine19beginNativePaintingEv
inline void QEmulationPaintEngine::beginNativePainting()
{
    real_engine->beginNativePainting();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 230, as _ZN21QEmulationPaintEngine17endNativePaintingEv
inline void QEmulationPaintEngine::endNativePainting()
{
    real_engine->endNativePainting();
}

//  from src/gui/painting/qemulationpaintengine.cpp, line 235, as _ZN21QEmulationPaintEngine10fillBGRectERK6QRectF
inline void QEmulationPaintEngine::fillBGRect(const QRectF &r)
{
    qreal pts[] = { r.x(), r.y(), r.x() + r.width(), r.y(),
                    r.x() + r.width(), r.y() + r.height(), r.x(), r.y() + r.height() };
    QVectorPath vp(pts, 4, nullptr, QVectorPath::RectangleHint);
    real_engine->fill(vp, state()->bgBrush);
}
//  -----------------------------------------------------------------------

//  bool QEmulationPaintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QEmulationPaintEngine5beginEP12QPaintDevice(
    QEmulationPaintEngine *self,
    QPaintDevice *pdev) {
  return self->begin(pdev);
}

//  bool QEmulationPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QEmulationPaintEngine3endEv(QEmulationPaintEngine *self) {
  return self->end();
}

//  Type QEmulationPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK21QEmulationPaintEngine4typeEv(
    const QEmulationPaintEngine *self) {
  return self->type();
}

//  QPainterState *QEmulationPaintEngine::createState(QPainterState *orig)
//      const
extern "C" Q_DECL_EXPORT
QPainterState *ritual_ZNK21QEmulationPaintEngine11createStateEP13QPainterState(
    const QEmulationPaintEngine *self,
    QPainterState *orig) {
  return self->createState(orig);
}

//  void QEmulationPaintEngine::drawPixmap(const QRectF &r, const QPixmap
//      &pm, const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QEmulationPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QEmulationPaintEngine::drawStaticTextItem(QStaticTextItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine18drawStaticTextItemEP15QStaticTextItem(
    QEmulationPaintEngine *self,
    QStaticTextItem *item) {
  self->drawStaticTextItem(item);
}

//  void QEmulationPaintEngine::drawTiledPixmap(const QRectF &r, const
//      QPixmap &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QEmulationPaintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->drawTiledPixmap(*r, *pixmap, *s);
}

//  void QEmulationPaintEngine::drawImage(const QRectF &r, const QImage &pm,
//      const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QEmulationPaintEngine *self,
    const QRectF *r,
    const QImage *pm,
    const QRectF *sr,
    int flags) {
  self->drawImage(
      *r,
      *pm,
      *sr,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QEmulationPaintEngine::clipEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine18clipEnabledChangedEv(
    QEmulationPaintEngine *self) {
  self->clipEnabledChanged();
}

//  void QEmulationPaintEngine::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine10penChangedEv(
    QEmulationPaintEngine *self) {
  self->penChanged();
}

//  void QEmulationPaintEngine::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine12brushChangedEv(
    QEmulationPaintEngine *self) {
  self->brushChanged();
}

//  void QEmulationPaintEngine::brushOriginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine18brushOriginChangedEv(
    QEmulationPaintEngine *self) {
  self->brushOriginChanged();
}

//  void QEmulationPaintEngine::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine14opacityChangedEv(
    QEmulationPaintEngine *self) {
  self->opacityChanged();
}

//  void QEmulationPaintEngine::compositionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine22compositionModeChangedEv(
    QEmulationPaintEngine *self) {
  self->compositionModeChanged();
}

//  void QEmulationPaintEngine::renderHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine18renderHintsChangedEv(
    QEmulationPaintEngine *self) {
  self->renderHintsChanged();
}

//  void QEmulationPaintEngine::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine16transformChangedEv(
    QEmulationPaintEngine *self) {
  self->transformChanged();
}

//  void QEmulationPaintEngine::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine8setStateEP13QPainterState(
    QEmulationPaintEngine *self,
    QPainterState *s) {
  self->setState(s);
}

//  void QEmulationPaintEngine::beginNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine19beginNativePaintingEv(
    QEmulationPaintEngine *self) {
  self->beginNativePainting();
}

//  void QEmulationPaintEngine::endNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine17endNativePaintingEv(
    QEmulationPaintEngine *self) {
  self->endNativePainting();
}

//  uint QEmulationPaintEngine::flags() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK21QEmulationPaintEngine5flagsEv(
    const QEmulationPaintEngine *self) {
  return self->flags();
}

//  QPainterState *QEmulationPaintEngine::state()
extern "C" Q_DECL_EXPORT
QPainterState *ritual_ZN21QEmulationPaintEngine5stateEv(
    QEmulationPaintEngine *self) {
  return self->state();
}

//  const QPainterState *QEmulationPaintEngine::state() const
extern "C" Q_DECL_EXPORT
const QPainterState *ritual_ZNK21QEmulationPaintEngine5stateEv(
    const QEmulationPaintEngine *self) {
  return self->state();
}

//  void QEmulationPaintEngine::fillBGRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEmulationPaintEngine10fillBGRectERK6QRectF(
    QEmulationPaintEngine *self,
    const QRectF *r) {
  self->fillBGRect(*r);
}

//  bool QEmulationPaintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QEmulationPaintEngine5beginEP12QPaintDevice(
    QEmulationPaintEngine *self,
    QPaintDevice *pdev) {
  return self->QEmulationPaintEngine::begin(pdev);
}

//  bool QEmulationPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QEmulationPaintEngine3endEv(
    QEmulationPaintEngine *self) {
  return self->QEmulationPaintEngine::end();
}

//  Type QEmulationPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_own_ZNK21QEmulationPaintEngine4typeEv(
    const QEmulationPaintEngine *self) {
  return self->QEmulationPaintEngine::type();
}

//  QPainterState *QEmulationPaintEngine::createState(QPainterState *orig)
//      const
extern "C" Q_DECL_EXPORT
QPainterState *ritual_own_ZNK21QEmulationPaintEngine11createStateEP13QPainterState(
    const QEmulationPaintEngine *self,
    QPainterState *orig) {
  return self->QEmulationPaintEngine::createState(orig);
}

//  void QEmulationPaintEngine::drawPixmap(const QRectF &r, const QPixmap
//      &pm, const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QEmulationPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->QEmulationPaintEngine::drawPixmap(*r, *pm, *sr);
}

//  void QEmulationPaintEngine::drawStaticTextItem(QStaticTextItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine18drawStaticTextItemEP15QStaticTextItem(
    QEmulationPaintEngine *self,
    QStaticTextItem *item) {
  self->QEmulationPaintEngine::drawStaticTextItem(item);
}

//  void QEmulationPaintEngine::drawTiledPixmap(const QRectF &r, const
//      QPixmap &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QEmulationPaintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->QEmulationPaintEngine::drawTiledPixmap(*r, *pixmap, *s);
}

//  void QEmulationPaintEngine::drawImage(const QRectF &r, const QImage &pm,
//      const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QEmulationPaintEngine *self,
    const QRectF *r,
    const QImage *pm,
    const QRectF *sr,
    int flags) {
  self->QEmulationPaintEngine::drawImage(
      *r,
      *pm,
      *sr,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QEmulationPaintEngine::clipEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine18clipEnabledChangedEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::clipEnabledChanged();
}

//  void QEmulationPaintEngine::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine10penChangedEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::penChanged();
}

//  void QEmulationPaintEngine::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine12brushChangedEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::brushChanged();
}

//  void QEmulationPaintEngine::brushOriginChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine18brushOriginChangedEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::brushOriginChanged();
}

//  void QEmulationPaintEngine::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine14opacityChangedEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::opacityChanged();
}

//  void QEmulationPaintEngine::compositionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine22compositionModeChangedEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::compositionModeChanged();
}

//  void QEmulationPaintEngine::renderHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine18renderHintsChangedEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::renderHintsChanged();
}

//  void QEmulationPaintEngine::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine16transformChangedEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::transformChanged();
}

//  void QEmulationPaintEngine::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine8setStateEP13QPainterState(
    QEmulationPaintEngine *self,
    QPainterState *s) {
  self->QEmulationPaintEngine::setState(s);
}

//  void QEmulationPaintEngine::beginNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine19beginNativePaintingEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::beginNativePainting();
}

//  void QEmulationPaintEngine::endNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEmulationPaintEngine17endNativePaintingEv(
    QEmulationPaintEngine *self) {
  self->QEmulationPaintEngine::endNativePainting();
}

//  uint QEmulationPaintEngine::flags() const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK21QEmulationPaintEngine5flagsEv(
    const QEmulationPaintEngine *self) {
  return self->QEmulationPaintEngine::flags();
}
