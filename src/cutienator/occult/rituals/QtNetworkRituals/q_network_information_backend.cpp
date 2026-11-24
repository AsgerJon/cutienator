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

//  A QNetworkInformationBackend that Python can take functions over in. Every QNetworkInformationBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQNetworkInformationBackendCall0)(const void *, int *);
typedef int (*CuteQNetworkInformationBackendCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkInformationBackendCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkInformationBackendCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkInformationBackendCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkInformationBackend : public QNetworkInformationBackend {
public:
  using QNetworkInformationBackend::QNetworkInformationBackend;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK26QNetworkInformationBackend4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QNetworkInformationBackend17featuresSupportedEv")) {
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

  //  QString QNetworkInformationBackend::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkInformationBackendCall0 call = reinterpret_cast<CuteQNetworkInformationBackendCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QNetworkInformation::Features
  //      QNetworkInformationBackend::featuresSupported() const
  QNetworkInformation::Features featuresSupported() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkInformationBackendCall1 call = reinterpret_cast<CuteQNetworkInformationBackendCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return QFlags<QNetworkInformation::Feature>::fromInt(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkInformationBackendCall2 call = reinterpret_cast<CuteQNetworkInformationBackendCall2>(taken[2]);
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
      CuteQNetworkInformationBackendCall3 call = reinterpret_cast<CuteQNetworkInformationBackendCall3>(taken[3]);
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
      CuteQNetworkInformationBackendCall4 call = reinterpret_cast<CuteQNetworkInformationBackendCall4>(taken[4]);
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
      CuteQNetworkInformationBackendCall5 call = reinterpret_cast<CuteQNetworkInformationBackendCall5>(taken[5]);
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
      CuteQNetworkInformationBackendCall6 call = reinterpret_cast<CuteQNetworkInformationBackendCall6>(taken[6]);
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
      CuteQNetworkInformationBackendCall7 call = reinterpret_cast<CuteQNetworkInformationBackendCall7>(taken[7]);
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
      CuteQNetworkInformationBackendCall8 call = reinterpret_cast<CuteQNetworkInformationBackendCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkInformationBackend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QNetworkInformationBackend10metaObjectEv(
    const QNetworkInformationBackend *self) {
  return self->metaObject();
}

//  QString QNetworkInformationBackend::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QNetworkInformationBackend2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkInformationBackend::tr(s, c, n));
}

//  QNetworkInformationBackend::~QNetworkInformationBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNetworkInformationBackendD1Ev(
    QNetworkInformationBackend *self) {
  delete self;
}

//  QString QNetworkInformationBackend::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QNetworkInformationBackend4nameEv(
    const QNetworkInformationBackend *self) {
  return new QString(self->name());
}

//  QNetworkInformation::Features
//      QNetworkInformationBackend::featuresSupported() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QNetworkInformationBackend17featuresSupportedEv(
    const QNetworkInformationBackend *self) {
  return static_cast<int>(self->featuresSupported().toInt());
}

//  Reachability QNetworkInformationBackend::reachability() const
extern "C" Q_DECL_EXPORT
QNetworkInformationBackend::Reachability ritual_ZNK26QNetworkInformationBackend12reachabilityEv(
    const QNetworkInformationBackend *self) {
  return self->reachability();
}

//  bool QNetworkInformationBackend::behindCaptivePortal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QNetworkInformationBackend19behindCaptivePortalEv(
    const QNetworkInformationBackend *self) {
  return self->behindCaptivePortal();
}

//  TransportMedium QNetworkInformationBackend::transportMedium() const
extern "C" Q_DECL_EXPORT
QNetworkInformationBackend::TransportMedium ritual_ZNK26QNetworkInformationBackend15transportMediumEv(
    const QNetworkInformationBackend *self) {
  return self->transportMedium();
}

//  bool QNetworkInformationBackend::isMetered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QNetworkInformationBackend9isMeteredEv(
    const QNetworkInformationBackend *self) {
  return self->isMetered();
}

//  void QNetworkInformationBackend::setReachability(QNetworkInformation::Rea
//      chability reachability)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNetworkInformationBackend15setReachabilityEN19QNetworkInformation12ReachabilityE(
    QNetworkInformationBackend *self,
    QNetworkInformation::Reachability reachability) {
  self->setReachability(reachability);
}

//  void QNetworkInformationBackend::setBehindCaptivePortal(bool
//      behindPortal)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNetworkInformationBackend22setBehindCaptivePortalEb(
    QNetworkInformationBackend *self,
    bool behindPortal) {
  self->setBehindCaptivePortal(behindPortal);
}

//  void QNetworkInformationBackend::setTransportMedium(TransportMedium
//      medium)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNetworkInformationBackend18setTransportMediumEN19QNetworkInformation15TransportMediumE(
    QNetworkInformationBackend *self,
    QNetworkInformationBackend::TransportMedium medium) {
  self->setTransportMedium(medium);
}

//  void QNetworkInformationBackend::setMetered(bool isMetered)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNetworkInformationBackend10setMeteredEb(
    QNetworkInformationBackend *self,
    bool isMetered) {
  self->setMetered(isMetered);
}

//  a Python function taken by a CuteQNetworkInformationBackend, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkInformationBackend(
    QNetworkInformationBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkInformationBackend *>(self)->take(key, call);
}
