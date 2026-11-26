//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformcolordia
//  log_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformcolordialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPlatformColorDialog that Python can take functions over in. Every QQuickPlatformColorDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPlatformColorDialogCall0)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQQuickPlatformColorDialogCall1)(const void *, int *);
typedef void (*CuteQQuickPlatformColorDialogCall2)(const void *, int *);
typedef bool (*CuteQQuickPlatformColorDialogCall3)(const void *, int, int, QWindow *, int *);
typedef void (*CuteQQuickPlatformColorDialogCall4)(const void *, int *);
typedef const QVariant * (*CuteQQuickPlatformColorDialogCall5)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformColorDialogCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformColorDialogCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformColorDialogCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformColorDialogCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformColorDialogCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformColorDialogCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformColorDialogCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPlatformColorDialog : public QQuickPlatformColorDialog {
public:
  using QQuickPlatformColorDialog::QQuickPlatformColorDialog;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QPlatformColorDialogHelper15setCurrentColorERK6QColor")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformColorDialogHelper12currentColorEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4execEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4hideEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformDialogHelper9styleHintENS_9StyleHintE")) {
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

  //  void QQuickPlatformColorDialog::setCurrentColor(const QColor &color)
  void setCurrentColor(const QColor &color) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPlatformColorDialogCall0 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall0>(taken[0]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QQuickPlatformColorDialog::setCurrentColor(color);
  }

  //  QColor QQuickPlatformColorDialog::currentColor() const
  QColor currentColor() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPlatformColorDialogCall1 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall1>(taken[1]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPlatformColorDialog::currentColor();
  }

  //  void QQuickPlatformColorDialog::exec()
  void exec() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPlatformColorDialogCall2 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformColorDialog::exec();
  }

  //  bool QQuickPlatformColorDialog::show(Qt::WindowFlags flags,
  //      Qt::WindowModality modality, QWindow *parent)
  bool show(
      Qt::WindowFlags flags,
      Qt::WindowModality modality,
      QWindow *parent) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPlatformColorDialogCall3 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall3>(taken[3]);
      bool given = call(this, static_cast<int>(flags.toInt()), static_cast<int>(modality), parent, &handled);
      if (handled) return given;
    }
    return QQuickPlatformColorDialog::show(flags, modality, parent);
  }

  //  void QQuickPlatformColorDialog::hide()
  void hide() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPlatformColorDialogCall4 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformColorDialog::hide();
  }

  //  QVariant QPlatformDialogHelper::styleHint(StyleHint hint) const
  QVariant styleHint(QPlatformDialogHelper::StyleHint hint) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPlatformColorDialogCall5 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(hint), &handled);
      if (handled && given) return *given;
    }
    return QPlatformDialogHelper::styleHint(hint);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPlatformColorDialogCall6 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall6>(taken[6]);
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
      CuteQQuickPlatformColorDialogCall7 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall7>(taken[7]);
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
      CuteQQuickPlatformColorDialogCall8 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall8>(taken[8]);
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
      CuteQQuickPlatformColorDialogCall9 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall9>(taken[9]);
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
      CuteQQuickPlatformColorDialogCall10 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall10>(taken[10]);
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
      CuteQQuickPlatformColorDialogCall11 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall11>(taken[11]);
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
      CuteQQuickPlatformColorDialogCall12 call = reinterpret_cast<CuteQQuickPlatformColorDialogCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPlatformColorDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickPlatformColorDialog10metaObjectEv(
    const QQuickPlatformColorDialog *self) {
  return self->metaObject();
}

//  void *QQuickPlatformColorDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuickPlatformColorDialog11qt_metacastEPKc(
    QQuickPlatformColorDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPlatformColorDialog::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuickPlatformColorDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPlatformColorDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPlatformColorDialog::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickPlatformColorDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPlatformColorDialog::tr(s, c, n));
}

//  QQuickPlatformColorDialog::QQuickPlatformColorDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPlatformColorDialog *ritual_ZN25QQuickPlatformColorDialogC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPlatformColorDialog(parent);
}

//  QQuickPlatformColorDialog::~QQuickPlatformColorDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickPlatformColorDialogD1Ev(
    QQuickPlatformColorDialog *self) {
  delete self;
}

//  bool QQuickPlatformColorDialog::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickPlatformColorDialog7isValidEv(
    const QQuickPlatformColorDialog *self) {
  return self->isValid();
}

//  void QQuickPlatformColorDialog::setCurrentColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickPlatformColorDialog15setCurrentColorERK6QColor(
    QQuickPlatformColorDialog *self,
    const QColor *color) {
  self->setCurrentColor(*color);
}

//  QColor QQuickPlatformColorDialog::currentColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQuickPlatformColorDialog12currentColorEv(
    const QQuickPlatformColorDialog *self) {
  return new QColor(self->currentColor());
}

//  void QQuickPlatformColorDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickPlatformColorDialog4execEv(
    QQuickPlatformColorDialog *self) {
  self->exec();
}

//  bool QQuickPlatformColorDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickPlatformColorDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformColorDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformColorDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickPlatformColorDialog4hideEv(
    QQuickPlatformColorDialog *self) {
  self->hide();
}

//  QQuickColorDialogImpl *QQuickPlatformColorDialog::dialog() const
extern "C" Q_DECL_EXPORT
QQuickColorDialogImpl *ritual_ZNK25QQuickPlatformColorDialog6dialogEv(
    const QQuickPlatformColorDialog *self) {
  return self->dialog();
}

//  a Python function taken by a CuteQQuickPlatformColorDialog, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPlatformColorDialog(
    QQuickPlatformColorDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPlatformColorDialog *>(self)->take(key, call);
}

//  void QQuickPlatformColorDialog::setCurrentColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickPlatformColorDialog15setCurrentColorERK6QColor(
    QQuickPlatformColorDialog *self,
    const QColor *color) {
  self->QQuickPlatformColorDialog::setCurrentColor(*color);
}

//  QColor QQuickPlatformColorDialog::currentColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK25QQuickPlatformColorDialog12currentColorEv(
    const QQuickPlatformColorDialog *self) {
  return new QColor(self->QQuickPlatformColorDialog::currentColor());
}

//  void QQuickPlatformColorDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickPlatformColorDialog4execEv(
    QQuickPlatformColorDialog *self) {
  self->QQuickPlatformColorDialog::exec();
}

//  bool QQuickPlatformColorDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QQuickPlatformColorDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformColorDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->QQuickPlatformColorDialog::show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformColorDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickPlatformColorDialog4hideEv(
    QQuickPlatformColorDialog *self) {
  self->QQuickPlatformColorDialog::hide();
}
