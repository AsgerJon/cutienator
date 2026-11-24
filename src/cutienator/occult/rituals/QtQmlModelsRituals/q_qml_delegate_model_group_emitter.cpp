//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlDelegateModelGroupEmitter that Python can take functions over in. Every QQmlDelegateModelGroupEmitter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelGroupEmitterCall0)(const void *, const QQmlChangeSet *, bool, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelGroupEmitterCall1)(const void *, int, QQuickPackage *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelGroupEmitterCall2)(const void *, int, QQuickPackage *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelGroupEmitterCall3)(const void *, QQuickPackage *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
class CuteQQmlDelegateModelGroupEmitter : public QQmlDelegateModelGroupEmitter {
public:
  using QQmlDelegateModelGroupEmitter::QQmlDelegateModelGroupEmitter;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter16emitModelUpdatedERK13QQmlChangeSetb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter14createdPackageEiP13QQuickPackage")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter11initPackageEiP13QQuickPackage")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter17destroyingPackageEP13QQuickPackage")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
    return false;
  }

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelGroupEmitter::emitModelUpdated(const
  //      QQmlChangeSet &changeSet, bool reset)
  void emitModelUpdated(
      const QQmlChangeSet &changeSet,
      bool reset) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDelegateModelGroupEmitterCall0 call = reinterpret_cast<CuteQQmlDelegateModelGroupEmitterCall0>(taken[0]);
      call(this, &changeSet, reset, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelGroupEmitter::createdPackage(int a0,
  //      QQuickPackage *a1)
  void createdPackage(int a0, QQuickPackage *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDelegateModelGroupEmitterCall1 call = reinterpret_cast<CuteQQmlDelegateModelGroupEmitterCall1>(taken[1]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlDelegateModelGroupEmitter::createdPackage(a0, a1);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelGroupEmitter::initPackage(int a0, QQuickPackage
  //      *a1)
  void initPackage(int a0, QQuickPackage *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDelegateModelGroupEmitterCall2 call = reinterpret_cast<CuteQQmlDelegateModelGroupEmitterCall2>(taken[2]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlDelegateModelGroupEmitter::initPackage(a0, a1);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelGroupEmitter::destroyingPackage(QQuickPackage
  //      *a0)
  void destroyingPackage(QQuickPackage *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDelegateModelGroupEmitterCall3 call = reinterpret_cast<CuteQQmlDelegateModelGroupEmitterCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDelegateModelGroupEmitter::destroyingPackage(a0);
  }
#endif  // QT_CONFIG(qml_delegate_model)
};

//  QQmlDelegateModelGroupEmitter::~QQmlDelegateModelGroupEmitter()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelGroupEmitterD1Ev(
    QQmlDelegateModelGroupEmitter *self) {
  delete self;
}

//  void QQmlDelegateModelGroupEmitter::emitModelUpdated(const QQmlChangeSet
//      &changeSet, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelGroupEmitter16emitModelUpdatedERK13QQmlChangeSetb(
    QQmlDelegateModelGroupEmitter *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->emitModelUpdated(*changeSet, reset);
}

//  void QQmlDelegateModelGroupEmitter::createdPackage(int a0, QQuickPackage
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelGroupEmitter14createdPackageEiP13QQuickPackage(
    QQmlDelegateModelGroupEmitter *self,
    int a0,
    QQuickPackage *a1) {
  self->createdPackage(a0, a1);
}

//  void QQmlDelegateModelGroupEmitter::initPackage(int a0, QQuickPackage
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelGroupEmitter11initPackageEiP13QQuickPackage(
    QQmlDelegateModelGroupEmitter *self,
    int a0,
    QQuickPackage *a1) {
  self->initPackage(a0, a1);
}

//  void QQmlDelegateModelGroupEmitter::destroyingPackage(QQuickPackage *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelGroupEmitter17destroyingPackageEP13QQuickPackage(
    QQmlDelegateModelGroupEmitter *self,
    QQuickPackage *a0) {
  self->destroyingPackage(a0);
}

//  a Python function taken by a CuteQQmlDelegateModelGroupEmitter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDelegateModelGroupEmitter(
    QQmlDelegateModelGroupEmitter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDelegateModelGroupEmitter *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
