//  Written by dev_tooling.RitualGenerator from the records of QtLabsWavefron
//  tMesh/6.12.0/QtLabsWavefrontMesh/private/qwavefrontmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtLabsWavefrontMesh/6.12.0/QtLabsWavefrontMesh/private/qqmlwavefrontmeshglobal_p.h>
#include <QtLabsWavefrontMesh/QtLabsWavefrontMesh>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsWavefrontMesh/6.12.0/QtLabsWavefrontMesh/private/qwavefrontmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qrect.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWavefrontMesh that Python can take functions over in. Every QWavefrontMesh
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteQWavefrontMeshCall0)(const void *, QSGGeometry *, int, int, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef QString * (*CuteQWavefrontMeshCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWavefrontMeshCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWavefrontMeshCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWavefrontMeshCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWavefrontMeshCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWavefrontMeshCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWavefrontMeshCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWavefrontMeshCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWavefrontMesh : public QWavefrontMesh {
public:
  using QWavefrontMesh::QWavefrontMesh;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN22QQuickShaderEffectMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK22QQuickShaderEffectMesh3logEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_shadereffect)
  //  QSGGeometry *QWavefrontMesh::updateGeometry(QSGGeometry *geometry,
  //      int attrCount, int posIndex, const QRectF &srcRect, const QRectF
  //      &rect)
  QSGGeometry *updateGeometry(
      QSGGeometry *geometry,
      int attrCount,
      int posIndex,
      const QRectF &srcRect,
      const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWavefrontMeshCall0 call = reinterpret_cast<CuteQWavefrontMeshCall0>(taken[0]);
      void * given = call(this, geometry, attrCount, posIndex, &srcRect, &rect, &handled);
      if (handled) return static_cast<QSGGeometry *>(given);
    }
    return QWavefrontMesh::updateGeometry(geometry, attrCount, posIndex, srcRect, rect);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  QString QWavefrontMesh::log() const
  QString log() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWavefrontMeshCall1 call = reinterpret_cast<CuteQWavefrontMeshCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QWavefrontMesh::log();
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWavefrontMeshCall2 call = reinterpret_cast<CuteQWavefrontMeshCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWavefrontMeshCall3 call = reinterpret_cast<CuteQWavefrontMeshCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWavefrontMeshCall4 call = reinterpret_cast<CuteQWavefrontMeshCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWavefrontMeshCall5 call = reinterpret_cast<CuteQWavefrontMeshCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWavefrontMeshCall6 call = reinterpret_cast<CuteQWavefrontMeshCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWavefrontMeshCall7 call = reinterpret_cast<CuteQWavefrontMeshCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWavefrontMeshCall8 call = reinterpret_cast<CuteQWavefrontMeshCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWavefrontMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QWavefrontMesh10metaObjectEv(
    const QWavefrontMesh *self) {
  return self->metaObject();
}

//  QString QWavefrontMesh::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QWavefrontMesh2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWavefrontMesh::tr(s, c, n));
}

//  QWavefrontMesh::QWavefrontMesh(QObject *parent)
extern "C" Q_DECL_EXPORT
QWavefrontMesh *ritual_ZN14QWavefrontMeshC1EP7QObject(QObject *parent) {
  return new CuteQWavefrontMesh(parent);
}

//  QWavefrontMesh::~QWavefrontMesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWavefrontMeshD1Ev(QWavefrontMesh *self) {
  delete self;
}

//  QUrl QWavefrontMesh::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QWavefrontMesh6sourceEv(const QWavefrontMesh *self) {
  return new QUrl(self->source());
}

//  void QWavefrontMesh::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWavefrontMesh9setSourceERK4QUrl(
    QWavefrontMesh *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  Error QWavefrontMesh::lastError() const
extern "C" Q_DECL_EXPORT
QWavefrontMesh::Error ritual_ZNK14QWavefrontMesh9lastErrorEv(
    const QWavefrontMesh *self) {
  return self->lastError();
}

//  void QWavefrontMesh::setLastError(Error lastError)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWavefrontMesh12setLastErrorENS_5ErrorE(
    QWavefrontMesh *self,
    QWavefrontMesh::Error lastError) {
  self->setLastError(lastError);
}

//  bool QWavefrontMesh::validateAttributes(const QList<QByteArray>
//      &attributes, int *posIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWavefrontMesh18validateAttributesERK5QListI10QByteArrayEPi(
    QWavefrontMesh *self,
    const QList<QByteArray> *attributes,
    int *posIndex) {
  return self->validateAttributes(*attributes, posIndex);
}

//  QSGGeometry *QWavefrontMesh::updateGeometry(QSGGeometry *geometry, int
//      attrCount, int posIndex, const QRectF &srcRect, const QRectF &rect)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_ZN14QWavefrontMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_(
    QWavefrontMesh *self,
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

//  QString QWavefrontMesh::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWavefrontMesh3logEv(const QWavefrontMesh *self) {
  return new QString(self->log());
}

//  QVector3D QWavefrontMesh::projectionPlaneV() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK14QWavefrontMesh16projectionPlaneVEv(
    const QWavefrontMesh *self) {
  return new QVector3D(self->projectionPlaneV());
}

//  void QWavefrontMesh::setProjectionPlaneV(const QVector3D
//      &projectionPlaneV)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWavefrontMesh19setProjectionPlaneVERK9QVector3D(
    QWavefrontMesh *self,
    const QVector3D *projectionPlaneV) {
  self->setProjectionPlaneV(*projectionPlaneV);
}

//  QVector3D QWavefrontMesh::projectionPlaneW() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK14QWavefrontMesh16projectionPlaneWEv(
    const QWavefrontMesh *self) {
  return new QVector3D(self->projectionPlaneW());
}

//  void QWavefrontMesh::setProjectionPlaneW(const QVector3D
//      &projectionPlaneW)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWavefrontMesh19setProjectionPlaneWERK9QVector3D(
    QWavefrontMesh *self,
    const QVector3D *projectionPlaneW) {
  self->setProjectionPlaneW(*projectionPlaneW);
}

//  void QWavefrontMesh::readData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWavefrontMesh8readDataEv(QWavefrontMesh *self) {
  self->readData();
}

//  a Python function taken by a CuteQWavefrontMesh, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWavefrontMesh(
    QWavefrontMesh *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWavefrontMesh *>(self)->take(key, call);
}

//  QSGGeometry *QWavefrontMesh::updateGeometry(QSGGeometry *geometry, int
//      attrCount, int posIndex, const QRectF &srcRect, const QRectF &rect)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_own_ZN14QWavefrontMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_(
    QWavefrontMesh *self,
    QSGGeometry *geometry,
    int attrCount,
    int posIndex,
    const QRectF *srcRect,
    const QRectF *rect) {
  return self->QWavefrontMesh::updateGeometry(
      geometry,
      attrCount,
      posIndex,
      *srcRect,
      *rect);
}

//  QString QWavefrontMesh::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QWavefrontMesh3logEv(const QWavefrontMesh *self) {
  return new QString(self->QWavefrontMesh::log());
}
