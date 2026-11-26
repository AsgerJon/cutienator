//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGGuiThreadShaderEffectManager that Python can take functions over in. Every QSGGuiThreadShaderEffectManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGGuiThreadShaderEffectManagerCall0)(const void *, int *);
typedef QString * (*CuteQSGGuiThreadShaderEffectManagerCall1)(const void *, int *);
typedef int (*CuteQSGGuiThreadShaderEffectManagerCall2)(const void *, int *);
typedef void (*CuteQSGGuiThreadShaderEffectManagerCall3)(const void *, int, const QUrl *, QSGGuiThreadShaderEffectManager::ShaderInfo *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGGuiThreadShaderEffectManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGGuiThreadShaderEffectManagerCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGGuiThreadShaderEffectManagerCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGGuiThreadShaderEffectManagerCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGGuiThreadShaderEffectManagerCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGGuiThreadShaderEffectManagerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGGuiThreadShaderEffectManagerCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGGuiThreadShaderEffectManager : public QSGGuiThreadShaderEffectManager {
public:
  using QSGGuiThreadShaderEffectManager::QSGGuiThreadShaderEffectManager;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK31QSGGuiThreadShaderEffectManager35hasSeparateSamplerAndTextureObjectsEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QSGGuiThreadShaderEffectManager3logEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QSGGuiThreadShaderEffectManager6statusEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QSGGuiThreadShaderEffectManager17prepareShaderCodeENS_10ShaderInfo4TypeERK4QUrlPS0_")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QSGGuiThreadShaderEffectManager::hasSeparateSamplerAndTextureObj
  //      ects() const
  bool hasSeparateSamplerAndTextureObjects() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall0 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QSGGuiThreadShaderEffectManager::log() const
  QString log() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall1 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  Status QSGGuiThreadShaderEffectManager::status() const
  QSGGuiThreadShaderEffectManager::Status status() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall2 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGGuiThreadShaderEffectManager::Status>(given);
    }
    return {};
  }

  //  void
  //      QSGGuiThreadShaderEffectManager::prepareShaderCode(ShaderInfo::Ty
  //      pe typeHint, const QUrl &src, ShaderInfo *result)
  void prepareShaderCode(
      QSGGuiThreadShaderEffectManager::ShaderInfo::Type typeHint,
      const QUrl &src,
      QSGGuiThreadShaderEffectManager::ShaderInfo *result) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall3 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall3>(taken[3]);
      call(this, static_cast<int>(typeHint), &src, result, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall4 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall5 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall6 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall7 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall8 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall9 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGGuiThreadShaderEffectManagerCall10 call = reinterpret_cast<CuteQSGGuiThreadShaderEffectManagerCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGGuiThreadShaderEffectManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QSGGuiThreadShaderEffectManager10metaObjectEv(
    const QSGGuiThreadShaderEffectManager *self) {
  return self->metaObject();
}

//  void *QSGGuiThreadShaderEffectManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QSGGuiThreadShaderEffectManager11qt_metacastEPKc(
    QSGGuiThreadShaderEffectManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGGuiThreadShaderEffectManager::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QSGGuiThreadShaderEffectManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGGuiThreadShaderEffectManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGGuiThreadShaderEffectManager::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QSGGuiThreadShaderEffectManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGGuiThreadShaderEffectManager::tr(s, c, n));
}

//  QSGGuiThreadShaderEffectManager::~QSGGuiThreadShaderEffectManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSGGuiThreadShaderEffectManagerD1Ev(
    QSGGuiThreadShaderEffectManager *self) {
  delete self;
}

//  bool
//      QSGGuiThreadShaderEffectManager::hasSeparateSamplerAndTextureObjects(
//      ) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QSGGuiThreadShaderEffectManager35hasSeparateSamplerAndTextureObjectsEv(
    const QSGGuiThreadShaderEffectManager *self) {
  return self->hasSeparateSamplerAndTextureObjects();
}

//  QString QSGGuiThreadShaderEffectManager::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QSGGuiThreadShaderEffectManager3logEv(
    const QSGGuiThreadShaderEffectManager *self) {
  return new QString(self->log());
}

//  Status QSGGuiThreadShaderEffectManager::status() const
extern "C" Q_DECL_EXPORT
QSGGuiThreadShaderEffectManager::Status ritual_ZNK31QSGGuiThreadShaderEffectManager6statusEv(
    const QSGGuiThreadShaderEffectManager *self) {
  return self->status();
}

//  void QSGGuiThreadShaderEffectManager::prepareShaderCode(ShaderInfo::Type
//      typeHint, const QUrl &src, ShaderInfo *result)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSGGuiThreadShaderEffectManager17prepareShaderCodeENS_10ShaderInfo4TypeERK4QUrlPS0_(
    QSGGuiThreadShaderEffectManager *self,
    QSGGuiThreadShaderEffectManager::ShaderInfo::Type typeHint,
    const QUrl *src,
    QSGGuiThreadShaderEffectManager::ShaderInfo *result) {
  self->prepareShaderCode(typeHint, *src, result);
}

//  void QSGGuiThreadShaderEffectManager::shaderCodePrepared(bool ok,
//      ShaderInfo::Type typeHint, const QUrl &src, ShaderInfo *result)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSGGuiThreadShaderEffectManager18shaderCodePreparedEbNS_10ShaderInfo4TypeERK4QUrlPS0_(
    QSGGuiThreadShaderEffectManager *self,
    bool ok,
    QSGGuiThreadShaderEffectManager::ShaderInfo::Type typeHint,
    const QUrl *src,
    QSGGuiThreadShaderEffectManager::ShaderInfo *result) {
  self->shaderCodePrepared(ok, typeHint, *src, result);
}

//  void QSGGuiThreadShaderEffectManager::logAndStatusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSGGuiThreadShaderEffectManager19logAndStatusChangedEv(
    QSGGuiThreadShaderEffectManager *self) {
  self->logAndStatusChanged();
}

//  a Python function taken by a CuteQSGGuiThreadShaderEffectManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGGuiThreadShaderEffectManager(
    QSGGuiThreadShaderEffectManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGGuiThreadShaderEffectManager *>(self)->take(key, call);
}
