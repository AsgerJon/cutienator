//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformscreen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformscreen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QNativeInterface::Private::QVsp2Screen that Python can take functions over in. Every QNativeInterface::Private::QVsp2Screen
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
typedef int (*CuteQNativeInterface_Private_QVsp2ScreenCall0)(const void *, int, const QSize *, const QPoint *, uint, uint, int *);
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_Private_QVsp2ScreenCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_Private_QVsp2ScreenCall2)(const void *, int, const QPoint *, int *);
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_Private_QVsp2ScreenCall3)(const void *, int, qreal, int *);
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
typedef bool (*CuteQNativeInterface_Private_QVsp2ScreenCall4)(const void *, int, int *);
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
class CuteQNativeInterface_Private_QVsp2Screen : public QNativeInterface::Private::QVsp2Screen {
public:
  using QNativeInterface::Private::QVsp2Screen::QVsp2Screen;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private11QVsp2Screen8addLayerEiRK5QSizeRK6QPointjj")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private11QVsp2Screen14setLayerBufferEii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private11QVsp2Screen16setLayerPositionEiRK6QPoint")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private11QVsp2Screen13setLayerAlphaEid")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
#if QT_CONFIG(vsp2) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private11QVsp2Screen11removeLayerEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(vsp2) || defined(Q_QDOC)
  //  int QNativeInterface::Private::QVsp2Screen::addLayer(int dmabufFd,
  //      const QSize &size, const QPoint &position, uint drmPixelFormat,
  //      uint bytesPerLine)
  int addLayer(
      int dmabufFd,
      const QSize &size,
      const QPoint &position,
      uint drmPixelFormat,
      uint bytesPerLine) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_Private_QVsp2ScreenCall0 call = reinterpret_cast<CuteQNativeInterface_Private_QVsp2ScreenCall0>(taken[0]);
      int given = call(this, dmabufFd, &size, &position, drmPixelFormat, bytesPerLine, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)

#if QT_CONFIG(vsp2) || defined(Q_QDOC)
  //  void QNativeInterface::Private::QVsp2Screen::setLayerBuffer(int id,
  //      int dmabufFd)
  void setLayerBuffer(int id, int dmabufFd) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeInterface_Private_QVsp2ScreenCall1 call = reinterpret_cast<CuteQNativeInterface_Private_QVsp2ScreenCall1>(taken[1]);
      call(this, id, dmabufFd, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)

#if QT_CONFIG(vsp2) || defined(Q_QDOC)
  //  void QNativeInterface::Private::QVsp2Screen::setLayerPosition(int id,
  //      const QPoint &position)
  void setLayerPosition(int id, const QPoint &position) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNativeInterface_Private_QVsp2ScreenCall2 call = reinterpret_cast<CuteQNativeInterface_Private_QVsp2ScreenCall2>(taken[2]);
      call(this, id, &position, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)

#if QT_CONFIG(vsp2) || defined(Q_QDOC)
  //  void QNativeInterface::Private::QVsp2Screen::setLayerAlpha(int id,
  //      qreal alpha)
  void setLayerAlpha(int id, qreal alpha) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNativeInterface_Private_QVsp2ScreenCall3 call = reinterpret_cast<CuteQNativeInterface_Private_QVsp2ScreenCall3>(taken[3]);
      call(this, id, alpha, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)

#if QT_CONFIG(vsp2) || defined(Q_QDOC)
  //  bool QNativeInterface::Private::QVsp2Screen::removeLayer(int id)
  bool removeLayer(int id) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNativeInterface_Private_QVsp2ScreenCall4 call = reinterpret_cast<CuteQNativeInterface_Private_QVsp2ScreenCall4>(taken[4]);
      bool given = call(this, id, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
};

//  QNativeInterface::Private::QVsp2Screen::~QVsp2Screen()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private11QVsp2ScreenD1Ev(
    QNativeInterface::Private::QVsp2Screen *self) {
  delete self;
}

//  int QNativeInterface::Private::QVsp2Screen::addLayer(int dmabufFd, const
//      QSize &size, const QPoint &position, uint drmPixelFormat, uint
//      bytesPerLine)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QNativeInterface7Private11QVsp2Screen8addLayerEiRK5QSizeRK6QPointjj(
    QNativeInterface::Private::QVsp2Screen *self,
    int dmabufFd,
    const QSize *size,
    const QPoint *position,
    uint drmPixelFormat,
    uint bytesPerLine) {
  return self->addLayer(
      dmabufFd,
      *size,
      *position,
      drmPixelFormat,
      bytesPerLine);
}

//  void QNativeInterface::Private::QVsp2Screen::setLayerBuffer(int id, int
//      dmabufFd)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private11QVsp2Screen14setLayerBufferEii(
    QNativeInterface::Private::QVsp2Screen *self,
    int id,
    int dmabufFd) {
  self->setLayerBuffer(id, dmabufFd);
}

//  void QNativeInterface::Private::QVsp2Screen::setLayerPosition(int id,
//      const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private11QVsp2Screen16setLayerPositionEiRK6QPoint(
    QNativeInterface::Private::QVsp2Screen *self,
    int id,
    const QPoint *position) {
  self->setLayerPosition(id, *position);
}

//  void QNativeInterface::Private::QVsp2Screen::setLayerAlpha(int id, qreal
//      alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private11QVsp2Screen13setLayerAlphaEid(
    QNativeInterface::Private::QVsp2Screen *self,
    int id,
    qreal alpha) {
  self->setLayerAlpha(id, alpha);
}

//  bool QNativeInterface::Private::QVsp2Screen::removeLayer(int id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QNativeInterface7Private11QVsp2Screen11removeLayerEi(
    QNativeInterface::Private::QVsp2Screen *self,
    int id) {
  return self->removeLayer(id);
}

//  void QNativeInterface::Private::QVsp2Screen::addBlendListener(void (*)()
//      callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private11QVsp2Screen16addBlendListenerEPFvvE(
    QNativeInterface::Private::QVsp2Screen *self,
    void *callback) {
  self->addBlendListener(reinterpret_cast<void (*)()>(callback));
}

//  a Python function taken by a CuteQNativeInterface_Private_QVsp2Screen,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_Private_QVsp2Screen(
    QNativeInterface::Private::QVsp2Screen *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_Private_QVsp2Screen *>(self)->take(key, call);
}

#endif  // QT_CONFIG(vsp2) || defined(Q_QDOC)
