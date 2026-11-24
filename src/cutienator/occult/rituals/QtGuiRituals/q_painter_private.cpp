//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpainter_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qpainter.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/qtransform.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <memory>
#include <qdebug.h>
#include <qmath.h>
#include <qmutex.h>
#include "qbitmap.h"
#include "qimage.h"
#include "qpaintdevice.h"
#include "qpaintengine.h"
#include "qpainter.h"
#include "qpainter_p.h"
#include "qpainterpath.h"
#include "qpicture.h"
#include "qpixmapcache.h"
#include "qpolygon.h"
#include "qtextlayout.h"
#include "qthread.h"
#include "qvarlengtharray.h"
#include "qstatictext.h"
#include "qglyphrun.h"
#include <qpa/qplatformtheme.h>
#include <qpa/qplatformintegration.h>
#include <private/qfontengine_p.h>
#include <private/qpaintengine_p.h>
#include <private/qemulationpaintengine_p.h>
#include <private/qpainterpath_p.h>
#include <private/qtextengine_p.h>
#include <private/qpaintengine_raster_p.h>
#include <private/qmath_p.h>
#include <private/qstatictext_p.h>
#include <private/qglyphrun_p.h>
#include <private/qhexstring_p.h>
#include <private/qguiapplication_p.h>
#include <private/qrawfont_p.h>
#include <private/qfont_p.h>
#include <QtCore/private/qtclasshelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpainter.cpp, line 475, as _ZN15QPainterPrivate20drawOpaqueBackgroundERK12QPainterPathNS_13DrawOperationE
inline void QPainterPrivate::drawOpaqueBackground(const QPainterPath &path, DrawOperation op)
{
    Q_Q(QPainter);

    q->setBackgroundMode(Qt::TransparentMode);

    if (op & FillDraw && state->brush.style() != Qt::NoBrush) {
        q->fillPath(path, state->bgBrush.color());
        q->fillPath(path, state->brush);
    }

    if (op & StrokeDraw && state->pen.style() != Qt::NoPen) {
        q->strokePath(path, QPen(state->bgBrush.color(), state->pen.width()));
        q->strokePath(path, state->pen);
    }

    q->setBackgroundMode(Qt::OpaqueMode);
}

//  from src/gui/painting/qpainter.cpp, line 628, as _ZN15QPainterPrivate12updateMatrixEv
inline void QPainterPrivate::updateMatrix()
{
    state->matrix = state->WxF ? state->worldMatrix : QTransform();
    if (state->VxF)
        state->matrix *= viewTransform();

    txinv = false;                                // no inverted matrix
    state->matrix *= state->redirectionMatrix;
    if (extended)
        extended->transformChanged();
    else
        state->dirtyFlags |= QPaintEngine::DirtyTransform;

    state->matrix *= hidpiScaleTransform();

//     printf("VxF=%d, WxF=%d\n", state->VxF, state->WxF);
//     qDebug() << " --- using matrix" << state->matrix << redirection_offset;
}

//  from src/gui/painting/qpainter.cpp, line 648, as _ZN15QPainterPrivate15updateInvMatrixEv
inline void QPainterPrivate::updateInvMatrix()
{
    Q_ASSERT(txinv == false);
    txinv = true;                                // creating inverted matrix
    invMatrix = state->matrix.inverted();
}

//  from src/gui/painting/qpainter.cpp, line 210, as _ZNK15QPainterPrivate13viewTransformEv
inline QTransform QPainterPrivate::viewTransform() const
{
    if (state->VxF) {
        qreal scaleW = qreal(state->vw)/qreal(state->ww);
        qreal scaleH = qreal(state->vh)/qreal(state->wh);
        return QTransform(scaleW, 0, 0, scaleH,
                          state->vx - state->wx*scaleW, state->vy - state->wy*scaleH);
    }
    return QTransform();
}

//  from src/gui/painting/qpainter.cpp, line 221, as _ZNK15QPainterPrivate25effectiveDevicePixelRatioEv
inline qreal QPainterPrivate::effectiveDevicePixelRatio() const
{
    // Special cases for devices that does not support PdmDevicePixelRatio go here:
    if (device->devType() == QInternal::Printer)
        return qreal(1);

    return device->devicePixelRatio();
}

//  from src/gui/painting/qpainter.cpp, line 230, as _ZNK15QPainterPrivate19hidpiScaleTransformEv
inline QTransform QPainterPrivate::hidpiScaleTransform() const
{
    const qreal devicePixelRatio = effectiveDevicePixelRatio();
    return QTransform::fromScale(devicePixelRatio, devicePixelRatio);
}

//  from src/gui/painting/qpainter.cpp, line 1535, as _ZN15QPainterPrivate8initFromEPK12QPaintDevice
inline void QPainterPrivate::initFrom(const QPaintDevice *device)
{
    if (!engine) {
        qWarning("QPainter::initFrom: Painter not active, aborted");
        return;
    }

    Q_Q(QPainter);
    device->initPainter(q);
}
//  -----------------------------------------------------------------------

//  QPainter *QPainterPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZN15QPainterPrivate6q_funcEv(QPainterPrivate *self) {
  return self->q_func();
}

//  const QPainter *QPainterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPainter *ritual_ZNK15QPainterPrivate6q_funcEv(
    const QPainterPrivate *self) {
  return self->q_func();
}

//  QPainterDummyState *QPainterPrivate::fakeState() const
extern "C" Q_DECL_EXPORT
QPainterDummyState *ritual_ZNK15QPainterPrivate9fakeStateEv(
    const QPainterPrivate *self) {
  return self->fakeState();
}

//  void QPainterPrivate::drawOpaqueBackground(const QPainterPath &path,
//      DrawOperation operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate20drawOpaqueBackgroundERK12QPainterPathNS_13DrawOperationE(
    QPainterPrivate *self,
    const QPainterPath *path,
    QPainterPrivate::DrawOperation operation) {
  self->drawOpaqueBackground(*path, operation);
}

//  void QPainterPrivate::updateMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate12updateMatrixEv(QPainterPrivate *self) {
  self->updateMatrix();
}

//  void QPainterPrivate::updateInvMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate15updateInvMatrixEv(QPainterPrivate *self) {
  self->updateInvMatrix();
}

//  QPainterPrivate *QPainterPrivate::get(QPainter *painter)
extern "C" Q_DECL_EXPORT
QPainterPrivate *ritual_ZN15QPainterPrivate3getEP8QPainter(
    QPainter *painter) {
  return QPainterPrivate::get(painter);
}

//  QTransform QPainterPrivate::viewTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK15QPainterPrivate13viewTransformEv(
    const QPainterPrivate *self) {
  return new QTransform(self->viewTransform());
}

//  qreal QPainterPrivate::effectiveDevicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QPainterPrivate25effectiveDevicePixelRatioEv(
    const QPainterPrivate *self) {
  return self->effectiveDevicePixelRatio();
}

//  QTransform QPainterPrivate::hidpiScaleTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK15QPainterPrivate19hidpiScaleTransformEv(
    const QPainterPrivate *self) {
  return new QTransform(self->hidpiScaleTransform());
}

//  void QPainterPrivate::initFrom(const QPaintDevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPainterPrivate8initFromEPK12QPaintDevice(
    QPainterPrivate *self,
    const QPaintDevice *device) {
  self->initFrom(device);
}
