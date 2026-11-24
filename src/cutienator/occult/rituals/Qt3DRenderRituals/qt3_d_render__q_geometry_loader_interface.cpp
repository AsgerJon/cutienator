//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qgeometryloaderinterface_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qgeometryloaderinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QGeometryLoaderInterface that Python can take functions over in. Every Qt3DRender::QGeometryLoaderInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQt3DRender_QGeometryLoaderInterfaceCall0)(const void *, int *);
typedef bool (*CuteQt3DRender_QGeometryLoaderInterfaceCall1)(const void *, QIODevice *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QGeometryLoaderInterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QGeometryLoaderInterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderInterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderInterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderInterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderInterfaceCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderInterfaceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QGeometryLoaderInterface : public Qt3DRender::QGeometryLoaderInterface {
public:
  using Qt3DRender::QGeometryLoaderInterface::QGeometryLoaderInterface;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10Qt3DRender24QGeometryLoaderInterface8geometryEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender24QGeometryLoaderInterface4loadEP9QIODeviceRK7QString")) {
      taken[1] = call;
      return true;
    }
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

  //  Qt3DCore::QGeometry *Qt3DRender::QGeometryLoaderInterface::geometry()
  //      const
  Qt3DCore::QGeometry *geometry() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderInterfaceCall0 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderInterfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt3DCore::QGeometry *>(given);
    }
    return {};
  }

  //  bool Qt3DRender::QGeometryLoaderInterface::load(QIODevice *ioDev,
  //      const QString &subMesh)
  bool load(QIODevice *ioDev, const QString &subMesh) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderInterfaceCall1 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderInterfaceCall1>(taken[1]);
      bool given = call(this, ioDev, &subMesh, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderInterfaceCall2 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderInterfaceCall2>(taken[2]);
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
      CuteQt3DRender_QGeometryLoaderInterfaceCall3 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderInterfaceCall3>(taken[3]);
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
      CuteQt3DRender_QGeometryLoaderInterfaceCall4 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderInterfaceCall4>(taken[4]);
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
      CuteQt3DRender_QGeometryLoaderInterfaceCall5 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderInterfaceCall5>(taken[5]);
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
      CuteQt3DRender_QGeometryLoaderInterfaceCall6 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderInterfaceCall6>(taken[6]);
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
      CuteQt3DRender_QGeometryLoaderInterfaceCall7 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderInterfaceCall7>(taken[7]);
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
      CuteQt3DRender_QGeometryLoaderInterfaceCall8 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderInterfaceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  Qt3DCore::QGeometry *Qt3DRender::QGeometryLoaderInterface::geometry()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometry *ritual_ZNK10Qt3DRender24QGeometryLoaderInterface8geometryEv(
    const Qt3DRender::QGeometryLoaderInterface *self) {
  return self->geometry();
}

//  bool Qt3DRender::QGeometryLoaderInterface::load(QIODevice *ioDev, const
//      QString &subMesh)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender24QGeometryLoaderInterface4loadEP9QIODeviceRK7QString(
    Qt3DRender::QGeometryLoaderInterface *self,
    QIODevice *ioDev,
    const QString *subMesh) {
  return self->load(ioDev, *subMesh);
}

//  a Python function taken by a CuteQt3DRender_QGeometryLoaderInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QGeometryLoaderInterface(
    Qt3DRender::QGeometryLoaderInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QGeometryLoaderInterface *>(self)->take(key, call);
}
