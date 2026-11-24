//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlDelegateModel that Python can take functions over in. Every QQmlDelegateModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelCall1)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQmlDelegateModelCall2)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef bool (*CuteQQmlDelegateModelCall3)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef void * (*CuteQQmlDelegateModelCall4)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQmlDelegateModelCall5)(const void *, QObject *, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelCall6)(const void *, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef const QVariant * (*CuteQQmlDelegateModelCall7)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQmlDelegateModelCall8)(const void *, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelCall9)(const void *, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQmlDelegateModelCall10)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQmlDelegateModelCall11)(const void *, QObject *, QObject *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef void * (*CuteQQmlDelegateModelCall12)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
typedef bool (*CuteQQmlDelegateModelCall13)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_object_model)
typedef bool (*CuteQQmlDelegateModelCall14)(const void *, int, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelegateModelCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDelegateModel : public QQmlDelegateModel {
public:
  using QQmlDelegateModel::QQmlDelegateModel;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel5countEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel7isValidEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel6objectEiN13QQmlIncubator14IncubationModeE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel7releaseEP7QObjectNS_12ReusableFlagE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel6cancelEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel12variantValueEiRK7QString")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel16incubationStatusEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel22drainReusableItemsPoolEi")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel8poolSizeEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel7indexOfEP7QObjectS1_")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel17abstractItemModelEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel19setRequiredPropertyEiRK7QStringRK8QVariant")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModel::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDelegateModelCall0 call = reinterpret_cast<CuteQQmlDelegateModelCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlDelegateModel::classBegin();
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModel::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDelegateModelCall1 call = reinterpret_cast<CuteQQmlDelegateModelCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlDelegateModel::componentComplete();
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  int QQmlDelegateModel::count() const
  int count() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDelegateModelCall2 call = reinterpret_cast<CuteQQmlDelegateModelCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlDelegateModel::count();
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  bool QQmlDelegateModel::isValid() const
  bool isValid() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDelegateModelCall3 call = reinterpret_cast<CuteQQmlDelegateModelCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlDelegateModel::isValid();
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  QObject *QQmlDelegateModel::object(int index,
  //      QQmlIncubator::IncubationMode incubationMode)
  QObject *object(
      int index,
      QQmlIncubator::IncubationMode incubationMode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDelegateModelCall4 call = reinterpret_cast<CuteQQmlDelegateModelCall4>(taken[4]);
      void * given = call(this, index, static_cast<int>(incubationMode), &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlDelegateModel::object(index, incubationMode);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  ReleaseFlags QQmlDelegateModel::release(QObject *object, ReusableFlag
  //      reusableFlag)
  QQmlInstanceModel::ReleaseFlags release(
      QObject *object,
      QQmlInstanceModel::ReusableFlag reusableFlag) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlDelegateModelCall5 call = reinterpret_cast<CuteQQmlDelegateModelCall5>(taken[5]);
      int given = call(this, object, static_cast<int>(reusableFlag), &handled);
      if (handled) return QFlags<QQmlInstanceModel::ReleaseFlag>::fromInt(given);
    }
    return QQmlDelegateModel::release(object, reusableFlag);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModel::cancel(int index)
  void cancel(int index) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlDelegateModelCall6 call = reinterpret_cast<CuteQQmlDelegateModelCall6>(taken[6]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlDelegateModel::cancel(index);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  QVariant QQmlDelegateModel::variantValue(int index, const QString
  //      &role)
  QVariant variantValue(int index, const QString &role) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlDelegateModelCall7 call = reinterpret_cast<CuteQQmlDelegateModelCall7>(taken[7]);
      const QVariant * given = call(this, index, &role, &handled);
      if (handled && given) return *given;
    }
    return QQmlDelegateModel::variantValue(index, role);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  QQmlIncubator::Status QQmlDelegateModel::incubationStatus(int index)
  QQmlIncubator::Status incubationStatus(int index) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlDelegateModelCall8 call = reinterpret_cast<CuteQQmlDelegateModelCall8>(taken[8]);
      int given = call(this, index, &handled);
      if (handled) return static_cast<QQmlIncubator::Status>(given);
    }
    return QQmlDelegateModel::incubationStatus(index);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModel::drainReusableItemsPool(int maxPoolTime)
  void drainReusableItemsPool(int maxPoolTime) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlDelegateModelCall9 call = reinterpret_cast<CuteQQmlDelegateModelCall9>(taken[9]);
      call(this, maxPoolTime, &handled);
      if (handled) return;
    }
    QQmlDelegateModel::drainReusableItemsPool(maxPoolTime);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  int QQmlDelegateModel::poolSize()
  int poolSize() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlDelegateModelCall10 call = reinterpret_cast<CuteQQmlDelegateModelCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlDelegateModel::poolSize();
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  int QQmlDelegateModel::indexOf(QObject *object, QObject
  //      *objectContext) const
  int indexOf(QObject *object, QObject *objectContext) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlDelegateModelCall11 call = reinterpret_cast<CuteQQmlDelegateModelCall11>(taken[11]);
      int given = call(this, object, objectContext, &handled);
      if (handled) return given;
    }
    return QQmlDelegateModel::indexOf(object, objectContext);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  const QAbstractItemModel *QQmlDelegateModel::abstractItemModel()
  //      const
  const QAbstractItemModel *abstractItemModel() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlDelegateModelCall12 call = reinterpret_cast<CuteQQmlDelegateModelCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QAbstractItemModel *>(given);
    }
    return QQmlDelegateModel::abstractItemModel();
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
  //  bool QQmlDelegateModel::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlDelegateModelCall13 call = reinterpret_cast<CuteQQmlDelegateModelCall13>(taken[13]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlDelegateModel::event(a0);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(qml_object_model)
  //  bool QQmlInstanceModel::setRequiredProperty(int index, const QString
  //      &name, const QVariant &value)
  bool setRequiredProperty(
      int index,
      const QString &name,
      const QVariant &value) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlDelegateModelCall14 call = reinterpret_cast<CuteQQmlDelegateModelCall14>(taken[14]);
      bool given = call(this, index, &name, &value, &handled);
      if (handled) return given;
    }
    return QQmlInstanceModel::setRequiredProperty(index, name, value);
  }
#endif  // QT_CONFIG(qml_object_model)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlDelegateModelCall15 call = reinterpret_cast<CuteQQmlDelegateModelCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlDelegateModelCall16 call = reinterpret_cast<CuteQQmlDelegateModelCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlDelegateModelCall17 call = reinterpret_cast<CuteQQmlDelegateModelCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlDelegateModelCall18 call = reinterpret_cast<CuteQQmlDelegateModelCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlDelegateModelCall19 call = reinterpret_cast<CuteQQmlDelegateModelCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlDelegateModelCall20 call = reinterpret_cast<CuteQQmlDelegateModelCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDelegateModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlDelegateModel10metaObjectEv(
    const QQmlDelegateModel *self) {
  return self->metaObject();
}

//  QString QQmlDelegateModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQmlDelegateModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDelegateModel::tr(s, c, n));
}

//  QQmlDelegateModelPrivate *QQmlDelegateModel::d_func()
extern "C" Q_DECL_EXPORT
QQmlDelegateModelPrivate *ritual_ZN17QQmlDelegateModel6d_funcEv(
    QQmlDelegateModel *self) {
  return self->d_func();
}

//  const QQmlDelegateModelPrivate *QQmlDelegateModel::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlDelegateModelPrivate *ritual_ZNK17QQmlDelegateModel6d_funcEv(
    const QQmlDelegateModel *self) {
  return self->d_func();
}

//  void QQmlDelegateModel::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel21qt_qmlMarker_attachedEv(
    QQmlDelegateModel *self) {
  self->qt_qmlMarker_attached();
}

//  QQmlDelegateModel::QQmlDelegateModel()
extern "C" Q_DECL_EXPORT
QQmlDelegateModel *ritual_ZN17QQmlDelegateModelC1Ev() {
  return new CuteQQmlDelegateModel();
}

//  QQmlDelegateModel::QQmlDelegateModel(QQmlContext *a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlDelegateModel *ritual_ZN17QQmlDelegateModelC1EP11QQmlContextP7QObject(
    QQmlContext *a0,
    QObject *parent) {
  return new CuteQQmlDelegateModel(a0, parent);
}

//  QQmlDelegateModel::~QQmlDelegateModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModelD1Ev(QQmlDelegateModel *self) {
  delete self;
}

//  void QQmlDelegateModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel10classBeginEv(QQmlDelegateModel *self) {
  self->classBegin();
}

//  void QQmlDelegateModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel17componentCompleteEv(
    QQmlDelegateModel *self) {
  self->componentComplete();
}

//  QVariant QQmlDelegateModel::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQmlDelegateModel5modelEv(
    const QQmlDelegateModel *self) {
  return new QVariant(self->model());
}

//  void QQmlDelegateModel::setModel(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel8setModelERK8QVariant(
    QQmlDelegateModel *self,
    const QVariant *a0) {
  self->setModel(*a0);
}

//  QQmlComponent *QQmlDelegateModel::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK17QQmlDelegateModel8delegateEv(
    const QQmlDelegateModel *self) {
  return self->delegate();
}

//  void QQmlDelegateModel::setDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel11setDelegateEP13QQmlComponent(
    QQmlDelegateModel *self,
    QQmlComponent *a0) {
  self->setDelegate(a0);
}

//  QVariant QQmlDelegateModel::rootIndex() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQmlDelegateModel9rootIndexEv(
    const QQmlDelegateModel *self) {
  return new QVariant(self->rootIndex());
}

//  void QQmlDelegateModel::setRootIndex(const QVariant &root)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel12setRootIndexERK8QVariant(
    QQmlDelegateModel *self,
    const QVariant *root) {
  self->setRootIndex(*root);
}

//  DelegateModelAccess QQmlDelegateModel::delegateModelAccess() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel::DelegateModelAccess ritual_ZNK17QQmlDelegateModel19delegateModelAccessEv(
    const QQmlDelegateModel *self) {
  return self->delegateModelAccess();
}

//  void QQmlDelegateModel::setDelegateModelAccess(DelegateModelAccess
//      delegateModelAccess)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel22setDelegateModelAccessENS_19DelegateModelAccessE(
    QQmlDelegateModel *self,
    QQmlDelegateModel::DelegateModelAccess delegateModelAccess) {
  self->setDelegateModelAccess(delegateModelAccess);
}

//  QVariant QQmlDelegateModel::modelIndex(int idx) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQmlDelegateModel10modelIndexEi(
    const QQmlDelegateModel *self,
    int idx) {
  return new QVariant(self->modelIndex(idx));
}

//  QVariant QQmlDelegateModel::parentModelIndex() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQmlDelegateModel16parentModelIndexEv(
    const QQmlDelegateModel *self) {
  return new QVariant(self->parentModelIndex());
}

//  int QQmlDelegateModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlDelegateModel5countEv(const QQmlDelegateModel *self) {
  return self->count();
}

//  bool QQmlDelegateModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlDelegateModel7isValidEv(const QQmlDelegateModel *self) {
  return self->isValid();
}

//  QObject *QQmlDelegateModel::object(int index,
//      QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlDelegateModel6objectEiN13QQmlIncubator14IncubationModeE(
    QQmlDelegateModel *self,
    int index,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->object(index, incubationMode);
}

//  ReleaseFlags QQmlDelegateModel::release(QObject *object, ReusableFlag
//      reusableFlag)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQmlDelegateModel7releaseEP7QObjectN17QQmlInstanceModel12ReusableFlagE(
    QQmlDelegateModel *self,
    QObject *object,
    QQmlInstanceModel::ReusableFlag reusableFlag) {
  return static_cast<int>(self->release(object, reusableFlag).toInt());
}

//  void QQmlDelegateModel::cancel(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel6cancelEi(
    QQmlDelegateModel *self,
    int index) {
  self->cancel(index);
}

//  QVariant QQmlDelegateModel::variantValue(int index, const QString &role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlDelegateModel12variantValueEiRK7QString(
    QQmlDelegateModel *self,
    int index,
    const QString *role) {
  return new QVariant(self->variantValue(index, *role));
}

//  void QQmlDelegateModel::setWatchedRoles(const QList<QByteArray> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel15setWatchedRolesERK5QListI10QByteArrayE(
    QQmlDelegateModel *self,
    const QList<QByteArray> *roles) {
  self->setWatchedRoles(*roles);
}

//  QQmlIncubator::Status QQmlDelegateModel::incubationStatus(int index)
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_ZN17QQmlDelegateModel16incubationStatusEi(
    QQmlDelegateModel *self,
    int index) {
  return self->incubationStatus(index);
}

//  void QQmlDelegateModel::drainReusableItemsPool(int maxPoolTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel22drainReusableItemsPoolEi(
    QQmlDelegateModel *self,
    int maxPoolTime) {
  self->drainReusableItemsPool(maxPoolTime);
}

//  int QQmlDelegateModel::poolSize()
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQmlDelegateModel8poolSizeEv(QQmlDelegateModel *self) {
  return self->poolSize();
}

//  int QQmlDelegateModel::indexOf(QObject *object, QObject *objectContext)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlDelegateModel7indexOfEP7QObjectS1_(
    const QQmlDelegateModel *self,
    QObject *object,
    QObject *objectContext) {
  return self->indexOf(object, objectContext);
}

//  QString QQmlDelegateModel::filterGroup() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQmlDelegateModel11filterGroupEv(
    const QQmlDelegateModel *self) {
  return new QString(self->filterGroup());
}

//  void QQmlDelegateModel::setFilterGroup(const QString &group)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel14setFilterGroupERK7QString(
    QQmlDelegateModel *self,
    const QString *group) {
  self->setFilterGroup(*group);
}

//  void QQmlDelegateModel::resetFilterGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel16resetFilterGroupEv(
    QQmlDelegateModel *self) {
  self->resetFilterGroup();
}

//  QQmlDelegateModelGroup *QQmlDelegateModel::items()
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroup *ritual_ZN17QQmlDelegateModel5itemsEv(
    QQmlDelegateModel *self) {
  return self->items();
}

//  QQmlDelegateModelGroup *QQmlDelegateModel::persistedItems()
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroup *ritual_ZN17QQmlDelegateModel14persistedItemsEv(
    QQmlDelegateModel *self) {
  return self->persistedItems();
}

//  QObject *QQmlDelegateModel::parts()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlDelegateModel5partsEv(QQmlDelegateModel *self) {
  return self->parts();
}

//  const QAbstractItemModel *QQmlDelegateModel::abstractItemModel() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK17QQmlDelegateModel17abstractItemModelEv(
    const QQmlDelegateModel *self) {
  return self->abstractItemModel();
}

//  bool QQmlDelegateModel::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlDelegateModel5eventEP6QEvent(
    QQmlDelegateModel *self,
    QEvent *a0) {
  return self->event(a0);
}

//  QQmlDelegateModelAttached
//      *QQmlDelegateModel::qmlAttachedProperties(QObject *obj)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelAttached *ritual_ZN17QQmlDelegateModel21qmlAttachedPropertiesEP7QObject(
    QObject *obj) {
  return QQmlDelegateModel::qmlAttachedProperties(obj);
}

//  void QQmlDelegateModel::_q_itemsInserted(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel16_q_itemsInsertedEii(
    QQmlDelegateModel *self,
    int index,
    int count) {
  self->_q_itemsInserted(index, count);
}

//  void QQmlDelegateModel::_q_itemsRemoved(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel15_q_itemsRemovedEii(
    QQmlDelegateModel *self,
    int index,
    int count) {
  self->_q_itemsRemoved(index, count);
}

//  void QQmlDelegateModel::_q_itemsMoved(int from, int to, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel13_q_itemsMovedEiii(
    QQmlDelegateModel *self,
    int from,
    int to,
    int count) {
  self->_q_itemsMoved(from, to, count);
}

//  void QQmlDelegateModel::_q_modelAboutToBeReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel22_q_modelAboutToBeResetEv(
    QQmlDelegateModel *self) {
  self->_q_modelAboutToBeReset();
}

//  void QQmlDelegateModel::_q_rowsInserted(const QModelIndex &a0, int a1,
//      int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel15_q_rowsInsertedERK11QModelIndexii(
    QQmlDelegateModel *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->_q_rowsInserted(*a0, a1, a2);
}

//  void QQmlDelegateModel::_q_columnsInserted(const QModelIndex &a0, int a1,
//      int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel18_q_columnsInsertedERK11QModelIndexii(
    QQmlDelegateModel *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->_q_columnsInserted(*a0, a1, a2);
}

//  void QQmlDelegateModel::_q_columnsRemoved(const QModelIndex &a0, int a1,
//      int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel17_q_columnsRemovedERK11QModelIndexii(
    QQmlDelegateModel *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->_q_columnsRemoved(*a0, a1, a2);
}

//  void QQmlDelegateModel::_q_columnsMoved(const QModelIndex &a0, int a1,
//      int a2, const QModelIndex &a3, int a4)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel15_q_columnsMovedERK11QModelIndexiiS2_i(
    QQmlDelegateModel *self,
    const QModelIndex *a0,
    int a1,
    int a2,
    const QModelIndex *a3,
    int a4) {
  self->_q_columnsMoved(*a0, a1, a2, *a3, a4);
}

//  void QQmlDelegateModel::_q_rowsAboutToBeRemoved(const QModelIndex
//      &parent, int begin, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel23_q_rowsAboutToBeRemovedERK11QModelIndexii(
    QQmlDelegateModel *self,
    const QModelIndex *parent,
    int begin,
    int end) {
  self->_q_rowsAboutToBeRemoved(*parent, begin, end);
}

//  void QQmlDelegateModel::_q_rowsRemoved(const QModelIndex &a0, int a1, int
//      a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel14_q_rowsRemovedERK11QModelIndexii(
    QQmlDelegateModel *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->_q_rowsRemoved(*a0, a1, a2);
}

//  void QQmlDelegateModel::_q_rowsMoved(const QModelIndex &a0, int a1, int
//      a2, const QModelIndex &a3, int a4)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel12_q_rowsMovedERK11QModelIndexiiS2_i(
    QQmlDelegateModel *self,
    const QModelIndex *a0,
    int a1,
    int a2,
    const QModelIndex *a3,
    int a4) {
  self->_q_rowsMoved(*a0, a1, a2, *a3, a4);
}

//  void QQmlDelegateModel::_q_layoutChanged(const
//      QList<QPersistentModelIndex> &a0,
//      QAbstractItemModel::LayoutChangeHint a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel16_q_layoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QQmlDelegateModel *self,
    const QList<QPersistentModelIndex> *a0,
    QAbstractItemModel::LayoutChangeHint a1) {
  self->_q_layoutChanged(*a0, a1);
}

//  void QQmlDelegateModel::handleModelReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlDelegateModel16handleModelResetEv(
    QQmlDelegateModel *self) {
  self->handleModelReset();
}

//  bool QQmlDelegateModel::isDescendantOf(const QPersistentModelIndex &desc,
//      const QList<QPersistentModelIndex> &parents) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlDelegateModel14isDescendantOfERK21QPersistentModelIndexRK5QListIS0_E(
    const QQmlDelegateModel *self,
    const QPersistentModelIndex *desc,
    const QList<QPersistentModelIndex> *parents) {
  return self->isDescendantOf(*desc, *parents);
}

//  QQmlDelegateModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlDelegateModel_QQmlParserStatus(
    QQmlDelegateModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlDelegateModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDelegateModel(
    QQmlDelegateModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDelegateModel *>(self)->take(key, call);
}

//  void QQmlDelegateModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlDelegateModel10classBeginEv(
    QQmlDelegateModel *self) {
  self->QQmlDelegateModel::classBegin();
}

//  void QQmlDelegateModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlDelegateModel17componentCompleteEv(
    QQmlDelegateModel *self) {
  self->QQmlDelegateModel::componentComplete();
}

//  int QQmlDelegateModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QQmlDelegateModel5countEv(
    const QQmlDelegateModel *self) {
  return self->QQmlDelegateModel::count();
}

//  bool QQmlDelegateModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QQmlDelegateModel7isValidEv(
    const QQmlDelegateModel *self) {
  return self->QQmlDelegateModel::isValid();
}

//  QObject *QQmlDelegateModel::object(int index,
//      QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN17QQmlDelegateModel6objectEiN13QQmlIncubator14IncubationModeE(
    QQmlDelegateModel *self,
    int index,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->QQmlDelegateModel::object(index, incubationMode);
}

//  ReleaseFlags QQmlDelegateModel::release(QObject *object, ReusableFlag
//      reusableFlag)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN17QQmlDelegateModel7releaseEP7QObjectN17QQmlInstanceModel12ReusableFlagE(
    QQmlDelegateModel *self,
    QObject *object,
    QQmlInstanceModel::ReusableFlag reusableFlag) {
  return static_cast<int>(
      self->QQmlDelegateModel::release(
          object,
          reusableFlag).toInt());
}

//  void QQmlDelegateModel::cancel(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlDelegateModel6cancelEi(
    QQmlDelegateModel *self,
    int index) {
  self->QQmlDelegateModel::cancel(index);
}

//  QVariant QQmlDelegateModel::variantValue(int index, const QString &role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN17QQmlDelegateModel12variantValueEiRK7QString(
    QQmlDelegateModel *self,
    int index,
    const QString *role) {
  return new QVariant(self->QQmlDelegateModel::variantValue(index, *role));
}

//  QQmlIncubator::Status QQmlDelegateModel::incubationStatus(int index)
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_own_ZN17QQmlDelegateModel16incubationStatusEi(
    QQmlDelegateModel *self,
    int index) {
  return self->QQmlDelegateModel::incubationStatus(index);
}

//  void QQmlDelegateModel::drainReusableItemsPool(int maxPoolTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlDelegateModel22drainReusableItemsPoolEi(
    QQmlDelegateModel *self,
    int maxPoolTime) {
  self->QQmlDelegateModel::drainReusableItemsPool(maxPoolTime);
}

//  int QQmlDelegateModel::poolSize()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN17QQmlDelegateModel8poolSizeEv(QQmlDelegateModel *self) {
  return self->QQmlDelegateModel::poolSize();
}

//  int QQmlDelegateModel::indexOf(QObject *object, QObject *objectContext)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QQmlDelegateModel7indexOfEP7QObjectS1_(
    const QQmlDelegateModel *self,
    QObject *object,
    QObject *objectContext) {
  return self->QQmlDelegateModel::indexOf(object, objectContext);
}

//  const QAbstractItemModel *QQmlDelegateModel::abstractItemModel() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_own_ZNK17QQmlDelegateModel17abstractItemModelEv(
    const QQmlDelegateModel *self) {
  return self->QQmlDelegateModel::abstractItemModel();
}

//  bool QQmlDelegateModel::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQmlDelegateModel5eventEP6QEvent(
    QQmlDelegateModel *self,
    QEvent *a0) {
  return self->QQmlDelegateModel::event(a0);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
