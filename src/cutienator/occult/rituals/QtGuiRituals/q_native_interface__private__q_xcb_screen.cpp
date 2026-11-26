//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformscreen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(xcb) || defined(Q_QDOC)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformscreen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QNativeInterface::Private::QXcbScreen that Python can take functions over in. Every QNativeInterface::Private::QXcbScreen
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(xcb) || defined(Q_QDOC)
typedef int (*CuteQNativeInterface_Private_QXcbScreenCall0)(const void *, int *);
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
class CuteQNativeInterface_Private_QXcbScreen : public QNativeInterface::Private::QXcbScreen {
public:
  using QNativeInterface::Private::QXcbScreen::QXcbScreen;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(xcb) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface7Private10QXcbScreen20virtualDesktopNumberEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(xcb) || defined(Q_QDOC)
  //  int QNativeInterface::Private::QXcbScreen::virtualDesktopNumber()
  //      const
  int virtualDesktopNumber() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_Private_QXcbScreenCall0 call = reinterpret_cast<CuteQNativeInterface_Private_QXcbScreenCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
};

//  QNativeInterface::Private::QXcbScreen::~QXcbScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private10QXcbScreenD1Ev(
    QNativeInterface::Private::QXcbScreen *self) {
  delete self;
}

//  QNativeInterface::Private::QXcbScreen::QXcbScreen()
extern "C" Q_DECL_EXPORT
QNativeInterface::Private::QXcbScreen *ritual_ZN16QNativeInterface7Private10QXcbScreenC1Ev() {
  return new CuteQNativeInterface_Private_QXcbScreen();
}

//  int QNativeInterface::Private::QXcbScreen::virtualDesktopNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QNativeInterface7Private10QXcbScreen20virtualDesktopNumberEv(
    const QNativeInterface::Private::QXcbScreen *self) {
  return self->virtualDesktopNumber();
}

//  a Python function taken by a CuteQNativeInterface_Private_QXcbScreen, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_Private_QXcbScreen(
    QNativeInterface::Private::QXcbScreen *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_Private_QXcbScreen *>(self)->take(key, call);
}

#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
