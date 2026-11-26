//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/layout_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/layout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on qdesigner_internal::Layout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_Layout : qdesigner_internal::Layout {
  using qdesigner_internal::Layout::finishLayout;
};

//  A qdesigner_internal::Layout that Python can take functions over in. Every qdesigner_internal::Layout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cuteqdesigner_internal_LayoutCall0)(const void *, int *);
typedef void (*Cuteqdesigner_internal_LayoutCall1)(const void *, int *);
typedef void (*Cuteqdesigner_internal_LayoutCall2)(const void *, int *);
typedef void (*Cuteqdesigner_internal_LayoutCall3)(const void *, int *);
typedef void (*Cuteqdesigner_internal_LayoutCall4)(const void *, int *);
typedef void (*Cuteqdesigner_internal_LayoutCall5)(const void *, bool, QLayout *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_LayoutCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_LayoutCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_LayoutCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_LayoutCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_LayoutCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_LayoutCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_LayoutCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_Layout : public qdesigner_internal::Layout {
public:
  using qdesigner_internal::Layout::Layout;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18qdesigner_internal6Layout4sortEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal6Layout8doLayoutEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal6Layout5setupEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal6Layout10undoLayoutEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal6Layout11breakLayoutEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal6Layout12finishLayoutEbP7QLayout")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void qdesigner_internal::Layout::sort()
  void sort() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall0 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::Layout::doLayout()
  void doLayout() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall1 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::Layout::setup()
  void setup() override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall2 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::Layout::setup();
  }

  //  void qdesigner_internal::Layout::undoLayout()
  void undoLayout() override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall3 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::Layout::undoLayout();
  }

  //  void qdesigner_internal::Layout::breakLayout()
  void breakLayout() override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall4 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::Layout::breakLayout();
  }

  //  void qdesigner_internal::Layout::finishLayout(bool needMove, QLayout
  //      *layout)
  void finishLayout(bool needMove, QLayout *layout) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall5 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall5>(taken[5]);
      call(this, needMove, layout, &handled);
      if (handled) return;
    }
    qdesigner_internal::Layout::finishLayout(needMove, layout);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall6 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall7 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall8 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall9 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall10 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall11 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCall12 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::Layout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal6Layout10metaObjectEv(
    const qdesigner_internal::Layout *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::Layout::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal6Layout11qt_metacastEPKc(
    qdesigner_internal::Layout *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::Layout::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal6Layout11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::Layout *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::Layout::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal6Layout2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::Layout::tr(s, c, n));
}

//  qdesigner_internal::Layout::Layout(const QWidgetList &wl, QWidget *p,
//      QDesignerFormWindowInterface *fw, QWidget *lb, LayoutInfo::Type
//      layoutType)
extern "C" Q_DECL_EXPORT
qdesigner_internal::Layout *ritual_ZN18qdesigner_internal6LayoutC1ERK5QListIP7QWidgetES3_P28QDesignerFormWindowInterfaceS3_NS_10LayoutInfo4TypeE(
    const QList<QWidget *> *wl,
    QWidget *p,
    QDesignerFormWindowInterface *fw,
    QWidget *lb,
    qdesigner_internal::LayoutInfo::Type layoutType) {
  return new Cuteqdesigner_internal_Layout(*wl, p, fw, lb, layoutType);
}

//  Layout *qdesigner_internal::Layout::createLayout(const QWidgetList
//      &widgets, QWidget *parentWidget, QDesignerFormWindowInterface *fw,
//      QWidget *layoutBase, LayoutInfo::Type layoutType)
extern "C" Q_DECL_EXPORT
qdesigner_internal::Layout *ritual_ZN18qdesigner_internal6Layout12createLayoutERK5QListIP7QWidgetES3_P28QDesignerFormWindowInterfaceS3_NS_10LayoutInfo4TypeE(
    const QList<QWidget *> *widgets,
    QWidget *parentWidget,
    QDesignerFormWindowInterface *fw,
    QWidget *layoutBase,
    qdesigner_internal::LayoutInfo::Type layoutType) {
  return qdesigner_internal::Layout::createLayout(
      *widgets,
      parentWidget,
      fw,
      layoutBase,
      layoutType);
}

//  qdesigner_internal::Layout::~Layout()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6LayoutD1Ev(
    qdesigner_internal::Layout *self) {
  delete self;
}

//  void qdesigner_internal::Layout::sort()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout4sortEv(
    qdesigner_internal::Layout *self) {
  self->sort();
}

//  void qdesigner_internal::Layout::doLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout8doLayoutEv(
    qdesigner_internal::Layout *self) {
  self->doLayout();
}

//  void qdesigner_internal::Layout::setup()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout5setupEv(
    qdesigner_internal::Layout *self) {
  self->setup();
}

//  void qdesigner_internal::Layout::undoLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout10undoLayoutEv(
    qdesigner_internal::Layout *self) {
  self->undoLayout();
}

//  void qdesigner_internal::Layout::breakLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout11breakLayoutEv(
    qdesigner_internal::Layout *self) {
  self->breakLayout();
}

//  const QWidgetList &qdesigner_internal::Layout::widgets() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal6Layout7widgetsEv(
    const qdesigner_internal::Layout *self) {
  return new QList<QWidget *>(self->widgets());
}

//  QWidget *qdesigner_internal::Layout::parentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal6Layout12parentWidgetEv(
    const qdesigner_internal::Layout *self) {
  return self->parentWidget();
}

//  QWidget *qdesigner_internal::Layout::layoutBaseWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal6Layout16layoutBaseWidgetEv(
    const qdesigner_internal::Layout *self) {
  return self->layoutBaseWidget();
}

//  bool qdesigner_internal::Layout::reparentLayoutWidget() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal6Layout20reparentLayoutWidgetEv(
    const qdesigner_internal::Layout *self) {
  return self->reparentLayoutWidget();
}

//  void qdesigner_internal::Layout::setReparentLayoutWidget(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout23setReparentLayoutWidgetEb(
    qdesigner_internal::Layout *self,
    bool v) {
  self->setReparentLayoutWidget(v);
}

//  void qdesigner_internal::Layout::finishLayout(bool needMove, QLayout
//      *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout12finishLayoutEbP7QLayout(
    qdesigner_internal::Layout *self,
    bool needMove,
    QLayout *layout) {
  self->finishLayout(needMove, layout);
}

//  bool qdesigner_internal::Layout::prepareLayout(bool &needMove, bool
//      &needReparent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal6Layout13prepareLayoutERbS1_(
    qdesigner_internal::Layout *self,
    bool *needMove,
    bool *needReparent) {
  return self->prepareLayout(*needMove, *needReparent);
}

//  void qdesigner_internal::Layout::setWidgets(const QWidgetList &widgets)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout10setWidgetsERK5QListIP7QWidgetE(
    qdesigner_internal::Layout *self,
    const QList<QWidget *> *widgets) {
  self->setWidgets(*widgets);
}

//  QLayout *qdesigner_internal::Layout::createLayout(int type)
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN18qdesigner_internal6Layout12createLayoutEi(
    qdesigner_internal::Layout *self,
    int type) {
  return self->createLayout(type);
}

//  void qdesigner_internal::Layout::reparentToLayoutBase(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout20reparentToLayoutBaseEP7QWidget(
    qdesigner_internal::Layout *self,
    QWidget *w) {
  self->reparentToLayoutBase(w);
}

//  void qdesigner_internal::Layout::widgetDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal6Layout15widgetDestroyedEv(
    qdesigner_internal::Layout *self) {
  self->widgetDestroyed();
}

//  a Python function taken by a Cuteqdesigner_internal_Layout, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_Layout(
    qdesigner_internal::Layout *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_Layout *>(self)->take(key, call);
}

//  void qdesigner_internal::Layout::setup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal6Layout5setupEv(
    qdesigner_internal::Layout *self) {
  self->qdesigner_internal::Layout::setup();
}

//  void qdesigner_internal::Layout::undoLayout()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal6Layout10undoLayoutEv(
    qdesigner_internal::Layout *self) {
  self->qdesigner_internal::Layout::undoLayout();
}

//  void qdesigner_internal::Layout::breakLayout()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal6Layout11breakLayoutEv(
    qdesigner_internal::Layout *self) {
  self->qdesigner_internal::Layout::breakLayout();
}

//  void qdesigner_internal::Layout::finishLayout(bool needMove, QLayout
//      *layout)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal6Layout12finishLayoutEbP7QLayout(
    qdesigner_internal::Layout *self,
    bool needMove,
    QLayout *layout) {
  static_cast<Ownqdesigner_internal_Layout *>(self)->Ownqdesigner_internal_Layout::finishLayout(
      needMove,
      layout);
}
