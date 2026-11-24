//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dgeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QQuick3DGeometryPrivate that Python can take functions over in. Every QQuick3DGeometryPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DGeometryPrivateCall0)(const void *, int *);
class CuteQQuick3DGeometryPrivate : public QQuick3DGeometryPrivate {
public:
  using QQuick3DGeometryPrivate::QQuick3DGeometryPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QQuick3DObjectPrivate12updatePolishEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQuick3DObjectPrivate::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DGeometryPrivateCall0 call = reinterpret_cast<CuteQQuick3DGeometryPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObjectPrivate::updatePolish();
  }
};

//  QQuick3DGeometryPrivate::QQuick3DGeometryPrivate()
extern "C" Q_DECL_EXPORT
QQuick3DGeometryPrivate *ritual_ZN23QQuick3DGeometryPrivateC1Ev() {
  return new CuteQQuick3DGeometryPrivate();
}

//  QQuick3DGeometry::Attribute::Semantic
//      QQuick3DGeometryPrivate::semanticFromName(const QByteArray &name)
extern "C" Q_DECL_EXPORT
QQuick3DGeometry::Attribute::Semantic ritual_ZN23QQuick3DGeometryPrivate16semanticFromNameERK10QByteArray(
    const QByteArray *name) {
  return QQuick3DGeometryPrivate::semanticFromName(*name);
}

//  QQuick3DGeometry::Attribute::ComponentType
//      QQuick3DGeometryPrivate::toComponentType(QSSGMesh::Mesh::ComponentTyp
//      e componentType)
extern "C" Q_DECL_EXPORT
QQuick3DGeometry::Attribute::ComponentType ritual_ZN23QQuick3DGeometryPrivate15toComponentTypeE23QSSGRenderComponentType(
    QSSGMesh::Mesh::ComponentType componentType) {
  return QQuick3DGeometryPrivate::toComponentType(componentType);
}

//  a Python function taken by a CuteQQuick3DGeometryPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DGeometryPrivate(
    QQuick3DGeometryPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DGeometryPrivate *>(self)->take(key, call);
}
