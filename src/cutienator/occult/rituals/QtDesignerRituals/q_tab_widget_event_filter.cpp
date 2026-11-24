//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_tabwidget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_tabwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTabWidgetEventFilter that Python can take functions over in. Every QTabWidgetEventFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTabWidgetEventFilterCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTabWidgetEventFilterCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTabWidgetEventFilterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTabWidgetEventFilterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTabWidgetEventFilterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTabWidgetEventFilterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTabWidgetEventFilterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTabWidgetEventFilter : public QTabWidgetEventFilter {
public:
  using QTabWidgetEventFilter::QTabWidgetEventFilter;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QTabWidgetEventFilter::eventFilter(QObject *o, QEvent *e)
  bool eventFilter(QObject *o, QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTabWidgetEventFilterCall0 call = reinterpret_cast<CuteQTabWidgetEventFilterCall0>(taken[0]);
      bool given = call(this, o, e, &handled);
      if (handled) return given;
    }
    return QTabWidgetEventFilter::eventFilter(o, e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTabWidgetEventFilterCall1 call = reinterpret_cast<CuteQTabWidgetEventFilterCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTabWidgetEventFilterCall2 call = reinterpret_cast<CuteQTabWidgetEventFilterCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTabWidgetEventFilterCall3 call = reinterpret_cast<CuteQTabWidgetEventFilterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTabWidgetEventFilterCall4 call = reinterpret_cast<CuteQTabWidgetEventFilterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTabWidgetEventFilterCall5 call = reinterpret_cast<CuteQTabWidgetEventFilterCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTabWidgetEventFilterCall6 call = reinterpret_cast<CuteQTabWidgetEventFilterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTabWidgetEventFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QTabWidgetEventFilter10metaObjectEv(
    const QTabWidgetEventFilter *self) {
  return self->metaObject();
}

//  QString QTabWidgetEventFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QTabWidgetEventFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTabWidgetEventFilter::tr(s, c, n));
}

//  QTabWidgetEventFilter::QTabWidgetEventFilter(QTabWidget *parent)
extern "C" Q_DECL_EXPORT
QTabWidgetEventFilter *ritual_ZN21QTabWidgetEventFilterC1EP10QTabWidget(
    QTabWidget *parent) {
  return new CuteQTabWidgetEventFilter(parent);
}

//  QTabWidgetEventFilter::~QTabWidgetEventFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTabWidgetEventFilterD1Ev(QTabWidgetEventFilter *self) {
  delete self;
}

//  void QTabWidgetEventFilter::install(QTabWidget *tabWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTabWidgetEventFilter7installEP10QTabWidget(
    QTabWidget *tabWidget) {
  QTabWidgetEventFilter::install(tabWidget);
}

//  QTabWidgetEventFilter *QTabWidgetEventFilter::eventFilterOf(const
//      QTabWidget *tabWidget)
extern "C" Q_DECL_EXPORT
QTabWidgetEventFilter *ritual_ZN21QTabWidgetEventFilter13eventFilterOfEPK10QTabWidget(
    const QTabWidget *tabWidget) {
  return QTabWidgetEventFilter::eventFilterOf(tabWidget);
}

//  QMenu *QTabWidgetEventFilter::addTabWidgetContextMenuActions(const
//      QTabWidget *tabWidget, QMenu *popup)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN21QTabWidgetEventFilter30addTabWidgetContextMenuActionsEPK10QTabWidgetP5QMenu(
    const QTabWidget *tabWidget,
    QMenu *popup) {
  return QTabWidgetEventFilter::addTabWidgetContextMenuActions(
      tabWidget,
      popup);
}

//  QMenu *QTabWidgetEventFilter::addContextMenuActions(QMenu *popup)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN21QTabWidgetEventFilter21addContextMenuActionsEP5QMenu(
    QTabWidgetEventFilter *self,
    QMenu *popup) {
  return self->addContextMenuActions(popup);
}

//  bool QTabWidgetEventFilter::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QTabWidgetEventFilter11eventFilterEP7QObjectP6QEvent(
    QTabWidgetEventFilter *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  QDesignerFormWindowInterface *QTabWidgetEventFilter::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK21QTabWidgetEventFilter10formWindowEv(
    const QTabWidgetEventFilter *self) {
  return self->formWindow();
}

//  void QTabWidgetEventFilter::removeCurrentPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTabWidgetEventFilter17removeCurrentPageEv(
    QTabWidgetEventFilter *self) {
  self->removeCurrentPage();
}

//  void QTabWidgetEventFilter::addPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTabWidgetEventFilter7addPageEv(
    QTabWidgetEventFilter *self) {
  self->addPage();
}

//  void QTabWidgetEventFilter::addPageAfter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTabWidgetEventFilter12addPageAfterEv(
    QTabWidgetEventFilter *self) {
  self->addPageAfter();
}

//  QTabBar *QTabWidgetEventFilter::tabBar() const
extern "C" Q_DECL_EXPORT
QTabBar *ritual_ZNK21QTabWidgetEventFilter6tabBarEv(
    const QTabWidgetEventFilter *self) {
  return self->tabBar();
}

//  a Python function taken by a CuteQTabWidgetEventFilter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTabWidgetEventFilter(
    QTabWidgetEventFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTabWidgetEventFilter *>(self)->take(key, call);
}

//  bool QTabWidgetEventFilter::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QTabWidgetEventFilter11eventFilterEP7QObjectP6QEvent(
    QTabWidgetEventFilter *self,
    QObject *o,
    QEvent *e) {
  return self->QTabWidgetEventFilter::eventFilter(o, e);
}
