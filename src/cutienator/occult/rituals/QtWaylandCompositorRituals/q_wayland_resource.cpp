//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandresource.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandresource.h>

//  void QWaylandResource::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandResource24qt_qmlMarker_uncreatableEv(
    QWaylandResource *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QWaylandResource::QWaylandResource()
extern "C" Q_DECL_EXPORT
QWaylandResource *ritual_ZN16QWaylandResourceC1Ev() {
  return new QWaylandResource();
}

//  QWaylandResource::~QWaylandResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandResourceD1Ev(QWaylandResource *self) {
  delete self;
}
