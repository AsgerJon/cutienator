//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qrestaccessmanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(http)
#include <QtNetwork/qrestaccessmanager.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QRestAccessManager that Python can take functions over in. Every QRestAccessManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRestAccessManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRestAccessManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRestAccessManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRestAccessManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRestAccessManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRestAccessManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRestAccessManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRestAccessManager : public QRestAccessManager {
public:
  using QRestAccessManager::QRestAccessManager;
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
      CuteQRestAccessManagerCall0 call = reinterpret_cast<CuteQRestAccessManagerCall0>(taken[0]);
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
      CuteQRestAccessManagerCall1 call = reinterpret_cast<CuteQRestAccessManagerCall1>(taken[1]);
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
      CuteQRestAccessManagerCall2 call = reinterpret_cast<CuteQRestAccessManagerCall2>(taken[2]);
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
      CuteQRestAccessManagerCall3 call = reinterpret_cast<CuteQRestAccessManagerCall3>(taken[3]);
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
      CuteQRestAccessManagerCall4 call = reinterpret_cast<CuteQRestAccessManagerCall4>(taken[4]);
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
      CuteQRestAccessManagerCall5 call = reinterpret_cast<CuteQRestAccessManagerCall5>(taken[5]);
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
      CuteQRestAccessManagerCall6 call = reinterpret_cast<CuteQRestAccessManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRestAccessManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QRestAccessManager10metaObjectEv(
    const QRestAccessManager *self) {
  return self->metaObject();
}

//  QString QRestAccessManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QRestAccessManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRestAccessManager::tr(s, c, n));
}

//  QRestAccessManager::QRestAccessManager(QNetworkAccessManager *manager,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QRestAccessManager *ritual_ZN18QRestAccessManagerC1EP21QNetworkAccessManagerP7QObject(
    QNetworkAccessManager *manager,
    QObject *parent) {
  return new CuteQRestAccessManager(manager, parent);
}

//  QRestAccessManager::~QRestAccessManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRestAccessManagerD1Ev(QRestAccessManager *self) {
  delete self;
}

//  QNetworkAccessManager *QRestAccessManager::networkAccessManager() const
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZNK18QRestAccessManager20networkAccessManagerEv(
    const QRestAccessManager *self) {
  return self->networkAccessManager();
}

//  QNetworkReply *QRestAccessManager::deleteResource(const QNetworkRequest
//      &request)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager14deleteResourceERK15QNetworkRequest(
    QRestAccessManager *self,
    const QNetworkRequest *request) {
  return self->deleteResource(*request);
}

//  QNetworkReply *QRestAccessManager::deleteResourceNoDataImpl(const
//      QNetworkRequest &request, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager24deleteResourceNoDataImplERK15QNetworkRequestPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->deleteResourceNoDataImpl(*request, context, slot);
}

//  QNetworkReply *QRestAccessManager::head(const QNetworkRequest &request)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager4headERK15QNetworkRequest(
    QRestAccessManager *self,
    const QNetworkRequest *request) {
  return self->head(*request);
}

//  QNetworkReply *QRestAccessManager::headNoDataImpl(const QNetworkRequest
//      &request, const QObject *context, QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager14headNoDataImplERK15QNetworkRequestPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->headNoDataImpl(*request, context, slot);
}

//  QNetworkReply *QRestAccessManager::get(const QNetworkRequest &request)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager3getERK15QNetworkRequest(
    QRestAccessManager *self,
    const QNetworkRequest *request) {
  return self->get(*request);
}

//  QNetworkReply *QRestAccessManager::getNoDataImpl(const QNetworkRequest
//      &request, const QObject *context, QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager13getNoDataImplERK15QNetworkRequestPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->getNoDataImpl(*request, context, slot);
}

//  QNetworkReply *QRestAccessManager::get(const QNetworkRequest &request,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager3getERK15QNetworkRequestRK10QByteArray(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data) {
  return self->get(*request, *data);
}

//  QNetworkReply *QRestAccessManager::getWithDataImpl(const QNetworkRequest
//      &request, const QByteArray &data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager15getWithDataImplERK15QNetworkRequestRK10QByteArrayPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->getWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::get(const QNetworkRequest &request,
//      const QJsonDocument &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager3getERK15QNetworkRequestRK13QJsonDocument(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QJsonDocument *data) {
  return self->get(*request, *data);
}

//  QNetworkReply *QRestAccessManager::getWithDataImpl(const QNetworkRequest
//      &request, const QJsonDocument &data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager15getWithDataImplERK15QNetworkRequestRK13QJsonDocumentPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QJsonDocument *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->getWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::get(const QNetworkRequest &request,
//      QIODevice *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager3getERK15QNetworkRequestP9QIODevice(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data) {
  return self->get(*request, data);
}

//  QNetworkReply *QRestAccessManager::getWithDataImpl(const QNetworkRequest
//      &request, QIODevice *data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager15getWithDataImplERK15QNetworkRequestP9QIODevicePK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->getWithDataImpl(*request, data, context, slot);
}

//  QNetworkReply *QRestAccessManager::post(const QNetworkRequest &request,
//      const QJsonDocument &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager4postERK15QNetworkRequestRK13QJsonDocument(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QJsonDocument *data) {
  return self->post(*request, *data);
}

//  QNetworkReply *QRestAccessManager::postWithDataImpl(const QNetworkRequest
//      &request, const QJsonDocument &data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager16postWithDataImplERK15QNetworkRequestRK13QJsonDocumentPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QJsonDocument *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->postWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::post(const QNetworkRequest &request,
//      const QVariantMap &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager4postERK15QNetworkRequestRK4QMapI7QString8QVariantE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QMap<QString, QVariant> *data) {
  return self->post(*request, *data);
}

//  QNetworkReply *QRestAccessManager::postWithDataImpl(const QNetworkRequest
//      &request, const QVariantMap &data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager16postWithDataImplERK15QNetworkRequestRK4QMapI7QString8QVariantEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QMap<QString, QVariant> *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->postWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::post(const QNetworkRequest &request,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager4postERK15QNetworkRequestRK10QByteArray(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data) {
  return self->post(*request, *data);
}

//  QNetworkReply *QRestAccessManager::postWithDataImpl(const QNetworkRequest
//      &request, const QByteArray &data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager16postWithDataImplERK15QNetworkRequestRK10QByteArrayPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->postWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::post(const QNetworkRequest &request,
//      QHttpMultiPart *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager4postERK15QNetworkRequestP14QHttpMultiPart(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QHttpMultiPart *data) {
  return self->post(*request, data);
}

//  QNetworkReply *QRestAccessManager::postWithDataImpl(const QNetworkRequest
//      &request, QHttpMultiPart *data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager16postWithDataImplERK15QNetworkRequestP14QHttpMultiPartPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QHttpMultiPart *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->postWithDataImpl(*request, data, context, slot);
}

//  QNetworkReply *QRestAccessManager::post(const QNetworkRequest &request,
//      QIODevice *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager4postERK15QNetworkRequestP9QIODevice(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data) {
  return self->post(*request, data);
}

//  QNetworkReply *QRestAccessManager::postWithDataImpl(const QNetworkRequest
//      &request, QIODevice *data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager16postWithDataImplERK15QNetworkRequestP9QIODevicePK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->postWithDataImpl(*request, data, context, slot);
}

//  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
//      const QJsonDocument &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager3putERK15QNetworkRequestRK13QJsonDocument(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QJsonDocument *data) {
  return self->put(*request, *data);
}

//  QNetworkReply *QRestAccessManager::putWithDataImpl(const QNetworkRequest
//      &request, const QJsonDocument &data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager15putWithDataImplERK15QNetworkRequestRK13QJsonDocumentPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QJsonDocument *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->putWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
//      const QVariantMap &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager3putERK15QNetworkRequestRK4QMapI7QString8QVariantE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QMap<QString, QVariant> *data) {
  return self->put(*request, *data);
}

//  QNetworkReply *QRestAccessManager::putWithDataImpl(const QNetworkRequest
//      &request, const QVariantMap &data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager15putWithDataImplERK15QNetworkRequestRK4QMapI7QString8QVariantEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QMap<QString, QVariant> *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->putWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager3putERK15QNetworkRequestRK10QByteArray(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data) {
  return self->put(*request, *data);
}

//  QNetworkReply *QRestAccessManager::putWithDataImpl(const QNetworkRequest
//      &request, const QByteArray &data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager15putWithDataImplERK15QNetworkRequestRK10QByteArrayPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->putWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
//      QHttpMultiPart *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager3putERK15QNetworkRequestP14QHttpMultiPart(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QHttpMultiPart *data) {
  return self->put(*request, data);
}

//  QNetworkReply *QRestAccessManager::putWithDataImpl(const QNetworkRequest
//      &request, QHttpMultiPart *data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager15putWithDataImplERK15QNetworkRequestP14QHttpMultiPartPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QHttpMultiPart *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->putWithDataImpl(*request, data, context, slot);
}

//  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
//      QIODevice *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager3putERK15QNetworkRequestP9QIODevice(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data) {
  return self->put(*request, data);
}

//  QNetworkReply *QRestAccessManager::putWithDataImpl(const QNetworkRequest
//      &request, QIODevice *data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager15putWithDataImplERK15QNetworkRequestP9QIODevicePK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->putWithDataImpl(*request, data, context, slot);
}

//  QNetworkReply *QRestAccessManager::patch(const QNetworkRequest &request,
//      const QJsonDocument &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager5patchERK15QNetworkRequestRK13QJsonDocument(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QJsonDocument *data) {
  return self->patch(*request, *data);
}

//  QNetworkReply *QRestAccessManager::patchWithDataImpl(const
//      QNetworkRequest &request, const QJsonDocument &data, const QObject
//      *context, QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager17patchWithDataImplERK15QNetworkRequestRK13QJsonDocumentPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QJsonDocument *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->patchWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::patch(const QNetworkRequest &request,
//      const QVariantMap &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager5patchERK15QNetworkRequestRK4QMapI7QString8QVariantE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QMap<QString, QVariant> *data) {
  return self->patch(*request, *data);
}

//  QNetworkReply *QRestAccessManager::patchWithDataImpl(const
//      QNetworkRequest &request, const QVariantMap &data, const QObject
//      *context, QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager17patchWithDataImplERK15QNetworkRequestRK4QMapI7QString8QVariantEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QMap<QString, QVariant> *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->patchWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::patch(const QNetworkRequest &request,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager5patchERK15QNetworkRequestRK10QByteArray(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data) {
  return self->patch(*request, *data);
}

//  QNetworkReply *QRestAccessManager::patchWithDataImpl(const
//      QNetworkRequest &request, const QByteArray &data, const QObject
//      *context, QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager17patchWithDataImplERK15QNetworkRequestRK10QByteArrayPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->patchWithDataImpl(*request, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::patch(const QNetworkRequest &request,
//      QIODevice *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager5patchERK15QNetworkRequestP9QIODevice(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data) {
  return self->patch(*request, data);
}

//  QNetworkReply *QRestAccessManager::patchWithDataImpl(const
//      QNetworkRequest &request, QIODevice *data, const QObject *context,
//      QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager17patchWithDataImplERK15QNetworkRequestP9QIODevicePK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->patchWithDataImpl(*request, data, context, slot);
}

//  QNetworkReply *QRestAccessManager::sendCustomRequest(const
//      QNetworkRequest &request, const QByteArray &method, const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager17sendCustomRequestERK15QNetworkRequestRK10QByteArrayS5_(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *method,
    const QByteArray *data) {
  return self->sendCustomRequest(*request, *method, *data);
}

//  QNetworkReply *QRestAccessManager::customWithDataImpl(const
//      QNetworkRequest &request, const QByteArray &method, const QByteArray
//      &data, const QObject *context, QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager18customWithDataImplERK15QNetworkRequestRK10QByteArrayS5_PK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *method,
    const QByteArray *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->customWithDataImpl(*request, *method, *data, context, slot);
}

//  QNetworkReply *QRestAccessManager::sendCustomRequest(const
//      QNetworkRequest &request, const QByteArray &method, QIODevice *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager17sendCustomRequestERK15QNetworkRequestRK10QByteArrayP9QIODevice(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *method,
    QIODevice *data) {
  return self->sendCustomRequest(*request, *method, data);
}

//  QNetworkReply *QRestAccessManager::customWithDataImpl(const
//      QNetworkRequest &request, const QByteArray &method, QIODevice *data,
//      const QObject *context, QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager18customWithDataImplERK15QNetworkRequestRK10QByteArrayP9QIODevicePK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *method,
    QIODevice *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->customWithDataImpl(*request, *method, data, context, slot);
}

//  QNetworkReply *QRestAccessManager::sendCustomRequest(const
//      QNetworkRequest &request, const QByteArray &method, QHttpMultiPart
//      *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager17sendCustomRequestERK15QNetworkRequestRK10QByteArrayP14QHttpMultiPart(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *method,
    QHttpMultiPart *data) {
  return self->sendCustomRequest(*request, *method, data);
}

//  QNetworkReply *QRestAccessManager::customWithDataImpl(const
//      QNetworkRequest &request, const QByteArray &method, QHttpMultiPart
//      *data, const QObject *context, QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN18QRestAccessManager18customWithDataImplERK15QNetworkRequestRK10QByteArrayP14QHttpMultiPartPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *method,
    QHttpMultiPart *data,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  return self->customWithDataImpl(*request, *method, data, context, slot);
}

//  QRestAccessManagerPrivate *QRestAccessManager::d_func()
extern "C" Q_DECL_EXPORT
QRestAccessManagerPrivate *ritual_ZN18QRestAccessManager6d_funcEv(
    QRestAccessManager *self) {
  return self->d_func();
}

//  const QRestAccessManagerPrivate *QRestAccessManager::d_func() const
extern "C" Q_DECL_EXPORT
const QRestAccessManagerPrivate *ritual_ZNK18QRestAccessManager6d_funcEv(
    const QRestAccessManager *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQRestAccessManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRestAccessManager(
    QRestAccessManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRestAccessManager *>(self)->take(key, call);
}

#endif  // QT_CONFIG(http)
