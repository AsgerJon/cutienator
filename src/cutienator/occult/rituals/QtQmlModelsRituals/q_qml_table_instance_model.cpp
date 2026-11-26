//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmltableinstancemodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmltableinstancemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlTableInstanceModel that Python can take functions over in. Every QQmlTableInstanceModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef int (*CuteQQmlTableInstanceModelCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef bool (*CuteQQmlTableInstanceModelCall1)(const void *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef void * (*CuteQQmlTableInstanceModelCall2)(const void *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef void * (*CuteQQmlTableInstanceModelCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef int (*CuteQQmlTableInstanceModelCall4)(const void *, QObject *, int, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef void (*CuteQQmlTableInstanceModelCall5)(const void *, int, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef void (*CuteQQmlTableInstanceModelCall6)(const void *, int, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef int (*CuteQQmlTableInstanceModelCall7)(const void *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef int (*CuteQQmlTableInstanceModelCall8)(const void *, int, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef const QVariant * (*CuteQQmlTableInstanceModelCall9)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
typedef int (*CuteQQmlTableInstanceModelCall10)(const void *, QObject *, QObject *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlTableInstanceModelCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlTableInstanceModelCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableInstanceModelCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableInstanceModelCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableInstanceModelCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableInstanceModelCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableInstanceModelCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlTableInstanceModel : public QQmlTableInstanceModel {
public:
  using QQmlTableInstanceModel::QQmlTableInstanceModel;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel5countEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel7isValidEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel17abstractItemModelEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel6objectEiN13QQmlIncubator14IncubationModeE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel7releaseEP7QObjectNS_12ReusableFlagE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel6cancelEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel22drainReusableItemsPoolEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel8poolSizeEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel16incubationStatusEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel12variantValueEiRK7QString")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel7indexOfEP7QObjectS1_")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  int QQmlTableInstanceModel::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall0 call = reinterpret_cast<CuteQQmlTableInstanceModelCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlTableInstanceModel::count();
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  bool QQmlTableInstanceModel::isValid() const
  bool isValid() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall1 call = reinterpret_cast<CuteQQmlTableInstanceModelCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlTableInstanceModel::isValid();
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  const QAbstractItemModel *QQmlTableInstanceModel::abstractItemModel()
  //      const
  const QAbstractItemModel *abstractItemModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall2 call = reinterpret_cast<CuteQQmlTableInstanceModelCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QAbstractItemModel *>(given);
    }
    return QQmlTableInstanceModel::abstractItemModel();
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  QObject *QQmlTableInstanceModel::object(int index,
  //      QQmlIncubator::IncubationMode incubationMode)
  QObject *object(
      int index,
      QQmlIncubator::IncubationMode incubationMode) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall3 call = reinterpret_cast<CuteQQmlTableInstanceModelCall3>(taken[3]);
      void * given = call(this, index, static_cast<int>(incubationMode), &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlTableInstanceModel::object(index, incubationMode);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  ReleaseFlags QQmlTableInstanceModel::release(QObject *object,
  //      ReusableFlag reusable)
  QQmlInstanceModel::ReleaseFlags release(
      QObject *object,
      QQmlInstanceModel::ReusableFlag reusable) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall4 call = reinterpret_cast<CuteQQmlTableInstanceModelCall4>(taken[4]);
      int given = call(this, object, static_cast<int>(reusable), &handled);
      if (handled) return QFlags<QQmlInstanceModel::ReleaseFlag>::fromInt(given);
    }
    return QQmlTableInstanceModel::release(object, reusable);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  void QQmlTableInstanceModel::cancel(int a0)
  void cancel(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall5 call = reinterpret_cast<CuteQQmlTableInstanceModelCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlTableInstanceModel::cancel(a0);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  void QQmlTableInstanceModel::drainReusableItemsPool(int maxPoolTime)
  void drainReusableItemsPool(int maxPoolTime) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall6 call = reinterpret_cast<CuteQQmlTableInstanceModelCall6>(taken[6]);
      call(this, maxPoolTime, &handled);
      if (handled) return;
    }
    QQmlTableInstanceModel::drainReusableItemsPool(maxPoolTime);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  int QQmlTableInstanceModel::poolSize()
  int poolSize() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall7 call = reinterpret_cast<CuteQQmlTableInstanceModelCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlTableInstanceModel::poolSize();
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  QQmlIncubator::Status QQmlTableInstanceModel::incubationStatus(int
  //      index)
  QQmlIncubator::Status incubationStatus(int index) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall8 call = reinterpret_cast<CuteQQmlTableInstanceModelCall8>(taken[8]);
      int given = call(this, index, &handled);
      if (handled) return static_cast<QQmlIncubator::Status>(given);
    }
    return QQmlTableInstanceModel::incubationStatus(index);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  QVariant QQmlTableInstanceModel::variantValue(int a0, const QString
  //      &a1)
  QVariant variantValue(int a0, const QString &a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall9 call = reinterpret_cast<CuteQQmlTableInstanceModelCall9>(taken[9]);
      const QVariant * given = call(this, a0, &a1, &handled);
      if (handled && given) return *given;
    }
    return QQmlTableInstanceModel::variantValue(a0, a1);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_table_model)
  //  int QQmlTableInstanceModel::indexOf(QObject *a0, QObject *a1) const
  int indexOf(QObject *a0, QObject *a1) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall10 call = reinterpret_cast<CuteQQmlTableInstanceModelCall10>(taken[10]);
      int given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQmlTableInstanceModel::indexOf(a0, a1);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_object_model)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall11 call = reinterpret_cast<CuteQQmlTableInstanceModelCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall12 call = reinterpret_cast<CuteQQmlTableInstanceModelCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall13 call = reinterpret_cast<CuteQQmlTableInstanceModelCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall14 call = reinterpret_cast<CuteQQmlTableInstanceModelCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall15 call = reinterpret_cast<CuteQQmlTableInstanceModelCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall16 call = reinterpret_cast<CuteQQmlTableInstanceModelCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlTableInstanceModelCall17 call = reinterpret_cast<CuteQQmlTableInstanceModelCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlTableInstanceModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQmlTableInstanceModel10metaObjectEv(
    const QQmlTableInstanceModel *self) {
  return self->metaObject();
}

//  void *QQmlTableInstanceModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQmlTableInstanceModel11qt_metacastEPKc(
    QQmlTableInstanceModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlTableInstanceModel::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlTableInstanceModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlTableInstanceModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlTableInstanceModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQmlTableInstanceModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlTableInstanceModel::tr(s, c, n));
}

//  QQmlTableInstanceModel::QQmlTableInstanceModel(QQmlContext *qmlContext,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlTableInstanceModel *ritual_ZN22QQmlTableInstanceModelC1EP11QQmlContextP7QObject(
    QQmlContext *qmlContext,
    QObject *parent) {
  return new CuteQQmlTableInstanceModel(qmlContext, parent);
}

//  QQmlTableInstanceModel::~QQmlTableInstanceModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModelD1Ev(QQmlTableInstanceModel *self) {
  delete self;
}

//  void QQmlTableInstanceModel::useImportVersion(QTypeRevision version)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel16useImportVersionE13QTypeRevision(
    QQmlTableInstanceModel *self,
    const QTypeRevision *version) {
  self->useImportVersion(*version);
}

//  int QQmlTableInstanceModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlTableInstanceModel5countEv(
    const QQmlTableInstanceModel *self) {
  return self->count();
}

//  int QQmlTableInstanceModel::rows() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlTableInstanceModel4rowsEv(
    const QQmlTableInstanceModel *self) {
  return self->rows();
}

//  int QQmlTableInstanceModel::columns() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlTableInstanceModel7columnsEv(
    const QQmlTableInstanceModel *self) {
  return self->columns();
}

//  bool QQmlTableInstanceModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQmlTableInstanceModel7isValidEv(
    const QQmlTableInstanceModel *self) {
  return self->isValid();
}

//  bool QQmlTableInstanceModel::canFetchMore() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQmlTableInstanceModel12canFetchMoreEv(
    const QQmlTableInstanceModel *self) {
  return self->canFetchMore();
}

//  void QQmlTableInstanceModel::fetchMore()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel9fetchMoreEv(
    QQmlTableInstanceModel *self) {
  self->fetchMore();
}

//  QVariant QQmlTableInstanceModel::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QQmlTableInstanceModel5modelEv(
    const QQmlTableInstanceModel *self) {
  return new QVariant(self->model());
}

//  void QQmlTableInstanceModel::setModel(const QVariant &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel8setModelERK8QVariant(
    QQmlTableInstanceModel *self,
    const QVariant *model) {
  self->setModel(*model);
}

//  QQmlComponent *QQmlTableInstanceModel::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK22QQmlTableInstanceModel8delegateEv(
    const QQmlTableInstanceModel *self) {
  return self->delegate();
}

//  void QQmlTableInstanceModel::setDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel11setDelegateEP13QQmlComponent(
    QQmlTableInstanceModel *self,
    QQmlComponent *a0) {
  self->setDelegate(a0);
}

//  QQmlDelegateModel::DelegateModelAccess
//      QQmlTableInstanceModel::delegateModelAccess() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel::DelegateModelAccess ritual_ZNK22QQmlTableInstanceModel19delegateModelAccessEv(
    const QQmlTableInstanceModel *self) {
  return self->delegateModelAccess();
}

//  void QQmlTableInstanceModel::setDelegateModelAccess(QQmlDelegateModel::De
//      legateModelAccess delegateModelAccess)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel22setDelegateModelAccessEN17QQmlDelegateModel19DelegateModelAccessE(
    QQmlTableInstanceModel *self,
    QQmlDelegateModel::DelegateModelAccess delegateModelAccess) {
  self->setDelegateModelAccess(delegateModelAccess);
}

//  const QAbstractItemModel *QQmlTableInstanceModel::abstractItemModel()
//      const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK22QQmlTableInstanceModel17abstractItemModelEv(
    const QQmlTableInstanceModel *self) {
  return self->abstractItemModel();
}

//  QObject *QQmlTableInstanceModel::object(int index,
//      QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN22QQmlTableInstanceModel6objectEiN13QQmlIncubator14IncubationModeE(
    QQmlTableInstanceModel *self,
    int index,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->object(index, incubationMode);
}

//  QObject
//      *QQmlTableInstanceModel::incubateModelItemIfNeeded(QQmlDelegateModelI
//      tem *modelItem, QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN22QQmlTableInstanceModel25incubateModelItemIfNeededEP21QQmlDelegateModelItemN13QQmlIncubator14IncubationModeE(
    QQmlTableInstanceModel *self,
    QQmlDelegateModelItem *modelItem,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->incubateModelItemIfNeeded(modelItem, incubationMode);
}

//  void QQmlTableInstanceModel::restoreFromReleasedItemsCache(QQmlDelegateMo
//      delItem *item, int newFlatIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel29restoreFromReleasedItemsCacheEP21QQmlDelegateModelItemi(
    QQmlTableInstanceModel *self,
    QQmlDelegateModelItem *item,
    int newFlatIndex) {
  self->restoreFromReleasedItemsCache(item, newFlatIndex);
}

//  void QQmlTableInstanceModel::commitReleasedItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel19commitReleasedItemsEv(
    QQmlTableInstanceModel *self) {
  self->commitReleasedItems();
}

//  ReleaseFlags QQmlTableInstanceModel::release(QObject *object,
//      ReusableFlag reusable)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlTableInstanceModel7releaseEP7QObjectN17QQmlInstanceModel12ReusableFlagE(
    QQmlTableInstanceModel *self,
    QObject *object,
    QQmlInstanceModel::ReusableFlag reusable) {
  return static_cast<int>(self->release(object, reusable).toInt());
}

//  void QQmlTableInstanceModel::dispose(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel7disposeEP7QObject(
    QQmlTableInstanceModel *self,
    QObject *object) {
  self->dispose(object);
}

//  void QQmlTableInstanceModel::cancel(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel6cancelEi(
    QQmlTableInstanceModel *self,
    int a0) {
  self->cancel(a0);
}

//  void QQmlTableInstanceModel::drainReusableItemsPool(int maxPoolTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel22drainReusableItemsPoolEi(
    QQmlTableInstanceModel *self,
    int maxPoolTime) {
  self->drainReusableItemsPool(maxPoolTime);
}

//  int QQmlTableInstanceModel::poolSize()
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlTableInstanceModel8poolSizeEv(
    QQmlTableInstanceModel *self) {
  return self->poolSize();
}

//  void QQmlTableInstanceModel::reuseItem(QQmlDelegateModelItem *item, int
//      newModelIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel9reuseItemEP21QQmlDelegateModelItemi(
    QQmlTableInstanceModel *self,
    QQmlDelegateModelItem *item,
    int newModelIndex) {
  self->reuseItem(item, newModelIndex);
}

//  QQmlIncubator::Status QQmlTableInstanceModel::incubationStatus(int index)
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_ZN22QQmlTableInstanceModel16incubationStatusEi(
    QQmlTableInstanceModel *self,
    int index) {
  return self->incubationStatus(index);
}

//  bool QQmlTableInstanceModel::setRequiredProperty(int index, const QString
//      &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQmlTableInstanceModel19setRequiredPropertyEiRK7QStringRK8QVariant(
    QQmlTableInstanceModel *self,
    int index,
    const QString *name,
    const QVariant *value) {
  return self->setRequiredProperty(index, *name, *value);
}

//  QVariant QQmlTableInstanceModel::variantValue(int a0, const QString &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN22QQmlTableInstanceModel12variantValueEiRK7QString(
    QQmlTableInstanceModel *self,
    int a0,
    const QString *a1) {
  return new QVariant(self->variantValue(a0, *a1));
}

//  void QQmlTableInstanceModel::setWatchedRoles(const QList<QByteArray> &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel15setWatchedRolesERK5QListI10QByteArrayE(
    QQmlTableInstanceModel *self,
    const QList<QByteArray> *a0) {
  self->setWatchedRoles(*a0);
}

//  int QQmlTableInstanceModel::indexOf(QObject *a0, QObject *a1) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlTableInstanceModel7indexOfEP7QObjectS1_(
    const QQmlTableInstanceModel *self,
    QObject *a0,
    QObject *a1) {
  return self->indexOf(a0, a1);
}

//  QQmlDelegateModelItem *QQmlTableInstanceModel::getModelItem(int index)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem *ritual_ZN22QQmlTableInstanceModel12getModelItemEi(
    QQmlTableInstanceModel *self,
    int index) {
  return self->getModelItem(index);
}

//  void QQmlTableInstanceModel::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel12modelChangedEv(
    QQmlTableInstanceModel *self) {
  self->modelChanged();
}

//  QQmlComponent *QQmlTableInstanceModel::resolveDelegate(int index)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN22QQmlTableInstanceModel15resolveDelegateEi(
    QQmlTableInstanceModel *self,
    int index) {
  return self->resolveDelegate(index);
}

//  void QQmlTableInstanceModel::incubateModelItem(QQmlDelegateModelItem
//      *modelItem, QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel17incubateModelItemEP21QQmlDelegateModelItemN13QQmlIncubator14IncubationModeE(
    QQmlTableInstanceModel *self,
    QQmlDelegateModelItem *modelItem,
    QQmlIncubator::IncubationMode incubationMode) {
  self->incubateModelItem(modelItem, incubationMode);
}

//  void QQmlTableInstanceModel::incubatorStatusChanged(QQmlTableInstanceMode
//      lIncubationTask *dmIncubationTask, QQmlIncubator::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel22incubatorStatusChangedEP36QQmlTableInstanceModelIncubationTaskN13QQmlIncubator6StatusE(
    QQmlTableInstanceModel *self,
    QQmlTableInstanceModelIncubationTask *dmIncubationTask,
    QQmlIncubator::Status status) {
  self->incubatorStatusChanged(dmIncubationTask, status);
}

//  void QQmlTableInstanceModel::deleteIncubationTaskLater(QQmlIncubator
//      *incubationTask)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel25deleteIncubationTaskLaterEP13QQmlIncubator(
    QQmlTableInstanceModel *self,
    QQmlIncubator *incubationTask) {
  self->deleteIncubationTaskLater(incubationTask);
}

//  void QQmlTableInstanceModel::deleteAllFinishedIncubationTasks()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel32deleteAllFinishedIncubationTasksEv(
    QQmlTableInstanceModel *self) {
  self->deleteAllFinishedIncubationTasks();
}

//  QQmlDelegateModelItem *QQmlTableInstanceModel::resolveModelItem(int
//      flatIndex, const QModelIndex &modelIndex)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem *ritual_ZN22QQmlTableInstanceModel16resolveModelItemEiRK11QModelIndex(
    QQmlTableInstanceModel *self,
    int flatIndex,
    const QModelIndex *modelIndex) {
  return self->resolveModelItem(flatIndex, *modelIndex);
}

//  void QQmlTableInstanceModel::destroyModelItem(QQmlDelegateModelItem
//      *modelItem, DestructionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel16destroyModelItemEP21QQmlDelegateModelItemNS_15DestructionModeE(
    QQmlTableInstanceModel *self,
    QQmlDelegateModelItem *modelItem,
    QQmlTableInstanceModel::DestructionMode mode) {
  self->destroyModelItem(modelItem, mode);
}

//  void QQmlTableInstanceModel::dataChangedCallback(const QModelIndex
//      &begin, const QModelIndex &end, const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel19dataChangedCallbackERK11QModelIndexS2_RK5QListIiE(
    QQmlTableInstanceModel *self,
    const QModelIndex *begin,
    const QModelIndex *end,
    const QList<int> *roles) {
  self->dataChangedCallback(*begin, *end, *roles);
}

//  void QQmlTableInstanceModel::modelAboutToBeResetCallback()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel27modelAboutToBeResetCallbackEv(
    QQmlTableInstanceModel *self) {
  self->modelAboutToBeResetCallback();
}

//  void QQmlTableInstanceModel::forceSetModel(const QVariant &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel13forceSetModelERK8QVariant(
    QQmlTableInstanceModel *self,
    const QVariant *model) {
  self->forceSetModel(*model);
}

//  bool QQmlTableInstanceModel::isDoneIncubating(QQmlDelegateModelItem
//      *modelItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQmlTableInstanceModel16isDoneIncubatingEP21QQmlDelegateModelItem(
    QQmlDelegateModelItem *modelItem) {
  return QQmlTableInstanceModel::isDoneIncubating(modelItem);
}

//  void QQmlTableInstanceModel::deleteModelItemLater(QQmlDelegateModelItem
//      *modelItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlTableInstanceModel20deleteModelItemLaterEP21QQmlDelegateModelItem(
    QQmlDelegateModelItem *modelItem) {
  QQmlTableInstanceModel::deleteModelItemLater(modelItem);
}

//  a Python function taken by a CuteQQmlTableInstanceModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlTableInstanceModel(
    QQmlTableInstanceModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlTableInstanceModel *>(self)->take(key, call);
}

//  int QQmlTableInstanceModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QQmlTableInstanceModel5countEv(
    const QQmlTableInstanceModel *self) {
  return self->QQmlTableInstanceModel::count();
}

//  bool QQmlTableInstanceModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QQmlTableInstanceModel7isValidEv(
    const QQmlTableInstanceModel *self) {
  return self->QQmlTableInstanceModel::isValid();
}

//  const QAbstractItemModel *QQmlTableInstanceModel::abstractItemModel()
//      const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_own_ZNK22QQmlTableInstanceModel17abstractItemModelEv(
    const QQmlTableInstanceModel *self) {
  return self->QQmlTableInstanceModel::abstractItemModel();
}

//  QObject *QQmlTableInstanceModel::object(int index,
//      QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN22QQmlTableInstanceModel6objectEiN13QQmlIncubator14IncubationModeE(
    QQmlTableInstanceModel *self,
    int index,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->QQmlTableInstanceModel::object(index, incubationMode);
}

//  ReleaseFlags QQmlTableInstanceModel::release(QObject *object,
//      ReusableFlag reusable)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN22QQmlTableInstanceModel7releaseEP7QObjectN17QQmlInstanceModel12ReusableFlagE(
    QQmlTableInstanceModel *self,
    QObject *object,
    QQmlInstanceModel::ReusableFlag reusable) {
  return static_cast<int>(
      self->QQmlTableInstanceModel::release(
          object,
          reusable).toInt());
}

//  void QQmlTableInstanceModel::cancel(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQmlTableInstanceModel6cancelEi(
    QQmlTableInstanceModel *self,
    int a0) {
  self->QQmlTableInstanceModel::cancel(a0);
}

//  void QQmlTableInstanceModel::drainReusableItemsPool(int maxPoolTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQmlTableInstanceModel22drainReusableItemsPoolEi(
    QQmlTableInstanceModel *self,
    int maxPoolTime) {
  self->QQmlTableInstanceModel::drainReusableItemsPool(maxPoolTime);
}

//  int QQmlTableInstanceModel::poolSize()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN22QQmlTableInstanceModel8poolSizeEv(
    QQmlTableInstanceModel *self) {
  return self->QQmlTableInstanceModel::poolSize();
}

//  QQmlIncubator::Status QQmlTableInstanceModel::incubationStatus(int index)
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_own_ZN22QQmlTableInstanceModel16incubationStatusEi(
    QQmlTableInstanceModel *self,
    int index) {
  return self->QQmlTableInstanceModel::incubationStatus(index);
}

//  QVariant QQmlTableInstanceModel::variantValue(int a0, const QString &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN22QQmlTableInstanceModel12variantValueEiRK7QString(
    QQmlTableInstanceModel *self,
    int a0,
    const QString *a1) {
  return new QVariant(self->QQmlTableInstanceModel::variantValue(a0, *a1));
}

//  int QQmlTableInstanceModel::indexOf(QObject *a0, QObject *a1) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QQmlTableInstanceModel7indexOfEP7QObjectS1_(
    const QQmlTableInstanceModel *self,
    QObject *a0,
    QObject *a1) {
  return self->QQmlTableInstanceModel::indexOf(a0, a1);
}

#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_table_model)
