//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformwindow_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(xcb) || defined(Q_QDOC)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QNativeInterface::Private::QXcbWindow that Python can take functions over in. Every QNativeInterface::Private::QXcbWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(xcb) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_Private_QXcbWindowCall0)(const void *, int, int *);
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
#if QT_CONFIG(xcb) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_Private_QXcbWindowCall1)(const void *, const QString *, int *);
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
#if QT_CONFIG(xcb) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_Private_QXcbWindowCall2)(const void *, const QString *, int *);
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
#if QT_CONFIG(xcb) || defined(Q_QDOC)
typedef uint (*CuteQNativeInterface_Private_QXcbWindowCall3)(const void *, int *);
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
class CuteQNativeInterface_Private_QXcbWindow : public QNativeInterface::Private::QXcbWindow {
public:
  using QNativeInterface::Private::QXcbWindow::QXcbWindow;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(xcb) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private10QXcbWindow13setWindowTypeE6QFlagsINS1_10WindowTypeEE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
#if QT_CONFIG(xcb) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private10QXcbWindow13setWindowRoleERK7QString")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
#if QT_CONFIG(xcb) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private10QXcbWindow17setWindowIconTextERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
#if QT_CONFIG(xcb) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface7Private10QXcbWindow8visualIdEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(xcb) || defined(Q_QDOC)
  //  void QNativeInterface::Private::QXcbWindow::setWindowType(WindowTypes
  //      type)
  void setWindowType(
      QNativeInterface::Private::QXcbWindow::WindowTypes type) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_Private_QXcbWindowCall0 call = reinterpret_cast<CuteQNativeInterface_Private_QXcbWindowCall0>(taken[0]);
      call(this, static_cast<int>(type.toInt()), &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)

#if QT_CONFIG(xcb) || defined(Q_QDOC)
  //  void QNativeInterface::Private::QXcbWindow::setWindowRole(const
  //      QString &role)
  void setWindowRole(const QString &role) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeInterface_Private_QXcbWindowCall1 call = reinterpret_cast<CuteQNativeInterface_Private_QXcbWindowCall1>(taken[1]);
      call(this, &role, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)

#if QT_CONFIG(xcb) || defined(Q_QDOC)
  //  void QNativeInterface::Private::QXcbWindow::setWindowIconText(const
  //      QString &text)
  void setWindowIconText(const QString &text) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNativeInterface_Private_QXcbWindowCall2 call = reinterpret_cast<CuteQNativeInterface_Private_QXcbWindowCall2>(taken[2]);
      call(this, &text, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)

#if QT_CONFIG(xcb) || defined(Q_QDOC)
  //  uint QNativeInterface::Private::QXcbWindow::visualId() const
  uint visualId() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNativeInterface_Private_QXcbWindowCall3 call = reinterpret_cast<CuteQNativeInterface_Private_QXcbWindowCall3>(taken[3]);
      uint given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
};

//  QNativeInterface::Private::QXcbWindow::~QXcbWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private10QXcbWindowD1Ev(
    QNativeInterface::Private::QXcbWindow *self) {
  delete self;
}

//  void QNativeInterface::Private::QXcbWindow::setWindowType(WindowTypes
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private10QXcbWindow13setWindowTypeE6QFlagsINS1_10WindowTypeEE(
    QNativeInterface::Private::QXcbWindow *self,
    int type) {
  self->setWindowType(
      QFlags<QNativeInterface::Private::QXcbWindow::WindowType>::fromInt(type));
}

//  void QNativeInterface::Private::QXcbWindow::setWindowRole(const QString
//      &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private10QXcbWindow13setWindowRoleERK7QString(
    QNativeInterface::Private::QXcbWindow *self,
    const QString *role) {
  self->setWindowRole(*role);
}

//  void QNativeInterface::Private::QXcbWindow::setWindowIconText(const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private10QXcbWindow17setWindowIconTextERK7QString(
    QNativeInterface::Private::QXcbWindow *self,
    const QString *text) {
  self->setWindowIconText(*text);
}

//  uint QNativeInterface::Private::QXcbWindow::visualId() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK16QNativeInterface7Private10QXcbWindow8visualIdEv(
    const QNativeInterface::Private::QXcbWindow *self) {
  return self->visualId();
}

//  a Python function taken by a CuteQNativeInterface_Private_QXcbWindow, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_Private_QXcbWindow(
    QNativeInterface::Private::QXcbWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_Private_QXcbWindow *>(self)->take(key, call);
}

#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
