//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQuickGridMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickGridMesh10metaObjectEv(
    const QQuickGridMesh *self) {
  return self->metaObject();
}

//  QString QQuickGridMesh::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickGridMesh2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGridMesh::tr(s, c, n));
}

//  QQuickGridMesh::QQuickGridMesh(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickGridMesh *ritual_ZN14QQuickGridMeshC1EP7QObject(QObject *parent) {
  return new QQuickGridMesh(parent);
}

//  bool QQuickGridMesh::validateAttributes(const QList<QByteArray>
//      &attributes, int *posIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickGridMesh18validateAttributesERK5QListI10QByteArrayEPi(
    QQuickGridMesh *self,
    const QList<QByteArray> *attributes,
    int *posIndex) {
  return self->validateAttributes(*attributes, posIndex);
}

//  QSGGeometry *QQuickGridMesh::updateGeometry(QSGGeometry *geometry, int
//      attrCount, int posIndex, const QRectF &srcRect, const QRectF &rect)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_ZN14QQuickGridMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_(
    QQuickGridMesh *self,
    QSGGeometry *geometry,
    int attrCount,
    int posIndex,
    const QRectF *srcRect,
    const QRectF *rect) {
  return self->updateGeometry(
      geometry,
      attrCount,
      posIndex,
      *srcRect,
      *rect);
}

//  QString QQuickGridMesh::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickGridMesh3logEv(const QQuickGridMesh *self) {
  return new QString(self->log());
}

//  void QQuickGridMesh::setResolution(const QSize &res)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGridMesh13setResolutionERK5QSize(
    QQuickGridMesh *self,
    const QSize *res) {
  self->setResolution(*res);
}

//  QSize QQuickGridMesh::resolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QQuickGridMesh10resolutionEv(const QQuickGridMesh *self) {
  return new QSize(self->resolution());
}

//  QSGGeometry *QQuickGridMesh::updateGeometry(QSGGeometry *geometry, int
//      attrCount, int posIndex, const QRectF &srcRect, const QRectF &rect)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_own_ZN14QQuickGridMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_(
    QQuickGridMesh *self,
    QSGGeometry *geometry,
    int attrCount,
    int posIndex,
    const QRectF *srcRect,
    const QRectF *rect) {
  return self->QQuickGridMesh::updateGeometry(
      geometry,
      attrCount,
      posIndex,
      *srcRect,
      *rect);
}

//  QString QQuickGridMesh::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QQuickGridMesh3logEv(const QQuickGridMesh *self) {
  return new QString(self->QQuickGridMesh::log());
}

#endif  // QT_CONFIG(quick_shadereffect)
