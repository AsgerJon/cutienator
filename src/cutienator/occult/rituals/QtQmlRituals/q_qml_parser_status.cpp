//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlparserstatus.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlparserstatus.h>
#include <cstring>

//  A QQmlParserStatus that Python can take functions over in. Every QQmlParserStatus
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlParserStatusCall0)(const void *, int *);
typedef void (*CuteQQmlParserStatusCall1)(const void *, int *);
class CuteQQmlParserStatus : public QQmlParserStatus {
public:
  using QQmlParserStatus::QQmlParserStatus;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQmlParserStatus::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlParserStatusCall0 call = reinterpret_cast<CuteQQmlParserStatusCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQmlParserStatus::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlParserStatusCall1 call = reinterpret_cast<CuteQQmlParserStatusCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QQmlParserStatus::QQmlParserStatus()
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_ZN16QQmlParserStatusC1Ev() {
  return new CuteQQmlParserStatus();
}

//  QQmlParserStatus::~QQmlParserStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlParserStatusD1Ev(QQmlParserStatus *self) {
  delete self;
}

//  void QQmlParserStatus::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlParserStatus10classBeginEv(QQmlParserStatus *self) {
  self->classBegin();
}

//  void QQmlParserStatus::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlParserStatus17componentCompleteEv(
    QQmlParserStatus *self) {
  self->componentComplete();
}

//  a Python function taken by a CuteQQmlParserStatus, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlParserStatus(
    QQmlParserStatus *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlParserStatus *>(self)->take(key, call);
}
