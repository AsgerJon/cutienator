//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlight_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhicustommaterialsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendereffect_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendercamera_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderskeleton_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderjoint_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendermorphtarget_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/private/qssgperframeallocator_p.h>
#include <QtQuick3DRuntimeRender/private/qssgruntimerenderlogging_p.h>
#include <QtQuick3DRuntimeRender/private/qssglightmapper_p.h>
#include <QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtCore/qspan.h>
#include <array>
#include <QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssglayerrenderdata.cpp, line 3121, as _ZN32QSSGLayerRenderPreparationResultC1ERK6QRectFR15QSSGRenderLayer
inline QSSGLayerRenderPreparationResult::QSSGLayerRenderPreparationResult(const QRectF &inViewport, QSSGRenderLayer &inLayer)
    : layer(&inLayer)
    , m_state(State::DataPrep)
{
    viewport = inViewport;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssglayerrenderdata.cpp, line 3128, as _ZNK32QSSGLayerRenderPreparationResult14isLayerVisibleEv
inline bool QSSGLayerRenderPreparationResult::isLayerVisible() const
{
    return viewport.height() >= 2.0f && viewport.width() >= 2.0f;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssglayerrenderdata.cpp, line 3133, as _ZNK32QSSGLayerRenderPreparationResult17textureDimensionsEv
inline QSize QSSGLayerRenderPreparationResult::textureDimensions() const
{
    const auto size = viewport.size().toSize();
    return QSize(QSSGRendererUtil::nextMultipleOf4(size.width()), QSSGRendererUtil::nextMultipleOf4(size.height()));
}
//  -----------------------------------------------------------------------

//  QSSGLayerRenderPreparationResult::QSSGLayerRenderPreparationResult()
extern "C" Q_DECL_EXPORT
QSSGLayerRenderPreparationResult *ritual_ZN32QSSGLayerRenderPreparationResultC1Ev() {
  return new QSSGLayerRenderPreparationResult();
}

//  QSSGLayerRenderPreparationResult::QSSGLayerRenderPreparationResult(const
//      QRectF &inViewport, QSSGRenderLayer &inLayer)
extern "C" Q_DECL_EXPORT
QSSGLayerRenderPreparationResult *ritual_ZN32QSSGLayerRenderPreparationResultC1ERK6QRectFR15QSSGRenderLayer(
    const QRectF *inViewport,
    QSSGRenderLayer *inLayer) {
  return new QSSGLayerRenderPreparationResult(*inViewport, *inLayer);
}

//  void QSSGLayerRenderPreparationResult::setState(State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGLayerRenderPreparationResult8setStateENS_5StateE(
    QSSGLayerRenderPreparationResult *self,
    QSSGLayerRenderPreparationResult::State state) {
  self->setState(state);
}

//  State QSSGLayerRenderPreparationResult::getState() const
extern "C" Q_DECL_EXPORT
QSSGLayerRenderPreparationResult::State ritual_ZNK32QSSGLayerRenderPreparationResult8getStateEv(
    const QSSGLayerRenderPreparationResult *self) {
  return self->getState();
}

//  bool QSSGLayerRenderPreparationResult::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QSSGLayerRenderPreparationResult6isNullEv(
    const QSSGLayerRenderPreparationResult *self) {
  return self->isNull();
}

//  bool QSSGLayerRenderPreparationResult::isLayerVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QSSGLayerRenderPreparationResult14isLayerVisibleEv(
    const QSSGLayerRenderPreparationResult *self) {
  return self->isLayerVisible();
}

//  QSize QSSGLayerRenderPreparationResult::textureDimensions() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK32QSSGLayerRenderPreparationResult17textureDimensionsEv(
    const QSSGLayerRenderPreparationResult *self) {
  return new QSize(self->textureDimensions());
}

//  QRectF QSSGLayerRenderPreparationResult::getViewport() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK32QSSGLayerRenderPreparationResult11getViewportEv(
    const QSSGLayerRenderPreparationResult *self) {
  return new QRectF(self->getViewport());
}

//  const QSSGLayerRenderPreparationResultFlags
//      &QSSGLayerRenderPreparationResult::getFlags() const
extern "C" Q_DECL_EXPORT
QSSGLayerRenderPreparationResultFlags *ritual_ZNK32QSSGLayerRenderPreparationResult8getFlagsEv(
    const QSSGLayerRenderPreparationResult *self) {
  return new QSSGLayerRenderPreparationResultFlags(self->getFlags());
}

//  QSSGRenderLayer *QSSGLayerRenderPreparationResult::getLayer() const
extern "C" Q_DECL_EXPORT
QSSGRenderLayer *ritual_ZNK32QSSGLayerRenderPreparationResult8getLayerEv(
    const QSSGLayerRenderPreparationResult *self) {
  return self->getLayer();
}

//  QSSGLayerRenderPreparationResult::~QSSGLayerRenderPreparationResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGLayerRenderPreparationResultD1Ev(
    QSSGLayerRenderPreparationResult *self) {
  delete self;
}
