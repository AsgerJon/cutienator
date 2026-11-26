//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvulkanwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(vulkan)
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || defined(Q_QDOC)
#include <QtGui/QtGui>
#include <QtGui/qvulkanwindow.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#include <QtGui/QVulkanInfoVector>
#include <QtGui/QVulkanExtension>
#include <QtGui/QVulkanWindow>

//  Only a class built on QVulkanWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQVulkanWindow : QVulkanWindow {
  using QVulkanWindow::exposeEvent;
  using QVulkanWindow::resizeEvent;
  using QVulkanWindow::event;
};

//  A QVulkanWindow that Python can take functions over in. Every QVulkanWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void * (*CuteQVulkanWindowCall0)(const void *, int *);
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowCall1)(const void *, QExposeEvent *, int *);
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowCall2)(const void *, QResizeEvent *, int *);
#endif
#if !defined(QT_NO_QOBJECT)
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef bool (*CuteQVulkanWindowCall3)(const void *, QEvent *, int *);
#endif
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQVulkanWindowCall4)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQVulkanWindowCall5)(const void *, int *);
typedef const QSize * (*CuteQVulkanWindowCall6)(const void *, int *);
typedef void * (*CuteQVulkanWindowCall7)(const void *, int *);
typedef void * (*CuteQVulkanWindowCall8)(const void *, int *);
typedef void (*CuteQVulkanWindowCall9)(const void *, QPaintEvent *, int *);
typedef void (*CuteQVulkanWindowCall10)(const void *, QMoveEvent *, int *);
typedef void (*CuteQVulkanWindowCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQVulkanWindowCall12)(const void *, QFocusEvent *, int *);
typedef void (*CuteQVulkanWindowCall13)(const void *, QShowEvent *, int *);
typedef void (*CuteQVulkanWindowCall14)(const void *, QHideEvent *, int *);
typedef void (*CuteQVulkanWindowCall15)(const void *, QCloseEvent *, int *);
typedef void (*CuteQVulkanWindowCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQVulkanWindowCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQVulkanWindowCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQVulkanWindowCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQVulkanWindowCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQVulkanWindowCall21)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQVulkanWindowCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQVulkanWindowCall23)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQVulkanWindowCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQVulkanWindowCall25)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVulkanWindowCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVulkanWindowCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVulkanWindowCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVulkanWindowCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVulkanWindowCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVulkanWindowCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVulkanWindow : public QVulkanWindow {
public:
  using QVulkanWindow::QVulkanWindow;
  void *taken[32] = {};

  bool take(const char *key, void *call) {
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN13QVulkanWindow14createRendererEv")) {
      taken[0] = call;
      return true;
    }
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[1] = call;
      return true;
    }
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[2] = call;
      return true;
    }
#endif
#if !defined(QT_NO_QOBJECT)
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK8QSurface13surfaceHandleEv")) {
      taken[25] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  QVulkanWindowRenderer *QVulkanWindow::createRenderer()
  QVulkanWindowRenderer *createRenderer() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVulkanWindowCall0 call = reinterpret_cast<CuteQVulkanWindowCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QVulkanWindowRenderer *>(given);
    }
    return QVulkanWindow::createRenderer();
  }
#endif

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQVulkanWindowCall1 call = reinterpret_cast<CuteQVulkanWindowCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QVulkanWindow::exposeEvent(a0);
  }
#endif

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindow::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQVulkanWindowCall2 call = reinterpret_cast<CuteQVulkanWindowCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QVulkanWindow::resizeEvent(a0);
  }
#endif

#if !defined(QT_NO_QOBJECT)
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  bool QVulkanWindow::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQVulkanWindowCall3 call = reinterpret_cast<CuteQVulkanWindowCall3>(taken[3]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QVulkanWindow::event(a0);
  }
#endif
#endif  // !defined(QT_NO_QOBJECT)

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQVulkanWindowCall4 call = reinterpret_cast<CuteQVulkanWindowCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQVulkanWindowCall5 call = reinterpret_cast<CuteQVulkanWindowCall5>(taken[5]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQVulkanWindowCall6 call = reinterpret_cast<CuteQVulkanWindowCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQVulkanWindowCall7 call = reinterpret_cast<CuteQVulkanWindowCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQVulkanWindowCall8 call = reinterpret_cast<CuteQVulkanWindowCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQVulkanWindowCall9 call = reinterpret_cast<CuteQVulkanWindowCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQVulkanWindowCall10 call = reinterpret_cast<CuteQVulkanWindowCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQVulkanWindowCall11 call = reinterpret_cast<CuteQVulkanWindowCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQVulkanWindowCall12 call = reinterpret_cast<CuteQVulkanWindowCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQVulkanWindowCall13 call = reinterpret_cast<CuteQVulkanWindowCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQVulkanWindowCall14 call = reinterpret_cast<CuteQVulkanWindowCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQVulkanWindowCall15 call = reinterpret_cast<CuteQVulkanWindowCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQVulkanWindowCall16 call = reinterpret_cast<CuteQVulkanWindowCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQVulkanWindowCall17 call = reinterpret_cast<CuteQVulkanWindowCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

  //  void QWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQVulkanWindowCall18 call = reinterpret_cast<CuteQVulkanWindowCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mousePressEvent(a0);
  }

  //  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQVulkanWindowCall19 call = reinterpret_cast<CuteQVulkanWindowCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseReleaseEvent(a0);
  }

  //  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQVulkanWindowCall20 call = reinterpret_cast<CuteQVulkanWindowCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseDoubleClickEvent(a0);
  }

  //  void QWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQVulkanWindowCall21 call = reinterpret_cast<CuteQVulkanWindowCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseMoveEvent(a0);
  }

#if QT_CONFIG(wheelevent)
  //  void QWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQVulkanWindowCall22 call = reinterpret_cast<CuteQVulkanWindowCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQVulkanWindowCall23 call = reinterpret_cast<CuteQVulkanWindowCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

#if QT_CONFIG(tabletevent)
  //  void QWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQVulkanWindowCall24 call = reinterpret_cast<CuteQVulkanWindowCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQVulkanWindowCall25 call = reinterpret_cast<CuteQVulkanWindowCall25>(taken[25]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurface *>(given);
    }
    return QWindow::surfaceHandle();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQVulkanWindowCall26 call = reinterpret_cast<CuteQVulkanWindowCall26>(taken[26]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQVulkanWindowCall27 call = reinterpret_cast<CuteQVulkanWindowCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQVulkanWindowCall28 call = reinterpret_cast<CuteQVulkanWindowCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQVulkanWindowCall29 call = reinterpret_cast<CuteQVulkanWindowCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[30]) {
      int handled = 0;
      CuteQVulkanWindowCall30 call = reinterpret_cast<CuteQVulkanWindowCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQVulkanWindowCall31 call = reinterpret_cast<CuteQVulkanWindowCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVulkanWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QVulkanWindow10metaObjectEv(
    const QVulkanWindow *self) {
  return self->metaObject();
}

//  void *QVulkanWindow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QVulkanWindow11qt_metacastEPKc(
    QVulkanWindow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QVulkanWindow::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QVulkanWindow11qt_metacallEN11QMetaObject4CallEiPPv(
    QVulkanWindow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QVulkanWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QVulkanWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVulkanWindow::tr(s, c, n));
}

//  QVulkanWindowPrivate *QVulkanWindow::d_func()
extern "C" Q_DECL_EXPORT
QVulkanWindowPrivate *ritual_ZN13QVulkanWindow6d_funcEv(
    QVulkanWindow *self) {
  return self->d_func();
}

//  const QVulkanWindowPrivate *QVulkanWindow::d_func() const
extern "C" Q_DECL_EXPORT
const QVulkanWindowPrivate *ritual_ZNK13QVulkanWindow6d_funcEv(
    const QVulkanWindow *self) {
  return self->d_func();
}

//  QVulkanWindow::QVulkanWindow(QWindow *parent)
extern "C" Q_DECL_EXPORT
QVulkanWindow *ritual_ZN13QVulkanWindowC1EP7QWindow(QWindow *parent) {
  return new CuteQVulkanWindow(parent);
}

//  QVulkanWindow::~QVulkanWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindowD1Ev(QVulkanWindow *self) {
  delete self;
}

//  void QVulkanWindow::setFlags(Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow8setFlagsE6QFlagsINS_4FlagEE(
    QVulkanWindow *self,
    int flags) {
  self->setFlags(QFlags<QVulkanWindow::Flag>::fromInt(flags));
}

//  Flags QVulkanWindow::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QVulkanWindow5flagsEv(const QVulkanWindow *self) {
  return static_cast<int>(self->flags().toInt());
}

//  QList<VkPhysicalDeviceProperties>
//      QVulkanWindow::availablePhysicalDevices()
extern "C" Q_DECL_EXPORT
QList<VkPhysicalDeviceProperties> *ritual_ZN13QVulkanWindow24availablePhysicalDevicesEv(
    QVulkanWindow *self) {
  return new QList<VkPhysicalDeviceProperties>(
      self->availablePhysicalDevices());
}

//  void QVulkanWindow::setPhysicalDeviceIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow22setPhysicalDeviceIndexEi(
    QVulkanWindow *self,
    int idx) {
  self->setPhysicalDeviceIndex(idx);
}

//  QVulkanInfoVector<QVulkanExtension>
//      QVulkanWindow::supportedDeviceExtensions()
extern "C" Q_DECL_EXPORT
QVulkanInfoVector<QVulkanExtension> *ritual_ZN13QVulkanWindow25supportedDeviceExtensionsEv(
    QVulkanWindow *self) {
  return new QVulkanInfoVector<QVulkanExtension>(
      self->supportedDeviceExtensions());
}

//  void QVulkanWindow::setDeviceExtensions(const QByteArrayList &extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow19setDeviceExtensionsERK5QListI10QByteArrayE(
    QVulkanWindow *self,
    const QList<QByteArray> *extensions) {
  self->setDeviceExtensions(*extensions);
}

//  void QVulkanWindow::setEnabledFeaturesModifier(const
//      EnabledFeaturesModifier &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow26setEnabledFeaturesModifierERKSt8functionIFvR24VkPhysicalDeviceFeaturesEE(
    QVulkanWindow *self,
    const QVulkanWindow::EnabledFeaturesModifier *modifier) {
  self->setEnabledFeaturesModifier(*modifier);
}

//  void QVulkanWindow::setEnabledFeaturesModifier(EnabledFeatures2Modifier
//      modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow26setEnabledFeaturesModifierESt8functionIFvR25VkPhysicalDeviceFeatures2EE(
    QVulkanWindow *self,
    const QVulkanWindow::EnabledFeatures2Modifier *modifier) {
  self->setEnabledFeaturesModifier(*modifier);
}

//  void QVulkanWindow::setPreferredColorFormats(const QList<VkFormat>
//      &formats)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow24setPreferredColorFormatsERK5QListI8VkFormatE(
    QVulkanWindow *self,
    const QList<VkFormat> *formats) {
  self->setPreferredColorFormats(*formats);
}

//  QList<int> QVulkanWindow::supportedSampleCounts()
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZN13QVulkanWindow21supportedSampleCountsEv(
    QVulkanWindow *self) {
  return new QList<int>(self->supportedSampleCounts());
}

//  void QVulkanWindow::setSampleCount(int sampleCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow14setSampleCountEi(
    QVulkanWindow *self,
    int sampleCount) {
  self->setSampleCount(sampleCount);
}

//  void QVulkanWindow::setQueueCreateInfoModifier(const
//      QueueCreateInfoModifier &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow26setQueueCreateInfoModifierERKSt8functionIFvPK23VkQueueFamilyPropertiesjR5QListI23VkDeviceQueueCreateInfoEEE(
    QVulkanWindow *self,
    const QVulkanWindow::QueueCreateInfoModifier *modifier) {
  self->setQueueCreateInfoModifier(*modifier);
}

//  bool QVulkanWindow::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QVulkanWindow7isValidEv(const QVulkanWindow *self) {
  return self->isValid();
}

//  QVulkanWindowRenderer *QVulkanWindow::createRenderer()
extern "C" Q_DECL_EXPORT
QVulkanWindowRenderer *ritual_ZN13QVulkanWindow14createRendererEv(
    QVulkanWindow *self) {
  return self->createRenderer();
}

//  void QVulkanWindow::frameReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow10frameReadyEv(QVulkanWindow *self) {
  self->frameReady();
}

//  VkPhysicalDevice QVulkanWindow::physicalDevice() const
extern "C" Q_DECL_EXPORT
VkPhysicalDevice *ritual_ZNK13QVulkanWindow14physicalDeviceEv(
    const QVulkanWindow *self) {
  return new VkPhysicalDevice(self->physicalDevice());
}

//  const VkPhysicalDeviceProperties
//      *QVulkanWindow::physicalDeviceProperties() const
extern "C" Q_DECL_EXPORT
const VkPhysicalDeviceProperties *ritual_ZNK13QVulkanWindow24physicalDevicePropertiesEv(
    const QVulkanWindow *self) {
  return self->physicalDeviceProperties();
}

//  VkDevice QVulkanWindow::device() const
extern "C" Q_DECL_EXPORT
VkDevice *ritual_ZNK13QVulkanWindow6deviceEv(const QVulkanWindow *self) {
  return new VkDevice(self->device());
}

//  VkQueue QVulkanWindow::graphicsQueue() const
extern "C" Q_DECL_EXPORT
VkQueue *ritual_ZNK13QVulkanWindow13graphicsQueueEv(
    const QVulkanWindow *self) {
  return new VkQueue(self->graphicsQueue());
}

//  uint32_t QVulkanWindow::graphicsQueueFamilyIndex() const
extern "C" Q_DECL_EXPORT
uint32_t ritual_ZNK13QVulkanWindow24graphicsQueueFamilyIndexEv(
    const QVulkanWindow *self) {
  return self->graphicsQueueFamilyIndex();
}

//  VkCommandPool QVulkanWindow::graphicsCommandPool() const
extern "C" Q_DECL_EXPORT
VkCommandPool *ritual_ZNK13QVulkanWindow19graphicsCommandPoolEv(
    const QVulkanWindow *self) {
  return new VkCommandPool(self->graphicsCommandPool());
}

//  uint32_t QVulkanWindow::hostVisibleMemoryIndex() const
extern "C" Q_DECL_EXPORT
uint32_t ritual_ZNK13QVulkanWindow22hostVisibleMemoryIndexEv(
    const QVulkanWindow *self) {
  return self->hostVisibleMemoryIndex();
}

//  uint32_t QVulkanWindow::deviceLocalMemoryIndex() const
extern "C" Q_DECL_EXPORT
uint32_t ritual_ZNK13QVulkanWindow22deviceLocalMemoryIndexEv(
    const QVulkanWindow *self) {
  return self->deviceLocalMemoryIndex();
}

//  VkRenderPass QVulkanWindow::defaultRenderPass() const
extern "C" Q_DECL_EXPORT
VkRenderPass *ritual_ZNK13QVulkanWindow17defaultRenderPassEv(
    const QVulkanWindow *self) {
  return new VkRenderPass(self->defaultRenderPass());
}

//  VkFormat QVulkanWindow::colorFormat() const
extern "C" Q_DECL_EXPORT
VkFormat *ritual_ZNK13QVulkanWindow11colorFormatEv(
    const QVulkanWindow *self) {
  return new VkFormat(self->colorFormat());
}

//  VkFormat QVulkanWindow::depthStencilFormat() const
extern "C" Q_DECL_EXPORT
VkFormat *ritual_ZNK13QVulkanWindow18depthStencilFormatEv(
    const QVulkanWindow *self) {
  return new VkFormat(self->depthStencilFormat());
}

//  QSize QVulkanWindow::swapChainImageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QVulkanWindow18swapChainImageSizeEv(
    const QVulkanWindow *self) {
  return new QSize(self->swapChainImageSize());
}

//  VkCommandBuffer QVulkanWindow::currentCommandBuffer() const
extern "C" Q_DECL_EXPORT
VkCommandBuffer *ritual_ZNK13QVulkanWindow20currentCommandBufferEv(
    const QVulkanWindow *self) {
  return new VkCommandBuffer(self->currentCommandBuffer());
}

//  VkFramebuffer QVulkanWindow::currentFramebuffer() const
extern "C" Q_DECL_EXPORT
VkFramebuffer *ritual_ZNK13QVulkanWindow18currentFramebufferEv(
    const QVulkanWindow *self) {
  return new VkFramebuffer(self->currentFramebuffer());
}

//  int QVulkanWindow::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QVulkanWindow12currentFrameEv(const QVulkanWindow *self) {
  return self->currentFrame();
}

//  int QVulkanWindow::concurrentFrameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QVulkanWindow20concurrentFrameCountEv(
    const QVulkanWindow *self) {
  return self->concurrentFrameCount();
}

//  int QVulkanWindow::swapChainImageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QVulkanWindow19swapChainImageCountEv(
    const QVulkanWindow *self) {
  return self->swapChainImageCount();
}

//  int QVulkanWindow::currentSwapChainImageIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QVulkanWindow26currentSwapChainImageIndexEv(
    const QVulkanWindow *self) {
  return self->currentSwapChainImageIndex();
}

//  VkImage QVulkanWindow::swapChainImage(int idx) const
extern "C" Q_DECL_EXPORT
VkImage *ritual_ZNK13QVulkanWindow14swapChainImageEi(
    const QVulkanWindow *self,
    int idx) {
  return new VkImage(self->swapChainImage(idx));
}

//  VkImageView QVulkanWindow::swapChainImageView(int idx) const
extern "C" Q_DECL_EXPORT
VkImageView *ritual_ZNK13QVulkanWindow18swapChainImageViewEi(
    const QVulkanWindow *self,
    int idx) {
  return new VkImageView(self->swapChainImageView(idx));
}

//  VkImage QVulkanWindow::depthStencilImage() const
extern "C" Q_DECL_EXPORT
VkImage *ritual_ZNK13QVulkanWindow17depthStencilImageEv(
    const QVulkanWindow *self) {
  return new VkImage(self->depthStencilImage());
}

//  VkImageView QVulkanWindow::depthStencilImageView() const
extern "C" Q_DECL_EXPORT
VkImageView *ritual_ZNK13QVulkanWindow21depthStencilImageViewEv(
    const QVulkanWindow *self) {
  return new VkImageView(self->depthStencilImageView());
}

//  VkSampleCountFlagBits QVulkanWindow::sampleCountFlagBits() const
extern "C" Q_DECL_EXPORT
VkSampleCountFlagBits *ritual_ZNK13QVulkanWindow19sampleCountFlagBitsEv(
    const QVulkanWindow *self) {
  return new VkSampleCountFlagBits(self->sampleCountFlagBits());
}

//  VkImage QVulkanWindow::msaaColorImage(int idx) const
extern "C" Q_DECL_EXPORT
VkImage *ritual_ZNK13QVulkanWindow14msaaColorImageEi(
    const QVulkanWindow *self,
    int idx) {
  return new VkImage(self->msaaColorImage(idx));
}

//  VkImageView QVulkanWindow::msaaColorImageView(int idx) const
extern "C" Q_DECL_EXPORT
VkImageView *ritual_ZNK13QVulkanWindow18msaaColorImageViewEi(
    const QVulkanWindow *self,
    int idx) {
  return new VkImageView(self->msaaColorImageView(idx));
}

//  bool QVulkanWindow::supportsGrab() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QVulkanWindow12supportsGrabEv(const QVulkanWindow *self) {
  return self->supportsGrab();
}

//  QImage QVulkanWindow::grab()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QVulkanWindow4grabEv(QVulkanWindow *self) {
  return new QImage(self->grab());
}

//  QMatrix4x4 QVulkanWindow::clipCorrectionMatrix()
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN13QVulkanWindow20clipCorrectionMatrixEv(
    QVulkanWindow *self) {
  return new QMatrix4x4(self->clipCorrectionMatrix());
}

//  void QVulkanWindow::frameGrabbed(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow12frameGrabbedERK6QImage(
    QVulkanWindow *self,
    const QImage *image) {
  self->frameGrabbed(*image);
}

//  void QVulkanWindow::exposeEvent(QExposeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow11exposeEventEP12QExposeEvent(
    QVulkanWindow *self,
    QExposeEvent *a0) {
  self->exposeEvent(a0);
}

//  void QVulkanWindow::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QVulkanWindow11resizeEventEP12QResizeEvent(
    QVulkanWindow *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  bool QVulkanWindow::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QVulkanWindow5eventEP6QEvent(
    QVulkanWindow *self,
    QEvent *a0) {
  return self->event(a0);
}

//  a Python function taken by a CuteQVulkanWindow, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVulkanWindow(
    QVulkanWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVulkanWindow *>(self)->take(key, call);
}

//  QVulkanWindowRenderer *QVulkanWindow::createRenderer()
extern "C" Q_DECL_EXPORT
QVulkanWindowRenderer *ritual_own_ZN13QVulkanWindow14createRendererEv(
    QVulkanWindow *self) {
  return self->QVulkanWindow::createRenderer();
}

//  void QVulkanWindow::exposeEvent(QExposeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QVulkanWindow11exposeEventEP12QExposeEvent(
    QVulkanWindow *self,
    QExposeEvent *a0) {
  static_cast<OwnQVulkanWindow *>(self)->OwnQVulkanWindow::exposeEvent(a0);
}

//  void QVulkanWindow::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QVulkanWindow11resizeEventEP12QResizeEvent(
    QVulkanWindow *self,
    QResizeEvent *a0) {
  static_cast<OwnQVulkanWindow *>(self)->OwnQVulkanWindow::resizeEvent(a0);
}

//  bool QVulkanWindow::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QVulkanWindow5eventEP6QEvent(
    QVulkanWindow *self,
    QEvent *a0) {
  return static_cast<OwnQVulkanWindow *>(self)->OwnQVulkanWindow::event(a0);
}

//  a QList<VkPhysicalDeviceProperties> a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__QList_VkPhysicalDeviceProperties(
    QList<VkPhysicalDeviceProperties> *self) {
  delete self;
}

//  a QVulkanInfoVector<QVulkanExtension> a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__QVulkanInfoVector_QVulkanExtension(
    QVulkanInfoVector<QVulkanExtension> *self) {
  delete self;
}

//  a QList<int> a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__QList_int(QList<int> *self) {
  delete self;
}

//  a VkPhysicalDevice a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkPhysicalDevice(VkPhysicalDevice *self) {
  delete self;
}

//  a VkDevice a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkDevice(VkDevice *self) {
  delete self;
}

//  a VkQueue a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkQueue(VkQueue *self) {
  delete self;
}

//  a VkCommandPool a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkCommandPool(VkCommandPool *self) {
  delete self;
}

//  a VkRenderPass a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkRenderPass(VkRenderPass *self) {
  delete self;
}

//  a VkFormat a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkFormat(VkFormat *self) {
  delete self;
}

//  a VkCommandBuffer a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkCommandBuffer(VkCommandBuffer *self) {
  delete self;
}

//  a VkFramebuffer a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkFramebuffer(VkFramebuffer *self) {
  delete self;
}

//  a VkImage a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkImage(VkImage *self) {
  delete self;
}

//  a VkImageView a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkImageView(VkImageView *self) {
  delete self;
}

//  a VkSampleCountFlagBits a ritual of QVulkanWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVulkanWindow__VkSampleCountFlagBits(
    VkSampleCountFlagBits *self) {
  delete self;
}

#endif  // (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan)
