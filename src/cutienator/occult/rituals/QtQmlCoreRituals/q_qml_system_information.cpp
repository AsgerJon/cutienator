//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCore/6.12.0/QtQmlCore/private/qqmlsysteminformation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlcoreglobal_p.h>
#include <QtQmlCore/QtQmlCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlsysteminformation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlSystemInformation that Python can take functions over in. Every QQmlSystemInformation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSystemInformationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSystemInformationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSystemInformationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSystemInformationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSystemInformationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSystemInformationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSystemInformationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlSystemInformation : public QQmlSystemInformation {
public:
  using QQmlSystemInformation::QQmlSystemInformation;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSystemInformationCall0 call = reinterpret_cast<CuteQQmlSystemInformationCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlSystemInformationCall1 call = reinterpret_cast<CuteQQmlSystemInformationCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlSystemInformationCall2 call = reinterpret_cast<CuteQQmlSystemInformationCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlSystemInformationCall3 call = reinterpret_cast<CuteQQmlSystemInformationCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlSystemInformationCall4 call = reinterpret_cast<CuteQQmlSystemInformationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlSystemInformationCall5 call = reinterpret_cast<CuteQQmlSystemInformationCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlSystemInformationCall6 call = reinterpret_cast<CuteQQmlSystemInformationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlSystemInformation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQmlSystemInformation10metaObjectEv(
    const QQmlSystemInformation *self) {
  return self->metaObject();
}

//  QString QQmlSystemInformation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQmlSystemInformation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlSystemInformation::tr(s, c, n));
}

//  void QQmlSystemInformation::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlSystemInformation22qt_qmlMarker_singletonEv(
    QQmlSystemInformation *self) {
  self->qt_qmlMarker_singleton();
}

//  QQmlSystemInformation::QQmlSystemInformation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlSystemInformation *ritual_ZN21QQmlSystemInformationC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlSystemInformation(parent);
}

//  int QQmlSystemInformation::wordSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQmlSystemInformation8wordSizeEv(
    const QQmlSystemInformation *self) {
  return self->wordSize();
}

//  Endian QQmlSystemInformation::byteOrder() const
extern "C" Q_DECL_EXPORT
QQmlSystemInformation::Endian ritual_ZNK21QQmlSystemInformation9byteOrderEv(
    const QQmlSystemInformation *self) {
  return self->byteOrder();
}

//  QString QQmlSystemInformation::buildCpuArchitecture() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlSystemInformation20buildCpuArchitectureEv(
    const QQmlSystemInformation *self) {
  return new QString(self->buildCpuArchitecture());
}

//  QString QQmlSystemInformation::currentCpuArchitecture() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlSystemInformation22currentCpuArchitectureEv(
    const QQmlSystemInformation *self) {
  return new QString(self->currentCpuArchitecture());
}

//  QString QQmlSystemInformation::buildAbi() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlSystemInformation8buildAbiEv(
    const QQmlSystemInformation *self) {
  return new QString(self->buildAbi());
}

//  QString QQmlSystemInformation::kernelType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlSystemInformation10kernelTypeEv(
    const QQmlSystemInformation *self) {
  return new QString(self->kernelType());
}

//  QString QQmlSystemInformation::kernelVersion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlSystemInformation13kernelVersionEv(
    const QQmlSystemInformation *self) {
  return new QString(self->kernelVersion());
}

//  QString QQmlSystemInformation::productType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlSystemInformation11productTypeEv(
    const QQmlSystemInformation *self) {
  return new QString(self->productType());
}

//  QString QQmlSystemInformation::productVersion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlSystemInformation14productVersionEv(
    const QQmlSystemInformation *self) {
  return new QString(self->productVersion());
}

//  QString QQmlSystemInformation::prettyProductName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlSystemInformation17prettyProductNameEv(
    const QQmlSystemInformation *self) {
  return new QString(self->prettyProductName());
}

//  QString QQmlSystemInformation::machineHostName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlSystemInformation15machineHostNameEv(
    const QQmlSystemInformation *self) {
  return new QString(self->machineHostName());
}

//  QByteArray QQmlSystemInformation::machineUniqueId() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK21QQmlSystemInformation15machineUniqueIdEv(
    const QQmlSystemInformation *self) {
  return new QByteArray(self->machineUniqueId());
}

//  QByteArray QQmlSystemInformation::bootUniqueId() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK21QQmlSystemInformation12bootUniqueIdEv(
    const QQmlSystemInformation *self) {
  return new QByteArray(self->bootUniqueId());
}

//  a Python function taken by a CuteQQmlSystemInformation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSystemInformation(
    QQmlSystemInformation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSystemInformation *>(self)->take(key, call);
}
