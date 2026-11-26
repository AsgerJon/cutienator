//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractwidgetfactory.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerWidgetFactoryInterface that Python can take functions over in. Every QDesignerWidgetFactoryInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerWidgetFactoryInterfaceCall0)(const void *, int *);
typedef void * (*CuteQDesignerWidgetFactoryInterfaceCall1)(const void *, QWidget *, int *);
typedef void * (*CuteQDesignerWidgetFactoryInterfaceCall2)(const void *, QWidget *, int *);
typedef void * (*CuteQDesignerWidgetFactoryInterfaceCall3)(const void *, const QString *, QWidget *, int *);
typedef void * (*CuteQDesignerWidgetFactoryInterfaceCall4)(const void *, QWidget *, QLayout *, int, int *);
typedef bool (*CuteQDesignerWidgetFactoryInterfaceCall5)(const void *, QWidget *, int *);
typedef void (*CuteQDesignerWidgetFactoryInterfaceCall6)(const void *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerWidgetFactoryInterfaceCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerWidgetFactoryInterfaceCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetFactoryInterfaceCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetFactoryInterfaceCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetFactoryInterfaceCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetFactoryInterfaceCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetFactoryInterfaceCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerWidgetFactoryInterface : public QDesignerWidgetFactoryInterface {
public:
  using QDesignerWidgetFactoryInterface::QDesignerWidgetFactoryInterface;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface4coreEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface17containerOfWidgetEP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface17widgetOfContainerEP7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface12createWidgetERK7QStringP7QWidget")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface12createLayoutEP7QWidgetP7QLayouti")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerWidgetFactoryInterface19isPassiveInteractorEP7QWidget")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerWidgetFactoryInterface10initializeEP7QObject")) {
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

  //  QDesignerFormEditorInterface *QDesignerWidgetFactoryInterface::core()
  //      const
  QDesignerFormEditorInterface *core() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerWidgetFactoryInterfaceCall0 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return {};
  }

  //  QWidget *QDesignerWidgetFactoryInterface::containerOfWidget(QWidget
  //      *w) const
  QWidget *containerOfWidget(QWidget *w) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerWidgetFactoryInterfaceCall1 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall1>(taken[1]);
      void * given = call(this, w, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  QWidget *QDesignerWidgetFactoryInterface::widgetOfContainer(QWidget
  //      *w) const
  QWidget *widgetOfContainer(QWidget *w) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerWidgetFactoryInterfaceCall2 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall2>(taken[2]);
      void * given = call(this, w, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  QWidget *QDesignerWidgetFactoryInterface::createWidget(const QString
  //      &name, QWidget *parentWidget) const
  QWidget *createWidget(
      const QString &name,
      QWidget *parentWidget) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerWidgetFactoryInterfaceCall3 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall3>(taken[3]);
      void * given = call(this, &name, parentWidget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  QLayout *QDesignerWidgetFactoryInterface::createLayout(QWidget
  //      *widget, QLayout *layout, int type) const
  QLayout *createLayout(
      QWidget *widget,
      QLayout *layout,
      int type) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerWidgetFactoryInterfaceCall4 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall4>(taken[4]);
      void * given = call(this, widget, layout, type, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return {};
  }

  //  bool QDesignerWidgetFactoryInterface::isPassiveInteractor(QWidget
  //      *widget)
  bool isPassiveInteractor(QWidget *widget) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerWidgetFactoryInterfaceCall5 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall5>(taken[5]);
      bool given = call(this, widget, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerWidgetFactoryInterface::initialize(QObject *object)
  //      const
  void initialize(QObject *object) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerWidgetFactoryInterfaceCall6 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall6>(taken[6]);
      call(this, object, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerWidgetFactoryInterfaceCall7 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall7>(taken[7]);
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
      CuteQDesignerWidgetFactoryInterfaceCall8 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall8>(taken[8]);
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
      CuteQDesignerWidgetFactoryInterfaceCall9 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall9>(taken[9]);
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
      CuteQDesignerWidgetFactoryInterfaceCall10 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall10>(taken[10]);
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
      CuteQDesignerWidgetFactoryInterfaceCall11 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall11>(taken[11]);
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
      CuteQDesignerWidgetFactoryInterfaceCall12 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall12>(taken[12]);
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
      CuteQDesignerWidgetFactoryInterfaceCall13 call = reinterpret_cast<CuteQDesignerWidgetFactoryInterfaceCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerWidgetFactoryInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QDesignerWidgetFactoryInterface10metaObjectEv(
    const QDesignerWidgetFactoryInterface *self) {
  return self->metaObject();
}

//  void *QDesignerWidgetFactoryInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QDesignerWidgetFactoryInterface11qt_metacastEPKc(
    QDesignerWidgetFactoryInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerWidgetFactoryInterface::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QDesignerWidgetFactoryInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerWidgetFactoryInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerWidgetFactoryInterface::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QDesignerWidgetFactoryInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerWidgetFactoryInterface::tr(s, c, n));
}

//  QDesignerWidgetFactoryInterface::QDesignerWidgetFactoryInterface(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QDesignerWidgetFactoryInterface *ritual_ZN31QDesignerWidgetFactoryInterfaceC1EP7QObject(
    QObject *parent) {
  return new CuteQDesignerWidgetFactoryInterface(parent);
}

//  QDesignerWidgetFactoryInterface::~QDesignerWidgetFactoryInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QDesignerWidgetFactoryInterfaceD1Ev(
    QDesignerWidgetFactoryInterface *self) {
  delete self;
}

//  QDesignerFormEditorInterface *QDesignerWidgetFactoryInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK31QDesignerWidgetFactoryInterface4coreEv(
    const QDesignerWidgetFactoryInterface *self) {
  return self->core();
}

//  QWidget *QDesignerWidgetFactoryInterface::containerOfWidget(QWidget *w)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK31QDesignerWidgetFactoryInterface17containerOfWidgetEP7QWidget(
    const QDesignerWidgetFactoryInterface *self,
    QWidget *w) {
  return self->containerOfWidget(w);
}

//  QWidget *QDesignerWidgetFactoryInterface::widgetOfContainer(QWidget *w)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK31QDesignerWidgetFactoryInterface17widgetOfContainerEP7QWidget(
    const QDesignerWidgetFactoryInterface *self,
    QWidget *w) {
  return self->widgetOfContainer(w);
}

//  QWidget *QDesignerWidgetFactoryInterface::createWidget(const QString
//      &name, QWidget *parentWidget) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK31QDesignerWidgetFactoryInterface12createWidgetERK7QStringP7QWidget(
    const QDesignerWidgetFactoryInterface *self,
    const QString *name,
    QWidget *parentWidget) {
  return self->createWidget(*name, parentWidget);
}

//  QLayout *QDesignerWidgetFactoryInterface::createLayout(QWidget *widget,
//      QLayout *layout, int type) const
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZNK31QDesignerWidgetFactoryInterface12createLayoutEP7QWidgetP7QLayouti(
    const QDesignerWidgetFactoryInterface *self,
    QWidget *widget,
    QLayout *layout,
    int type) {
  return self->createLayout(widget, layout, type);
}

//  bool QDesignerWidgetFactoryInterface::isPassiveInteractor(QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QDesignerWidgetFactoryInterface19isPassiveInteractorEP7QWidget(
    QDesignerWidgetFactoryInterface *self,
    QWidget *widget) {
  return self->isPassiveInteractor(widget);
}

//  void QDesignerWidgetFactoryInterface::initialize(QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK31QDesignerWidgetFactoryInterface10initializeEP7QObject(
    const QDesignerWidgetFactoryInterface *self,
    QObject *object) {
  self->initialize(object);
}

//  a Python function taken by a CuteQDesignerWidgetFactoryInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerWidgetFactoryInterface(
    QDesignerWidgetFactoryInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerWidgetFactoryInterface *>(self)->take(key, call);
}
