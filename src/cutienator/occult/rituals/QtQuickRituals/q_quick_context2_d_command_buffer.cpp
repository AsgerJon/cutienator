//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcontext2dcommandbuffer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcontext2dcommandbuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcontext2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpen.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/private/qquickcanvasitem_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickcanvascontext_p.h>
#include <QtQuick/private/qquickcontext2d_p.h>
#include <QtQuick/private/qquickcontext2dtexture_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/qsgtextureprovider.h>
#include <QtQuick/private/qquickpixmap_p.h>
#include <QtGui/QGuiApplication>
#include <QtQuick/qsgtextureprovider.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtCore/QBuffer>
#include <QtCore/QDir>
#include <QtCore/qdatetime.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQuick/private/qquickcontext2dcommandbuffer_p.h>
#include <QtQuick/private/qquickcanvasitem_p.h>
#include <QtQml/qqml.h>
#include <QtCore/QMutex>
#include <QtQuick/qsgtexture.h>
#include <QtGui/QPaintEngine>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 53, as _ZN18QQuickCanvasPixmapD1Ev
inline QQuickCanvasPixmap::~QQuickCanvasPixmap()
{
    delete m_pixmap;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dcommandbuffer.cpp, line 437, as _ZN28QQuickContext2DCommandBufferC1Ev
inline QQuickContext2DCommandBuffer::QQuickContext2DCommandBuffer()
    : cmdIdx(0)
    , intIdx(0)
    , boolIdx(0)
    , realIdx(0)
    , rectIdx(0)
    , colorIdx(0)
    , matrixIdx(0)
    , brushIdx(0)
    , pathIdx(0)
    , imageIdx(0)
    , pixmapIdx(0)
{
    static bool registered = false;
    if (!registered) {
        qRegisterMetaType<QQuickContext2DCommandBuffer*>("QQuickContext2DCommandBuffer*");
        registered = true;
    }
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dcommandbuffer.cpp, line 458, as _ZN28QQuickContext2DCommandBufferD1Ev
inline QQuickContext2DCommandBuffer::~QQuickContext2DCommandBuffer()
{
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dcommandbuffer.cpp, line 478, as _ZN28QQuickContext2DCommandBuffer5resetEv
inline void QQuickContext2DCommandBuffer::reset()
{
    cmdIdx = 0;
    intIdx = 0;
    boolIdx = 0;
    realIdx = 0;
    rectIdx = 0;
    colorIdx = 0;
    matrixIdx = 0;
    brushIdx = 0;
    pathIdx = 0;
    imageIdx = 0;
    pixmapIdx = 0;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dcommandbuffer.cpp, line 462, as _ZN28QQuickContext2DCommandBuffer5clearEv
inline void QQuickContext2DCommandBuffer::clear()
{
    commands.clear();
    ints.clear();
    bools.clear();
    reals.clear();
    rects.clear();
    colors.clear();
    matrixes.clear();
    brushes.clear();
    pathes.clear();
    images.clear();
    pixmaps.clear();
    reset();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dcommandbuffer.cpp, line 148, as _ZN28QQuickContext2DCommandBuffer7makePenERKN15QQuickContext2D5StateE
inline QPen QQuickContext2DCommandBuffer::makePen(const QQuickContext2D::State& state)
{
    QPen pen;
    pen.setWidthF(state.lineWidth);
    pen.setCapStyle(state.lineCap);
    pen.setJoinStyle(state.lineJoin);
    pen.setMiterLimit(state.miterLimit);
    pen.setBrush(state.strokeStyle);
    if (!state.lineDash.isEmpty()) {
        pen.setDashPattern(state.lineDash);
    }
    pen.setDashOffset(state.lineDashOffset);
    return pen;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dcommandbuffer.cpp, line 163, as _ZN28QQuickContext2DCommandBuffer15setPainterStateEP8QPainterRKN15QQuickContext2D5StateERK4QPen
inline void QQuickContext2DCommandBuffer::setPainterState(QPainter* p, const QQuickContext2D::State& state, const QPen& pen)
{
   p->setTransform(state.matrix * p->transform());

   if (pen != p->pen())
       p->setPen(pen);

   if (state.fillStyle != p->brush())
       p->setBrush(state.fillStyle);

   if (state.font != p->font())
       p->setFont(state.font);

   if (state.globalAlpha != p->opacity()) {
       p->setOpacity(state.globalAlpha);
   }

   if (state.globalCompositeOperation != p->compositionMode())
       p->setCompositionMode(state.globalCompositeOperation);

   p->setClipping(state.clip);
   if (state.clip)
       p->setClipPath(state.clipPath);
}
//  -----------------------------------------------------------------------

//  QQuickContext2DCommandBuffer::QQuickContext2DCommandBuffer()
extern "C" Q_DECL_EXPORT
QQuickContext2DCommandBuffer *ritual_ZN28QQuickContext2DCommandBufferC1Ev() {
  return new QQuickContext2DCommandBuffer();
}

//  QQuickContext2DCommandBuffer::~QQuickContext2DCommandBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBufferD1Ev(
    QQuickContext2DCommandBuffer *self) {
  delete self;
}

//  void QQuickContext2DCommandBuffer::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer5resetEv(
    QQuickContext2DCommandBuffer *self) {
  self->reset();
}

//  void QQuickContext2DCommandBuffer::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer5clearEv(
    QQuickContext2DCommandBuffer *self) {
  self->clear();
}

//  int QQuickContext2DCommandBuffer::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuickContext2DCommandBuffer4sizeEv(
    const QQuickContext2DCommandBuffer *self) {
  return self->size();
}

//  bool QQuickContext2DCommandBuffer::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickContext2DCommandBuffer7isEmptyEv(
    const QQuickContext2DCommandBuffer *self) {
  return self->isEmpty();
}

//  bool QQuickContext2DCommandBuffer::hasNext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickContext2DCommandBuffer7hasNextEv(
    const QQuickContext2DCommandBuffer *self) {
  return self->hasNext();
}

//  QQuickContext2D::PaintCommand
//      QQuickContext2DCommandBuffer::takeNextCommand()
extern "C" Q_DECL_EXPORT
QQuickContext2D::PaintCommand ritual_ZN28QQuickContext2DCommandBuffer15takeNextCommandEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeNextCommand();
}

//  qreal QQuickContext2DCommandBuffer::takeGlobalAlpha()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN28QQuickContext2DCommandBuffer15takeGlobalAlphaEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeGlobalAlpha();
}

//  QPainter::CompositionMode
//      QQuickContext2DCommandBuffer::takeGlobalCompositeOperation()
extern "C" Q_DECL_EXPORT
QPainter::CompositionMode ritual_ZN28QQuickContext2DCommandBuffer28takeGlobalCompositeOperationEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeGlobalCompositeOperation();
}

//  QBrush QQuickContext2DCommandBuffer::takeStrokeStyle()
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN28QQuickContext2DCommandBuffer15takeStrokeStyleEv(
    QQuickContext2DCommandBuffer *self) {
  return new QBrush(self->takeStrokeStyle());
}

//  QBrush QQuickContext2DCommandBuffer::takeFillStyle()
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN28QQuickContext2DCommandBuffer13takeFillStyleEv(
    QQuickContext2DCommandBuffer *self) {
  return new QBrush(self->takeFillStyle());
}

//  qreal QQuickContext2DCommandBuffer::takeLineWidth()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN28QQuickContext2DCommandBuffer13takeLineWidthEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeLineWidth();
}

//  Qt::PenCapStyle QQuickContext2DCommandBuffer::takeLineCap()
extern "C" Q_DECL_EXPORT
Qt::PenCapStyle ritual_ZN28QQuickContext2DCommandBuffer11takeLineCapEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeLineCap();
}

//  Qt::PenJoinStyle QQuickContext2DCommandBuffer::takeLineJoin()
extern "C" Q_DECL_EXPORT
Qt::PenJoinStyle ritual_ZN28QQuickContext2DCommandBuffer12takeLineJoinEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeLineJoin();
}

//  qreal QQuickContext2DCommandBuffer::takeMiterLimit()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN28QQuickContext2DCommandBuffer14takeMiterLimitEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeMiterLimit();
}

//  void QQuickContext2DCommandBuffer::setGlobalAlpha(qreal alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer14setGlobalAlphaEd(
    QQuickContext2DCommandBuffer *self,
    qreal alpha) {
  self->setGlobalAlpha(alpha);
}

//  void QQuickContext2DCommandBuffer::setGlobalCompositeOperation(QPainter::
//      CompositionMode cm)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer27setGlobalCompositeOperationEN8QPainter15CompositionModeE(
    QQuickContext2DCommandBuffer *self,
    QPainter::CompositionMode cm) {
  self->setGlobalCompositeOperation(cm);
}

//  void QQuickContext2DCommandBuffer::setStrokeStyle(const QBrush &style,
//      bool repeatX, bool repeatY)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer14setStrokeStyleERK6QBrushbb(
    QQuickContext2DCommandBuffer *self,
    const QBrush *style,
    bool repeatX,
    bool repeatY) {
  self->setStrokeStyle(*style, repeatX, repeatY);
}

//  void QQuickContext2DCommandBuffer::drawImage(const QImage &image, const
//      QRectF &sr, const QRectF &dr)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer9drawImageERK6QImageRK6QRectFS5_(
    QQuickContext2DCommandBuffer *self,
    const QImage *image,
    const QRectF *sr,
    const QRectF *dr) {
  self->drawImage(*image, *sr, *dr);
}

//  qreal QQuickContext2DCommandBuffer::takeShadowOffsetX()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN28QQuickContext2DCommandBuffer17takeShadowOffsetXEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeShadowOffsetX();
}

//  qreal QQuickContext2DCommandBuffer::takeShadowOffsetY()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN28QQuickContext2DCommandBuffer17takeShadowOffsetYEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeShadowOffsetY();
}

//  qreal QQuickContext2DCommandBuffer::takeShadowBlur()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN28QQuickContext2DCommandBuffer14takeShadowBlurEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeShadowBlur();
}

//  QColor QQuickContext2DCommandBuffer::takeShadowColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN28QQuickContext2DCommandBuffer15takeShadowColorEv(
    QQuickContext2DCommandBuffer *self) {
  return new QColor(self->takeShadowColor());
}

//  void QQuickContext2DCommandBuffer::updateMatrix(const QTransform &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer12updateMatrixERK10QTransform(
    QQuickContext2DCommandBuffer *self,
    const QTransform *matrix) {
  self->updateMatrix(*matrix);
}

//  void QQuickContext2DCommandBuffer::clearRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer9clearRectERK6QRectF(
    QQuickContext2DCommandBuffer *self,
    const QRectF *r) {
  self->clearRect(*r);
}

//  void QQuickContext2DCommandBuffer::fillRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer8fillRectERK6QRectF(
    QQuickContext2DCommandBuffer *self,
    const QRectF *r) {
  self->fillRect(*r);
}

//  void QQuickContext2DCommandBuffer::strokeRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer10strokeRectERK6QRectF(
    QQuickContext2DCommandBuffer *self,
    const QRectF *r) {
  self->strokeRect(*r);
}

//  void QQuickContext2DCommandBuffer::fill(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer4fillERK12QPainterPath(
    QQuickContext2DCommandBuffer *self,
    const QPainterPath *path) {
  self->fill(*path);
}

//  void QQuickContext2DCommandBuffer::stroke(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer6strokeERK12QPainterPath(
    QQuickContext2DCommandBuffer *self,
    const QPainterPath *path) {
  self->stroke(*path);
}

//  void QQuickContext2DCommandBuffer::clip(bool enabled, const QPainterPath
//      &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer4clipEbRK12QPainterPath(
    QQuickContext2DCommandBuffer *self,
    bool enabled,
    const QPainterPath *path) {
  self->clip(enabled, *path);
}

//  void QQuickContext2DCommandBuffer::setFillStyle(const QBrush &style, bool
//      repeatX, bool repeatY)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer12setFillStyleERK6QBrushbb(
    QQuickContext2DCommandBuffer *self,
    const QBrush *style,
    bool repeatX,
    bool repeatY) {
  self->setFillStyle(*style, repeatX, repeatY);
}

//  void QQuickContext2DCommandBuffer::setLineWidth(qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer12setLineWidthEd(
    QQuickContext2DCommandBuffer *self,
    qreal w) {
  self->setLineWidth(w);
}

//  void QQuickContext2DCommandBuffer::setLineCap(Qt::PenCapStyle cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer10setLineCapEN2Qt11PenCapStyleE(
    QQuickContext2DCommandBuffer *self,
    Qt::PenCapStyle cap) {
  self->setLineCap(cap);
}

//  void QQuickContext2DCommandBuffer::setLineJoin(Qt::PenJoinStyle join)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer11setLineJoinEN2Qt12PenJoinStyleE(
    QQuickContext2DCommandBuffer *self,
    Qt::PenJoinStyle join) {
  self->setLineJoin(join);
}

//  void QQuickContext2DCommandBuffer::setLineDashOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer17setLineDashOffsetEd(
    QQuickContext2DCommandBuffer *self,
    qreal offset) {
  self->setLineDashOffset(offset);
}

//  void QQuickContext2DCommandBuffer::setMiterLimit(qreal limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer13setMiterLimitEd(
    QQuickContext2DCommandBuffer *self,
    qreal limit) {
  self->setMiterLimit(limit);
}

//  void QQuickContext2DCommandBuffer::setShadowOffsetX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer16setShadowOffsetXEd(
    QQuickContext2DCommandBuffer *self,
    qreal x) {
  self->setShadowOffsetX(x);
}

//  void QQuickContext2DCommandBuffer::setShadowOffsetY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer16setShadowOffsetYEd(
    QQuickContext2DCommandBuffer *self,
    qreal y) {
  self->setShadowOffsetY(y);
}

//  void QQuickContext2DCommandBuffer::setShadowBlur(qreal b)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer13setShadowBlurEd(
    QQuickContext2DCommandBuffer *self,
    qreal b) {
  self->setShadowBlur(b);
}

//  void QQuickContext2DCommandBuffer::setShadowColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer14setShadowColorERK6QColor(
    QQuickContext2DCommandBuffer *self,
    const QColor *color) {
  self->setShadowColor(*color);
}

//  QTransform QQuickContext2DCommandBuffer::takeMatrix()
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN28QQuickContext2DCommandBuffer10takeMatrixEv(
    QQuickContext2DCommandBuffer *self) {
  return new QTransform(self->takeMatrix());
}

//  QRectF QQuickContext2DCommandBuffer::takeRect()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN28QQuickContext2DCommandBuffer8takeRectEv(
    QQuickContext2DCommandBuffer *self) {
  return new QRectF(self->takeRect());
}

//  QPainterPath QQuickContext2DCommandBuffer::takePath()
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZN28QQuickContext2DCommandBuffer8takePathEv(
    QQuickContext2DCommandBuffer *self) {
  return new QPainterPath(self->takePath());
}

//  const QImage &QQuickContext2DCommandBuffer::takeImage()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN28QQuickContext2DCommandBuffer9takeImageEv(
    QQuickContext2DCommandBuffer *self) {
  return new QImage(self->takeImage());
}

//  int QQuickContext2DCommandBuffer::takeInt()
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuickContext2DCommandBuffer7takeIntEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeInt();
}

//  bool QQuickContext2DCommandBuffer::takeBool()
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QQuickContext2DCommandBuffer8takeBoolEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeBool();
}

//  qreal QQuickContext2DCommandBuffer::takeReal()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN28QQuickContext2DCommandBuffer8takeRealEv(
    QQuickContext2DCommandBuffer *self) {
  return self->takeReal();
}

//  QColor QQuickContext2DCommandBuffer::takeColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN28QQuickContext2DCommandBuffer9takeColorEv(
    QQuickContext2DCommandBuffer *self) {
  return new QColor(self->takeColor());
}

//  QBrush QQuickContext2DCommandBuffer::takeBrush()
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN28QQuickContext2DCommandBuffer9takeBrushEv(
    QQuickContext2DCommandBuffer *self) {
  return new QBrush(self->takeBrush());
}

//  QPen QQuickContext2DCommandBuffer::makePen(const QQuickContext2D::State
//      &state)
extern "C" Q_DECL_EXPORT
QPen *ritual_ZN28QQuickContext2DCommandBuffer7makePenERKN15QQuickContext2D5StateE(
    const QQuickContext2D::State *state) {
  return new QPen(QQuickContext2DCommandBuffer::makePen(*state));
}

//  void QQuickContext2DCommandBuffer::setPainterState(QPainter *painter,
//      const QQuickContext2D::State &state, const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickContext2DCommandBuffer15setPainterStateEP8QPainterRKN15QQuickContext2D5StateERK4QPen(
    QQuickContext2DCommandBuffer *self,
    QPainter *painter,
    const QQuickContext2D::State *state,
    const QPen *pen) {
  self->setPainterState(painter, *state, *pen);
}

#endif  // QT_CONFIG(quick_canvas)
#endif  // QT_CONFIG(quick_canvas)
