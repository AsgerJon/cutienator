//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrview_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuick3DViewport *QQuick3DXrViewPrivate::getView3d(QQuick3DXrView *view)
extern "C" Q_DECL_EXPORT
QQuick3DViewport *ritual_ZN21QQuick3DXrViewPrivate9getView3dEP14QQuick3DXrView(
    QQuick3DXrView *view) {
  return QQuick3DXrViewPrivate::getView3d(view);
}

//  QQuick3DXrViewPrivate::~QQuick3DXrViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrViewPrivateD1Ev(QQuick3DXrViewPrivate *self) {
  delete self;
}
