//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickShaderEffectMesh that Python can take functions over in. Every QQuickShaderEffectMesh
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteQQuickShaderEffectMeshCall0)(const void *, QSGGeometry *, int, int, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef QString * (*CuteQQuickShaderEffectMeshCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShaderEffectMeshCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShaderEffectMeshCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectMeshCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectMeshCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectMeshCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectMeshCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShaderEffectMeshCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickShaderEffectMesh : public QQuickShaderEffectMesh {
public:
  using QQuickShaderEffectMesh::QQuickShaderEffectMesh;
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
  //  QSGGeometry *QQuickShaderEffectMesh::updateGeometry(QSGGeometry
  //      *geometry, int attrCount, int posIndex, const QRectF &srcRect,
  //      const QRectF &rect)
  QSGGeometry *updateGeometry(
      QSGGeometry *geometry,
      int attrCount,
      int posIndex,
      const QRectF &srcRect,
      const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShaderEffectMeshCall0 call = reinterpret_cast<CuteQQuickShaderEffectMeshCall0>(taken[0]);
      void * given = call(this, geometry, attrCount, posIndex, &srcRect, &rect, &handled);
      if (handled) return static_cast<QSGGeometry *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  QString QQuickShaderEffectMesh::log() const
  QString log() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShaderEffectMeshCall1 call = reinterpret_cast<CuteQQuickShaderEffectMeshCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickShaderEffectMesh::log();
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShaderEffectMeshCall2 call = reinterpret_cast<CuteQQuickShaderEffectMeshCall2>(taken[2]);
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
      CuteQQuickShaderEffectMeshCall3 call = reinterpret_cast<CuteQQuickShaderEffectMeshCall3>(taken[3]);
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
      CuteQQuickShaderEffectMeshCall4 call = reinterpret_cast<CuteQQuickShaderEffectMeshCall4>(taken[4]);
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
      CuteQQuickShaderEffectMeshCall5 call = reinterpret_cast<CuteQQuickShaderEffectMeshCall5>(taken[5]);
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
      CuteQQuickShaderEffectMeshCall6 call = reinterpret_cast<CuteQQuickShaderEffectMeshCall6>(taken[6]);
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
      CuteQQuickShaderEffectMeshCall7 call = reinterpret_cast<CuteQQuickShaderEffectMeshCall7>(taken[7]);
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
      CuteQQuickShaderEffectMeshCall8 call = reinterpret_cast<CuteQQuickShaderEffectMeshCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickShaderEffectMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickShaderEffectMesh10metaObjectEv(
    const QQuickShaderEffectMesh *self) {
  return self->metaObject();
}

//  void *QQuickShaderEffectMesh::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickShaderEffectMesh11qt_metacastEPKc(
    QQuickShaderEffectMesh *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickShaderEffectMesh::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickShaderEffectMesh11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickShaderEffectMesh *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickShaderEffectMesh::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickShaderEffectMesh2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickShaderEffectMesh::tr(s, c, n));
}

//  void QQuickShaderEffectMesh::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickShaderEffectMesh24qt_qmlMarker_uncreatableEv(
    QQuickShaderEffectMesh *self) {
  self->qt_qmlMarker_uncreatable();
}

//  bool QQuickShaderEffectMesh::validateAttributes(const QList<QByteArray>
//      &attributes, int *posIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickShaderEffectMesh18validateAttributesERK5QListI10QByteArrayEPi(
    QQuickShaderEffectMesh *self,
    const QList<QByteArray> *attributes,
    int *posIndex) {
  return self->validateAttributes(*attributes, posIndex);
}

//  QSGGeometry *QQuickShaderEffectMesh::updateGeometry(QSGGeometry
//      *geometry, int attrCount, int posIndex, const QRectF &srcRect, const
//      QRectF &rect)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_ZN22QQuickShaderEffectMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_(
    QQuickShaderEffectMesh *self,
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

//  QString QQuickShaderEffectMesh::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickShaderEffectMesh3logEv(
    const QQuickShaderEffectMesh *self) {
  return new QString(self->log());
}

//  void QQuickShaderEffectMesh::geometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickShaderEffectMesh15geometryChangedEv(
    QQuickShaderEffectMesh *self) {
  self->geometryChanged();
}

//  a Python function taken by a CuteQQuickShaderEffectMesh, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShaderEffectMesh(
    QQuickShaderEffectMesh *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShaderEffectMesh *>(self)->take(key, call);
}

//  QString QQuickShaderEffectMesh::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK22QQuickShaderEffectMesh3logEv(
    const QQuickShaderEffectMesh *self) {
  return new QString(self->QQuickShaderEffectMesh::log());
}

#endif  // QT_CONFIG(quick_shadereffect)
#endif  // QT_CONFIG(quick_shadereffect)
