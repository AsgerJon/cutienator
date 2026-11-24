//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrruntimeinfo_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrruntimeinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQuick3DXrRuntimeInfo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DXrRuntimeInfo10metaObjectEv(
    const QQuick3DXrRuntimeInfo *self) {
  return self->metaObject();
}

//  QString QQuick3DXrRuntimeInfo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuick3DXrRuntimeInfo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrRuntimeInfo::tr(s, c, n));
}

//  void QQuick3DXrRuntimeInfo::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DXrRuntimeInfo24qt_qmlMarker_uncreatableEv(
    QQuick3DXrRuntimeInfo *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DXrRuntimeInfo::QQuick3DXrRuntimeInfo(QQuick3DXrManager *manager,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DXrRuntimeInfo *ritual_ZN21QQuick3DXrRuntimeInfoC1EP17QQuick3DXrManagerP7QObject(
    QQuick3DXrManager *manager,
    QObject *parent) {
  return new QQuick3DXrRuntimeInfo(manager, parent);
}

//  QStringList QQuick3DXrRuntimeInfo::enabledExtensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QQuick3DXrRuntimeInfo17enabledExtensionsEv(
    const QQuick3DXrRuntimeInfo *self) {
  return new QList<QString>(self->enabledExtensions());
}

//  QString QQuick3DXrRuntimeInfo::runtimeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuick3DXrRuntimeInfo11runtimeNameEv(
    const QQuick3DXrRuntimeInfo *self) {
  return new QString(self->runtimeName());
}

//  QString QQuick3DXrRuntimeInfo::runtimeVersion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuick3DXrRuntimeInfo14runtimeVersionEv(
    const QQuick3DXrRuntimeInfo *self) {
  return new QString(self->runtimeVersion());
}

//  QString QQuick3DXrRuntimeInfo::graphicsApiName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuick3DXrRuntimeInfo15graphicsApiNameEv(
    const QQuick3DXrRuntimeInfo *self) {
  return new QString(self->graphicsApiName());
}
