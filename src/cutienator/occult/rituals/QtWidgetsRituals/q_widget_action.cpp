//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qwidgetaction.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qwidgetaction.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QWidgetAction may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWidgetAction : QWidgetAction {
  using QWidgetAction::event;
  using QWidgetAction::eventFilter;
  using QWidgetAction::createWidget;
  using QWidgetAction::deleteWidget;
};

//  A QWidgetAction that Python can take functions over in. Every QWidgetAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQWidgetActionCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQWidgetActionCall1)(const void *, QObject *, QEvent *, int *);
typedef void * (*CuteQWidgetActionCall2)(const void *, QWidget *, int *);
typedef void (*CuteQWidgetActionCall3)(const void *, QWidget *, int *);
typedef void (*CuteQWidgetActionCall4)(const void *, QTimerEvent *, int *);
typedef void (*CuteQWidgetActionCall5)(const void *, QChildEvent *, int *);
typedef void (*CuteQWidgetActionCall6)(const void *, QEvent *, int *);
typedef void (*CuteQWidgetActionCall7)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQWidgetActionCall8)(const void *, const QMetaMethod *, int *);
class CuteQWidgetAction : public QWidgetAction {
public:
  using QWidgetAction::QWidgetAction;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QWidgetAction12createWidgetEP7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QWidgetAction12deleteWidgetEP7QWidget")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  bool QWidgetAction::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWidgetActionCall0 call = reinterpret_cast<CuteQWidgetActionCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidgetAction::event(a0);
  }

  //  bool QWidgetAction::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWidgetActionCall1 call = reinterpret_cast<CuteQWidgetActionCall1>(taken[1]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QWidgetAction::eventFilter(a0, a1);
  }

  //  QWidget *QWidgetAction::createWidget(QWidget *parent)
  QWidget *createWidget(QWidget *parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWidgetActionCall2 call = reinterpret_cast<CuteQWidgetActionCall2>(taken[2]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QWidgetAction::createWidget(parent);
  }

  //  void QWidgetAction::deleteWidget(QWidget *widget)
  void deleteWidget(QWidget *widget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWidgetActionCall3 call = reinterpret_cast<CuteQWidgetActionCall3>(taken[3]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QWidgetAction::deleteWidget(widget);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWidgetActionCall4 call = reinterpret_cast<CuteQWidgetActionCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWidgetActionCall5 call = reinterpret_cast<CuteQWidgetActionCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWidgetActionCall6 call = reinterpret_cast<CuteQWidgetActionCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWidgetActionCall7 call = reinterpret_cast<CuteQWidgetActionCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWidgetActionCall8 call = reinterpret_cast<CuteQWidgetActionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QWidgetAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QWidgetAction10metaObjectEv(
    const QWidgetAction *self) {
  return self->metaObject();
}

//  QString QWidgetAction::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QWidgetAction2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWidgetAction::tr(s, c, n));
}

//  QWidgetActionPrivate *QWidgetAction::d_func()
extern "C" Q_DECL_EXPORT
QWidgetActionPrivate *ritual_ZN13QWidgetAction6d_funcEv(
    QWidgetAction *self) {
  return self->d_func();
}

//  const QWidgetActionPrivate *QWidgetAction::d_func() const
extern "C" Q_DECL_EXPORT
const QWidgetActionPrivate *ritual_ZNK13QWidgetAction6d_funcEv(
    const QWidgetAction *self) {
  return self->d_func();
}

//  QWidgetAction::QWidgetAction(QObject *parent)
extern "C" Q_DECL_EXPORT
QWidgetAction *ritual_ZN13QWidgetActionC1EP7QObject(QObject *parent) {
  return new CuteQWidgetAction(parent);
}

//  QWidgetAction::~QWidgetAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetActionD1Ev(QWidgetAction *self) {
  delete self;
}

//  void QWidgetAction::setDefaultWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetAction16setDefaultWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *w) {
  self->setDefaultWidget(w);
}

//  QWidget *QWidgetAction::defaultWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QWidgetAction13defaultWidgetEv(
    const QWidgetAction *self) {
  return self->defaultWidget();
}

//  QWidget *QWidgetAction::requestWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN13QWidgetAction13requestWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *parent) {
  return self->requestWidget(parent);
}

//  void QWidgetAction::releaseWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetAction13releaseWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *widget) {
  self->releaseWidget(widget);
}

//  bool QWidgetAction::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QWidgetAction5eventEP6QEvent(
    QWidgetAction *self,
    QEvent *a0) {
  return self->event(a0);
}

//  bool QWidgetAction::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QWidgetAction11eventFilterEP7QObjectP6QEvent(
    QWidgetAction *self,
    QObject *a0,
    QEvent *a1) {
  return self->eventFilter(a0, a1);
}

//  QWidget *QWidgetAction::createWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN13QWidgetAction12createWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *parent) {
  return self->createWidget(parent);
}

//  void QWidgetAction::deleteWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetAction12deleteWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *widget) {
  self->deleteWidget(widget);
}

//  QList<QWidget *> QWidgetAction::createdWidgets() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK13QWidgetAction14createdWidgetsEv(
    const QWidgetAction *self) {
  return new QList<QWidget *>(self->createdWidgets());
}

//  a Python function taken by a CuteQWidgetAction, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidgetAction(
    QWidgetAction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWidgetAction *>(self)->take(key, call);
}

//  bool QWidgetAction::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QWidgetAction5eventEP6QEvent(
    QWidgetAction *self,
    QEvent *a0) {
  return static_cast<OwnQWidgetAction *>(self)->OwnQWidgetAction::event(a0);
}

//  bool QWidgetAction::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QWidgetAction11eventFilterEP7QObjectP6QEvent(
    QWidgetAction *self,
    QObject *a0,
    QEvent *a1) {
  return static_cast<OwnQWidgetAction *>(self)->OwnQWidgetAction::eventFilter(
      a0,
      a1);
}

//  QWidget *QWidgetAction::createWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZN13QWidgetAction12createWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *parent) {
  return static_cast<OwnQWidgetAction *>(self)->OwnQWidgetAction::createWidget(
      parent);
}

//  void QWidgetAction::deleteWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QWidgetAction12deleteWidgetEP7QWidget(
    QWidgetAction *self,
    QWidget *widget) {
  static_cast<OwnQWidgetAction *>(self)->OwnQWidgetAction::deleteWidget(
      widget);
}
