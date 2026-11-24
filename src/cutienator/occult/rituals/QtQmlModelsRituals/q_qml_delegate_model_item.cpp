//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlDelegateModelItem that Python can take functions over in. Every QQmlDelegateModelItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelItemCall0)(const void *, int, int, int, bool, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef QV4::ReturnedValue (*CuteQQmlDelegateModelItemCall1)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelItemCall2)(const void *, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelegateModelItemCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelegateModelItemCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelItemCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelItemCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelItemCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelItemCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelItemCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDelegateModelItem : public QQmlDelegateModelItem {
public:
  using QQmlDelegateModelItem::QQmlDelegateModelItem;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN21QQmlDelegateModelItem13setModelIndexEiiib")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN21QQmlDelegateModelItem3getEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN21QQmlDelegateModelItem8setValueERK7QStringRK8QVariant")) {
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
  //  void QQmlDelegateModelItem::setModelIndex(int idx, int newRow, int
  //      newColumn, bool alwaysEmit)
  void setModelIndex(
      int idx,
      int newRow,
      int newColumn,
      bool alwaysEmit) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDelegateModelItemCall0 call = reinterpret_cast<CuteQQmlDelegateModelItemCall0>(taken[0]);
      call(this, idx, newRow, newColumn, alwaysEmit, &handled);
      if (handled) return;
    }
    QQmlDelegateModelItem::setModelIndex(idx, newRow, newColumn, alwaysEmit);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  QV4::ReturnedValue QQmlDelegateModelItem::get()
  QV4::ReturnedValue get() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDelegateModelItemCall1 call = reinterpret_cast<CuteQQmlDelegateModelItemCall1>(taken[1]);
      QV4::ReturnedValue given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlDelegateModelItem::get();
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelItem::setValue(const QString &role, const
  //      QVariant &value)
  void setValue(const QString &role, const QVariant &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDelegateModelItemCall2 call = reinterpret_cast<CuteQQmlDelegateModelItemCall2>(taken[2]);
      call(this, &role, &value, &handled);
      if (handled) return;
    }
    QQmlDelegateModelItem::setValue(role, value);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDelegateModelItemCall3 call = reinterpret_cast<CuteQQmlDelegateModelItemCall3>(taken[3]);
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
      CuteQQmlDelegateModelItemCall4 call = reinterpret_cast<CuteQQmlDelegateModelItemCall4>(taken[4]);
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
      CuteQQmlDelegateModelItemCall5 call = reinterpret_cast<CuteQQmlDelegateModelItemCall5>(taken[5]);
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
      CuteQQmlDelegateModelItemCall6 call = reinterpret_cast<CuteQQmlDelegateModelItemCall6>(taken[6]);
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
      CuteQQmlDelegateModelItemCall7 call = reinterpret_cast<CuteQQmlDelegateModelItemCall7>(taken[7]);
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
      CuteQQmlDelegateModelItemCall8 call = reinterpret_cast<CuteQQmlDelegateModelItemCall8>(taken[8]);
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
      CuteQQmlDelegateModelItemCall9 call = reinterpret_cast<CuteQQmlDelegateModelItemCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDelegateModelItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQmlDelegateModelItem10metaObjectEv(
    const QQmlDelegateModelItem *self) {
  return self->metaObject();
}

//  QString QQmlDelegateModelItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQmlDelegateModelItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDelegateModelItem::tr(s, c, n));
}

//  QQmlDelegateModelItem::~QQmlDelegateModelItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItemD1Ev(QQmlDelegateModelItem *self) {
  delete self;
}

//  QObject *QQmlDelegateModelItem::referenceObjectWeak()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN21QQmlDelegateModelItem19referenceObjectWeakEv(
    QQmlDelegateModelItem *self) {
  return self->referenceObjectWeak();
}

//  bool QQmlDelegateModelItem::releaseObjectWeak()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQmlDelegateModelItem17releaseObjectWeakEv(
    QQmlDelegateModelItem *self) {
  return self->releaseObjectWeak();
}

//  void QQmlDelegateModelItem::clearObjectWeakReferences()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem25clearObjectWeakReferencesEv(
    QQmlDelegateModelItem *self) {
  self->clearObjectWeakReferences();
}

//  bool QQmlDelegateModelItem::isObjectReferenced() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQmlDelegateModelItem18isObjectReferencedEv(
    const QQmlDelegateModelItem *self) {
  return self->isObjectReferenced();
}

//  void QQmlDelegateModelItem::childContextObjectDestroyed(QObject
//      *childContextObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem27childContextObjectDestroyedEP7QObject(
    QQmlDelegateModelItem *self,
    QObject *childContextObject) {
  self->childContextObjectDestroyed(childContextObject);
}

//  bool QQmlDelegateModelItem::isScriptReferenced() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQmlDelegateModelItem18isScriptReferencedEv(
    const QQmlDelegateModelItem *self) {
  return self->isScriptReferenced();
}

//  void QQmlDelegateModelItem::dispose()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem7disposeEv(
    QQmlDelegateModelItem *self) {
  self->dispose();
}

//  QObject *QQmlDelegateModelItem::modelObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN21QQmlDelegateModelItem11modelObjectEv(
    QQmlDelegateModelItem *self) {
  return self->modelObject();
}

//  void QQmlDelegateModelItem::destroyObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem13destroyObjectEv(
    QQmlDelegateModelItem *self) {
  self->destroyObject();
}

//  void QQmlDelegateModelItem::destroyObjectLater()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem18destroyObjectLaterEv(
    QQmlDelegateModelItem *self) {
  self->destroyObjectLater();
}

//  QQmlDelegateModelItem *QQmlDelegateModelItem::dataForObject(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem *ritual_ZN21QQmlDelegateModelItem13dataForObjectEP7QObject(
    QObject *object) {
  return QQmlDelegateModelItem::dataForObject(object);
}

//  int QQmlDelegateModelItem::modelRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQmlDelegateModelItem8modelRowEv(
    const QQmlDelegateModelItem *self) {
  return self->modelRow();
}

//  int QQmlDelegateModelItem::modelColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQmlDelegateModelItem11modelColumnEv(
    const QQmlDelegateModelItem *self) {
  return self->modelColumn();
}

//  int QQmlDelegateModelItem::modelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQmlDelegateModelItem10modelIndexEv(
    const QQmlDelegateModelItem *self) {
  return self->modelIndex();
}

//  bool QQmlDelegateModelItem::hasValidModelIndex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQmlDelegateModelItem18hasValidModelIndexEv(
    const QQmlDelegateModelItem *self) {
  return self->hasValidModelIndex();
}

//  void QQmlDelegateModelItem::setModelIndex(int idx, int newRow, int
//      newColumn, bool alwaysEmit)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem13setModelIndexEiiib(
    QQmlDelegateModelItem *self,
    int idx,
    int newRow,
    int newColumn,
    bool alwaysEmit) {
  self->setModelIndex(idx, newRow, newColumn, alwaysEmit);
}

//  void QQmlDelegateModelItem::setPersistentModelIndex(const
//      QPersistentModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem23setPersistentModelIndexERK21QPersistentModelIndex(
    QQmlDelegateModelItem *self,
    const QPersistentModelIndex *index) {
  self->setPersistentModelIndex(*index);
}

//  QPersistentModelIndex QQmlDelegateModelItem::persistentModelIndex() const
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_ZNK21QQmlDelegateModelItem20persistentModelIndexEv(
    const QQmlDelegateModelItem *self) {
  return new QPersistentModelIndex(self->persistentModelIndex());
}

//  bool QQmlDelegateModelItem::usesStructuredModelData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQmlDelegateModelItem23usesStructuredModelDataEv(
    const QQmlDelegateModelItem *self) {
  return self->usesStructuredModelData();
}

//  QV4::ReturnedValue QQmlDelegateModelItem::get()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN21QQmlDelegateModelItem3getEv(
    QQmlDelegateModelItem *self) {
  return self->get();
}

//  void QQmlDelegateModelItem::setValue(const QString &role, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem8setValueERK7QStringRK8QVariant(
    QQmlDelegateModelItem *self,
    const QString *role,
    const QVariant *value) {
  self->setValue(*role, *value);
}

//  QV4::ReturnedValue QQmlDelegateModelItem::get_model(const
//      QV4::FunctionObject *a0, const QV4::Value *thisObject, const
//      QV4::Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN21QQmlDelegateModelItem9get_modelEPKN3QV414FunctionObjectEPKNS0_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QQmlDelegateModelItem::get_model(a0, thisObject, argv, argc);
}

//  QV4::ReturnedValue QQmlDelegateModelItem::get_groups(const
//      QV4::FunctionObject *a0, const QV4::Value *thisObject, const
//      QV4::Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN21QQmlDelegateModelItem10get_groupsEPKN3QV414FunctionObjectEPKNS0_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QQmlDelegateModelItem::get_groups(a0, thisObject, argv, argc);
}

//  QV4::ReturnedValue QQmlDelegateModelItem::set_groups(const
//      QV4::FunctionObject *a0, const QV4::Value *thisObject, const
//      QV4::Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN21QQmlDelegateModelItem10set_groupsEPKN3QV414FunctionObjectEPKNS0_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QQmlDelegateModelItem::set_groups(a0, thisObject, argv, argc);
}

//  QV4::ReturnedValue
//      QQmlDelegateModelItem::get_member(QQmlDelegateModelItem *thisItem,
//      uint flag, const QV4::Value &a2)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN21QQmlDelegateModelItem10get_memberEPS_jRKN3QV45ValueE(
    QQmlDelegateModelItem *thisItem,
    uint flag,
    const QV4::Value *a2) {
  return QQmlDelegateModelItem::get_member(thisItem, flag, *a2);
}

//  QV4::ReturnedValue
//      QQmlDelegateModelItem::set_member(QQmlDelegateModelItem *thisItem,
//      uint flag, const QV4::Value &arg)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN21QQmlDelegateModelItem10set_memberEPS_jRKN3QV45ValueE(
    QQmlDelegateModelItem *thisItem,
    uint flag,
    const QV4::Value *arg) {
  return QQmlDelegateModelItem::set_member(thisItem, flag, *arg);
}

//  QV4::ReturnedValue QQmlDelegateModelItem::get_index(QQmlDelegateModelItem
//      *thisItem, uint flag, const QV4::Value &arg)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN21QQmlDelegateModelItem9get_indexEPS_jRKN3QV45ValueE(
    QQmlDelegateModelItem *thisItem,
    uint flag,
    const QV4::Value *arg) {
  return QQmlDelegateModelItem::get_index(thisItem, flag, *arg);
}

//  QQmlDelegateModelAttached *QQmlDelegateModelItem::attached() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModelAttached *ritual_ZNK21QQmlDelegateModelItem8attachedEv(
    const QQmlDelegateModelItem *self) {
  return self->attached();
}

//  void QQmlDelegateModelItem::disableStructuredModelData()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem26disableStructuredModelDataEv(
    QQmlDelegateModelItem *self) {
  self->disableStructuredModelData();
}

//  QDynamicMetaObjectData
//      *QQmlDelegateModelItem::exchangeMetaObject(QDynamicMetaObjectData
//      *metaObject)
extern "C" Q_DECL_EXPORT
QDynamicMetaObjectData *ritual_ZN21QQmlDelegateModelItem18exchangeMetaObjectEP22QDynamicMetaObjectData(
    QQmlDelegateModelItem *self,
    QDynamicMetaObjectData *metaObject) {
  return self->exchangeMetaObject(metaObject);
}

//  QQDMIncubationTask *QQmlDelegateModelItem::incubationTask() const
extern "C" Q_DECL_EXPORT
QQDMIncubationTask *ritual_ZNK21QQmlDelegateModelItem14incubationTaskEv(
    const QQmlDelegateModelItem *self) {
  return self->incubationTask();
}

//  void QQmlDelegateModelItem::clearIncubationTask()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem19clearIncubationTaskEv(
    QQmlDelegateModelItem *self) {
  self->clearIncubationTask();
}

//  void QQmlDelegateModelItem::setIncubationTask(QQDMIncubationTask
//      *incubationTask)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem17setIncubationTaskEP18QQDMIncubationTask(
    QQmlDelegateModelItem *self,
    QQDMIncubationTask *incubationTask) {
  self->setIncubationTask(incubationTask);
}

//  quint16 QQmlDelegateModelItem::objectStrongRef() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK21QQmlDelegateModelItem15objectStrongRefEv(
    const QQmlDelegateModelItem *self) {
  return self->objectStrongRef();
}

//  quint16 QQmlDelegateModelItem::objectWeakRef() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK21QQmlDelegateModelItem13objectWeakRefEv(
    const QQmlDelegateModelItem *self) {
  return self->objectWeakRef();
}

//  quint16 QQmlDelegateModelItem::scriptRef() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK21QQmlDelegateModelItem9scriptRefEv(
    const QQmlDelegateModelItem *self) {
  return self->scriptRef();
}

//  QObject *QQmlDelegateModelItem::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK21QQmlDelegateModelItem6objectEv(
    const QQmlDelegateModelItem *self) {
  return self->object();
}

//  void QQmlDelegateModelItem::setObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem9setObjectEP7QObject(
    QQmlDelegateModelItem *self,
    QObject *object) {
  self->setObject(object);
}

//  QQmlComponent *QQmlDelegateModelItem::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK21QQmlDelegateModelItem8delegateEv(
    const QQmlDelegateModelItem *self) {
  return self->delegate();
}

//  void QQmlDelegateModelItem::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem11setDelegateEP13QQmlComponent(
    QQmlDelegateModelItem *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  int QQmlDelegateModelItem::groups() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQmlDelegateModelItem6groupsEv(
    const QQmlDelegateModelItem *self) {
  return self->groups();
}

//  void QQmlDelegateModelItem::setGroups(int groups)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem9setGroupsEi(
    QQmlDelegateModelItem *self,
    int groups) {
  self->setGroups(groups);
}

//  void QQmlDelegateModelItem::addGroups(int groups)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem9addGroupsEi(
    QQmlDelegateModelItem *self,
    int groups) {
  self->addGroups(groups);
}

//  void QQmlDelegateModelItem::removeGroups(int groups)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem12removeGroupsEi(
    QQmlDelegateModelItem *self,
    int groups) {
  self->removeGroups(groups);
}

//  void QQmlDelegateModelItem::clearGroups()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem11clearGroupsEv(
    QQmlDelegateModelItem *self) {
  self->clearGroups();
}

//  void QQmlDelegateModelItem::referenceSript()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem14referenceSriptEv(
    QQmlDelegateModelItem *self) {
  self->referenceSript();
}

//  bool QQmlDelegateModelItem::releaseScript()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQmlDelegateModelItem13releaseScriptEv(
    QQmlDelegateModelItem *self) {
  return self->releaseScript();
}

//  a Python function taken by a CuteQQmlDelegateModelItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDelegateModelItem(
    QQmlDelegateModelItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDelegateModelItem *>(self)->take(key, call);
}

//  void QQmlDelegateModelItem::setModelIndex(int idx, int newRow, int
//      newColumn, bool alwaysEmit)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQmlDelegateModelItem13setModelIndexEiiib(
    QQmlDelegateModelItem *self,
    int idx,
    int newRow,
    int newColumn,
    bool alwaysEmit) {
  self->QQmlDelegateModelItem::setModelIndex(
      idx,
      newRow,
      newColumn,
      alwaysEmit);
}

//  QV4::ReturnedValue QQmlDelegateModelItem::get()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_own_ZN21QQmlDelegateModelItem3getEv(
    QQmlDelegateModelItem *self) {
  return self->QQmlDelegateModelItem::get();
}

//  void QQmlDelegateModelItem::setValue(const QString &role, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQmlDelegateModelItem8setValueERK7QStringRK8QVariant(
    QQmlDelegateModelItem *self,
    const QString *role,
    const QVariant *value) {
  self->QQmlDelegateModelItem::setValue(*role, *value);
}

//  QList<QQmlDelegateModelItem *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlDelegateModelItem *> *ritual_list_make_QQmlDelegateModelItem_ptr() {
  return new QList<QQmlDelegateModelItem *>();
}

//  void QList<QQmlDelegateModelItem *>::append(const QQmlDelegateModelItem *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlDelegateModelItem_ptr(
    QList<QQmlDelegateModelItem *> *self,
    QQmlDelegateModelItem *element) {
  self->append(element);
}

//  qsizetype QList<QQmlDelegateModelItem *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlDelegateModelItem_ptr(
    const QList<QQmlDelegateModelItem *> *self) {
  return self->size();
}

//  const QQmlDelegateModelItem * &QList<QQmlDelegateModelItem
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem *ritual_list_at_QQmlDelegateModelItem_ptr(
    const QList<QQmlDelegateModelItem *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQmlDelegateModelItem *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlDelegateModelItem_ptr(
    QList<QQmlDelegateModelItem *> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
