//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformmessaged
//  ialog_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformmessagedialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPlatformMessageDialog that Python can take functions over in. Every QQuickPlatformMessageDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPlatformMessageDialogCall0)(const void *, int *);
typedef bool (*CuteQQuickPlatformMessageDialogCall1)(const void *, int, int, QWindow *, int *);
typedef void (*CuteQQuickPlatformMessageDialogCall2)(const void *, int *);
typedef const QVariant * (*CuteQQuickPlatformMessageDialogCall3)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformMessageDialogCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformMessageDialogCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformMessageDialogCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformMessageDialogCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformMessageDialogCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformMessageDialogCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformMessageDialogCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPlatformMessageDialog : public QQuickPlatformMessageDialog {
public:
  using QQuickPlatformMessageDialog::QQuickPlatformMessageDialog;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4execEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4hideEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformDialogHelper9styleHintENS_9StyleHintE")) {
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

  //  void QQuickPlatformMessageDialog::exec()
  void exec() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPlatformMessageDialogCall0 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformMessageDialog::exec();
  }

  //  bool QQuickPlatformMessageDialog::show(Qt::WindowFlags flags,
  //      Qt::WindowModality modality, QWindow *parent)
  bool show(
      Qt::WindowFlags flags,
      Qt::WindowModality modality,
      QWindow *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPlatformMessageDialogCall1 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall1>(taken[1]);
      bool given = call(this, static_cast<int>(flags.toInt()), static_cast<int>(modality), parent, &handled);
      if (handled) return given;
    }
    return QQuickPlatformMessageDialog::show(flags, modality, parent);
  }

  //  void QQuickPlatformMessageDialog::hide()
  void hide() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPlatformMessageDialogCall2 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformMessageDialog::hide();
  }

  //  QVariant QPlatformDialogHelper::styleHint(StyleHint hint) const
  QVariant styleHint(QPlatformDialogHelper::StyleHint hint) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPlatformMessageDialogCall3 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(hint), &handled);
      if (handled && given) return *given;
    }
    return QPlatformDialogHelper::styleHint(hint);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPlatformMessageDialogCall4 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall4>(taken[4]);
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
      CuteQQuickPlatformMessageDialogCall5 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall5>(taken[5]);
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
      CuteQQuickPlatformMessageDialogCall6 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall6>(taken[6]);
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
      CuteQQuickPlatformMessageDialogCall7 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall7>(taken[7]);
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
      CuteQQuickPlatformMessageDialogCall8 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall8>(taken[8]);
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
      CuteQQuickPlatformMessageDialogCall9 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall9>(taken[9]);
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
      CuteQQuickPlatformMessageDialogCall10 call = reinterpret_cast<CuteQQuickPlatformMessageDialogCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPlatformMessageDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickPlatformMessageDialog10metaObjectEv(
    const QQuickPlatformMessageDialog *self) {
  return self->metaObject();
}

//  void *QQuickPlatformMessageDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQuickPlatformMessageDialog11qt_metacastEPKc(
    QQuickPlatformMessageDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPlatformMessageDialog::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQuickPlatformMessageDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPlatformMessageDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPlatformMessageDialog::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQuickPlatformMessageDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPlatformMessageDialog::tr(s, c, n));
}

//  QQuickPlatformMessageDialog::QQuickPlatformMessageDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPlatformMessageDialog *ritual_ZN27QQuickPlatformMessageDialogC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPlatformMessageDialog(parent);
}

//  QQuickPlatformMessageDialog::~QQuickPlatformMessageDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickPlatformMessageDialogD1Ev(
    QQuickPlatformMessageDialog *self) {
  delete self;
}

//  bool QQuickPlatformMessageDialog::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickPlatformMessageDialog7isValidEv(
    const QQuickPlatformMessageDialog *self) {
  return self->isValid();
}

//  void QQuickPlatformMessageDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickPlatformMessageDialog4execEv(
    QQuickPlatformMessageDialog *self) {
  self->exec();
}

//  bool QQuickPlatformMessageDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickPlatformMessageDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformMessageDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformMessageDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickPlatformMessageDialog4hideEv(
    QQuickPlatformMessageDialog *self) {
  self->hide();
}

//  QQuickMessageDialogImpl *QQuickPlatformMessageDialog::dialog() const
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImpl *ritual_ZNK27QQuickPlatformMessageDialog6dialogEv(
    const QQuickPlatformMessageDialog *self) {
  return self->dialog();
}

//  a Python function taken by a CuteQQuickPlatformMessageDialog, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPlatformMessageDialog(
    QQuickPlatformMessageDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPlatformMessageDialog *>(self)->take(key, call);
}

//  void QQuickPlatformMessageDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickPlatformMessageDialog4execEv(
    QQuickPlatformMessageDialog *self) {
  self->QQuickPlatformMessageDialog::exec();
}

//  bool QQuickPlatformMessageDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QQuickPlatformMessageDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformMessageDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->QQuickPlatformMessageDialog::show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformMessageDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickPlatformMessageDialog4hideEv(
    QQuickPlatformMessageDialog *self) {
  self->QQuickPlatformMessageDialog::hide();
}
