//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlabstractdelegatecomponent_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlabstractdelegatecomponent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlAbstractDelegateComponent that Python can take functions over in. Every QQmlAbstractDelegateComponent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_delegate_model)
typedef void * (*CuteQQmlAbstractDelegateComponentCall0)(const void *, QQmlAdaptorModel *, int, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef QString * (*CuteQQmlAbstractDelegateComponentCall1)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
typedef void * (*CuteQQmlAbstractDelegateComponentCall2)(const void *, QQmlContext *, int *);
typedef void * (*CuteQQmlAbstractDelegateComponentCall3)(const void *, QQmlContext *, int *);
typedef void (*CuteQQmlAbstractDelegateComponentCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractDelegateComponentCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractDelegateComponentCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractDelegateComponentCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractDelegateComponentCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractDelegateComponentCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractDelegateComponentCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractDelegateComponentCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlAbstractDelegateComponent : public QQmlAbstractDelegateComponent {
public:
  using QQmlAbstractDelegateComponent::QQmlAbstractDelegateComponent;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK29QQmlAbstractDelegateComponent8delegateEP16QQmlAdaptorModelii")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK29QQmlAbstractDelegateComponent4roleEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN13QQmlComponent6createEP11QQmlContext")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQmlComponent11beginCreateEP11QQmlContext")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQmlComponent14completeCreateEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_delegate_model)
  //  QQmlComponent
  //      *QQmlAbstractDelegateComponent::delegate(QQmlAdaptorModel
  //      *adaptorModel, int row, int column) const
  QQmlComponent *delegate(
      QQmlAdaptorModel *adaptorModel,
      int row,
      int column) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall0 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall0>(taken[0]);
      void * given = call(this, adaptorModel, row, column, &handled);
      if (handled) return static_cast<QQmlComponent *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  QString QQmlAbstractDelegateComponent::role() const
  QString role() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall1 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(qml_delegate_model)

  //  QObject *QQmlComponent::create(QQmlContext *context)
  QObject *create(QQmlContext *context) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall2 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall2>(taken[2]);
      void * given = call(this, context, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlComponent::create(context);
  }

  //  QObject *QQmlComponent::beginCreate(QQmlContext *a0)
  QObject *beginCreate(QQmlContext *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall3 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall3>(taken[3]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlComponent::beginCreate(a0);
  }

  //  void QQmlComponent::completeCreate()
  void completeCreate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall4 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlComponent::completeCreate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall5 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall6 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall7 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall8 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall9 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall10 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlAbstractDelegateComponentCall11 call = reinterpret_cast<CuteQQmlAbstractDelegateComponentCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlAbstractDelegateComponent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQmlAbstractDelegateComponent10metaObjectEv(
    const QQmlAbstractDelegateComponent *self) {
  return self->metaObject();
}

//  QString QQmlAbstractDelegateComponent::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQmlAbstractDelegateComponent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlAbstractDelegateComponent::tr(s, c, n));
}

//  void QQmlAbstractDelegateComponent::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlAbstractDelegateComponent24qt_qmlMarker_uncreatableEv(
    QQmlAbstractDelegateComponent *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQmlAbstractDelegateComponent::~QQmlAbstractDelegateComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlAbstractDelegateComponentD1Ev(
    QQmlAbstractDelegateComponent *self) {
  delete self;
}

//  QQmlComponent *QQmlAbstractDelegateComponent::delegate(QQmlAdaptorModel
//      *adaptorModel, int row, int column) const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK29QQmlAbstractDelegateComponent8delegateEP16QQmlAdaptorModelii(
    const QQmlAbstractDelegateComponent *self,
    QQmlAdaptorModel *adaptorModel,
    int row,
    int column) {
  return self->delegate(adaptorModel, row, column);
}

//  QString QQmlAbstractDelegateComponent::role() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QQmlAbstractDelegateComponent4roleEv(
    const QQmlAbstractDelegateComponent *self) {
  return new QString(self->role());
}

//  QVariant QQmlAbstractDelegateComponent::value(QQmlAdaptorModel
//      *adaptorModel, int row, int column, const QString &role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK29QQmlAbstractDelegateComponent5valueEP16QQmlAdaptorModeliiRK7QString(
    const QQmlAbstractDelegateComponent *self,
    QQmlAdaptorModel *adaptorModel,
    int row,
    int column,
    const QString *role) {
  return new QVariant(self->value(adaptorModel, row, column, *role));
}

//  a Python function taken by a CuteQQmlAbstractDelegateComponent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlAbstractDelegateComponent(
    QQmlAbstractDelegateComponent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlAbstractDelegateComponent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_delegate_model)
