//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformDialogHelper that Python can take functions over in. Every QPlatformDialogHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQPlatformDialogHelperCall0)(const void *, int, int *);
typedef void (*CuteQPlatformDialogHelperCall1)(const void *, int *);
typedef bool (*CuteQPlatformDialogHelperCall2)(const void *, int, int, QWindow *, int *);
typedef void (*CuteQPlatformDialogHelperCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformDialogHelperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformDialogHelperCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformDialogHelperCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformDialogHelperCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformDialogHelperCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformDialogHelperCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformDialogHelperCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformDialogHelper : public QPlatformDialogHelper {
public:
  using QPlatformDialogHelper::QPlatformDialogHelper;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QPlatformDialogHelper9styleHintENS_9StyleHintE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4execEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4hideEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QVariant QPlatformDialogHelper::styleHint(StyleHint hint) const
  QVariant styleHint(QPlatformDialogHelper::StyleHint hint) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall0 call = reinterpret_cast<CuteQPlatformDialogHelperCall0>(taken[0]);
      const QVariant * given = call(this, static_cast<int>(hint), &handled);
      if (handled && given) return *given;
    }
    return QPlatformDialogHelper::styleHint(hint);
  }

  //  void QPlatformDialogHelper::exec()
  void exec() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall1 call = reinterpret_cast<CuteQPlatformDialogHelperCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QPlatformDialogHelper::show(Qt::WindowFlags windowFlags,
  //      Qt::WindowModality windowModality, QWindow *parent)
  bool show(
      Qt::WindowFlags windowFlags,
      Qt::WindowModality windowModality,
      QWindow *parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall2 call = reinterpret_cast<CuteQPlatformDialogHelperCall2>(taken[2]);
      bool given = call(this, static_cast<int>(windowFlags.toInt()), static_cast<int>(windowModality), parent, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPlatformDialogHelper::hide()
  void hide() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall3 call = reinterpret_cast<CuteQPlatformDialogHelperCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall4 call = reinterpret_cast<CuteQPlatformDialogHelperCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall5 call = reinterpret_cast<CuteQPlatformDialogHelperCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall6 call = reinterpret_cast<CuteQPlatformDialogHelperCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall7 call = reinterpret_cast<CuteQPlatformDialogHelperCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall8 call = reinterpret_cast<CuteQPlatformDialogHelperCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall9 call = reinterpret_cast<CuteQPlatformDialogHelperCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformDialogHelperCall10 call = reinterpret_cast<CuteQPlatformDialogHelperCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformDialogHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QPlatformDialogHelper10metaObjectEv(
    const QPlatformDialogHelper *self) {
  return self->metaObject();
}

//  QString QPlatformDialogHelper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QPlatformDialogHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformDialogHelper::tr(s, c, n));
}

//  QPlatformDialogHelper::~QPlatformDialogHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformDialogHelperD1Ev(QPlatformDialogHelper *self) {
  delete self;
}

//  QVariant QPlatformDialogHelper::styleHint(StyleHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QPlatformDialogHelper9styleHintENS_9StyleHintE(
    const QPlatformDialogHelper *self,
    QPlatformDialogHelper::StyleHint hint) {
  return new QVariant(self->styleHint(hint));
}

//  void QPlatformDialogHelper::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformDialogHelper4execEv(QPlatformDialogHelper *self) {
  self->exec();
}

//  bool QPlatformDialogHelper::show(Qt::WindowFlags windowFlags,
//      Qt::WindowModality windowModality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QPlatformDialogHelper4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QPlatformDialogHelper *self,
    int windowFlags,
    Qt::WindowModality windowModality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(windowFlags),
      windowModality,
      parent);
}

//  void QPlatformDialogHelper::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformDialogHelper4hideEv(QPlatformDialogHelper *self) {
  self->hide();
}

//  QVariant
//      QPlatformDialogHelper::defaultStyleHint(QPlatformDialogHelper::StyleH
//      int hint)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN21QPlatformDialogHelper16defaultStyleHintENS_9StyleHintE(
    QPlatformDialogHelper::StyleHint hint) {
  return new QVariant(QPlatformDialogHelper::defaultStyleHint(hint));
}

//  ButtonRole QPlatformDialogHelper::buttonRole(StandardButton button)
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper::ButtonRole ritual_ZN21QPlatformDialogHelper10buttonRoleENS_14StandardButtonE(
    QPlatformDialogHelper::StandardButton button) {
  return QPlatformDialogHelper::buttonRole(button);
}

//  a Python function taken by a CuteQPlatformDialogHelper, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformDialogHelper(
    QPlatformDialogHelper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformDialogHelper *>(self)->take(key, call);
}

//  QVariant QPlatformDialogHelper::styleHint(StyleHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK21QPlatformDialogHelper9styleHintENS_9StyleHintE(
    const QPlatformDialogHelper *self,
    QPlatformDialogHelper::StyleHint hint) {
  return new QVariant(self->QPlatformDialogHelper::styleHint(hint));
}
