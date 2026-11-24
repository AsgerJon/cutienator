//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/desktopinputpanel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/qvirtualkeyboard_global.h>
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#if QT_CONFIG(vkb_desktop)
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/desktopinputpanel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtVirtualKeyboard::DesktopInputPanel that Python can take functions over in. Every QtVirtualKeyboard::DesktopInputPanel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall0)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall1)(const void *, int *);
typedef bool (*CuteQtVirtualKeyboard_DesktopInputPanelCall2)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall3)(const void *, const QRect *, int *);
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall4)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_DesktopInputPanelCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_DesktopInputPanelCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputPanelCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_DesktopInputPanel : public QtVirtualKeyboard::DesktopInputPanel {
public:
  using QtVirtualKeyboard::DesktopInputPanel::DesktopInputPanel;
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

  //  void QtVirtualKeyboard::DesktopInputPanel::show()
  void show() override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputPanelCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::DesktopInputPanel::show();
  }

  //  void QtVirtualKeyboard::DesktopInputPanel::hide()
  void hide() override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputPanelCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::DesktopInputPanel::hide();
  }

  //  bool QtVirtualKeyboard::DesktopInputPanel::isVisible() const
  bool isVisible() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputPanelCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::DesktopInputPanel::isVisible();
  }

  //  void QtVirtualKeyboard::DesktopInputPanel::setInputRect(const QRect
  //      &inputRect)
  void setInputRect(const QRect &inputRect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputPanelCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall3>(taken[3]);
      call(this, &inputRect, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::DesktopInputPanel::setInputRect(inputRect);
  }

  //  void QtVirtualKeyboard::DesktopInputPanel::createView()
  void createView() override {
    if (taken[4]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputPanelCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::DesktopInputPanel::createView();
  }

  //  void QtVirtualKeyboard::DesktopInputPanel::destroyView()
  void destroyView() override {
    if (taken[5]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputPanelCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::DesktopInputPanel::destroyView();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputPanelCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall6>(taken[6]);
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
      CuteQtVirtualKeyboard_DesktopInputPanelCall7 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall7>(taken[7]);
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
      CuteQtVirtualKeyboard_DesktopInputPanelCall8 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall8>(taken[8]);
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
      CuteQtVirtualKeyboard_DesktopInputPanelCall9 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall9>(taken[9]);
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
      CuteQtVirtualKeyboard_DesktopInputPanelCall10 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall10>(taken[10]);
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
      CuteQtVirtualKeyboard_DesktopInputPanelCall11 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall11>(taken[11]);
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
      CuteQtVirtualKeyboard_DesktopInputPanelCall12 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputPanelCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::DesktopInputPanel::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard17DesktopInputPanel10metaObjectEv(
    const QtVirtualKeyboard::DesktopInputPanel *self) {
  return self->metaObject();
}

//  QString QtVirtualKeyboard::DesktopInputPanel::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard17DesktopInputPanel2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::DesktopInputPanel::tr(s, c, n));
}

//  a Python function taken by a CuteQtVirtualKeyboard_DesktopInputPanel, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_DesktopInputPanel(
    QtVirtualKeyboard::DesktopInputPanel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_DesktopInputPanel *>(self)->take(key, call);
}

//  void QtVirtualKeyboard::DesktopInputPanel::show()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel4showEv(
    QtVirtualKeyboard::DesktopInputPanel *self) {
  self->QtVirtualKeyboard::DesktopInputPanel::show();
}

//  void QtVirtualKeyboard::DesktopInputPanel::hide()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel4hideEv(
    QtVirtualKeyboard::DesktopInputPanel *self) {
  self->QtVirtualKeyboard::DesktopInputPanel::hide();
}

//  bool QtVirtualKeyboard::DesktopInputPanel::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QtVirtualKeyboard17DesktopInputPanel9isVisibleEv(
    const QtVirtualKeyboard::DesktopInputPanel *self) {
  return self->QtVirtualKeyboard::DesktopInputPanel::isVisible();
}

//  void QtVirtualKeyboard::DesktopInputPanel::setInputRect(const QRect
//      &inputRect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel12setInputRectERK5QRect(
    QtVirtualKeyboard::DesktopInputPanel *self,
    const QRect *inputRect) {
  self->QtVirtualKeyboard::DesktopInputPanel::setInputRect(*inputRect);
}

//  void QtVirtualKeyboard::DesktopInputPanel::createView()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel10createViewEv(
    QtVirtualKeyboard::DesktopInputPanel *self) {
  self->QtVirtualKeyboard::DesktopInputPanel::createView();
}

//  void QtVirtualKeyboard::DesktopInputPanel::destroyView()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard17DesktopInputPanel11destroyViewEv(
    QtVirtualKeyboard::DesktopInputPanel *self) {
  self->QtVirtualKeyboard::DesktopInputPanel::destroyView();
}

#endif  // QT_CONFIG(vkb_desktop)
