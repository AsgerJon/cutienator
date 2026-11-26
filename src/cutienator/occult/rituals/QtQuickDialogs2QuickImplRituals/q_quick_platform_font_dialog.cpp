//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformfontdial
//  og_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformfontdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPlatformFontDialog that Python can take functions over in. Every QQuickPlatformFontDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPlatformFontDialogCall0)(const void *, const QFont *, int *);
typedef const QFont * (*CuteQQuickPlatformFontDialogCall1)(const void *, int *);
typedef void (*CuteQQuickPlatformFontDialogCall2)(const void *, int *);
typedef bool (*CuteQQuickPlatformFontDialogCall3)(const void *, int, int, QWindow *, int *);
typedef void (*CuteQQuickPlatformFontDialogCall4)(const void *, int *);
typedef const QVariant * (*CuteQQuickPlatformFontDialogCall5)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformFontDialogCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformFontDialogCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFontDialogCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFontDialogCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFontDialogCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFontDialogCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFontDialogCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPlatformFontDialog : public QQuickPlatformFontDialog {
public:
  using QQuickPlatformFontDialog::QQuickPlatformFontDialog;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QPlatformFontDialogHelper14setCurrentFontERK5QFont")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QPlatformFontDialogHelper11currentFontEv")) {
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

  //  void QQuickPlatformFontDialog::setCurrentFont(const QFont &font)
  void setCurrentFont(const QFont &font) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPlatformFontDialogCall0 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall0>(taken[0]);
      call(this, &font, &handled);
      if (handled) return;
    }
    QQuickPlatformFontDialog::setCurrentFont(font);
  }

  //  QFont QQuickPlatformFontDialog::currentFont() const
  QFont currentFont() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPlatformFontDialogCall1 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall1>(taken[1]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPlatformFontDialog::currentFont();
  }

  //  void QQuickPlatformFontDialog::exec()
  void exec() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPlatformFontDialogCall2 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformFontDialog::exec();
  }

  //  bool QQuickPlatformFontDialog::show(Qt::WindowFlags flags,
  //      Qt::WindowModality modality, QWindow *parent)
  bool show(
      Qt::WindowFlags flags,
      Qt::WindowModality modality,
      QWindow *parent) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPlatformFontDialogCall3 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall3>(taken[3]);
      bool given = call(this, static_cast<int>(flags.toInt()), static_cast<int>(modality), parent, &handled);
      if (handled) return given;
    }
    return QQuickPlatformFontDialog::show(flags, modality, parent);
  }

  //  void QQuickPlatformFontDialog::hide()
  void hide() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPlatformFontDialogCall4 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformFontDialog::hide();
  }

  //  QVariant QPlatformDialogHelper::styleHint(StyleHint hint) const
  QVariant styleHint(QPlatformDialogHelper::StyleHint hint) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPlatformFontDialogCall5 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall5>(taken[5]);
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
      CuteQQuickPlatformFontDialogCall6 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall6>(taken[6]);
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
      CuteQQuickPlatformFontDialogCall7 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall7>(taken[7]);
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
      CuteQQuickPlatformFontDialogCall8 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall8>(taken[8]);
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
      CuteQQuickPlatformFontDialogCall9 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall9>(taken[9]);
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
      CuteQQuickPlatformFontDialogCall10 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall10>(taken[10]);
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
      CuteQQuickPlatformFontDialogCall11 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall11>(taken[11]);
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
      CuteQQuickPlatformFontDialogCall12 call = reinterpret_cast<CuteQQuickPlatformFontDialogCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPlatformFontDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickPlatformFontDialog10metaObjectEv(
    const QQuickPlatformFontDialog *self) {
  return self->metaObject();
}

//  void *QQuickPlatformFontDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickPlatformFontDialog11qt_metacastEPKc(
    QQuickPlatformFontDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPlatformFontDialog::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickPlatformFontDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPlatformFontDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPlatformFontDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickPlatformFontDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPlatformFontDialog::tr(s, c, n));
}

//  QQuickPlatformFontDialog::QQuickPlatformFontDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPlatformFontDialog *ritual_ZN24QQuickPlatformFontDialogC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPlatformFontDialog(parent);
}

//  QQuickPlatformFontDialog::~QQuickPlatformFontDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFontDialogD1Ev(
    QQuickPlatformFontDialog *self) {
  delete self;
}

//  bool QQuickPlatformFontDialog::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickPlatformFontDialog7isValidEv(
    const QQuickPlatformFontDialog *self) {
  return self->isValid();
}

//  void QQuickPlatformFontDialog::setCurrentFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFontDialog14setCurrentFontERK5QFont(
    QQuickPlatformFontDialog *self,
    const QFont *font) {
  self->setCurrentFont(*font);
}

//  QFont QQuickPlatformFontDialog::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK24QQuickPlatformFontDialog11currentFontEv(
    const QQuickPlatformFontDialog *self) {
  return new QFont(self->currentFont());
}

//  void QQuickPlatformFontDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFontDialog4execEv(
    QQuickPlatformFontDialog *self) {
  self->exec();
}

//  bool QQuickPlatformFontDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickPlatformFontDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformFontDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformFontDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFontDialog4hideEv(
    QQuickPlatformFontDialog *self) {
  self->hide();
}

//  QQuickFontDialogImpl *QQuickPlatformFontDialog::dialog() const
extern "C" Q_DECL_EXPORT
QQuickFontDialogImpl *ritual_ZNK24QQuickPlatformFontDialog6dialogEv(
    const QQuickPlatformFontDialog *self) {
  return self->dialog();
}

//  a Python function taken by a CuteQQuickPlatformFontDialog, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPlatformFontDialog(
    QQuickPlatformFontDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPlatformFontDialog *>(self)->take(key, call);
}

//  void QQuickPlatformFontDialog::setCurrentFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickPlatformFontDialog14setCurrentFontERK5QFont(
    QQuickPlatformFontDialog *self,
    const QFont *font) {
  self->QQuickPlatformFontDialog::setCurrentFont(*font);
}

//  QFont QQuickPlatformFontDialog::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK24QQuickPlatformFontDialog11currentFontEv(
    const QQuickPlatformFontDialog *self) {
  return new QFont(self->QQuickPlatformFontDialog::currentFont());
}

//  void QQuickPlatformFontDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickPlatformFontDialog4execEv(
    QQuickPlatformFontDialog *self) {
  self->QQuickPlatformFontDialog::exec();
}

//  bool QQuickPlatformFontDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQuickPlatformFontDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformFontDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->QQuickPlatformFontDialog::show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformFontDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickPlatformFontDialog4hideEv(
    QQuickPlatformFontDialog *self) {
  self->QQuickPlatformFontDialog::hide();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
