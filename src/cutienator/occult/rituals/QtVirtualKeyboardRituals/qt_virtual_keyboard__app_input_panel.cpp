//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/appinputpanel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/appinputpanel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtVirtualKeyboard::AppInputPanel that Python can take functions over in. Every QtVirtualKeyboard::AppInputPanel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall0)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall1)(const void *, int *);
typedef bool (*CuteQtVirtualKeyboard_AppInputPanelCall2)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall3)(const void *, const QRect *, int *);
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall4)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_AppInputPanelCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_AppInputPanelCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AppInputPanelCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_AppInputPanel : public QtVirtualKeyboard::AppInputPanel {
public:
  using QtVirtualKeyboard::AppInputPanel::AppInputPanel;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QtVirtualKeyboard18AbstractInputPanel4showEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QtVirtualKeyboard18AbstractInputPanel4hideEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QtVirtualKeyboard18AbstractInputPanel9isVisibleEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QtVirtualKeyboard18AbstractInputPanel12setInputRectERK5QRect")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QtVirtualKeyboard18AbstractInputPanel10createViewEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QtVirtualKeyboard18AbstractInputPanel11destroyViewEv")) {
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

  //  void QtVirtualKeyboard::AppInputPanel::show()
  void show() override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AppInputPanelCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::AppInputPanel::show();
  }

  //  void QtVirtualKeyboard::AppInputPanel::hide()
  void hide() override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AppInputPanelCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::AppInputPanel::hide();
  }

  //  bool QtVirtualKeyboard::AppInputPanel::isVisible() const
  bool isVisible() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AppInputPanelCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::AppInputPanel::isVisible();
  }

  //  void QtVirtualKeyboard::AbstractInputPanel::setInputRect(const QRect
  //      &inputRect)
  void setInputRect(const QRect &inputRect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AppInputPanelCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall3>(taken[3]);
      call(this, &inputRect, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::AbstractInputPanel::setInputRect(inputRect);
  }

  //  void QtVirtualKeyboard::AbstractInputPanel::createView()
  void createView() override {
    if (taken[4]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AppInputPanelCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::AbstractInputPanel::createView();
  }

  //  void QtVirtualKeyboard::AbstractInputPanel::destroyView()
  void destroyView() override {
    if (taken[5]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AppInputPanelCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::AbstractInputPanel::destroyView();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AppInputPanelCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall6>(taken[6]);
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
      CuteQtVirtualKeyboard_AppInputPanelCall7 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall7>(taken[7]);
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
      CuteQtVirtualKeyboard_AppInputPanelCall8 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall8>(taken[8]);
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
      CuteQtVirtualKeyboard_AppInputPanelCall9 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall9>(taken[9]);
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
      CuteQtVirtualKeyboard_AppInputPanelCall10 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall10>(taken[10]);
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
      CuteQtVirtualKeyboard_AppInputPanelCall11 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall11>(taken[11]);
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
      CuteQtVirtualKeyboard_AppInputPanelCall12 call = reinterpret_cast<CuteQtVirtualKeyboard_AppInputPanelCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::AppInputPanel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard13AppInputPanel10metaObjectEv(
    const QtVirtualKeyboard::AppInputPanel *self) {
  return self->metaObject();
}

//  QString QtVirtualKeyboard::AppInputPanel::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard13AppInputPanel2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::AppInputPanel::tr(s, c, n));
}

//  AppInputPanelPrivate *QtVirtualKeyboard::AppInputPanel::d_func()
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::AppInputPanelPrivate *ritual_ZN17QtVirtualKeyboard13AppInputPanel6d_funcEv(
    QtVirtualKeyboard::AppInputPanel *self) {
  return self->d_func();
}

//  const AppInputPanelPrivate *QtVirtualKeyboard::AppInputPanel::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QtVirtualKeyboard::AppInputPanelPrivate *ritual_ZNK17QtVirtualKeyboard13AppInputPanel6d_funcEv(
    const QtVirtualKeyboard::AppInputPanel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQtVirtualKeyboard_AppInputPanel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_AppInputPanel(
    QtVirtualKeyboard::AppInputPanel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_AppInputPanel *>(self)->take(key, call);
}

//  void QtVirtualKeyboard::AppInputPanel::show()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard13AppInputPanel4showEv(
    QtVirtualKeyboard::AppInputPanel *self) {
  self->QtVirtualKeyboard::AppInputPanel::show();
}

//  void QtVirtualKeyboard::AppInputPanel::hide()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard13AppInputPanel4hideEv(
    QtVirtualKeyboard::AppInputPanel *self) {
  self->QtVirtualKeyboard::AppInputPanel::hide();
}

//  bool QtVirtualKeyboard::AppInputPanel::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QtVirtualKeyboard13AppInputPanel9isVisibleEv(
    const QtVirtualKeyboard::AppInputPanel *self) {
  return self->QtVirtualKeyboard::AppInputPanel::isVisible();
}
