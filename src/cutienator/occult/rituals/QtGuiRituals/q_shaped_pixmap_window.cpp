//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qshapedpixmapdndwindow_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qshapedpixmapdndwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qshapedpixmapdndwindow_p.h"
#include <QtGui/QPainter>
#include <QtGui/QCursor>
#include <QtGui/QGuiApplication>
#include <QtGui/QPalette>
#include <QtGui/QBitmap>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/kernel/qshapedpixmapdndwindow.cpp, line 28, as _ZN19QShapedPixmapWindowD1Ev
inline QShapedPixmapWindow::~QShapedPixmapWindow()
{
}

//  from src/gui/kernel/qshapedpixmapdndwindow.cpp, line 50, as _ZN19QShapedPixmapWindow10setHotspotERK6QPoint
inline void QShapedPixmapWindow::setHotspot(const QPoint &hotspot)
{
    m_hotSpot = hotspot;
}

//  from src/gui/kernel/qshapedpixmapdndwindow.cpp, line 68, as _ZN19QShapedPixmapWindow14updateGeometryERK6QPoint
inline void QShapedPixmapWindow::updateGeometry(const QPoint &pos)
{
    QSize size(1, 1);
    if (!m_pixmap.isNull()) {
        size = m_pixmap.deviceIndependentSize().toSize();
    }
    setGeometry(QRect(pos - m_hotSpot, size));
}

//  from src/gui/kernel/qshapedpixmapdndwindow.cpp, line 55, as _ZN19QShapedPixmapWindow10paintEventEP11QPaintEvent
inline void QShapedPixmapWindow::paintEvent(QPaintEvent *)
{
    if (!m_pixmap.isNull()) {
        const QRect rect(QPoint(0, 0), size());
        QPainter painter(this);
        if (m_useCompositing)
            painter.setCompositionMode(QPainter::CompositionMode_Source);
        else
            painter.fillRect(rect, QGuiApplication::palette().base());
        painter.drawPixmap(rect, m_pixmap);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QShapedPixmapWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQShapedPixmapWindow : QShapedPixmapWindow {
  using QShapedPixmapWindow::paintEvent;
};

//  A QShapedPixmapWindow that Python can take functions over in. Every QShapedPixmapWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(draganddrop)
typedef void (*CuteQShapedPixmapWindowCall0)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef int (*CuteQShapedPixmapWindowCall1)(const void *, int, int *);
typedef void * (*CuteQShapedPixmapWindowCall2)(const void *, QPoint *, int *);
typedef void (*CuteQShapedPixmapWindowCall3)(const void *, QResizeEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall4)(const void *, QExposeEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQShapedPixmapWindowCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQShapedPixmapWindowCall6)(const void *, int *);
typedef int (*CuteQShapedPixmapWindowCall7)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQShapedPixmapWindowCall8)(const void *, int *);
typedef const QSize * (*CuteQShapedPixmapWindowCall9)(const void *, int *);
typedef void * (*CuteQShapedPixmapWindowCall10)(const void *, int *);
typedef void * (*CuteQShapedPixmapWindowCall11)(const void *, int *);
typedef void (*CuteQShapedPixmapWindowCall12)(const void *, QMoveEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall13)(const void *, QFocusEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall15)(const void *, QShowEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall16)(const void *, QHideEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall17)(const void *, QCloseEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQShapedPixmapWindowCall23)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQShapedPixmapWindowCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQShapedPixmapWindowCall25)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQShapedPixmapWindowCall26)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQShapedPixmapWindowCall27)(const void *, int *);
typedef int (*CuteQShapedPixmapWindowCall28)(const void *, int *);
typedef void (*CuteQShapedPixmapWindowCall29)(const void *, QPainter *, int *);
typedef void * (*CuteQShapedPixmapWindowCall30)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQShapedPixmapWindowCall31)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShapedPixmapWindowCall32)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShapedPixmapWindowCall33)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShapedPixmapWindowCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShapedPixmapWindowCall35)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQShapedPixmapWindowCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQShapedPixmapWindow : public QShapedPixmapWindow {
public:
  using QShapedPixmapWindow::QShapedPixmapWindow;
  void *taken[37] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK8QSurface13surfaceHandleEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[30] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(draganddrop)
  //  void QShapedPixmapWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall0 call = reinterpret_cast<CuteQShapedPixmapWindowCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QShapedPixmapWindow::paintEvent(a0);
  }
#endif  // QT_CONFIG(draganddrop)

  //  int QRasterWindow::metric(PaintDeviceMetric metric) const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall1 call = reinterpret_cast<CuteQShapedPixmapWindowCall1>(taken[1]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QRasterWindow::metric(metric);
  }

  //  QPaintDevice *QRasterWindow::redirected(QPoint *a0) const
  QPaintDevice *redirected(QPoint *a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall2 call = reinterpret_cast<CuteQShapedPixmapWindowCall2>(taken[2]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QRasterWindow::redirected(a0);
  }

  //  void QRasterWindow::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall3 call = reinterpret_cast<CuteQShapedPixmapWindowCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QRasterWindow::resizeEvent(event);
  }

  //  void QPaintDeviceWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall4 call = reinterpret_cast<CuteQShapedPixmapWindowCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPaintDeviceWindow::exposeEvent(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QPaintDeviceWindow::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall5 call = reinterpret_cast<CuteQShapedPixmapWindowCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QPaintDeviceWindow::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QPaintEngine *QPaintDeviceWindow::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall6 call = reinterpret_cast<CuteQShapedPixmapWindowCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintDeviceWindow::paintEngine();
  }

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall7 call = reinterpret_cast<CuteQShapedPixmapWindowCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall8 call = reinterpret_cast<CuteQShapedPixmapWindowCall8>(taken[8]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall9 call = reinterpret_cast<CuteQShapedPixmapWindowCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall10 call = reinterpret_cast<CuteQShapedPixmapWindowCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall11 call = reinterpret_cast<CuteQShapedPixmapWindowCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall12 call = reinterpret_cast<CuteQShapedPixmapWindowCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall13 call = reinterpret_cast<CuteQShapedPixmapWindowCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall14 call = reinterpret_cast<CuteQShapedPixmapWindowCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall15 call = reinterpret_cast<CuteQShapedPixmapWindowCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall16 call = reinterpret_cast<CuteQShapedPixmapWindowCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall17 call = reinterpret_cast<CuteQShapedPixmapWindowCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall18 call = reinterpret_cast<CuteQShapedPixmapWindowCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall19 call = reinterpret_cast<CuteQShapedPixmapWindowCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

  //  void QWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall20 call = reinterpret_cast<CuteQShapedPixmapWindowCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mousePressEvent(a0);
  }

  //  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall21 call = reinterpret_cast<CuteQShapedPixmapWindowCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseReleaseEvent(a0);
  }

  //  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall22 call = reinterpret_cast<CuteQShapedPixmapWindowCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseDoubleClickEvent(a0);
  }

  //  void QWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall23 call = reinterpret_cast<CuteQShapedPixmapWindowCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseMoveEvent(a0);
  }

#if QT_CONFIG(wheelevent)
  //  void QWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall24 call = reinterpret_cast<CuteQShapedPixmapWindowCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall25 call = reinterpret_cast<CuteQShapedPixmapWindowCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

#if QT_CONFIG(tabletevent)
  //  void QWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall26 call = reinterpret_cast<CuteQShapedPixmapWindowCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall27 call = reinterpret_cast<CuteQShapedPixmapWindowCall27>(taken[27]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurface *>(given);
    }
    return QWindow::surfaceHandle();
  }

  //  int QPaintDevice::devType() const
  int devType() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall28 call = reinterpret_cast<CuteQShapedPixmapWindowCall28>(taken[28]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintDevice::devType();
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall29 call = reinterpret_cast<CuteQShapedPixmapWindowCall29>(taken[29]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall30 call = reinterpret_cast<CuteQShapedPixmapWindowCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall31 call = reinterpret_cast<CuteQShapedPixmapWindowCall31>(taken[31]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall32 call = reinterpret_cast<CuteQShapedPixmapWindowCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall33 call = reinterpret_cast<CuteQShapedPixmapWindowCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall34 call = reinterpret_cast<CuteQShapedPixmapWindowCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[35]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall35 call = reinterpret_cast<CuteQShapedPixmapWindowCall35>(taken[35]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[36]) {
      int handled = 0;
      CuteQShapedPixmapWindowCall36 call = reinterpret_cast<CuteQShapedPixmapWindowCall36>(taken[36]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QShapedPixmapWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QShapedPixmapWindow10metaObjectEv(
    const QShapedPixmapWindow *self) {
  return self->metaObject();
}

//  QShapedPixmapWindow::~QShapedPixmapWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QShapedPixmapWindowD1Ev(QShapedPixmapWindow *self) {
  delete self;
}

//  void QShapedPixmapWindow::setUseCompositing(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QShapedPixmapWindow17setUseCompositingEb(
    QShapedPixmapWindow *self,
    bool on) {
  self->setUseCompositing(on);
}

//  void QShapedPixmapWindow::setHotspot(const QPoint &hotspot)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QShapedPixmapWindow10setHotspotERK6QPoint(
    QShapedPixmapWindow *self,
    const QPoint *hotspot) {
  self->setHotspot(*hotspot);
}

//  void QShapedPixmapWindow::updateGeometry(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QShapedPixmapWindow14updateGeometryERK6QPoint(
    QShapedPixmapWindow *self,
    const QPoint *pos) {
  self->updateGeometry(*pos);
}

//  void QShapedPixmapWindow::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QShapedPixmapWindow10paintEventEP11QPaintEvent(
    QShapedPixmapWindow *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  a Python function taken by a CuteQShapedPixmapWindow, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QShapedPixmapWindow(
    QShapedPixmapWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQShapedPixmapWindow *>(self)->take(key, call);
}

//  void QShapedPixmapWindow::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QShapedPixmapWindow10paintEventEP11QPaintEvent(
    QShapedPixmapWindow *self,
    QPaintEvent *a0) {
  static_cast<OwnQShapedPixmapWindow *>(self)->OwnQShapedPixmapWindow::paintEvent(
      a0);
}

#endif  // QT_CONFIG(draganddrop)
