//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmlistaccessordata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldmlistaccessordata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmladaptormodelenginedata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmladaptormodelenginedata.cpp, line 10, as _ZN26QQmlAdaptorModelEngineDataC1EPN3QV415ExecutionEngineE
inline QQmlAdaptorModelEngineData::QQmlAdaptorModelEngineData(QV4::ExecutionEngine *v4)
    : v4(v4)
{
    QV4::Scope scope(v4);
    QV4::ScopedObject proto(scope, v4->newObject());
    proto->defineAccessorProperty(QStringLiteral("index"), get_index, nullptr);
    proto->defineAccessorProperty(
                QStringLiteral("modelData"),
                QQmlDMListAccessorData::get_modelData, QQmlDMListAccessorData::set_modelData);
    proto->defineAccessorProperty(
                QString(),
                QQmlDMListAccessorData::get_modelData, QQmlDMListAccessorData::set_modelData);
    listItemProto.set(v4, proto);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmlistaccessordata.cpp, line 20, as _ZN22QQmlDMListAccessorDataD1Ev
inline QQmlDMListAccessorData::~QQmlDMListAccessorData()
{
    QObjectPrivate *d = QObjectPrivate::get(this);
    static_cast<VDMListDelegateDataType *>(d->metaObject)->release();
    d->metaObject = nullptr;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmlistaccessordata.cpp, line 37, as _ZN22QQmlDMListAccessorData8setValueERK7QStringRK8QVariant
inline void QQmlDMListAccessorData::setValue(const QString &role, const QVariant &value)
{
    // Used only for initialization of the cached data. Does not have to emit change signals.
    Q_ASSERT(!cachedDataClean);

    if (role == QLatin1String("modelData") || role.isEmpty())
        cachedData = value;
    else
        VDMListDelegateDataType::setValue(&cachedData, role, value);
}
//  -----------------------------------------------------------------------

//  A QQmlDMListAccessorData that Python can take functions over in. Every QQmlDMListAccessorData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_delegate_model)
typedef QV4::ReturnedValue (*CuteQQmlDMListAccessorDataCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDMListAccessorDataCall1)(const void *, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDMListAccessorDataCall2)(const void *, int, int, int, bool, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDMListAccessorDataCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDMListAccessorDataCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDMListAccessorDataCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDMListAccessorDataCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDMListAccessorDataCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDMListAccessorDataCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDMListAccessorDataCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDMListAccessorData : public QQmlDMListAccessorData {
public:
  using QQmlDMListAccessorData::QQmlDMListAccessorData;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN21QQmlDelegateModelItem3getEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN21QQmlDelegateModelItem8setValueERK7QStringRK8QVariant")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN21QQmlDelegateModelItem13setModelIndexEiiib")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_delegate_model)
  //  QV4::ReturnedValue QQmlDMListAccessorData::get()
  QV4::ReturnedValue get() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall0 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall0>(taken[0]);
      QV4::ReturnedValue given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlDMListAccessorData::get();
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDMListAccessorData::setValue(const QString &role, const
  //      QVariant &value)
  void setValue(const QString &role, const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall1 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall1>(taken[1]);
      call(this, &role, &value, &handled);
      if (handled) return;
    }
    QQmlDMListAccessorData::setValue(role, value);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelItem::setModelIndex(int idx, int newRow, int
  //      newColumn, bool alwaysEmit)
  void setModelIndex(
      int idx,
      int newRow,
      int newColumn,
      bool alwaysEmit) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall2 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall2>(taken[2]);
      call(this, idx, newRow, newColumn, alwaysEmit, &handled);
      if (handled) return;
    }
    QQmlDelegateModelItem::setModelIndex(idx, newRow, newColumn, alwaysEmit);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall3 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall4 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall5 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall6 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall7 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall8 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlDMListAccessorDataCall9 call = reinterpret_cast<CuteQQmlDMListAccessorDataCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDMListAccessorData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQmlDMListAccessorData10metaObjectEv(
    const QQmlDMListAccessorData *self) {
  return self->metaObject();
}

//  QQmlDMListAccessorData::~QQmlDMListAccessorData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDMListAccessorDataD1Ev(QQmlDMListAccessorData *self) {
  delete self;
}

//  QVariant QQmlDMListAccessorData::modelData() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QQmlDMListAccessorData9modelDataEv(
    const QQmlDMListAccessorData *self) {
  return new QVariant(self->modelData());
}

//  QV4::ReturnedValue QQmlDMListAccessorData::get()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN22QQmlDMListAccessorData3getEv(
    QQmlDMListAccessorData *self) {
  return self->get();
}

//  void QQmlDMListAccessorData::setValue(const QString &role, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDMListAccessorData8setValueERK7QStringRK8QVariant(
    QQmlDMListAccessorData *self,
    const QString *role,
    const QVariant *value) {
  self->setValue(*role, *value);
}

//  a Python function taken by a CuteQQmlDMListAccessorData, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDMListAccessorData(
    QQmlDMListAccessorData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDMListAccessorData *>(self)->take(key, call);
}

//  void QQmlDMListAccessorData::setValue(const QString &role, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQmlDMListAccessorData8setValueERK7QStringRK8QVariant(
    QQmlDMListAccessorData *self,
    const QString *role,
    const QVariant *value) {
  self->QQmlDMListAccessorData::setValue(*role, *value);
}

#endif  // QT_CONFIG(qml_delegate_model)
