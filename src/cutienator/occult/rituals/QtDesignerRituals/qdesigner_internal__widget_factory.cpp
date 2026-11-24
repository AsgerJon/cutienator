//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/widgetfactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/widgetfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A qdesigner_internal::WidgetFactory that Python can take functions over in. Every qdesigner_internal::WidgetFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*Cuteqdesigner_internal_WidgetFactoryCall0)(const void *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_WidgetFactoryCall1)(const void *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_WidgetFactoryCall2)(const void *, const QString *, QWidget *, int *);
typedef void * (*Cuteqdesigner_internal_WidgetFactoryCall3)(const void *, QWidget *, QLayout *, int, int *);
typedef bool (*Cuteqdesigner_internal_WidgetFactoryCall4)(const void *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_WidgetFactoryCall5)(const void *, QObject *, int *);
typedef void * (*Cuteqdesigner_internal_WidgetFactoryCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_WidgetFactoryCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_WidgetFactoryCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetFactoryCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetFactoryCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetFactoryCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetFactoryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_WidgetFactoryCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_WidgetFactory : public qdesigner_internal::WidgetFactory {
public:
  using qdesigner_internal::WidgetFactory::WidgetFactory;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface17containerOfWidgetEP7QWidget")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface17widgetOfContainerEP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface12createWidgetERK7QStringP7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface12createLayoutEP7QWidgetP7QLayouti")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerWidgetFactoryInterface19isPassiveInteractorEP7QWidget")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface10initializeEP7QObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface4coreEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QWidget *qdesigner_internal::WidgetFactory::containerOfWidget(QWidget
  //      *widget) const
  QWidget *containerOfWidget(QWidget *widget) const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall0 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall0>(taken[0]);
      void * given = call(this, widget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return qdesigner_internal::WidgetFactory::containerOfWidget(widget);
  }

  //  QWidget *qdesigner_internal::WidgetFactory::widgetOfContainer(QWidget
  //      *widget) const
  QWidget *widgetOfContainer(QWidget *widget) const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall1 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall1>(taken[1]);
      void * given = call(this, widget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return qdesigner_internal::WidgetFactory::widgetOfContainer(widget);
  }

  //  QWidget *qdesigner_internal::WidgetFactory::createWidget(const
  //      QString &className, QWidget *parentWidget) const
  QWidget *createWidget(
      const QString &className,
      QWidget *parentWidget) const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall2 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall2>(taken[2]);
      void * given = call(this, &className, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return qdesigner_internal::WidgetFactory::createWidget(className, parentWidget);
  }

  //  QLayout *qdesigner_internal::WidgetFactory::createLayout(QWidget
  //      *widget, QLayout *layout, int type) const
  QLayout *createLayout(
      QWidget *widget,
      QLayout *layout,
      int type) const override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall3 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall3>(taken[3]);
      void * given = call(this, widget, layout, type, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return qdesigner_internal::WidgetFactory::createLayout(widget, layout, type);
  }

  //  bool qdesigner_internal::WidgetFactory::isPassiveInteractor(QWidget
  //      *widget)
  bool isPassiveInteractor(QWidget *widget) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall4 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall4>(taken[4]);
      bool given = call(this, widget, &handled);
      if (handled) return given;
    }
    return qdesigner_internal::WidgetFactory::isPassiveInteractor(widget);
  }

  //  void qdesigner_internal::WidgetFactory::initialize(QObject *object)
  //      const
  void initialize(QObject *object) const override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall5 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall5>(taken[5]);
      call(this, object, &handled);
      if (handled) return;
    }
    qdesigner_internal::WidgetFactory::initialize(object);
  }

  //  QDesignerFormEditorInterface
  //      *qdesigner_internal::WidgetFactory::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall6 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return qdesigner_internal::WidgetFactory::core();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall7 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall8 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall9 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall10 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall11 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall12 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_WidgetFactoryCall13 call = reinterpret_cast<Cuteqdesigner_internal_WidgetFactoryCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::WidgetFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal13WidgetFactory10metaObjectEv(
    const qdesigner_internal::WidgetFactory *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::WidgetFactory::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal13WidgetFactory2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::WidgetFactory::tr(s, c, n));
}

//  QString qdesigner_internal::WidgetFactory::classNameOf(QDesignerFormEdito
//      rInterface *core, const QObject *o)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal13WidgetFactory11classNameOfEP28QDesignerFormEditorInterfacePK7QObject(
    QDesignerFormEditorInterface *core,
    const QObject *o) {
  return new QString(
      qdesigner_internal::WidgetFactory::classNameOf(
          core,
          o));
}

//  bool qdesigner_internal::WidgetFactory::isFormEditorObject(const QObject
//      *o)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal13WidgetFactory18isFormEditorObjectEPK7QObject(
    const QObject *o) {
  return qdesigner_internal::WidgetFactory::isFormEditorObject(o);
}

//  a Python function taken by a Cuteqdesigner_internal_WidgetFactory, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_WidgetFactory(
    qdesigner_internal::WidgetFactory *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_WidgetFactory *>(self)->take(key, call);
}

//  QWidget *qdesigner_internal::WidgetFactory::containerOfWidget(QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK18qdesigner_internal13WidgetFactory17containerOfWidgetEP7QWidget(
    const qdesigner_internal::WidgetFactory *self,
    QWidget *widget) {
  return self->qdesigner_internal::WidgetFactory::containerOfWidget(widget);
}

//  QWidget *qdesigner_internal::WidgetFactory::widgetOfContainer(QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK18qdesigner_internal13WidgetFactory17widgetOfContainerEP7QWidget(
    const qdesigner_internal::WidgetFactory *self,
    QWidget *widget) {
  return self->qdesigner_internal::WidgetFactory::widgetOfContainer(widget);
}

//  QWidget *qdesigner_internal::WidgetFactory::createWidget(const QString
//      &className, QWidget *parentWidget) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK18qdesigner_internal13WidgetFactory12createWidgetERK7QStringP7QWidget(
    const qdesigner_internal::WidgetFactory *self,
    const QString *className,
    QWidget *parentWidget) {
  return self->qdesigner_internal::WidgetFactory::createWidget(
      *className,
      parentWidget);
}

//  QLayout *qdesigner_internal::WidgetFactory::createLayout(QWidget *widget,
//      QLayout *layout, int type) const
extern "C" Q_DECL_EXPORT
QLayout *ritual_own_ZNK18qdesigner_internal13WidgetFactory12createLayoutEP7QWidgetP7QLayouti(
    const qdesigner_internal::WidgetFactory *self,
    QWidget *widget,
    QLayout *layout,
    int type) {
  return self->qdesigner_internal::WidgetFactory::createLayout(
      widget,
      layout,
      type);
}

//  bool qdesigner_internal::WidgetFactory::isPassiveInteractor(QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal13WidgetFactory19isPassiveInteractorEP7QWidget(
    qdesigner_internal::WidgetFactory *self,
    QWidget *widget) {
  return self->qdesigner_internal::WidgetFactory::isPassiveInteractor(
      widget);
}

//  void qdesigner_internal::WidgetFactory::initialize(QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18qdesigner_internal13WidgetFactory10initializeEP7QObject(
    const qdesigner_internal::WidgetFactory *self,
    QObject *object) {
  self->qdesigner_internal::WidgetFactory::initialize(object);
}

//  QDesignerFormEditorInterface *qdesigner_internal::WidgetFactory::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_own_ZNK18qdesigner_internal13WidgetFactory4coreEv(
    const qdesigner_internal::WidgetFactory *self) {
  return self->qdesigner_internal::WidgetFactory::core();
}
