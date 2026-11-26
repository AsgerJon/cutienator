//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickWidgets/qquickwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickWidgets/qquickwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qanystringview.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlerror.h>
#include <QtCore/qsize.h>
#include <QtGui/qsurfaceformat.h>
#include <QtGui/qimage.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QQuickWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWidget : QQuickWidget {
  using QQuickWidget::resizeEvent;
  using QQuickWidget::timerEvent;
  using QQuickWidget::keyPressEvent;
  using QQuickWidget::keyReleaseEvent;
  using QQuickWidget::mousePressEvent;
  using QQuickWidget::mouseReleaseEvent;
  using QQuickWidget::mouseMoveEvent;
  using QQuickWidget::mouseDoubleClickEvent;
  using QQuickWidget::showEvent;
  using QQuickWidget::hideEvent;
  using QQuickWidget::focusInEvent;
  using QQuickWidget::focusOutEvent;
  using QQuickWidget::wheelEvent;
  using QQuickWidget::dragEnterEvent;
  using QQuickWidget::dragMoveEvent;
  using QQuickWidget::dragLeaveEvent;
  using QQuickWidget::dropEvent;
  using QQuickWidget::event;
  using QQuickWidget::paintEvent;
  using QQuickWidget::focusNextPrevChild;
};

//  A QQuickWidget that Python can take functions over in. Every QQuickWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQQuickWidgetCall0)(const void *, int *);
typedef void (*CuteQQuickWidgetCall1)(const void *, QResizeEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWidgetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWidgetCall3)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWidgetCall4)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWidgetCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWidgetCall6)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWidgetCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWidgetCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWidgetCall9)(const void *, QShowEvent *, int *);
typedef void (*CuteQQuickWidgetCall10)(const void *, QHideEvent *, int *);
typedef void (*CuteQQuickWidgetCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWidgetCall12)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWidgetCall13)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWidgetCall14)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWidgetCall15)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWidgetCall16)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWidgetCall17)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWidgetCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWidgetCall19)(const void *, QPaintEvent *, int *);
typedef bool (*CuteQQuickWidgetCall20)(const void *, bool, int *);
typedef int (*CuteQQuickWidgetCall21)(const void *, int *);
typedef void (*CuteQQuickWidgetCall22)(const void *, bool, int *);
typedef const QSize * (*CuteQQuickWidgetCall23)(const void *, int *);
typedef int (*CuteQQuickWidgetCall24)(const void *, int, int *);
typedef bool (*CuteQQuickWidgetCall25)(const void *, int *);
typedef void * (*CuteQQuickWidgetCall26)(const void *, int *);
typedef void (*CuteQQuickWidgetCall27)(const void *, QEnterEvent *, int *);
typedef void (*CuteQQuickWidgetCall28)(const void *, QEvent *, int *);
typedef void (*CuteQQuickWidgetCall29)(const void *, QMoveEvent *, int *);
typedef void (*CuteQQuickWidgetCall30)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQQuickWidgetCall31)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQQuickWidgetCall32)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQQuickWidgetCall33)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQQuickWidgetCall34)(const void *, QEvent *, int *);
typedef int (*CuteQQuickWidgetCall35)(const void *, int, int *);
typedef void (*CuteQQuickWidgetCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQQuickWidgetCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQQuickWidgetCall38)(const void *, int *);
typedef void (*CuteQQuickWidgetCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQQuickWidgetCall40)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWidgetCall41)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWidgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWidgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWidgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWidget : public QQuickWidget {
public:
  using QQuickWidget::QQuickWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[30] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[40] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSize QQuickWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWidgetCall0 call = reinterpret_cast<CuteQQuickWidgetCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickWidget::sizeHint();
  }

  //  void QQuickWidget::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWidgetCall1 call = reinterpret_cast<CuteQQuickWidgetCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::resizeEvent(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickWidget::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWidgetCall2 call = reinterpret_cast<CuteQQuickWidgetCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickWidget::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWidgetCall3 call = reinterpret_cast<CuteQQuickWidgetCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::keyPressEvent(a0);
  }

  //  void QQuickWidget::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWidgetCall4 call = reinterpret_cast<CuteQQuickWidgetCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::keyReleaseEvent(a0);
  }

  //  void QQuickWidget::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWidgetCall5 call = reinterpret_cast<CuteQQuickWidgetCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::mousePressEvent(a0);
  }

  //  void QQuickWidget::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWidgetCall6 call = reinterpret_cast<CuteQQuickWidgetCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::mouseReleaseEvent(a0);
  }

  //  void QQuickWidget::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWidgetCall7 call = reinterpret_cast<CuteQQuickWidgetCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::mouseMoveEvent(a0);
  }

  //  void QQuickWidget::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWidgetCall8 call = reinterpret_cast<CuteQQuickWidgetCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::mouseDoubleClickEvent(a0);
  }

  //  void QQuickWidget::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWidgetCall9 call = reinterpret_cast<CuteQQuickWidgetCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::showEvent(a0);
  }

  //  void QQuickWidget::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWidgetCall10 call = reinterpret_cast<CuteQQuickWidgetCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::hideEvent(a0);
  }

  //  void QQuickWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickWidgetCall11 call = reinterpret_cast<CuteQQuickWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickWidget::focusInEvent(event);
  }

  //  void QQuickWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickWidgetCall12 call = reinterpret_cast<CuteQQuickWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickWidget::focusOutEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickWidget::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickWidgetCall13 call = reinterpret_cast<CuteQQuickWidgetCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
  //  void QQuickWidget::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickWidgetCall14 call = reinterpret_cast<CuteQQuickWidgetCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
  //  void QQuickWidget::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickWidgetCall15 call = reinterpret_cast<CuteQQuickWidgetCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
  //  void QQuickWidget::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickWidgetCall16 call = reinterpret_cast<CuteQQuickWidgetCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(quick_draganddrop)
  //  void QQuickWidget::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickWidgetCall17 call = reinterpret_cast<CuteQQuickWidgetCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickWidget::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(draganddrop)

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickWidget::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickWidgetCall18 call = reinterpret_cast<CuteQQuickWidgetCall18>(taken[18]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickWidget::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickWidgetCall19 call = reinterpret_cast<CuteQQuickWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickWidget::paintEvent(event);
  }

  //  bool QQuickWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickWidgetCall20 call = reinterpret_cast<CuteQQuickWidgetCall20>(taken[20]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QQuickWidget::focusNextPrevChild(next);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickWidgetCall21 call = reinterpret_cast<CuteQQuickWidgetCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickWidgetCall22 call = reinterpret_cast<CuteQQuickWidgetCall22>(taken[22]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickWidgetCall23 call = reinterpret_cast<CuteQQuickWidgetCall23>(taken[23]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickWidgetCall24 call = reinterpret_cast<CuteQQuickWidgetCall24>(taken[24]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickWidgetCall25 call = reinterpret_cast<CuteQQuickWidgetCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickWidgetCall26 call = reinterpret_cast<CuteQQuickWidgetCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickWidgetCall27 call = reinterpret_cast<CuteQQuickWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickWidgetCall28 call = reinterpret_cast<CuteQQuickWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickWidgetCall29 call = reinterpret_cast<CuteQQuickWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickWidgetCall30 call = reinterpret_cast<CuteQQuickWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickWidgetCall31 call = reinterpret_cast<CuteQQuickWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickWidgetCall32 call = reinterpret_cast<CuteQQuickWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickWidgetCall33 call = reinterpret_cast<CuteQQuickWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickWidgetCall34 call = reinterpret_cast<CuteQQuickWidgetCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickWidgetCall35 call = reinterpret_cast<CuteQQuickWidgetCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickWidgetCall36 call = reinterpret_cast<CuteQQuickWidgetCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickWidgetCall37 call = reinterpret_cast<CuteQQuickWidgetCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickWidgetCall38 call = reinterpret_cast<CuteQQuickWidgetCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickWidgetCall39 call = reinterpret_cast<CuteQQuickWidgetCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickWidgetCall40 call = reinterpret_cast<CuteQQuickWidgetCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickWidgetCall41 call = reinterpret_cast<CuteQQuickWidgetCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickWidgetCall42 call = reinterpret_cast<CuteQQuickWidgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickWidgetCall43 call = reinterpret_cast<CuteQQuickWidgetCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickWidgetCall44 call = reinterpret_cast<CuteQQuickWidgetCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickWidgetCall45 call = reinterpret_cast<CuteQQuickWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickWidget10metaObjectEv(
    const QQuickWidget *self) {
  return self->metaObject();
}

//  void *QQuickWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQuickWidget11qt_metacastEPKc(
    QQuickWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWidget::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQuickWidget11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWidget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWidget::tr(s, c, n));
}

//  QQuickWidget::QQuickWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QQuickWidget *ritual_ZN12QQuickWidgetC1EP7QWidget(QWidget *parent) {
  return new CuteQQuickWidget(parent);
}

//  QQuickWidget::QQuickWidget(QQmlEngine *engine, QWidget *parent)
extern "C" Q_DECL_EXPORT
QQuickWidget *ritual_ZN12QQuickWidgetC1EP10QQmlEngineP7QWidget(
    QQmlEngine *engine,
    QWidget *parent) {
  return new CuteQQuickWidget(engine, parent);
}

//  QQuickWidget::QQuickWidget(const QUrl &source, QWidget *parent)
extern "C" Q_DECL_EXPORT
QQuickWidget *ritual_ZN12QQuickWidgetC1ERK4QUrlP7QWidget(
    const QUrl *source,
    QWidget *parent) {
  return new CuteQQuickWidget(*source, parent);
}

//  QQuickWidget::QQuickWidget(QAnyStringView uri, QAnyStringView typeName,
//      QWidget *parent)
extern "C" Q_DECL_EXPORT
QQuickWidget *ritual_ZN12QQuickWidgetC1E14QAnyStringViewS0_P7QWidget(
    const QString *uri,
    const QString *typeName,
    QWidget *parent) {
  return new CuteQQuickWidget(
      QAnyStringView(*uri),
      QAnyStringView(*typeName),
      parent);
}

//  QQuickWidget::~QQuickWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidgetD1Ev(QQuickWidget *self) {
  delete self;
}

//  QUrl QQuickWidget::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QQuickWidget6sourceEv(const QQuickWidget *self) {
  return new QUrl(self->source());
}

//  QQmlEngine *QQuickWidget::engine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK12QQuickWidget6engineEv(const QQuickWidget *self) {
  return self->engine();
}

//  QQmlContext *QQuickWidget::rootContext() const
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZNK12QQuickWidget11rootContextEv(
    const QQuickWidget *self) {
  return self->rootContext();
}

//  QQuickItem *QQuickWidget::rootObject() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK12QQuickWidget10rootObjectEv(
    const QQuickWidget *self) {
  return self->rootObject();
}

//  ResizeMode QQuickWidget::resizeMode() const
extern "C" Q_DECL_EXPORT
QQuickWidget::ResizeMode ritual_ZNK12QQuickWidget10resizeModeEv(
    const QQuickWidget *self) {
  return self->resizeMode();
}

//  void QQuickWidget::setResizeMode(ResizeMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget13setResizeModeENS_10ResizeModeE(
    QQuickWidget *self,
    QQuickWidget::ResizeMode a0) {
  self->setResizeMode(a0);
}

//  Status QQuickWidget::status() const
extern "C" Q_DECL_EXPORT
QQuickWidget::Status ritual_ZNK12QQuickWidget6statusEv(
    const QQuickWidget *self) {
  return self->status();
}

//  QList<QQmlError> QQuickWidget::errors() const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK12QQuickWidget6errorsEv(
    const QQuickWidget *self) {
  return new QList<QQmlError>(self->errors());
}

//  QSize QQuickWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QQuickWidget8sizeHintEv(const QQuickWidget *self) {
  return new QSize(self->sizeHint());
}

//  QSize QQuickWidget::initialSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QQuickWidget11initialSizeEv(const QQuickWidget *self) {
  return new QSize(self->initialSize());
}

//  void QQuickWidget::setFormat(const QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget9setFormatERK14QSurfaceFormat(
    QQuickWidget *self,
    const QSurfaceFormat *format) {
  self->setFormat(*format);
}

//  QSurfaceFormat QQuickWidget::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK12QQuickWidget6formatEv(const QQuickWidget *self) {
  return new QSurfaceFormat(self->format());
}

//  QImage QQuickWidget::grabFramebuffer() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK12QQuickWidget15grabFramebufferEv(
    const QQuickWidget *self) {
  return new QImage(self->grabFramebuffer());
}

//  void QQuickWidget::setClearColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget13setClearColorERK6QColor(
    QQuickWidget *self,
    const QColor *color) {
  self->setClearColor(*color);
}

//  QQuickWindow *QQuickWidget::quickWindow() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZNK12QQuickWidget11quickWindowEv(
    const QQuickWidget *self) {
  return self->quickWindow();
}

//  void QQuickWidget::setSource(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget9setSourceERK4QUrl(
    QQuickWidget *self,
    const QUrl *a0) {
  self->setSource(*a0);
}

//  void QQuickWidget::setContent(const QUrl &url, QQmlComponent *component,
//      QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget10setContentERK4QUrlP13QQmlComponentP7QObject(
    QQuickWidget *self,
    const QUrl *url,
    QQmlComponent *component,
    QObject *item) {
  self->setContent(*url, component, item);
}

//  void QQuickWidget::setInitialProperties(const QVariantMap
//      &initialProperties)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget20setInitialPropertiesERK4QMapI7QString8QVariantE(
    QQuickWidget *self,
    const QMap<QString, QVariant> *initialProperties) {
  self->setInitialProperties(*initialProperties);
}

//  void QQuickWidget::loadFromModule(QAnyStringView uri, QAnyStringView
//      typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget14loadFromModuleE14QAnyStringViewS0_(
    QQuickWidget *self,
    const QString *uri,
    const QString *typeName) {
  self->loadFromModule(QAnyStringView(*uri), QAnyStringView(*typeName));
}

//  void QQuickWidget::statusChanged(QQuickWidget::Status a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget13statusChangedENS_6StatusE(
    QQuickWidget *self,
    QQuickWidget::Status a0) {
  self->statusChanged(a0);
}

//  void QQuickWidget::sceneGraphError(QQuickWindow::SceneGraphError error,
//      const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget15sceneGraphErrorEN12QQuickWindow15SceneGraphErrorERK7QString(
    QQuickWidget *self,
    QQuickWindow::SceneGraphError error,
    const QString *message) {
  self->sceneGraphError(error, *message);
}

//  void QQuickWidget::continueExecute()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget15continueExecuteEv(QQuickWidget *self) {
  self->continueExecute();
}

//  void QQuickWidget::createFramebufferObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget23createFramebufferObjectEv(QQuickWidget *self) {
  self->createFramebufferObject();
}

//  void QQuickWidget::destroyFramebufferObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget24destroyFramebufferObjectEv(
    QQuickWidget *self) {
  self->destroyFramebufferObject();
}

//  void QQuickWidget::triggerUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget13triggerUpdateEv(QQuickWidget *self) {
  self->triggerUpdate();
}

//  void QQuickWidget::propagateFocusObjectChanged(QObject *focusObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget27propagateFocusObjectChangedEP7QObject(
    QQuickWidget *self,
    QObject *focusObject) {
  self->propagateFocusObjectChanged(focusObject);
}

//  void QQuickWidget::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget11resizeEventEP12QResizeEvent(
    QQuickWidget *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QQuickWidget::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget10timerEventEP11QTimerEvent(
    QQuickWidget *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  void QQuickWidget::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget13keyPressEventEP9QKeyEvent(
    QQuickWidget *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QQuickWidget::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget15keyReleaseEventEP9QKeyEvent(
    QQuickWidget *self,
    QKeyEvent *a0) {
  self->keyReleaseEvent(a0);
}

//  void QQuickWidget::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget15mousePressEventEP11QMouseEvent(
    QQuickWidget *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QQuickWidget::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget17mouseReleaseEventEP11QMouseEvent(
    QQuickWidget *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QQuickWidget::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget14mouseMoveEventEP11QMouseEvent(
    QQuickWidget *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

//  void QQuickWidget::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget21mouseDoubleClickEventEP11QMouseEvent(
    QQuickWidget *self,
    QMouseEvent *a0) {
  self->mouseDoubleClickEvent(a0);
}

//  void QQuickWidget::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget9showEventEP10QShowEvent(
    QQuickWidget *self,
    QShowEvent *a0) {
  self->showEvent(a0);
}

//  void QQuickWidget::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget9hideEventEP10QHideEvent(
    QQuickWidget *self,
    QHideEvent *a0) {
  self->hideEvent(a0);
}

//  void QQuickWidget::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget12focusInEventEP11QFocusEvent(
    QQuickWidget *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickWidget::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget13focusOutEventEP11QFocusEvent(
    QQuickWidget *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickWidget::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget10wheelEventEP11QWheelEvent(
    QQuickWidget *self,
    QWheelEvent *a0) {
  self->wheelEvent(a0);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickWidget::dragEnterEvent(QDragEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget14dragEnterEventEP15QDragEnterEvent(
    QQuickWidget *self,
    QDragEnterEvent *a0) {
  self->dragEnterEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickWidget::dragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget13dragMoveEventEP14QDragMoveEvent(
    QQuickWidget *self,
    QDragMoveEvent *a0) {
  self->dragMoveEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickWidget::dragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget14dragLeaveEventEP15QDragLeaveEvent(
    QQuickWidget *self,
    QDragLeaveEvent *a0) {
  self->dragLeaveEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickWidget::dropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget9dropEventEP10QDropEvent(
    QQuickWidget *self,
    QDropEvent *a0) {
  self->dropEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  bool QQuickWidget::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickWidget5eventEP6QEvent(QQuickWidget *self, QEvent *a0) {
  return self->event(a0);
}

//  void QQuickWidget::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWidget10paintEventEP11QPaintEvent(
    QQuickWidget *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  bool QQuickWidget::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickWidget18focusNextPrevChildEb(
    QQuickWidget *self,
    bool next) {
  return self->focusNextPrevChild(next);
}

//  QQuickWidgetPrivate *QQuickWidget::d_func()
extern "C" Q_DECL_EXPORT
QQuickWidgetPrivate *ritual_ZN12QQuickWidget6d_funcEv(QQuickWidget *self) {
  return self->d_func();
}

//  const QQuickWidgetPrivate *QQuickWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickWidgetPrivate *ritual_ZNK12QQuickWidget6d_funcEv(
    const QQuickWidget *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWidget(
    QQuickWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWidget *>(self)->take(key, call);
}

//  QSize QQuickWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QQuickWidget8sizeHintEv(const QQuickWidget *self) {
  return new QSize(self->QQuickWidget::sizeHint());
}

//  void QQuickWidget::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget11resizeEventEP12QResizeEvent(
    QQuickWidget *self,
    QResizeEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::resizeEvent(a0);
}

//  void QQuickWidget::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget10timerEventEP11QTimerEvent(
    QQuickWidget *self,
    QTimerEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::timerEvent(a0);
}

//  void QQuickWidget::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget13keyPressEventEP9QKeyEvent(
    QQuickWidget *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::keyPressEvent(a0);
}

//  void QQuickWidget::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget15keyReleaseEventEP9QKeyEvent(
    QQuickWidget *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::keyReleaseEvent(a0);
}

//  void QQuickWidget::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget15mousePressEventEP11QMouseEvent(
    QQuickWidget *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::mousePressEvent(a0);
}

//  void QQuickWidget::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget17mouseReleaseEventEP11QMouseEvent(
    QQuickWidget *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::mouseReleaseEvent(
      a0);
}

//  void QQuickWidget::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget14mouseMoveEventEP11QMouseEvent(
    QQuickWidget *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::mouseMoveEvent(a0);
}

//  void QQuickWidget::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget21mouseDoubleClickEventEP11QMouseEvent(
    QQuickWidget *self,
    QMouseEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::mouseDoubleClickEvent(
      a0);
}

//  void QQuickWidget::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget9showEventEP10QShowEvent(
    QQuickWidget *self,
    QShowEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::showEvent(a0);
}

//  void QQuickWidget::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget9hideEventEP10QHideEvent(
    QQuickWidget *self,
    QHideEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::hideEvent(a0);
}

//  void QQuickWidget::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget12focusInEventEP11QFocusEvent(
    QQuickWidget *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::focusInEvent(event);
}

//  void QQuickWidget::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget13focusOutEventEP11QFocusEvent(
    QQuickWidget *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::focusOutEvent(
      event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickWidget::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget10wheelEventEP11QWheelEvent(
    QQuickWidget *self,
    QWheelEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::wheelEvent(a0);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickWidget::dragEnterEvent(QDragEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget14dragEnterEventEP15QDragEnterEvent(
    QQuickWidget *self,
    QDragEnterEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::dragEnterEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickWidget::dragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget13dragMoveEventEP14QDragMoveEvent(
    QQuickWidget *self,
    QDragMoveEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::dragMoveEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickWidget::dragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget14dragLeaveEventEP15QDragLeaveEvent(
    QQuickWidget *self,
    QDragLeaveEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::dragLeaveEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickWidget::dropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget9dropEventEP10QDropEvent(
    QQuickWidget *self,
    QDropEvent *a0) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::dropEvent(a0);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  bool QQuickWidget::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQuickWidget5eventEP6QEvent(
    QQuickWidget *self,
    QEvent *a0) {
  return static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::event(a0);
}

//  void QQuickWidget::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickWidget10paintEventEP11QPaintEvent(
    QQuickWidget *self,
    QPaintEvent *event) {
  static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::paintEvent(event);
}

//  bool QQuickWidget::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQuickWidget18focusNextPrevChildEb(
    QQuickWidget *self,
    bool next) {
  return static_cast<OwnQQuickWidget *>(self)->OwnQQuickWidget::focusNextPrevChild(
      next);
}
