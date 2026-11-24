//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>
#include <cstring>

//  A QQmlPrivate::AOTTrackedLocalsStorage that Python can take functions over in. Every QQmlPrivate::AOTTrackedLocalsStorage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlPrivate_AOTTrackedLocalsStorageCall0)(const void *, QV4::MarkStack *, int *);
class CuteQQmlPrivate_AOTTrackedLocalsStorage : public QQmlPrivate::AOTTrackedLocalsStorage {
public:
  using QQmlPrivate::AOTTrackedLocalsStorage::AOTTrackedLocalsStorage;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QQmlPrivate23AOTTrackedLocalsStorage11markObjectsEPN3QV49MarkStackE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQmlPrivate::AOTTrackedLocalsStorage::markObjects(QV4::MarkStack
  //      *markStack) const
  void markObjects(QV4::MarkStack *markStack) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlPrivate_AOTTrackedLocalsStorageCall0 call = reinterpret_cast<CuteQQmlPrivate_AOTTrackedLocalsStorageCall0>(taken[0]);
      call(this, markStack, &handled);
      if (handled) return;
    }
  }
};

//  QQmlPrivate::AOTTrackedLocalsStorage::~AOTTrackedLocalsStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate23AOTTrackedLocalsStorageD1Ev(
    QQmlPrivate::AOTTrackedLocalsStorage *self) {
  delete self;
}

//  void QQmlPrivate::AOTTrackedLocalsStorage::markObjects(QV4::MarkStack
//      *markStack) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate23AOTTrackedLocalsStorage11markObjectsEPN3QV49MarkStackE(
    const QQmlPrivate::AOTTrackedLocalsStorage *self,
    QV4::MarkStack *markStack) {
  self->markObjects(markStack);
}

//  a Python function taken by a CuteQQmlPrivate_AOTTrackedLocalsStorage, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlPrivate_AOTTrackedLocalsStorage(
    QQmlPrivate::AOTTrackedLocalsStorage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlPrivate_AOTTrackedLocalsStorage *>(self)->take(key, call);
}
