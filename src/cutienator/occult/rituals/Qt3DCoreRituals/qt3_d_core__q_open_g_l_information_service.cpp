//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qopenglinformationservice_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qopenglinformationservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QOpenGLInformationService that Python can take functions over in. Every Qt3DCore::QOpenGLInformationService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSurfaceFormat * (*CuteQt3DCore_QOpenGLInformationServiceCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QOpenGLInformationServiceCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QOpenGLInformationServiceCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QOpenGLInformationServiceCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QOpenGLInformationServiceCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QOpenGLInformationServiceCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QOpenGLInformationServiceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QOpenGLInformationServiceCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QOpenGLInformationService : public Qt3DCore::QOpenGLInformationService {
public:
  using Qt3DCore::QOpenGLInformationService::QOpenGLInformationService;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore25QOpenGLInformationService6formatEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSurfaceFormat Qt3DCore::QOpenGLInformationService::format() const
  QSurfaceFormat format() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QOpenGLInformationServiceCall0 call = reinterpret_cast<CuteQt3DCore_QOpenGLInformationServiceCall0>(taken[0]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QOpenGLInformationServiceCall1 call = reinterpret_cast<CuteQt3DCore_QOpenGLInformationServiceCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QOpenGLInformationServiceCall2 call = reinterpret_cast<CuteQt3DCore_QOpenGLInformationServiceCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QOpenGLInformationServiceCall3 call = reinterpret_cast<CuteQt3DCore_QOpenGLInformationServiceCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_QOpenGLInformationServiceCall4 call = reinterpret_cast<CuteQt3DCore_QOpenGLInformationServiceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_QOpenGLInformationServiceCall5 call = reinterpret_cast<CuteQt3DCore_QOpenGLInformationServiceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_QOpenGLInformationServiceCall6 call = reinterpret_cast<CuteQt3DCore_QOpenGLInformationServiceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DCore_QOpenGLInformationServiceCall7 call = reinterpret_cast<CuteQt3DCore_QOpenGLInformationServiceCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QOpenGLInformationService::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore25QOpenGLInformationService10metaObjectEv(
    const Qt3DCore::QOpenGLInformationService *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QOpenGLInformationService::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore25QOpenGLInformationService11qt_metacastEPKc(
    Qt3DCore::QOpenGLInformationService *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QOpenGLInformationService::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore25QOpenGLInformationService11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QOpenGLInformationService *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QOpenGLInformationService::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore25QOpenGLInformationService2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QOpenGLInformationService::tr(s, c, n));
}

//  QSurfaceFormat Qt3DCore::QOpenGLInformationService::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK8Qt3DCore25QOpenGLInformationService6formatEv(
    const Qt3DCore::QOpenGLInformationService *self) {
  return new QSurfaceFormat(self->format());
}

//  Qt3DCore::QOpenGLInformationService::QOpenGLInformationService(const
//      QString &description)
extern "C" Q_DECL_EXPORT
Qt3DCore::QOpenGLInformationService *ritual_ZN8Qt3DCore25QOpenGLInformationServiceC1ERK7QString(
    const QString *description) {
  return new CuteQt3DCore_QOpenGLInformationService(*description);
}

//  Qt3DCore::QOpenGLInformationService::QOpenGLInformationService(QOpenGLInf
//      ormationServicePrivate &dd)
extern "C" Q_DECL_EXPORT
Qt3DCore::QOpenGLInformationService *ritual_ZN8Qt3DCore25QOpenGLInformationServiceC1ERNS_32QOpenGLInformationServicePrivateE(
    Qt3DCore::QOpenGLInformationServicePrivate *dd) {
  return new CuteQt3DCore_QOpenGLInformationService(*dd);
}

//  a Python function taken by a CuteQt3DCore_QOpenGLInformationService, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QOpenGLInformationService(
    Qt3DCore::QOpenGLInformationService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QOpenGLInformationService *>(self)->take(key, call);
}
