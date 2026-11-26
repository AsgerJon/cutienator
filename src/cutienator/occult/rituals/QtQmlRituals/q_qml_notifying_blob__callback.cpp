//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlnotifyingblob_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlnotifyingblob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlNotifyingBlob::Callback that Python can take functions over in. Every QQmlNotifyingBlob::Callback
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlNotifyingBlob_CallbackCall0)(const void *, QQmlNotifyingBlob *, int *);
typedef void (*CuteQQmlNotifyingBlob_CallbackCall1)(const void *, QQmlNotifyingBlob *, qreal, int *);
class CuteQQmlNotifyingBlob_Callback : public QQmlNotifyingBlob::Callback {
public:
  using QQmlNotifyingBlob::Callback::Callback;
  CuteQQmlNotifyingBlob_Callback(const QQmlNotifyingBlob::Callback & other) : QQmlNotifyingBlob::Callback(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQmlNotifyingBlob8Callback5readyEPS_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQmlNotifyingBlob8Callback8progressEPS_d")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQmlNotifyingBlob::Callback::ready(QQmlNotifyingBlob *a0)
  void ready(QQmlNotifyingBlob *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlNotifyingBlob_CallbackCall0 call = reinterpret_cast<CuteQQmlNotifyingBlob_CallbackCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlNotifyingBlob::Callback::ready(a0);
  }

  //  void QQmlNotifyingBlob::Callback::progress(QQmlNotifyingBlob *a0,
  //      qreal a1)
  void progress(QQmlNotifyingBlob *a0, qreal a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlNotifyingBlob_CallbackCall1 call = reinterpret_cast<CuteQQmlNotifyingBlob_CallbackCall1>(taken[1]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlNotifyingBlob::Callback::progress(a0, a1);
  }
};

//  QQmlNotifyingBlob::Callback::~Callback()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlNotifyingBlob8CallbackD1Ev(
    QQmlNotifyingBlob::Callback *self) {
  delete self;
}

//  void QQmlNotifyingBlob::Callback::ready(QQmlNotifyingBlob *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlNotifyingBlob8Callback5readyEPS_(
    QQmlNotifyingBlob::Callback *self,
    QQmlNotifyingBlob *a0) {
  self->ready(a0);
}

//  void QQmlNotifyingBlob::Callback::progress(QQmlNotifyingBlob *a0, qreal
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlNotifyingBlob8Callback8progressEPS_d(
    QQmlNotifyingBlob::Callback *self,
    QQmlNotifyingBlob *a0,
    qreal a1) {
  self->progress(a0, a1);
}

//  a Python function taken by a CuteQQmlNotifyingBlob_Callback, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlNotifyingBlob_Callback(
    QQmlNotifyingBlob::Callback *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlNotifyingBlob_Callback *>(self)->take(key, call);
}

//  void QQmlNotifyingBlob::Callback::ready(QQmlNotifyingBlob *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlNotifyingBlob8Callback5readyEPS_(
    QQmlNotifyingBlob::Callback *self,
    QQmlNotifyingBlob *a0) {
  self->QQmlNotifyingBlob::Callback::ready(a0);
}

//  void QQmlNotifyingBlob::Callback::progress(QQmlNotifyingBlob *a0, qreal
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlNotifyingBlob8Callback8progressEPS_d(
    QQmlNotifyingBlob::Callback *self,
    QQmlNotifyingBlob *a0,
    qreal a1) {
  self->QQmlNotifyingBlob::Callback::progress(a0, a1);
}
