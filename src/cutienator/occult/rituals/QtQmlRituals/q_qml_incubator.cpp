//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlincubator.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlincubator.h>
#include <QtQml/qqmlerror.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QQmlIncubator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlIncubator : QQmlIncubator {
  using QQmlIncubator::statusChanged;
  using QQmlIncubator::setInitialState;
};

//  A QQmlIncubator that Python can take functions over in. Every QQmlIncubator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlIncubatorCall0)(const void *, int, int *);
typedef void (*CuteQQmlIncubatorCall1)(const void *, QObject *, int *);
class CuteQQmlIncubator : public QQmlIncubator {
public:
  using QQmlIncubator::QQmlIncubator;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QQmlIncubator13statusChangedENS_6StatusE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQmlIncubator15setInitialStateEP7QObject")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQmlIncubator::statusChanged(Status a0)
  void statusChanged(QQmlIncubator::Status a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlIncubatorCall0 call = reinterpret_cast<CuteQQmlIncubatorCall0>(taken[0]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlIncubator::statusChanged(a0);
  }

  //  void QQmlIncubator::setInitialState(QObject *a0)
  void setInitialState(QObject *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlIncubatorCall1 call = reinterpret_cast<CuteQQmlIncubatorCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlIncubator::setInitialState(a0);
  }
};

//  QQmlIncubator::QQmlIncubator(IncubationMode a0)
extern "C" Q_DECL_EXPORT
QQmlIncubator *ritual_ZN13QQmlIncubatorC1ENS_14IncubationModeE(
    QQmlIncubator::IncubationMode a0) {
  return new CuteQQmlIncubator(a0);
}

//  QQmlIncubator::~QQmlIncubator()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlIncubatorD1Ev(QQmlIncubator *self) {
  delete self;
}

//  void QQmlIncubator::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlIncubator5clearEv(QQmlIncubator *self) {
  self->clear();
}

//  void QQmlIncubator::forceCompletion()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlIncubator15forceCompletionEv(QQmlIncubator *self) {
  self->forceCompletion();
}

//  bool QQmlIncubator::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlIncubator6isNullEv(const QQmlIncubator *self) {
  return self->isNull();
}

//  bool QQmlIncubator::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlIncubator7isReadyEv(const QQmlIncubator *self) {
  return self->isReady();
}

//  bool QQmlIncubator::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlIncubator7isErrorEv(const QQmlIncubator *self) {
  return self->isError();
}

//  bool QQmlIncubator::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlIncubator9isLoadingEv(const QQmlIncubator *self) {
  return self->isLoading();
}

//  QList<QQmlError> QQmlIncubator::errors() const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK13QQmlIncubator6errorsEv(
    const QQmlIncubator *self) {
  return new QList<QQmlError>(self->errors());
}

//  IncubationMode QQmlIncubator::incubationMode() const
extern "C" Q_DECL_EXPORT
QQmlIncubator::IncubationMode ritual_ZNK13QQmlIncubator14incubationModeEv(
    const QQmlIncubator *self) {
  return self->incubationMode();
}

//  Status QQmlIncubator::status() const
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_ZNK13QQmlIncubator6statusEv(
    const QQmlIncubator *self) {
  return self->status();
}

//  QObject *QQmlIncubator::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QQmlIncubator6objectEv(const QQmlIncubator *self) {
  return self->object();
}

//  void QQmlIncubator::setInitialProperties(const QVariantMap
//      &initialProperties)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlIncubator20setInitialPropertiesERK4QMapI7QString8QVariantE(
    QQmlIncubator *self,
    const QMap<QString, QVariant> *initialProperties) {
  self->setInitialProperties(*initialProperties);
}

//  void QQmlIncubator::statusChanged(Status a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlIncubator13statusChangedENS_6StatusE(
    QQmlIncubator *self,
    QQmlIncubator::Status a0) {
  self->statusChanged(a0);
}

//  void QQmlIncubator::setInitialState(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlIncubator15setInitialStateEP7QObject(
    QQmlIncubator *self,
    QObject *a0) {
  self->setInitialState(a0);
}

//  a Python function taken by a CuteQQmlIncubator, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlIncubator(
    QQmlIncubator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlIncubator *>(self)->take(key, call);
}

//  void QQmlIncubator::statusChanged(Status a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQmlIncubator13statusChangedENS_6StatusE(
    QQmlIncubator *self,
    QQmlIncubator::Status a0) {
  static_cast<OwnQQmlIncubator *>(self)->OwnQQmlIncubator::statusChanged(a0);
}

//  void QQmlIncubator::setInitialState(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQmlIncubator15setInitialStateEP7QObject(
    QQmlIncubator *self,
    QObject *a0) {
  static_cast<OwnQQmlIncubator *>(self)->OwnQQmlIncubator::setInitialState(
      a0);
}
