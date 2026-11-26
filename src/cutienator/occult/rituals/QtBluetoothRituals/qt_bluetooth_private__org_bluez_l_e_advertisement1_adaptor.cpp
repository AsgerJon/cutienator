//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/leadvertisement1adaptor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/leadvertisement1adaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/leadvertisement1adaptor_p.h>
#include <QtCore/QMetaObject>
#include <QtCore/QByteArray>
#include <QtCore/QList>
#include <QtCore/QMap>
#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QVariant>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 38, as _ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor12discoverableEv
namespace QtBluetoothPrivate {
inline bool OrgBluezLEAdvertisement1Adaptor::discoverable() const
{
    // get the value of property Discoverable
    return qvariant_cast< bool >(parent()->property("Discoverable"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 44, as _ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor15setDiscoverableEb
namespace QtBluetoothPrivate {
inline void OrgBluezLEAdvertisement1Adaptor::setDiscoverable(bool value)
{
    // set the value of property Discoverable
    parent()->setProperty("Discoverable", QVariant::fromValue(value));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 50, as _ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor8includesEv
namespace QtBluetoothPrivate {
inline QStringList OrgBluezLEAdvertisement1Adaptor::includes() const
{
    // get the value of property Includes
    return qvariant_cast< QStringList >(parent()->property("Includes"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 56, as _ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11setIncludesERK5QListI7QStringE
namespace QtBluetoothPrivate {
inline void OrgBluezLEAdvertisement1Adaptor::setIncludes(const QStringList &value)
{
    // set the value of property Includes
    parent()->setProperty("Includes", QVariant::fromValue(value));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 62, as _ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor9localNameEv
namespace QtBluetoothPrivate {
inline QString OrgBluezLEAdvertisement1Adaptor::localName() const
{
    // get the value of property LocalName
    return qvariant_cast< QString >(parent()->property("LocalName"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 68, as _ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor12setLocalNameERK7QString
namespace QtBluetoothPrivate {
inline void OrgBluezLEAdvertisement1Adaptor::setLocalName(const QString &value)
{
    // set the value of property LocalName
    parent()->setProperty("LocalName", QVariant::fromValue(value));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 86, as _ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11maxIntervalEv
namespace QtBluetoothPrivate {
inline uint OrgBluezLEAdvertisement1Adaptor::maxInterval() const
{
    // get the value of property MaxInterval
    return qvariant_cast< uint >(parent()->property("MaxInterval"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 92, as _ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor14setMaxIntervalEj
namespace QtBluetoothPrivate {
inline void OrgBluezLEAdvertisement1Adaptor::setMaxInterval(uint value)
{
    // set the value of property MaxInterval
    parent()->setProperty("MaxInterval", QVariant::fromValue(value));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 98, as _ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11minIntervalEv
namespace QtBluetoothPrivate {
inline uint OrgBluezLEAdvertisement1Adaptor::minInterval() const
{
    // get the value of property MinInterval
    return qvariant_cast< uint >(parent()->property("MinInterval"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 104, as _ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor14setMinIntervalEj
namespace QtBluetoothPrivate {
inline void OrgBluezLEAdvertisement1Adaptor::setMinInterval(uint value)
{
    // set the value of property MinInterval
    parent()->setProperty("MinInterval", QVariant::fromValue(value));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 110, as _ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor12serviceUUIDsEv
namespace QtBluetoothPrivate {
inline QStringList OrgBluezLEAdvertisement1Adaptor::serviceUUIDs() const
{
    // get the value of property ServiceUUIDs
    return qvariant_cast< QStringList >(parent()->property("ServiceUUIDs"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 116, as _ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor15setServiceUUIDsERK5QListI7QStringE
namespace QtBluetoothPrivate {
inline void OrgBluezLEAdvertisement1Adaptor::setServiceUUIDs(const QStringList &value)
{
    // set the value of property ServiceUUIDs
    parent()->setProperty("ServiceUUIDs", QVariant::fromValue(value));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 122, as _ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor4typeEv
namespace QtBluetoothPrivate {
inline QString OrgBluezLEAdvertisement1Adaptor::type() const
{
    // get the value of property Type
    return qvariant_cast< QString >(parent()->property("Type"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisement1adaptor.cpp, line 128, as _ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor7setTypeERK7QString
namespace QtBluetoothPrivate {
inline void OrgBluezLEAdvertisement1Adaptor::setType(const QString &value)
{
    // set the value of property Type
    parent()->setProperty("Type", QVariant::fromValue(value));
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1Adaptor : public QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor {
public:
  using QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::OrgBluezLEAdvertisement1Adaptor;
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1AdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  return self->metaObject();
}

//  void
//      *QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::qt_metacast(con
//      st char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::qt_metacall(QMet
//      aObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::~OrgBluezLEAdvertise
//      ment1Adaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1AdaptorD1Ev(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  delete self;
}

//  bool QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::discoverable()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor12discoverableEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  return self->discoverable();
}

//  void
//      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setDiscoverable(
//      bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor15setDiscoverableEb(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    bool value) {
  self->setDiscoverable(value);
}

//  QStringList
//      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::includes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor8includesEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  return new QList<QString>(self->includes());
}

//  void
//      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setIncludes(cons
//      t QStringList &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11setIncludesERK5QListI7QStringE(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    const QList<QString> *value) {
  self->setIncludes(*value);
}

//  QString QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::localName()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor9localNameEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  return new QString(self->localName());
}

//  void
//      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setLocalName(con
//      st QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor12setLocalNameERK7QString(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    const QString *value) {
  self->setLocalName(*value);
}

//  uint QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::maxInterval()
//      const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11maxIntervalEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  return self->maxInterval();
}

//  void
//      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setMaxInterval(u
//      int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor14setMaxIntervalEj(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    uint value) {
  self->setMaxInterval(value);
}

//  uint QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::minInterval()
//      const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11minIntervalEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  return self->minInterval();
}

//  void
//      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setMinInterval(u
//      int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor14setMinIntervalEj(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    uint value) {
  self->setMinInterval(value);
}

//  QStringList
//      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::serviceUUIDs()
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor12serviceUUIDsEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  return new QList<QString>(self->serviceUUIDs());
}

//  void QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setServiceUUIDs
//      (const QStringList &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor15setServiceUUIDsERK5QListI7QStringE(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    const QList<QString> *value) {
  self->setServiceUUIDs(*value);
}

//  QString QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::type() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor4typeEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  return new QString(self->type());
}

//  void QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setType(const
//      QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor7setTypeERK7QString(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    const QString *value) {
  self->setType(*value);
}

//  void QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::Release()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor7ReleaseEv(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "Release()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "Release()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1Adaptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezLEAdvertisement1Adaptor(
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisement1Adaptor *>(self)->take(key, call);
}

//  a ManufacturerDataList a ritual of
//      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezLEAdvertisement1Adaptor__ManufacturerDataList(
    ManufacturerDataList *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
