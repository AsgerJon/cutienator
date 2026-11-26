//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractformwindowtool.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDesigner/abstractformwindowtool.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerFormWindowToolInterface that Python can take functions over in. Every QDesignerFormWindowToolInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerFormWindowToolInterfaceCall0)(const void *, int *);
typedef void * (*CuteQDesignerFormWindowToolInterfaceCall1)(const void *, int *);
typedef void * (*CuteQDesignerFormWindowToolInterfaceCall2)(const void *, int *);
typedef void * (*CuteQDesignerFormWindowToolInterfaceCall3)(const void *, int *);
typedef void (*CuteQDesignerFormWindowToolInterfaceCall4)(const void *, int *);
typedef void (*CuteQDesignerFormWindowToolInterfaceCall5)(const void *, int *);
typedef void (*CuteQDesignerFormWindowToolInterfaceCall6)(const void *, DomUI *, QWidget *, int *);
typedef void (*CuteQDesignerFormWindowToolInterfaceCall7)(const void *, DomUI *, QWidget *, int *);
typedef bool (*CuteQDesignerFormWindowToolInterfaceCall8)(const void *, QWidget *, QWidget *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerFormWindowToolInterfaceCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerFormWindowToolInterfaceCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowToolInterfaceCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowToolInterfaceCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowToolInterfaceCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowToolInterfaceCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowToolInterfaceCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerFormWindowToolInterface : public QDesignerFormWindowToolInterface {
public:
  using QDesignerFormWindowToolInterface::QDesignerFormWindowToolInterface;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK32QDesignerFormWindowToolInterface4coreEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerFormWindowToolInterface10formWindowEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerFormWindowToolInterface6editorEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerFormWindowToolInterface6actionEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerFormWindowToolInterface9activatedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerFormWindowToolInterface11deactivatedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerFormWindowToolInterface9saveToDomEP5DomUIP7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerFormWindowToolInterface11loadFromDomEP5DomUIP7QWidget")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerFormWindowToolInterface11handleEventEP7QWidgetS1_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QDesignerFormEditorInterface
  //      *QDesignerFormWindowToolInterface::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall0 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return {};
  }

  //  QDesignerFormWindowInterface
  //      *QDesignerFormWindowToolInterface::formWindow() const
  QDesignerFormWindowInterface *formWindow() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall1 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormWindowInterface *>(given);
    }
    return {};
  }

  //  QWidget *QDesignerFormWindowToolInterface::editor() const
  QWidget *editor() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall2 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  QAction *QDesignerFormWindowToolInterface::action() const
  QAction *action() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall3 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowToolInterface::activated()
  void activated() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall4 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowToolInterface::deactivated()
  void deactivated() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall5 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowToolInterface::saveToDom(DomUI *a0, QWidget
  //      *a1)
  void saveToDom(DomUI *a0, QWidget *a1) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall6 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall6>(taken[6]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QDesignerFormWindowToolInterface::saveToDom(a0, a1);
  }

  //  void QDesignerFormWindowToolInterface::loadFromDom(DomUI *a0, QWidget
  //      *a1)
  void loadFromDom(DomUI *a0, QWidget *a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall7 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall7>(taken[7]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QDesignerFormWindowToolInterface::loadFromDom(a0, a1);
  }

  //  bool QDesignerFormWindowToolInterface::handleEvent(QWidget *widget,
  //      QWidget *managedWidget, QEvent *event)
  bool handleEvent(
      QWidget *widget,
      QWidget *managedWidget,
      QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall8 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall8>(taken[8]);
      bool given = call(this, widget, managedWidget, event, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall9 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall10 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall11 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall12 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall13 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall14 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerFormWindowToolInterfaceCall15 call = reinterpret_cast<CuteQDesignerFormWindowToolInterfaceCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerFormWindowToolInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QDesignerFormWindowToolInterface10metaObjectEv(
    const QDesignerFormWindowToolInterface *self) {
  return self->metaObject();
}

//  void *QDesignerFormWindowToolInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QDesignerFormWindowToolInterface11qt_metacastEPKc(
    QDesignerFormWindowToolInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerFormWindowToolInterface::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QDesignerFormWindowToolInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerFormWindowToolInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerFormWindowToolInterface::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QDesignerFormWindowToolInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerFormWindowToolInterface::tr(s, c, n));
}

//  QDesignerFormWindowToolInterface::QDesignerFormWindowToolInterface(QObjec
//      t *parent)
extern "C" Q_DECL_EXPORT
QDesignerFormWindowToolInterface *ritual_ZN32QDesignerFormWindowToolInterfaceC1EP7QObject(
    QObject *parent) {
  return new CuteQDesignerFormWindowToolInterface(parent);
}

//  QDesignerFormWindowToolInterface::~QDesignerFormWindowToolInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerFormWindowToolInterfaceD1Ev(
    QDesignerFormWindowToolInterface *self) {
  delete self;
}

//  QDesignerFormEditorInterface *QDesignerFormWindowToolInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK32QDesignerFormWindowToolInterface4coreEv(
    const QDesignerFormWindowToolInterface *self) {
  return self->core();
}

//  QDesignerFormWindowInterface
//      *QDesignerFormWindowToolInterface::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK32QDesignerFormWindowToolInterface10formWindowEv(
    const QDesignerFormWindowToolInterface *self) {
  return self->formWindow();
}

//  QWidget *QDesignerFormWindowToolInterface::editor() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK32QDesignerFormWindowToolInterface6editorEv(
    const QDesignerFormWindowToolInterface *self) {
  return self->editor();
}

//  QAction *QDesignerFormWindowToolInterface::action() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK32QDesignerFormWindowToolInterface6actionEv(
    const QDesignerFormWindowToolInterface *self) {
  return self->action();
}

//  void QDesignerFormWindowToolInterface::activated()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerFormWindowToolInterface9activatedEv(
    QDesignerFormWindowToolInterface *self) {
  self->activated();
}

//  void QDesignerFormWindowToolInterface::deactivated()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerFormWindowToolInterface11deactivatedEv(
    QDesignerFormWindowToolInterface *self) {
  self->deactivated();
}

//  void QDesignerFormWindowToolInterface::saveToDom(DomUI *a0, QWidget *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerFormWindowToolInterface9saveToDomEP5DomUIP7QWidget(
    QDesignerFormWindowToolInterface *self,
    DomUI *a0,
    QWidget *a1) {
  self->saveToDom(a0, a1);
}

//  void QDesignerFormWindowToolInterface::loadFromDom(DomUI *a0, QWidget
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerFormWindowToolInterface11loadFromDomEP5DomUIP7QWidget(
    QDesignerFormWindowToolInterface *self,
    DomUI *a0,
    QWidget *a1) {
  self->loadFromDom(a0, a1);
}

//  bool QDesignerFormWindowToolInterface::handleEvent(QWidget *widget,
//      QWidget *managedWidget, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QDesignerFormWindowToolInterface11handleEventEP7QWidgetS1_P6QEvent(
    QDesignerFormWindowToolInterface *self,
    QWidget *widget,
    QWidget *managedWidget,
    QEvent *event) {
  return self->handleEvent(widget, managedWidget, event);
}

//  a Python function taken by a CuteQDesignerFormWindowToolInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerFormWindowToolInterface(
    QDesignerFormWindowToolInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerFormWindowToolInterface *>(self)->take(key, call);
}

//  void QDesignerFormWindowToolInterface::saveToDom(DomUI *a0, QWidget *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QDesignerFormWindowToolInterface9saveToDomEP5DomUIP7QWidget(
    QDesignerFormWindowToolInterface *self,
    DomUI *a0,
    QWidget *a1) {
  self->QDesignerFormWindowToolInterface::saveToDom(a0, a1);
}

//  void QDesignerFormWindowToolInterface::loadFromDom(DomUI *a0, QWidget
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QDesignerFormWindowToolInterface11loadFromDomEP5DomUIP7QWidget(
    QDesignerFormWindowToolInterface *self,
    DomUI *a0,
    QWidget *a1) {
  self->QDesignerFormWindowToolInterface::loadFromDom(a0, a1);
}
