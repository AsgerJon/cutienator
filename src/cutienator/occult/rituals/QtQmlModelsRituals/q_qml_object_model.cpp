//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlobjectmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_object_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlobjectmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlObjectModel that Python can take functions over in. Every QQmlObjectModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_object_model)
typedef int (*CuteQQmlObjectModelCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef bool (*CuteQQmlObjectModelCall1)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void * (*CuteQQmlObjectModelCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef int (*CuteQQmlObjectModelCall3)(const void *, QObject *, int, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef const QVariant * (*CuteQQmlObjectModelCall4)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef int (*CuteQQmlObjectModelCall5)(const void *, int, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef int (*CuteQQmlObjectModelCall6)(const void *, QObject *, QObject *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQmlObjectModelCall7)(const void *, int, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQmlObjectModelCall8)(const void *, int, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef int (*CuteQQmlObjectModelCall9)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void * (*CuteQQmlObjectModelCall10)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef bool (*CuteQQmlObjectModelCall11)(const void *, int, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlObjectModelCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlObjectModelCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlObjectModelCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlObjectModelCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlObjectModelCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlObjectModelCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlObjectModelCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlObjectModel : public QQmlObjectModel {
public:
  using QQmlObjectModel::QQmlObjectModel;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel5countEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel7isValidEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel6objectEiN13QQmlIncubator14IncubationModeE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel7releaseEP7QObjectNS_12ReusableFlagE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel12variantValueEiRK7QString")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel16incubationStatusEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel7indexOfEP7QObjectS1_")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel6cancelEi")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel22drainReusableItemsPoolEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel8poolSizeEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel17abstractItemModelEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel19setRequiredPropertyEiRK7QStringRK8QVariant")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_object_model)
  //  int QQmlObjectModel::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlObjectModelCall0 call = reinterpret_cast<CuteQQmlObjectModelCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlObjectModel::count();
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  bool QQmlObjectModel::isValid() const
  bool isValid() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlObjectModelCall1 call = reinterpret_cast<CuteQQmlObjectModelCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlObjectModel::isValid();
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  QObject *QQmlObjectModel::object(int index,
  //      QQmlIncubator::IncubationMode incubationMode)
  QObject *object(
      int index,
      QQmlIncubator::IncubationMode incubationMode) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlObjectModelCall2 call = reinterpret_cast<CuteQQmlObjectModelCall2>(taken[2]);
      void * given = call(this, index, static_cast<int>(incubationMode), &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlObjectModel::object(index, incubationMode);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  ReleaseFlags QQmlObjectModel::release(QObject *object, ReusableFlag
  //      reusable)
  QQmlInstanceModel::ReleaseFlags release(
      QObject *object,
      QQmlInstanceModel::ReusableFlag reusable) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlObjectModelCall3 call = reinterpret_cast<CuteQQmlObjectModelCall3>(taken[3]);
      int given = call(this, object, static_cast<int>(reusable), &handled);
      if (handled) return QFlags<QQmlInstanceModel::ReleaseFlag>::fromInt(given);
    }
    return QQmlObjectModel::release(object, reusable);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  QVariant QQmlObjectModel::variantValue(int index, const QString
  //      &role)
  QVariant variantValue(int index, const QString &role) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlObjectModelCall4 call = reinterpret_cast<CuteQQmlObjectModelCall4>(taken[4]);
      const QVariant * given = call(this, index, &role, &handled);
      if (handled && given) return *given;
    }
    return QQmlObjectModel::variantValue(index, role);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  QQmlIncubator::Status QQmlObjectModel::incubationStatus(int index)
  QQmlIncubator::Status incubationStatus(int index) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlObjectModelCall5 call = reinterpret_cast<CuteQQmlObjectModelCall5>(taken[5]);
      int given = call(this, index, &handled);
      if (handled) return static_cast<QQmlIncubator::Status>(given);
    }
    return QQmlObjectModel::incubationStatus(index);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  int QQmlObjectModel::indexOf(QObject *object, QObject *objectContext)
  //      const
  int indexOf(QObject *object, QObject *objectContext) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlObjectModelCall6 call = reinterpret_cast<CuteQQmlObjectModelCall6>(taken[6]);
      int given = call(this, object, objectContext, &handled);
      if (handled) return given;
    }
    return QQmlObjectModel::indexOf(object, objectContext);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  void QQmlInstanceModel::cancel(int a0)
  void cancel(int a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlObjectModelCall7 call = reinterpret_cast<CuteQQmlObjectModelCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlInstanceModel::cancel(a0);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  void QQmlInstanceModel::drainReusableItemsPool(int maxPoolTime)
  void drainReusableItemsPool(int maxPoolTime) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlObjectModelCall8 call = reinterpret_cast<CuteQQmlObjectModelCall8>(taken[8]);
      call(this, maxPoolTime, &handled);
      if (handled) return;
    }
    QQmlInstanceModel::drainReusableItemsPool(maxPoolTime);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  int QQmlInstanceModel::poolSize()
  int poolSize() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlObjectModelCall9 call = reinterpret_cast<CuteQQmlObjectModelCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlInstanceModel::poolSize();
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  const QAbstractItemModel *QQmlInstanceModel::abstractItemModel()
  //      const
  const QAbstractItemModel *abstractItemModel() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlObjectModelCall10 call = reinterpret_cast<CuteQQmlObjectModelCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QAbstractItemModel *>(given);
    }
    return QQmlInstanceModel::abstractItemModel();
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  bool QQmlInstanceModel::setRequiredProperty(int index, const QString
  //      &name, const QVariant &value)
  bool setRequiredProperty(
      int index,
      const QString &name,
      const QVariant &value) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlObjectModelCall11 call = reinterpret_cast<CuteQQmlObjectModelCall11>(taken[11]);
      bool given = call(this, index, &name, &value, &handled);
      if (handled) return given;
    }
    return QQmlInstanceModel::setRequiredProperty(index, name, value);
  }
#endif  // QT_CONFIG(qml_object_model)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlObjectModelCall12 call = reinterpret_cast<CuteQQmlObjectModelCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlObjectModelCall13 call = reinterpret_cast<CuteQQmlObjectModelCall13>(taken[13]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlObjectModelCall14 call = reinterpret_cast<CuteQQmlObjectModelCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlObjectModelCall15 call = reinterpret_cast<CuteQQmlObjectModelCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlObjectModelCall16 call = reinterpret_cast<CuteQQmlObjectModelCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlObjectModelCall17 call = reinterpret_cast<CuteQQmlObjectModelCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlObjectModelCall18 call = reinterpret_cast<CuteQQmlObjectModelCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlObjectModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlObjectModel10metaObjectEv(
    const QQmlObjectModel *self) {
  return self->metaObject();
}

//  QString QQmlObjectModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlObjectModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlObjectModel::tr(s, c, n));
}

//  void QQmlObjectModel::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlObjectModel21qt_qmlMarker_attachedEv(
    QQmlObjectModel *self) {
  self->qt_qmlMarker_attached();
}

//  QQmlObjectModel::QQmlObjectModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlObjectModel *ritual_ZN15QQmlObjectModelC1EP7QObject(QObject *parent) {
  return new CuteQQmlObjectModel(parent);
}

//  QQmlObjectModel::~QQmlObjectModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlObjectModelD1Ev(QQmlObjectModel *self) {
  delete self;
}

//  int QQmlObjectModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQmlObjectModel5countEv(const QQmlObjectModel *self) {
  return self->count();
}

//  bool QQmlObjectModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlObjectModel7isValidEv(const QQmlObjectModel *self) {
  return self->isValid();
}

//  QObject *QQmlObjectModel::object(int index, QQmlIncubator::IncubationMode
//      incubationMode)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN15QQmlObjectModel6objectEiN13QQmlIncubator14IncubationModeE(
    QQmlObjectModel *self,
    int index,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->object(index, incubationMode);
}

//  ReleaseFlags QQmlObjectModel::release(QObject *object, ReusableFlag
//      reusable)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlObjectModel7releaseEP7QObjectN17QQmlInstanceModel12ReusableFlagE(
    QQmlObjectModel *self,
    QObject *object,
    QQmlInstanceModel::ReusableFlag reusable) {
  return static_cast<int>(self->release(object, reusable).toInt());
}

//  QVariant QQmlObjectModel::variantValue(int index, const QString &role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QQmlObjectModel12variantValueEiRK7QString(
    QQmlObjectModel *self,
    int index,
    const QString *role) {
  return new QVariant(self->variantValue(index, *role));
}

//  void QQmlObjectModel::setWatchedRoles(const QList<QByteArray> &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlObjectModel15setWatchedRolesERK5QListI10QByteArrayE(
    QQmlObjectModel *self,
    const QList<QByteArray> *a0) {
  self->setWatchedRoles(*a0);
}

//  QQmlIncubator::Status QQmlObjectModel::incubationStatus(int index)
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_ZN15QQmlObjectModel16incubationStatusEi(
    QQmlObjectModel *self,
    int index) {
  return self->incubationStatus(index);
}

//  int QQmlObjectModel::indexOf(QObject *object, QObject *objectContext)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQmlObjectModel7indexOfEP7QObjectS1_(
    const QQmlObjectModel *self,
    QObject *object,
    QObject *objectContext) {
  return self->indexOf(object, objectContext);
}

//  QQmlObjectModelAttached *QQmlObjectModel::qmlAttachedProperties(QObject
//      *obj)
extern "C" Q_DECL_EXPORT
QQmlObjectModelAttached *ritual_ZN15QQmlObjectModel21qmlAttachedPropertiesEP7QObject(
    QObject *obj) {
  return QQmlObjectModel::qmlAttachedProperties(obj);
}

//  QObject *QQmlObjectModel::get(int index) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QQmlObjectModel3getEi(
    const QQmlObjectModel *self,
    int index) {
  return self->get(index);
}

//  void QQmlObjectModel::append(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlObjectModel6appendEP7QObject(
    QQmlObjectModel *self,
    QObject *object) {
  self->append(object);
}

//  void QQmlObjectModel::insert(int index, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlObjectModel6insertEiP7QObject(
    QQmlObjectModel *self,
    int index,
    QObject *object) {
  self->insert(index, object);
}

//  void QQmlObjectModel::move(int from, int to, int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlObjectModel4moveEiii(
    QQmlObjectModel *self,
    int from,
    int to,
    int n) {
  self->move(from, to, n);
}

//  void QQmlObjectModel::remove(int index, int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlObjectModel6removeEii(
    QQmlObjectModel *self,
    int index,
    int n) {
  self->remove(index, n);
}

//  void QQmlObjectModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlObjectModel5clearEv(QQmlObjectModel *self) {
  self->clear();
}

//  a Python function taken by a CuteQQmlObjectModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlObjectModel(
    QQmlObjectModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlObjectModel *>(self)->take(key, call);
}

//  int QQmlObjectModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QQmlObjectModel5countEv(const QQmlObjectModel *self) {
  return self->QQmlObjectModel::count();
}

//  bool QQmlObjectModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QQmlObjectModel7isValidEv(const QQmlObjectModel *self) {
  return self->QQmlObjectModel::isValid();
}

//  QObject *QQmlObjectModel::object(int index, QQmlIncubator::IncubationMode
//      incubationMode)
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN15QQmlObjectModel6objectEiN13QQmlIncubator14IncubationModeE(
    QQmlObjectModel *self,
    int index,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->QQmlObjectModel::object(index, incubationMode);
}

//  ReleaseFlags QQmlObjectModel::release(QObject *object, ReusableFlag
//      reusable)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN15QQmlObjectModel7releaseEP7QObjectN17QQmlInstanceModel12ReusableFlagE(
    QQmlObjectModel *self,
    QObject *object,
    QQmlInstanceModel::ReusableFlag reusable) {
  return static_cast<int>(
      self->QQmlObjectModel::release(
          object,
          reusable).toInt());
}

//  QVariant QQmlObjectModel::variantValue(int index, const QString &role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN15QQmlObjectModel12variantValueEiRK7QString(
    QQmlObjectModel *self,
    int index,
    const QString *role) {
  return new QVariant(self->QQmlObjectModel::variantValue(index, *role));
}

//  QQmlIncubator::Status QQmlObjectModel::incubationStatus(int index)
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_own_ZN15QQmlObjectModel16incubationStatusEi(
    QQmlObjectModel *self,
    int index) {
  return self->QQmlObjectModel::incubationStatus(index);
}

//  int QQmlObjectModel::indexOf(QObject *object, QObject *objectContext)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QQmlObjectModel7indexOfEP7QObjectS1_(
    const QQmlObjectModel *self,
    QObject *object,
    QObject *objectContext) {
  return self->QQmlObjectModel::indexOf(object, objectContext);
}

#endif  // QT_CONFIG(qml_object_model)
