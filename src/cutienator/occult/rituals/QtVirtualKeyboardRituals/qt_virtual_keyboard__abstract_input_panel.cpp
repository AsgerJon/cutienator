//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/abstractinputpanel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/abstractinputpanel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtVirtualKeyboard::AbstractInputPanel that Python can take functions over in. Every QtVirtualKeyboard::AbstractInputPanel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall0)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall1)(const void *, int *);
typedef bool (*CuteQtVirtualKeyboard_AbstractInputPanelCall2)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall3)(const void *, const QRect *, int *);
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall4)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_AbstractInputPanelCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_AbstractInputPanelCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_AbstractInputPanelCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_AbstractInputPanel : public QtVirtualKeyboard::AbstractInputPanel {
public:
  using QtVirtualKeyboard::AbstractInputPanel::AbstractInputPanel;
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

  //  void QtVirtualKeyboard::AbstractInputPanel::show()
  void show() override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AbstractInputPanelCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QtVirtualKeyboard::AbstractInputPanel::hide()
  void hide() override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AbstractInputPanelCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QtVirtualKeyboard::AbstractInputPanel::isVisible() const
  bool isVisible() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AbstractInputPanelCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QtVirtualKeyboard::AbstractInputPanel::setInputRect(const QRect
  //      &inputRect)
  void setInputRect(const QRect &inputRect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AbstractInputPanelCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall3>(taken[3]);
      call(this, &inputRect, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::AbstractInputPanel::setInputRect(inputRect);
  }

  //  void QtVirtualKeyboard::AbstractInputPanel::createView()
  void createView() override {
    if (taken[4]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AbstractInputPanelCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::AbstractInputPanel::createView();
  }

  //  void QtVirtualKeyboard::AbstractInputPanel::destroyView()
  void destroyView() override {
    if (taken[5]) {
      int handled = 0;
      CuteQtVirtualKeyboard_AbstractInputPanelCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall5>(taken[5]);
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
      CuteQtVirtualKeyboard_AbstractInputPanelCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall6>(taken[6]);
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
      CuteQtVirtualKeyboard_AbstractInputPanelCall7 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall7>(taken[7]);
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
      CuteQtVirtualKeyboard_AbstractInputPanelCall8 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall8>(taken[8]);
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
      CuteQtVirtualKeyboard_AbstractInputPanelCall9 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall9>(taken[9]);
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
      CuteQtVirtualKeyboard_AbstractInputPanelCall10 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall10>(taken[10]);
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
      CuteQtVirtualKeyboard_AbstractInputPanelCall11 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall11>(taken[11]);
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
      CuteQtVirtualKeyboard_AbstractInputPanelCall12 call = reinterpret_cast<CuteQtVirtualKeyboard_AbstractInputPanelCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::AbstractInputPanel::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard18AbstractInputPanel10metaObjectEv(
    const QtVirtualKeyboard::AbstractInputPanel *self) {
  return self->metaObject();
}

//  void *QtVirtualKeyboard::AbstractInputPanel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard18AbstractInputPanel11qt_metacastEPKc(
    QtVirtualKeyboard::AbstractInputPanel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtVirtualKeyboard::AbstractInputPanel::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard18AbstractInputPanel11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::AbstractInputPanel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtVirtualKeyboard::AbstractInputPanel::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard18AbstractInputPanel2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::AbstractInputPanel::tr(s, c, n));
}

//  QtVirtualKeyboard::AbstractInputPanel::AbstractInputPanel(QObjectPrivate
//      &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::AbstractInputPanel *ritual_ZN17QtVirtualKeyboard18AbstractInputPanelC1ER14QObjectPrivateP7QObject(
    QObjectPrivate *dd,
    QObject *parent) {
  return new CuteQtVirtualKeyboard_AbstractInputPanel(*dd, parent);
}

//  QtVirtualKeyboard::AbstractInputPanel::AbstractInputPanel(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::AbstractInputPanel *ritual_ZN17QtVirtualKeyboard18AbstractInputPanelC1EP7QObject(
    QObject *parent) {
  return new CuteQtVirtualKeyboard_AbstractInputPanel(parent);
}

//  QtVirtualKeyboard::AbstractInputPanel::~AbstractInputPanel()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18AbstractInputPanelD1Ev(
    QtVirtualKeyboard::AbstractInputPanel *self) {
  delete self;
}

//  void QtVirtualKeyboard::AbstractInputPanel::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18AbstractInputPanel4showEv(
    QtVirtualKeyboard::AbstractInputPanel *self) {
  self->show();
}

//  void QtVirtualKeyboard::AbstractInputPanel::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18AbstractInputPanel4hideEv(
    QtVirtualKeyboard::AbstractInputPanel *self) {
  self->hide();
}

//  bool QtVirtualKeyboard::AbstractInputPanel::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard18AbstractInputPanel9isVisibleEv(
    const QtVirtualKeyboard::AbstractInputPanel *self) {
  return self->isVisible();
}

//  void QtVirtualKeyboard::AbstractInputPanel::setInputRect(const QRect
//      &inputRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18AbstractInputPanel12setInputRectERK5QRect(
    QtVirtualKeyboard::AbstractInputPanel *self,
    const QRect *inputRect) {
  self->setInputRect(*inputRect);
}

//  void QtVirtualKeyboard::AbstractInputPanel::createView()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18AbstractInputPanel10createViewEv(
    QtVirtualKeyboard::AbstractInputPanel *self) {
  self->createView();
}

//  void QtVirtualKeyboard::AbstractInputPanel::destroyView()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18AbstractInputPanel11destroyViewEv(
    QtVirtualKeyboard::AbstractInputPanel *self) {
  self->destroyView();
}

//  a Python function taken by a CuteQtVirtualKeyboard_AbstractInputPanel,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_AbstractInputPanel(
    QtVirtualKeyboard::AbstractInputPanel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_AbstractInputPanel *>(self)->take(key, call);
}

//  void QtVirtualKeyboard::AbstractInputPanel::setInputRect(const QRect
//      &inputRect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard18AbstractInputPanel12setInputRectERK5QRect(
    QtVirtualKeyboard::AbstractInputPanel *self,
    const QRect *inputRect) {
  self->QtVirtualKeyboard::AbstractInputPanel::setInputRect(*inputRect);
}

//  void QtVirtualKeyboard::AbstractInputPanel::createView()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard18AbstractInputPanel10createViewEv(
    QtVirtualKeyboard::AbstractInputPanel *self) {
  self->QtVirtualKeyboard::AbstractInputPanel::createView();
}

//  void QtVirtualKeyboard::AbstractInputPanel::destroyView()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard18AbstractInputPanel11destroyViewEv(
    QtVirtualKeyboard::AbstractInputPanel *self) {
  self->QtVirtualKeyboard::AbstractInputPanel::destroyView();
}
