//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/q3dscene_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/q3dscene.h>
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/q3dscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

//  Q3DScene *Q3DScenePrivate::q_func()
extern "C" Q_DECL_EXPORT
Q3DScene *ritual_ZN15Q3DScenePrivate6q_funcEv(Q3DScenePrivate *self) {
  return self->q_func();
}

//  const Q3DScene *Q3DScenePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Q3DScene *ritual_ZNK15Q3DScenePrivate6q_funcEv(
    const Q3DScenePrivate *self) {
  return self->q_func();
}

//  Q3DScenePrivate::Q3DScenePrivate()
extern "C" Q_DECL_EXPORT
Q3DScenePrivate *ritual_ZN15Q3DScenePrivateC1Ev() {
  return new Q3DScenePrivate();
}

//  Q3DScenePrivate::~Q3DScenePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivateD1Ev(Q3DScenePrivate *self) {
  delete self;
}

//  void Q3DScenePrivate::sync(Q3DScenePrivate &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate4syncERS_(
    Q3DScenePrivate *self,
    Q3DScenePrivate *other) {
  self->sync(*other);
}

//  void Q3DScenePrivate::setViewport(const QRect viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate11setViewportE5QRect(
    Q3DScenePrivate *self,
    const QRect *viewport) {
  self->setViewport(*viewport);
}

//  void Q3DScenePrivate::setViewportSize(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate15setViewportSizeEii(
    Q3DScenePrivate *self,
    int width,
    int height) {
  self->setViewportSize(width, height);
}

//  void Q3DScenePrivate::setWindowSize(QSize size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate13setWindowSizeE5QSize(
    Q3DScenePrivate *self,
    const QSize *size) {
  self->setWindowSize(*size);
}

//  QSize Q3DScenePrivate::windowSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15Q3DScenePrivate10windowSizeEv(
    const Q3DScenePrivate *self) {
  return new QSize(self->windowSize());
}

//  void Q3DScenePrivate::updateDefaultViewports()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate22updateDefaultViewportsEv(
    Q3DScenePrivate *self) {
  self->updateDefaultViewports();
}

//  void Q3DScenePrivate::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate9markDirtyEv(Q3DScenePrivate *self) {
  self->markDirty();
}

//  bool Q3DScenePrivate::isInArea(const QRect area, int x, int y) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15Q3DScenePrivate8isInAreaE5QRectii(
    const Q3DScenePrivate *self,
    const QRect *area,
    int x,
    int y) {
  return self->isInArea(*area, x, y);
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
