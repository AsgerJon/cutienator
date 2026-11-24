//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkinformation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkinformation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNetworkInformationBackendFactory that Python can take functions over in. Every QNetworkInformationBackendFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQNetworkInformationBackendFactoryCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkInformationBackendFactoryCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkInformationBackendFactoryCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendFactoryCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendFactoryCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendFactoryCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendFactoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkInformationBackendFactory : public QNetworkInformationBackendFactory {
public:
  using QNetworkInformationBackendFactory::QNetworkInformationBackendFactory;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK33QNetworkInformationBackendFactory4nameEv")) {
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

  //  QString QNetworkInformationBackendFactory::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkInformationBackendFactoryCall0 call = reinterpret_cast<CuteQNetworkInformationBackendFactoryCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkInformationBackendFactoryCall1 call = reinterpret_cast<CuteQNetworkInformationBackendFactoryCall1>(taken[1]);
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
      CuteQNetworkInformationBackendFactoryCall2 call = reinterpret_cast<CuteQNetworkInformationBackendFactoryCall2>(taken[2]);
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
      CuteQNetworkInformationBackendFactoryCall3 call = reinterpret_cast<CuteQNetworkInformationBackendFactoryCall3>(taken[3]);
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
      CuteQNetworkInformationBackendFactoryCall4 call = reinterpret_cast<CuteQNetworkInformationBackendFactoryCall4>(taken[4]);
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
      CuteQNetworkInformationBackendFactoryCall5 call = reinterpret_cast<CuteQNetworkInformationBackendFactoryCall5>(taken[5]);
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
      CuteQNetworkInformationBackendFactoryCall6 call = reinterpret_cast<CuteQNetworkInformationBackendFactoryCall6>(taken[6]);
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
      CuteQNetworkInformationBackendFactoryCall7 call = reinterpret_cast<CuteQNetworkInformationBackendFactoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkInformationBackendFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QNetworkInformationBackendFactory10metaObjectEv(
    const QNetworkInformationBackendFactory *self) {
  return self->metaObject();
}

//  QString QNetworkInformationBackendFactory::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QNetworkInformationBackendFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkInformationBackendFactory::tr(s, c, n));
}

//  QNetworkInformationBackendFactory::~QNetworkInformationBackendFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QNetworkInformationBackendFactoryD1Ev(
    QNetworkInformationBackendFactory *self) {
  delete self;
}

//  QString QNetworkInformationBackendFactory::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK33QNetworkInformationBackendFactory4nameEv(
    const QNetworkInformationBackendFactory *self) {
  return new QString(self->name());
}

//  QNetworkInformationBackend
//      *QNetworkInformationBackendFactory::create(Features requiredFeatures)
//      const
extern "C" Q_DECL_EXPORT
QNetworkInformationBackend *ritual_ZNK33QNetworkInformationBackendFactory6createE6QFlagsIN19QNetworkInformation7FeatureEE(
    const QNetworkInformationBackendFactory *self,
    int requiredFeatures) {
  return self->create(
      QFlags<QNetworkInformation::Feature>::fromInt(requiredFeatures));
}

//  Features QNetworkInformationBackendFactory::featuresSupported() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QNetworkInformationBackendFactory17featuresSupportedEv(
    const QNetworkInformationBackendFactory *self) {
  return static_cast<int>(self->featuresSupported().toInt());
}

//  a Python function taken by a CuteQNetworkInformationBackendFactory, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkInformationBackendFactory(
    QNetworkInformationBackendFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkInformationBackendFactory *>(self)->take(key, call);
}
